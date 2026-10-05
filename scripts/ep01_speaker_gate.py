"""Fail-closed evidence gate for SIA-01. Validates evidence, does not hear audio.

No API, generation or media mutation. Passing a schema is not independent proof
that a reviewer listened; truthful reviewer records and owner control remain required.
"""
import argparse
import hashlib
import json
import math
import re
import subprocess
import wave
from pathlib import Path


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(',', ':'), allow_nan=False).encode('utf-8')).hexdigest()


def source_request(package_path, captions, slots, mode='AUDIO_SELECTION', target=None):
    package_path = Path(package_path).resolve()
    package = json.loads(package_path.read_text(encoding='utf-8'))
    script = package_path.parents[2] / package['script_source']
    rows = []
    for line in package['lines']:
        cues = [c for c in captions if c['line_id'] == line['id']]
        slot = next(s for s in slots if line['id'] in s['line_ids'])
        rows.append({
            'line_id': line['id'], 'expected_speaker': line['speaker'],
            'text': line['text'], 'expected_voice': package['voices'][line['speaker']],
            'source': {'path': str(Path(slot['source']).resolve()), 'sha256': slot['source_sha256']},
            'source_range': [round(cues[0]['start'] - slot['timeline_in'], 6),
                             round(cues[-1]['end'] - slot['timeline_in'], 6)],
            'timeline_range': [cues[0]['start'], cues[-1]['end']],
            'timing_basis': 'ASR_HINT_NOT_SAMPLE_ACCURATE',
        })
    return {'schema_version': 1, 'mode': mode,
            'package': {'path': str(package_path), 'sha256': digest(package_path)},
            'script': {'path': str(script.resolve()), 'sha256': digest(script)},
            'script_version': package['script_version'], 'lines': rows, 'target': target}


def evaluate(request, report):
    """Report HOLD for missing/unverified evidence, REWORK for observed mismatch."""
    holds, defects = [], []

    def hold(message):
        holds.append(message)

    def artifact(item, label):
        if not isinstance(item, dict) or not isinstance(item.get('path'), str) or not isinstance(item.get('sha256'), str):
            hold(f'{label}: missing file/hash'); return False
        try:
            if digest(item['path']) != item['sha256']:
                hold(f'{label}: bytes changed'); return False
            if Path(item['path']).stat().st_size == 0:
                hold(f'{label}: empty file'); return False
        except (OSError, ValueError):
            hold(f'{label}: unavailable file'); return False
        return True

    durations = {}
    def audio_artifact(item, label):
        if not artifact(item, label):
            return None
        key = (item['path'], item['sha256'])
        if key in durations:
            return durations[key]
        try:
            path = Path(item['path'])
            if path.suffix.lower() == '.wav':
                with wave.open(str(path), 'rb') as audio:
                    duration = audio.getnframes() / audio.getframerate()
            else:
                probe = Path(__file__).resolve().parents[1] / '.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/ffprobe.exe'
                metadata = json.loads(subprocess.check_output([str(probe), '-v', 'error',
                    '-show_streams', '-show_format', '-of', 'json', str(path)], stderr=subprocess.PIPE))
                if not any(s['codec_type'] == 'audio' for s in metadata['streams']):
                    raise ValueError('No audio stream')
                duration = float(metadata['format']['duration'])
            if not math.isfinite(duration) or duration <= 0:
                raise ValueError('Empty audio')
        except (OSError, ValueError, KeyError, EOFError, wave.Error, subprocess.SubprocessError):
            hold(label + ': unreadable/no audio'); return None
        durations[key] = duration
        return duration

    if not isinstance(request, dict) or type(request.get('schema_version')) is not int or request.get('schema_version') != 1:
        return {'status': 'HOLD_FOR_INPUT', 'holds': ['Invalid request schema'], 'defects': []}
    mode = request.get('mode')
    if mode not in ('AUDIO_SELECTION', 'AV_ASSEMBLY', 'FINAL_AV'):
        hold('Unknown review scope')
    package_ok = artifact(request.get('package'), 'Package')
    script_ok = artifact(request.get('script'), 'Script')
    package = {}
    if package_ok:
        try:
            package = json.loads(Path(request['package']['path']).read_text(encoding='utf-8'))
            if (not isinstance(package, dict) or not isinstance(package.get('lines'), list)
                or not all(isinstance(r, dict) for r in package['lines'])
                or not isinstance(package.get('voices'), dict)
                or not all(isinstance(v, dict) for v in package['voices'].values())):
                package = {}; hold('Invalid package shape')
        except (ValueError, OSError):
            hold('Unreadable package')
    if package.get('text_status') != 'OWNER_APPROVED' or package.get('script_version') != request.get('script_version'):
        hold('Unapproved or changed script package')
    if script_ok and package:
        try:
            approved = re.findall(r'\*\*(N\d{2}) — (Đào|Khoai):\*\* “([^”]+)”',
                                  Path(request['script']['path']).read_text(encoding='utf-8'))
            actual = [(r['id'], r['speaker'], r['text']) for r in package['lines']]
            if approved != actual:
                hold('Package does not match approved script text/roles')
        except (KeyError, TypeError, OSError):
            hold('Invalid script/role mapping')
    rows = request.get('lines', [])
    if not isinstance(rows, list):
        rows = []; hold('Invalid requested lines')
    expected = package.get('lines', [])
    if [r.get('line_id') for r in rows if isinstance(r, dict)] != [r.get('id') for r in expected] or not rows:
        hold('Missing, duplicated or reordered requested lines')
    for row, line in zip(rows, expected):
        if not isinstance(row, dict) or not isinstance(line, dict):
            hold('Invalid line'); continue
        voice = package.get('voices', {}).get(line.get('speaker'))
        if (row.get('expected_speaker'), row.get('text'), row.get('expected_voice')) != (line.get('speaker'), line.get('text'), voice):
            hold('Expected role/text/voice altered')
        duration = audio_artifact(row.get('source'), str(row.get('line_id')) + ' source')
        for key in ('source_range', 'timeline_range'):
            value = row.get(key)
            if (not isinstance(value, list) or len(value) != 2
                or any(type(n) not in (int, float) or not math.isfinite(n) for n in value)
                or value[0] < 0 or value[1] <= value[0]):
                hold(str(row.get('line_id')) + ': invalid ' + key)
            elif key == 'source_range' and duration is not None and value[1] > duration + 0.001:
                hold(str(row.get('line_id')) + ': source interval exceeds audio')
        if row.get('timing_basis') != 'ASR_HINT_NOT_SAMPLE_ACCURATE':
            hold('Unexpected source timing basis; rebind reviewed intervals')
    if mode != 'AUDIO_SELECTION' and artifact(request.get('target'), 'Current AV cut'):
        try:
            probe = Path(__file__).resolve().parents[1] / '.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/ffprobe.exe'
            metadata = json.loads(subprocess.check_output([str(probe), '-v', 'error',
                '-show_streams', '-show_format', '-of', 'json', request['target']['path']], stderr=subprocess.PIPE))
            types = {s['codec_type'] for s in metadata['streams']}
            duration = float(metadata['format']['duration'])
            if not {'audio', 'video'}.issubset(types) or not math.isfinite(duration) or duration <= 0:
                raise ValueError('Target is not playable AV')
            for row in rows:
                value = row.get('timeline_range') if isinstance(row, dict) else None
                if (isinstance(value, list) and len(value) == 2 and type(value[1]) in (float, int)
                    and math.isfinite(value[1]) and value[1] > duration + 0.001):
                    hold(str(row.get('line_id')) + ': timeline exceeds AV duration')
        except (OSError, ValueError, KeyError, subprocess.SubprocessError):
            hold('Current AV cut: unreadable or missing video/audio stream')
    if not isinstance(report, dict):
        hold('No independent speaker review')
        report = {}
    try:
        if report.get('request_sha256') != fingerprint(request):
            hold('Review belongs to different source/version/range/cut')
    except (ValueError, TypeError):
        hold('Unhashable request')
    reviewer, maker = report.get('reviewer_id'), report.get('maker_id')
    if not isinstance(reviewer, str) or not reviewer.strip() or not isinstance(maker, str) or not maker.strip() or reviewer.strip() == maker.strip():
        hold('Independent reviewer and maker identity required')
    if report.get('independent_of_maker') is not True:
        hold('Reviewer independence not attested')
    if report.get('method') not in ('HUMAN_LISTENING_WITH_REFERENCE', 'AUDIO_CAPABLE_REVIEW_WITH_REFERENCE'):
        hold('ASR/prompt/anonymous diarization is not identity evidence')
    if report.get('actual_audio_reviewed') is not True or report.get('references_compared') is not True:
        hold('Actual listening/reference comparison missing')
    artifact(report.get('review_evidence'), 'Listening record')
    refs = report.get('references', {})
    if not isinstance(refs, dict):
        refs = {}; hold('Missing references')
    for speaker, voice in package.get('voices', {}).items():
        reference = refs.get(speaker, {})
        if not isinstance(reference, dict):
            reference = {}
        audio_artifact(reference.get('audio'), speaker + ' approved reference audio')
        artifact(reference.get('approval_evidence'), speaker + ' reference approval record')
        if reference.get('reference_id') != voice.get('reference_id') or reference.get('preset') != voice.get('preset'):
            hold(speaker + ': wrong reference ID/preset')
        if reference.get('approved_reference_provenance_checked') is not True:
            hold(speaker + ': reference provenance not reviewed')
    observations = report.get('lines', [])
    if not isinstance(observations, list):
        observations = []
    if [r.get('line_id') for r in observations if isinstance(r, dict)] != [r.get('line_id') for r in rows if isinstance(r, dict)]:
        hold('Missing, duplicated or reordered observations')
    evidence_ready = not holds
    for row, observed in zip(rows, observations):
        if not isinstance(row, dict) or not isinstance(observed, dict):
            hold('Invalid observation'); continue
        ident = row.get('line_id')
        if observed.get('line_id') != ident:
            hold(str(ident) + ': observation ID mismatch'); continue
        if observed.get('reviewed_full_source') is not True:
            hold(str(ident) + ': source audio not actually reviewed')
        if not isinstance(observed.get('observation'), str) or not observed['observation'].strip():
            hold(str(ident) + ': missing observation note')
        if observed.get('heard_text') is None or observed.get('observed_speaker') is None or observed.get('observed_voice_reference_id') is None:
            hold(str(ident) + ': actual speaker/text/voice unknown')
        elif evidence_ready and observed.get('reviewed_full_source') is True and (observed['heard_text'], observed['observed_speaker'], observed['observed_voice_reference_id']) != (row['text'], row['expected_speaker'], row['expected_voice']['reference_id']):
            defects.append(str(ident) + ': wrong spoken text/speaker/selected voice')
        if observed.get('identity_verdict') != 'PASS':
            hold(str(ident) + ': identity not established')
        for field, passed, failed in [('within_turn_identity_verdict', 'PASS_CONSISTENT', 'FAIL_SWITCHED'),
                                      ('overlap_verdict', 'PASS_NO_OVERLAP', 'FAIL_OVERLAP')]:
            if observed.get(field) == failed and evidence_ready and observed.get('reviewed_full_source') is True:
                defects.append(str(ident) + ': ' + field + ' failed')
            elif observed.get(field) != passed:
                hold(str(ident) + ': ' + field + ' unknown')
        if mode != 'AUDIO_SELECTION':
            if report.get('actual_full_av_reviewed') is not True:
                hold('Full current AV cut was not reviewed')
            sync = observed.get('sync_verdict')
            if sync == 'PASS_ONSCREEN':
                if observed.get('visible_speaker') != row.get('expected_speaker') and evidence_ready and report.get('actual_full_av_reviewed') is True:
                    defects.append(str(ident) + ': visible speaking character differs')
                if observed.get('other_character_silent') is not True:
                    hold(str(ident) + ': listener mouth/acting not checked')
            elif sync == 'PASS_APPROVED_OFFSCREEN':
                artifact(observed.get('offscreen_approval'), str(ident) + ' offscreen shot approval')
            elif sync == 'FAIL' and evidence_ready and report.get('actual_full_av_reviewed') is True:
                defects.append(str(ident) + ': AV speaker/lip-sync failed')
            else:
                hold(str(ident) + ': actual AV sync unknown')
    return {'status': 'REWORK' if defects else 'HOLD_FOR_INPUT' if holds else 'PASS',
            'scope': mode, 'holds': list(dict.fromkeys(holds)), 'defects': defects,
            'identity_detection_performed_by_gate': False,
            'release_authorized': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    prepare = sub.add_parser('prepare')
    prepare.add_argument('--package', type=Path, required=True)
    prepare.add_argument('--manifest', type=Path, required=True)
    prepare.add_argument('--out', type=Path, required=True)
    prepare.add_argument('--mode', choices=['AUDIO_SELECTION', 'AV_ASSEMBLY', 'FINAL_AV'], default='AUDIO_SELECTION')
    prepare.add_argument('--target', type=Path)
    check = sub.add_parser('check')
    check.add_argument('--request', type=Path, required=True)
    check.add_argument('--review', type=Path)
    check.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        parser.error('Existing output is preserved; choose a new path.')
    if args.command == 'prepare':
        manifest = json.loads(args.manifest.read_text(encoding='utf-8'))
        target = {'path': str(args.target.resolve()), 'sha256': digest(args.target)} if args.target else None
        value = source_request(args.package, manifest['captions'], manifest['audio_slots'], args.mode, target)
        value = {'request_sha256': fingerprint(value), 'request': value}
        status = 0
    else:
        request = json.loads(args.request.read_text(encoding='utf-8'))['request']
        review = json.loads(args.review.read_text(encoding='utf-8')) if args.review else None
        value = evaluate(request, review)
        status = 0 if value['status'] == 'PASS' else 2
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    print(json.dumps({'output': str(args.out), 'status': value.get('status', 'REQUEST_PREPARED')}, ensure_ascii=False))
    raise SystemExit(status)


if __name__ == '__main__':
    main()

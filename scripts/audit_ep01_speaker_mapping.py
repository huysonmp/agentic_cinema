"""Read-only source audit and diagnostic excerpts; does not infer speaker identity.

No network, no generation, no edit of source/assembly, no audio-only QC approval.
Outputs exact PCM excerpts with intended roles explicitly distinct from observations.
"""
import argparse
import hashlib
import json
import os
import subprocess
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EP = ROOT / 'he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot'
MEDIA = Path('C:/Users/PC/Downloads/du_an_nem_bui')
FF = ROOT / '.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/ffmpeg.exe'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pcm(path):
    with wave.open(str(path), 'rb') as audio:
        assert (audio.getframerate(), audio.getnchannels(), audio.getsampwidth()) == (48000, 2, 2)
        return audio.readframes(audio.getnframes())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists() and any(args.out.iterdir()):
        parser.error('Use a fresh directory. Existing evidence is preserved.')
    manifest = json.loads((EP / 'evidence/182/assembly-manifest.json').read_text(encoding='utf-8'))
    package = json.loads((EP / 'evidence/179/dialogue-package.json').read_text(encoding='utf-8'))
    sources = manifest['audio_slots']
    assert len(sources) == 2
    master_wav = MEDIA / '182_c_v06_assembly/render_v0.5/EP01_C-v0.6_PLANNING_AUDIO.wav'
    master = pcm(master_wav)
    source_data = []
    for source in sources:
        path = Path(source['source'])
        assert digest(path) == source['source_sha256']
        data = pcm(path) if path.suffix == '.wav' else subprocess.check_output([
            str(FF), '-nostdin', '-hide_banner', '-loglevel', 'error', '-i', str(path),
            '-vn', '-c:a', 'pcm_s16le', '-f', 's16le', 'pipe:1'])
        offset = round(source['timeline_in'] * 48000) * 4
        assert master[offset:offset + len(data)] == data
        source_data.append(data)
    args.out.mkdir(parents=True)
    rows = []
    for line in package['lines']:
        cues = [c for c in manifest['captions'] if c['line_id'] == line['id']]
        assert ' '.join(c['text'].replace('\n', ' ') for c in cues) == line['text']
        assert all(c.get('expected_speaker', c.get('speaker')) == line['speaker'] for c in cues)
        source_index = next(i for i, s in enumerate(sources) if line['id'] in s['line_ids'])
        slot = sources[source_index]
        start, end = cues[0]['start'], cues[-1]['end']
        # ASR-based timing only; generous short pads are listening aids, not final stems.
        lo = max(0, start - slot['timeline_in'] - 0.12)
        hi = min(len(source_data[source_index]) / (48000 * 4),
                 end - slot['timeline_in'] + 0.15)
        excerpt = source_data[source_index][round(lo * 48000) * 4:round(hi * 48000) * 4]
        target = args.out / f"{line['id']}_intended_{'Khoai' if line['speaker'] == 'Khoai' else 'Dao'}_UNVERIFIED.wav"
        with wave.open(str(target), 'wb') as audio:
            audio.setnchannels(2)
            audio.setsampwidth(2)
            audio.setframerate(48000)
            audio.writeframes(excerpt)
        rows.append({
            'line_id': line['id'], 'approved_text': line['text'],
            'expected_speaker': line['speaker'],
            'expected_voice': package['voices'][line['speaker']],
            'planned_timeline_start': start, 'planned_timeline_end': end,
            'source': slot['source'], 'source_in': round(lo, 3), 'source_out': round(hi, 3),
            'diagnostic_excerpt': str(target), 'excerpt_sha256': digest(target),
            'observed_speaker': None, 'voice_identity_verdict': 'UNVERIFIED',
            'observed_lipsync_speaker': None,
            'evidence_limit': 'Script/caption agreement and PCM provenance do not establish who actually speaks.'
        })
    report = {
        'status': 'PARTIAL_TECHNICAL_AUDIT_SPEAKER_IDENTITY_BLOCKED',
        'source_pcm_preserved_in_planning_wav': True,
        'turns_individually_reordered_by_assembly': False,
        'caption_role_from_approved_script': True,
        'actual_identity_verified': False,
        'heard_by_reviewer': False,
        'identity_reference_audio': 'Audition149/151 have UI previews only, no verified local reference WAV.',
        'available_local_asr': 'faster-whisper small, no diarization or reference identity verification',
        'openai_diarize_key_present': bool(os.environ.get('OPENAI_API_KEY')),
        'credit_spend': 0, 'source_or_assembly_modified': False, 'lines': rows
    }
    (args.out / 'speaker-audit.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'status': report['status'], 'diagnostic_excerpts': len(rows), 'credit_spend': 0}, ensure_ascii=False))


if __name__ == '__main__':
    main()

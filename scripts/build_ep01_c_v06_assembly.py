"""Build a clearly labelled C-v0.6 planning cut; never substitute it for a finished film.

Local-only derived media. Preserves source files and refuses to overwrite an output.
Uses the approved text package, full accepted audio, and a labelled C01 insert.
"""
import argparse
import hashlib
import json
import re
import subprocess
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EP = ROOT / 'he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot'
MEDIA = Path('C:/Users/PC/Downloads/du_an_nem_bui')
FF = ROOT / '.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/ffmpeg.exe'
FP = FF.with_name('ffprobe.exe')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')


def probe(path):
    return json.loads(subprocess.check_output(
        [str(FP), '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(path)],
        text=True, encoding='utf-8'))


def run(args):
    subprocess.run([str(FF), '-nostdin', '-hide_banner', '-loglevel', 'error', '-n', *args], check=True)


def escaped(path):
    return path.as_posix().replace(':', r'\:')


def seconds_srt(seconds):
    ms = round(seconds * 1000)
    hours, ms = divmod(ms, 3600000)
    minutes, ms = divmod(ms, 60000)
    secs, ms = divmod(ms, 1000)
    return f'{hours:02}:{minutes:02}:{secs:02},{ms:03}'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--closing-asr', type=Path, required=True)
    opts = parser.parse_args()
    out = opts.out
    if out.exists() and any(out.iterdir()):
        parser.error('Use a fresh render directory; existing output is preserved.')

    package_path = EP / 'evidence/179/dialogue-package.json'
    package = json.loads(package_path.read_text(encoding='utf-8'))
    approved = re.findall(r'\*\*(N\d{2}) — (Đào|Khoai):\*\* “([^”]+)”',
                          (EP / '178_owner-dialogue-amendment-c-v0.6.md').read_text(encoding='utf-8'))
    actual = [(line['id'], line['speaker'], line['text']) for line in package['lines']]
    assert len(approved) == 7 and actual == approved, 'Text differs from script178.'
    lines = {line['id']: line for line in package['lines']}
    core = MEDIA / '180_c_v06_dialogue/A03_VOICE_REVIEW.wav'
    closing = MEDIA / '154_visual_lock/R01.mp4'
    assert sha(core) == '9b560b03a98e3d0cd722a0a2877d5395c08110ad2f361230f534d8a8736b3ae0'
    assert sha(closing) == '9530c8c8315a7e3653c43cc400e7ab8891f536256e4d7dfaee5b16f326e59b19'
    core_duration = float(probe(core)['format']['duration'])
    closing_duration = float(probe(closing)['format']['duration'])
    assert abs(core_duration - 10.005) < 0.001 and closing_duration == 8

    # ASR word boundaries are timing hints, not new text or a pronunciation verdict.
    core_asr_path = EP / 'evidence/180/asr-A03.json'
    core_asr = json.loads(core_asr_path.read_text(encoding='utf-8'))
    words = [w for segment in core_asr['segments'] for w in segment['words']]
    assert len(words) == 34, 'A03 timing evidence changed; inspect before rendering.'
    ranges = [('N01', 0, 8, lines['N01']['caption']),
              ('N02', 8, 9, 'Khoan.'),
              ('N02', 9, 18, 'Mùi này làm anh nhớ\nđến bếp nhà anh.'),
              ('N02', 18, 26, 'Hồi bé, mẹ rang gạo,\nanh đứng chờ.'),
              ('N03', 26, 30, lines['N03']['caption']),
              ('N04', 30, 34, lines['N04']['caption'])]
    captions = []
    for line_id, lo, hi, text in ranges:
        captions.append({'line_id': line_id, 'speaker': lines[line_id]['speaker'],
                         'start': round(2 + words[lo]['start'], 3),
                         'end': round(2 + words[hi-1]['end'], 3), 'text': text})
    closing_asr = json.loads(opts.closing_asr.read_text(encoding='utf-8'))
    assert len(closing_asr['segments']) == 3
    for line_id, segment in zip(['N05', 'N06', 'N07'], closing_asr['segments']):
        captions.append({'line_id': line_id, 'speaker': lines[line_id]['speaker'],
                         'start': round(20 + segment['start'], 3),
                         'end': round(20 + segment['end'], 3), 'text': lines[line_id]['caption']})
    ids = list(dict.fromkeys(c['line_id'] for c in captions))
    assert ids == list(lines)
    for line_id in ids:
        joined = ' '.join(c['text'].replace('\n', ' ') for c in captions if c['line_id'] == line_id)
        assert joined == lines[line_id]['text'], f'Caption drift: {line_id}'
    assert all(c['start'] < c['end'] for c in captions)
    assert all(a['end'] <= b['start'] for a, b in zip(captions, captions[1:]))

    opening = MEDIA / 'T2-CODEX-OPEN_v0.7.png'
    hold = MEDIA / '161_source_retest/START_short_tuft_v0.1.png'
    reaction = MEDIA / '163_low-hold-reaction/END_low_reaction_v0.1.png'
    pickup = MEDIA / '159_closeup_pickup/C01.mp4'
    shot_specs = [
        ('S01', 0, 2, opening, None, 'ẢNH TẠM: nhận diện món / đặt nhịp'),
        ('S02', 2, 10, opening, None, 'ẢNH TẠM: thoại mới / thiếu diễn và khớp môi'),
        ('S03', 12, 1.5, opening, None, 'THIẾU VIDEO: Đào quay lấy cốc'),
        ('S04', 13.5, 2.5, pickup, 2.75, 'VIDEO C01: động tác gắp / chưa duyệt nối'),
        ('S05', 16, 2.5, hold, None, 'THIẾU VIDEO: nâng về mình rồi khựng'),
        ('S06', 18.5, 1.5, reaction, None, 'THIẾU VIDEO: Đào quay lại, bắt gặp'),
        ('S07', 20, 2.6, reaction, None, 'ẢNH TẠM: Đào hỏi / thiếu diễn'),
        ('S08', 22.6, 2.4, reaction, None, 'THIẾU VIDEO: đổi hướng, đưa bát nhận'),
        ('S09', 25, 3, opening, None, 'THIẾU VIDEO: đặt nem vào bát Đào'),
        ('S10', 28, 2, opening, None, 'THIẾU VIDEO: cười nhẹ / Khoai gắp tiếp'),
    ]
    assert all(a[1] + a[2] == b[1] for a, b in zip(shot_specs, shot_specs[1:]))
    overlays = [{'id': 'F01', 'start': 0, 'end': 4,
                 'text': 'Nem Bùi — gắn với\nBùi Xá, Bắc Ninh.'},
                {'id': 'F02', 'start': 5.1, 'end': 9.66,
                 'text': 'Thính gạo rang góp một phần\nvào mùi vị của Nem Bùi.'},
                {'id': 'AI', 'start': 0, 'end': 30, 'text': 'Video được tạo bằng AI.'}]
    for overlay, expected in zip(overlays, package['release_text']):
        assert overlay['id'] == expected['id']
        assert overlay['text'].replace('\n', ' ') == expected['text']

    out.mkdir(parents=True, exist_ok=True)
    font = escaped(Path('C:/Windows/Fonts/arial.ttf'))
    draft = out / 'draft-label.txt'
    draft.write_text('BẢN KIỂM MẠCH C-v0.6 — CHƯA BÀN GIAO', encoding='utf-8')
    manifest_shots = []
    parts = []
    for name, begin, duration, source, seek, label in shot_specs:
        label_file = out / f'{name}-label.txt'
        label_file.write_text(label, encoding='utf-8')
        vf = 'scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24'
        vf += ',drawbox=x=0:y=0:w=iw:h=115:color=black@0.85:t=fill'
        vf += f",drawtext=fontfile='{font}':textfile='{escaped(draft)}':fontsize=24:fontcolor=yellow:x=(w-text_w)/2:y=20"
        vf += f",drawtext=fontfile='{font}':textfile='{escaped(label_file)}':fontsize=23:fontcolor=white:x=(w-text_w)/2:y=67"
        vf += ',drawbox=x=0:y=1080:w=iw:h=200:color=black@0.8:t=fill'
        for i, cue in enumerate(captions + overlays):
            lo, hi = max(begin, cue['start']), min(begin + duration, cue['end'])
            if hi <= lo:
                continue
            text_file = out / f'{name}-cue-{i}.txt'
            text_file.write_text(cue['text'], encoding='utf-8')
            is_ai = cue.get('id') == 'AI'
            is_fact = cue.get('id') in ('F01', 'F02')
            y = 1010 if is_ai else 145 if is_fact else 1130
            size = 22 if is_ai else 27 if is_fact else 29
            vf += f",drawtext=fontfile='{font}':textfile='{escaped(text_file)}':fontsize={size}:fontcolor=white:box=1:boxcolor=black@0.65:boxborderw=8:line_spacing=10:x=(w-text_w)/2:y={y}:enable='gte(t,{lo-begin})*lt(t,{hi-begin})'"
        target = out / f'{name}.mp4'
        source_args = ['-loop', '1', '-i', str(source)] if seek is None else ['-ss', str(seek), '-i', str(source)]
        run([*source_args, '-t', str(duration), '-vf', vf, '-an', '-c:v', 'libx264',
             '-preset', 'fast', '-crf', '20', '-pix_fmt', 'yuv420p', str(target)])
        parts.append(target)
        manifest_shots.append({'shot': name, 'timeline_in': begin, 'timeline_out': begin+duration,
                               'source': source.as_posix(), 'source_in': seek,
                               'source_out': None if seek is None else seek+duration,
                               'source_sha256': sha(source), 'status': label})
    concat = out / 'concat.txt'
    concat.write_text('\n'.join("file '" + p.as_posix() + "'" for p in parts), encoding='utf-8')
    pcm = out / 'EP01_C-v0.6_PLANNING_AUDIO.wav'
    audio_filter = ('[0:a]adelay=2000:all=1,apad=whole_dur=30[core];'
                    '[1:a]adelay=20000:all=1,apad=whole_dur=30[end];'
                    '[core][end]amix=inputs=2:duration=longest:normalize=0[a]')
    run(['-i', str(core), '-i', str(closing), '-filter_complex', audio_filter,
         '-map', '[a]', '-t', '30', '-c:a', 'pcm_s16le', str(pcm)])
    master = out / 'EP01_30s_C-v0.6_PLANNING_v0.5.mp4'
    run(['-f', 'concat', '-safe', '0', '-i', str(concat), '-i', str(pcm), '-map', '0:v',
         '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', '30',
         '-movflags', '+faststart', str(master)])
    run(['-i', str(master), '-vf', 'fps=1/2,scale=180:320,tile=5x3', '-frames:v', '1', str(out/'contact.png')])
    run(['-ss', '8.2', '-i', str(master), '-frames:v', '1', str(out/'caption-fact-check.png')])
    run(['-i', str(master), '-f', 'null', 'NUL'])

    # Independent of the filter graph: build expected PCM by byte placement.
    closing_wav = out / 'R01_native_audio.wav'
    run(['-i', str(closing), '-vn', '-c:a', 'pcm_s16le', str(closing_wav)])
    expected_pcm = bytearray(30 * 48000 * 2 * 2)
    for source, offset in [(core, 2), (closing_wav, 20)]:
        with wave.open(str(source), 'rb') as audio:
            assert (audio.getframerate(), audio.getnchannels(), audio.getsampwidth()) == (48000, 2, 2)
            data = audio.readframes(audio.getnframes())
        start_byte = offset * 48000 * 4
        expected_pcm[start_byte:start_byte+len(data)] = data
    with wave.open(str(pcm), 'rb') as audio:
        assert audio.getnframes() == 30 * 48000
        rendered_pcm = audio.readframes(audio.getnframes())
    assert rendered_pcm == expected_pcm, 'Audio placement changed/truncated source PCM.'
    metadata = probe(master)
    video = next(s for s in metadata['streams'] if s['codec_type'] == 'video')
    assert (video['width'], video['height'], video['r_frame_rate']) == (720, 1280, '24/1')
    assert float(metadata['format']['duration']) == 30
    assert any(s['codec_type'] == 'audio' for s in metadata['streams'])
    audio_slots = [
        {'source': core.as_posix(), 'source_sha256': sha(core), 'timeline_in': 2,
         'timeline_out': 2 + core_duration, 'line_ids': ['N01','N02','N03','N04'],
         'status': 'OWNER_PROVISIONAL_BATCH_ACCEPTED_ROOT_A03_WORKING_SELECTION'},
        {'source': closing.as_posix(), 'source_sha256': sha(closing), 'timeline_in': 20,
         'timeline_out': 28, 'line_ids': ['N05','N06','N07'], 'status': 'OWNER_REUSE_APPROVED_168'},
    ]
    report = {'status': 'PLANNING_NOT_DELIVERY', 'script_version': 'C-v0.6',
              'assembly_version': 'v0.5', 'local_credit_spend': 0, 'script_source': '178',
              'text_package_sha256': sha(package_path), 'shots': manifest_shots,
              'audio_slots': audio_slots, 'captions': captions, 'release_overlays': overlays,
              'caption_timing_basis': 'ASR word/segment hints, manually mapped to approved text; provisional, not forced alignment.',
              'core_asr_sha256': sha(core_asr_path), 'closing_asr_sha256': sha(opts.closing_asr),
              'audio_working_choice_reason': 'A03 has -0.4dBFS peak versus 0.0 for A01/A02; technical tie-break, not independent ear verdict or owner winner.',
              'still_placeholder_seconds': 27.5, 'video_insert_seconds': 2.5,
              'silent_action_window_seconds': [12.005, 20], 'source_audio_complete_pcm_match': 'PASS',
              'gain_or_speed_change': False, 'performance_lipsync_continuity': 'NOT_APPROVED',
              'independent_ear_review': 'NOT_PERFORMED', 'final_mix': 'NOT_DONE',
              'output_metadata': metadata, 'master_sha256': sha(master), 'master_bytes': master.stat().st_size}
    write_json(out/'manifest.json', report)
    srt = '\n\n'.join(f"{i}\n{seconds_srt(c['start'])} --> {seconds_srt(c['end'])}\n{c['text']}"
                        for i, c in enumerate(captions, 1)) + '\n'
    (out/'EP01_C-v0.6_TIMING_DRAFT.srt').write_text(srt, encoding='utf-8')
    write_json(out/'technical-qc.json', {
        'status': 'TECHNICAL_AND_TEXT_PASS_NOT_FINAL_CREATIVE_QC', 'exact_script_lines': 7,
        'subtitle_cues': len(captions), 'full_decode': 'PASS', 'input_audio_hashes': 'PASS',
        'complete_source_pcm_placement': 'PASS', 'duration_seconds': 30, 'dimensions': [720,1280],
        'fps': 24, 'master_sha256': sha(master), 'master_bytes': master.stat().st_size,
        'still_placeholder_seconds': 27.5, 'lip_sync': 'NOT_APPROVED', 'ear_qc': 'NOT_PERFORMED'})
    print(json.dumps({'master': master.as_posix(), 'bytes': master.stat().st_size,
                      'duration_seconds': 30, 'source_pcm_match': True}, ensure_ascii=False))


if __name__ == '__main__':
    main()

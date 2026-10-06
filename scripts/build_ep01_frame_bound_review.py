"""Local frame-bound AV review; never changes source media or marks a release PASS."""
import argparse
import hashlib
import json
import subprocess
import wave
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate_timeline(data):
    assert data['fps'] == 24 and data['duration_frames'] == 720
    cursor = 0
    by_source = {}
    for shot in data['shots']:
        assert shot['in_frame'] == cursor
        assert shot['out_frame'] > cursor
        lo, hi = shot['source_range_frames']
        assert isinstance(lo, int) and isinstance(hi, int) and lo >= 0
        assert hi - lo == shot['out_frame'] - cursor
        assert shot['selection_status'].startswith('ROOT_CANDIDATE')
        source = shot['source']
        for prior_lo, prior_hi in by_source.get(source, []):
            assert hi <= prior_lo or lo >= prior_hi, 'Repeated source frames'
        by_source.setdefault(source, []).append((lo, hi))
        cursor = shot['out_frame']
    assert cursor == 720


def place_pcm(raw, slots, rate=48000, frame_bytes=4):
    assert len(raw) % frame_bytes == 0
    out = bytearray(30 * rate * frame_bytes)
    consumed = []
    occupied = []
    for slot in slots:
        lo = round(slot['review_in'] * rate)
        hi = round(slot['review_out'] * rate)
        dest = round(slot['timeline_in'] * rate)
        assert 0 <= lo < hi <= len(raw) // frame_bytes
        assert 0 <= dest and dest + hi - lo <= 30 * rate
        for prev_lo, prev_hi in occupied:
            assert dest + hi - lo <= prev_lo or dest >= prev_hi
        consumed.append((lo, hi))
        occupied.append((dest, dest + hi - lo))
        out[dest * frame_bytes:(dest + hi - lo) * frame_bytes] = raw[lo * frame_bytes:hi * frame_bytes]
    consumed.sort()
    assert consumed[0][0] == 0 and consumed[-1][1] == len(raw) // frame_bytes
    assert all(a[1] == b[0] for a, b in zip(consumed, consumed[1:]))
    return bytes(out)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--timeline', type=Path, required=True)
    p.add_argument('--audio', type=Path, required=True)
    p.add_argument('--ffmpeg-bin', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    opts = p.parse_args()
    if opts.out.exists():
        p.error('Use a fresh directory; never overwrite an earlier review.')
    data = json.loads(opts.timeline.read_text(encoding='utf-8'))
    validate_timeline(data)
    assert sha(opts.audio) == data['audio_review_sha256']
    for shot in data['shots']:
        assert sha(shot['source']) == shot['sha256'], shot['id']
    with wave.open(str(opts.audio), 'rb') as w:
        assert (w.getnchannels(), w.getsampwidth(), w.getframerate()) == (2, 2, 48000)
        raw = w.readframes(w.getnframes())
    expected_pcm = place_pcm(raw, data['audio_placements'])
    opts.out.mkdir(parents=True)
    pcm = opts.out / 'EP01_EXACT_APPROVED_PCM_30S.wav'
    with wave.open(str(pcm), 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(48000)
        w.writeframes(expected_pcm)
    with wave.open(str(pcm), 'rb') as w:
        assert w.readframes(w.getnframes()) == expected_pcm
    ff = opts.ffmpeg_bin / 'ffmpeg.exe'
    fp = opts.ffmpeg_bin / 'ffprobe.exe'

    def run(args):
        subprocess.run([str(ff), '-nostdin', '-hide_banner', '-loglevel', 'error', '-n', *args], check=True)

    def probe(path):
        return json.loads(subprocess.check_output([str(fp), '-v', 'error', '-count_frames', '-show_streams',
                                                  '-show_format', '-of', 'json', str(path)], text=True))

    parts = []
    for shot in data['shots']:
        lo, hi = shot['source_range_frames']
        source_probe = probe(shot['source'])
        source_v = next(s for s in source_probe['streams'] if s['codec_type'] == 'video')
        assert (source_v['width'], source_v['height'], source_v['avg_frame_rate']) == (720, 1280, '24/1')
        assert int(source_v['nb_read_frames']) >= hi
        part = opts.out / (shot['id'] + '.mp4')
        run(['-i', shot['source'], '-vf', f'trim=start_frame={lo}:end_frame={hi},setpts=PTS-STARTPTS,setsar=1',
             '-an', '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-pix_fmt', 'yuv420p', str(part)])
        assert int(next(s for s in probe(part)['streams'] if s['codec_type'] == 'video')['nb_read_frames']) == hi - lo
        parts.append(part)
    concat = opts.out / 'concat.txt'
    concat.write_text('\n'.join("file '" + part.as_posix() + "'" for part in parts) + '\n', encoding='utf-8')
    picture = opts.out / 'EP01_30S_PICTURE_REVIEW_NOT_FINAL.mp4'
    run(['-f', 'concat', '-safe', '0', '-i', str(concat), '-map', '0:v:0', '-c:v', 'copy', '-an', str(picture)])
    review = opts.out / 'EP01_30S_AV_REVIEW_NOT_FINAL.mp4'
    run(['-i', str(picture), '-i', str(pcm), '-map', '0:v:0', '-map', '1:a:0', '-c:v', 'copy',
         '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', str(review)])
    metadata = probe(review)
    video = next(s for s in metadata['streams'] if s['codec_type'] == 'video')
    assert int(video['nb_read_frames']) == 720 and abs(float(metadata['format']['duration']) - 30) < 0.001
    run(['-i', str(review), '-f', 'null', 'NUL'])
    run(['-i', str(review), '-vf', 'fps=1,scale=180:320,tile=10x3', '-frames:v', '1', str(opts.out/'contact.png')])
    for shot in data['shots']:
        assert sha(shot['source']) == shot['sha256']
    report = {'status': 'TECHNICAL_REVIEW_NOT_OWNER_ACCEPTANCE_OR_RELEASE',
              'timeline_sha256': sha(opts.timeline), 'approved_audio_sha256': sha(opts.audio),
              'complete_approved_pcm_placement_match': True, 'picture_frames': 720,
              'duration_seconds': 30, 'repeat_freeze_speed_or_pitch_change': False,
              'generated_source_audio_used': False, 'output': str(review.resolve()),
              'output_sha256': sha(review), 'output_metadata': metadata,
              'formal_SIA_report': 'NOT_CREATED', 'creative_AV_gate': 'PENDING_OWNER',
              'subtitle_fact_AI_overlays_music_final_mix': 'NOT_ADDED_IN_THIS_REVIEW'}
    (opts.out/'technical-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('output','output_sha256','picture_frames','duration_seconds')}))


if __name__ == '__main__':
    main()

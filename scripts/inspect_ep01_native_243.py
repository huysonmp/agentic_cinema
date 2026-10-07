"""Read-only native-video QC evidence; no edit, retake or release approval."""
import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from pathlib import Path
from PIL import Image, ImageDraw


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source', type=Path, required=True)
    ap.add_argument('--bin', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        ap.error('Use a new output directory, do not overwrite previous evidence.')
    original_hash = hashlib.sha256(args.source.read_bytes()).hexdigest()
    probe = json.loads(subprocess.check_output([
        str(args.bin / 'ffprobe.exe'), '-v', 'error', '-count_frames',
        '-show_streams', '-show_format', '-of', 'json', str(args.source)
    ], text=True))
    video = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    fps = Fraction(video['avg_frame_rate'])
    frame_probe = json.loads(subprocess.check_output([
        str(args.bin / 'ffprobe.exe'), '-v', 'error', '-select_streams', 'v:0',
        '-show_frames', '-show_entries', 'frame=best_effort_timestamp_time',
        '-of', 'json', str(args.source)
    ], text=True))
    timestamps = [float(f['best_effort_timestamp_time']) for f in frame_probe['frames']]
    args.out.mkdir(parents=True)
    frames_dir = args.out / 'all_native_frames'
    frames_dir.mkdir()
    ff = str(args.bin / 'ffmpeg.exe')
    def run(*extra):
        subprocess.run([ff, '-nostdin', '-hide_banner', '-loglevel', 'error',
                        '-n', '-i', str(args.source), *extra], check=True)
    run('-f', 'null', 'NUL')
    run('-map', '0:v:0', '-fps_mode', 'passthrough', str(frames_dir / '%05d.png'))
    if any(s['codec_type'] == 'audio' for s in probe['streams']):
        run('-map', '0:a:0', '-vn', '-c:a', 'pcm_s16le', str(args.out / 'native_audio.wav'))
    files = sorted(frames_dir.glob('*.png'))
    assert len(files) == len(timestamps), 'Frame count and timestamp evidence mismatch'
    evidence = []
    for rate, name in [(1, 'overview_1fps'), (6, 'mouth_hands_6fps')]:
        selected = sorted(set(min(range(len(files)), key=lambda i: abs(timestamps[i]-n/rate))
                              for n in range(int(float(probe['format']['duration'])*rate))))
        for page, start in enumerate(range(0, len(selected), 15), 1):
            sheet = Image.new('RGB', (1000, 1155), '#181818')
            draw = ImageDraw.Draw(sheet)
            for cell, index in enumerate(selected[start:start+15]):
                img = Image.open(files[index]).convert('RGB')
                img.thumbnail((196, 352))
                x, y = (cell % 5)*200, (cell//5)*385
                sheet.paste(img, (x+(200-img.width)//2, y))
                sec = timestamps[index]
                draw.text((x+4, y+357), f'frame {index} / {sec:.3f}s', fill='white')
                evidence.append({'board': f'{name}_{page:02d}.jpg',
                                 'frame_zero_based': index, 'time_seconds': sec})
            sheet.save(args.out / f'{name}_{page:02d}.jpg', quality=92)
    assert original_hash == hashlib.sha256(args.source.read_bytes()).hexdigest()
    report = {'status': 'TECHNICAL_AND_FRAME_EVIDENCE_NOT_AV_PASS',
              'source': str(args.source.resolve()), 'sha256': original_hash,
              'probe': probe, 'extracted_frames': len(files),
              'native_frame_timestamps': timestamps,
              'video_fps': str(fps), 'full_decode_success': True,
              'source_unchanged': True, 'boards': evidence,
              'actual_listening': 'NOT_PERFORMED', 'lip_sync': 'NOT_CERTIFIED',
              'frame_sampling_not_continuous_AV': True}
    (args.out / 'native_evidence.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding='utf8')
    print(json.dumps({k: report[k] for k in ['sha256','extracted_frames','video_fps','status']}))


if __name__ == '__main__':
    main()

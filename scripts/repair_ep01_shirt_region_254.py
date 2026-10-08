"""Local video shirt-region repair, original audio stream copied; never overwrite sources.

No synthesis, image generation, speech, face alteration or full-frame freeze.
Uses already decoded source frames; clean shirt anchors are zero-based F22/F58.
Every altered pixel before encoding is restricted to a small shirt rectangle.
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

SOURCE_HASH = '780ab0b3fb29454f732d2f56ed30526a77f81ed98bbaf04ca04cdb5cf094b231'
PATCH = (260, 830, 463, 918)
ROI = (230, 715, 510, 943)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def register(anchor, target):
    # Translation only, measured on visible shirt around (not underneath) the word.
    x0, y0, x1, y1 = ROI
    xs, ys, xe, ye = PATCH
    valid = np.ones((y1-y0, x1-x0), dtype=bool)
    valid[ys-y0:ye-y0, xs-x0:xe-x0] = False
    target_roi = target[y0:y1, x0:x1].astype(float)
    choices = []
    # Coarse-to-fine measurements, not an assumed stationary fabric patch.
    for dy in range(-40, 41, 4):
        for dx in range(-8, 9, 2):
            moved = anchor[y0-dy:y1-dy, x0-dx:x1-dx].astype(float)
            choices.append((float(np.mean(np.abs(moved-target_roi)[valid])), dx, dy))
    _, coarse_x, coarse_y = min(choices)
    for dy in range(max(-40, coarse_y-2), min(40, coarse_y+2)+1):
        for dx in range(max(-8, coarse_x-1), min(8, coarse_x+1)+1):
            moved = anchor[y0-dy:y1-dy, x0-dx:x1-dx].astype(float)
            choices.append((float(np.mean(np.abs(moved-target_roi)[valid])), dx, dy))
    error, dx, dy = min(choices)
    return {'dx': dx, 'dy': dy, 'visible_shirt_mae': error}


def shift_crop(image, move):
    x0, y0, x1, y1 = PATCH
    dx, dy = move['dx'], move['dy']
    return image[y0-dy:y1-dy, x0-dx:x1-dx].astype(float)


def audio_packets(ffprobe, path):
    data = json.loads(subprocess.check_output([
        str(ffprobe), '-v', 'error', '-select_streams', 'a:0', '-show_packets',
        '-show_data_hash', 'sha256', '-show_entries',
        'packet=pts_time,dts_time,duration_time,data_hash', '-of', 'json', str(path)
    ], text=True))
    return data['packets']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--source-qc', type=Path, required=True)
    parser.add_argument('--bin', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--video-out', type=Path, required=True)
    parser.add_argument('--analyze-only', action='store_true')
    args = parser.parse_args()
    if args.out.exists() or args.video_out.exists():
        parser.error('New output/evidence paths required; never overwrite.')
    if sha(args.source) != SOURCE_HASH:
        parser.error('Not the owner-approved original T02.')
    source_qc = json.loads((args.source_qc / 'native_evidence.json').read_text(encoding='utf8'))
    if source_qc['sha256'] != SOURCE_HASH or source_qc['video_fps'] != '24':
        parser.error('Source evidence/hash/fps mismatch.')
    files = sorted((args.source_qc / 'all_native_frames').glob('*.png'))
    if len(files) != 96:
        parser.error('This narrow repair is bound to the exact 96-frame source.')
    args.out.mkdir(parents=True)
    before = np.asarray(Image.open(files[22]).convert('RGB'))
    after = np.asarray(Image.open(files[58]).convert('RGB'))
    if args.analyze_only:
        analysis = []
        for index in range(23, 58):
            frame = np.asarray(Image.open(files[index]).convert('RGB'))
            analysis.append({'frame': index, 'anchor22': register(before, frame),
                             'anchor58': register(after, frame)})
        (args.out / 'shirt_registration_analysis.json').write_text(
            json.dumps({'source_sha256': SOURCE_HASH, 'roi': ROI, 'excluded_patch': PATCH,
                        'search_limit_pixels_xy': [8, 40], 'frames': analysis,
                        'media_created': False}, indent=2), encoding='utf8')
        print(json.dumps(analysis))
        return
    x0, y0, x1, y1 = PATCH
    w, h = x1-x0, y1-y0
    # The lettering lies in the full-opacity interior; the eight-pixel edge is feathered.
    yy, xx = np.indices((h, w))
    edge = np.minimum.reduce([xx, yy, w-1-xx, h-1-yy])
    alpha = np.clip(edge / 8.0, 0, 1)[..., None]
    frame_dir = args.out / 'composited_frames'
    frame_dir.mkdir()
    records = []
    for index, file in enumerate(files):
        original = np.asarray(Image.open(file).convert('RGB'))
        candidate = original.copy()
        item = {'frame': index, 'time': source_qc['native_frame_timestamps'][index],
                'altered': 23 <= index <= 57}
        if item['altered']:
            left = register(before, original)
            right = register(after, original)
            if any(abs(m['dx']) == 8 or abs(m['dy']) == 40 for m in (left, right)):
                raise RuntimeError(f'Registration hits search boundary at F{index}: {left}, {right}.')
            mix = (index - 22) / (58 - 22)
            clean = (1-mix)*shift_crop(before, left) + mix*shift_crop(after, right)
            candidate[y0:y1, x0:x1] = np.rint(
                (1-alpha)*original[y0:y1, x0:x1] + alpha*clean).astype(np.uint8)
            item.update(anchor22=left, anchor58=right, anchor58_weight=mix)
        changed = np.any(candidate != original, axis=2)
        changed[y0:y1, x0:x1] = False
        assert not changed.any(), 'A pixel outside the allowed shirt rectangle changed.'
        if not item['altered']:
            assert np.array_equal(candidate, original)
        records.append(item)
        Image.fromarray(candidate).save(frame_dir / file.name)
    # All-frame close-shirt boards, actual source left / compositor right.
    for start in range(0, 96, 12):
        board = Image.new('RGB', (1200, 930), '#181818')
        draw = ImageDraw.Draw(board)
        for cell, index in enumerate(range(start, start+12)):
            x, y = (cell % 4)*300, (cell//4)*310
            for offset, file in [(0, files[index]), (150, frame_dir / files[index].name)]:
                crop = Image.open(file).crop((240, 725, 490, 950)).convert('RGB')
                crop.thumbnail((150, 250))
                board.paste(crop, (x+offset, y+28))
            draw.text((x+2, y+2), f'F{index} {index/24:.3f}s source | local', fill='white')
        board.save(args.out / f'shirt_all_frames_{start//12+1:02d}.jpg', quality=95)
    ffmpeg, ffprobe = args.bin / 'ffmpeg.exe', args.bin / 'ffprobe.exe'
    subprocess.run([
        str(ffmpeg), '-nostdin', '-hide_banner', '-loglevel', 'error', '-n',
        '-framerate', '24', '-i', str(frame_dir / '%05d.png'), '-i', str(args.source),
        '-map', '0:v:0', '-map', '1:a:0', '-c:v', 'libx264', '-crf', '12',
        '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'copy',
        '-map_metadata', '-1', '-movflags', '+faststart', str(args.video_out)
    ], check=True)
    source_packets = audio_packets(ffprobe, args.source)
    result_packets = audio_packets(ffprobe, args.video_out)
    assert source_packets == result_packets, 'Original audio packet hashes/timing changed.'
    assert sha(args.source) == SOURCE_HASH
    report = {'record': 'REC254', 'status': 'LOCAL_CANDIDATE_NOT_SELECTED_NOT_AV_PASS',
              'source': str(args.source.resolve()), 'source_sha256': SOURCE_HASH,
              'output': str(args.video_out.resolve()), 'output_sha256': sha(args.video_out),
              'patch_xyxy': list(PATCH), 'clean_anchor_frames': [22, 58],
              'changed_frame_range_inclusive': [23, 57], 'frames': records,
              'pre_encode_outside_patch_exactly_unchanged': True,
              'pre_encode_other61_frames_exactly_unchanged': True,
              'video_reencoded': True,
              'outside_patch_encoded_pixels_not_guaranteed_bit_exact': True,
              'audio_packets_hashes_and_timing_exactly_equal': True,
              'audio_packets_count': len(source_packets),
              'source_unchanged': True, 'Flow_submits': 0, 'Flow_credits_spent': 0,
              'actual_listening': 'NOT_PERFORMED', 'lip_sync': 'NOT_CERTIFIED'}
    (args.out / 'repair_manifest.json').write_text(json.dumps(report, indent=2), encoding='utf8')
    print(json.dumps({key: report[key] for key in ['status', 'output_sha256',
                                                 'audio_packets_hashes_and_timing_exactly_equal']}))


if __name__ == '__main__':
    main()

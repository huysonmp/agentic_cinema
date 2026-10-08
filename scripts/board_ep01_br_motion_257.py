"""REC257 dense still evidence for every BR frame, not continuous-AV approval."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--qc', type=Path, required=True)
p.add_argument('--out', type=Path, required=True)
a = p.parse_args()
evidence = json.loads((a.qc / 'native_evidence.json').read_text(encoding='utf-8'))
frames = sorted((a.qc / 'all_native_frames').glob('*.png'))
assert len(frames) == evidence['extracted_frames']
timestamps = evidence['native_frame_timestamps']
a.out.mkdir(exist_ok=False)
pages = []
for start in range(0, len(frames), 8):
    board = Image.new('RGB', (1000, 1520), '#181818')
    draw = ImageDraw.Draw(board)
    indices = list(range(start, min(start + 8, len(frames))))
    for cell, idx in enumerate(indices):
        im = Image.open(frames[idx]).convert('RGB')
        assert im.size == (720, 1280)
        x, y = (cell % 2) * 500, (cell // 2) * 380
        full = im.copy()
        full.thumbnail((195, 347))
        board.paste(full, (x, y))
        hand = im.crop((365, 760, 720, 1060))
        hand.thumbnail((290, 150))
        board.paste(hand, (x + 205, y))
        face = im.crop((345, 320, 720, 740))
        face.thumbnail((290, 185))
        board.paste(face, (x + 205, y + 155))
        draw.text((x + 3, y + 353), f'F{idx} / {timestamps[idx]:.6f}s / full + Dao hand + face', fill='white')
    name = f'all_frames_{start//8+1:02d}.png'
    board.save(a.out / name)
    pages.append({'board': name, 'zero_based_frames': indices})
manifest = {'target_sha256': evidence['sha256'], 'all_frames_included': len(frames),
            'pages': pages, 'scope': 'ALL_FRAME_STILLS_NOT_CONTINUOUS_AV',
            'audio_streams': sum(s['codec_type'] == 'audio' for s in evidence['probe']['streams'])}
(a.out / 'board_manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
print(json.dumps(manifest, indent=2))

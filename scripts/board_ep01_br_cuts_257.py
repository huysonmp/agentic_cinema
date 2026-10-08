"""Dense encoded boundary boards; all BR candidate frames, no AV approval."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--qc', type=Path, required=True)
p.add_argument('--out', type=Path, required=True)
a = p.parse_args()
e = json.loads((a.qc / 'native_evidence.json').read_text(encoding='utf8'))
assert e['extracted_frames'] == 330
frames = sorted((a.qc / 'all_native_frames').glob('*.png'))
a.out.mkdir(exist_ok=False)
# Every candidate BR frame plus eight encoded frames on either side of each new cut.
indices = list(range(91, 157))
pages = []
for start in range(0, len(indices), 12):
    board = Image.new('RGB', (900, 1640), '#181818')
    draw = ImageDraw.Draw(board)
    selection = indices[start:start+12]
    for cell, idx in enumerate(selection):
        im = Image.open(frames[idx]).convert('RGB')
        assert im.size == (720, 1280)
        im.thumbnail((216, 384))
        x, y = (cell % 3)*300, (cell//3)*410
        board.paste(im, (x, y))
        source = f'BM F{idx-81}' if idx < 99 else (f'BR F{idx-99+28}' if idx < 149 else f'C02 F{idx-149}')
        draw.text((x+2, y+387), f'F{idx} {idx/24:.3f}s {source}', fill='white')
    name = f'new_cuts_{start//12+1:02d}.png'
    board.save(a.out/name)
    pages.append({'board': name, 'target_frames_zero_based': selection})
(a.out/'manifest.json').write_text(json.dumps({'target_sha256': e['sha256'],
    'reviewed_frame_range_half_open': [91,157], 'pages': pages,
    'scope': '66_CONSECUTIVE_ENCODED_STILLS_NOT_AV'}, indent=2), encoding='utf8')
print('66 encoded frames including all50BR and both new cuts.')

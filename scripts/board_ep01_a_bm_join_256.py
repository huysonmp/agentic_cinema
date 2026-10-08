"""Build dense boards around the actual A→BM cut; no listening/AV approval."""
from pathlib import Path
from PIL import Image, ImageDraw

BASE = Path('C:/Users/PC/Downloads/du_an_nem_bui/256_A_BM_JOIN')
frames = sorted((BASE / 'encoded_qc/all_native_frames').glob('*.png'))
assert len(frames) == 99
out = BASE / 'join_boards'
out.mkdir(exist_ok=False)
# Review last eight A frames and every BM frame after actual encoding.
indices = list(range(73, 99))
for page in range(2):
    board = Image.new('RGB', (900, 2000), '#181818')
    draw = ImageDraw.Draw(board)
    for cell, index in enumerate(indices[page * 15:(page + 1) * 15]):
        im = Image.open(frames[index]).convert('RGB')
        assert im.size == (720, 1280)
        x, y = (cell % 3) * 300, (cell // 3) * 400
        im.thumbnail((205, 365))
        board.paste(im, (x, y))
        shot = 'A' if index < 81 else 'BM'
        native_idx = index if index < 81 else index - 81
        draw.text((x + 2, y + 370), f'JOIN F{index} / {index/24:.3f}s / {shot} F{native_idx}', fill='white')
    board.save(out / f'cut_dense_{page + 1}.png')
print('26 encoded frames: A73..80 followed by BM0..17; cut at join F81 (3.375s).')

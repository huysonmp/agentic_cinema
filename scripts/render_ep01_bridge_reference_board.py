"""Lay out existing stills for QC; never generate motion or certify continuity."""
import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
EP = ROOT / 'he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--config', type=Path, default=EP/'evidence/187/bridge-input-preflight.json')
    args = parser.parse_args()
    out = args.out.resolve()
    if out.exists() and any(out.iterdir()):
        parser.error('Use a fresh empty output directory; no overwrite.')
    config = json.loads(args.config.read_text(encoding='utf-8'))
    assert config['ready_for_paid_submission'] is False
    panels = config['board_panels']
    pair_layout = config.get('board_layout') == 'pair'
    assert len(panels) == (2 if pair_layout else 6)
    inventory = []
    for panel in panels:
        source = ROOT / panel['repo_path']
        if sha(source) != panel['sha256']:
            parser.error(f'Source changed: {source.name}')
        with Image.open(source) as img:
            img.load()
            inventory.append({'file': source.as_posix(), 'size': list(img.size),
                              'mode': img.mode, 'sha256': sha(source)})
    canvas_height = 1130 if pair_layout else 1460
    canvas = Image.new('RGB', (1080, canvas_height), '#151a22')
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 21)
    small = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 17)
    draw.text((20, 12), config.get('board_title', '187 — KHUNG ĐẦU VÀO TĨNH / CHƯA DUYỆT / KHÔNG PHẢI VIDEO'), font=font, fill='#ffdd79')
    draw.text((20, 45), config.get('board_subtitle', 'Hàng A: gắp → trước bát → nâng. Hàng B: đổi hướng → bát Đào → đặt nem.'), font=small, fill='white')
    for i, (panel, item) in enumerate(zip(panels, inventory)):
        columns = 2 if pair_layout else 3
        panel_width = 540 if pair_layout else 360
        col, row = i % columns, i // columns
        x, y = col * panel_width, 90 + row * 650
        draw.text((x+12, y), panel['label'], font=font, fill='#ffdd79')
        draw.text((x+12, y+31), panel['status_label'], font=small, fill='white')
        with Image.open(item['file']) as source:
            thumb = ImageOps.contain(source.convert('RGB'), (516, 916) if pair_layout else (336, 585), Image.Resampling.LANCZOS)
            canvas.paste(thumb, (x+(panel_width-thumb.width)//2, y+58))
    footer_y = 1080 if pair_layout else 1408
    draw.text((20, footer_y), config.get('board_footer', 'Không nội suy giữa ảnh. Chưa kiểm FOOD, diễn động, điểm nối hoặc người nói.'), font=small, fill='#ffdd79')
    draw.text((20, footer_y+27), config.get('board_footer_second', 'A3 → B1 đổi cỡ cảnh; B1 đã giữ bát: nhịp Đào rời cốc/đưa bát còn thiếu.'), font=small, fill='white')
    out.mkdir(parents=True, exist_ok=True)
    board_name = config.get('board_name', '187_STILL_INPUTS_NOT_MOTION_v0.1.png')
    if Path(board_name).name != board_name or not board_name.endswith('.png'):
        parser.error('Board name must be a plain PNG filename.')
    board = out/board_name
    canvas.save(board)
    report = {'status': 'STILL_COMPARISON_NOT_MOTION_OR_APPROVAL', 'sources': inventory,
              'output': board.as_posix(), 'sha256': sha(board), 'size': [1080,canvas_height],
              'ready_for_paid_submission': False, 'credit_spend': 0}
    if pair_layout:
        report['credit_spend_scope'] = 'FLOW_ONLY_NO_FLOW_CALLED'
        report['image_tool_cost'] = 'NOT_ASSESSED'
    (out/'board-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False))


if __name__ == '__main__':
    main()

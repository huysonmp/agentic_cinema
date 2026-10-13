"""Owner-authorized local still composite; never edits source or active EDL.

Only configured mask pixels may change; protected chopsticks are restored from
the base. All outputs are versioned and exclusive-created (no overwrite).
"""
import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_new(image, path):
    if path.exists():
        raise FileExistsError(path)
    image.save(path)


def grid_crop(image, box):
    crop = image.crop(box).resize(((box[2]-box[0])*3, (box[3]-box[1])*3))
    draw = ImageDraw.Draw(crop)
    for x in range((box[0]//10+1)*10, box[2], 10):
        xx = (x-box[0])*3
        draw.line((xx, 0, xx, crop.height), fill=(255, 0, 255), width=1)
        draw.text((xx+1, 1), str(x), fill=(255, 255, 255), stroke_width=1, stroke_fill=(0, 0, 0))
    for y in range((box[1]//10+1)*10, box[3], 10):
        yy = (y-box[1])*3
        draw.line((0, yy, crop.width, yy), fill=(255, 0, 255), width=1)
        draw.text((1, yy+1), str(y), fill=(255, 255, 255), stroke_width=1, stroke_fill=(0, 0, 0))
    return crop


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', type=Path, required=True)
    parser.add_argument('--donor', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--config', type=Path)
    parser.add_argument('--inspect', action='store_true')
    args = parser.parse_args()
    source_hash, donor_hash = sha(args.base), sha(args.donor)
    base = Image.open(args.base).convert('RGB')
    donor = Image.open(args.donor).convert('RGB').resize(base.size, Image.Resampling.LANCZOS)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if args.inspect:
        for name, box in [('held', (185, 720, 280, 810)), ('plate', (225, 900, 580, 1090))]:
            save_new(grid_crop(base, box), args.output_dir / f'{name}_source_grid.png')
            save_new(grid_crop(donor, box), args.output_dir / f'{name}_donor_grid.png')
        return
    cfg = json.loads(args.config.read_text(encoding='utf-8-sig'))
    assert base.size == tuple(cfg['base_size'])
    assert source_hash == cfg['base_sha256'] and donor_hash == cfg['donor_sha256']
    combined = Image.new('L', base.size, 0)
    result = base.copy()
    for region in cfg['regions']:
        mask = Image.new('L', base.size, 0)
        ImageDraw.Draw(mask).polygon([tuple(p) for p in region['polygon']], fill=255)
        # Feather inward only: support never grows beyond the declared polygon.
        if region.get('feather', 0):
            mask = ImageChops.multiply(mask, mask.filter(ImageFilter.GaussianBlur(region['feather'])))
        donor_box, target_box = tuple(region['donor_box']), tuple(region['target_box'])
        patch = donor.crop(donor_box).resize((target_box[2]-target_box[0], target_box[3]-target_box[1]), Image.Resampling.LANCZOS)
        if region.get('brightness', 1) != 1:
            patch = patch.point(lambda p: min(255, round(p*region['brightness'])))
        layer = base.copy()
        if region.get('background_box'):
            # Reconstruct only the old held-food occlusion from adjacent native
            # shirt pixels; donor background is never imported into this zone.
            clear_box = tuple(region.get('clear_box', target_box))
            bg = base.crop(tuple(region['background_box'])).resize((clear_box[2]-clear_box[0], clear_box[3]-clear_box[1]), Image.Resampling.BICUBIC)
            layer.paste(bg, clear_box[:2])
            food_alpha = Image.new('L', patch.size, 0)
            alpha_pixels = []
            for r, g, b in patch.get_flattened_data():
                chroma = min(r-g-20, g-b-15)
                alpha_pixels.append(max(0, min(255, chroma*22)))
            food_alpha.putdata(alpha_pixels)
            layer.paste(patch, target_box[:2], food_alpha)
        else:
            layer.paste(patch, target_box[:2])
        result = Image.composite(layer, result, mask)
        combined = ImageChops.lighter(combined, mask)
        save_new(mask, args.output_dir / f"mask_{region['name']}.png")
    protect = Image.new('L', base.size, 0)
    for polygon in cfg.get('protected_polygons', []):
        ImageDraw.Draw(protect).polygon([tuple(p) for p in polygon], fill=255)
    result = Image.composite(base, result, protect)
    combined = ImageChops.multiply(combined, ImageOps.invert(protect))
    target = args.output_dir / cfg['output_name']
    save_new(result, target)
    save_new(combined, args.output_dir / 'EDIT_MASK.png')
    save_new(protect, args.output_dir / 'PROTECTED_MASK.png')
    # Reopen actual saved PNG; verify decoded pixels, not merely in-memory intent.
    saved = Image.open(target).convert('RGB')
    diff = ImageChops.difference(base, saved)
    maximum = ImageChops.lighter(ImageChops.lighter(*diff.split()[:2]), diff.split()[2])
    changed = maximum.point(lambda p: 255 if p else 0)
    outside = ImageChops.multiply(changed, combined.point(lambda p: 0 if p else 255))
    outside_changed = outside.histogram()[255]
    save_new(changed, args.output_dir / 'CHANGED_PIXELS.png')
    tint = Image.new('RGB', base.size, (255, 30, 150))
    save_new(Image.blend(base, Image.composite(tint, base, combined), 0.4), args.output_dir / 'MASK_OVERLAY_QC.png')
    board = Image.new('RGB', (base.width*2, base.height))
    board.paste(base, (0, 0)); board.paste(saved, (base.width, 0))
    save_new(board, args.output_dir / 'SOURCE_LEFT_COMPOSITE_RIGHT_QC.png')
    for name, box in [('held', (185, 720, 280, 810)), ('plate', (225, 900, 580, 1090))]:
        save_new(saved.crop(box).resize(((box[2]-box[0])*3, (box[3]-box[1])*3)), args.output_dir / f'{name}_composite_detail.png')
    report = {'record': 'REC291', 'base': str(args.base.resolve()), 'base_sha256': source_hash,
              'donor': str(args.donor.resolve()), 'donor_sha256': donor_hash,
              'config_sha256': sha(args.config), 'output': str(target.resolve()), 'output_sha256': sha(target),
              'size': list(saved.size), 'mask_sha256': sha(args.output_dir/'EDIT_MASK.png'),
              'outside_mask_changed_pixels': outside_changed, 'inside_changed_pixels': changed.histogram()[255],
              'scope': 'DECODED_RGB_PIXEL_INVARIANCE_NOT_VISUAL_OR_OWNER_APPROVAL',
              'inputs_unchanged': sha(args.base) == source_hash and sha(args.donor) == donor_hash}
    if outside_changed or not report['inputs_unchanged']:
        raise AssertionError(report)
    with (args.output_dir/'PIXEL_QC.json').open('x', encoding='utf-8') as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False))


if __name__ == '__main__':
    main()

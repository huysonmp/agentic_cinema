"""Bounded, owner-authorized C07 video repair from same-native closed-mouth donors.

No generated imagery, whole-face replacement, new speech or production EDL edits.
Pre-encode pixel invariance does not imply lossy output pixel equality or AV pass.
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

NATIVE_SHA = '12a0baa2d7ccedfaa16631b7cddd2c4331480e4fa8784880403eb425a8fb397b'
AUDIO_CLIP_SHA = '7a7d2bc4d4fdd7a4ec220daa67477e3063583d1b2f9366a089318b9ab1104e18'
PATCH = (180, 526, 296, 590)
REGION = (158, 490, 315, 640)
ANCHORS = (4, 15)
EDIT_RANGE = range(5, 15)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def register(anchor, target):
    """Translation measured from nearby native potato texture, excluding mouth."""
    x0, y0, x1, y1 = REGION
    px0, py0, px1, py1 = PATCH
    valid = np.ones((y1-y0, x1-x0), dtype=bool)
    valid[py0-y0-4:py1-y0+4, px0-x0-4:px1-x0+4] = False
    target_roi = target[y0:y1, x0:x1].astype(np.int16)
    choices = []
    for dy in range(-8, 9):
        for dx in range(-8, 9):
            moved = anchor[y0-dy:y1-dy, x0-dx:x1-dx].astype(np.int16)
            choices.append((float(np.mean(np.abs(moved-target_roi)[valid])), dx, dy))
    error, dx, dy = min(choices)
    if abs(dx) == 8 or abs(dy) == 8:
        raise RuntimeError('Registration at search limit; stop, do not broaden face edit.')
    return {'dx': dx, 'dy': dy, 'texture_mae': error}


def feather():
    x0, y0, x1, y1 = PATCH
    yy, xx = np.indices((y1-y0, x1-x0))
    edge = np.minimum.reduce([xx, yy, x1-x0-1-xx, y1-y0-1-yy])
    return np.clip(edge/10.0, 0, 1)[..., None]


def composite(original, left, right, index):
    result = original.copy()
    meta = {'frame': index, 'altered': index in EDIT_RANGE}
    if index in EDIT_RANGE:
        x0, y0, x1, y1 = PATCH
        moves = [register(a, original) for a in (left, right)]
        crops = [a[y0-m['dy']:y1-m['dy'], x0-m['dx']:x1-m['dx']].astype(float)
                 for a, m in zip((left, right), moves)]
        mix = (index-ANCHORS[0])/(ANCHORS[1]-ANCHORS[0])
        clean = (1-mix)*crops[0] + mix*crops[1]
        alpha = feather()
        result[y0:y1, x0:x1] = np.rint((1-alpha)*original[y0:y1, x0:x1]+alpha*clean).astype(np.uint8)
        meta.update(anchor4=moves[0], anchor15=moves[1], anchor15_weight=mix)
    changed = np.any(result != original, axis=2)
    total_changed = int(changed.sum())
    x0, y0, x1, y1 = PATCH
    changed[y0:y1, x0:x1] = False
    if changed.any():
        raise AssertionError('Pixels outside allowed mouth rectangle changed.')
    if index not in EDIT_RANGE and total_changed:
        raise AssertionError('An unapproved frame changed.')
    meta.update(changed_pixels=total_changed, outside_patch_changed_pixels=0)
    return result, meta


def packets(ffprobe, path):
    data = json.loads(subprocess.check_output([str(ffprobe), '-v', 'error',
        '-select_streams', 'a:0', '-show_packets', '-show_data_hash', 'sha256',
        '-show_entries', 'packet=pts_time,dts_time,duration_time,data_hash',
        '-of', 'json', str(path)], text=True))
    return data['packets']


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native', type=Path, required=True)
    ap.add_argument('--source-qc', type=Path, required=True)
    ap.add_argument('--approved-clip', type=Path, required=True)
    ap.add_argument('--bin', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--video-out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists() or args.video_out.exists():
        ap.error('Use new paths; never overwrite existing evidence or media.')
    if sha(args.native) != NATIVE_SHA or sha(args.approved_clip) != AUDIO_CLIP_SHA:
        ap.error('Wrong native or owner-approved exact audio clip.')
    evidence = json.loads((args.source_qc/'native_evidence.json').read_text(encoding='utf8'))
    if evidence['sha256'] != NATIVE_SHA or evidence['video_fps'] != '24':
        ap.error('Source evidence hash/fps mismatch.')
    files = sorted((args.source_qc/'all_native_frames').glob('*.png'))
    if len(files) != 96:
        ap.error('Expected exact 96-frame native evidence.')
    ff, probe = args.bin/'ffmpeg.exe', args.bin/'ffprobe.exe'
    # Decode once again into a temporary subfolder and verify actual source frames.
    args.out.mkdir(parents=True)
    fresh = args.out/'native_decode_verified'
    fresh.mkdir()
    subprocess.run([str(ff), '-nostdin', '-hide_banner', '-loglevel', 'error', '-n',
        '-i', str(args.native), '-map', '0:v:0', '-fps_mode', 'passthrough',
        str(fresh/'%05d.png')], check=True)
    fresh_files = sorted(fresh.glob('*.png'))
    if len(fresh_files) != 96 or any(sha(a) != sha(b) for a,b in zip(files,fresh_files)):
        raise AssertionError('Stored extracted frames do not match fresh native decode.')
    anchors = [np.asarray(Image.open(files[i]).convert('RGB')) for i in ANCHORS]
    outframes = args.out/'composited_frames'
    outframes.mkdir()
    rows = []
    for index, path in enumerate(files[:72]):
        original = np.asarray(Image.open(path).convert('RGB'))
        if original.shape != (1280,720,3):
            raise AssertionError('Wrong image size.')
        result, meta = composite(original, *anchors, index)
        destination = outframes/path.name
        Image.fromarray(result).save(destination)
        saved = np.asarray(Image.open(destination).convert('RGB'))
        if not np.array_equal(saved, result):
            raise AssertionError('Saved composite pixels differ.')
        rows.append(meta)
    for start in (0, 10):
        sheet = Image.new('RGB', (1100, 560), '#181818')
        draw = ImageDraw.Draw(sheet)
        for cell, index in enumerate(range(start, min(start+10,20))):
            x,y=(cell%5)*220,(cell//5)*280
            for offset,path in [(0,files[index]),(110,outframes/files[index].name)]:
                im=Image.open(path).crop((145,480,315,650)).resize((110,110))
                sheet.paste(im,(x+offset,y+24))
            draw.text((x+2,y+2),f'F{index}: native | local',fill='white')
            diff=Image.fromarray(np.abs(np.asarray(Image.open(files[index])).astype(np.int16)-
                np.asarray(Image.open(outframes/files[index].name)).astype(np.int16)).astype(np.uint8))
            diff=diff.crop((145,480,315,650)).point(lambda a:min(255,a*6)).resize((110,110))
            sheet.paste(diff,(x,y+148))
        sheet.save(args.out/f'mouth_compare_{start//10+1:02d}.png')
    # Copy AAC bitstream from the exact clip owner actually heard, no speech rewrite.
    subprocess.run([str(ff), '-nostdin', '-hide_banner', '-loglevel', 'error', '-n',
        '-framerate','24','-i',str(outframes/'%05d.png'),'-i',str(args.approved_clip),
        '-map','0:v:0','-map','1:a:0','-c:v','libx264','-crf','12','-preset','medium',
        '-pix_fmt','yuv420p','-c:a','copy','-map_metadata','-1','-movflags','+faststart',
        str(args.video_out)], check=True)
    source_audio=packets(probe,args.approved_clip)
    output_audio=packets(probe,args.video_out)
    if source_audio != output_audio:
        raise AssertionError('Approved AAC packet hashes/timing changed.')
    if sha(args.native)!=NATIVE_SHA or sha(args.approved_clip)!=AUDIO_CLIP_SHA:
        raise AssertionError('Source was changed.')
    manifest={'record':'REC307','status':'LOCAL_REPAIR_CANDIDATE_NOT_SELECTED_NOT_AV_PASS',
        'native_sha256':NATIVE_SHA,'approved_audio_clip_sha256':AUDIO_CLIP_SHA,
        'output':str(args.video_out.resolve()),'output_sha256':sha(args.video_out),
        'frame_range':'[0,72)','changed_frames_inclusive':[5,14],'donor_frames':[4,15],
        'patch_xyxy':PATCH,'registration_region_xyxy':REGION,'frames':rows,
        'fresh_decode_frames_match_stored96':True,
        'pre_encode_outside_patch_exact_unchanged':True,
        'pre_encode_unedited62_frames_exact_unchanged':True,
        'lossy_encoded_pixels_not_claimed_exact':True,
        'approved_AAC_packets_and_timing_equal':True,'audio_packet_count':len(source_audio),
        'source_unchanged':True,'Flow_submits':0,'Flow_credit_debit':0,
        'root_actual_listening':False,'lip_sync_certified':False}
    with (args.out/'repair_manifest.json').open('x',encoding='utf8') as h:
        json.dump(manifest,h,ensure_ascii=False,indent=2)
    print(json.dumps({k:manifest[k] for k in ('status','output_sha256',
        'approved_AAC_packets_and_timing_equal','pre_encode_outside_patch_exact_unchanged')}))


if __name__=='__main__':
    main()

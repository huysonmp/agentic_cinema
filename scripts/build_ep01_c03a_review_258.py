"""REC258 exact-range review derivatives; no voice or release approval."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--restart', type=Path, required=True)
p.add_argument('--bin', type=Path, required=True)
p.add_argument('--evidence', type=Path, required=True)
a = p.parse_args()
native = a.restart / '05_native/EP01_720_C03A_T01_NATIVE.mp4'
opening = a.restart / '07_edits/C01A_BM_BR_C02_13p75S_CONDITIONAL_QC_NOT_FINAL.mp4'
digest = lambda f: hashlib.sha256(f.read_bytes()).hexdigest()
assert digest(native) == '051202d30ea7317b38ee74de8a690db48510940f3311543e208f2807b56b3b0c'
assert digest(opening) == 'dd8a24d271b28796a1df28b35e5d7ac4f3e5902614cc53ca9d7886c0e3eaf12c'
cut = a.restart / '07_edits/C03A_T01_F0_41_1p75S_FOR_REVIEW.mp4'
join = a.restart / '07_edits/OPENING_C03A_15p5S_QC_NOT_FINAL.mp4'
assert not cut.exists() and not join.exists(), 'Never overwrite review targets'
ff = str(a.bin / 'ffmpeg.exe')
base = [ff, '-nostdin', '-hide_banner', '-loglevel', 'error', '-n']
encode = ['-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p',
          '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart']
subprocess.run(base + ['-i', str(native), '-filter_complex',
    '[0:v]trim=start_frame=0:end_frame=42,setpts=PTS-STARTPTS[v];'
    '[0:a]atrim=start=0:end=1.75,asetpts=PTS-STARTPTS[a]',
    '-map', '[v]', '-map', '[a]'] + encode + [str(cut)], check=True)
subprocess.run(base + ['-i', str(opening), '-i', str(cut), '-filter_complex',
    '[0:v]setpts=PTS-STARTPTS[v0];[0:a]asetpts=PTS-STARTPTS[a0];'
    '[1:v]setpts=PTS-STARTPTS[v1];[1:a]asetpts=PTS-STARTPTS[a1];'
    '[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]',
    '-map', '[v]', '-map', '[a]'] + encode + [str(join)], check=True)
reports = []
for target, expected in [(cut, 42), (join, 372)]:
    info = json.loads(subprocess.check_output([str(a.bin/'ffprobe.exe'), '-v', 'error',
        '-count_frames', '-show_streams', '-show_format', '-of', 'json', str(target)], text=True))
    video = next(s for s in info['streams'] if s['codec_type'] == 'video')
    assert int(video['nb_read_frames']) == expected
    assert (video['width'], video['height'], video['avg_frame_rate']) == (720, 1280, '24/1')
    subprocess.run(base + ['-i', str(target), '-f', 'null', 'NUL'], check=True)
    reports.append({'file': str(target.resolve()), 'sha256': digest(target),
                    'frames': expected, 'probe': info, 'full_decode_success': True})
frames = a.evidence / 'actual_join_frames'
frames.mkdir(exist_ok=False)
subprocess.run(base + ['-i', str(join), '-vf', 'select=between(n\\,324\\,371)',
    '-fps_mode', 'passthrough', str(frames/'%03d.png')], check=True)
files = sorted(frames.glob('*.png'))
assert len(files) == 48
for page, start in enumerate(range(0, 48, 12), 1):
    sheet = Image.new('RGB', (1200, 1120), '#151515')
    d = ImageDraw.Draw(sheet)
    for cell, f in enumerate(files[start:start+12]):
        im = Image.open(f).convert('RGB')
        im.thumbnail((194, 344))
        x, y = (cell % 6)*200, (cell//6)*560
        sheet.paste(im, (x, y))
        mouth = Image.open(f).convert('RGB').crop((55, 400, 350, 655))
        mouth.thumbnail((194, 165))
        sheet.paste(mouth, (x, y+348))
        idx = 324+start+cell
        d.text((x+2,y+518), f'F{idx} {idx/24:.3f}s', fill='white')
    sheet.save(a.evidence/f'actual_join_board_{page:02d}.jpg', quality=94)
report = {'record': 'REC258', 'status': 'CANDIDATE_NOT_SELECTED_OWNER_AV_PENDING',
    'native_half_open_range': [0,42], 'candidate_seconds': 1.75,
    'reason': 'Question ASR ends1.36; independent PNG review Dao closure stableF38..41; excludes Khoai slitF42 and openingF43..47. ASR eat-word ambiguous: owner must listen.',
    'new_cut': {'frame':330,'seconds':13.75}, 'joined_seconds':15.5,
    'encoded_join_review_frames': [324,372], 'outputs': reports,
    'speed_or_pitch_change': False, 'native_preserved': digest(native),
    'actual_listening': 'NOT_PERFORMED', 'lip_sync': 'NOT_CERTIFIED'}
(a.restart/'06_qc/C03A_review_derivatives_technical_258.json').write_text(
    json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

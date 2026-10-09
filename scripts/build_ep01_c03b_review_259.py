"""REC259 exact reply/reaction review, not approval of the missing glass cue."""
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
native = a.restart / '05_native/EP01_720_C03B_T01_NATIVE.mp4'
opening = a.restart / '07_edits/OPENING_C03A_15p5S_QC_NOT_FINAL.mp4'
digest = lambda f: hashlib.sha256(f.read_bytes()).hexdigest()
assert digest(native) == 'f85df55c24a267851258bc64a8d0e5579e954175a34039ed563903a89ed343a1'
assert digest(opening) == '47b779559c643770a4cd63eb7ca5c65836df408d148a9eddd8789e51a8fb343d'
cut = a.restart / '07_edits/C03B_T01_F0_49_2p083S_FOR_REVIEW.mp4'
join = a.restart / '07_edits/OPENING_C03B_17p583S_QC_NOT_FINAL.mp4'
assert not cut.exists() and not join.exists(), 'Never overwrite review targets'
ff = str(a.bin / 'ffmpeg.exe')
base = [ff, '-nostdin', '-hide_banner', '-loglevel', 'error', '-n']
encode = ['-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p',
          '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart']
subprocess.run(base + ['-i', str(native), '-filter_complex',
    '[0:v]trim=start_frame=0:end_frame=50,setpts=PTS-STARTPTS[v];'
    '[0:a]atrim=start=0:end=2.083333333333333,asetpts=PTS-STARTPTS[a]',
    '-map', '[v]', '-map', '[a]'] + encode + [str(cut)], check=True)
subprocess.run(base + ['-i', str(opening), '-i', str(cut), '-filter_complex',
    '[0:v]setpts=PTS-STARTPTS[v0];[0:a]asetpts=PTS-STARTPTS[a0];'
    '[1:v]setpts=PTS-STARTPTS[v1];[1:a]asetpts=PTS-STARTPTS[a1];'
    '[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]',
    '-map', '[v]', '-map', '[a]'] + encode + [str(join)], check=True)
reports = []
for target, expected in [(cut, 50), (join, 422)]:
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
subprocess.run(base + ['-i', str(join), '-vf', 'select=between(n\\,366\\,421)',
    '-fps_mode', 'passthrough', str(frames/'%03d.png')], check=True)
files = sorted(frames.glob('*.png'))
assert len(files) == 56
for page, start in enumerate(range(0, 56, 8), 1):
    sheet = Image.new('RGB', (1000, 1520), '#151515')
    d = ImageDraw.Draw(sheet)
    for cell, f in enumerate(files[start:start+8]):
        im = Image.open(f).convert('RGB')
        full = im.copy()
        full.thumbnail((195, 347))
        x, y = (cell % 2)*500, (cell//2)*380
        sheet.paste(full, (x, y))
        mouths = im.crop((25, 360, 705, 660))
        mouths.thumbnail((290, 145))
        sheet.paste(mouths, (x+205, y))
        hands = im.crop((25, 730, 705, 1040))
        hands.thumbnail((290, 160))
        sheet.paste(hands, (x+205, y+155))
        idx = 366+start+cell
        d.text((x+2,y+353), f'F{idx} {idx/24:.3f}s / actual encoded join', fill='white')
    sheet.save(a.evidence/f'actual_join_board_{page:02d}.jpg', quality=94)
report = {'record': 'REC259', 'status': 'CANDIDATE_NOT_SELECTED_OWNER_AV_AND_BOUNDARY_PENDING',
    'native_half_open_range': [0,50], 'candidate_seconds': 50/24,
    'reason': 'Includes whole ASR N04 ending1.24 and beginning closed-lip reaction; excludes later front-facing tail. Outer-right-glass cue NOT achieved, cannot declare C03B full pass.',
    'new_cut': {'frame':372,'seconds':15.5}, 'joined_seconds':422/24,
    'encoded_join_review_frames': [366,422], 'outputs': reports,
    'speed_or_pitch_change': False, 'native_preserved': digest(native),
    'actual_listening': 'NOT_PERFORMED', 'lip_sync': 'NOT_CERTIFIED',
    'C04': 'HOLD_FOR_OWNER_DECISION_ON_MISSING_C03B_GLASS_CUE'}
(a.restart/'06_qc/C03B_review_derivatives_technical_259.json').write_text(
    json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

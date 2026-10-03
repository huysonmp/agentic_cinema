"""Render a labelled 30s planning animatic from existing local media only."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FF = ROOT / '.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/ffmpeg.exe'
FP = FF.with_name('ffprobe.exe')
MEDIA = Path('C:/Users/PC/Downloads/du_an_nem_bui')
parser = argparse.ArgumentParser()
parser.add_argument('--out', type=Path, default=MEDIA / '166_completion_animatic')
parser.add_argument('--reaction', type=Path)
parser.add_argument('--reaction-in', type=float, default=0)
parser.add_argument('--voice-owner-approved', action='store_true')
parser.add_argument('--version', choices=['v0.1', 'v0.2'], default='v0.1')
opts = parser.parse_args()
OUT = opts.out
if OUT.exists() and any(OUT.iterdir()):
    parser.error('Output folder must be empty; preserve existing renders and manifests.')
if opts.reaction_in < 0:
    parser.error('--reaction-in must be non-negative.')
if opts.reaction:
    if not opts.reaction.is_file():
        parser.error('Reaction input file does not exist.')
    duration = float(subprocess.check_output([
        str(FP), '-v', 'error', '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1', str(opts.reaction),
    ], text=True))
    if opts.reaction_in + 2 > duration:
        parser.error('Reaction selection must contain a full two seconds.')
OUT.mkdir(parents=True, exist_ok=True)
MASTER = OUT / f'EP01_30s_PLANNING_{opts.version}.mp4'
OPEN = MEDIA / 'T2-CODEX-OPEN_v0.7.png'
START = MEDIA / '161_source_retest/START_short_tuft_v0.1.png'
END = MEDIA / '163_low-hold-reaction/END_low_reaction_v0.1.png'
C01 = MEDIA / '159_closeup_pickup/C01.mp4'
VOICE = MEDIA / '154_visual_lock/R01.mp4'


def run(args):
    subprocess.run([str(FF), '-hide_banner', '-loglevel', 'error', '-n', *args], check=True)


def escaped(path):
    return path.as_posix().replace(':', r'\:')


shots = [
    ('S01', 0, 6.5, OPEN, None, 'ẢNH TẠM: mở bàn ăn / chưa có giọng'),
    ('S02', 6.5, 7, OPEN, None, 'ẢNH TẠM: ký ức / chưa có giọng'),
    ('S03', 13.5, 2.5, OPEN, None, 'ẢNH TẠM: đối đáp / chưa có giọng'),
    ('S04', 16, 1.5, OPEN, None, 'THIẾU CẢNH: Đào quay lấy cốc'),
    ('S05', 17.5, 2.5, C01, 2.75, 'VIDEO C01: gắp / nối cảnh chưa duyệt'),
    ('S06', 20, 2, START, None, 'ẢNH TẠM: giữ nem / thiếu nâng-khựng'),
    ('S07', 22, 2.6, END, None, 'ẢNH TẠM: bắt gặp / audio chưa duyệt'),
    ('S08', 24.6, 2.4, END, None, 'THIẾU CẢNH: chuyển nem vào bát Đào'),
    ('S09', 27, 3, OPEN, None, 'THIẾU CẢNH: nhận món / gắp miếng khác'),
]
if opts.reaction:
    shots[5] = ('S06', 20, 2, opts.reaction, opts.reaction_in, 'THỬ PHẢN ỨNG: vẫn thiếu nâng-khựng')
if opts.voice_owner_approved:
    shots[6] = ('S07', 22, 2.6, END, None, 'ẢNH TẠM: audio owner duyệt tái dùng')
captions = [
    (0, 3, 'Đào: Anh nhìn mãi.\nKhông hợp thì để em.'),
    (3, 6.5, 'Khoai: Khoan. Mùi này\nlàm anh nhớ cái chảo.'),
    (6.5, 9, 'Đào: Nem thì đây. Chảo ở đâu?'),
    (9, 13.5, 'Khoai: Bếp nhà anh, hồi bé.\nMẹ rang gạo, anh đứng chờ.'),
    (13.5, 14.5, 'Đào: Chờ ăn?'),
    (14.5, 16, 'Khoai: Chờ mẹ quay lưng.'),
    (22, 23.9, 'Đào: Chờ em quay lưng nữa à?'),
    (24.62, 26.46, 'Khoai: Anh gắp cho em mà.'),
    (26.74, 28.5, 'Đào: Thế em quay lại đúng lúc rồi.'),
]
font = escaped(Path('C:/Windows/Fonts/arial.ttf'))
base = 'scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24'
draft = OUT / 'draft-label.txt'
draft.write_text('BẢN NHÁP 30s — KHÔNG PHẢI BẢN BÀN GIAO', encoding='utf-8')
parts = []
manifest = []
for name, begin, duration, source, seek, label in shots:
    labelpath = OUT / f'{name}-label.txt'
    labelpath.write_text(label, encoding='utf-8')
    vf = base + ',drawbox=x=0:y=0:w=iw:h=115:color=black@0.8:t=fill'
    vf += f",drawtext=fontfile='{font}':textfile='{escaped(draft)}':fontsize=24:fontcolor=yellow:x=(w-text_w)/2:y=20"
    vf += f",drawtext=fontfile='{font}':textfile='{escaped(labelpath)}':fontsize=23:fontcolor=white:x=(w-text_w)/2:y=67"
    vf += ',drawbox=x=0:y=1080:w=iw:h=200:color=black@0.8:t=fill'
    for i, (start, end, text) in enumerate(captions):
        lo, hi = max(start, begin), min(end, begin + duration)
        if hi <= lo:
            continue
        textpath = OUT / f'{name}-caption-{i}.txt'
        textpath.write_text(text, encoding='utf-8')
        vf += f",drawtext=fontfile='{font}':textfile='{escaped(textpath)}':fontsize=29:fontcolor=white:line_spacing=10:x=(w-text_w)/2:y=1140:enable='gte(t,{lo-begin})*lt(t,{hi-begin})'"
    target = OUT / f'{name}.mp4'
    args = ['-loop', '1', '-i', str(source)] if seek is None else ['-ss', str(seek), '-i', str(source)]
    run([*args, '-t', str(duration), '-vf', vf, '-an', '-c:v', 'libx264', '-preset', 'fast', '-crf', '20', '-pix_fmt', 'yuv420p', str(target)])
    parts.append(target)
    manifest.append({'shot': name, 'timeline_in': begin, 'timeline_out': begin+duration, 'source': str(source), 'source_in': seek, 'source_out': None if seek is None else seek+duration, 'status': label, 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest()})

concat = OUT / 'concat.txt'
concat.write_text('\n'.join("file '" + p.as_posix() + "'" for p in parts), encoding='utf-8')
run(['-f', 'concat', '-safe', '0', '-i', str(concat), '-i', str(VOICE), '-filter_complex', '[1:a]atrim=0:8,asetpts=PTS-STARTPTS,adelay=22000:all=1,apad=whole_dur=30[a]', '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', '30', '-movflags', '+faststart', str(MASTER)])
voice_suffix = 'OWNER_REUSE_APPROVED' if opts.voice_owner_approved else 'UNAPPROVED'
run(['-i', str(VOICE), '-vn', '-c:a', 'pcm_s16le', str(OUT/f'closing_voice_R01_{voice_suffix}.wav')])
for sample in ('R02', 'R03'):
    run(['-i', str(VOICE.with_name(sample+'.mp4')), '-vn', '-c:a', 'pcm_s16le', str(OUT/f'closing_voice_{sample}_UNAPPROVED.wav')])
run(['-i', str(MASTER), '-vf', 'fps=1/2,scale=180:320,tile=5x3', '-frames:v', '1', str(OUT/'animatic-contact.png')])
run(['-i', str(MASTER), '-f', 'null', 'NUL'])
metadata = json.loads(subprocess.check_output([str(FP), '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(MASTER)], text=True))
report = {'status': 'PLANNING_NOT_DELIVERY', 'local_render_credit_spend': 0, 'voice_status': 'OWNER_REUSE_APPROVED_NOT_INDEPENDENT_EAR_QC' if opts.voice_owner_approved else 'UNAPPROVED_NO_ACCENT_OR_IDENTITY_VERIFICATION', 'silent_until_seconds': 22, 'shots': manifest, 'captions': captions, 'output_metadata': metadata}
(OUT/'manifest.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'output': str(MASTER), 'duration': metadata['format']['duration'], 'bytes': metadata['format']['size'], 'shots': len(manifest)}, ensure_ascii=False))

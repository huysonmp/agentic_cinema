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
parser.add_argument('--version', choices=['v0.1', 'v0.2', 'v0.3'], default='v0.1')
parser.add_argument('--middle-voice', type=Path)
parser.add_argument('--middle-voice-test-accepted', action='store_true')
opts = parser.parse_args()
OUT = opts.out
if OUT.exists() and any(OUT.iterdir()):
    parser.error('Output folder must be empty; preserve existing renders and manifests.')
if opts.reaction_in < 0:
    parser.error('--reaction-in must be non-negative.')
if opts.version == 'v0.3':
    if not opts.middle_voice or not opts.middle_voice_test_accepted or not opts.voice_owner_approved:
        parser.error('v0.3 requires an accepted middle voice test and approved closing audio reuse.')
    if not opts.middle_voice.is_file():
        parser.error('Middle voice input file does not exist.')
    if hashlib.sha256(opts.middle_voice.read_bytes()).hexdigest() != '3861280b335e1f8c9249dd484cd63a8432f5a89c2c15dca5a81c3764b1ec0d5e':
        parser.error('v0.3 planning input must be the recorded batch175 B01 PCM WAV.')
elif opts.middle_voice or opts.middle_voice_test_accepted:
    parser.error('Middle voice integration is only implemented for v0.3.')
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
if opts.version == 'v0.3':
    shots[:3] = [
        ('S01', 0, 6, OPEN, None, 'ẢNH TẠM: hai câu mở chưa có audio đạt'),
        ('S02', 6, 7, OPEN, None, 'ẢNH TẠM: audio bộ test giọng đã chấp nhận'),
        ('S03', 13, 3, OPEN, None, 'ẢNH TẠM: đối đáp / chưa có cảnh diễn'),
    ]
    captions[:6] = [
        (0, 3, 'Đào: Anh nhìn mãi.\nKhông hợp thì để em.'),
        (3, 6, 'Khoai: Khoan. Mùi này\nlàm anh nhớ cái chảo.'),
        (6, 8, 'Đào: Nem thì đây. Chảo ở đâu?'),
        (8.46, 12.22, 'Khoai: Bếp nhà anh, hồi bé.\nMẹ rang gạo, anh đứng chờ.'),
        (12.82, 13.54, 'Đào: Chờ ăn?'),
        (14.18, 15.08, 'Khoai: Chờ mẹ quay lưng.'),
    ]
    captions[7] = (24.62, 25.84, 'Khoai: Anh gắp cho em mà.')
    captions[8] = (26.74, 28.34, 'Đào: Thế em quay lại đúng lúc rồi.')
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
audio_inputs = ['-i', str(VOICE)]
audio_filter = '[1:a]atrim=0:8,asetpts=PTS-STARTPTS,adelay=22000:all=1,apad=whole_dur=30[a]'
if opts.version == 'v0.3':
    audio_inputs += ['-i', str(opts.middle_voice)]
    audio_filter = ('[1:a]atrim=0:8,asetpts=PTS-STARTPTS,adelay=22000:all=1,apad=whole_dur=30[closing];'
                    '[2:a]atrim=0:10,asetpts=PTS-STARTPTS,adelay=6000:all=1,apad=whole_dur=30[middle];'
                    '[middle][closing]amix=inputs=2:duration=longest:normalize=0[a]')
run(['-f', 'concat', '-safe', '0', '-i', str(concat), *audio_inputs, '-filter_complex', audio_filter, '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', '30', '-movflags', '+faststart', str(MASTER)])
voice_suffix = 'OWNER_REUSE_APPROVED' if opts.voice_owner_approved else 'UNAPPROVED'
run(['-i', str(VOICE), '-vn', '-c:a', 'pcm_s16le', str(OUT/f'closing_voice_R01_{voice_suffix}.wav')])
for sample in ('R02', 'R03'):
    run(['-i', str(VOICE.with_name(sample+'.mp4')), '-vn', '-c:a', 'pcm_s16le', str(OUT/f'closing_voice_{sample}_UNAPPROVED.wav')])
run(['-i', str(MASTER), '-vf', 'fps=1/2,scale=180:320,tile=5x3', '-frames:v', '1', str(OUT/'animatic-contact.png')])
run(['-i', str(MASTER), '-f', 'null', 'NUL'])
metadata = json.loads(subprocess.check_output([str(FP), '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(MASTER)], text=True))
report = {'status': 'PLANNING_NOT_DELIVERY', 'local_render_credit_spend': 0, 'voice_status': 'OWNER_REUSE_APPROVED_NOT_INDEPENDENT_EAR_QC' if opts.voice_owner_approved else 'UNAPPROVED_NO_ACCENT_OR_IDENTITY_VERIFICATION', 'silent_until_seconds': 22, 'shots': manifest, 'captions': captions, 'output_metadata': metadata}
if opts.version == 'v0.3':
    report.update({
        'voice_status': 'MIDDLE_OWNER_TEST_ACCEPTED_CLOSING_OWNER_REUSE_APPROVED',
        'silent_until_seconds': 6,
        'audio_slots': [
            {'timeline_in': 0, 'timeline_out': 6, 'lines': ['L01', 'L02'], 'status': 'MISSING_APPROVED_AUDIO'},
            {'timeline_in': 6, 'timeline_out': 16, 'source': str(opts.middle_voice), 'source_sha256': hashlib.sha256(opts.middle_voice.read_bytes()).hexdigest(), 'source_in': 0, 'source_out': 10, 'lines': ['L03', 'L04', 'L05', 'L06'], 'status': 'OWNER_TEST_ACCEPTED_B01_WORKING_CHOICE_NOT_OWNER_WINNER'},
            {'timeline_in': 22, 'timeline_out': 30, 'source': str(VOICE), 'source_sha256': hashlib.sha256(VOICE.read_bytes()).hexdigest(), 'source_in': 0, 'source_out': 8, 'lines': ['L07', 'L08', 'L09'], 'status': 'OWNER_REUSE_APPROVED_168'},
        ],
        'caption_timing_basis': 'Local ASR timing hints; text from approved script32, not an exact pronunciation or speaker verdict.',
        'independent_ear_qc': 'NOT_PERFORMED',
        'release_overlays': 'F01/F02/AI labels still required for final delivery; this is a labelled internal planning cut.',
    })
(OUT/'manifest.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'output': str(MASTER), 'duration': metadata['format']['duration'], 'bytes': metadata['format']['size'], 'shots': len(manifest)}, ensure_ascii=False))

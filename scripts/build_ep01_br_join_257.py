"""REC257 conditional review render only; does not select BR or approve film."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--base', type=Path, required=True)
p.add_argument('--bin', type=Path, required=True)
p.add_argument('--evidence', type=Path, required=True)
a = p.parse_args()
ff = str(a.bin / 'ffmpeg.exe')
sources = [
    ('07_edits/C01A_BM_4p125S_JOIN_QC_NOT_FINAL.mp4', '4cb1b2d7c94081ec1c301eec57f9fdfcb7d08bceb40ada089f081991ed030510'),
    ('07_edits/C01B_BR_T01_SILENT_DERIVED_NOT_SELECTED.mp4', None),
    ('07_edits/C02_T02_FLOW_0_7p5S_FOR_APPROVAL.mp4', 'd151eb1d9f5f5b4486fed030579d9da3de0d23f434a65db2f6c4dca88b3228f3'),
]
records = []
for rel, expected in sources:
    sha = hashlib.sha256((a.base / rel).read_bytes()).hexdigest()
    assert expected is None or sha == expected, f'Source hash mismatch: {rel}'
    records.append({'path': rel, 'sha256': sha})

br = a.base / '07_edits/C01B_BR_T01_F28_77_SILENT_CONDITIONAL_REVIEW.mp4'
subprocess.run([ff, '-nostdin', '-hide_banner', '-loglevel', 'error', '-n',
                '-i', str(a.base / sources[1][0]), '-vf',
                'trim=start_frame=28:end_frame=78,setpts=PTS-STARTPTS',
                '-an', '-c:v', 'libx264', '-crf', '16', '-preset', 'medium',
                '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(br)], check=True)

out = a.base / '07_edits/C01A_BM_BR_C02_13p75S_CONDITIONAL_QC_NOT_FINAL.mp4'
graph = (
    '[0:v]trim=end_frame=99,setpts=PTS-STARTPTS[v0];'
    '[1:v]trim=start_frame=28:end_frame=78,setpts=PTS-STARTPTS[v1];'
    '[2:v]trim=end_frame=181,setpts=PTS-STARTPTS[v2];'
    '[v0][v1][v2]concat=n=3:v=1:a=0[v];'
    '[0:a]aresample=48000,apad,atrim=end_sample=198000,asetpts=PTS-STARTPTS[a0];'
    'anullsrc=r=48000:cl=stereo,atrim=end_sample=100000,asetpts=PTS-STARTPTS[a1];'
    '[2:a]aresample=48000,apad,atrim=end_sample=362000,asetpts=PTS-STARTPTS[a2];'
    '[a0][a1][a2]concat=n=3:v=0:a=1[a]'
)
cmd = [ff, '-nostdin', '-hide_banner', '-loglevel', 'error', '-n']
for rel, _ in sources:
    cmd += ['-i', str(a.base / rel)]
cmd += ['-filter_complex', graph, '-map', '[v]', '-map', '[a]',
        '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', '-pix_fmt', 'yuv420p',
        '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-movflags', '+faststart', str(out)]
subprocess.run(cmd, check=True)
for item in records:
    assert item['sha256'] == hashlib.sha256((a.base / item['path']).read_bytes()).hexdigest()
report = {
    'record': 'REC257', 'status': 'CONDITIONAL_REVIEW_NOT_SELECTED_NOT_DELIVERY',
    'sources': records, 'BR_native_range_half_open': [28, 78],
    'BR_trim_sha256': hashlib.sha256(br.read_bytes()).hexdigest(),
    'target_path': str(out.resolve()), 'target_sha256': hashlib.sha256(out.read_bytes()).hexdigest(),
    'expected_frames': 330, 'expected_seconds': 13.75,
    'cuts_zero_based': [81, 99, 149], 'cuts_seconds': [3.375, 4.125, 149/24],
    'source_order': ['A 81 frames', 'BM 18 frames', 'BR 50 frames', 'C02 181 frames'],
    'audio': 'Accepted A-BM source then 100000 stereo silence sample frames then accepted C02; pad source audio to image duration; no new voice/gain/speed/crossfade; encoded AAC not bit-exact',
    'open_blocker': 'BR enters with apparent two-rim contact; native inner renewed reach omitted, not corrected. Requires owner exception and actual joins AV checkpoint.',
    'full_AV_actual_listening': 'NOT_PERFORMED', 'whole_film': False,
    'ffmpeg_command': cmd,
}
a.evidence.mkdir(exist_ok=True)
(a.evidence / 'conditional_edl.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf8')
print(json.dumps({k: report[k] for k in ['status', 'target_sha256', 'BR_trim_sha256', 'expected_frames', 'expected_seconds']}))

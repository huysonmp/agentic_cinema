"""Check planning-cut provenance and structure; not an ear or performance review."""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/32_p5-script-c-v0.5-approved-content.md'
FF = ROOT / '.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/ffmpeg.exe'
parser = argparse.ArgumentParser()
parser.add_argument('folder', type=Path)
opts = parser.parse_args()
manifest = json.loads((opts.folder / 'manifest.json').read_text(encoding='utf-8'))
master = opts.folder / 'EP01_30s_PLANNING_v0.3.mp4'
expected = re.findall(r'\*\*(Đào|Khoai):\*\* “([^”]+)”', SCRIPT.read_text(encoding='utf-8'))
actual = [tuple(c[2].replace('\n', ' ').split(': ', 1)) for c in manifest['captions']]
assert len(expected) == 9 and actual == expected, 'Captions differ from approved script32.'
shots = manifest['shots']
assert shots[0]['timeline_in'] == 0 and shots[-1]['timeline_out'] == 30
assert all(a['timeline_out'] == b['timeline_in'] for a, b in zip(shots, shots[1:])), 'Shot timeline is not contiguous.'
for shot in shots:
    assert hashlib.sha256(Path(shot['source']).read_bytes()).hexdigest() == shot['source_sha256']
slots = manifest['audio_slots']
assert [(s['timeline_in'], s['timeline_out']) for s in slots] == [(0, 6), (6, 16), (22, 30)]
for slot in slots[1:]:
    assert hashlib.sha256(Path(slot['source']).read_bytes()).hexdigest() == slot['source_sha256']
metadata = json.loads(subprocess.check_output([str(FF.with_name('ffprobe.exe')), '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(master)], text=True))
video = next(s for s in metadata['streams'] if s['codec_type'] == 'video')
assert (video['width'], video['height'], video['r_frame_rate']) == (720, 1280, '24/1')
assert float(metadata['format']['duration']) == 30
assert any(s['codec_type'] == 'audio' for s in metadata['streams'])
subprocess.run([str(FF), '-v', 'error', '-i', str(master), '-f', 'null', 'NUL'], check=True)
# Verify the missing opening audio is truly silent, not an old rejected voice.
pcm = subprocess.check_output([str(FF), '-v', 'error', '-i', str(master), '-t', '5.9', '-vn', '-f', 's16le', '-acodec', 'pcm_s16le', '-'])
assert not any(pcm), 'Opening placeholder unexpectedly has audio.'
report = {
    'status': 'TECHNICAL_AND_PROVENANCE_PASS_NOT_FINAL_QC',
    'script32_exact_captions': 9,
    'contiguous_timeline_seconds': 30,
    'dimensions': [720, 1280], 'fps': 24,
    'full_decode': 'PASS', 'opening_silence': 'PASS', 'input_hashes': 'PASS',
    'master_sha256': hashlib.sha256(master.read_bytes()).hexdigest(),
    'master_bytes': master.stat().st_size,
    'independent_ear_review': 'NOT_PERFORMED',
    'performance_and_lip_sync': 'NOT_APPROVED',
    'still_placeholder_seconds': sum(s['timeline_out'] - s['timeline_in'] for s in shots if s['source_in'] is None),
    'release_overlays': 'NOT_IMPLEMENTED_IN_INTERNAL_PLANNING_CUT',
}
(opts.folder / 'technical-qc.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False))

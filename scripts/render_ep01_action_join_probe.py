"""Render a silent, labelled action-join probe; never a production/final cut."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MEDIA = Path('C:/Users/PC/Downloads/du_an_nem_bui')
FF = ROOT / '.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/ffmpeg.exe'
FP = FF.with_name('ffprobe.exe')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def escaped(path):
    return path.as_posix().replace(':', r'\:')


def probe(path):
    return json.loads(subprocess.check_output(
        [str(FP), '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(path)],
        text=True, encoding='utf-8'))


def run(args):
    subprocess.run([str(FF), '-nostdin', '-hide_banner', '-loglevel', 'error', '-n', *args], check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    out = args.out.resolve()
    if out.exists() and any(out.iterdir()):
        parser.error('Use a fresh empty render directory; existing files are preserved.')
    pickup = MEDIA / '159_closeup_pickup/C01.mp4'
    lift = MEDIA / '185_split_motion/V02_0.00-1.75_SILENT_CANDIDATE.mp4'
    expected = {
        pickup: 'b574b2fd21b2a959ccd73901873fefbd217e4e5049310ae84c77d5e6641e7dd1',
        lift: '08b202df0b4776527f35dc398f40b0c9832316c985b8f4cff7f2a84101c51eb6',
    }
    for source, digest in expected.items():
        if sha(source) != digest:
            parser.error(f'Source changed: {source.name}')
    specs = [
        ('S01', 1.25, 'STILL', MEDIA/'185_split_motion/START_Dao_reaction_v0.2.png', None,
         'ẢNH TẠM: Đào ở cốc / thiếu động tác'),
        ('S02', 2.5, 'VIDEO_CANDIDATE', pickup, 2.75,
         'C01: gắp / chưa duyệt điểm nối'),
        ('S03', .75, 'MISSING_BRIDGE_CARD', None, None,
         'THIẾU: từ đĩa chung về bát Khoai'),
        ('S04', 1.75, 'VIDEO_CANDIDATE', lift, 0,
         'V02: nâng ngắn / chưa duyệt nối'),
        ('S05', 1.25, 'STILL', MEDIA/'185_split_motion/END_Dao_reaction_v0.2.png', None,
         'ẢNH TẠM: bắt gặp / chưa có chuyển động'),
        ('S06', .5, 'STILL', MEDIA/'186_continuity_planning/H185_out_1.708.png', None,
         'ẢNH TẠM: tay khựng / chưa duyệt diễn'),
    ]
    assert sum(s[1] for s in specs) == 8
    for _, duration, kind, source, seek, _ in specs:
        if source and not source.is_file():
            parser.error(f'Missing source: {source}')
        if kind == 'VIDEO_CANDIDATE':
            assert seek + duration <= float(probe(source)['format']['duration']) + 1e-6
    out.mkdir(parents=True, exist_ok=True)
    banner = out/'banner.txt'
    banner.write_text('NHÁP KIỂM NỐI — CHƯA DUYỆT', encoding='utf-8')
    font = escaped(Path('C:/Windows/Fonts/arial.ttf'))
    parts, shots = [], []
    timeline = 0
    for name, duration, kind, source, seek, label in specs:
        label_file = out/f'{name}-label.txt'
        label_file.write_text(label, encoding='utf-8')
        if source is None:
            inputs = ['-f', 'lavfi', '-i', 'color=c=black:s=720x1280:r=24']
        elif kind == 'STILL':
            inputs = ['-loop', '1', '-i', str(source)]
        else:
            inputs = ['-ss', str(seek), '-i', str(source)]
        # Put the full source below the label band; do not hide grip or watermark.
        vf = 'scale=720:1152:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:128,setsar=1,fps=24'
        vf += ',drawbox=x=0:y=0:w=iw:h=115:color=black@0.85:t=fill'
        vf += f",drawtext=fontfile='{font}':textfile='{escaped(banner)}':fontsize=27:fontcolor=yellow:x=(w-text_w)/2:y=20"
        vf += f",drawtext=fontfile='{font}':textfile='{escaped(label_file)}':fontsize=24:fontcolor=white:x=(w-text_w)/2:y=67"
        if source is None:
            vf += f",drawtext=fontfile='{font}':textfile='{escaped(label_file)}':fontsize=30:fontcolor=yellow:x=(w-text_w)/2:y=(h-text_h)/2"
        target = out/f'{name}.mp4'
        run([*inputs, '-t', str(duration), '-vf', vf, '-an', '-c:v', 'libx264',
             '-preset', 'fast', '-crf', '20', '-pix_fmt', 'yuv420p', str(target)])
        parts.append(target)
        shots.append({'shot': name, 'type': kind, 'timeline_in': timeline,
                      'timeline_out': timeline+duration, 'source': source.as_posix() if source else None,
                      'source_in': seek, 'source_out': seek+duration if seek is not None else None,
                      'source_sha256': sha(source) if source else None, 'label': label,
                      'approval': 'NOT_APPROVED'})
        timeline += duration
    concat = out/'concat.txt'
    concat.write_text('\n'.join("file '"+p.as_posix()+"'" for p in parts), encoding='utf-8')
    result = out/'EP01_ACTION_JOIN_8s_PLANNING_v0.2.mp4'
    run(['-f', 'concat', '-safe', '0', '-i', str(concat), '-map', '0:v:0', '-an',
         '-c:v', 'copy', '-movflags', '+faststart', str(result)])
    metadata = probe(result)
    assert len(metadata['streams']) == 1
    video = metadata['streams'][0]
    assert (video['width'], video['height'], video['r_frame_rate'], video['nb_frames']) == (720,1280,'24/1','192')
    assert float(metadata['format']['duration']) == 8
    run(['-i', str(result), '-f', 'null', 'NUL'])
    run(['-i', str(result), '-vf', 'fps=2,scale=180:320,tile=4x4', '-frames:v', '1', str(out/'contact.png')])
    manifest = {'status': 'JOIN_PROBE_NOT_DELIVERY', 'probe_version': 'v0.2', 'script_version': 'C-v0.6',
                'silent': True, 'audio_streams': 0, 'speaker_gate': 'HOLD_DEFERRED_NOT_APPROVED',
                'source_audio_used': False, 'credit_spend': 0, 'project_credit_remaining': 23,
                'shots': shots, 'still_placeholder_seconds': 3.0, 'missing_bridge_card_seconds': .75,
                'video_candidate_seconds': 4.25, 'coverage_approval': 'NOT_APPROVED',
                'performance_lipsync_continuity': 'NOT_APPROVED', 'speed_change': False,
                'source_files_preserved': True, 'full_source_visible_below_label_band': True,
                'technical': 'DECODE_AND_TIMELINE_PASS_NOT_CREATIVE_PASS',
                'output': result.as_posix(), 'sha256': sha(result), 'bytes': result.stat().st_size,
                'metadata': metadata}
    (out/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'output': result.as_posix(), 'duration':8, 'sha256':sha(result),
                      'status':manifest['status']}, ensure_ascii=False))


if __name__ == '__main__':
    main()

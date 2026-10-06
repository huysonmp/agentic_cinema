"""Finish the hash-bound owner-approved cut locally; never publishes or approves release."""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EP = ROOT / 'he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot'
BASE = Path('C:/Users/PC/Downloads/du_an_nem_bui/209_full_AV_review')
FF = ROOT / '.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/ffmpeg.exe'
FP = FF.with_name('ffprobe.exe')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def srt_time(seconds):
    ms = round(seconds * 1000)
    hour, ms = divmod(ms, 3600000)
    minute, ms = divmod(ms, 60000)
    second, ms = divmod(ms, 1000)
    return f'{hour:02}:{minute:02}:{second:02},{ms:03}'


def validate_cues(cues, package):
    assert all(0 <= c['start'] < c['end'] <= 30 for c in cues)
    assert all(a['end'] <= b['start'] for a, b in zip(cues, cues[1:]))
    for line in package['lines']:
        selected = [c for c in cues if c['line_id'] == line['id']]
        assert selected and all(c['speaker'] == line['speaker'] for c in selected)
        assert ' '.join(c['text'].replace('\n', ' ') for c in selected) == line['text']
    assert list(dict.fromkeys(c['line_id'] for c in cues)) == [l['id'] for l in package['lines']]


def captions(package, n02_asr, whole_asr):
    lines = {l['id']: l for l in package['lines']}
    n02_words = [w for s in n02_asr['segments'] for w in s['words']]
    assert len(n02_words) == 18
    # ASR is a timing hint only. Source-bound identity and script supply speaker/text.
    specs = [('N01', 0, 2.10, lines['N01']['caption']),
             ('N02', 2.15, 3.05, 'Khoan.'),
             ('N02', 2.15 + n02_words[1]['start'], 2.15 + n02_words[9]['end'] + 0.15,
              'Mùi này làm anh nhớ\nđến bếp nhà anh.'),
             ('N02', 2.15 + n02_words[10]['start'], 2.15 + n02_words[14]['end'] + 0.15,
              'Hồi bé, mẹ rang gạo,'),
             ('N02', 2.15 + n02_words[15]['start'], 12.10, 'anh đứng chờ.'),
             ('N03', 12.155, 13.025, lines['N03']['caption']),
             ('N04', 13.025, 14.10, lines['N04']['caption'])]
    shift = 21.958333333333332 - 14.055
    for line_id, seg in zip(['N05', 'N06', 'N07'], whole_asr['segments'][-3:]):
        specs.append((line_id, seg['start'] + shift, seg['end'] + shift + 0.18,
                      lines[line_id]['caption']))
    cues = [{'line_id': i, 'speaker': lines[i]['speaker'], 'start': round(a, 3),
             'end': round(b, 3), 'text': text} for i, a, b, text in specs]
    validate_cues(cues, package)
    return cues


def measure(path):
    result = subprocess.run([str(FF), '-nostdin', '-hide_banner', '-i', str(path), '-vn',
                             '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json',
                             '-f', 'null', 'NUL'], check=True, capture_output=True, text=True)
    payload = json.loads(re.findall(r'\{[^{}]+"input_i"[^{}]+\}', result.stderr, re.S)[-1])
    return {'integrated_lufs': float(payload['input_i']), 'true_peak_dbtp': float(payload['input_tp']),
            'loudness_range_lu': float(payload['input_lra'])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    opts = parser.parse_args()
    if opts.out.exists():
        parser.error('Use a fresh output folder; approved cut and earlier versions stay intact.')
    approval = json.loads((EP/'evidence/210/owner-approval.json').read_text(encoding='utf-8'))
    approved = Path(approval['approved_artifact'])
    assert sha(approved) == approval['approved_artifact_sha256']
    package = json.loads((EP/'evidence/179/dialogue-package.json').read_text(encoding='utf-8'))
    cues = captions(package,
                    json.loads((EP/'evidence/201/asr.json').read_text(encoding='utf-8')),
                    json.loads((EP/'evidence/202/asr.json').read_text(encoding='utf-8')))
    pcm = BASE / 'EP01_EXACT_APPROVED_PCM_30S.wav'
    before = measure(pcm)
    # Uniform gain keeps approved performance/dynamics, rather than re-voicing or compressing.
    gain = round(min(0.0, -16.0 - before['integrated_lufs'], -1.5 - before['true_peak_dbtp']), 2)
    opts.out.mkdir(parents=True)
    assets = opts.out/'editable_assets'
    assets.mkdir()
    shutil.copy2(pcm, assets/pcm.name)
    for part in sorted(BASE.glob('S*.mp4')):
        shutil.copy2(part, assets/part.name)
    shutil.copy2(EP/'evidence/209/timeline-v0.5.json', assets/'original-source-timeline.json')
    shutil.copy2(EP/'evidence/210/owner-approval.json', assets/'owner-approval.json')
    srt = '\n\n'.join(f"{i}\n{srt_time(c['start'])} --> {srt_time(c['end'])}\n{c['text']}"
                        for i,c in enumerate(cues, 1)) + '\n'
    (opts.out/'EP01_C-v0.6_vi.srt').write_text(srt, encoding='utf-8', newline='\n')
    overlays = [{'id':'F01', 'start':0, 'end':4.167, 'text':'Nem Bùi — gắn với\nBùi Xá, Bắc Ninh.'},
                {'id':'F02', 'start':5.2, 'end':9.7,
                 'text':'Thính gạo rang góp một phần\nvào mùi vị của Nem Bùi.'},
                {'id':'AI','start':0,'end':30,'text':'Video được tạo bằng AI.'}]
    for overlay, expected in zip(overlays, package['release_text']):
        assert overlay['id'] == expected['id']
        assert overlay['text'].replace('\n',' ') == expected['text']
    font = 'C\\:/Windows/Fonts/arialbd.ttf'
    vf = 'setsar=1'
    for index, cue in enumerate(cues + overlays):
        textfile = assets/f'cue-{index:02}.txt'
        textfile.write_text(cue['text'], encoding='utf-8', newline='\n')
        escaped = textfile.as_posix().replace(':', r'\:')
        is_fact, is_ai = cue.get('id') in ('F01','F02'), cue.get('id') == 'AI'
        size = 24 if is_fact else 18 if is_ai else 29
        y = 154 if is_fact else 110 if is_ai else 990
        x = '54' if is_fact or is_ai else '(w-text_w)/2-20'
        vf += (f",drawtext=fontfile='{font}':textfile='{escaped}':fontsize={size}:fontcolor=white:"
               f"box=1:boxcolor=black@0.65:boxborderw=9:line_spacing=8:x={x}:y={y}:"
               f"enable='gte(t,{cue['start']})*lt(t,{cue['end']})'")

    def run(args):
        subprocess.run([str(FF), '-nostdin', '-hide_banner', '-loglevel', 'error', '-n', *args], check=True)

    mixed = assets/'EP01_DIALOGUE_STATIC_GAIN_30S.wav'
    run(['-i', str(pcm), '-af', f'volume={gain}dB', '-c:a', 'pcm_s16le', str(mixed)])
    clean = opts.out/'EP01_30S_CLEAN_v1.1.mp4'
    run(['-i', str(BASE/'EP01_30S_PICTURE_REVIEW_NOT_FINAL.mp4'), '-i', str(mixed),
         '-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k',
         '-movflags','+faststart',str(clean)])
    final = opts.out/'EP01_30S_SUBTITLED_v1.1_FOR_APPROVAL.mp4'
    run(['-i', str(BASE/'EP01_30S_PICTURE_REVIEW_NOT_FINAL.mp4'), '-i', str(mixed),
         '-map','0:v:0','-map','1:a:0','-vf',vf,'-c:v','libx264','-preset','fast','-crf','18',
         '-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',str(final)])
    after = measure(final)
    metadata = json.loads(subprocess.check_output([str(FP),'-v','error','-count_frames',
        '-show_streams','-show_format','-of','json',str(final)],text=True))
    v = next(s for s in metadata['streams'] if s['codec_type']=='video')
    assert (v['width'],v['height'],v['avg_frame_rate'],int(v['nb_read_frames'])) == (720,1280,'24/1',720)
    assert abs(float(metadata['format']['duration'])-30)<0.001
    assert after['true_peak_dbtp'] <= -1.0
    run(['-i',str(final),'-f','null','NUL'])
    run(['-i',str(final),'-vf','fps=1,scale=180:320,tile=10x3','-frames:v','1',str(opts.out/'contact.png')])
    for time in [1,4,6.4,8,9,12.4,13.5,22.5,25,27.5,29]:
        run(['-ss',str(time),'-i',str(final),'-frames:v','1',str(opts.out/f'frame-{time:g}.png')])
    assert sha(approved)==approval['approved_artifact_sha256']
    report = {'status':'FINISHED_EXPORT_PENDING_OWNER_TEXT_MIX_RELEASE_REVIEW',
        'approved_cut_sha256':sha(approved),'source_pcm_sha256':sha(pcm),'output':str(final),
        'output_sha256':sha(final),'clean_sha256':sha(clean),'srt_sha256':sha(opts.out/'EP01_C-v0.6_vi.srt'),
        'captions':cues,'release_overlays':overlays,'caption_timing':'source-bounded ASR hints with approved exact text; not forced alignment or ear verdict',
        'caption_text_and_speaker_mapping':'EXACT_SCRIPT_PASS','input_measurement':before,'output_measurement':after,
        'uniform_gain_db':gain,'speed_pitch_EQ_dynamic_compression_change':False,
        'new_music_ambience_foley':'NONE_ADDED; preserve original accepted audio including its existing sound',
        'fps':24,'frames':720,'duration':30,'full_decode_exit':0,'credit_spend':0,
        'picture_edit_changed':False,'continuity_deviations':'OWNER_ACCEPTED210_NOT_ERASED',
        'independent_agent_or_ear_pass':False,'publication':'NOT_PERFORMED_OR_AUTHORIZED',
        'editable_asset_hashes':{p.name:sha(p) for p in sorted(assets.iterdir()) if p.is_file()},
        'metadata':metadata}
    (opts.out/'delivery-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['output','output_sha256','uniform_gain_db','output_measurement']}))


if __name__=='__main__':
    main()

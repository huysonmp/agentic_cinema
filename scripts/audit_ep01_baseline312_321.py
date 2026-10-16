"""Evidence-only audit of preserved rough312. No edit, generation or AV approval."""
import argparse
import hashlib
import json
import subprocess
from array import array
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

EP = Path('he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot')
EXPECTED = '44bd2c591a00f085b8d4c4e4e69c5a25fb9d4f4357e7dbc76263ca068fec1e66'


def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def make_board(output, entries, images, columns=4, width=210):
    height = round(width * 1280 / 720)
    label_height = 42
    canvas = Image.new('RGB', (columns * width, ((len(entries)+columns-1)//columns) * (height+label_height)), '#181818')
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 15)
    for i, (label, frame) in enumerate(entries):
        x, y = i % columns * width, i // columns * (height+label_height)
        with Image.open(images[frame]) as im:
            canvas.paste(im.resize((width, height)), (x, y+label_height))
        draw.text((x+4, y+3), label, fill='white', font=font)
        draw.text((x+4, y+21), f'F{frame} | {frame/24:.3f}s', fill='#b5d9ff', font=font)
    canvas.save(output)


def supplement(base, source, ffbin, out):
    """Inspect unused native handles without changing any selected range."""
    target=out/'native_handles_321.json'
    if target.exists():
        raise ValueError('Supplement already exists; no overwrite')
    definitions=[
        ('C04',base/'05_native/EP01_720_C04_T02_NATIVE.mp4',116,144,
         '8ad98f21c0c904b01055d6f579900cd60c107a152a9166a8cfa563165a47a209'),
        ('C09',base/'07_edits/C09_PICK_B_FULL_SILENT_REVIEW_ONLY_311.mp4',72,96,
         '68589b58fcc342fc1d72c111828c9bf430d4713a2ba9ee78ed60f57bc09f5958')]
    results=[]
    for name, path, lo, hi, expected in definitions:
        assert sha(path)==expected
        folder=out/f'{name}_native_handle_frames'; folder.mkdir()
        subprocess.run([str(ffbin/'ffmpeg.exe'),'-nostdin','-hide_banner','-v','error','-n','-i',str(path),'-vf',f"select='between(n,{lo},{hi-1})',scale=360:640",'-fps_mode','vfr','-start_number',str(lo),str(folder/'%04d.png')],check=True)
        images={n:folder/f'{n:04}.png' for n in range(lo,hi)}
        assert all(p.exists() for p in images.values())
        make_board(out/f'{name}_native_handles.png',[(name+' native',n) for n in range(lo,hi)],images,columns=7 if name=='C04' else 6,width=160)
        results.append({'source':str(path),'sha256':expected,'frames_viewable':list(range(lo,hi)),'selected_range_changed':False})
    pcm=subprocess.check_output([str(ffbin/'ffmpeg.exe'),'-nostdin','-hide_banner','-v','error','-i',str(source),'-ss','29.25','-map','0:a:0','-ar','48000','-ac','2','-f','f32le','-'])
    samples=array('f'); samples.frombytes(pcm)
    payload={'record':'REC321','unused_source_handles':results,
             'rough_tail_pcm_check':{'start_seconds':29.25,'sample_values':len(samples),'nonzero_values':sum(v!=0 for v in samples),'max_abs':max(map(abs,samples),default=0),'meaning':'Existing ASR subscribe sentence in silent tail is not evidence of actual dialogue'},
             'no_endpoint_selected':True,'no_EDL_changed':True,'no_generation':True}
    target.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(payload['rough_tail_pcm_check']))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--supplement', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    base = root / EP / 'restart_720p_v1'
    source = base / '07_edits/EP01_ROUGH35_TRIAL_v1_NOT_FINAL_312.mp4'
    edl = json.loads((base / '07_edits/EP01_ROUGH35_TRIAL_edl_312.json').read_text(encoding='utf-8'))
    if sha(source) != EXPECTED:
        raise ValueError('Baseline hash mismatch')
    ffbin = root / '.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin'
    if args.supplement:
        existing=json.loads((args.out/'audit_321.json').read_text(encoding='utf-8'))
        assert existing['sha256']==EXPECTED
        supplement(base, source, ffbin, args.out)
        return
    if args.out.exists():
        raise ValueError('Fresh evidence directory required')
    args.out.mkdir(parents=True)
    probe = json.loads(subprocess.check_output([str(ffbin/'ffprobe.exe'), '-v', 'error', '-count_frames', '-show_streams', '-show_format', '-of', 'json', str(source)], text=True, encoding='utf-8'))
    v = next(s for s in probe['streams'] if s['codec_type']=='video')
    assert (v['width'], v['height'], int(v['nb_read_frames']), v['avg_frame_rate']) == (720,1280,840,'24/1')
    sources=[]
    for item in edl['sources']:
        actual=sha(base/item['path'])
        assert actual == item['sha256'], item['path']
        sources.append({'path':item['path'],'sha256':actual,'matches':True})
    rows=[]
    cursor=0
    for segment in edl['segments']:
        a,b=segment['timeline']
        assert a==cursor and b-a==segment['range'][1]-segment['range'][0]
        rows.append({'shot':segment['shot'],'start_frame':a,'end_frame_exclusive':b,'start_seconds':a/24,'end_seconds':b/24,'duration_seconds':(b-a)/24})
        cursor=b
    assert cursor==840
    picks=set(range(0,840,24))
    for cut in edl['cuts_zero_based']:
        picks.update(range(cut-4,cut+4))
    picks.update(range(816,840))
    picks=sorted(picks)
    frames=args.out/'selected_frames'; frames.mkdir()
    # Read the actual assembled export, not a reference or a separately trimmed clip.
    # Compact runs avoid FFmpeg expression-depth limits from a 100+ term sum.
    select='+'.join(['not(mod(n,24))','between(n,816,839)']+
                    [f'between(n,{n-4},{n+3})' for n in edl['cuts_zero_based']])
    subprocess.run([str(ffbin/'ffmpeg.exe'),'-nostdin','-hide_banner','-v','error','-n','-i',str(source),'-vf',f"select='{select}',scale=360:640",'-fps_mode','vfr','-start_number','0',str(frames/'%04d.png')],check=True)
    files=sorted(frames.glob('*.png')); assert len(files)==len(picks)
    images=dict(zip(picks,files))
    make_board(args.out/'overview_35_samples.png',[(f'Timeline {n//24}s',n) for n in range(0,840,24)],images,columns=7,width=150)
    for page in range(3):
        entries=[]
        for cut in edl['cuts_zero_based'][page*4:(page+1)*4]:
            for offset in (-2,-1,0,1):
                entries.append((f'Cut {cut}: {offset:+d}',cut+offset))
        make_board(args.out/f'cuts_page_{page+1}.png',entries,images)
    make_board(args.out/'ending_last_second_all24.png',[(f'Ending +{n-816:02}',n) for n in range(816,840)],images,columns=6,width=150)
    asr=json.loads((base/'06_qc/EP01_ROUGH35_ASR_312/asr.json').read_text(encoding='utf-8'))
    report={
        'record':'REC321','date':'2026-10-16','status':'BASELINE_AUDIT_EVIDENCE_NOT_EDIT_OR_AV_PASS',
        'baseline':str(source),'sha256':EXPECTED,'sources_verified':sources,
        'measured':{'width':720,'height':1280,'frames':840,'fps':24,'seconds':35},
        'source_windows':rows,'cuts':[{'frame':n,'seconds':n/24} for n in edl['cuts_zero_based']],
        'extracted_frame_indices_zero_based':picks,'extraction':'fresh frames selected from exact rough export; evidence thumbnails 360x640, no pixel retouch',
        'asr_existing_machine_segments_not_listening':[{'start':s['start'],'end':s['end'],'text':s['text']} for s in asr['segments']],
        'target30_reduction_frames':120,'target30_safe_trim_proven':False,
        'continuous_motion_review':False,'actual_listening':False,'independent_agent_report':False,
        'new_video_generated':False,'Flow_credit_spend':0,'source_overwritten':False,'EDL_changed':False,
        'source_hash_after':sha(source)
    }
    assert report['source_hash_after']==EXPECTED
    (args.out/'audit_321.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'frames_extracted':len(picks),'verified_sources':len(sources),'seconds':35,'Flow_spend':0}))


if __name__=='__main__':
    main()

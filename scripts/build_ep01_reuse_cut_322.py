"""One review-only reuse cut. Preserve sources; never generates, spends or approves."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
EP=ROOT/'he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot'
BASE=EP/'restart_720p_v1'
FFBIN=ROOT/'.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin'
QC=BASE/'06_qc/REUSE_CUT_322'
TARGET=BASE/'07_edits/EP01_REUSE_CUT_v1_322_FOR_REVIEW.mp4'
EDL=BASE/'07_edits/EP01_REUSE_CUT_edl_322.json'
FILTER=BASE/'07_edits/EP01_REUSE_CUT_filter_v2_322.txt'
SOURCES=[
    ('07_edits/EP01_ROUGH35_TRIAL_v1_NOT_FINAL_312.mp4','44bd2c591a00f085b8d4c4e4e69c5a25fb9d4f4357e7dbc76263ca068fec1e66'),
    ('05_native/EP01_720_C02_COVERAGE_K20_T01_320_NATIVE.mp4','32539bfe68fe9518ce7b14732033f5316d9251bafe53b74be8fb0ae65b18af78'),
    ('05_native/EP01_720_C04_T02_NATIVE.mp4','8ad98f21c0c904b01055d6f579900cd60c107a152a9166a8cfa563165a47a209'),
    ('07_edits/C09_PICK_B_FULL_SILENT_REVIEW_ONLY_311.mp4','68589b58fcc342fc1d72c111828c9bf430d4713a2ba9ee78ed60f57bc09f5958')]
# source index, zero-based half-open frame range, sound policy.
SEGMENTS=[
    ('C01A',0,0,81,'source'),('BM_KHOAN',0,81,99,'source'),
    ('BR_RETURN',0,99,141,'source'),('C02_MEMORY_NEW_320_REVIEW',1,0,180,'source'),
    ('C03A_DAO_QUESTION',0,314,344,'source'),('C03B_KHOAI_REPLY',0,350,384,'source'),
    ('C04_PICK_A',2,12,144,'silence'),('C05_CAUGHT',0,510,564,'source'),
    ('C06_EXCUSE',0,582,624,'source'),('C07_RECEIVE',0,628,696,'source'),
    ('C08_DEPOSIT_A',0,696,760,'silence'),('C09_PICK_B_END',3,8,96,'silence')]


def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream,'sha256').hexdigest()


def write_json(path,data):
    if path.exists(): raise ValueError(f'No overwrite: {path}')
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')


def probe(path):
    return json.loads(subprocess.check_output([str(FFBIN/'ffprobe.exe'),'-v','error','-count_frames','-show_streams','-show_format','-of','json',str(path)],text=True,encoding='utf-8'))


def run(args):
    subprocess.run([str(FFBIN/'ffmpeg.exe'),'-nostdin','-hide_banner','-v','error','-n',*args],check=True)


def board(path,items,columns=4,width=180):
    h=320; labelh=44
    im=Image.new('RGB',(columns*width,((len(items)+columns-1)//columns)*(h+labelh)),'#181818')
    d=ImageDraw.Draw(im); font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',13)
    for i,(label,pic) in enumerate(items):
        x=i%columns*width; y=i//columns*(h+labelh)
        with Image.open(pic) as src: im.paste(src.resize((width,h)),(x,y+labelh))
        d.multiline_text((x+3,y+2),label,fill='white',font=font,spacing=2)
    im.save(path)


def prepare():
    if QC.exists() or EDL.exists() or FILTER.exists() or TARGET.exists():
        raise ValueError('Use a fresh record; outputs already exist')
    QC.mkdir(parents=True)
    sources=[]; frames={}
    for i,(rel,expected) in enumerate(SOURCES):
        path=BASE/rel
        assert sha(path)==expected,rel
        p=probe(path); v=next(s for s in p['streams'] if s['codec_type']=='video')
        assert (v['width'],v['height'],v['avg_frame_rate'])==(720,1280,'24/1')
        frames[i]=int(v['nb_read_frames'])
        sources.append({'input':i,'path':rel,'sha256':expected,'probe':p})
    rows=[]; cursor=0
    for name,source,a,b,audio in SEGMENTS:
        assert 0<=a<b<=frames[source]
        rows.append({'shot':name,'input':source,'range':[a,b],'timeline':[cursor,cursor+b-a],'audio':audio})
        cursor+=b-a
    assert cursor==833
    payload={'record':'REC322','date':'2026-10-16','status':'TRIAL_EDIT_NOT_APPROVED_OR_FINAL',
             'authority':'Owner requested one consolidated pass; local edit only, no paid generation',
             'sources':sources,'segments':rows,'frames':cursor,'fps':24,'seconds':cursor/24,
             'target':str(TARGET),'new_C02_320_owner_approval':False,
             'voices':'Source-synchronous only; no voice reassignment, speed, pitch or replacement TTS',
             'known_open':['Food morphology/quantity changes at C05-C06; not repaired by this cut','Whole-episode 30s target not met','New C02320 owner voice/acting checkpoint pending; shown in this consolidated trial','C09 hand-role exception remains rough-only','Native motion and perceptual AV still require review'],
             'no_old_source_or_EDL_overwrite':True,'Flow_spend':0,'release_authorized':False}
    write_json(EDL,payload)
    # Inspect actual boundary states before rendering the single full trial.
    for i in range(len(SOURCES)):
        picks=sorted({n for row in rows if row['input']==i for n in (row['range'][0],row['range'][1]-1)})
        folder=QC/f'input_{i}_boundary_frames'; folder.mkdir()
        select='+'.join(f'eq(n,{n})' for n in picks)
        run(['-i',str(BASE/SOURCES[i][0]),'-vf',f"select='{select}',scale=360:640",'-fps_mode','vfr','-start_number','0',str(folder/'%03d.png')])
        extracted=sorted(folder.glob('*.png')); assert len(extracted)==len(picks)
        for n,path in zip(picks,extracted): frames[(i,n)]=path
    for page in range(3):
        items=[]
        for row in rows[page*4:(page+1)*4]:
            for tag,n in [('START',row['range'][0]),('END',row['range'][1]-1)]:
                items.append((row['shot']+' '+tag+'\nI'+str(row['input'])+' F'+str(n),frames[(row['input'],n)]))
        board(QC/f'planned_boundaries_{page+1}.png',items)
    print(json.dumps({'prepared_frames':cursor,'seconds':cursor/24,'credit_spend':0}))


def render():
    edl=json.loads(EDL.read_text(encoding='utf-8'))
    assert [(r['shot'],r['input'],*r['range'],r['audio']) for r in edl['segments']]==SEGMENTS
    for src in edl['sources']: assert sha(BASE/src['path'])==src['sha256']
    if TARGET.exists() or FILTER.exists(): raise ValueError('No overwrite/render retry')
    filters=[]; video_inputs={}; audio_inputs={}
    for source in range(len(edl['sources'])):
        indices=[i for i,row in enumerate(edl['segments']) if row['input']==source]
        if len(indices)>1:
            filters.append(f'[{source}:v]split={len(indices)}'+''.join(f'[vs{i}]' for i in indices))
            video_inputs.update({i:f'vs{i}' for i in indices})
        else:
            video_inputs.update({i:f'{source}:v' for i in indices})
        indices=[i for i,row in enumerate(edl['segments']) if row['input']==source and row['audio']=='source']
        if len(indices)>1:
            filters.append(f'[{source}:a]asplit={len(indices)}'+''.join(f'[as{i}]' for i in indices))
            audio_inputs.update({i:f'as{i}' for i in indices})
        else:
            audio_inputs.update({i:f'{source}:a' for i in indices})
    for i,row in enumerate(edl['segments']):
        src=row['input']; a,b=row['range']; length=b-a
        filters.append(f'[{video_inputs[i]}]trim=start_frame={a}:end_frame={b},setpts=PTS-STARTPTS[v{i}]')
        if row['audio']=='source':
            filters.append(f'[{audio_inputs[i]}]aresample=48000,apad,atrim=start_sample={a*2000}:end_sample={b*2000},asetpts=PTS-STARTPTS[a{i}]')
        else:
            filters.append(f'anullsrc=r=48000:cl=stereo,atrim=end_sample={length*2000},asetpts=PTS-STARTPTS[a{i}]')
    count=len(edl['segments'])
    filters.append(''.join(f'[v{i}][a{i}]' for i in range(count))+f'concat=n={count}:v=1:a=1[v][a]')
    FILTER.write_text(';\n'.join(filters),encoding='utf-8')
    inputs=[]
    for src in edl['sources']: inputs+=['-i',str(BASE/src['path'])]
    command=[*inputs,'-filter_complex',FILTER.read_text(encoding='utf-8'),'-map','[v]','-map','[a]',
             '-c:v','libx264','-preset','medium','-crf','16','-pix_fmt','yuv420p',
             '-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',str(TARGET)]
    write_json(QC/'render_command_v2_322.json',{'command':[str(FFBIN/'ffmpeg.exe'),'-nostdin','-hide_banner','-v','error','-n',*command],'filter_sha256':sha(FILTER),'EDL_sha256':sha(EDL)})
    run(command)
    print(str(TARGET))


def pcm(path):
    return np.frombuffer(subprocess.check_output([str(FFBIN/'ffmpeg.exe'),'-nostdin','-hide_banner','-v','error','-i',str(path),'-map','0:a:0','-ar','48000','-ac','2','-f','f32le','-']),dtype='<f4').reshape(-1,2)


def verify():
    edl=json.loads(EDL.read_text(encoding='utf-8')); p=probe(TARGET)
    v=next(s for s in p['streams'] if s['codec_type']=='video')
    assert (v['width'],v['height'],int(v['nb_read_frames']),v['avg_frame_rate'])==(720,1280,833,'24/1')
    assert abs(float(p['format']['duration'])-833/24)<.025
    run(['-i',str(TARGET),'-f','null','-'])
    output=pcm(TARGET); expected=833*2000
    assert expected<=len(output)<=expected+1024
    source_pcm={i:pcm(BASE/src['path']) for i,src in enumerate(edl['sources']) if any(s['input']==i and s['audio']=='source' for s in edl['segments'])}
    comparisons=[]
    for row in edl['segments']:
        lo,hi=row['timeline']; a,b=row['range']; guard=4096
        actual=output[lo*2000+guard:hi*2000-guard]
        if row['audio']=='source':
            ref=source_pcm[row['input']][a*2000+guard:b*2000-guard]
            assert actual.shape==ref.shape
            if float(np.max(np.abs(ref),initial=0))<1e-7:
                maximum=float(np.max(np.abs(actual),initial=0))
                assert maximum<1e-5
                comparisons.append({'shot':row['shot'],'source_is_silence':True,'output_interior_max_abs':maximum,'correlation':'undefined for constant-zero signal'})
            else:
                corr=float(np.corrcoef(ref.reshape(-1),actual.reshape(-1))[0,1])
                assert corr>.995,(row['shot'],corr)
                comparisons.append({'shot':row['shot'],'zero_lag_PCM_correlation':corr,'voice_identity_or_lipsync_pass':False})
        else:
            maximum=float(np.max(np.abs(actual),initial=0))
            assert maximum<1e-5
            comparisons.append({'shot':row['shot'],'interior_silence_max_abs':maximum})
    # Fresh encoded-output pictures; input stills are not an export QC substitute.
    cuts=[r['timeline'][0] for r in edl['segments'][1:]]
    picks=sorted(set(range(0,833,24))|{n for cut in cuts for n in (cut-2,cut-1,cut,cut+1)}|set(range(817,833)))
    folder=QC/'encoded_sample_frames'; folder.mkdir()
    select='not(mod(n,24))+between(n,817,832)+'+'+'.join(f'between(n,{n-2},{n+1})' for n in cuts)
    run(['-i',str(TARGET),'-vf',f"select='{select}',scale=360:640",'-fps_mode','vfr','-start_number','0',str(folder/'%03d.png')])
    extracted=sorted(folder.glob('*.png')); assert len(extracted)==len(picks)
    images=dict(zip(picks,extracted))
    board(QC/'encoded_overview.png',[(f'{n/24:.3f}s F{n}',images[n]) for n in range(0,833,24)],columns=7,width=150)
    for page in range(3):
        items=[]
        for cut in cuts[page*4:(page+1)*4]:
            for n in (cut-2,cut-1,cut,cut+1): items.append((f'Cut {cut/24:.3f}s\nF{n}',images[n]))
        board(QC/f'encoded_cuts_{page+1}.png',items)
    board(QC/'encoded_ending_last16.png',[(f'{n/24:.3f}s F{n}',images[n]) for n in range(817,833)],columns=4)
    for src in edl['sources']: assert sha(BASE/src['path'])==src['sha256']
    write_json(QC/'verification_322.json',{'record':'REC322','status':'TECHNICAL_PCM_AND_FRAME_EVIDENCE_NOT_PERCEPTUAL_AV_APPROVAL','sha256':sha(TARGET),'probe':p,'full_decode_exit':0,'audio_sample_frames':len(output),'expected_audio_sample_frames':expected,'PCM_comparisons':comparisons,'encoded_sample_indices':picks,'source_hashes_after_match':True,'target30_pass':False,'Flow_spend':0,'actual_listening':False,'continuous_motion_review':False,'independent_agent_report':False,'release_authorized':False})
    print(json.dumps({'frames':833,'seconds':833/24,'sha256':sha(TARGET),'PCM_segments':len(comparisons),'full_decode_exit':0}))


def tailcheck():
    samples=pcm(TARGET)[int(28.5*48000):]
    data={'record':'REC322','source_sha256':sha(TARGET),'start_seconds':28.5,
          'sample_values':int(samples.size),'nonzero_sample_values':int(np.count_nonzero(samples)),
          'max_abs':float(np.max(np.abs(samples),initial=0)),
          'meaning':'Unprompted ASR subscribe sentence in this silent tail is a machine hallucination, not output dialogue'}
    assert data['nonzero_sample_values']==0
    write_json(QC/'tail_ASR_false_positive_322.json',data)
    print(json.dumps(data))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stage',choices=['prepare','render','verify','tailcheck'])
    args=parser.parse_args()
    {'prepare':prepare,'render':render,'verify':verify,'tailcheck':tailcheck}[args.stage]()

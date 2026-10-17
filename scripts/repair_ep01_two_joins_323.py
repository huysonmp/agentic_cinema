"""Two local motion-compensated join repairs; no new AI generation or voice edit."""
import argparse
import json
import math
import shutil
import subprocess
from pathlib import Path

import numpy as np

from build_ep01_reuse_cut_322 import BASE, FFBIN, board, probe, run, sha, write_json

SOURCE=BASE/'07_edits/EP01_REUSE_CUT_v1_322_FOR_REVIEW.mp4'
EXPECTED='68d595328bfd858b998583ee56584e20643393c6f3497b3aeb4c47c02afa57b0'
QC=BASE/'06_qc/TWO_JOIN_REPAIR_323'
TARGET=BASE/'07_edits/EP01_TWO_JOIN_REPAIR_v2_323_FOR_REVIEW.mp4'
WINDOWS=[{'id':'J1','cut':385,'start':381,'end':389},
         {'id':'J2','cut':517,'start':513,'end':520}]


def check_source():
    assert sha(SOURCE)==EXPECTED


def prepare():
    check_source()
    if QC.exists() or TARGET.exists(): raise ValueError('Fresh record required')
    QC.mkdir(parents=True)
    for w in WINDOWS:
        folder=QC/w['id']; folder.mkdir()
        before=folder/'before'; before.mkdir()
        a,b=w['start'],w['end']
        run(['-i',str(SOURCE),'-vf',f"select='between(n,{a-2},{b+1})'",'-fps_mode','vfr','-start_number',str(a-2),str(before/'%04d.png')])
        assert len(list(before.glob('*.png')))==b-a+4
        board(folder/'before_all.png',[(f"{w['id']} BEFORE\nF{n} {n/24:.3f}s",before/f'{n:04}.png') for n in range(a-2,b+2)],columns=4)
        anchors=folder/'anchors'; anchors.mkdir()
        for n in range(6):
            anchor=a if n<3 else b-1
            shutil.copyfile(before/f'{anchor:04}.png',anchors/f'{n:02}.png')
        write_json(folder/'patch_spec.json',{'record':'REC323','source_sha256':EXPECTED,
            'window_half_open':[a,b],'source_cut':w['cut'],'anchors':[a,b-1],
            'method':'FFmpeg motion-compensated intermediate frames, not crossfade/freeze or generative AI',
            'frames':b-a,'audio_changed':False,'subjective_quality_approved':False})
    write_json(QC/'source_323.json',{'record':'REC323','date':'2026-10-17','source':str(SOURCE),'sha256':EXPECTED,'probe':probe(SOURCE),'owner_request':'giây 15-16 chuyển cảnh chưa ổn, giây 20-21 cũng thế; sửa nốt bản cuối này đi là ổn rồi đó','scope':'Only two picture join windows; do not silently change dialogue, duration, other cuts or final30 target','windows':WINDOWS,'Flow_spend':0})


def patches():
    check_source()
    for w in WINDOWS:
        folder=QC/w['id']; length=w['end']-w['start']; span=length-1
        target=folder/'motion_patch.mkv'
        if target.exists(): raise ValueError('Patch exists; no overwrite')
        vf=(f'minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1:scd=none,'
            f'trim=start_frame={span*2}:end_frame={span*2+length},setpts=PTS-STARTPTS,format=yuv420p')
        command=['-framerate',f'24/{span}','-i',str(folder/'anchors/%02d.png'),'-vf',vf,
                 '-an','-fps_mode','passthrough','-c:v','libx264','-crf','0','-preset','medium',str(target)]
        write_json(folder/'patch_command.json',{'command':command,'filter':vf})
        run(command)
        p=probe(target); v=next(s for s in p['streams'] if s['codec_type']=='video')
        assert int(v['nb_read_frames'])==length,(w['id'],v)
        after=folder/'patch_frames'; after.mkdir()
        run(['-i',str(target),'-fps_mode','passthrough','-start_number',str(w['start']),str(after/'%04d.png')])
        board(folder/'patch_all.png',[(f"{w['id']} PATCH\nF{n} {n/24:.3f}s",after/f'{n:04}.png') for n in range(w['start'],w['end'])],columns=4)
        write_json(folder/'patch_media.json',{'probe':p,'sha256':sha(target),'frames':length,'owner_approval':False})


def render():
    check_source()
    if TARGET.exists(): raise ValueError('No overwrite')
    rows=[{'input':0,'range':[0,381]},{'input':1,'range':[0,8]},
          {'input':0,'range':[389,513]},{'input':2,'range':[0,7]},
          {'input':0,'range':[520,833]}]
    assert sum(r['range'][1]-r['range'][0] for r in rows)==833
    filters=['[0:v]split=3[s0][s2][s4]']
    for i,row in enumerate(rows):
        label=f's{i}' if row['input']==0 else f"{row['input']}:v"
        a,b=row['range']
        filters.append(f'[{label}]trim=start_frame={a}:end_frame={b},settb=1/12288,setpts=N*512[v{i}]')
    filters.append('[v0][v1][v2][v3][v4]concat=n=5:v=1:a=0[v]')
    filter_text=';\n'.join(filters)
    patchpaths=[QC/w['id']/'motion_patch.mkv' for w in WINDOWS]
    command=['-i',str(SOURCE),'-i',str(patchpaths[0]),'-i',str(patchpaths[1]),
        '-filter_complex',filter_text,'-map','[v]','-map','0:a:0','-c:v','libx264',
        '-preset','medium','-crf','16','-pix_fmt','yuv420p','-fps_mode','passthrough',
        '-c:a','copy','-movflags','+faststart',str(TARGET)]
    write_json(QC/'render_command_323.json',{'command':command,'filter':filter_text,'windows':WINDOWS,
        'sources':[{'path':str(p),'sha256':sha(p)} for p in [SOURCE,*patchpaths]],
        'audio':'copy original AAC packets from exact REC322; no mix/gain/pitch/speed or new voice',
        'frames':833,'seconds':833/24,'new_generation':False,'Flow_spend':0})
    run(command)
    print(str(TARGET))


def packets(path):
    data=json.loads(subprocess.check_output([str(FFBIN/'ffprobe.exe'),'-v','error','-select_streams','a:0','-show_packets','-show_data_hash','sha256','-show_entries','packet=pts,dts,duration,size,data_hash','-of','json',str(path)],text=True,encoding='utf-8'))
    return data['packets']


def rgb_frames(path,indices):
    select='+'.join(f'eq(n,{n})' for n in indices)
    raw=subprocess.check_output([str(FFBIN/'ffmpeg.exe'),'-nostdin','-hide_banner','-v','error','-i',str(path),'-vf',f"select='{select}',format=rgb24",'-fps_mode','vfr','-f','rawvideo','-'])
    frames=np.frombuffer(raw,np.uint8).reshape(-1,1280,720,3)
    assert len(frames)==len(indices)
    return dict(zip(indices,frames))


def verify():
    check_source(); p=probe(TARGET); v=next(s for s in p['streams'] if s['codec_type']=='video')
    assert (v['width'],v['height'],int(v['nb_read_frames']),v['avg_frame_rate'])==(720,1280,833,'24/1')
    assert abs(float(p['format']['duration'])-833/24)<.025
    run(['-i',str(TARGET),'-f','null','-'])
    old_packets=packets(SOURCE); new_packets=packets(TARGET)
    assert old_packets==new_packets,'Audio packets or timing changed'
    outside=[0,80,140,320,350,380,389,512,520,570,612,680,744,832]
    picks=sorted(set(outside)|{n for w in WINDOWS for n in range(w['start']-2,w['end']+2)})
    old=rgb_frames(SOURCE,picks); new=rgb_frames(TARGET,picks)
    scores=[]
    for n in outside:
        difference=old[n].astype(np.float32)-new[n].astype(np.float32)
        mse=float(np.mean(difference*difference))
        psnr=10*math.log10(255*255/max(mse,1e-10))
        assert psnr>38,(n,psnr)
        scores.append({'frame':n,'RGB_PSNR_dB':psnr,'mean_absolute_channel_difference':float(np.mean(np.abs(difference)))})
    motion=[]
    for w in WINDOWS:
        # Fixed face/upper-body ROI for diagnostics only, not a face detector or perceptual pass.
        before=[]; after=[]
        for n in range(w['start']+1,w['end']):
            before.append(float(np.mean(np.abs(old[n][200:700,50:660].astype(np.float32)-old[n-1][200:700,50:660].astype(np.float32)))))
            after.append(float(np.mean(np.abs(new[n][200:700,50:660].astype(np.float32)-new[n-1][200:700,50:660].astype(np.float32)))))
        motion.append({'id':w['id'],'rough_window':[w['start'],w['end']],
                       'max_adjacent_ROI_MAD_before':max(before),'max_adjacent_ROI_MAD_after':max(after),
                       'all_before':before,'all_after':after,'not_motion_or_face_quality_certification':True})
        folder=QC/w['id']/'encoded_frames'; folder.mkdir()
        for n in range(w['start']-2,w['end']+2):
            from PIL import Image
            Image.fromarray(new[n]).save(folder/f'{n:04}.png')
        board(QC/w['id']/'encoded_all.png',[(f"{w['id']} EXPORT\nF{n} {n/24:.3f}s",folder/f'{n:04}.png') for n in range(w['start']-2,w['end']+2)],columns=4)
    write_json(QC/'verification_323.json',{'record':'REC323','sha256':sha(TARGET),'probe':p,'full_decode_exit':0,
        'audio_packets_and_PTS_DTS_duration_size_SHA256_identical':True,'audio_packets_compared':len(old_packets),
        'outside_window_samples':scores,'outside_patches_reencoded_not_pixel_identical':True,
        'motion_diagnostics':motion,'baseline322_hash_unchanged':sha(SOURCE)==EXPECTED,
        'continuous_motion_or_perceptual_AV_approval':False,'root_frame_review_pending':True,
        'Flow_spend':0,'target30_pass':False,'food_seam_23p792_not_repaired':True,'release_authorized':False})
    print(json.dumps({'sha256':sha(TARGET),'seconds':833/24,'audio_packets_identical':len(old_packets),'motion_diagnostics':motion}))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stage',choices=['prepare','patches','render','verify'])
    args=parser.parse_args()
    {'prepare':prepare,'patches':patches,'render':render,'verify':verify}[args.stage]()

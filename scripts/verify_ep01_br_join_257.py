"""Technical source/silence/alignment checks, not heard-text or AV approval."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path
import numpy as np

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--base', type=Path, required=True)
p.add_argument('--bin', type=Path, required=True)
p.add_argument('--out', type=Path, required=True)
a = p.parse_args()
ff = str(a.bin/'ffmpeg.exe')
probe = str(a.bin/'ffprobe.exe')
def path(rel):
    return str(a.base/rel)
def streams(rel):
    return json.loads(subprocess.check_output([probe,'-v','error','-show_streams','-of','json',path(rel)],text=True))['streams']
def video_hash(rel):
    data = subprocess.check_output([ff,'-nostdin','-hide_banner','-loglevel','error','-i',path(rel),'-map','0:v:0','-f','framemd5','-'])
    return [line for line in data.decode().splitlines() if not line.startswith('#')]
def pcm(rel):
    return np.frombuffer(subprocess.check_output([ff,'-nostdin','-hide_banner','-loglevel','error','-i',path(rel),'-vn','-ac','2','-ar','48000','-f','s16le','-']),dtype=np.int16).reshape(-1,2)
native='05_native/EP01_720_C01B_BR_T01_NATIVE.mp4'
silent='07_edits/C01B_BR_T01_SILENT_DERIVED_NOT_SELECTED.mp4'
join='07_edits/C01A_BM_BR_C02_13p75S_CONDITIONAL_QC_NOT_FINAL.mp4'
accepted='07_edits/C01A_BM_4p125S_JOIN_QC_NOT_FINAL.mp4'
c02='07_edits/C02_T02_FLOW_0_7p5S_FOR_APPROVAL.mp4'
assert video_hash(native) == video_hash(silent), 'Remux changed decoded video'
assert not any(s['codec_type']=='audio' for s in streams(silent))
encoded=pcm(join)
expected_a=pcm(accepted)[:198000]
expected_c=pcm(c02)
def correlate(x,y):
    count=min(len(x),len(y))
    return float(np.corrcoef(x[:count].ravel(),y[:count].ravel())[0,1])
cor_a=correlate(expected_a,encoded[:198000])
cor_c=correlate(expected_c,encoded[298000:])
interior=encoded[198000+2048:298000-2048]
assert np.count_nonzero(interior)==0, 'Unexpected interior sound in BR'
assert cor_a>0.99 and cor_c>0.99, 'Unexpected audio source alignment'
raw=pcm(native)
report={'record':'REC257','target_sha256':hashlib.sha256((a.base/join).read_bytes()).hexdigest(),
    'status':'TECHNICAL_AUDIO_SOURCE_AND_SILENCE_ONLY_NOT_AV_PASS',
    'native_audio_max_abs_pcm':int(np.abs(raw.astype(np.int32)).max()),
    'native_audio_nonzero_values':int(np.count_nonzero(raw)),
    'silent_derivative_sha256':hashlib.sha256((a.base/silent).read_bytes()).hexdigest(),
    'silent_derivative_audio_streams':0,'silent_derivative_all96_decoded_video_frames_exact':True,
    'join_audio_start_A_BM_sample_frame':0,'join_BR_silence_sample_range_half_open':[198000,298000],
    'join_C02_audio_start_sample_frame':298000,
    'join_A_BM_source_zero_lag_correlation':cor_a,'join_C02_source_zero_lag_correlation':cor_c,
    'join_silence_interior_2048_sample_margin_nonzero':int(np.count_nonzero(interior)),
    'boundary_AAC_leakage_not_ruled_out':True,'agent_actual_listening':'NOT_PERFORMED',
    'owner_join_AV_acceptance':'PENDING','encoding_audio_not_bit_exact':True}
assert not a.out.exists()
a.out.write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps(report,indent=2))

"""Read-back finishing checks; speaker identity remains the owner's listening approval."""
import argparse
import json
import subprocess
import wave
from pathlib import Path
import numpy as np
from finish_ep01_approved_cut import BASE, FF, EP, sha, validate_cues


def picture_hash(path):
    return subprocess.check_output([str(FF),'-nostdin','-v','error','-i',str(path),
        '-map','0:v:0','-f','hash','-hash','sha256','-'],text=True).strip()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('folder',type=Path)
    p.add_argument('--report',type=Path,required=True)
    a=p.parse_args()
    assert not a.report.exists(), 'Do not overwrite a prior verification'
    manifest=json.loads((a.folder/'delivery-manifest.json').read_text(encoding='utf-8'))
    package=json.loads((EP/'evidence/179/dialogue-package.json').read_text(encoding='utf-8'))
    validate_cues(manifest['captions'],package)
    assert sha(manifest['output'])==manifest['output_sha256']
    assert sha(a.folder/'EP01_30S_CLEAN_v1.1.mp4')==manifest['clean_sha256']
    assert picture_hash(a.folder/'EP01_30S_CLEAN_v1.1.mp4')==picture_hash(BASE/'EP01_30S_PICTURE_REVIEW_NOT_FINAL.mp4')
    waves=[]
    for name in ['EP01_EXACT_APPROVED_PCM_30S.wav','EP01_DIALOGUE_STATIC_GAIN_30S.wav']:
        with wave.open(str(a.folder/'editable_assets'/name),'rb') as w:
            assert (w.getframerate(),w.getnchannels(),w.getsampwidth(),w.getnframes())==(48000,2,2,1440000)
            waves.append(np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').astype(np.float64))
    expected=waves[0]*10**(manifest['uniform_gain_db']/20)
    max_error=float(np.max(np.abs(waves[1]-expected)))
    assert max_error <= 1.0
    for name,digest in manifest['editable_asset_hashes'].items():
        assert sha(a.folder/'editable_assets'/name)==digest
    text_files=list((a.folder/'editable_assets').glob('cue-*.txt'))
    assert len(text_files)==13
    assert all(b'\r' not in f.read_bytes() for f in text_files)
    report={'status':'READBACK_TECHNICAL_TEXT_PASS_NOT_EAR_OR_PUBLICATION_APPROVAL',
        'output_sha256':manifest['output_sha256'],'clean_decoded_picture_identical_to_approved_edit':True,
        'audio_uniform_gain_only_max_pcm_quantization_error':max_error,
        'caption_exact_seven_lines_and_speaker_mapping':True,'caption_files_utf8_LF_no_CR':True,
        'layout_metric':'NOT_AUTOMATICALLY_MEASURED; root rendered-frame review recorded separately',
        'editable_asset_hash_readback':True,
        'source_media_modified':False,'new_credit_spend':0,
        'owner_current_gate':'Final overlays, volume and delivery review pending; picture edit accepted210',
        'independent_ear_or_agent_verdict':'NOT_CLAIMED'}
    a.report.parent.mkdir(parents=True,exist_ok=True)
    a.report.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report))


if __name__=='__main__': main()

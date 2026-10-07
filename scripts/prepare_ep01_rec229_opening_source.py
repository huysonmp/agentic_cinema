"""Prepare a non-final audiovisual source for one R01 production request.

No generation, upload, or spending. Originals remain untouched.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import wave

BASE = Path('C:/Users/PC/Downloads/du_an_nem_bui')
OUT = BASE / '229_r01_production_input'
FF = Path('D:/Workspace/agentic_cinema/.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/ffmpeg.exe')
SOURCES = {
    'A03': (BASE / '180_c_v06_dialogue/A03.mp4', '3921e8f9d3a4475bcbd7677f3ca7a180e499adbf432702ccec08aa45dac1620b'),
    'N01': (BASE / '183_speaker_audit/N01_intended_Dao_UNVERIFIED.wav', '366e95086c57dc1c5d2a2d366d6b24410ab85b0dcc7b2f2d4fbb61d3aa69cfe1'),
    'B': (BASE / '221_n02_pa_v_trial/N02_B_NATIVE.mp4', '660f175775db6b082458846edb5c8edc8beb771b90a3330f53cb37d07f31a535'),
    'B_PCM': (BASE / '221_n02_pa_v_trial/inspection/N02_B_NATIVE/AUDIO_REVIEW.wav', 'bafac31224a35eb80d2121dc05f0e6f5ae4839e6623895a1d51adeff21decb1f'),
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    for path, expected in SOURCES.values():
        assert sha(path) == expected, path
    OUT.mkdir(exist_ok=False)
    parts = []
    for key, count in [('N01', 103200), ('B_PCM', 48000)]:
        with wave.open(str(SOURCES[key][0]), 'rb') as source:
            assert (source.getnchannels(), source.getsampwidth(), source.getframerate()) == (2, 2, 48000)
            parts.append(source.readframes(count))
        assert len(parts[-1]) == count * 4
    exact = OUT / 'R01_N01_plus_B_prefix_EXACT_PCM.wav'
    with wave.open(str(exact), 'wb') as target:
        target.setnchannels(2)
        target.setsampwidth(2)
        target.setframerate(48000)
        target.writeframes(b''.join(parts))
    with wave.open(str(exact), 'rb') as check:
        assert check.readframes(check.getnframes()) == b''.join(parts)
    # A03 contributes picture only for N01. B contributes only [0;1).
    # fps rounding is picture-only, at most one video frame. PCM does not move.
    filters = (
        '[0:v]trim=start=0:end=2.15,setpts=PTS-STARTPTS,scale=360:640,setsar=1[a];'
        '[1:v]trim=start=0:end=1,setpts=PTS-STARTPTS,scale=360:640,setsar=1[b];'
        '[a][b]concat=n=2:v=1:a=0,fps=24,tpad=stop_mode=clone:stop_duration=1,trim=duration=4[v];'
        '[2:a]apad,atrim=duration=4[audio]'
    )
    guide = OUT / 'R01_SOURCE_GUIDE_NOT_FINAL.mp4'
    result = subprocess.run([str(FF), '-n', '-i', str(SOURCES['A03'][0]), '-i', str(SOURCES['B'][0]),
        '-i', str(exact), '-filter_complex', filters, '-map', '[v]', '-map', '[audio]',
        '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
        '-movflags', '+faststart', str(guide)], capture_output=True, text=True, check=True)
    (OUT / 'build.log').write_text(result.stderr, encoding='utf-8')
    manifest = {
        'record_id': 'REC229', 'status': 'PRODUCTION_INPUT_NOT_FINAL_NOT_AV_PASS',
        'sources': {key: {'path': str(path), 'sha256': expected} for key, (path, expected) in SOURCES.items()},
        'audio_pcm_ranges': [{'source': 'N01', 'start_sample': 0, 'end_sample': 103200, 'output_start_sample': 0},
                             {'source': 'B_PCM', 'start_sample': 0, 'end_sample': 48000, 'output_start_sample': 103200}],
        'audio_duration_s': 3.15, 'guide_duration_s': 4, 'guide_padding_s': 0.85,
        'b_picture_boundary_candidate': {'frame': 24, 'seconds': 1.0, 'fps': 24,
            'basis': 'ASR Khoan 0-.34, next word 1.10; silence .364292-1.209979; no new actual hearing',
            'status': 'PROVISIONAL_JOIN_REQUIRES_ACTUAL_OUTPUT_AV_CHECK'},
        'guide_warnings': ['A03 picture is not target table or identity lock; replacement guided by S/M/E.',
            'Guide hard cut is not desired movement or accepted join.',
            'AAC upload guide is lossy; exact PCM sidecar is retained for verification/master.',
            'Guide tail silence/held picture is padding only, not additional story beat.',
            'Do not change voice, timing or words; no repeated Khoan or regenerated memory.'],
        'master_rule': 'Use complete original B PCM continuously once at N02 start. Replace picture prefix only if new AV aligns; retain B picture from frame24 candidate after join QC. No cut/retime of B speech.',
        'artifacts': {'pcm': {'path': str(exact), 'sha256': sha(exact)},
                      'guide': {'path': str(guide), 'sha256': sha(guide)}},
        'actual_listening': False, 'full_av_pass': False, 'paid_submission': False,
    }
    (OUT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(manifest, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()

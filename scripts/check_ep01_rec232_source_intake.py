"""Local source verification only; no browser, generation, voice/AV judgement."""
import hashlib
import json
from pathlib import Path
import subprocess
import wave
import numpy as np

FF = Path('D:/Workspace/agentic_cinema/.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/ffmpeg.exe')
SRC = Path('C:/Users/PC/Downloads/du_an_nem_bui/229_r01_production_input/R01_SOURCE_GUIDE_NOT_FINAL.mp4')
FLOW = Path('C:/Users/PC/Downloads/R01_SOURCE_GUIDE_NOT_FINAL_20261007125205.mp4')
OUT = Path('C:/Users/PC/Downloads/du_an_nem_bui/232_source_intake_check')

def main():
    OUT.mkdir(exist_ok=False)
    audio = []
    for key, source in [('local', SRC), ('flow', FLOW)]:
        wav = OUT / (key + '.wav')
        subprocess.run([str(FF), '-v', 'error', '-n', '-i', str(source), '-vn',
                        '-ar', '48000', '-ac', '2', '-c:a', 'pcm_s16le', str(wav)], check=True)
        with wave.open(str(wav), 'rb') as stream:
            assert (stream.getnchannels(), stream.getsampwidth(), stream.getframerate()) == (2, 2, 48000)
            audio.append(np.frombuffer(stream.readframes(stream.getnframes()), dtype='<i2').reshape(-1, 2).astype(np.float64))
    # Fixed zero-offset segments, not an alignment optimiser or voice classifier.
    ranges = [('N01', 0, 103200), ('B_prefix', 103200, 151200)]
    measurements = []
    for label, start, end in ranges:
        a, b = audio[0][start:end].ravel(), audio[1][start:end].ravel()
        assert len(a) == len(b)
        measurements.append({'range': label, 'start_sample': start, 'end_sample': end,
            'zero_offset_pearson': float(np.corrcoef(a, b)[0, 1]),
            'mean_absolute_sample_error': float(np.abs(a-b).mean())})
    report = {'record_id': 'REC232', 'local_source': str(SRC), 'flow_download': str(FLOW),
        'local_sha256': hashlib.sha256(SRC.read_bytes()).hexdigest(),
        'flow_sha256': hashlib.sha256(FLOW.read_bytes()).hexdigest(),
        'byte_identical': SRC.read_bytes() == FLOW.read_bytes(),
        'decoded_sample_frames': {'local': len(audio[0]), 'flow': len(audio[1])},
        'measurements': measurements, 'actual_listening': False, 'voice_identity_pass': False,
        'status': 'TECHNICAL_SOURCE_CORRESPONDENCE_ONLY_NOT_AV_PASS'}
    (OUT/'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf8')
    board = OUT/'FLOW_GUIDE_CONTACT_NOT_TARGET.jpg'
    subprocess.run([str(FF), '-v', 'error', '-n', '-i', str(FLOW), '-vf',
        'select=eq(n\\,0)+eq(n\\,24)+eq(n\\,48)+eq(n\\,52)+eq(n\\,74)+eq(n\\,95),scale=180:320,tile=3x2',
        '-frames:v', '1', '-update', '1', str(board)], check=True)
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()

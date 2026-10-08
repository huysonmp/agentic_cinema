"""REC255: exact source-offset frame/PCM checks; not listening or AV approval."""
import hashlib
import json
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

BASE = Path('C:/Users/PC/Downloads/du_an_nem_bui')
SOURCE = BASE / '254_LOCAL_SHIRT_REPAIR/encoded_qc'
TARGET = BASE / '255_KHOAN_SHORT'
QC = TARGET / 'encoded_qc'
OUT = TARGET / 'offset_comparison'
OUT.mkdir(exist_ok=False)


def pcm(path):
    with wave.open(str(path), 'rb') as wav:
        assert (wav.getframerate(), wav.getnchannels(), wav.getsampwidth()) == (48000, 2, 2)
        return wav.readframes(wav.getnframes())


expected = pcm(SOURCE / 'native_audio.wav')[40000 * 4:76000 * 4]
companion = pcm(TARGET / 'KHOAN_EXACT_SOURCE_RANGE_PCM.wav')
encoded = pcm(QC / 'native_audio.wav')
assert len(expected) == 36000 * 4 and expected == companion
assert len(encoded) == len(expected)
x = np.frombuffer(expected, dtype='<i2').astype(float)
y = np.frombuffer(encoded, dtype='<i2').astype(float)
correlation = float(np.corrcoef(x, y)[0, 1])
assert correlation > 0.98
source_frames = sorted((SOURCE / 'all_native_frames').glob('*.png'))
target_frames = sorted((QC / 'all_native_frames').glob('*.png'))
assert len(source_frames) == 96 and len(target_frames) == 18
mapping = []
for page in range(3):
    board = Image.new('RGB', (1080, 840), 'white')
    draw = ImageDraw.Draw(board)
    for row in range(6):
        idx = page * 6 + row
        src_idx = idx + 20
        src = Image.open(source_frames[src_idx]).convert('RGB')
        dst = Image.open(target_frames[idx]).convert('RGB')
        assert src.size == dst.size == (720, 1280)
        a, b = np.asarray(src, dtype=float), np.asarray(dst, dtype=float)
        mae = float(np.abs(a - b).mean())
        mapping.append({'output_frame': idx, 'source_frame': src_idx, 'rgb_mae_after_reencode': mae})
        # Full frame plus mouth/shirt crop on both sides; every native frame is included.
        for col, im in enumerate((src, dst)):
            left = col * 540
            draw.text((left + 5, row * 140 + 2), f'{"SOURCE" if col == 0 else "CUT"} F{src_idx if col == 0 else idx}', fill='black')
            board.paste(im.resize((65, 116)), (left + 5, row * 140 + 22))
            crop = im.crop((180, 350, 570, 930))
            crop.thumbnail((450, 116))
            board.paste(crop, (left + 95, row * 140 + 22))
    board.save(OUT / f'all18_comparison_{page + 1}.png')
result = {
    'source_range_frames_half_open_zero_based': [20, 38],
    'source_time_range_seconds_half_open': [20 / 24, 38 / 24],
    'output_frames': 18, 'duration_seconds': 0.75,
    'video_and_audio_offset_seconds': 20 / 24,
    'exact_pcm_companion_equals_source_slice': True,
    'exact_pcm_companion_sha256': hashlib.sha256(companion).hexdigest(),
    'encoded_aac_pcm_bit_exact': encoded == expected,
    'encoded_aac_zero_lag_pcm_correlation': correlation,
    'frame_mapping': mapping,
    'actual_listening': 'NOT_PERFORMED', 'lip_sync': 'NOT_CERTIFIED',
    'status': 'TECHNICAL_SOURCE_MAPPING_ONLY_NOT_OWNER_APPROVAL',
}
(OUT / 'trim_check.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))

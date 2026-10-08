"""Read-only frame/PCM evidence for an exact source and its lettering repair."""
import argparse
import hashlib
import json
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


def pcm(path):
    with wave.open(str(path), 'rb') as stream:
        params = {'channels': stream.getnchannels(), 'rate': stream.getframerate(),
                  'sample_width': stream.getsampwidth(), 'frames': stream.getnframes()}
        data = stream.readframes(stream.getnframes())
    return params, data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-qc', type=Path, required=True)
    parser.add_argument('--repair-qc', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        parser.error('Use a new output directory; preserve all earlier evidence.')
    args.out.mkdir(parents=True)
    original = json.loads((args.source_qc / 'native_evidence.json').read_text(encoding='utf8'))
    repair = json.loads((args.repair_qc / 'native_evidence.json').read_text(encoding='utf8'))
    source_frames = sorted((args.source_qc / 'all_native_frames').glob('*.png'))
    repaired_frames = sorted((args.repair_qc / 'all_native_frames').glob('*.png'))
    comparisons = []
    # Every output frame is displayed, not a sample. Nearest source timestamp is explicit.
    for start in range(0, len(repaired_frames), 8):
        board = Image.new('RGB', (1200, 1112), '#181818')
        draw = ImageDraw.Draw(board)
        for cell, index in enumerate(range(start, min(start + 8, len(repaired_frames)))):
            time = repair['native_frame_timestamps'][index]
            source_index = min(range(len(source_frames)),
                               key=lambda i: abs(original['native_frame_timestamps'][i] - time))
            x, y = (cell % 4) * 300, (cell // 4) * 556
            for offset, file in [(0, source_frames[source_index]), (150, repaired_frames[index])]:
                image = Image.open(file).convert('RGB')
                image.thumbnail((150, 268))
                board.paste(image, (x + offset, y + 20))
                # Fixed native-pixel shirt region, inspect full images if registration drifts.
                crop = Image.open(file).convert('RGB').crop((155, 500, 600, 920))
                crop.thumbnail((150, 230))
                board.paste(crop, (x + offset, y + 300))
            draw.text((x + 3, y + 2), f'S{source_index} | R{index} / {time:.3f}s', fill='white')
            comparisons.append({'repair_frame': index, 'repair_time': time,
                                'source_frame': source_index,
                                'source_time': original['native_frame_timestamps'][source_index],
                                'board': f'all_frames_{start // 8 + 1:02d}.jpg'})
        board.save(args.out / f'all_frames_{start // 8 + 1:02d}.jpg', quality=95)
    source_params, source_data = pcm(args.source_qc / 'native_audio.wav')
    repair_params, repair_data = pcm(args.repair_qc / 'native_audio.wav')
    audio = {'source_params': source_params, 'repair_params': repair_params,
             'source_pcm_sha256': hashlib.sha256(source_data).hexdigest(),
             'repair_pcm_sha256': hashlib.sha256(repair_data).hexdigest(),
             'decoded_pcm_exactly_equal': source_params == repair_params and source_data == repair_data,
             'actual_listening': 'NOT_PERFORMED', 'lip_sync': 'NOT_CERTIFIED'}
    if source_params['sample_width'] == repair_params['sample_width'] == 2:
        a = np.frombuffer(source_data, dtype='<i2').astype(float)
        b = np.frombuffer(repair_data, dtype='<i2').astype(float)
        length = min(len(a), len(b))
        audio['zero_lag_correlation_overlap'] = float(np.corrcoef(a[:length], b[:length])[0, 1])
        audio['overlap_samples'] = length
        audio['correlation_not_proof_of_voice_or_sync'] = True
    report = {'source_sha256': original['sha256'], 'repair_sha256': repair['sha256'],
              'comparisons': comparisons, 'all_output_frames_in_boards': len(comparisons),
              'audio': audio, 'status': 'EVIDENCE_ONLY_NOT_QUALITY_OR_RELEASE_PASS'}
    (args.out / 'comparison.json').write_text(json.dumps(report, indent=2), encoding='utf8')
    print(json.dumps({'frames': len(comparisons), 'audio': audio}))


if __name__ == '__main__':
    main()

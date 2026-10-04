"""Bounded batch177 voice-context review, not voice acceptance or final delivery."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MEDIA = Path('C:/Users/PC/Downloads/du_an_nem_bui')
OUT = MEDIA / '177_opening_voice'
FF = ROOT / '.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/ffmpeg.exe'
MIDDLE = MEDIA / '175_k20_d06_dialogue/B01_VOICE_PENDING.wav'
CLOSING = MEDIA / '154_visual_lock/R01.mp4'
expected = {
    'A01': ('2da4f3fb-7ab5-44ff-8f86-80eeb4948020', '39e6ec3a2caa0f37e70628db15fae8ae0022e0c3893258b475241abd1c9a6e75'),
    'A02': ('a053520b-6765-46be-8b47-7a8081229b11', '73264fe40791872afa7102bb59c9df8f4ca3dbe5101fc7ca8aa5a5b4666cd4a7'),
    'A03': ('eac27f20-f059-48f6-a5cb-ef30f50a1e52', '8f7486e03b97cafeef4cc9b8dada598146aafa3da8d12c5d5ba59ab3a5190370'),
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pcm(path):
    return subprocess.check_output([str(FF), '-v', 'error', '-i', str(path), '-vn', '-acodec', 'pcm_s16le', '-f', 's16le', '-'])


def probe(path):
    return json.loads(subprocess.check_output([str(FF.with_name('ffprobe.exe')), '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(path)], text=True))


assert sha(MIDDLE) == '3861280b335e1f8c9249dd484cd63a8432f5a89c2c15dca5a81c3764b1ec0d5e'
prior = ROOT / 'he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/evidence/176/assembly-manifest.json'
closing_hash = json.loads(prior.read_text(encoding='utf-8'))['audio_slots'][2]['source_sha256']
assert sha(CLOSING) == closing_hash
middle_pcm, closing_pcm = pcm(MIDDLE), pcm(CLOSING)
report = {
    'date': '2026-10-04', 'status': 'THREE_NATIVE_DECODED_OWNER_OPENING_LISTENING_PENDING',
    'account_before': 296, 'account_after': 275, 'actual_credits_spent': 21,
    'project_cap': 155, 'project_spent': 151, 'project_remaining': 4,
    'generation_submissions': 1, 'outputs': 3, 'local_review_credit_spend': 0,
    'independent_audio_listening_by_root': False,
    'asr_method': 'faster-whisper small CPU int8 offline Vietnamese; no initial prompt',
    'context_middle': {'path': str(MIDDLE), 'sha256': sha(MIDDLE), 'status': 'OWNER_TEST_ACCEPTED_176_B01_WORKING_SOURCE'},
    'context_closing': {'path': str(CLOSING), 'sha256': sha(CLOSING), 'status': 'OWNER_REUSE_APPROVED_168'},
    'context_note': 'Full opening10s + middle10s + closing8s; no action gap. Review audio only, not 30s film timing or acceptance.',
    'media': [],
}
for label, (media_id, native_hash) in expected.items():
    source, voice = OUT / f'{label}.mp4', OUT / f'{label}_VOICE_REVIEW.wav'
    assert sha(source) == native_hash, f'{label} native changed'
    native_pcm, voice_pcm = pcm(source), pcm(voice)
    assert native_pcm == voice_pcm, f'{label} extraction changed PCM'
    metadata = probe(source)
    segments = json.loads((ROOT / f'artifacts/voice-qc/177-{label}/asr.json').read_text(encoding='utf-8'))['segments']
    context = OUT / f'{label}_9-cau_REVIEW.wav'
    subprocess.run([
        str(FF), '-v', 'error', '-n', '-i', str(voice), '-i', str(MIDDLE), '-i', str(CLOSING),
        '-filter_complex', '[0:a][1:a][2:a]concat=n=3:v=0:a=1[a]', '-map', '[a]', '-c:a', 'pcm_s16le', str(context),
    ], check=True)
    context_pcm = pcm(context)
    assert context_pcm == native_pcm + middle_pcm + closing_pcm, f'{label} context differs from exact source PCM order'
    context_duration = len(context_pcm) / (48000 * 2 * 2)
    report['media'].append({
        'label': label, 'id': media_id, 'bytes': source.stat().st_size, 'mp4_sha256': native_hash,
        'wav_sha256': sha(voice), 'mp4_wav_pcm_sha256': hashlib.sha256(voice_pcm).hexdigest(),
        'pcm_match': True, 'full_decode': 'PASS', 'duration': metadata['format']['duration'],
        'video': {k: metadata['streams'][0][k] for k in ('codec_name', 'width', 'height', 'r_frame_rate')},
        'voice_review': 'OWNER_PENDING', 'visual_review': 'REWORK_SAMPLED_ONLY_NOT_FOR_MASTER',
        'asr_segments': [{'start': s['start'], 'end': s['end'], 'text': s['text']} for s in segments],
        'context_file': str(context), 'context_seconds': context_duration, 'context_sha256': sha(context),
        'context_pcm_mapping': 'PASS_EXACT_OPENING_THEN_MIDDLE_THEN_CLOSING_NO_GAIN_SPEED_OR_REORDER',
    })
(OUT / 'results.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))

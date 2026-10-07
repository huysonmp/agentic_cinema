"""Check production-only decision, cancelled draft and unchanged source identities."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EP = ROOT / 'he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot'
EV = EP / 'evidence/228'

def sha(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()

def main():
    decision = json.loads((EV / 'owner-production-direction.json').read_text(encoding='utf-8'))
    old_request = json.loads((EP / 'evidence/227/motion-request-DRAFT.json').read_text(encoding='utf-8'))
    assert decision['separate_hand_test_status'] == 'CANCELLED_BEFORE_SUBMISSION'
    assert old_request['status'] == 'CANCELLED_BY_OWNER_BEFORE_SUBMISSION_SEE_REC228'
    assert not decision['standalone_tests_authorized']
    assert decision['generation_submissions_this_record'] == decision['credit_spent_this_record'] == 0
    ax = (EV / 'cancelled-test-draft-ax.txt').read_text(encoding='utf-8')
    assert 'Create one continuous eight-second' not in ax
    assert 'button (disabled) Bắt đầu tạo' in ax
    assert '77 tín dụng Google Flow' in (EV / 'balance-live-ax.txt').read_text(encoding='utf-8')
    sources = [
        ('N02_B', Path('C:/Users/PC/Downloads/du_an_nem_bui/221_n02_pa_v_trial/N02_B_NATIVE.mp4'),
         '660f175775db6b082458846edb5c8edc8beb771b90a3330f53cb37d07f31a535'),
        ('N01_AUDIO', Path('C:/Users/PC/Downloads/du_an_nem_bui/183_speaker_audit/N01_intended_Dao_UNVERIFIED.wav'),
         '366e95086c57dc1c5d2a2d366d6b24410ab85b0dcc7b2f2d4fbb61d3aa69cfe1'),
    ]
    for key in ('start', 'end'):
        row = old_request[key]
        sources.append((row['id'], Path(row['native_path']), row['native_sha256']))
    rows = []
    for label, path, expected in sources:
        observed = sha(path)
        assert observed == expected, f'Source mismatch: {label}'
        rows.append(dict(id=label, path=str(path), sha256=observed, matches_expected=True))
    result = dict(record_id='REC228', owner_direction_verified=True,
                  cancelled_flow_prompt_absent=True, submit_disabled=True,
                  balance_live=77, submissions=0, credit_spent=0,
                  original_sources=rows, first_production_request_ready=False,
                  blocker='R01 causal Khoan stop versus unchanged N02-B opening picture needs coverage decision',
                  actual_audio_hearing=False, full_av_pass=False)
    (EV / 'root-readback.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'source_hashes_verified':len(rows), 'cancelled_draft_verified':True,
                      'balance':77, 'spent':0, 'production_request_ready':False}))

if __name__ == '__main__':
    main()

"""Record native v03, source identity and visual QA boards for REC226."""
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
EP = ROOT / 'he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot'
EV = EP / 'evidence/226'
OWNER = Path('C:/Users/PC/Downloads/du_an_nem_bui/226_ref01_m_v03_from_s')
SOURCE = Path('C:/Users/PC/Downloads/du_an_nem_bui/224_g1_opening_refs_v01/REF01-S_v01_NATIVE.jpg')
PRIOR = Path('C:/Users/PC/Downloads/du_an_nem_bui/225_g1_repaired_refs_v02/REF01-M_v02_NATIVE.jpg')
ORIGINAL = Path('C:/Users/PC/Downloads/REF01-S_v01_REC224_20261007103419.jpg')
NATIVE = OWNER / 'REF01-M_v03_NATIVE.jpg'
REPO = EP / 'media/226_ref01_m_v03_from_s/REF01-M_v03_NATIVE.jpg'
PROMPT = EP / 'evidence/225/REF01-M.repair-v03-DRAFT.txt'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    approval = json.loads((EV / 'owner-approval.json').read_text(encoding='utf-8'))
    assert approval['max_requests'] == 1 and approval['total_credit_cap'] == 0
    assert sha(SOURCE) == approval['source_sha256']
    assert len({sha(p) for p in (ORIGINAL, NATIVE, REPO)}) == 1
    exact = PROMPT.read_text(encoding='utf-8').strip()
    for filename in ('pre-submit-ax.txt', 'result-full-ax.txt'):
        assert exact in (EV / filename).read_text(encoding='utf-8')
    assert '0 tín dụng' in (EV / 'pre-submit-ax.txt').read_text(encoding='utf-8')
    assert '77 tín dụng Google Flow' in (EV / 'balance-after-ax.txt').read_text(encoding='utf-8')
    with Image.open(NATIVE) as im:
        im.verify()
    with Image.open(NATIVE) as im:
        dimensions, fmt = list(im.size), im.format
    payload = dict(record_id='REC226', submissions=1, retries=0, quote_credits=0,
        previous_run_balance=77, same_turn_balance_before=None, balance_after=77,
        observed_balance_delta=None, billing_receipt_available=False,
        model_live='Nano Banana 2.1', requested_aspect='9:16', route='existing_asset_edit_history',
        source_flow_container_id=approval['source_flow_asset_id'],
        source_flow_image_id='22a0d77a-c8db-4a62-82ef-9ed93d34e7f2',
        output_flow_image_id='944bb01f-da47-4b68-8281-2aa5c04c546a',
        output_is_separate_flow_container=False, flow_container_label='REF01-S_v01_REC224',
        source_path=str(SOURCE), source_sha256=sha(SOURCE),
        prompt_path=str(PROMPT), prompt_sha256=sha(PROMPT), exact_prompt_verified=True,
        download_original=str(ORIGINAL), owner_native=str(NATIVE), repo_native=str(REPO),
        native_sha256=sha(NATIVE), native_dimensions=dimensions, native_format=fmt,
        copies_equal=True, qc_status='PENDING_INDEPENDENT_REVIEW',
        owner_output_accepted=False, full_g1_approved=False, motion_tested=False,
        video_generated=False, voice_generated=False)
    (EV / 'native-output-manifest.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 19)
    board = Image.new('RGB', (1080, 710), '#161d25')
    draw = ImageDraw.Draw(board)
    for i, (label, path) in enumerate((('Source S v01', SOURCE), ('M v02 - HOLD', PRIOR), ('M v03 - CANDIDATE', NATIVE))):
        draw.text((i*360+8, 10), label, fill='white', font=font)
        with Image.open(path) as im:
            im.thumbnail((360, 670), Image.Resampling.LANCZOS)
            board.paste(im, (i*360+(360-im.width)//2, 40))
    board.save(OWNER / 'REC226_SOURCE_V02_V03.png')
    with Image.open(NATIVE) as im:
        im.crop((420, 820, 768, 1210)).resize((696, 780), Image.Resampling.LANCZOS).save(OWNER / 'REC226_HAND_DETAIL.png')
    print(json.dumps({'copies_equal':True, 'exact_prompt_verified':True, 'dimensions':dimensions, 'native_sha256':sha(NATIVE)}, indent=2))

if __name__ == '__main__':
    main()

"""Verify separated Flow inputs and build the static motion-preflight board."""
import hashlib
import json
import shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
EP = ROOT / 'he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot'
EV = EP / 'evidence/227'
OWNER = Path('C:/Users/PC/Downloads/du_an_nem_bui/227_motion_preflight')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    request = json.loads((EV / 'motion-request-DRAFT.json').read_text(encoding='utf-8'))
    approval = json.loads((EV / 'owner-reference-approval.json').read_text(encoding='utf-8'))
    assert request['end']['native_sha256'] == approval['accepted_native_sha256']
    assert not approval['paid_motion_request_approved']
    exact = (EV / request['prompt_file']).read_text(encoding='utf-8').strip()
    preflight = (EV / 'motion-preflight-DRAFT-ax.txt').read_text(encoding='utf-8')
    assert exact in preflight
    assert '10 tín dụng' in preflight
    assert request['requests_proposed'] * request['quote_each_credits_live'] == request['credit_cap_proposed'] == 30
    OWNER.mkdir(parents=True, exist_ok=True)
    rows = []
    for key in ('start', 'end'):
        entry = request[key]
        native, downloaded = Path(entry['native_path']), Path(entry['separated_download'])
        assert sha(native) == sha(downloaded) == entry['native_sha256']
        owner_copy = OWNER / (entry['id'] + '.jpg')
        shutil.copy2(native, owner_copy)
        assert sha(owner_copy) == entry['native_sha256']
        with Image.open(owner_copy) as im:
            im.verify()
        with Image.open(owner_copy) as im:
            dimensions = list(im.size)
        rows.append(dict(role=key, id=entry['id'], flow_asset_id=entry['flow_asset_id'],
            flow_image_id=entry['flow_image_id'], source_native=str(native),
            separated_download=str(downloaded), owner_copy=str(owner_copy),
            native_sha256=sha(native), native_dimensions=dimensions, copies_equal=True,
            approval_scope=entry['status']))
    result = dict(record_id='REC227', inputs=rows,
        prompt_sha256=sha(EV / request['prompt_file']), exact_prompt_in_live_draft=True,
        separate_assets_verified=True, quote_each_credits_live=10,
        proposed_take_count=3, proposed_cap=30, generation_submissions=0,
        retries=0, video_generated=False, video_quality_verified=False)
    (EV / 'input-readback.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 19)
    board = Image.new('RGB', (720, 720), '#161d25')
    draw = ImageDraw.Draw(board)
    for i, row in enumerate(rows):
        draw.text((i*360+8, 10), 'START S v01' if i == 0 else 'END M v03 - accepted pose', fill='white', font=font)
        with Image.open(row['owner_copy']) as im:
            im.thumbnail((360, 650), Image.Resampling.LANCZOS)
            board.paste(im, (i*360+(360-im.width)//2, 42))
    draw.text((8, 690), 'STATIC INPUTS / MOTION NOT TESTED', fill='white', font=font)
    board.save(OWNER / 'REC227_S_TO_M_INPUTS.png')
    print(json.dumps({'verified_inputs':2, 'copies_equal':True, 'prompt_matches':True, 'generation_submissions':0}, indent=2))

if __name__ == '__main__':
    main()

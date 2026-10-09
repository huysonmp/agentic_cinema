"""REC261 every-frame still evidence: both faces and chopstick/cup path, not AV approval."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--qc', type=Path, required=True)
p.add_argument('--out', type=Path, required=True)
a = p.parse_args()
e = json.loads((a.qc/'native_evidence.json').read_text(encoding='utf8'))
frames = sorted((a.qc/'all_native_frames').glob('*.png'))
assert len(frames) == e['extracted_frames']
a.out.mkdir(exist_ok=False)
pages = []
for start in range(0,len(frames),8):
    board = Image.new('RGB',(1200,1520),'#181818')
    d = ImageDraw.Draw(board)
    indices = list(range(start,min(start+8,len(frames))))
    for cell,idx in enumerate(indices):
        im = Image.open(frames[idx]).convert('RGB')
        assert im.size == (720,1280)
        x,y = (cell%2)*600,(cell//2)*380
        full=im.copy(); full.thumbnail((195,347)); board.paste(full,(x,y))
        faces=im.crop((0,330,720,680)); faces.thumbnail((395,165)); board.paste(faces,(x+200,y))
        table=im.crop((0,690,720,1120)); table.thumbnail((395,180)); board.paste(table,(x+200,y+167))
        d.text((x+3,y+353),f'F{idx} / {e["native_frame_timestamps"][idx]:.6f}s',fill='white')
    name=f'action_all_{start//8+1:02d}.jpg'
    board.save(a.out/name,quality=96)
    pages.append({'file':name,'frames':indices})
(a.out/'manifest.json').write_text(json.dumps({'target_sha256':e['sha256'],'scope':'ALL_FRAME_STILLS_NOT_AV','pages':pages},indent=2),encoding='utf8')
print(json.dumps({'frames':len(frames),'pages':len(pages),'target_sha256':e['sha256']}))

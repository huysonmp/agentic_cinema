"""Local technical inspection/contact sheets; never assigns creative PASS."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def run(command):
    return subprocess.run(command, check=True, capture_output=True, text=True)


def sheet(paths, out, code, fps, columns, width=180):
    height = width * 16 // 9
    label = 26
    rows = (len(paths) + columns - 1) // columns
    board = Image.new("RGB", (columns * width, rows * (height + label)), "#161616")
    draw = ImageDraw.Draw(board)
    font = ImageFont.load_default(size=16)
    for i, path in enumerate(paths):
        with Image.open(path) as frame:
            tile = frame.convert("RGB").resize((width, height))
        x, y = i % columns * width, i // columns * (height + label)
        board.paste(tile, (x, y))
        draw.text((x + 4, y + height + 3), f"{code} {i/fps:.3f}s", font=font, fill="white")
    board.save(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--ffmpeg", required=True)
    parser.add_argument("--ffprobe", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    sources = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    target = Path(args.output)
    if target.exists() and any(target.iterdir()):
        raise SystemExit("Refuse to overwrite nonempty inspection directory")
    target.mkdir(parents=True, exist_ok=True)
    report = []
    for item in sources:
        code, source = item["code"], Path(item["source"])
        payload = source.read_bytes()
        digest = hashlib.sha256(payload).hexdigest()
        copied = target / f"{code}.mp4"
        copied.write_bytes(payload)
        probe = json.loads(run([args.ffprobe, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(copied)]).stdout)
        video = next(stream for stream in probe["streams"] if stream["codec_type"] == "video")
        if video["r_frame_rate"] != "24/1" or abs(float(probe["format"]["duration"]) - 8) > 0.01:
            raise RuntimeError("Contact sheet timestamps require this pilot's 24fps/8s source")
        decode = run([args.ffmpeg, "-v", "error", "-i", str(copied), "-f", "null", "-"])
        if decode.stderr.strip():
            raise RuntimeError(f"{code} decode errors: {decode.stderr}")
        frames = target / f"{code}_frames"
        frames.mkdir()
        run([args.ffmpeg, "-v", "error", "-i", str(copied), "-vf", "fps=2", "-frames:v", "16", str(frames / "full_%03d.png")])
        run([args.ffmpeg, "-v", "error", "-i", str(copied), "-t", "3", str(frames / "opening_%03d.png")])
        sheet(sorted(frames.glob("full_*.png")), target / f"{code}-full-grid.png", code, 2, 4, 240)
        opening = sorted(frames.glob("opening_*.png"))
        sheet(opening, target / f"{code}-opening-all72.png", code, 24, 8)
        report.append({**item, "native": str(copied), "sha256": digest, "bytes": len(payload), "probe": probe, "decode_clean": True, "opening_frames": len(opening), "creative_qc": "NOT_AUTOMATIC"})
    (target / "technical-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps([{k: r[k] for k in ("code", "sha256", "bytes", "decode_clean", "opening_frames")} for r in report], indent=2))


if __name__ == "__main__":
    main()

"""Render two silent local opening diagnostics; never a production approval."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

SOURCE_HASH = "A3D80F09BFB7242BAE3007AD7B4F37473BB2F0ED019A84CC4956C4D32A8DBF9A"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--bin", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    source = args.source.resolve(strict=True)
    if sha(source) != SOURCE_HASH:
        raise SystemExit("Source differs from the approved diagnostic OPEN7.")
    if args.out.exists():
        raise SystemExit("Output folder exists; choose a new revision, never overwrite.")
    args.out.mkdir(parents=True)
    # Fit rather than stretch; any tiny ratio mismatch receives black padding.
    preparation = "scale=2160:3840:force_original_aspect_ratio=decrease,pad=2160:3840:(ow-iw)/2:(oh-ih)/2"
    ease = "(on/95)*(on/95)*(3-2*on/95)"
    variants = {
        "A_static": "zoompan=z=1:x=0:y=0:d=96:s=1080x1920:fps=24",
        # Right-edge anchoring protects the glass near the image's right border.
        "B_gentle_push": f"zoompan=z='1+0.015*({ease})':x='iw-iw/zoom':y='(ih-ih/zoom)/2':d=96:s=1080x1920:fps=24",
    }
    manifest = {"status": "LOCAL_SILENT_DIAGNOSTIC_NOT_PRODUCTION", "source": str(source),
                "source_sha256": SOURCE_HASH, "duration_target": 4, "fps": 24,
                "note": "2D push, not a 3D camera tilt; no generated acting, voice or new facts.",
                "outputs": []}
    for name, motion in variants.items():
        target = args.out / f"{name}.mp4"
        command = [str(args.bin / "ffmpeg.exe"), "-nostdin", "-n", "-v", "error",
                   "-i", str(source), "-vf", preparation + "," + motion,
                   "-frames:v", "96", "-an", "-c:v", "libx264", "-preset", "medium",
                   "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(target)]
        subprocess.run(command, check=True)
        probe = subprocess.run([str(args.bin / "ffprobe.exe"), "-v", "error",
                                "-show_format", "-show_streams", "-of", "json", str(target)],
                               check=True, capture_output=True, text=True)
        metadata = json.loads(probe.stdout)
        stream = metadata["streams"][0]
        if (stream["width"], stream["height"], stream["nb_frames"]) != (1080, 1920, "96"):
            raise RuntimeError("Unexpected render dimensions or frame count.")
        subprocess.run([str(args.bin / "ffmpeg.exe"), "-v", "error", "-i", str(target),
                        "-f", "null", "-"], check=True)
        manifest["outputs"].append({"name": name, "path": str(target.resolve()),
                                    "sha256": sha(target), "command": command,
                                    "metadata": metadata, "decode": "CLEAN"})
    if sha(source) != SOURCE_HASH:
        raise RuntimeError("Source changed during rendering.")
    (args.out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps([{k: item[k] for k in ("name", "path", "sha256")} for item in manifest["outputs"]], indent=2))


if __name__ == "__main__":
    main()

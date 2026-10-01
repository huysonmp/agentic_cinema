"""Create bounded local concat diagnostics from V01; never a production cut."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path


def mapping_findings(expected, actual):
    """Exact source/version/in/out mapping, not duration-only QC."""
    return [] if expected == actual else ["SOURCE_MAPPING_MISMATCH"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--ffmpeg-bin", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    source = args.input.resolve(strict=True)
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    if source_hash != "A291BF77C9B913DE43A006F4737DFCB5D27DA2E9811CA6812BDC045C6E81BF76".lower():
        raise SystemExit("This bounded diagnostic is approved for exact V01 only.")
    if args.out.exists():
        raise SystemExit("Use a fresh diagnostic directory, never overwrite.")
    args.out.mkdir(parents=True)
    evidence = {"mode": "LOCAL_CONCAT_DIAGNOSTIC_NOT_PRODUCTION", "source": str(source),
                "source_sha256": source_hash, "split_seconds": 2.5, "outputs": []}
    pieces = {"A": [0, 2.5], "B": [2.5, 8]}
    expected = [{"source_sha256": source_hash, "in": pieces[k][0], "out": pieces[k][1]} for k in ["A", "B"]]
    for label, order in [("control", ["A", "B"]), ("repeat", ["A", "B", "B"])]:
        target = args.out / (label + ".mp4")
        filters, refs = [], []
        for i, key in enumerate(order):
            start, end = pieces[key]
            filters += [f"[0:v]trim=start={start}:end={end},setpts=PTS-STARTPTS[v{i}]",
                        f"[0:a]atrim=start={start}:end={end},asetpts=PTS-STARTPTS[a{i}]"]
            refs.append(f"[v{i}][a{i}]")
        filters.append("".join(refs) + f"concat=n={len(order)}:v=1:a=1[v][a]")
        command = [str(args.ffmpeg_bin / "ffmpeg.exe"), "-nostdin", "-n", "-i", str(source),
                   "-filter_complex", ";".join(filters), "-map", "[v]", "-map", "[a]",
                   "-c:v", "libx264", "-preset", "fast", "-crf", "23", "-c:a", "aac",
                   "-movflags", "+faststart", str(target)]
        with (args.out / (label + "-render.log")).open("w", encoding="utf-8") as log:
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=log)
        probe = subprocess.run([str(args.ffmpeg_bin / "ffprobe.exe"), "-v", "error",
                                "-show_format", "-show_streams", "-of", "json", str(target)],
                               check=True, capture_output=True, text=True, encoding="utf-8")
        metadata = json.loads(probe.stdout)
        mapping = [{"source_sha256": source_hash, "in": pieces[k][0], "out": pieces[k][1]} for k in order]
        evidence["outputs"].append({"label": label, "path": str(target.resolve()),
                                    "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                                    "expected_mapping": expected, "executed_mapping": mapping,
                                    "target_duration": 8, "rendered_duration": metadata["format"]["duration"],
                                    "metadata": metadata, "command": command})
    if hashlib.sha256(source.read_bytes()).hexdigest() != source_hash:
        raise RuntimeError("Source changed during diagnostic")
    (args.out / "manifest.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps([{k: row[k] for k in ("label", "path", "rendered_duration", "sha256")}
                      for row in evidence["outputs"]], indent=2))


if __name__ == "__main__":
    main()

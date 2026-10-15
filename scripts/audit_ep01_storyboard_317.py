"""Read-only provenance/range arithmetic audit. Never certifies story, AV or release.

Prints JSON to stdout. No media rendering, pixel edits, downloads or API calls.
All EDL ranges are zero-based, half-open. Segment windows are NOT speech bounds.
"""
import argparse
import hashlib
import json
import struct
import subprocess
from fractions import Fraction
from pathlib import Path


EP = Path("he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot")
DIALOGUE_SHOTS = {
    "C01A_BM_BR", "C02", "C03A", "C03B", "C05",
    "C06_C07_EXACT_ACCEPTED_BLOCK308",
}


def validate_edl(edl, source_frames):
    fps = Fraction(str(edl["fps"]))
    if fps <= 0:
        raise ValueError("Non-positive fps")
    lengths = {}
    cursor = 0
    for seg in edl["segments"]:
        lo, hi = seg["range"]
        start, end = seg["timeline"]
        if not all(type(v) is int for v in (lo, hi, start, end)):
            raise ValueError("Non-integral range")
        if not 0 <= lo < hi <= source_frames[seg["input"]]:
            raise ValueError("Source range outside native bounds")
        if start != cursor or end - start != hi - lo:
            raise ValueError("Gap, overlap or length mismatch")
        if seg["shot"] in lengths:
            raise ValueError("Duplicate shot id")
        lengths[seg["shot"]] = hi - lo
        cursor = end
    if cursor != edl["expected_video_frames"]:
        raise ValueError("EDL total differs from expected frames")
    if Fraction(cursor, 1) / fps != Fraction(str(edl["expected_seconds"])):
        raise ValueError("EDL duration mismatch")
    dialogue = sum(v for k, v in lengths.items() if k in DIALOGUE_SHOTS)
    target = 30 * fps
    if target.denominator != 1:
        raise ValueError("Non-integral final30 frame target")
    target = int(target)
    return {
        "fps": str(fps),
        "rough_frames": cursor,
        "rough_seconds": float(Fraction(cursor, 1) / fps),
        "segment_frames": lengths,
        "dialogue_bearing_segment_windows_frames": dialogue,
        "dialogue_bearing_segment_windows_seconds": float(Fraction(dialogue, 1) / fps),
        "non_dialogue_segment_windows_frames": cursor - dialogue,
        "non_dialogue_segment_windows_seconds": float(Fraction(cursor - dialogue, 1) / fps),
        "target30_frames": target,
        "reduction_to_target_frames": cursor - target,
        "reduction_to_target_seconds": float(Fraction(cursor - target, 1) / fps),
        "remaining_for_non_dialogue_if_other_windows_unchanged_frames": target - dialogue,
        "remaining_for_non_dialogue_if_other_windows_unchanged_seconds": float(Fraction(target - dialogue, 1) / fps),
        "C04_current_last_frame": next(s for s in edl["segments"] if s["shot"] == "C04")["range"][1] - 1,
        "C04_reference_frame": 143,
        "C04_if_extend_end_to_144_extra_frames": 144 - next(s for s in edl["segments"] if s["shot"] == "C04")["range"][1],
        "speech_minimum_measured": False,
        "new_timeline_or_ranges_approved": False,
    }


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def png_size(path):
    with path.open("rb") as source:
        header = source.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError("Not a PNG with leading IHDR")
    return struct.unpack(">II", header[16:24])


def probe(path, executable):
    result = json.loads(subprocess.check_output([
        str(executable), "-v", "error", "-count_frames", "-show_streams",
        "-show_format", "-of", "json", str(path),
    ], text=True, encoding="utf-8"))
    video = next(s for s in result["streams"] if s["codec_type"] == "video")
    return {
        "frames": int(video["nb_read_frames"]),
        "fps": video["avg_frame_rate"],
        "width": video["width"], "height": video["height"],
        "video_seconds": video.get("duration"),
        "audio_seconds": [s.get("duration") for s in result["streams"] if s["codec_type"] == "audio"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--ffprobe", type=Path, required=True)
    opts = parser.parse_args()
    base = opts.root.resolve() / EP / "restart_720p_v1"
    edl_path = base / "07_edits/EP01_ROUGH35_TRIAL_edl_312.json"
    edl = json.loads(edl_path.read_text(encoding="utf-8"))
    source_rows = []
    source_frames = {}
    for source in edl["sources"]:
        path = base / source["path"]
        measured = probe(path, opts.ffprobe)
        actual_hash = sha(path)
        if actual_hash != source["sha256"]:
            raise ValueError(f"Source hash mismatch: {source['path']}")
        if Fraction(measured["fps"]) != Fraction(str(edl["fps"])):
            raise ValueError("Source fps mismatch")
        if (measured["width"], measured["height"]) != (720, 1280):
            raise ValueError("Unexpected source size")
        source_frames[source["input"]] = measured["frames"]
        source_rows.append({**source, "measured": measured, "hash_matches": True})
    reference_rows = []
    decisions = [
        "00_decisions/first-closeup-reference-approval-315.json",
        "00_decisions/caught-excuse-reference-approval-316.json",
        "00_decisions/receive-ending-handshift-approval-317.json",
    ]
    for rel in decisions:
        decision = json.loads((base / rel).read_text(encoding="utf-8"))
        for item in decision["approved_images"]:
            path = base / item["file"]
            if sha(path) != item["sha256"]:
                raise ValueError(f"Reference hash mismatch: {item['file']}")
            width, height = png_size(path)
            reference_rows.append({
                **item, "approval_record": rel,
                "hash_matches": True, "width": width, "height": height,
                "exact_9_16": width * 16 == height * 9,
                "approval_scope": "STILL_DIRECTION_ONLY_NOT_NATIVE_AV",
            })
    c02 = json.loads((base / "00_decisions/C02-export-approval-246.json").read_text(encoding="utf-8"))
    c02_path = base / c02["target_file"]
    if sha(c02_path) != c02["target_sha256"]:
        raise ValueError("C02 approved export hash mismatch")
    rough_path = base / edl["target"]
    if sha(rough_path) != edl["target_sha256"]:
        raise ValueError("Rough312 hash mismatch")
    rough_probe = probe(rough_path, opts.ffprobe)
    if rough_probe["frames"] != edl["expected_video_frames"]:
        raise ValueError("Rough decoded frame count mismatch")
    print(json.dumps({
        "record": "REC317", "date": "2026-10-15",
        "status": "PROVENANCE_AND_EDL_ARITHMETIC_VERIFIED_NOT_AV_OR_FINAL30_PASS",
        "edl_file": str(edl_path.relative_to(base)).replace("\\", "/"),
        "edl_sha256": sha(edl_path),
        "sources": source_rows, "approved_reference_images": reference_rows,
        "C02_exact_approved_export": {
            "path": c02["target_file"], "sha256": c02["target_sha256"],
            "hash_matches": True, "measured": probe(c02_path, opts.ffprobe),
            "new_camera_lipsync_approved": False,
        },
        "rough312": {"path": edl["target"], "sha256": edl["target_sha256"], "hash_matches": True, "measured": rough_probe},
        "timing": validate_edl(edl, source_frames),
        "Flow_credit_cost": 0, "new_video_or_voice": False,
        "continuous_motion_review": False, "audio_listening": False,
        "independent_agent_review": False, "paid_generation_authorized": False,
        "new_EDL_written": False,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

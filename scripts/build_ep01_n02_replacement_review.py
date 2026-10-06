"""Bounded EP01 seven-turn listening review. Not a production audio/master gate."""
import argparse
import hashlib
import json
import subprocess
import wave
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
EP = REPO / "he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot"
OWNER = Path("C:/Users/PC/Downloads/du_an_nem_bui")
N02_HASH = "52c7a027f55c6e354b0c5ac1d697bd8789682bfbc9ac99907a45e741f129b062"
CLOSING_HASH = "9530c8c8315a7e3653c43cc400e7ab8891f536256e4d7dfaee5b16f326e59b19"
EXCERPT_HASHES = {
    "N01": "366e95086c57dc1c5d2a2d366d6b24410ab85b0dcc7b2f2d4fbb61d3aa69cfe1",
    "N03": "30de99253ed78a37a6765f6bf28690063bd3888398d593263d417bec20bb2738",
    "N04": "47c55646041c878f15b53114ed3b5299b5b2cb99b018f1e90711c0a0181b0ec4",
}
FORMAT = (2, 2, 48000)


def checked_source(path, expected_hash):
    path = Path(path).resolve(strict=True)
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected_hash:
        raise ValueError(f"Source hash mismatch: {path}")
    return path


def read_pcm(path):
    with wave.open(str(path), "rb") as wav:
        if (wav.getnchannels(), wav.getsampwidth(), wav.getframerate()) != FORMAT:
            raise ValueError(f"Unexpected WAV format: {path}")
        if wav.getcomptype() != "NONE":
            raise ValueError("Only uncompressed PCM is supported")
        return wav.readframes(wav.getnframes())


def check_n02_approval(approval):
    if (approval.get("N02_owner_acceptance") != "APPROVED"
            or approval.get("reviewed_sha256") != N02_HASH
            or approval.get("observed_speaker_by_owner") != "Khoai"
            or approval.get("observed_preset_by_owner") != "K20"
            or approval.get("within_turn_consistency_by_owner") != "ACCEPTED_THROUGHOUT"):
        raise ValueError("Exact whole-N02 owner approval required")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--ffmpeg-bin", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise SystemExit("Use a fresh review directory; existing files are never overwritten")
    approval = json.loads((EP / "evidence/201/owner-approval.json").read_text(encoding="utf-8"))
    check_n02_approval(approval)
    audit = json.loads((EP / "evidence/183/speaker-audit.json").read_text(encoding="utf-8"))
    lines = {row["line_id"]: row for row in audit["lines"]}
    sources, blocks, mapping = [], [], []

    def add(path, source_hash, line_ids, source_description):
        path = checked_source(path, source_hash)
        pcm = read_pcm(path)
        start_frames = sum(len(block) // 4 for block in blocks)
        blocks.append(pcm)
        sources.append((path, source_hash))
        mapping.append({
            "line_ids": line_ids, "source": str(path), "source_sha256": source_hash,
            "source_description": source_description, "source_used": "WHOLE_WAV",
            "timeline_start_seconds": start_frames / 48000,
            "timeline_end_seconds": (start_frames + len(pcm) // 4) / 48000,
            "approved_texts": [lines[key]["approved_text"] for key in line_ids],
            "expected_speakers": [lines[key]["expected_speaker"] for key in line_ids],
            "owner_identity_approval": "201_N02_ONLY" if line_ids == ["N02"] else "NOT_ESTABLISHED_BY_201",
        })

    for key in ["N01", "N02", "N03", "N04"]:
        if key == "N02":
            add(approval["reviewed_artifact"], N02_HASH, [key], {
                "origin": "200_SINGLE_KHOAI_REPLACEMENT", "trim": "NONE", "whole_owner_approved_source": True,
            })
        else:
            row = lines[key]
            add(row["diagnostic_excerpt"], EXCERPT_HASHES[key], [key], {
                "origin": "183_EXISTING_DIAGNOSTIC_EXCERPT_NOT_FINAL_STEM",
                "original_source": row["source"], "original_in": row["source_in"],
                "original_out": row["source_out"], "new_trim": "NONE",
                "cut_boundary_heard_by_root": False,
            })

    closing = checked_source(OWNER / "154_visual_lock/R01.mp4", CLOSING_HASH)
    closing_command = [str(args.ffmpeg_bin / "ffmpeg.exe"), "-v", "error", "-nostdin",
                       "-i", str(closing), "-map", "0:a:0", "-vn", "-ac", "2", "-ar", "48000",
                       "-c:a", "pcm_s16le", "-f", "s16le", "pipe:1"]
    closing_pcm = subprocess.run(closing_command, capture_output=True, check=True).stdout
    if not closing_pcm or len(closing_pcm) % 4:
        raise ValueError("Invalid closing PCM")
    start_frames = sum(len(block) // 4 for block in blocks)
    blocks.append(closing_pcm)
    sources.append((closing, CLOSING_HASH))
    mapping.append({
        "line_ids": ["N05", "N06", "N07"], "source": str(closing), "source_sha256": CLOSING_HASH,
        "source_used": "FULL_AUDIO_DECODE_NO_TRIM", "decode_command": closing_command,
        "timeline_start_seconds": start_frames / 48000,
        "timeline_end_seconds": (start_frames + len(closing_pcm) // 4) / 48000,
        "approved_texts": [lines[key]["approved_text"] for key in ["N05", "N06", "N07"]],
        "expected_speakers": [lines[key]["expected_speaker"] for key in ["N05", "N06", "N07"]],
        "owner_identity_approval": "NOT_ESTABLISHED_BY_201",
    })
    executed_order = [key for block in mapping for key in block["line_ids"]]
    if executed_order != [f"N{index:02d}" for index in range(1, 8)]:
        raise ValueError("Seven-turn order mismatch")
    pcm = b"".join(blocks)
    args.out.mkdir(parents=True)
    output = args.out / "EP01_7_LUOT_N02_MOI_REVIEW_NOT_FINAL.wav"
    with wave.open(str(output), "wb") as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(48000)
        wav.writeframes(pcm)
    if read_pcm(output) != pcm:
        raise RuntimeError("Output PCM does not match exact ordered input blocks")
    for path, digest in sources:
        checked_source(path, digest)
    manifest = {
        "mode": "SEVEN_TURN_LISTENING_REVIEW_NOT_FINAL_OR_RELEASE",
        "output": str(output.resolve()), "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "duration_seconds": len(pcm) / (4 * 48000), "format": "PCM_S16LE_48000_STEREO",
        "mapping": mapping, "executed_line_order": executed_order,
        "old_N02_source_included": False, "reused_183_old_N02_excerpt": False,
        "new_N02_pcm_unchanged": True, "output_pcm_matches_ordered_sources": True,
        "source_hashes_unchanged_after_build": True, "gain_speed_pitch_fade_mix_added": False,
        "new_generation": False, "credit_spend": 0, "root_heard_audio": False,
        "owner_join_approval": "PENDING", "audio_selection_gate": "NOT_PASS_PENDING_FULL_REVIEW",
        "formal_SIA_all_turns_report": "NOT_CREATED", "picture_or_lipsync_review": "NOT_RUN",
        "limits": ["183 excerpts are diagnostic ranges, not ear-approved final edit points",
                   "Whole new N02 includes its complete tail; final pacing is not claimed",
                   "Closing retains its existing native sound and spacing",
                   "No narrative action pause or 30-second final timing has been added",
                   "PCM mapping proves source usage, not perceived speaker identity"],
    }
    (args.out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: manifest[key] for key in ("output", "output_sha256", "duration_seconds", "executed_line_order")}, ensure_ascii=False))


if __name__ == "__main__":
    main()

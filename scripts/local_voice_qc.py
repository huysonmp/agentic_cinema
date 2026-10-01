"""Local-only media inspection and unprompted Vietnamese ASR. Not a voice approval."""
import argparse
import hashlib
import json
import subprocess
from dataclasses import asdict
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--ffmpeg-bin", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--model", default="small")
    parser.add_argument("--model-cache", type=Path, required=True)
    parser.add_argument("--offline", action="store_true", help="Use cached model without network access")
    args = parser.parse_args()
    source = args.input.resolve(strict=True)
    args.out.mkdir(parents=True, exist_ok=True)
    report_path = args.out / "media.json"
    transcript_path = args.out / "asr.json"
    audio = args.out / "audio-16k-mono.wav"
    if any(p.exists() for p in (report_path, transcript_path, audio)):
        raise SystemExit("Use a fresh output directory; existing results are not overwritten.")
    probe = subprocess.run(
        [str(args.ffmpeg_bin / "ffprobe.exe"), "-v", "error", "-show_format",
         "-show_streams", "-of", "json", str(source)],
        check=True, capture_output=True, text=True, encoding="utf-8")
    media = json.loads(probe.stdout)
    media["input_sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    report_path.write_text(json.dumps(media, ensure_ascii=False, indent=2), encoding="utf-8")
    if not any(s["codec_type"] == "audio" for s in media["streams"]):
        raise SystemExit("No audio stream; transcription not run.")
    subprocess.run([str(args.ffmpeg_bin / "ffmpeg.exe"), "-nostdin", "-n",
                    "-i", str(source), "-vn", "-ac", "1", "-ar", "16000",
                    "-c:a", "pcm_s16le", str(audio)], check=True)
    with (args.out / "audio-diagnostics.log").open("w", encoding="utf-8") as log:
        subprocess.run([str(args.ffmpeg_bin / "ffmpeg.exe"), "-nostdin",
                        "-i", str(source), "-vn", "-af",
                        "volumedetect,silencedetect=noise=-40dB:d=0.3", "-f", "null", "-"],
                       check=True, stdout=subprocess.DEVNULL, stderr=log)
    from faster_whisper import WhisperModel
    model = WhisperModel(args.model, device="cpu", compute_type="int8",
                         download_root=str(args.model_cache), local_files_only=args.offline)
    segments, info = model.transcribe(str(audio), language="vi", beam_size=5,
                                      word_timestamps=True, vad_filter=False,
                                      condition_on_previous_text=False)
    rows = [asdict(s) for s in segments]
    payload = {"model": args.model, "device": "cpu", "compute_type": "int8",
               "language": info.language, "initial_prompt": None,
               "status": "ASR_EVIDENCE_ONLY_NOT_VOICE_APPROVAL", "segments": rows}
    transcript_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    text = "\n".join(s["text"].strip() for s in rows)
    (args.out / "transcript.txt").write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

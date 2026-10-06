"""Fail-closed checks for the bounded listening-review builder; not acoustic tests."""
import json
import tempfile
import unittest
import wave
from pathlib import Path

from build_ep01_n02_replacement_review import EP, N02_HASH, check_n02_approval, checked_source, read_pcm


class ReplacementReviewTests(unittest.TestCase):
    def setUp(self):
        self.approval = json.loads((EP / "evidence/201/owner-approval.json").read_text(encoding="utf-8"))

    def test_exact_owner_approval_accepted(self):
        check_n02_approval(self.approval)

    def test_missing_or_wrong_approval_blocked(self):
        for key, value in [("N02_owner_acceptance", "PENDING"), ("reviewed_sha256", "old-source"),
                           ("observed_speaker_by_owner", "Dao"), ("observed_preset_by_owner", "D06"),
                           ("within_turn_consistency_by_owner", "UNVERIFIED")]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                check_n02_approval({**self.approval, key: value})

    def test_wrong_source_hash_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "wrong.wav"
            path.write_bytes(b"not approved audio")
            with self.assertRaises(ValueError):
                checked_source(path, N02_HASH)

    def test_pcm_read_preserves_samples_and_rejects_mono(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.wav"
            for channels in [2, 1]:
                with wave.open(str(path), "wb") as wav:
                    wav.setnchannels(channels)
                    wav.setsampwidth(2)
                    wav.setframerate(48000)
                    wav.writeframes(b"\x01\x00\x02\x00")
                if channels == 2:
                    self.assertEqual(read_pcm(path), b"\x01\x00\x02\x00")
                else:
                    with self.assertRaises(ValueError):
                        read_pcm(path)


if __name__ == "__main__":
    unittest.main()

"""Arithmetic and failure-path tests; no production media required."""
import copy
import unittest
from audit_ep01_storyboard_317 import validate_edl


class EdlTests(unittest.TestCase):
    def setUp(self):
        self.edl = {
            "fps": 24, "expected_video_frames": 840, "expected_seconds": 35,
            "segments": [
                {"shot": "C02", "input": 0, "range": [0, 584], "timeline": [0, 584]},
                {"shot": "C04", "input": 1, "range": [12, 124], "timeline": [584, 696]},
                {"shot": "C08", "input": 2, "range": [0, 64], "timeline": [696, 760]},
                {"shot": "C09", "input": 3, "range": [8, 88], "timeline": [760, 840]},
            ],
        }
        self.frames = {0: 584, 1: 144, 2: 64, 3: 96}

    def test_arithmetic_is_not_speech_minimum(self):
        result = validate_edl(self.edl, self.frames)
        self.assertEqual(result["reduction_to_target_frames"], 120)
        self.assertEqual(result["remaining_for_non_dialogue_if_other_windows_unchanged_frames"], 136)
        self.assertFalse(result["speech_minimum_measured"])
        self.assertEqual(result["C04_current_last_frame"], 123)
        self.assertEqual(result["C04_if_extend_end_to_144_extra_frames"], 20)

    def test_reject_gap(self):
        self.edl["segments"][1]["timeline"][0] += 1
        with self.assertRaises(ValueError):
            validate_edl(self.edl, self.frames)

    def test_reject_source_overrun(self):
        self.frames[1] = 123
        with self.assertRaises(ValueError):
            validate_edl(self.edl, self.frames)

    def test_reject_overlap(self):
        self.edl["segments"][1]["timeline"] = [583, 695]
        with self.assertRaises(ValueError):
            validate_edl(self.edl, self.frames)

    def test_reject_incorrect_total(self):
        self.edl["expected_video_frames"] = 720
        with self.assertRaises(ValueError):
            validate_edl(self.edl, self.frames)

    def test_reject_zero_duration(self):
        self.edl["segments"][2]["range"] = [4, 4]
        with self.assertRaises(ValueError):
            validate_edl(self.edl, self.frames)

    def test_reject_duplicate_id(self):
        self.edl["segments"][2]["shot"] = "C04"
        with self.assertRaises(ValueError):
            validate_edl(self.edl, self.frames)

    def test_no_edl_mutation(self):
        before = copy.deepcopy(self.edl)
        validate_edl(self.edl, self.frames)
        self.assertEqual(before, self.edl)


if __name__ == "__main__":
    unittest.main()

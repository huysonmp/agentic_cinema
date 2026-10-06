import unittest
from build_ep01_frame_bound_review import place_pcm, validate_timeline


class TimelineTests(unittest.TestCase):
    def fixture(self):
        return {'fps':24,'duration_frames':720,'shots':[
            {'id':'a','in_frame':0,'out_frame':360,'source':'one','source_range_frames':[0,360],
             'selection_status':'ROOT_CANDIDATE_PENDING_AV'},
            {'id':'b','in_frame':360,'out_frame':720,'source':'one','source_range_frames':[360,720],
             'selection_status':'ROOT_CANDIDATE_PENDING_AV'}]}

    def test_exact_distinct_ranges(self):
        validate_timeline(self.fixture())

    def test_repeated_range_rejected(self):
        data = self.fixture()
        data['shots'][1]['source_range_frames'] = [0,360]
        with self.assertRaises(AssertionError):
            validate_timeline(data)

    def test_gap_rejected(self):
        data = self.fixture()
        data['shots'][1]['in_frame'] = 361
        with self.assertRaises(AssertionError):
            validate_timeline(data)

    def test_pending_without_selected_range_rejected(self):
        data = self.fixture()
        data['shots'][1]['selection_status'] = 'REWORK'
        with self.assertRaises(AssertionError):
            validate_timeline(data)

    def test_pcm_all_bytes_and_gap(self):
        raw = bytes(range(40))
        result = place_pcm(raw,[{'review_in':0,'review_out':2,'timeline_in':0},
                                {'review_in':2,'review_out':5,'timeline_in':10}],rate=2)
        self.assertEqual(result[:16],raw[:16])
        self.assertEqual(result[16:80],bytes(64))
        self.assertEqual(result[80:104],raw[16:])

    def test_pcm_drop_rejected(self):
        with self.assertRaises(AssertionError):
            place_pcm(bytes(range(40)),[{'review_in':0,'review_out':4,'timeline_in':0}],rate=2)


if __name__ == '__main__':
    unittest.main()

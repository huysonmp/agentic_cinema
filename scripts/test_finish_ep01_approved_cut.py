import copy
import unittest
from finish_ep01_approved_cut import validate_cues, srt_time


class CaptionTests(unittest.TestCase):
    def setUp(self):
        self.package={'lines':[{'id':'N01','speaker':'Đào','text':'Anh nhìn mãi.'},
                               {'id':'N02','speaker':'Khoai','text':'Khoan. Anh đứng chờ.'}]}
        self.cues=[{'line_id':'N01','speaker':'Đào','start':0,'end':1,'text':'Anh nhìn mãi.'},
                   {'line_id':'N02','speaker':'Khoai','start':1,'end':2,'text':'Khoan.'},
                   {'line_id':'N02','speaker':'Khoai','start':2,'end':3,'text':'Anh đứng chờ.'}]

    def test_exact(self):
        validate_cues(self.cues,self.package)

    def test_wrong_speaker_rejected(self):
        bad=copy.deepcopy(self.cues); bad[1]['speaker']='Đào'
        with self.assertRaises(AssertionError): validate_cues(bad,self.package)

    def test_typo_rejected(self):
        bad=copy.deepcopy(self.cues); bad[2]['text']='Anh đưng chờ.'
        with self.assertRaises(AssertionError): validate_cues(bad,self.package)

    def test_overlap_rejected(self):
        bad=copy.deepcopy(self.cues); bad[2]['start']=1.8
        with self.assertRaises(AssertionError): validate_cues(bad,self.package)

    def test_time(self):
        self.assertEqual(srt_time(21.95833333),'00:00:21,958')


if __name__=='__main__': unittest.main()

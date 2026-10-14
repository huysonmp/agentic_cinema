"""Deterministic scope tests; not a visual or AV approval."""
import unittest
import numpy as np
from repair_ep01_c07_mouth_307 import composite, register, feather, PATCH, EDIT_RANGE


class MouthScopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.closed = np.random.default_rng(307).integers(30,220,(1280,720,3),dtype=np.uint8)
        cls.opened = cls.closed.copy()
        cls.opened[540:570,205:277] = 0

    def test_unedited_frame_exact(self):
        for n in (0,4,15,71):
            result, meta = composite(self.opened,self.closed,self.closed,n)
            self.assertTrue(np.array_equal(result,self.opened))
            self.assertFalse(meta['altered'])

    def test_only_allowed_pixels_change(self):
        result, meta = composite(self.opened,self.closed,self.closed,10)
        changed = np.any(result!=self.opened,axis=2)
        x0,y0,x1,y1=PATCH
        self.assertGreater(meta['changed_pixels'],0)
        self.assertTrue(np.array_equal(result[540:570,205:277],self.closed[540:570,205:277]))
        changed[y0:y1,x0:x1]=False
        self.assertFalse(changed.any())

    def test_registration_measures_translation(self):
        target=np.roll(np.roll(self.closed,2,axis=0),-3,axis=1)
        target[540:570,205:277]=0
        move=register(self.closed,target)
        self.assertEqual((move['dx'],move['dy']),(-3,2))

    def test_temporal_scope(self):
        self.assertEqual(list(EDIT_RANGE),list(range(5,15)))

    def test_feather_stays_inside(self):
        alpha=feather()
        self.assertTrue(np.all(alpha[0]==0))
        self.assertTrue(np.all(alpha[-1]==0))
        self.assertEqual(float(alpha[32,58,0]),1)


if __name__=='__main__':
    unittest.main()

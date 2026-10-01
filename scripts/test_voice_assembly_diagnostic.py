import unittest
from voice_assembly_diagnostic import mapping_findings


class MappingTests(unittest.TestCase):
    def setUp(self):
        self.a = {"source_sha256": "a", "in": 0, "out": 3}
        self.b = {"source_sha256": "b", "in": 0, "out": 5}

    def test_clean(self):
        self.assertEqual([], mapping_findings([self.a, self.b], [self.a, self.b]))

    def test_repeat(self):
        self.assertTrue(mapping_findings([self.a, self.b], [self.a, self.b, self.b]))

    def test_reordered_same_duration(self):
        self.assertTrue(mapping_findings([self.a, self.b], [self.b, self.a]))

    def test_changed_version(self):
        self.assertTrue(mapping_findings([self.a, self.b], [self.a, dict(self.b, source_sha256="new")]))

    def test_changed_trim(self):
        self.assertTrue(mapping_findings([self.a, self.b], [self.a, dict(self.b, out=4.5)]))


if __name__ == "__main__":
    unittest.main()

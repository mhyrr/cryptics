import unittest
from romanize import variants


class T(unittest.TestCase):
    def test_plain(self):
        self.assertIn("LOGOS", variants("λόγος"))

    def test_rough_both_ways(self):
        v = variants("ὕπνος")
        self.assertIn("YPNOS", v)
        self.assertIn("HYPNOS", v)
        self.assertIn("HUPNOS", v)

    def test_kappa_and_phi(self):
        self.assertTrue({"KEPHALE", "CEPHALE", "KEFALE"} <= variants("κεφαλή"))

    def test_ou_and_nasal_gamma(self):
        self.assertIn("URANOS", variants("οὐρανός"))
        self.assertIn("ANGELOS", variants("ἄγγελος"))
        self.assertIn("AGGELOS", variants("ἄγγελος"))

    def test_rejects_mixed_script(self):
        self.assertEqual(variants("λόγ" + "o" + "ς"), set())   # Latin o inside a Greek word
        self.assertEqual(variants("abc"), set())


if __name__ == "__main__":
    unittest.main()

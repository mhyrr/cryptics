import unittest
from lookup import key, strip_frame, within_one
from run import skeleton, near, exact


class LookupRules(unittest.TestCase):
    def test_e2_development_pairs_join(self):
        for nominated, printed in (("Kriegsmann", "Kriegsman"), ("Reiter", "Reuter"), ("alter Mann", "Alter man"),
                                   ("Reiter", "Reitter"), ("Blume", "Blum"), ("Schlange", "Schlang")):
            self.assertEqual(key(nominated), key(printed))

    def test_distinct_words_stay_distinct(self):
        for a, b in (("Reiter", "Ritter"), ("Mann", "Mond"), ("Adler", "Ader"), ("Kriegsmann", "Kriegsman sein")):
            self.assertNotEqual(key(a), key(b))

    def test_frame_head_only(self):
        self.assertIn("Adler", strip_frame("Adlersgestalt"))
        self.assertIn("Schlange", strip_frame("Schlangengestalt"))
        self.assertEqual(strip_frame("Kriegsmann"), [])
        self.assertEqual(strip_frame("Goldmünze"), [])

    def test_ocr_tolerance_is_one_edit(self):
        self.assertTrue(within_one("uaser", "uafer"))
        self.assertFalse(within_one("uaser", "uater1"))

    def test_transliteration_matching(self):
        self.assertEqual(skeleton("racchabh"), skeleton("RACAB"))
        self.assertEqual(skeleton("parasch"), skeleton("PARAS"))
        self.assertNotEqual(exact("parasch"), exact("PARAS"))
        self.assertTrue(near("NESHER", "NESCHER"))
        self.assertFalse(near("PARA", "PARAS"))


if __name__ == "__main__":
    unittest.main()

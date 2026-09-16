import unittest
from extract import extract


class ExtractTests(unittest.TestCase):
    def test_merged_web_lines_and_footnote_markers(self):
        squares = extract("L1: 27\\5* AB, B. 27\\13^{1} CD, DC")
        self.assertEqual([s["id"] for s in squares], ["27/5", "27/13"])
        self.assertEqual(squares[0]["grid"], [["A", "B"], ["B", None]])

    def test_layout_anomalies_are_preserved_and_excluded(self):
        for text in ["L1: 1\\1 AB, B", "L1: 1\\1 AB B.", "L1: 1\\1 Ab, BA"]:
            square = extract(text)[0]
            self.assertIsNone(square["grid"])
            self.assertIn("exclude_reason", square)

    def test_duplicate_ids_fail(self):
        with self.assertRaises(ValueError):
            extract("L1: 1\\1 AB, BA\nL2: 1\\1 AB, BA")


if __name__ == "__main__":
    unittest.main()

import unittest
import posthoc


class LocatorMappingTest(unittest.TestCase):
    def setUp(self):
        self.a = {(243, 1): {"chapter": 4, "number": 1, "grid_index": 1, "rows": ["AB", "CD"]}}
        self.b = {(243, 2): {"chapter": 1, "number": 1, "grid_index": 2, "rows": ["AB", "CE"]}}
        self.mapping = [{"physical_page": 243, "reader_a_grid_index": 1, "reader_b_grid_index": 2,
                         "locator_id": "p243-c1-g1", "chapter": 1, "number": 1, "reason": "source heading"}]

    def test_only_locators_change(self):
        left, right, records = posthoc.remap(self.a, self.b, self.mapping)
        self.assertEqual(self.a[(243, 1)]["chapter"], 4)
        self.assertEqual(left[(243, 1)]["rows"], ["AB", "CD"])
        self.assertEqual(right[(243, 1)]["rows"], ["AB", "CE"])
        self.assertEqual(posthoc.cell_records(records[0])[-1]["consensus"], "?")

    def test_reuse_rejected(self):
        with self.assertRaises(ValueError):
            posthoc.remap(self.a, self.b, self.mapping * 2)

    def test_omission_rejected(self):
        with self.assertRaises(ValueError):
            posthoc.remap(self.a, self.b, [])

    def test_wrong_page_rejected(self):
        with self.assertRaises(ValueError):
            posthoc.remap(self.a, self.b, [dict(self.mapping[0], physical_page=244)])

    def test_no_cells_for_different_shapes(self):
        self.assertIsNone(posthoc.cell_records({"reader_a": {"rows": ["AB", "CD"]},
                                               "reader_b": {"rows": ["ABC", "D"]}}))


if __name__ == "__main__":
    unittest.main()

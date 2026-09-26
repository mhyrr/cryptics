import unittest
from score import consensus, evaluate


class PilotTests(unittest.TestCase):
    def grid(self, center="A", sid="1/1"):
        return {"physical_page": 243, "grid_index": 1, "source_id": sid,
                "complete_both": True, "rows": ["ABA", f"B{center}B", "ABA"]}

    def run_grid(self, grid):
        cell = {"row": 1, "column": 1, "interior": True, "sym_TA": None,
                "letter_filler": "A", "letter_global": "A", "class_checkerboard": "V"}
        return evaluate([grid], {"1/1": ["ABA", "B.B", "ABA"]}, {"1/1": [cell]}, {"1/1": {(1, 1): "R"}})

    def test_no_identifier_means_no_primary_join(self):
        result = self.run_grid(self.grid(sid=None))
        self.assertEqual(result["aligned"], [])
        self.assertEqual(result["cells"], [])

    def test_unknown_truth_is_not_a_wrong_prediction(self):
        result = self.run_grid(self.grid(center="?"))
        self.assertEqual(result["tally"]["letter_class_mode|interior"], {"unreadable_truth": 1})

    def test_frozen_guesses_score_only_mathers_blank(self):
        result = self.run_grid(self.grid())
        self.assertEqual(len(result["cells"]), 1)
        self.assertEqual(result["tally"]["class_checkerboard|interior"], {"correct": 1})
        self.assertEqual(result["tally"]["letter_chapter|interior"], {"wrong": 1})
        self.assertEqual(result["tally"]["sym_TA|interior"], {"abstain": 1})

    def test_consonant_is_scored_as_class_not_letter(self):
        result = self.run_grid(self.grid(center="R"))
        self.assertEqual(result["tally"]["class_checkerboard|interior"], {"wrong": 1})
        self.assertEqual(result["tally"]["letter_chapter|interior"], {"correct": 1})

    def test_ij_normalization_preserves_raw_disagreement_information(self):
        a = {(243, 1): {"rows": ["I??"], "chapter": 1, "number": 1, "complete": False}}
        b = {(243, 1): {"rows": ["J??"], "chapter": 1, "number": 1, "complete": False}}
        grids, counts, _ = consensus(a, b)
        self.assertEqual(grids[0]["rows"], ["I??"])
        self.assertEqual(counts["normalized_agreed_letters"], 1)
        self.assertEqual(counts["unresolved_positions"], 2)

    def test_partial_grid_does_not_enter_primary_scoring(self):
        grid = dict(self.grid(), complete_both=False)
        self.assertEqual(self.run_grid(grid)["aligned"], [])


if __name__ == "__main__":
    unittest.main()

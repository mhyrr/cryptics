#!/usr/bin/env python3
"""Checks on synthetic inputs only. Run: python3 test_score.py"""
import random, unittest

import score


class Consensus(unittest.TestCase):
    def test_agreement_conflict_and_unknown(self):
        a = ["ABC", "DEF", "GH?"]
        b = ["ABC", "DXF", "GHI"]
        self.assertEqual(score.consensus_grid(a, b), ["ABC", "D?F", "GH?"])

    def test_shape_mismatch_is_excluded(self):
        self.assertIsNone(score.consensus_grid(["ABC", "DE"], ["ABC", "DEF"]))
        self.assertIsNone(score.consensus_grid([], ["A"]))

    def test_j_to_i_only_when_normalized(self):
        self.assertEqual(score.consensus_grid(["J"], ["I"]), ["?"])
        self.assertEqual(score.consensus_grid(["J"], ["I"], normalize=True), ["I"])

    def test_blank_cells_are_not_letters(self):
        self.assertEqual(score.consensus_grid(["A."], ["A."]), ["A?"])

    def test_square_requires_n_at_least_four(self):
        self.assertIsNone(score.square(["ABC", "DEF", "GHI"]))
        self.assertEqual(score.square(["ABCD"] * 4), ["ABCD"] * 4)
        self.assertIsNone(score.square(["ABCD", "ABC", "ABCD", "ABCD"]))


class Joins(unittest.TestCase):
    def test_gate_half_agreement(self):
        m = ["ABCD", "B...", "C...", "D..."]
        self.assertTrue(score.gate(m, ["ABCD", "BXXX", "CXXX", "DXXX"]))
        self.assertFalse(score.gate(m, ["WXYZ", "WXXX", "CXXX", "DXXX"]))
        self.assertFalse(score.gate(m, ["ABCDE"] * 5))

    def test_primary_join_skips_unknown_ids_and_duplicates(self):
        m = {"5/1": ["ABCD", "B...", "C...", "D..."]}
        rows = ["ABCD", "BAAA", "CAAA", "DAAA"]
        grids = [{"locator_id": "x", "chapter": None, "item": 1, "rows": rows},
                 {"locator_id": "y", "chapter": 5, "item": 1, "rows": rows},
                 {"locator_id": "z", "chapter": 5, "item": 1, "rows": rows}]
        joined = score.primary_join(grids, m)
        self.assertEqual(list(joined), ["5/1"])
        self.assertEqual(joined["5/1"]["locator_id"], "y")


class Scoring(unittest.TestCase):
    def setUp(self):
        self.joined = {"5/1": {"locator_id": "y", "rows": ["MILON", "IRAGO", "LAMAL", "OGARI", "NOLIM"]}}
        cells = [
            {"row": 1, "column": 1, "interior": True, "sym_TA": None, "class_checkerboard": "C",
             "letter_filler": "R", "letter_global": "A"},
            {"row": 1, "column": 2, "interior": True, "sym_TA": None, "class_checkerboard": "C",
             "letter_filler": "R", "letter_global": "A"},
            {"row": 4, "column": 4, "interior": False, "sym_TA": "M", "class_checkerboard": "V",
             "letter_filler": "A", "letter_global": "A"},
        ]
        self.p13 = {"5/1": {"cells": cells}}
        self.p20 = {"5/1": {(1, 1): "R", (1, 2): "N"}}
        self.p24 = {"5/1": {(1, 1): {"palette": {"V": "O", "C": "R"}, "class_mode": {"V": "A", "C": "R"}},
                            (1, 2): {"palette": {"V": "A", "C": "L"}, "class_mode": {"V": "A", "C": "R"}}}}

    def test_cell_outcomes(self):
        cells = score.cell_outcomes(self.joined, self.p13, self.p20, self.p24)
        by = {(c["row"], c["column"]): c for c in cells}
        self.assertEqual(by[(1, 1)]["letter_filler"], "correct")         # R
        self.assertEqual(by[(1, 2)]["class_checkerboard"], "wrong")       # A is a vowel
        self.assertEqual(by[(1, 2)]["palette_true_class"], "correct")     # vowel palette A
        self.assertEqual(by[(1, 2)]["palette_cb"], "wrong")               # consonant palette L
        self.assertEqual(by[(4, 4)]["sym_TA"], "correct")
        self.assertEqual(by[(4, 4)]["zone"], "border")

    def test_measures_and_orbits(self):
        cells = score.cell_outcomes(self.joined, self.p13, self.p20, self.p24)
        m = score.measures(cells)
        self.assertEqual(m["targets"], {"interior": 2, "border": 1, "squares": 1})
        self.assertEqual(m["M2_class_interior"]["accuracy"], 0.5)
        orb = score.orbit_counts(cells, {"5/1": 5})
        self.assertEqual(orb["orbits"], 2)

    def test_bootstrap_is_deterministic(self):
        cells = score.cell_outcomes(self.joined, self.p13, self.p20, self.p24)
        a = score.bootstrap(cells, random.Random(1), nboot=50)
        b = score.bootstrap(cells, random.Random(1), nboot=50)
        self.assertEqual(a, b)


class Decision(unittest.TestCase):
    def m(self, m1, m2, letters, interior=60, border=40):
        out = {"targets": {"interior": interior, "border": border, "squares": 5},
               "M1_sym_border": {"accuracy": m1}, "M2_class_interior": {"accuracy": m2}}
        for k, v in zip(score.LETTER_MODELS, letters):
            out[f"M3_{k}"] = {"accuracy": v}
        return out

    def test_rules(self):
        self.assertEqual(score.decide(self.m(0.9, 0.8, [0.3, 0.2, 0.2, 0.3])), "recipe holds")
        self.assertEqual(score.decide(self.m(0.9, 0.8, [0.3, 0.2, 0.2, 0.3], interior=49)), "too few targets")
        self.assertEqual(score.decide(self.m(0.9, 0.55, [0.3, 0.2, 0.2, 0.3])), "class fails")
        self.assertEqual(score.decide(self.m(0.6, 0.8, [0.3, 0.2, 0.2, 0.3])), "frame fails")
        self.assertEqual(score.decide(self.m(0.9, 0.8, [0.55, 0.2, 0.2, 0.3])), "generator signal")
        self.assertEqual(score.decide(self.m(0.75, 0.8, [0.3, 0.2, 0.2, 0.3])), "undecided")

    def test_alternates(self):
        self.assertTrue(score.alternates("MILON"))
        self.assertFalse(score.alternates("APPARET"))
        self.assertIsNone(score.alternates("MI.ON"))


if __name__ == "__main__":
    unittest.main()

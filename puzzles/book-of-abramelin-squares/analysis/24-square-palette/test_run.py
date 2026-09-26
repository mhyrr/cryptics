#!/usr/bin/env python3
"""Checks on synthetic inputs only. Run: python3 test_run.py"""
import collections, random, unittest

import run

ORBITS7 = sorted({run.orbit_cells(7, i, j) for i in range(1, 6) for j in range(1, 6)})


def toy_item(k, letters, chapter=1):
    cells = ORBITS7[:len(letters)]
    pairs = [(p, q, not run.adjacent(cells[p], cells[q])) for p in range(len(cells)) for q in range(p + 1, len(cells))]
    return {"id": f"{chapter}/{k}", "chapter": chapter, "n": 7, "letters": list(letters),
            "cls": ["V" if l in run.V else "C" for l in letters], "cells": cells, "pairs": pairs}


def toy_corpus(rng, palette_share, n=150):
    cons, vows = "BDGKLMNPRST", "AEIOU"
    items = []
    for k in range(n):
        chapter = 1 + k % 5
        if k < palette_share * n:
            pc, pv = rng.sample(cons, 2), rng.sample(vows, 2)
        else:
            pc, pv = cons, vows
        pattern = "CVCVCVCVC"
        items.append(toy_item(k, [rng.choice(pc if c == "C" else pv) for c in pattern], chapter))
    return items


class Structure(unittest.TestCase):
    def test_seven_by_seven_has_nine_interior_orbits(self):
        self.assertEqual(len(ORBITS7), 9)
        self.assertEqual(run.orbit_cells(7, 1, 2), ((1, 2), (2, 1), (4, 5), (5, 4)))

    def test_rep_counts_same_letter_pairs(self):
        it = toy_item(0, "RARAR")
        rep, far = run.rep_stats([it], [it["letters"]])
        self.assertEqual(rep, 3 + 1)  # three R pairs, one A pair
        self.assertLessEqual(far, rep)

    def test_shuffle_keeps_class_and_chapter_counts(self):
        rng = random.Random(1)
        items = toy_corpus(rng, 0.0)
        new = run.shuffle_within(items, rng, run.KEYS["chapter"])
        for it, ls in zip(items, new):
            self.assertEqual(["V" if l in run.V else "C" for l in ls], it["cls"])
        before = collections.Counter((it["chapter"], l) for it in items for l in it["letters"])
        after = collections.Counter((it["chapter"], l) for it, ls in zip(items, new) for l in ls)
        self.assertEqual(before, after)


class Power(unittest.TestCase):
    def test_planted_palette_is_detected(self):
        items = toy_corpus(random.Random(2), 0.3)
        self.assertLess(run.part_a(items, "chapter", 300, seed=3)["Rep"]["p"], 0.01)

    def test_homogeneous_corpus_is_not_detected(self):
        items = toy_corpus(random.Random(4), 0.0)
        self.assertGreater(run.part_a(items, "chapter", 300, seed=5)["Rep"]["p"], 0.05)

    def test_loo_gain_positive_only_with_palette(self):
        with_pal = run.loo(toy_corpus(random.Random(6), 0.5), [it["letters"] for it in toy_corpus(random.Random(6), 0.5)])
        without = run.loo(toy_corpus(random.Random(7), 0.0), [it["letters"] for it in toy_corpus(random.Random(7), 0.0)])
        self.assertGreater(with_pal["gain"], 0.1)
        self.assertLess(without["gain"], with_pal["gain"])


class Scoring(unittest.TestCase):
    def test_sign_test(self):
        self.assertAlmostEqual(run.sign_test(5, 0), 1 / 32)
        self.assertAlmostEqual(run.sign_test(0, 1), 1.0)
        self.assertIsNone(run.sign_test(0, 0))

    def test_score_counts_orbits_once(self):
        orbit = [list(c) for c in run.orbit_cells(5, 1, 2)]
        cells = [{"row": r, "column": c, "orbit": orbit, "class_mode": {"V": "A", "C": "R"},
                  "palette": {"V": "O", "C": "R"}, "palette_size": {"V": 1, "C": 0}, "checkerboard": "V"}
                 for r, c in orbit]
        preds = {"squares": [{"id": "1/1", "size": 5, "cells": cells}]}
        rows = ["ABCDE", "FGOHI", "JOKLM", "NPQRO", "STUOV"]
        out = run.score(preds, {"1/1": rows})
        self.assertEqual(out["orbits"], 1)
        self.assertEqual(out["cells"]["cells"], 4)
        self.assertEqual(out["palette_wins"], 1)
        self.assertEqual(out["palette_losses"], 0)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Checks on synthetic inputs only. Run: python3 test_run.py"""
import random, string, unittest

import run


def toy_items(n_squares, closed_share, rng, m=6):
    """Size-5 squares with random seeds; a share draws every interior letter from its seed."""
    items = []
    for k in range(n_squares):
        seed = "".join(rng.choice(string.ascii_uppercase) for _ in range(5))
        closed = k < closed_share * n_squares
        letters = [rng.choice(seed) if closed else rng.choice(string.ascii_uppercase) for _ in range(m)]
        cls = ["V" if l in run.V else "C" for l in letters]
        items.append({"id": f"t/{k}", "n": 5, "seed": seed, "letters": letters, "cls": cls,
                      "conform": [True] * m, "interior": []})
    return items


class Closure(unittest.TestCase):
    def test_counts_set_membership(self):
        self.assertEqual(run.closure(["A", "A", "B", "Z"], "ABC"), 3)
        self.assertEqual(run.closure([], "ABC"), 0)

    def test_moments_exclude_small_size_class(self):
        rng = random.Random(1)
        items = toy_items(4, 0, rng)
        usable, excluded = run.attach_moments(items)
        self.assertEqual(usable, [])
        self.assertEqual(len(excluded), 4)

    def test_z_matches_hand_computation(self):
        items = [{"id": str(k), "n": 5, "seed": s, "letters": ["A", "B"], "cls": ["V", "C"],
                  "conform": [True, True], "interior": []}
                 for k, s in enumerate(["AB", "AC", "CC", "CD", "DD", "EE"])]
        usable, _ = run.attach_moments(items)
        first = [u for u in usable if u["id"] == "0"][0]
        # references AC CC CD DD EE give k = 1, 0, 0, 0, 0
        self.assertAlmostEqual(first["E"], 0.2)
        self.assertAlmostEqual(first["sd"], 0.4)
        self.assertAlmostEqual(first["z"], (2 - 0.2) / 0.4)


class Power(unittest.TestCase):
    def test_planted_closed_subset_is_supported(self):
        rng = random.Random(2)
        usable, _ = run.attach_moments(toy_items(120, 0.15, rng))
        test = run.permutation_test(usable, 500, seed=3)
        self.assertEqual(run.verdict(test), "supported")
        self.assertGreater(test["excess_U"]["estimate"], 5)

    def test_homogeneous_corpus_is_not_supported(self):
        rng = random.Random(4)
        usable, _ = run.attach_moments(toy_items(120, 0.0, rng))
        test = run.permutation_test(usable, 500, seed=5)
        self.assertNotEqual(run.verdict(test), "supported")


class Helpers(unittest.TestCase):
    def test_spearman(self):
        self.assertAlmostEqual(run.spearman([1, 2, 3, 4], [10, 20, 30, 40]), 1.0)
        self.assertAlmostEqual(run.spearman([1, 2, 3, 4], [4, 3, 2, 1]), -1.0)
        self.assertEqual(run.ranks([5, 1, 5]), [2.5, 1.0, 2.5])

    def test_checkerboard_class(self):
        g = [list("MILON"), list("I...."), list("L...."), list("O...."), list("N....")]
        # MILON / IRAGO / LAMAL: R at (1,1), A at (2,1), A at (1,2)
        self.assertEqual(run.checkerboard_class(g, (1, 1)), "C")
        self.assertEqual(run.checkerboard_class(g, (2, 1)), "V")
        self.assertEqual(run.checkerboard_class(g, (1, 2)), "V")

    def test_prepare_drops_motivating_seed(self):
        rows = ["APPARET", "PAREOTE", "PREREOR", "AEREREA", "ROERERP", "ETOERAP", "TERAPPA"]
        sq = {"id": "x/1", "n": 7, "g": run.to_grid(rows)}
        self.assertEqual(run.prepare([sq]), [])
        self.assertEqual(len(run.prepare([sq], drop_motivating=False)), 1)


if __name__ == "__main__":
    unittest.main()

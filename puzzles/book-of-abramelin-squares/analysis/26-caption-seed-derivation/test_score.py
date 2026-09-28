#!/usr/bin/env python3
"""Synthetic checks for score.py. No seed, reading or caption from the corpus is used."""
import unittest

import score as S


def cands(lat=(), grk=()):
    return S.Candidates([(t, {"form": t, "language": "hebrew"}) for t in lat],
                        [(g, {"form": g, "language": "greek"}) for g in grk])


class Normalization(unittest.TestCase):
    def test_norm(self):
        self.assertEqual(S.norm("náchal"), "NACHAL")
        self.assertEqual(S.norm("ſcheleg"), "SCHELEG")
        self.assertEqual(S.norm("Jawe"), "IAUE")
        self.assertEqual(S.norm("cælum"), "CAELUM")

    def test_agreement_keys(self):
        self.assertEqual(S.lat_agree_key("Náchal"), S.lat_agree_key("nachal"))
        self.assertEqual(S.lat_agree_key("ben-adam"), "ben adam")
        self.assertEqual(S.grk_agree_key("ἀετὸς"), S.grk_agree_key("ἀετός"))
        self.assertNotEqual(S.grk_agree_key("ἥλιος"), S.grk_agree_key("ἤλιος"))   # rough breathing kept

    def test_agreed_multiset_and_doubt(self):
        a = ["arieh", "cephir", "cephir", "gu?"]
        b = ["cephir", "arieh", "gur", "labhi"]
        self.assertEqual(S.agreed(a, b, S.lat_agree_key), ["arieh", "cephir"])
        self.assertEqual(S.agreed(["pe?hen"], ["pethen"], S.lat_agree_key), [])

    def test_tokens(self):
        self.assertEqual(S.tokens("ben adam"), ["ben", "adam", "benadam"])
        self.assertEqual(S.tokens("reem"), ["reem"])


class Tiers(unittest.TestCase):
    def test_aspirate_variants(self):
        v = S.aspirate_variants("SCHACHAL")
        self.assertEqual(v, {"SCHACHAL", "SACHAL", "SCHACAL", "SACAL"})
        self.assertIn("NESER", S.aspirate_variants("NESCHER"))
        self.assertIn("PETHEN", S.aspirate_variants("PETHEN"))

    def test_ladder(self):
        c = cands(["nescher", "pethen", "bethulah"])
        self.assertEqual(c.lat_level("PETHEN"), 0)        # exact
        self.assertEqual(c.lat_level("NESER"), 1)         # aspirate
        self.assertEqual(c.lat_level("BETULA"), 2)        # skeleton: final h deleted
        self.assertEqual(c.lat_level("BETULAM"), 3)       # near: one edit on the skeleton
        self.assertIsNone(c.lat_level("GOLIAT"))
        self.assertIsNone(cands(["abcd"]).lat_level("ABCE"))   # near needs five letters

    def test_aspirate_is_per_type(self):
        # CH reduced in one place and kept in another is not an aspirate-tier match
        c = cands(["chachal"])
        self.assertEqual(c.lat_level("CACHAL"), 2)        # reached only by the skeleton
        self.assertEqual(c.lat_level("CACAL"), 1)

    def test_greek(self):
        c = cands(grk=["ἀετὸς", "θήραμα", "ἥλιος"])
        self.assertEqual(c.grk_level("AETOS"), 0)
        self.assertEqual(c.grk_level("THERAMA"), 0)
        self.assertEqual(c.grk_level("THIRAMA"), 1)       # itacist
        self.assertEqual(c.grk_level("HILIOS"), 1)        # itacist with rough breathing
        self.assertIsNone(c.grk_level("TIRAMA"))
        self.assertIsNone(c.lat_level("AETOS"))           # Greek never enters the Latin ladder


class Counting(unittest.TestCase):
    def test_counts_cumulative(self):
        lv = [(0, None), (1, None), (2, None), (3, None), (None, 1), (None, None)]
        c = S.counts(lv)
        self.assertEqual([c[t] for t in S.LAT_TIERS], [1, 2, 3, 4])
        self.assertEqual(c["greek"], 0)
        self.assertEqual(c["greek_itacist"], 1)
        self.assertEqual(c["all_tiers"], 4)
        self.assertEqual(c["all_with_near"], 5)

    def test_planted_permutation(self):
        grids = [f"g{i}" for i in range(30)]
        chapter = {g: i // 10 for i, g in enumerate(grids)}
        words = ["ALPHAR", "BETHOR", "GIMELS", "DALETH", "HEUUAS", "ZAINIS", "CHETHA", "TETHOS", "IODHIM", "CAPHEL"]
        seeds = {g: words[i % 10] + "ABCDEFGHIK"[i // 10] for i, g in enumerate(grids)}
        cmap = {g: cands([seeds[g].lower()]) for g in grids}
        targets = {g: [seeds[g]] for g in grids}
        _, tests = S.score_cohort(grids, chapter, targets, cmap, draws=200, seed=1)
        w = tests["within_chapter"]["exact"]
        self.assertEqual(w["observed"], 30)
        self.assertLess(w["control_max"], 30)
        self.assertAlmostEqual(w["p"], 1 / 201, places=4)

    def test_null_permutation(self):
        # every caption carries every seed: permutation cannot lower the count
        grids = [f"g{i}" for i in range(12)]
        chapter = {g: 0 for g in grids}
        seeds = {g: f"SEED{chr(65 + i)}X" for i, g in enumerate(grids)}
        allc = cands([s.lower() for s in seeds.values()])
        _, tests = S.score_cohort(grids, chapter, {g: [seeds[g]] for g in grids}, {g: allc for g in grids}, draws=50, seed=2)
        self.assertEqual(tests["within_chapter"]["exact"]["p"], 1.0)

    def test_verdict(self):
        self.assertEqual(S.verdict(99, 90, 0.0005), "too few seeds")
        self.assertEqual(S.verdict(200, 120, 0.0005), "seed layer derived")
        self.assertEqual(S.verdict(200, 119, 0.0005), "partial")
        self.assertEqual(S.verdict(200, 130, 0.005), "open")
        self.assertEqual(S.verdict(200, 20, 0.03), "open")
        self.assertEqual(S.verdict(200, 20, 0.05), "not supported")


class Stages(unittest.TestCase):
    def test_failure_stages(self):
        self.assertEqual(S.failure("g", {"nominations": 0, "located": 0, "with_forms": 0}, None, None, [], False)[0],
                         "F1 no nomination")
        self.assertEqual(S.failure("g", {"nominations": 2, "located": 0, "with_forms": 0}, None, None, [], False)[0],
                         "F2 no entry located")
        self.assertEqual(S.failure("g", {"nominations": 2, "located": 1, "with_forms": 0}, None, None, [], False)[0],
                         "F3 entry located, no agreed form")
        st, flags = S.failure("g", {"nominations": 2, "located": 1, "with_forms": 1}, 3, 1, ["g2"], True)
        self.assertEqual(st, "F4 agreed forms, no match")
        self.assertEqual(flags, ["near", "greek_itacist", "other_caption", "elsewhere"])

    def test_top_consensus(self):
        self.assertEqual(S.top_consensus(["ABCD", "EFGH"], ["ABXD", "EFGH"]), ["AB?D", "EFGH"])
        self.assertIsNone(S.top_consensus(["ABCD"], ["ABC"]))
        self.assertEqual(S.top_consensus(["AJ?."], ["AI?."]), ["AI??"])

    def test_centre_targets(self):
        half, full = S.centre_targets(["ABCDE", "FGHIJ", "APPAR", "KLMNO", "PQRST"])
        self.assertEqual(half, ["APP", "RAP"])
        self.assertEqual(full, ["APPAR", "RAPPA"])
        self.assertEqual(S.centre_targets(["ABCD"] * 4), (None, None))
        self.assertIsNone(S.centre_targets(["ABCDE", "FGHIJ", "ABCBA", "KLMNO", "PQRST"])[1])


class Spelling(unittest.TestCase):
    def test_marks(self):
        self.assertEqual(S.s4_marks("NESER", "nescher"), [("SCH", "reduced")])
        self.assertEqual(S.s4_marks("PETHEN", "pethen"), [("TH", "kept")])
        self.assertEqual(S.s4_marks("CEPHIR", "cephir"), [("PH", "kept")])
        self.assertEqual(S.s4_marks("BETULAH", "bethulah"), [("TH", "reduced"), ("H", "kept")])
        self.assertEqual(S.s4_marks("CALA", "callah"), [("double", "reduced"), ("H", "reduced")])
        self.assertIsNone(S.s4_marks("XYZ", "pethen"))

    def test_identity(self):
        self.assertTrue(S.headword_identity("schlang / edechs", "Schlange"))
        self.assertTrue(S.headword_identity("waſſer", "Wasser"))
        self.assertFalse(S.headword_identity("vatter", "Wasser"))
        self.assertFalse(S.headword_identity(None, "Wasser"))


class EndToEnd(unittest.TestCase):
    def test_cohort(self):
        manifest = {"e1": {"volume": "v", "scan": 1, "column": 1, "parts": [{"box": [0, 0, 1, 1]}]},
                    "e2": {"volume": "v", "scan": 2, "column": 2, "parts": [{"box": [0, 0, 1, 1]}]},
                    "e3": {"volume": "v", "scan": 3, "column": 1, "parts": [{"box": [0, 0, 1, 1]}]}}
        readings = {"e1": {"A": {"headword_printed": "Adler.", "entry_found": True, "hebrew": ["nescher"], "greek": ["ἀετὸς"], "latin": ["Aquila"]},
                           "B": {"headword_printed": "Adler.", "entry_found": True, "hebrew": ["neſcher"], "greek": ["ἀετός"], "latin": ["Aquila"]}},
                    "e2": {"A": {"headword_printed": "Gold.", "entry_found": True, "hebrew": ["segor"], "greek": [], "latin": ["Aurum"]},
                           "B": {"headword_printed": "Gold.", "entry_found": True, "hebrew": ["se?or"], "greek": [], "latin": ["Aurum"]}},
                    "e3": {"A": {"headword_printed": "Wand.", "entry_found": True, "hebrew": [], "greek": [], "latin": []},
                           "B": {"headword_printed": "Wand.", "entry_found": True, "hebrew": [], "greek": [], "latin": []}}}
        entries = S.agreed_entries(readings)
        self.assertEqual(entries["e2"]["hebrew"], [])            # the doubtful letter kills the form
        hw = {"Adler": ["e1"], "Gold": ["e2"], "Wand": ["e3"]}
        noms = {"g1": [{"german": "Adler", "nominator": "A"}], "g2": [{"german": "Gold", "nominator": "B"}],
                "g3": [{"german": "Wand", "nominator": "C"}], "g4": [], "g5": [{"german": "Gans", "nominator": "A"}],
                "g6": [{"german": "Adler", "nominator": "B"}]}
        cmap, stages = {}, {}
        for g, n in noms.items():
            cmap[g], stages[g] = S.caption_candidates(n, hw, entries, manifest)
        seeds = {"g1": "NESER", "g2": "SEGOR", "g3": "MURUS", "g4": "ABCDE", "g5": "ANSER", "g6": "AETOS", "g7": "AB?DE"}
        chapter = {g: 1 for g in seeds}
        read_set = S.Candidates([(t, {}) for e in entries.values() for c in ("hebrew", "latin") for f in e[c] for t in S.tokens(f)], [])
        res, _, _ = S.run_cohort("T", sorted(seeds), chapter, seeds, cmap, stages, read_set)
        self.assertEqual(res["eligible"], 6)
        self.assertEqual(res["ineligible"], ["g7"])
        d = {x["grid"]: x for x in res["derivations"]}
        self.assertEqual(d["g1"]["tier"], "aspirate")
        self.assertEqual(d["g1"]["chains"][0]["entry"], "e1")
        self.assertTrue(d["g1"]["chains"][0]["identity"])
        self.assertEqual(d["g6"]["greek_tier"], "greek")
        f = {x["grid"]: x for x in res["failures"]}
        self.assertEqual(f["g2"]["stage"], "F4 agreed forms, no match")     # only the Latin form was agreed
        self.assertEqual(f["g3"]["stage"], "F3 entry located, no agreed form")
        self.assertEqual(f["g4"]["stage"], "F1 no nomination")
        self.assertEqual(f["g5"]["stage"], "F2 no entry located")
        self.assertIn("greek", f["g6"]["flags"])
        self.assertEqual(res["tests"]["within_chapter"]["skeleton"]["observed"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=1)

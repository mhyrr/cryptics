"""Synthetic checks only; never opens witness images or historical readings."""
import json
import pathlib
import tempfile
import unittest
from unittest import mock

import score_checked as checked


class PreflightTests(unittest.TestCase):
    def test_unknown_cells_cannot_make_a_page_readable(self):
        rows = ["A????", "?????", "?????", "?????", "?????"]
        result = checked.gate({(1, 1): rows}, {(1, 1): rows})
        self.assertEqual(result["original_counts"]["lettered_top"], 1)
        self.assertEqual(result["potentially_lettered"], 25)
        self.assertEqual(result["agreed_share"], 0.04)
        self.assertFalse(result["readable"])

    def test_missing_rows_are_blanks_not_uncertain_letters(self):
        rows = ["ABCDE"]
        result = checked.gate({(1, 1): rows}, {(1, 1): rows})
        self.assertEqual(result["potentially_lettered"], 5)
        self.assertTrue(result["readable"])
        items, _ = checked.corrected_merge({(1, 1): rows}, {(1, 1): rows})
        self.assertEqual(items[(1, 1)]["grid"][1:], ["....."] * 4)

    def test_disagreement_stays_unknown(self):
        a, b = {(1, 1): ["ABCDE"]}, {(1, 1): ["ABCXE"]}
        items, _ = checked.corrected_merge(a, b)
        self.assertEqual(items[(1, 1)]["grid"][0], "ABC?E")
        self.assertIsNone(items[(1, 1)]["top"])

    def test_ragged_list_cannot_rescue_legibility(self):
        a = {(1, 1): ["ABCDE", "XYZ"], (1, 2): ["ABC"]}
        result = checked.gate(a, a)
        self.assertEqual(result["potentially_lettered"], 11)
        self.assertEqual(result["agreed"], 3)
        self.assertFalse(result["readable"])

    def test_reader_coverage_must_agree(self):
        with self.assertRaisesRegex(ValueError, "identifiers differ"):
            checked.gate({(1, 1): ["ABCDE"]}, {})

    def test_duplicate_ids_and_invalid_symbols_are_not_silently_lost(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "reader.json"
            item = {"chapter": 1, "number": 1, "page": 324, "rows": ["ABCDE"]}
            for records, message in (([item, item], "duplicate"),
                                     ([dict(item, rows=["ABC1E"])], "noncanonical"),
                                     ([dict(item, page=None)], "PDF page")):
                with self.subTest(message=message):
                    path.write_text(json.dumps({"items": records}))
                    with self.assertRaisesRegex(ValueError, message):
                        checked.read_items(path)

    def test_unreadable_packet_never_calls_historical_scorer(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = pathlib.Path(tmp)
            item = {"chapter": 1, "number": 1, "page": 324,
                    "rows": ["A????"] + ["?????"] * 4}
            for name in ("readings-A.json", "readings-B.json"):
                (directory / name).write_text(json.dumps({"items": [item]}))
            with mock.patch.object(checked.frozen, "main", side_effect=AssertionError("Must not score")):
                result, squares = checked.score(directory)
            self.assertFalse(result["historical_scores_reported"])
            self.assertIsNone(squares)

    def test_both_prediction_freezes_and_dependency_hashes(self):
        self.assertEqual(checked.verify_inputs()["original_freeze_commit"], "a4e2ad6")


def report():
    rows = ["A????"] + ["?????"] * 4
    result = {"scope": "synthetic 5 by 5 grid; no historical witness read",
              "fixture": rows, "gate": checked.gate({(1, 1): rows}, {(1, 1): rows})}
    (checked.HERE / "preflight-results.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    report()
    unittest.main()

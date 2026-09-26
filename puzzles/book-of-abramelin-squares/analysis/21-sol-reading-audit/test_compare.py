import unittest
from compare import pair, cross_consensus


class CompareTests(unittest.TestCase):
    def test_unknowns_count_as_unresolved(self):
        a = {(1, 1, 324): ["A??"]}
        result = pair(a, a, list(a), False)
        self.assertEqual(result["counts"]["unresolved_positions"], 2)
        self.assertEqual(result["agreement_on_comparable_positions"], 1/3)

    def test_ragged_strings_are_comparable_but_shape_changes_are_not(self):
        key = (1, 1, 324)
        a = {key: ["ABCDE", "ABC"]}
        same = pair(a, a, [key], True)
        self.assertEqual(same["counts"]["same_shape_ragged_items"], 1)
        different = pair(a, {key: ["ABCDE", "ABCD"]}, [key], True)
        self.assertEqual(different["counts"]["shape_disagreement_items"], 1)
        self.assertIsNone(different["agreement_on_comparable_positions"])

    def test_ij_policy_is_explicit(self):
        key = (1, 1, 324)
        a, b = {key: ["IAB"]}, {key: ["JAB"]}
        self.assertEqual(pair(a, b, [key], False)["counts"]["letter_or_blank_conflicts"], 1)
        self.assertEqual(pair(a, b, [key], True)["counts"]["agreed_letters"], 3)

    def test_both_pairs_can_agree_and_still_conflict(self):
        key = (1, 1, 324)
        a, b = {key: ["ABC"]}, {key: ["AXC"]}
        result = cross_consensus(a, a, b, b, [key])
        self.assertEqual(result["counts"]["pairs_conflict"], 1)
        self.assertEqual(result["conflicts"][0]["position"], 2)


if __name__ == "__main__":
    unittest.main()

import itertools
import unittest
import analyze


class ErasureTests(unittest.TestCase):
    def test_exact_controls_against_exhaustive_masks(self):
        for rows in [('aba', 'bba', 'aab'), ('aaa', 'aaa', 'aaa'), ('abc', 'def', 'ghi')]:
            letters = {(r + 1, c + 1): v for r, row in enumerate(rows) for c, v in enumerate(row)}
            for family in analyze.FAMILIES:
                orbits = analyze.geometry.orbits(3, family)
                expected = [0] * 10
                for bits in itertools.product((False, True), repeat=9):
                    mask = {c for c, bit in zip(letters, bits) if bit}
                    if not analyze.conflicts(orbits, letters, mask):
                        expected[len(mask)] += 1
                self.assertEqual(analyze.compatible_mask_counts(orbits, letters), expected)

    def test_frame_control_against_exhaustive_masks(self):
        rows = ['Aba', 'bBa', 'aaB']
        record = {'rows': rows}
        letters = {(r + 1, c + 1): v.upper() for r, row in enumerate(rows) for c, v in enumerate(row)}
        for family in analyze.FAMILIES:
            actual = analyze.analyze(record, family)
            numerator = denominator = 0
            for mask_tuple in itertools.combinations(letters, 3):
                mask = set(mask_tuple)
                if (2, 2) not in mask:
                    continue
                denominator += 1
                if not analyze.conflicts(analyze.geometry.orbits(3, family), letters, mask):
                    numerator += 1
            self.assertEqual(actual['frame_matched_control']['numerator'], numerator)
            self.assertEqual(actual['frame_matched_control']['denominator'], denominator)

    def test_wholly_erased_center_stays_free(self):
        r = analyze.analyze({'rows': ['aaa', 'aBa', 'aaa']}, 'TA')
        self.assertTrue(r['compatible_after_capital_erasure'])
        self.assertEqual(r['unconstrained_capital_cells'], [(2, 2)])
        self.assertEqual(r['conditional_precursor_cells'], [])

    def test_capital_with_visible_mates_and_conflict_guard(self):
        r = analyze.analyze({'rows': ['Baa', 'aaa', 'aaa']}, 'TA')
        self.assertEqual(r['conditional_precursor_cells'][0]['conditional_precursor'], 'A')
        self.assertTrue(r['conditional_precursor_cells'][0]['changed'])
        r = analyze.analyze({'rows': ['Bba', 'aaa', 'aaa']}, 'TA')
        self.assertFalse(r['compatible_after_capital_erasure'])
        self.assertEqual(r['conditional_precursor_cells'], [])


if __name__ == '__main__':
    unittest.main()

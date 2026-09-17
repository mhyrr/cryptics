import itertools
import unittest

import run


class CompletionTests(unittest.TestCase):
    def test_planted_and_ambiguous(self):
        cases = {c['case']: c for c in run.evaluate()['synthetic']['cases']}
        unique = cases['planted_unique']
        self.assertEqual(unique['result']['completion_count'], 1)
        self.assertEqual(unique['score']['correct'], 9)
        self.assertEqual(unique['score']['wrong'], 0)
        ambiguous = cases['competing_center']
        self.assertEqual(ambiguous['result']['completion_count'], 2)
        self.assertEqual(ambiguous['score']['abstained'], 1)
        self.assertEqual(ambiguous['score']['correct'], 8)
        self.assertFalse(any(p[:2] == [2, 2] for p in ambiguous['result']['predictions']))
        self.assertGreater(cases['seed_only']['result']['completion_count'], 1)
        self.assertEqual(cases['seed_only']['score']['predicted'], 0)
        self.assertEqual(cases['contradiction']['result']['completion_count'], 0)
        self.assertEqual(cases['contradiction']['score']['predicted'], 0)

    def test_against_exhaustive_small_squares(self):
        # Independent brute-force enumeration over cells, not solver orbits.
        for words in [['AB'], ['AA', 'BB'], ['AB', 'BA'], ['AA', 'AB', 'BA', 'BB']]:
            expected = []
            for letters in itertools.product('AB', repeat=4):
                a, b, c, d = letters
                if b == c and a == d and a + b in words:
                    expected.append(letters)
            result = run.solve([[None] * 2 for _ in range(2)],
                               [([(0, 0), (0, 1)], words)], 'AB')
            self.assertEqual(result['completion_count'], len(expected))
            consensus = [[i // 2, i % 2, expected[0][i]] for i in range(4)
                         if expected and len({g[i] for g in expected}) == 1]
            self.assertEqual(result['predictions'], consensus)

    def test_free_orbits_counted_and_no_vacuous_predictions(self):
        expected = sum(all(g[3*r+c] == g[3*c+r] == g[3*(2-r)+(2-c)]
                           for r in range(3) for c in range(3))
                       for g in itertools.product('AB', repeat=9))
        self.assertEqual(run.solve([[None] * 3 for _ in range(3)], [], 'AB')['completion_count'], expected)
        contradictory = run.solve([list('ABC'), list('DEF'), list('GHI')], [])
        self.assertEqual(contradictory['predictions'], [])
        empty_domain = run.solve([[None]], [([(0, 0)], [])])
        self.assertEqual(empty_domain['completion_count'], 0)
        self.assertEqual(empty_domain['predictions'], [])

    def test_repeated_paths_and_words_do_not_multiply_solutions(self):
        p = ([(0, 0)], ['A', 'A', 'B'])
        self.assertEqual(run.solve([[None]], [p, p], 'AB')['completion_count'], 2)

    def test_no_approximate_normalization(self):
        self.assertEqual(run.normalize('tſippor'), 'TSIPPOR')
        self.assertNotEqual(run.normalize('maiim'), run.normalize('MAIAM'))
        with self.assertRaises(ValueError):
            run.normalize('ἀναγωγὴ')

    def test_source_gate(self):
        result = run.evaluate()
        self.assertIsNone(result['historical_scores'])
        self.assertIsNone(result['historical_predictions'])
        self.assertFalse(any(r['primary_verified'] for r in result['quoted_spelling_audit']))


if __name__ == '__main__':
    unittest.main()

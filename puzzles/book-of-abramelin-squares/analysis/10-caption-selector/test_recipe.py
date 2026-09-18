import itertools
import unittest
from recipe import select, solve


def entry(head, words, uncertain=False):
    return dict(id=head, headword_raw=head, words=[{'raw': w} for w in words], uncertain=uncertain)


class RecipeTests(unittest.TestCase):
    def test_no_semantic_synonym_or_stemming(self):
        lex = [entry('Lehrer', ['moreh'])]
        self.assertEqual(select('Vergangene Sachen Zuwissen', 5, lex)['status'], 'sample_miss')
        self.assertEqual(select('Lehrern', 5, lex)['status'], 'sample_miss')
        self.assertEqual(select('Lehrer', 5, lex)['words'], ['MOREH'])

    def test_alternatives_misses_and_uncertainty(self):
        lex = [entry('A / B', ['aba', 'aaa', 'a-a', 'aa'])]
        s = select('b', 3, lex)
        self.assertEqual(s['words'], ['AAA', 'ABA'])
        self.assertEqual(len(s['exclusions']), 2)
        self.assertEqual(select(None, 3, lex)['status'], 'missing_caption')
        self.assertEqual(select('b', 4, lex)['status'], 'ineligible_size')
        self.assertEqual(select('b', 3, lex + [entry('b', ['bbb'], True)])['words'], [])

    def test_no_capital_or_lowercase_repair(self):
        grid = [['A', 'A', None], ['B', None, None], [None] * 3]
        self.assertEqual(solve(grid, ['AAA'], 'AB')['completion_count'], 0)

    def test_exhaustive_binary_completion_and_consensus(self):
        # Enumerate all 2^9 grids independently of orbit helpers. Check exact
        # counts and unanimous predictions for every central-word subset below.
        grids = []
        for values in itertools.product('AB', repeat=9):
            g = [values[i:i+3] for i in range(0, 9, 3)]
            if all(g[r][c] == g[c][r] for r in range(3) for c in range(3)):
                grids.append(g)
        for words in (['ABA'], ['AAA', 'ABA'], ['AAA', 'AAA'], []):
            for observed in ([[None]*3 for _ in range(3)],
                             [['A', None, 'B'], [None]*3, ['B', None, 'A']]):
                valid = [g for g in grids if ''.join(g[1]) in words and
                         all(observed[r][c] is None or observed[r][c] == g[r][c]
                             for r in range(3) for c in range(3))]
                result = solve(observed, words, 'AB')
                self.assertEqual(result['completion_count'], len(valid))
                expected = []
                for r, c in itertools.product(range(3), repeat=2):
                    values = {g[r][c] for g in valid}
                    if observed[r][c] is None and len(values) == 1:
                        expected.append([r, c, next(iter(values))])
                self.assertEqual(result['predictions'], expected)

    def test_whole_interior_orbits_competing_center(self):
        g = [list('AAAAA') for _ in range(5)]
        for r, c in itertools.product(range(1, 4), repeat=2):
            g[r][c] = None
        one = solve(g, ['AAAAA'], 'AB')
        two = solve(g, ['AAAAA', 'AABAA'], 'AB')
        self.assertIn([2, 2, 'A'], one['predictions'])
        self.assertFalse(any(p[:2] == [2, 2] for p in two['predictions']))
        self.assertEqual(two['completion_count'], 2 * one['completion_count'])
        self.assertGreater(one['completion_count'], 1)  # still not a generator


if __name__ == '__main__':
    unittest.main()

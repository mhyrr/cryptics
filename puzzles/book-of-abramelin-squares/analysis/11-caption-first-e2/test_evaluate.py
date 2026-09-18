import copy
from collections import Counter
import unittest
from unittest.mock import patch

from evaluate import (entry_words, mask_sets, masked, orbit_shuffle, orbits,
                      predict_task, select)


def entry(identity, raw):
    return {'id': identity, 'uncertain': False,
            'words': [{'raw': raw, 'uncertain': False}]}


class EvaluationTests(unittest.TestCase):
    def test_masks_hide_whole_groups_and_cover_each_interior_once(self):
        for n in [3, 5, 7]:
            grid = [['A'] * n for _ in range(n)]
            sets = mask_sets(n)
            all_hidden = set(sets[0][2])
            self.assertEqual(len(all_hidden), (n-2)**2)
            counts = Counter(p for _, _, group in sets[1:] for p in group)
            self.assertEqual(set(counts), all_hidden)
            self.assertEqual(set(counts.values()), {1})
            for _, _, hidden in sets:
                m = masked(grid, hidden)
                for group in orbits(n, 'd4'):
                    self.assertIn(sum(m[r][c] is None for r, c in group), [0, len(group)])
        with self.assertRaises(AssertionError):
            masked([['A']*5 for _ in range(5)], [(1, 2)])

    def test_unresolved_or_disallowed_alternative_cannot_be_dropped(self):
        lex = {'entries': [entry('a', 'ABA')], 'lookups': [
            {'lookup': 'first', 'status': 'verified', 'entry_id': 'a'},
            {'lookup': 'second', 'status': 'unresolved', 'entry_id': None}]}
        nom = {'nominations': [{'lookup': 'first'}, {'lookup': 'second'}]}
        for state in ['unresolved', 'spelling_excluded']:
            lex['lookups'][1]['status'] = state
            self.assertEqual(select(nom, 3, lex)['words'], [])
        lex['lookups'][1] = {'lookup': 'second', 'status': 'verified', 'entry_id': 'a'}
        self.assertEqual(select(nom, 3, lex)['words'], ['ABA'])
        self.assertEqual(entry_words(entry('a', 'a-b'), 3), [])
        self.assertEqual(entry_words(entry('a', 'ábá'), 3), [])

    def test_caption_signal_recovers_planted_center_without_reading_files(self):
        lex = {'entries': [entry('a', 'ABA'), entry('b', 'AAA')],
               'lookups': [{'lookup': 'flower', 'status': 'verified', 'entry_id': 'a'}]}
        nom = {'nominations': [{'lookup': 'flower'}]}
        task = {'n': 3, 'observed': [['A','A','A'], ['A',None,'A'], ['A','A','A']],
                'hidden': [(1,1)], 'variant': 'original', 'training_mode': 'A'}
        before = copy.deepcopy(task)
        with patch('pathlib.Path.read_text', side_effect=AssertionError('File access in predictor')):
            result = predict_task(task, nom, lex, [])
        self.assertEqual(result['caption']['predictions'], [[1,1,'B']])
        self.assertEqual(result['without_captions']['predictions'], [])
        self.assertEqual(result['symmetry_T']['predictions'], [])
        self.assertEqual(task, before)

    def test_orbit_control_preserves_symmetry_and_size_stratum_histograms(self):
        grid = [['A','B','C'], ['B','D','E'], ['C','E','F']]
        def histogram(g):
            return Counter((len(o),g[o[0][0]][o[0][1]]) for o in orbits(3,'transpose'))
        changed = False
        for seed in range(20):
            shuffled = orbit_shuffle(grid, seed)
            self.assertEqual(histogram(grid), histogram(shuffled))
            self.assertTrue(all(shuffled[r][c] == shuffled[c][r] for r in range(3) for c in range(3)))
            changed |= shuffled != grid
        self.assertTrue(changed)
        grid[0][1] = 'Z'
        self.assertIsNone(orbit_shuffle(grid, 1))


if __name__ == '__main__':
    unittest.main()

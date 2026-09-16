"""Failure-oriented tests: grouping, controls, abstention and causal evaluation."""
from collections import Counter
import copy
import importlib.util
from pathlib import Path
import unittest

import common


def experiment(name):
    spec = importlib.util.spec_from_file_location(name, common.ANALYSIS/name/'run.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


frames = experiment('02-frame-model')
fragments = experiment('03-fragment-transfer')
recurrence = experiment('04-local-recurrence')


class DataTests(unittest.TestCase):
    def test_transform_agrees_with_grid_orientation(self):
        grid = [[str(r*5+c) for c in range(5)] for r in range(5)]
        for k in range(8):
            oriented = common.orient(grid, k)
            for r in range(5):
                for c in range(5):
                    rr, cc = common.transform(r, c, 5, k)
                    self.assertEqual(grid[r][c], oriented[rr][cc])
        self.assertIn(((0, 1), (1, 0)), common.orbits(5, 'transpose'))
        self.assertIn(((0, 1), (3, 4)), common.orbits(5, 'anti_transpose'))

    def test_related_grids_stay_together_transitively(self):
        a = [list(w) for w in ['ABC', 'DEF', 'GHI']]
        b = [list(w) for w in ['CBA', 'JKL', 'MNO']]
        c = common.orient(b, 1)
        d = [c[0][:], list('PQR'), list('STU')]
        records = [{'id': str(i), 'grid': g} for i, g in enumerate(
            [a, b, c, d, [list('ZZZ') for _ in range(3)]])]
        originals = [copy.deepcopy(s['grid']) for s in records]
        self.assertEqual(common.group_records(records), 2)
        self.assertEqual(len({s['group'] for s in records[:4]}), 1)
        self.assertEqual(len({s['fold'] for s in records[:4]}), 1)
        self.assertNotEqual(records[0]['group'], records[4]['group'])
        self.assertEqual(originals, [s['grid'] for s in records])

    def test_orbit_masks_remove_every_geometric_copy(self):
        for record in common.load():
            hidden = {tuple(p) for p in record['masks']['orbits']}
            for orbit in common.orbits(len(record['grid']), 'd4'):
                overlap = hidden & set(orbit)
                self.assertTrue(not overlap or overlap == set(orbit))

    def test_controls_preserve_histograms_and_matched_subset(self):
        original = common.load()
        for kind in ['shuffled', 'orbit_shuffled']:
            for changed in common.control(original, kind):
                source = next(s for s in original if s['id'] == changed['id'])
                self.assertEqual(Counter(x for row in source['grid'] for x in row),
                                 Counter(x for row in changed['grid'] for x in row))
                self.assertEqual(source['masks'], changed['masks'])
                if kind == 'orbit_shuffled':
                    self.assertTrue(common.is_symmetric(changed['grid']))
        self.assertEqual([s['id'] for s in common.control(original, 'orbit_shuffled')],
                         [s['id'] for s in common.control(original, 'symmetric_original')])

    def test_scoring_rejects_visible_predictions_and_tracks_abstention(self):
        grid = [list('AB'), list('BA')]
        with self.assertRaises(ValueError):
            common.score(grid, [(1, 1)], {(0, 0): 'A'}, 'A')
        score = common.score(grid, [(1, 0), (1, 1)], {(1, 0): 'B'}, 'A')
        self.assertEqual((score['correct'], score['abstained'], score['exact_tasks']), (1, 1, 0))
        self.assertEqual(score['baseline_correct_same_cells'], 0)
        self.assertEqual(score['baseline_correct_all_hidden'], 1)


class FrameTests(unittest.TestCase):
    def test_unseen_orbit_stays_unknown(self):
        grid = [list('AAAAA') for _ in range(5)]
        hidden = [(0, 0), (0, 4), (4, 0), (4, 4)]
        self.assertEqual(frames.frame_model(common.mask(grid, hidden))[0], {})

    def test_fill_and_repair_do_not_mutate_readings(self):
        grid = [list('AAAAA') for _ in range(5)]
        grid[0][0] = None
        grid[1][1] = 'B'
        original = copy.deepcopy(grid)
        predictions, repairs, _ = frames.frame_model(grid)
        self.assertEqual(predictions, {(0, 0): 'A'})
        self.assertEqual(repairs, {(1, 1): 'A'})
        self.assertEqual(grid, original)

    def test_majority_ties_do_not_choose_a_letter(self):
        self.assertIsNone(common.majority(['A', 'B']))
        self.assertIsNone(common.majority([]))
        self.assertEqual(common.majority(['B', 'A', 'B']), 'B')


class FragmentTests(unittest.TestCase):
    @staticmethod
    def donors(word='ABC', groups=('x', 'y', 'z')):
        return [{'grid': [list(word) for _ in range(3)], 'group': g} for g in groups]

    def test_reflected_copies_do_not_create_donors(self):
        vocabulary = fragments.Vocabulary(self.donors(groups=('x', 'x', 'x')))
        self.assertIsNone(vocabulary.match(['A', None, 'C'], 1))
        vocabulary = fragments.Vocabulary(self.donors())
        self.assertEqual(vocabulary.match(['A', None, 'C'], 1)[0], 'B')

    def test_ambiguous_donors_and_insufficient_context_abstain(self):
        vocabulary = fragments.Vocabulary(self.donors() + self.donors('ADC'))
        self.assertIsNone(vocabulary.match(['A', None, 'C'], 1))
        self.assertIsNone(vocabulary.match(['A', None, None], 1))

    def test_planted_fragments_recover_in_unseen_groups(self):
        records = fragments.planted()
        train = [s for s in records if s['fold'] != 0]
        test = [s for s in records if s['fold'] == 0]
        vocabulary = fragments.Vocabulary(train)
        self.assertFalse(vocabulary.groups & {s['group'] for s in test})
        for s in test:
            hidden = s['masks']['motif_centers']
            preds = vocabulary.predict(common.mask(s['grid'], hidden))
            self.assertEqual(preds, {(r, c): s['grid'][r][c] for r, c in hidden})


class RecurrenceTests(unittest.TestCase):
    def test_rollout_cannot_read_unpredicted_neighbours(self):
        rule = recurrence.Rule([], ('pair_lookup', False, False))
        rule.table = {(0, 1): (2, 1.0, 3)}  # A,B -> C; A,A is unknown.
        truth = [list('AAA'), list('ABC'), list('AAA')]
        hidden = [(1, 1), (1, 2)]
        observed = common.mask(truth, hidden)
        self.assertEqual(rule.predict(observed), {})
        self.assertEqual(rule.predict(observed, teacher=truth), {(1, 2): 'C'})
        self.assertIsNone(observed[1][1])

    def test_confidence_requires_agreement_and_independent_support(self):
        rule = recurrence.Rule([], ('pair_lookup', False, False))
        for frequency, groups in [(.89, 4), (1.0, 2)]:
            rule.table = {(0, 0): (1, frequency, groups)}
            self.assertEqual(rule.step('A', 'A', False), 'B')
            self.assertIsNone(rule.step('A', 'A', True))

    def test_reversed_traversals_return_original_coordinates(self):
        truth = recurrence.planted()[0]['grid']
        for config in recurrence.CONFIGS:
            oriented = recurrence.orient(truth, config)
            for r in range(8):
                for c in range(8):
                    rr, cc = recurrence.unorient_position(r, c, 8, config)
                    self.assertEqual(oriented[r][c], truth[rr][cc])

    def test_nested_selection_recovers_planted_rule_and_rollout(self):
        records = recurrence.planted()
        train = [s for s in records if s['fold'] != 0]
        test = [s for s in records if s['fold'] == 0]
        rule, selection = recurrence.select(train)
        self.assertFalse(rule.groups & {s['group'] for s in test})
        self.assertTrue(set(selection['inner_groups']) < rule.groups)
        self.assertEqual(rule.config, ('north_plus_f_west', False, False))
        for s in test:
            hidden = s['masks']['gnomon']
            preds = rule.predict(common.mask(s['grid'], hidden), confident=True)
            self.assertEqual(preds, {(r, c): s['grid'][r][c] for r, c in hidden})


if __name__ == '__main__':
    unittest.main()

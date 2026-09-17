"""Independent finite checks of orbit counts and the source boundary."""
import itertools
import unittest

from audit import analyze, geometry, orbits


class AuditTests(unittest.TestCase):
    def test_binary_three_by_three_by_direct_equations(self):
        # Brute-force every binary grid, with no orbit helper in the predicate.
        counts = dict.fromkeys(('I', 'T', 'A', 'TA', 'HV', 'D4'), 0)
        for a in itertools.product('AB', repeat=9):
            t = all(a[3*r+c] == a[3*c+r] for r in range(3) for c in range(3))
            anti = all(a[3*r+c] == a[3*(2-c)+2-r] for r in range(3) for c in range(3))
            h = all(a[3*r+c] == a[3*(2-r)+c] for r in range(3) for c in range(3))
            v = all(a[3*r+c] == a[3*r+2-c] for r in range(3) for c in range(3))
            for f, valid in dict(I=True, T=t, A=anti, TA=t and anti, HV=h and v, D4=t and h and v).items():
                counts[f] += valid
        self.assertEqual(counts, {f: 2**len(orbits(3, f)) for f in counts})
        self.assertNotEqual(counts['TA'], counts['D4'])

    def test_boundary_never_reaches_interior(self):
        for n in range(3, 13):
            for f in ('I', 'T', 'A', 'TA', 'HV', 'D4'):
                g = geometry(n, f, [(1, c) for c in range(1, n+1)])
                self.assertEqual(g['interior_orbits_reached_by_path'], [])
                self.assertEqual(g['interior_orbits_reached_by_boundary'], [])
        g = geometry(5, 'TA', [(3, c) for c in range(1, 6)])
        self.assertEqual(len(g['interior_orbits']), 4)
        self.assertEqual(len(g['unconstrained_interior_orbits']), 2)

    def test_invalid_input_and_spelling_are_not_repaired(self):
        ex = dict(id='toy', rows_raw=['ABA', 'BCB', 'ABA'], square_string='BCB',
                  path=dict(start=[2,1], step=[0,1], length=3),
                  caption_display='toy', edition_locator='toy', edition_url='toy', facsimile_record='toy')
        read = dict(target_transliteration_raw='bb', layout_operations=[], image='toy',
                    headword_raw='toy', alternative_transliterations=[])
        result = analyze(ex, {'toy': read})
        self.assertFalse(result['lexical']['target_exactly_fits_nominated_path'])
        ex['rows_raw'] = ['AB', 'BCB', 'ABA']
        with self.assertRaises(ValueError):
            analyze(ex, {'toy': read})


if __name__ == '__main__':
    unittest.main()

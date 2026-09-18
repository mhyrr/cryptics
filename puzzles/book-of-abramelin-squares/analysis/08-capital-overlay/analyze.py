"""Exact erasure diagnostics of exposed, case-preserving edited grids."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ORBIT_SOURCE = HERE.parent / '06-construction-evidence' / 'audit.py'
spec = importlib.util.spec_from_file_location('construction_audit', ORBIT_SOURCE)
geometry = importlib.util.module_from_spec(spec)
spec.loader.exec_module(geometry)
FAMILIES = ('T', 'A', 'TA', 'HV', 'D4')


def frame(cell, n):
    r, c = cell
    return min(r - 1, c - 1, n - r, n - c)


def orbit_polynomial(values):
    """Coefficient k counts compatible subsets erasing exactly k cells."""
    counts = Counter(values)
    size = len(values)
    result = [0] * (size + 1)
    result[size] = 1  # Erase everything, counted once rather than per letter.
    for count in counts.values():
        for retained in range(1, count + 1):
            result[size - retained] += comb(count, retained)
    return result


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def compatible_mask_counts(orbits, letters):
    polynomial = [1]
    for orbit in orbits:
        polynomial = multiply(polynomial, orbit_polynomial([letters[c] for c in orbit]))
    return polynomial


def conflicts(orbits, letters, mask):
    out = []
    for orbit in orbits:
        visible = [(c, letters[c]) for c in orbit if c not in mask]
        counts = Counter(v for _, v in visible)
        if len(counts) > 1:
            out.append({'orbit': orbit, 'surviving_cells': visible,
                        'minimum_further_erasures': len(visible) - max(counts.values())})
    return out


def ratio(numerator, denominator):
    value = Fraction(numerator, denominator)
    return {'numerator': numerator, 'denominator': denominator,
            'reduced': str(value), 'fraction': float(value)}


def analyze(record, family):
    rows = record['rows']
    n = len(rows)
    if not n or any(len(row) != n for row in rows):
        raise ValueError('Grid must be square')
    if any(not ('a' <= c <= 'z' or 'A' <= c <= 'Z') for row in rows for c in row):
        raise ValueError('Only explicitly transcribed ASCII letters accepted')
    letters = {(r + 1, c + 1): v.upper() for r, row in enumerate(rows) for c, v in enumerate(row)}
    mask = {(r + 1, c + 1) for r, row in enumerate(rows) for c, v in enumerate(row) if v.isupper()}
    orbits = geometry.orbits(n, family)
    residual = conflicts(orbits, letters, mask)
    forced, free = [], []
    if not residual:
        for orbit in orbits:
            values = {letters[c] for c in orbit if c not in mask}
            for cell in sorted(mask.intersection(orbit)):
                if values:
                    value = next(iter(values))
                    forced.append({'cell': cell, 'printed': letters[cell], 'conditional_precursor': value,
                                   'changed': letters[cell] != value})
                else:
                    free.append(cell)
    count = len(mask)
    controls = compatible_mask_counts(orbits, letters)
    frame_numerator = frame_denominator = 1
    frame_details = []
    for depth in range((n + 1) // 2):
        cells = {c for c in letters if frame(c, n) == depth}
        local_orbits = [o for o in orbits if frame(o[0], n) == depth]
        assert all(set(o) <= cells for o in local_orbits)
        k = len(cells & mask)
        numerator = compatible_mask_counts(local_orbits, letters)[k]
        denominator = comb(len(cells), k)
        frame_numerator *= numerator
        frame_denominator *= denominator
        frame_details.append({'depth': depth, 'deleted': k, 'cells': len(cells),
                              **ratio(numerator, denominator)})
    return {'family': family, 'capital_cells': sorted(mask),
            'full_conflicting_orbits': len(conflicts(orbits, letters, set())),
            'residual_conflicts': residual,
            'minimum_further_lowercase_erasures': sum(c['minimum_further_erasures'] for c in residual),
            'compatible_after_capital_erasure': not residual,
            'conditional_precursor_cells': forced, 'unconstrained_capital_cells': free,
            'count_matched_control': ratio(controls[count], comb(n * n, count)),
            'frame_matched_control': ratio(frame_numerator, frame_denominator),
            'frame_control_details': frame_details}


def build():
    readings = json.loads((HERE / 'readings.json').read_text())['records']
    records = [{**r, 'families': {f: analyze(r, f) for f in FAMILIES}} for r in readings]
    paths = [HERE / 'README.md', HERE / 'readings.json', HERE / 'analyze.py', ORBIT_SOURCE,
             HERE.parent.parent / 'sources' / 'LOCAL-PDFS.json']
    result = {'status': 'Discovery erasure diagnostic; no historical prediction score',
              'hashes': {str(p.relative_to(HERE.parent.parent)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in paths}, 'records': records}
    lines = ['# Capital-overlay diagnostic', '',
             'TA is the predeclared primary family. Counts refer to edited, exposed grids.', '',
             '| Grid | Capitals | Full conflicting orbits | After erasure | Further lowercase erasures needed | Forced changed / same / free capitals | Compatible masks, count-matched | Compatible masks, frame-matched |',
             '|---|---:|---:|---:|---:|---|---|---|']
    for r in records:
        a = r['families']['TA']
        changed = sum(c['changed'] for c in a['conditional_precursor_cells'])
        same = len(a['conditional_precursor_cells']) - changed
        precursor = f"{changed} / {same} / {len(a['unconstrained_capital_cells'])}" if a['compatible_after_capital_erasure'] else 'incompatible'
        lines.append(f"| {r['id']} ({r['figure']}) | {len(a['capital_cells'])} | {a['full_conflicting_orbits']} | {len(a['residual_conflicts'])} | {a['minimum_further_lowercase_erasures']} | {precursor} | {a['count_matched_control']['reduced']} | {a['frame_matched_control']['reduced']} |")
    lines += ['', '## All declared families', '', '| Grid | T | A | TA | HV | D4 |', '|---|---:|---:|---:|---:|---:|']
    for r in records:
        lines.append('| ' + r['id'] + ' | ' + ' | '.join(str(len(r['families'][f]['residual_conflicts'])) for f in FAMILIES) + ' |')
    lines += ['', 'Entries are residual conflicting orbits after capital erasure. Zero means compatibility,',
              'not proof of historical construction. JSON preserves conflicts and conditional letters.', '',
              'Controls count compatible masks exactly. They are descriptive fractions, not p-values.',
              'No name spelling, traversal or independent lexical input is tested. A forced precursor',
              'letter is conditional on the specified symmetry and unchanged lowercase cells.', '']
    return {'results.json': json.dumps(result, ensure_ascii=False, indent=2) + '\n',
            'RESULTS.md': '\n'.join(lines)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for name, content in build().items():
        path = HERE / name
        if args.check:
            if path.read_text() != content:
                raise SystemExit(f'Output differs: {name}')
        else:
            path.write_text(content)
    print('Capital-overlay outputs verified.' if args.check else 'Capital-overlay outputs written.')

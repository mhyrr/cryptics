"""Audit exposed sequences and geometry; never evaluate a historical recipe."""
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent / '05-period-dictionary'
FAMILIES = {'I': (), 'T': ('T',), 'A': ('A',), 'TA': ('T', 'A'),
            'HV': ('H', 'V'), 'D4': ('T', 'H', 'V')}


def normalize(s):
    return s.replace('ſ', 's').translate(str.maketrans(
        'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))


def transform(cell, n, name):
    r, c = cell
    return {'T': (c, r), 'A': (n + 1 - c, n + 1 - r),
            'H': (n + 1 - r, c), 'V': (r, n + 1 - c)}[name]


def orbits(n, family):
    unseen = {(r, c) for r in range(1, n + 1) for c in range(1, n + 1)}
    result = []
    while unseen:
        orbit = {min(unseen)}
        frontier = list(orbit)
        while frontier:
            cell = frontier.pop()
            for name in FAMILIES[family]:
                other = transform(cell, n, name)
                if other not in orbit:
                    orbit.add(other)
                    frontier.append(other)
        unseen -= orbit
        result.append(sorted(orbit))
    return result


def path_cells(path):
    r, c = path['start']
    dr, dc = path['step']
    return [(r + i * dr, c + i * dc) for i in range(path['length'])]


def geometry(n, family, path):
    boundary = {(r, c) for r in range(1, n + 1) for c in range(1, n + 1)
                if r in (1, n) or c in (1, n)}
    groups = orbits(n, family)
    inner = [o for o in groups if not set(o) & boundary]
    reached = [o for o in inner if set(o) & set(path)]
    free = [o for o in inner if not set(o) & set(path)]
    return dict(all_orbits=groups, interior_orbits=inner,
                interior_orbits_reached_by_path=reached,
                unconstrained_interior_orbits=free,
                interior_orbits_reached_by_boundary=[o for o in inner if set(o) & boundary],
                path_cells_in_boundary_orbits=[c for c in path if any(
                    c in o and set(o) & boundary for o in groups)])


def analyze(ex, readings):
    raw = ex['rows_raw']
    n = len(raw)
    if not n or any(len(row) != n for row in raw):
        raise ValueError(f"Non-square input: {ex['id']}")
    grid = [normalize(row) for row in raw]
    at = lambda cell: grid[cell[0] - 1][cell[1] - 1]
    path = path_cells(ex['path'])
    if len(set(path)) != len(path) or any(not (1 <= r <= n and 1 <= c <= n) for r, c in path):
        raise ValueError('Invalid nominated path')
    word = normalize(ex['square_string'])
    value = ''.join(map(at, path))
    if value != word:
        raise ValueError(f"Nominated path does not read cited string: {ex['id']}")
    occurrences = []
    for axis in ('row', 'column'):
        for i in range(1, n + 1):
            cells = [(i, j) if axis == 'row' else (j, i) for j in range(1, n + 1)]
            for direction, trial in (('forward', cells), ('reverse', cells[::-1])):
                if ''.join(map(at, trial)) == word:
                    occurrences.append(dict(axis=axis, index=i, direction=direction, cells=trial))
    families = {}
    for family in FAMILIES:
        report = geometry(n, family, path)
        report['full_grid_conflicts'] = [dict(cells=o, letters=sorted({at(c) for c in o}))
                                        for o in report['all_orbits'] if len({at(c) for c in o}) > 1]
        report['full_grid_compatible'] = not report['full_grid_conflicts']
        report['path_conflicts'] = [o for o in report['all_orbits']
                                    if len({at(c) for c in o if c in path}) > 1]
        families[family] = report
    lexical = None
    if ex['facsimile_record']:
        record = readings[ex['facsimile_record']]
        target = record['target_transliteration_raw']
        for op in record['layout_operations']:
            if op['operation'] != 'join_printed_line_break' or target != op['from']:
                raise ValueError('Unknown layout operation')
            target = op['to']
        alternative_lengths = []
        for alt in record['alternative_transliterations']:
            raw_alt = alt.get('raw')
            eligible = bool(raw_alt) and not alt['uncertain'] and '\n' not in raw_alt
            alternative_lengths.append(dict(raw=raw_alt, eligible_without_further_operations=eligible,
                                            length=len(raw_alt) if eligible else None,
                                            fits_nominated_path=normalize(raw_alt) == value if eligible else None))
        lexical = dict(image=record['image'], headword_raw=record['headword_raw'],
                       target_raw=record['target_transliteration_raw'],
                       layout_operations=record['layout_operations'],
                       alternatives=record['alternative_transliterations'],
                       alternative_lengths=alternative_lengths,
                       target_normalized=normalize(target), target_length=len(target),
                       target_exactly_fits_nominated_path=normalize(target) == value)
    overlap = None
    if ex.get('overlap_components'):
        components = []
        for component in ex['overlap_components']:
            cells = path_cells(component)
            components.append(dict(cells=cells, word=component['word'],
                                   agrees=''.join(map(at, cells)) == normalize(component['word'])))
        shared = sorted(set(components[0]['cells']).intersection(*(set(c['cells']) for c in components[1:])))
        overlap = dict(components=components, shared_cells=shared,
                       status='Exposed-string explanation only; dictionary and applicability not verified')
    return dict(id=ex['id'], size=n, caption=ex['caption_display'], locator=ex['edition_locator'],
                source_url=ex['edition_url'], source_figure_verified=False,
                normalized_rows=grid, nominated_path=path, nominated_path_reading=value,
                nominated_inner_cells=[c for c in path if 1 < c[0] < n and 1 < c[1] < n],
                full_line_occurrences=occurrences, lexical=lexical, proposed_overlap=overlap,
                capitals=[dict(cell=(r, c), letter=ch) for r, row in enumerate(raw, 1)
                          for c, ch in enumerate(row, 1) if 'A' <= ch <= 'Z'],
                symmetry=families)


def table(result):
    lines = ['# Construction-evidence table (generated)', '',
             'All coordinates refer to polygrams placed as rows. Source diagrams remain unverified.',
             'Exact fit means the previously image-read dictionary target, not a historical prediction.',
             'Free-orbit columns are **conditional geometry**: boundary plus nominated square-string path.',
             'They use exposed square spellings even when those spellings do not match the dictionary.',
             'A conflicting family does not describe a completion of the full unmodified grid.', '',
             '| Example; edition page,line | Caption | Source string → cited string; alternatives | Nominated path | Full-grid compatible families | Free inner orbits I / T / A / TA / HV / D4 | Exact dictionary fit |',
             '|---|---|---|---|---|---|---|---|']
    for r in result['records']:
        lex = r['lexical']
        if lex:
            candidates = ', '.join(str(a.get('raw') or a.get('candidates')) + (' [?]' if a['uncertain'] else '')
                                   for a in lex['alternatives']) or 'none in scoped excerpt'
            reading = f"{lex['target_raw']} → {r['nominated_path_reading']}; {candidates}"
        else:
            reading = f"unverified dictionary input → {r['nominated_path_reading']}"
        reading = reading.replace('\n', ' / ')
        compatible = ', '.join(f for f, x in r['symmetry'].items() if x['full_grid_compatible'])
        counts = ' / '.join(str(len(x['unconstrained_interior_orbits'])) for x in r['symmetry'].values())
        fit = str(lex['target_exactly_fits_nominated_path']).lower() if lex else 'not checked'
        lines.append(f"| {r['id']}; {r['locator']} | {r['caption']} | {reading} | {r['nominated_path'][0]} → {r['nominated_path'][-1]} | {compatible} | {counts} | {fit} |")
    lines += ['', 'I = identity; T = main diagonal; A = anti-diagonal; TA = both diagonals;',
              'HV = horizontal and vertical reflections; D4 = all eight square isometries.', '',
              '## Paths, alternatives, and residual constraints', '',
              'The nominated paths are observations from exposed sequences, not permitted evaluation placements.',
              'Only case/long-s folding and the logged water line join are allowed for exact source comparison.',
              'No spelling edits or historical propagation are authorized. Full coordinate lists, capital',
              'positions, conflicts and all alternative full-line occurrences are in `results.json`.',
              'Additional entry candidates, caption ambiguity, name insertion, overlap recipes and the',
              'missing applicability rule are discussed in `EVIDENCE.md` and `examples.json`.', '']
    return '\n'.join(lines)


def build():
    data = json.loads((HERE / 'examples.json').read_text())
    readings = {r['id']: r for r in json.loads((PRIOR / 'facsimile-readings.json').read_text())['records']}
    inputs = [HERE / 'README.md', HERE / 'examples.json', HERE / 'audit.py', PRIOR / 'facsimile-readings.json']
    result = dict(status='Discovery geometry only; historical performance not evaluated',
                  source_figure_verified=False, historical_performance=None,
                  hashes={str(p.relative_to(HERE.parent)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
                  records=[analyze(ex, readings) for ex in data['examples']])
    # TABLE.md is the human report; keep repeated coordinate arrays compact.
    return {'results.json': json.dumps(result, ensure_ascii=False, separators=(',', ':')) + '\n', 'TABLE.md': table(result)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for name, content in build().items():
        path = HERE / name
        if args.check:
            if not path.exists() or path.read_text() != content:
                raise SystemExit(f'Output differs: {path}')
        else:
            path.write_text(content)
    print('Construction audit outputs verified.' if args.check else 'Construction audit outputs written.')


if __name__ == '__main__':
    main()

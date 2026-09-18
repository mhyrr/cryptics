"""Separate source discrepancies from conditional overlay diagnostics."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OVERLAY = HERE.parent / '08-capital-overlay' / 'analyze.py'
spec = importlib.util.spec_from_file_location('overlay', OVERLAY)
overlay = importlib.util.module_from_spec(spec)
spec.loader.exec_module(overlay)


def build():
    data = json.loads((HERE / 'readings.json').read_text())
    compilation_path = HERE.parent / '07-published-diagrams' / 'readings.json'
    prior_path = HERE.parent / '08-capital-overlay' / 'readings.json'
    compilation = {r['id']: r for r in json.loads(compilation_path.read_text())['records']}
    prior = {r['id']: r for r in json.loads(prior_path.read_text())['records']}
    differences = []
    for reading in data['figure_readings']:
        old = compilation[reading['id']]['rows']
        new = reading['rows']
        if len(new) != len(old) or any(len(row) != len(old) for row in new):
            raise ValueError('Figure dimensions differ')
        cells = [{'cell': [r + 1, c + 1], 'compilation': old[r][c], 'draft_figure': value}
                 for r, row in enumerate(new) for c, value in enumerate(row) if value != old[r][c]]
        differences.append({'id': reading['id'], 'differences': cells})
    results = []
    for name, family in data['prior_family_comparisons'].items():
        results.append({'id': name, 'reading_basis': 'compilation; not discrepant draft figure',
                        **overlay.analyze(prior[name], family)})
    for record in data['overlay_examples']:
        results.append({'id': record['id'], 'reading_basis': 'draft figure, visually checked',
                        **overlay.analyze(record, record['family'])})
    all_readings = {**prior, **{r['id']: r for r in data['overlay_examples']}}
    for record in results:
        n = len(all_readings[record['id']]['rows'])
        mask = {tuple(c) for c in record['capital_cells']}
        free_orbits = [o for o in overlay.geometry.orbits(n, record['family']) if set(o) <= mask]
        record['free_orbits'] = free_orbits
        record['conditional_completions_over_A_Z'] = 26 ** len(free_orbits) if record['compatible_after_capital_erasure'] else 0
    paths = [HERE / 'README.md', HERE / 'readings.json', HERE / 'source.json', HERE / 'audit.py',
             compilation_path, prior_path, OVERLAY, overlay.ORBIT_SOURCE]
    result = {'status': 'Source audit and conditional discovery diagnostics; no historical score',
              'hashes': {str(p.relative_to(HERE.parent)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'figure_comparisons': differences, 'overlay_diagnostics': results}
    lines = ['# Structural-draft audit', '', '## Figure comparisons', '']
    for d in differences:
        lines.append(f"- {d['id']}: {len(d['differences'])} differing cells.")
        for cell in d['differences']:
            value = 'blank' if cell['draft_figure'] is None else cell['draft_figure']
            lines.append(f"  - {cell['cell']}: compilation `{cell['compilation']}`; draft figure `{value}`.")
    lines += ['', '## Conditional overlay diagnostics', '',
              '| Grid | Family | Lowercase conflicting orbits after erasure | Minimum further lowercase erasures | Forced changed / same / free capitals | Conditional A–Z completions |',
              '|---|---|---:|---:|---|---:|']
    for r in results:
        forced = r['conditional_precursor_cells']
        changed = sum(c['changed'] for c in forced)
        detail = f"{changed} / {len(forced)-changed} / {len(r['unconstrained_capital_cells'])}" if r['compatible_after_capital_erasure'] else 'incompatible'
        lines.append(f"| {r['id']} | {r['family']} | {len(r['residual_conflicts'])} | {r['minimum_further_lowercase_erasures']} | {detail} | {r['conditional_completions_over_A_Z']} |")
    lines += ['', 'Compatible examples do not supply the lost letters of wholly erased orbits.',
              'The four free inner cells of a 2×2 center must not be confused with four independent',
              'letters: the JSON lists cells, while the selected symmetry may link some of them.',
              'No historical prediction accuracy is measured. Source-specified families are discovery',
              'interpretations, not an independently selected recipe for new squares.', '']
    return {'results.json': json.dumps(result, ensure_ascii=False, indent=2) + '\n', 'RESULTS.md': '\n'.join(lines)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--check-source', action='store_true')
    args = parser.parse_args()
    if args.check_source:
        source = json.loads((HERE / 'source.json').read_text())
        path = HERE.parent.parent / 'sources' / source['file']
        if hashlib.sha256(path.read_bytes()).hexdigest() != source['sha256']:
            raise SystemExit('Source PDF checksum differs')
        print('Structural draft PDF checksum verified.')
    else:
        for name, content in build().items():
            p = HERE / name
            if args.check:
                if p.read_text() != content:
                    raise SystemExit(f'Output differs: {name}')
            else:
                p.write_text(content)
        print('Draft audit verified.' if args.check else 'Draft audit written.')

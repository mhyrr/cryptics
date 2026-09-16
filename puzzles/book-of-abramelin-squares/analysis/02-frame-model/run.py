#!/usr/bin/env python3
"""Fit independent frame symmetries under a fixed symbol-plus-error code cost."""
from collections import Counter
import math
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'stressbench'))
from common import (GROUPS, aggregate, control, exact_symmetry, letter_mode, load,
                    majority, mask, orbits, provenance, report, rng, score, write_result)

ERROR_COST = math.log2(25 * .95 / .05)
SYMBOL_COST = math.log2(26)


def frame_model(grid):
    n = len(grid)
    predictions, repairs, frames = {}, {}, []
    for ring in range((n+1)//2):
        models = []
        for group in GROUPS:
            assignments = {}
            edits = symbols = 0
            for orbit in orbits(n, group, ring):
                values = [grid[r][c] for r, c in orbit if grid[r][c] is not None]
                if values:
                    symbols += 1
                    edits += len(values)-max(Counter(values).values())
                    value = majority(values)
                    if value is not None:
                        assignments.update({p: value for p in orbit})
            cost = symbols*SYMBOL_COST + edits*ERROR_COST
            models.append((cost, group, assignments, edits))
        best_cost = min(m[0] for m in models)
        best = [m for m in models if abs(m[0]-best_cost) < 1e-9]
        frames.append({'ring': ring, 'models': [m[1] for m in best],
                       'cost': best_cost, 'minimum_edits': min(m[3] for m in best)})
        # Identity or any tied model without a prediction vetoes the cell.
        for p in set.intersection(*(set(m[2]) for m in best)):
            values = {m[2][p] for m in best}
            if len(values) == 1:
                value = next(iter(values))
                r, c = p
                if grid[r][c] is None:
                    predictions[p] = value
                elif grid[r][c] != value:
                    repairs[p] = value
    return predictions, repairs, frames


def corruption_trials(records, kind):
    details = []
    for s in records:
        truth = s['grid']
        n = len(truth)
        for count in (1, 2):
            rand = rng((kind, s['id'], 'damage', count))
            positions = rand.sample([(r,c) for r in range(n) for c in range(n)], count)
            damaged = [row[:] for row in truth]
            for r, c in positions:
                damaged[r][c] = rand.choice([x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if x != truth[r][c]])
            _, repairs, _ = frame_model(damaged)
            correct = sum(v == truth[r][c] for (r,c),v in repairs.items())
            collateral = sum((r,c) not in positions for r,c in repairs)
            repaired = [row[:] for row in damaged]
            for (r,c),v in repairs.items():
                repaired[r][c] = v
            details.append({'id':s['id'], 'control':kind, 'injected':count,
                            'suggested':len(repairs), 'correct':correct,
                            'wrong':len(repairs)-correct, 'collateral':collateral,
                            'exact_grid': repaired == truth,
                            'corrupted':positions,
                            'repairs': [[r,c,v] for (r,c),v in sorted(repairs.items())]})
    return details


def planted():
    records = []
    for i in range(60):
        rand = rng(('planted_frames',i))
        n = (5,6,7)[i%3]
        grid = [[None]*n for _ in range(n)]
        for ring in range((n+1)//2):
            family = ('diagonals','transpose','anti_transpose','axes')[(i+ring)%4]
            for orbit in orbits(n, family, ring):
                value = rand.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                for r,c in orbit:
                    grid[r][c] = value
        hidden = rand.sample([(r,c) for r in range(n) for c in range(n)], round(n*n/4))
        records.append({'id':f'planted-{i}', 'grid':grid, 'masks':{'cells':hidden}})
    return records


def main():
    original = load()
    audit, damage = [], []
    family_counts = Counter()
    for kind in ('original','shuffled','symmetric_original','orbit_shuffled','planted_frames'):
        records = planted() if kind == 'planted_frames' else control(original,kind)
        for s in records:
            train = [t for t in records if t['id'] != s['id']] if kind == 'planted_frames' else [t for t in records if t['fold'] != s['fold']]
            mode = letter_mode(train)
            for pattern,hidden in s['masks'].items():
                observed = mask(s['grid'],hidden)
                preds, _, frames = frame_model(observed)
                for method,p in [('frame_mdl',preds),('global_exact',exact_symmetry(observed))]:
                    audit.append({'id':s['id'],'control':kind,'mask':pattern,'method':method,
                                  'fold':s.get('fold'), 'score':score(s['grid'],hidden,p,mode),
                                  'predictions':[[r,c,v] for (r,c),v in sorted(p.items())]})
            if kind == 'original':
                for f in frame_model(s['grid'])[2]:
                    family_counts['+'.join(f['models'])] += 1
        if kind in ('original','shuffled','planted_frames'):
            damage.extend(corruption_trials(records,kind))
            # Measure edits suggested to undamaged digital inputs too.
            for s in records:
                repairs = frame_model(s['grid'])[1]
                damage.append({'id':s['id'],'control':kind,'injected':0,
                               'suggested':len(repairs), 'correct':0,'wrong':len(repairs),
                               'collateral':len(repairs), 'exact_grid':not repairs,
                               'repairs': [[r,c,v] for (r,c),v in sorted(repairs.items())]})
    damage_totals = {}
    for kind in ('original','shuffled','planted_frames'):
        for count in (0,1,2):
            ds = [d for d in damage if d['control']==kind and d['injected']==count]
            damage_totals[f'{kind}|{count}'] = {'grids':len(ds), **{
                key:sum(d[key] for d in ds) for key in ('injected','suggested','correct','wrong','collateral','exact_grid')}}
    summary = aggregate(audit)
    write_result(HERE/'results.json',{'provenance':provenance(),'summary':summary,
                 'frame_model_counts':dict(family_counts),'corruption':damage_totals,
                 'corruption_audit':damage,'records':audit})
    report(HERE/'RESULTS.md','02 — Frame rules and error tolerance',summary,
           'Fixed 5% error channel; ties abstain. Accuracy is against withheld digital cells. '
           'The symmetric-original and orbit-shuffled controls use the identical subset. '
           'Corruption results are in results.json; no source reading was changed.')
    print('02 completed:',len(audit),'evaluation cases;',len(damage),'corruption cases')


if __name__ == '__main__':
    main()

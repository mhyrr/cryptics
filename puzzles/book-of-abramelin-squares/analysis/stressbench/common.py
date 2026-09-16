"""Shared deterministic data, masks, controls and scoring. Standard library only."""
from collections import Counter, defaultdict
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import random

HERE = Path(__file__).resolve().parent
ANALYSIS = HERE.parent
CORPUS = ANALYSIS.parent / 'sources/mathers-squares.json'
SEED = 20260916


def digest(value):
    return hashlib.sha256(str(value).encode()).hexdigest()


def rng(key):
    return random.Random(int(digest((SEED, key)), 16))


def orient(grid, k):
    out = [list(row) for row in grid]
    for _ in range(k % 4):
        out = [list(row) for row in zip(*out[::-1])]
    return [row[::-1] for row in out] if k >= 4 else out


def transform(r, c, n, k):
    for _ in range(k % 4):
        r, c = c, n - 1 - r
    return (r, n - 1 - c) if k >= 4 else (r, c)


# Each tuple lists generators; closure supplies all members.
GROUPS = {'identity': (), 'transpose': (5,), 'anti_transpose': (7,),
          'half_turn': (2,), 'quarter_turn': (1,),
          'column_reflection': (4,), 'row_reflection': (6,),
          'diagonals': (7, 2), 'axes': (4, 6), 'd4': (1, 4)}


@lru_cache(None)
def orbits(n, group, ring=None):
    left = {(r, c) for r in range(n) for c in range(n)
            if ring is None or min(r, c, n-1-r, n-1-c) == ring}
    result = []
    while left:
        seed = min(left)
        orbit, todo = {seed}, [seed]
        while todo:
            r, c = todo.pop()
            for k in GROUPS[group]:
                p = transform(r, c, n, k)
                if p not in orbit:
                    orbit.add(p)
                    todo.append(p)
        left -= orbit
        result.append(tuple(sorted(orbit)))
    return tuple(result)


def majority(values):
    counts = Counter(values)
    if not counts:
        return None
    best = max(counts.values())
    winners = [x for x, count in counts.items() if count == best]
    return winners[0] if len(winners) == 1 else None


def write_result(path, data):
    """One per-case audit record per line; readable summary above it."""
    data = dict(data)
    records = data.pop('records', [])
    head = json.dumps(data, indent=2, sort_keys=True)
    path.write_text(head[:-2] + ',\n  "records": [\n' + ',\n'.join(
        '    ' + json.dumps(r, sort_keys=True) for r in records) + '\n  ]\n}\n')


def group_records(records):
    """Assign connected seed/orientation families together; mutate metadata only."""
    parent = list(range(len(records)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    keys = {}
    for i, s in enumerate(records):
        seed = ''.join(s['grid'][0])
        canonical = min(''.join(''.join(row) for row in orient(s['grid'], k)) for k in range(8))
        for key in [('seed', min(seed, seed[::-1])), ('grid', len(s['grid']), canonical)]:
            if key in keys:
                parent[find(i)] = find(keys[key])
            keys[key] = i
    members = defaultdict(list)
    for i, s in enumerate(records):
        members[find(i)].append(s['id'])
    for i, s in enumerate(records):
        s['group'] = min(members[find(i)])
        s['fold'] = int(digest(s['group'])[:8], 16) % 5
    return len(members)


def prepare():
    all_rows = json.loads(CORPUS.read_text())['squares']
    records = [dict(id=s['id'], grid=s['grid']) for s in all_rows
               if s['grid'] and all(x is not None for row in s['grid'] for x in row)]
    groups = group_records(records)
    for s in records:
        n = len(s['grid'])
        cells = [(r, c) for r in range(n) for c in range(n)]
        random_hidden = rng((s['id'], 'cells')).sample(cells, max(1, round(n*n/4)))
        os = list(orbits(n, 'd4'))
        erased = rng((s['id'], 'orbits')).sample(os, max(1, round(len(os)/4)))
        s['masks'] = {'cells': sorted(random_hidden),
                      'orbits': sorted(p for orbit in erased for p in orbit),
                      'gnomon': [(r, c) for r in range(1, n) for c in range(1, n)]}
    out = {'seed': SEED, 'corpus_sha256': hashlib.sha256(CORPUS.read_bytes()).hexdigest(),
           'groups': groups, 'fold_counts': dict(Counter(s['fold'] for s in records)),
           'records': records}
    write_result(HERE / 'manifest.json', out)
    return out


def load():
    data = json.loads((HERE / 'manifest.json').read_text())
    assert data['corpus_sha256'] == hashlib.sha256(CORPUS.read_bytes()).hexdigest()
    return data['records']


def mask(grid, hidden):
    out = [row[:] for row in grid]
    for r, c in hidden:
        out[r][c] = None
    return out


def is_symmetric(grid, group='diagonals'):
    return all(len({grid[r][c] for r, c in orbit}) == 1 for orbit in orbits(len(grid), group))


def control(records, kind):
    out = []
    for s in records:
        grid = [row[:] for row in s['grid']]
        n = len(grid)
        rand = rng((s['id'], kind))
        if kind == 'shuffled':
            values = [x for row in grid for x in row]
            rand.shuffle(values)
            grid = [values[r*n:(r+1)*n] for r in range(n)]
        elif kind in ('symmetric_original', 'orbit_shuffled'):
            if not is_symmetric(grid):
                continue
            if kind == 'orbit_shuffled':
                sizes = defaultdict(list)
                for orbit in orbits(n, 'diagonals'):
                    sizes[len(orbit)].append(orbit)
                for os in sizes.values():
                    values = [grid[orbit[0][0]][orbit[0][1]] for orbit in os]
                    rand.shuffle(values)
                    for orbit, value in zip(os, values):
                        for r, c in orbit:
                            grid[r][c] = value
        elif kind != 'original':
            raise ValueError(kind)
        out.append(dict(s, grid=grid))
    return out


def letter_mode(train):
    counts = Counter(x for s in train for row in s['grid'] for x in row)
    return min(counts, key=lambda x: (-counts[x], x))


def exact_symmetry(grid):
    if any(len({grid[r][c] for r, c in orbit if grid[r][c] is not None}) > 1
           for orbit in orbits(len(grid), 'diagonals')):
        return {}
    preds = {}
    for orbit in orbits(len(grid), 'diagonals'):
        values = {grid[r][c] for r, c in orbit if grid[r][c] is not None}
        if values:
            value = next(iter(values))
            preds.update({(r, c): value for r, c in orbit if grid[r][c] is None})
    return preds


def score(truth, hidden, predictions, baseline):
    hidden = {tuple(p) for p in hidden}
    if not set(predictions) <= hidden:
        raise ValueError('Predicted a visible/non-target cell')
    correct = sum(truth[r][c] == value for (r, c), value in predictions.items())
    count = len(predictions)
    return {'tasks': 1, 'hidden': len(hidden), 'predicted': count, 'correct': correct,
            'wrong': count-correct, 'abstained': len(hidden)-count,
            'baseline_correct_same_cells': sum(truth[r][c] == baseline for r, c in predictions),
            'baseline_correct_all_hidden': sum(truth[r][c] == baseline for r, c in hidden),
            'exact_tasks': int(correct == len(hidden)),
            'tasks_with_predictions': int(count > 0)}


def aggregate(records):
    totals = defaultdict(Counter)
    for r in records:
        key = '|'.join(str(r[k]) for k in ('control', 'mask', 'method'))
        totals[key].update(r['score'])
    result = {}
    for key, counts in sorted(totals.items()):
        d = dict(counts)
        d['accuracy'] = counts['correct']/counts['predicted'] if counts['predicted'] else None
        d['coverage'] = counts['predicted']/counts['hidden'] if counts['hidden'] else 0
        d['baseline_accuracy_same_cells'] = counts['baseline_correct_same_cells']/counts['predicted'] if counts['predicted'] else None
        result[key] = d
    return result


def report(path, title, summary, notes):
    lines = [f'# {title}', '', notes, '',
             '| Control / mask / method | Correct / predicted | Coverage | Baseline correct on same cells | Exact tasks |',
             '|---|---:|---:|---:|---:|']
    for key, s in summary.items():
        lines.append(f"| {key.replace('|', ' / ')} | {s['correct']}/{s['predicted']} | {100*s['coverage']:.1f}% | {s['baseline_correct_same_cells']} | {s['exact_tasks']}/{s['tasks']} |")
    path.write_text('\n'.join(lines) + '\n')


def provenance():
    return {'manifest_sha256': hashlib.sha256((HERE/'manifest.json').read_bytes()).hexdigest(),
            'corpus_sha256': hashlib.sha256(CORPUS.read_bytes()).hexdigest(),
            'seed': SEED, 'scope': 'Internal feasibility tests; no independent manuscript targets.'}


if __name__ == '__main__':
    d = prepare()
    print(json.dumps({k:v for k,v in d.items() if k != 'records'}, indent=2))

"""Source audit and synthetic constraint preflight; no historical scoring."""
import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import random
import string
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'stressbench'))
from common import exact_symmetry, mask, orbits, score


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(raw):
    value = raw.replace('ſ', 's').upper()
    if not value or any(c not in string.ascii_uppercase for c in value):
        raise ValueError('Not an unambiguous Latin-letter token')
    return value


def solve(observed, placements, alphabet=string.ascii_uppercase):
    """Exact diagonal-symmetric models with fixed paths and finite word domains.

    Each branch assigns the same set of orbits. Remaining orbits independently
    range over alphabet. Thus unique branches are disjoint and counts add.
    No truth or captions enter this solver. Caption filtering belongs upstream.
    Suitable only for small frozen candidate sets; no silent search truncation.
    """
    n = len(observed)
    if not n or any(len(row) != n for row in observed):
        raise ValueError('Expected square')
    if not alphabet or len(set(alphabet)) != len(alphabet):
        raise ValueError('Alphabet must be nonempty and unique')
    os = orbits(n, 'diagonals')
    lookup = {p: i for i, orbit in enumerate(os) for p in orbit}
    assignments = {}
    impossible = {'completion_count': 0, 'branches': [], 'predictions': []}
    for r, row in enumerate(observed):
        for c, letter in enumerate(row):
            if letter is None:
                continue
            if letter not in alphabet:
                raise ValueError('Observed letter outside alphabet')
            i = lookup[r, c]
            if i in assignments and assignments[i] != letter:
                return impossible
            assignments[i] = letter
    branches = {tuple(sorted(assignments.items()))}
    for path, words in placements:
        path = [tuple(p) for p in path]
        if not path or any(p not in lookup for p in path):
            raise ValueError('Invalid placement')
        words = sorted(set(words))
        if any(len(w) != len(path) or any(c not in alphabet for c in w) for w in words):
            raise ValueError('Invalid word length/alphabet')
        new = set()
        for branch, word in itertools.product(sorted(branches), words):
            values = dict(branch)
            for p, letter in zip(path, word):
                i = lookup[p]
                if i in values and values[i] != letter:
                    break
                values[i] = letter
            else:
                new.add(tuple(sorted(values.items())))
        branches = new
    if not branches:
        return impossible
    branches = [dict(b) for b in sorted(branches)]
    # Fixed paths imply the same assigned orbit set in every branch.
    assert all(set(b) == set(branches[0]) for b in branches)
    out = []
    for b in branches:
        free = [i for i in range(len(os)) if i not in b]
        out.append({'assigned_orbits': [[i, v] for i, v in sorted(b.items())],
                    'free_orbits': free,
                    'completions': len(alphabet) ** len(free)})
    predictions = []
    for r in range(n):
        for c in range(n):
            if observed[r][c] is not None:
                continue
            i = lookup[r, c]
            values = {b[i] for b in branches if i in b}
            if all(i in b for b in branches) and len(values) == 1:
                predictions.append([r, c, next(iter(values))])
            elif i not in branches[0] and len(alphabet) == 1:
                predictions.append([r, c, alphabet[0]])
    return {'completion_count': sum(b['completions'] for b in out),
            'orbits': os, 'free_domain': alphabet, 'branches': out,
            'predictions': predictions}


def evaluate():
    freeze = json.loads((HERE / 'freeze.json').read_text())
    for name, expected in freeze['files'].items():
        if sha(HERE / name) != expected:
            raise ValueError(f'Frozen input changed: {name}; start a new protocol revision')
    claims = json.loads((HERE / 'claims.json').read_text())
    audit = []
    for row in claims['records']:
        a, b = normalize(row['reported_dictionary_spelling']), normalize(row['edition_square_spelling'])
        audit.append({'id': row['id'], 'normalized_quoted_dictionary': a,
                      'normalized_edition_square': b, 'exact': a == b,
                      'primary_verified': row['facsimile_verified']})
    fixture = json.loads((HERE / 'synthetic.json').read_text())
    truth = [list(row) for row in fixture['rows']]
    hidden = fixture['hidden']
    n = len(truth)
    targets = set(map(tuple, hidden))
    assert all(not (targets & set(o)) or set(o) <= targets for o in orbits(n, 'd4'))
    observed = mask(truth, hidden)
    words = fixture['lexicon']
    alternative = sorted(set(words + [fixture['alternative_center_word']]))
    shuffled = []
    rand = random.Random(fixture['shuffle_seed'])
    for word in words:
        letters = list(word)
        rand.shuffle(letters)
        shuffled.append(''.join(letters))
    freq = Counter(''.join(words))
    baseline = min(freq, key=lambda c: (-freq[c], c))
    cases = []
    for label, domain, rows in [
            ('planted_unique', words, fixture['constrained_rows']),
            ('competing_center', alternative, fixture['constrained_rows']),
            ('seed_only', words, []),
            ('contradiction', ['ZZZZZ'], fixture['constrained_rows']),
            ('word_shuffle', shuffled, fixture['constrained_rows'])]:
        placements = [([(r, c) for c in range(n)], domain) for r in rows]
        result = solve(observed, placements, fixture['alphabet'])
        predictions = {(r, c): v for r, c, v in result['predictions']}
        cases.append({'case': label, 'placements': placements, 'result': result,
                      'score': score(truth, hidden, predictions, baseline)})
    symmetric = exact_symmetry(observed)
    return {'status': 'historical_evaluation_blocked',
            'wall': 'No dictionary entry facsimiles verified; no independent lexicon or justified interior placement rule.',
            'historical_scores': None, 'historical_predictions': None,
            'hashes': {name: sha(HERE / name) for name in
                       ['PROTOCOL.md', 'claims.json', 'synthetic.json', 'freeze.json',
                        'run.py', '../stressbench/common.py']},
            'quoted_spelling_audit': audit,
            'synthetic': {'scope': 'Software preflight only; one artificial square, overlapping cases.',
                          'frequency_baseline_letter': baseline,
                          'symmetry_score': score(truth, hidden, symmetric, baseline),
                          'cases': cases}}


def report(data):
    lines = ['# Experiment 05 preflight results', '',
             '**Historical dictionary test: BLOCKED, not failed.**', '',
             data['wall'], '',
             'No Mathers reconstruction was scored. No incomplete-square or German-witness',
             'predictions were issued. The quoted spelling audit is not primary verification.', '',
             '| Quoted pair | Exact after long-s/case folding | Dictionary facsimile verified |',
             '|---|---|---|']
    for a in data['quoted_spelling_audit']:
        lines.append(f"| {a['id']} | {a['exact']} | {a['primary_verified']} |")
    lines += ['', '## Synthetic machinery checks', '',
              'One artificial square; these overlapping cases are not independent trials.',
              'All nine inner cells are hidden together, including every reflected copy.',
              'Branches in results.json enumerate assignments and all residual orbit domains.', '',
              '| Case | Completions | Correct | Errors | Abstentions | Coverage | Exact square | Frequency correct on same cells |',
              '|---|---:|---:|---:|---:|---:|---:|---:|']
    for case in data['synthetic']['cases']:
        s = case['score']
        lines.append(f"| {case['case']} | {case['result']['completion_count']} | {s['correct']} | {s['wrong']} | {s['abstained']} | {s['predicted']/s['hidden']:.1%} | {s['exact_tasks']} | {s['baseline_correct_same_cells']} |")
    s = data['synthetic']['symmetry_score']
    lines += ['', f"Symmetry alone predicts {s['predicted']}/{s['hidden']} hidden cells.",
              'The artificial-vocabulary modal baseline and per-case denominators are saved',
              'in JSON. The one shuffled vocabulary is a software control, not a p-value.',
              'No historical performance, randomness or recipe rejection follows from these checks.', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='compare outputs without writing')
    args = parser.parse_args()
    result = evaluate()
    outputs = {'results.json': json.dumps(result, indent=2, sort_keys=True) + '\n',
               'RESULTS.md': report(result)}
    for name, text in outputs.items():
        path = HERE / name
        if args.check:
            if path.read_text() != text:
                raise SystemExit(f'Not reproducible: {name}')
        else:
            path.write_text(text)
    print('Preflight outputs verified' if args.check else 'Preflight outputs written; historical evaluation BLOCKED')

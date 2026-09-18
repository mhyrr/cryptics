"""E2 staged internal evaluation. Selector and predictor take no answer file."""
import argparse
from collections import Counter, defaultdict
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import random
import string
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ANALYSIS = HERE.parent
sys.path.insert(0, str(ANALYSIS / '10-caption-selector'))
from recipe import solve
sys.path.insert(0, str(ANALYSIS / 'stressbench'))
from common import orbits, majority


def read(name):
    return json.loads((HERE / name).read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name, value, check=False):
    content = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
    path = HERE / name
    if check:
        assert path.read_text() == content, name
    else:
        if path.exists():
            assert path.read_text() == content, f'Refusing to overwrite changed artifact: {name}'
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)


def verify():
    for path in sorted(HERE.glob('*freeze.json')):
        for f, expected in json.loads(path.read_text())['files'].items():
            assert sha(HERE / f) == expected, f'Frozen file changed: {f}'
    for image in read('dictionary-images.json'):
        assert sha(ROOT / image['file']) == image['sha256']
    for caption in read('captions.json')['records']:
        assert sha(HERE / caption['crop']) == caption['crop_sha256']


def normalize(word):
    s = word.get('joined', word['raw']).replace('ſ', 's')
    return ''.join(c.upper() if c in string.ascii_lowercase else c for c in s)


def entry_words(entry, n):
    return sorted({normalize(w) for w in entry['words'] if not w['uncertain']
                   and len(normalize(w)) == n
                   and set(normalize(w)) <= set(string.ascii_uppercase)})


def select(nomination, n, lexicon):
    """Frozen nomination/lookup join; never receive grid letters."""
    entries = {e['id']: e for e in lexicon['entries']}
    lookups = {e['lookup']: e for e in lexicon['lookups']}
    used, blockers, words = [], [], []
    for nom in nomination['nominations']:
        lookup = lookups[nom['lookup']]
        used.append(nom['lookup'])
        if lookup['status'] != 'verified':
            blockers.append([nom['lookup'], lookup['status']])
        else:
            entry = entries[lookup['entry_id']]
            if entry['uncertain'] or any(w['uncertain'] for w in entry['words']):
                blockers.append([nom['lookup'], 'uncertain_entry'])
            else:
                words.extend(entry_words(entry, n))
    status = ('ineligible_size' if n < 3 or n % 2 == 0 else
              'unresolved_lookup' if blockers else
              'ready' if words else 'no_length_matched_word')
    return {'status': status, 'lookups': used, 'blockers': blockers,
            'words': sorted(set(words)) if status == 'ready' else []}


def mask_sets(n):
    interior = {(r, c) for r in range(1, n-1) for c in range(1, n-1)}
    inner_orbits = [list(o) for o in orbits(n, 'd4') if set(o) <= interior]
    assert set(p for o in inner_orbits for p in o) == interior
    return [('all_interior', 'all', sorted(interior))] + [
        ('one_inner_orbit', str(i), o) for i, o in enumerate(inner_orbits)]


def masked(grid, hidden):
    hidden = set(map(tuple, hidden))
    n = len(grid)
    for orbit in orbits(n, 'd4'):
        assert not (set(orbit) & hidden) or set(orbit) <= hidden
    return [[None if (r, c) in hidden else value for c, value in enumerate(row)]
            for r, row in enumerate(grid)]


def orbit_shuffle(grid, seed):
    grid = deepcopy(grid)
    groups = defaultdict(list)
    for orbit in orbits(len(grid), 'transpose'):
        values = {grid[r][c] for r, c in orbit}
        if len(values) != 1:
            return None
        groups[len(orbit)].append((orbit, next(iter(values))))
    rng = random.Random(seed)
    for size in sorted(groups):
        members = groups[size]
        values = [v for _, v in members]
        rng.shuffle(values)
        for (orbit, _), value in zip(members, values):
            for r, c in orbit:
                grid[r][c] = value
    return grid


def prepare(check=False):
    """Data custodian: emit masked packets and store truth in gitignored cache."""
    verify()
    manifest_path = ANALYSIS / 'stressbench/manifest.json'
    manifest = json.loads(manifest_path.read_text())
    corpus_path = HERE.parent.parent / 'sources/mathers-squares.json'
    assert manifest['corpus_sha256'] == sha(corpus_path)
    records = manifest['records']
    byid = {r['id']: r for r in records}
    nominations = {r['caption_id']: r for r in read('nominations.json')['records']}
    lexicon = read('lexicon.json')
    alignment = read('alignment.json')['records']
    ledger = []
    eligible = []
    for row in alignment:
        s = select(nominations[row['caption_id']], row['n'], lexicon) if row['n'] else None
        reasons = []
        if row['target_id'] is None:
            reasons.append('unmatched_caption')
        else:
            if not row['complete']:
                reasons.append('incomplete_target')
            if row['n'] < 3 or row['n'] % 2 == 0:
                reasons.append('ineligible_size')
        ledger.append(dict(row, selection=s, evaluation_exclusions=reasons))
        if not reasons:
            assert row['target_id'] in byid
            eligible.append(row)
    caption_permutations = []
    for i in range(20):
        rng = random.Random(2026091800+i)
        groups = defaultdict(list)
        mapping = {}
        for row in eligible:
            groups[row['n']].append(row)
        for n in sorted(groups):
            group = sorted(groups[n], key=lambda r: r['target_id'])
            assigned = [r['caption_id'] for r in group]
            rng.shuffle(assigned)
            mapping.update({r['target_id']: caption for r, caption in zip(group, assigned)})
        caption_permutations.append({'seed': 2026091800+i, 'mapping': mapping,
            'unchanged': sum(mapping[r['target_id']] == r['caption_id'] for r in eligible)})
    tasks, truth, symmetric_ids = [], {}, []
    for row in eligible:
        record = byid[row['target_id']]
        grid, fold = record['grid'], record['fold']
        training = [c for s in records if s['fold'] != fold for line in s['grid'] for c in line]
        training_mode = majority(training)
        variants = [('original', grid)]
        for i in range(20):
            shuffled = orbit_shuffle(grid, 2026091800+i)
            if shuffled is not None:
                variants.append((f'orbit_shuffle_{i:02d}', shuffled))
        if len(variants) > 1:
            symmetric_ids.append(row['target_id'])
        for variant, target_grid in variants:
            for kind, orbit_id, hidden in mask_sets(row['n']):
                if not hidden:
                    continue
                key = f'{row["target_id"]}:{variant}:{kind}:{orbit_id}'
                tasks.append({'key': key, 'target_id': row['target_id'], 'caption_id': row['caption_id'],
                    'n': row['n'], 'fold': fold, 'variant': variant, 'mask_kind': kind,
                    'exposure': row['exposure_stratum'], 'hidden': hidden,
                    'observed': masked(target_grid, hidden), 'training_mode': training_mode,
                    'control_grid_unchanged': target_grid == grid if variant != 'original' else None})
                truth[key] = [[r, c, target_grid[r][c]] for r, c in hidden]
    payload = {'corpus_sha256': sha(corpus_path), 'manifest_sha256': sha(manifest_path),
               'ledger': ledger, 'caption_permutations': caption_permutations,
               'orbit_control_symmetric_targets': symmetric_ids, 'tasks': tasks}
    save('tasks.json', payload, check)
    answer_path = '../../sources/cache/e2/answers.json'
    save(answer_path, truth, check)
    return payload


def symmetry_predictions(observed, group):
    predictions = []
    for orbit in orbits(len(observed), group):
        known = {observed[r][c] for r, c in orbit if observed[r][c] is not None}
        if len(known) > 1:
            return {'status': 'contradiction', 'predictions': []}
        if known:
            value = next(iter(known))
            predictions.extend([r, c, value] for r, c in orbit if observed[r][c] is None)
    return {'status': 'compatible', 'predictions': sorted(predictions)}


def predict_task(task, nomination, lexicon, permutations):
    """Only masked task data enter this function. No filesystem access."""
    n, observed = task['n'], task['observed']
    chosen = select(nomination, n, lexicon)
    result = {'caption': solve(observed, chosen['words'])}
    result['caption']['selection'] = chosen
    if task['variant'] != 'original':
        return result
    pool = sorted({w for e in lexicon['entries'] for w in entry_words(e, n) if not e['uncertain']})
    result['without_captions'] = solve(observed, pool)
    result['symmetry_T'] = symmetry_predictions(observed, 'transpose')
    result['symmetry_TA'] = symmetry_predictions(observed, 'diagonals')
    mode = task['training_mode']
    result['training_frequency'] = {'status': 'ready' if mode else 'tie_or_empty',
        'predictions': [[r, c, mode] for r, c in task['hidden']] if mode else []}
    position_predictions = []
    center = n // 2
    for r, c in task['hidden']:
        index = c if r == center else r if c == center else None
        value = majority([w[index] for w in pool]) if index is not None else None
        if value:
            position_predictions.append([r, c, value])
    result['dictionary_position_frequency'] = {'status': 'ready', 'predictions': position_predictions}
    for i, perm in enumerate(permutations):
        perm_selection = perm['selection']
        result[f'caption_shuffle_{i:02d}'] = solve(observed, perm_selection['words'])
        result[f'caption_shuffle_{i:02d}']['selection'] = perm_selection
        rng = random.Random(2026091800+i)
        shuffled_words = []
        for word in chosen['words']:
            chars = list(word)
            rng.shuffle(chars)
            shuffled_words.append(''.join(chars))
        result[f'word_shuffle_{i:02d}'] = solve(observed, sorted(set(shuffled_words)))
    return result


def predict(check=False):
    verify()
    tasks = read('tasks.json')
    nominations = {r['caption_id']: r for r in read('nominations.json')['records']}
    lexicon = read('lexicon.json')
    records = []
    for task in tasks['tasks']:
        perms = [{'selection': select(nominations[p['mapping'][task['target_id']]], task['n'], lexicon)}
                 for p in tasks['caption_permutations']]
        methods = predict_task(task, nominations[task['caption_id']], lexicon, perms)
        hidden = set(map(tuple, task['hidden']))
        for result in methods.values():
            assert all((r, c) in hidden for r, c, _ in result['predictions'])
        records.append({'key': task['key'], 'methods': methods})
    payload = {'tasks_sha256': sha(HERE / 'tasks.json'), 'records': records}
    save('predictions.json', payload, check)
    return payload


def score(check=False):
    """Separate scorer. Predictions and their freeze must already exist."""
    verify()
    assert (HERE / 'prediction-freeze.json').exists()
    tasks = read('tasks.json')
    predictions = read('predictions.json')
    truth = read('../../sources/cache/e2/answers.json')
    predicted = {r['key']: r['methods'] for r in predictions['records']}
    totals = defaultdict(Counter)
    records = []
    for task in tasks['tasks']:
        answers = {(r, c): value for r, c, value in truth[task['key']]}
        hidden = set(answers)
        for name, result in predicted[task['key']].items():
            proposed = {(r, c): value for r, c, value in result['predictions']}
            assert len(proposed) == len(result['predictions'])
            assert set(proposed) <= hidden
            correct = sum(answers[p] == value for p, value in proposed.items())
            group_counts = Counter()
            for orbit in orbits(task['n'], 'd4'):
                if not set(orbit) <= hidden:
                    continue
                if not set(orbit) <= set(proposed):
                    group_counts['abstained_groups'] += 1
                elif all(proposed[p] == answers[p] for p in orbit):
                    group_counts['correct_groups'] += 1
                else:
                    group_counts['wrong_groups'] += 1
            row = {'target_id': task['target_id'], 'fold': task['fold'], 'task': task['key'],
                   'variant': task['variant'], 'mask_kind': task['mask_kind'], 'method': name,
                   'exposure': task['exposure'], 'target_cells': len(answers),
                   'predicted': len(proposed), 'correct': correct, 'errors': len(proposed)-correct,
                   'abstentions': len(answers)-len(proposed),
                   'contradictions': int(result['status'] == 'contradiction'),
                   'exact_tasks': int(len(proposed) == len(answers) and correct == len(answers)),
                   **{k: group_counts[k] for k in ['correct_groups','wrong_groups','abstained_groups']},
                   'compatible_branches': len(result.get('branches', [])) if 'branches' in result else None,
                   'completion_count': result.get('completion_count')}
            caption_cells = {(r, c) for r, c, _ in predicted[task['key']]['caption']['predictions']}
            row['caption_subset_cells'] = len(caption_cells)
            row['predicted_on_caption_subset'] = len(caption_cells & set(proposed))
            row['correct_on_caption_subset'] = sum(proposed.get(p) == answers[p] for p in caption_cells)
            records.append(row)
            key = (task['variant'], task['mask_kind'], name)
            totals[key].update({k: row[k] for k in ['target_cells','predicted','correct','errors','abstentions',
                'contradictions','exact_tasks','correct_groups','wrong_groups','abstained_groups',
                'caption_subset_cells','predicted_on_caption_subset','correct_on_caption_subset']})
            totals[key]['tasks'] += 1
    summary = []
    for (variant, kind, method), counts in sorted(totals.items()):
        summary.append({'variant': variant, 'mask_kind': kind, 'method': method, **counts,
            'accuracy': counts['correct']/counts['predicted'] if counts['predicted'] else None,
            'coverage': counts['predicted']/counts['target_cells'] if counts['target_cells'] else None})
    # Matched-original caption counts for orbit-value controls, not all originals.
    matched = [r for r in records if r['variant'] == 'original' and r['method'] == 'caption'
               and r['target_id'] in tasks['orbit_control_symmetric_targets']]
    lookup_counts = Counter(r['status'] for r in read('lexicon.json')['lookups'])
    output = {'interpretation': 'Uninformative selector pilot: no usable caption lexical inputs on complete targets. Neither support nor refutation of broader dictionary derivation.',
        'historical_witness_validation': False, 'captions': len(tasks['ledger']),
        'aligned': sum(r['target_id'] is not None for r in tasks['ledger']),
        'complete_odd_targets': len({t['target_id'] for t in tasks['tasks']}),
        'lookup_status_counts': dict(sorted(lookup_counts.items())),
        'caption_permutations': tasks['caption_permutations'],
        'orbit_control_symmetric_targets': tasks['orbit_control_symmetric_targets'],
        'orbit_control_matched_originals': matched,
        'scores': summary, 'records': records,
        'predictions_sha256': sha(HERE / 'predictions.json')}
    save('results.json', output, check)
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('stage', choices=['prepare','predict','score','check'])
    args = parser.parse_args()
    if args.stage == 'check':
        prepare(True)
        predict(True)
        d = score(True)
    elif args.stage == 'prepare':
        prepare()
        print('Masked tasks prepared; answer packet remains in gitignored cache.')
        sys.exit()
    elif args.stage == 'predict':
        predict()
        print('Predictions written; freeze before scoring.')
        sys.exit()
    else:
        d = score()
    print(json.dumps({k:d[k] for k in ['captions','aligned','complete_odd_targets','lookup_status_counts']},indent=2))
    for r in d['scores']:
        if r['variant'] == 'original' and r['mask_kind'] == 'all_interior' and not 'shuffle' in r['method']:
            print(r['method'], 'correct', r['correct'], 'predicted', r['predicted'], 'of', r['target_cells'], 'accuracy', r['accuracy'])

#!/usr/bin/env python3
"""Infer missing letters from fragments in other seed families, with donor voting."""
from collections import defaultdict
import importlib.util
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'stressbench'))
from common import (aggregate, control, letter_mode, load, mask, provenance,
                    report, rng, score, write_result)
spec = importlib.util.spec_from_file_location('frames',HERE.parent/'02-frame-model/run.py')
frames = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frames)


class Vocabulary:
    def __init__(self, train):
        self.words = defaultdict(lambda: defaultdict(set))
        self.groups = {s['group'] for s in train}
        for s in train:
            grid = s['grid']
            n = len(grid)
            rows = grid + [list(row) for row in zip(*grid)]
            strings = {''.join(row) for row in rows}
            strings |= {w[::-1] for w in list(strings)}
            for w in strings:
                for length in sorted(set([3,4,5,n])):
                    if length > n:
                        continue
                    for start in range(n-length+1):
                        self.words[length][w[start:start+length]].add(s['group'])
        self.cache = {}

    def match(self, window, target):
        key = (tuple(window),target)
        if key in self.cache:
            return self.cache[key]
        known = [(i,x) for i,x in enumerate(window) if x is not None]
        if len(known) < 2:
            return None
        donors = defaultdict(set)
        for word,groups in self.words[len(window)].items():
            if all(word[i] == x for i,x in known):
                for group in groups:
                    donors[group].add(word[target])
        result = None
        if len(donors) >= 3:
            votes = defaultdict(float)
            for choices in donors.values():
                for letter in sorted(choices):
                    votes[letter] += 1/len(choices)
            highest = max(votes.values())
            winners = [x for x,v in votes.items() if abs(v-highest) < 1e-9]
            if len(winners)==1 and highest/len(donors) >= .9-1e-9:
                result = (winners[0],len(known),len(window),len(donors),highest/len(donors))
        self.cache[key] = result
        return result

    def predict(self, grid):
        n = len(grid)
        predictions = {}
        for r in range(n):
            for c in range(n):
                if grid[r][c] is not None:
                    continue
                candidates = []
                for line,pos in [(grid[r],c),([grid[i][c] for i in range(n)],r)]:
                    for length in sorted(set([3,4,5,n])):
                        for start in range(max(0,pos-length+1),min(pos,n-length)+1):
                            found = self.match(line[start:start+length],pos-start)
                            if found:
                                candidates.append(found)
                if candidates:
                    # Count of observations, then context length, then donor support.
                    best_rank = max(x[1:4] for x in candidates)
                    letters = {x[0] for x in candidates if x[1:4] == best_rank}
                    if len(letters)==1:
                        predictions[(r,c)] = next(iter(letters))
        return predictions


def predict_with_frames(vocabulary, observed):
    first = frames.frame_model(observed)[0]
    working = [row[:] for row in observed]
    for (r,c),value in first.items():
        working[r][c] = value
    # One declared pass, not iterative self-confirmation of guessed fragments.
    extra = vocabulary.predict(working)
    return {**first,**extra}, extra


def planted():
    vocabulary = ['ABQCD','EFRGH','IJSKL','MNTOP','QRUVW','WXAYZ']
    records = []
    for i in range(80):
        rand = rng(('planted_fragments',i))
        grid = [[rand.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)]]
        grid += [list(rand.choice(vocabulary)) for _ in range(4)]
        records.append({'id':f'fragment-{i}','group':f'fragment-{i}','fold':i%5,
                        'grid':grid,'masks':{'motif_centers':[(r,2) for r in range(1,5)]}})
    return records


def main():
    original = load()
    audit = []
    for kind in ('original','shuffled','symmetric_original','orbit_shuffled','planted_fragments'):
        records = planted() if kind=='planted_fragments' else control(original,kind)
        for fold in range(5):
            train = [s for s in records if s['fold'] != fold]
            test = [s for s in records if s['fold'] == fold]
            vocabulary = Vocabulary(train)
            assert not (vocabulary.groups & {s['group'] for s in test})
            mode = letter_mode(train)
            for s in test:
                for pattern,hidden in s['masks'].items():
                    observed = mask(s['grid'],hidden)
                    transfer = vocabulary.predict(observed)
                    combined, extra = predict_with_frames(vocabulary,observed)
                    for method,pred in [('fragments',transfer),('frame_then_fragments',combined),('fragments_added_after_frames',extra)]:
                        audit.append({'id':s['id'],'fold':fold,'control':kind,
                                      'mask':pattern,'method':method,
                                      'score':score(s['grid'],hidden,pred,mode),
                                      'predictions':[[r,c,v] for (r,c),v in sorted(pred.items())]})
    summary = aggregate(audit)
    write_result(HERE/'results.json',{'provenance':provenance(),'summary':summary,'records':audit})
    report(HERE/'RESULTS.md','03 — Transfer of fragments between seed families',summary,
           'Five fixed folds. Each donor group has one total vote, divided among its compatible letters. '
           'At least three donor groups, two observed context letters and 90% agreement required. '
           'Added-after-frames rows isolate the incremental predictions; the combined row includes frame predictions too.')
    print('03 completed:',len(audit),'evaluation cases')


if __name__ == '__main__':
    main()

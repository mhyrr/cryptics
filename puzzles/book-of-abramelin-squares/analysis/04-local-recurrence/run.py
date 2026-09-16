#!/usr/bin/env python3
"""Learn nonlinear local transitions with nested, group-held-out evaluation."""
from collections import Counter, defaultdict
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'stressbench'))
from common import (aggregate, control, digest, letter_mode, load, mask,
                    provenance, report, rng, score, write_result)

CONFIGS = [(family,flip_r,flip_c) for family in ('north_plus_f_west','west_plus_f_north','pair_lookup')
           for flip_r in (False,True) for flip_c in (False,True)]


def orient(grid,config):
    _,flip_r,flip_c = config
    out = grid[::-1] if flip_r else grid
    return [row[::-1] if flip_c else row[:] for row in out]


def unorient_position(r,c,n,config):
    return (n-1-r if config[1] else r,n-1-c if config[2] else c)


def encode(north,west,current,family):
    n,w,c = (ord(x)-65 for x in (north,west,current))
    if family=='north_plus_f_west':
        return (w,), (c-n)%26
    if family=='west_plus_f_north':
        return (n,), (c-w)%26
    return (n,w),c


class Rule:
    def __init__(self,train,config):
        self.config = config
        self.groups = {s['group'] for s in train}
        counts = defaultdict(Counter)
        support = defaultdict(lambda:defaultdict(set))
        for s in train:
            grid = orient(s['grid'],config)
            for r in range(1,len(grid)):
                for c in range(1,len(grid)):
                    key,value = encode(grid[r-1][c],grid[r][c-1],grid[r][c],config[0])
                    counts[key][value] += 1
                    support[key][value].add(s['group'])
        self.table = {}
        for key,values in counts.items():
            value = min(values,key=lambda v:(-values[v],v))
            self.table[key] = (value,values[value]/sum(values.values()),len(support[key][value]))

    def step(self,north,west,confident):
        if north is None or west is None:
            return None
        key,_ = encode(north,west,'A',self.config[0])
        fit = self.table.get(key)
        if fit is None or (confident and (fit[1] < .9 or fit[2] < 3)):
            return None
        value = fit[0]
        if self.config[0]=='north_plus_f_west':
            value = (ord(north)-65+value)%26
        elif self.config[0]=='west_plus_f_north':
            value = (ord(west)-65+value)%26
        return chr(65+value)

    def predict(self,observed,confident=False,teacher=None):
        grid = orient(observed,self.config)
        true_grid = orient(teacher,self.config) if teacher is not None else None
        predictions = {}
        n = len(grid)
        for r in range(1,n):
            for c in range(1,n):
                if grid[r][c] is not None:
                    continue
                context = true_grid if true_grid is not None else grid
                value = self.step(context[r-1][c],context[r][c-1],confident)
                if value is not None:
                    predictions[unorient_position(r,c,n,self.config)] = value
                    grid[r][c] = value
        return predictions


def select(train):
    groups = sorted({s['group'] for s in train},key=lambda g:digest(('inner',g)))
    validation_groups = set(groups[:max(1,len(groups)//4)])
    fitting = [s for s in train if s['group'] not in validation_groups]
    validation = [s for s in train if s['group'] in validation_groups]
    results = []
    for config in CONFIGS:
        rule = Rule(fitting,config)
        correct = targets = predictions = 0
        for s in validation:
            grid = orient(s['grid'],config)
            for r in range(1,len(grid)):
                for c in range(1,len(grid)):
                    value = rule.step(grid[r-1][c],grid[r][c-1],False)
                    targets += 1
                    predictions += value is not None
                    correct += value == grid[r][c]
        results.append({'config':config,'correct':correct,'targets':targets,'predicted':predictions})
    # Every config has the same number of validation interior targets.
    best = max(range(len(results)),key=lambda i:results[i]['correct'])
    config = CONFIGS[best]
    return Rule(train,config), {'chosen':config,'inner_groups':sorted(validation_groups),'candidates':results}


def planted():
    function = [rng(('planted_transition',i)).randrange(26) for i in range(26)]
    records = []
    for i in range(80):
        rand = rng(('planted_recurrence',i))
        n = 8
        grid = [[chr(65+rand.randrange(26)) for _ in range(n)] for _ in range(n)]
        for r in range(1,n):
            for c in range(1,n):
                grid[r][c] = chr(65+(ord(grid[r-1][c])-65+function[ord(grid[r][c-1])-65])%26)
        records.append({'id':f'recurrence-{i}','group':f'recurrence-{i}','fold':i%5,
                        'grid':grid,'masks':{'gnomon':[(r,c) for r in range(1,n) for c in range(1,n)]}})
    return records


def main():
    original = load()
    audit,selection = [],[]
    for kind in ('original','shuffled','symmetric_original','orbit_shuffled','planted_recurrence'):
        records = planted() if kind=='planted_recurrence' else control(original,kind)
        for fold in range(5):
            train = [s for s in records if s['fold'] != fold]
            test = [s for s in records if s['fold'] == fold]
            rule,details = select(train)
            assert not (rule.groups & {s['group'] for s in test})
            selection.append({'control':kind,'fold':fold,**details})
            mode = letter_mode(train)
            for s in test:
                n = len(s['grid'])
                # Separate boundary test supplies the corner chosen on training data.
                corner_hidden = [unorient_position(r,c,n,rule.config) for r in range(1,n) for c in range(1,n)]
                masks = dict(s['masks'],selected_corner_boundary=corner_hidden)
                for pattern,hidden in masks.items():
                    observed = mask(s['grid'],hidden)
                    for confident in (False,True):
                        for teacher in (False,True):
                            pred = rule.predict(observed,confident,s['grid'] if teacher else None)
                            method = ('confident' if confident else 'modal')+('_teacher_forced' if teacher else '_rollout')
                            audit.append({'id':s['id'],'fold':fold,'control':kind,'mask':pattern,
                                          'method':method,'config':rule.config,
                                          'score':score(s['grid'],hidden,pred,mode),
                                          'predictions':[[r,c,v] for (r,c),v in sorted(pred.items())]})
    summary = aggregate(audit)
    write_result(HERE/'results.json',{'provenance':provenance(),'selection':selection,
                                    'summary':summary,'records':audit})
    report(HERE/'RESULTS.md','04 — Learned local recurrences',summary,
           'Family and traversal corner chosen using an inner split of training groups. '
           'Teacher-forced predictions use true neighbours and are not generation. '
           'Rollout uses only supplied boundaries, visible cells and its own earlier predictions. '
           'The selected-corner boundary test supplies a different boundary when training chooses a different corner.')
    print('04 completed:',len(audit),'evaluation cases;',len(selection),'nested selections')


if __name__ == '__main__':
    main()

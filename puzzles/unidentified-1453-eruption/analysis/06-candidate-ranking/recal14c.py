"""Recalibrate the extracted 14C lab ages (lab_ages.csv) with IntCal20.

Usage: python3 -I recal14c.py <intcal20.14c> <lab_ages.csv>

For each age: 95.4 % HPD and P(1452.0-1453.5). For each candidate: the combination rule from
README (product of likelihoods for ages marked `combine`; `event` used alone; `minimum` /
`maximum` as one-sided bounds), the Ward & Wilson (1978) T statistic for the combined ages
against chi-square(n-1) at 5 %, and P(eruption in the NHET window 1452.9-1453.5), the tropical
window 1452.0-1453.1, and the uniform-rate baseline (window width / 95.4 % HPD width).
"""
import csv, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pipeline as P

ic = P.IntCal(sys.argv[1])
grid = P.make_grid(1000, 1950)
CHI2_95 = {1: 3.84, 2: 5.99, 3: 7.81, 4: 9.49, 5: 11.07, 6: 12.59, 7: 14.07}

def pin(p, a, b):
    return sum(x for t, x in zip(grid, p) if a <= t < b)

def cum(p, reverse=False):
    out, acc = [], 0.0
    seq = list(reversed(p)) if reverse else p
    for x in seq: acc += x; out.append(acc)
    return list(reversed(out)) if reverse else out

groups = {}
for g in csv.DictReader(open(sys.argv[2], encoding='utf-8')):
    groups.setdefault((g['candidate'], g['enum']), []).append(g)

for (cand, enum), grp in groups.items():
    print(f'\n== {cand} (GVP eruption {enum})')
    for g in grp:
        p = P.pdf_14c(ic, grid, [(float(g['age_bp']), float(g['err']))])
        h = P.hpd(grid, p)
        print(f'   {g["lab_code"]:24} {g["age_bp"]:>4}±{g["err"]:<4} {g["material"][:26]:26} use={g["use"]:8} '
              f'HPD95 ' + ', '.join(f'{a:.0f}-{b:.0f}' for a, b in h) + f'   P(1452.0-1453.5) {pin(p, 1452.0, 1453.5):.4f}')
    comb = [g for g in grp if g['use'] in ('combine', 'event')]
    if not comb: continue
    ages = [(float(g['age_bp']), float(g['err'])) for g in comb]
    if len(ages) > 1:
        w = [1 / e ** 2 for _, e in ages]
        m = sum(a * wi for (a, _), wi in zip(ages, w)) / sum(w)
        T = sum(((a - m) / e) ** 2 for a, e in ages)
        crit = CHI2_95.get(len(ages) - 1, float('nan'))
        print(f'   combined {len(ages)} ages: weighted mean {m:.0f}±{math.sqrt(1 / sum(w)):.0f} BP; '
              f'T = {T:.2f} vs chi2(0.05, {len(ages) - 1}) = {crit:.2f} -> {"consistent" if T < crit else "NOT consistent (combination questionable)"}')
    p = P.pdf_14c(ic, grid, ages)
    for g in grp:
        q = P.pdf_14c(ic, grid, [(float(g['age_bp']), float(g['err']))])
        if g['use'] == 'maximum': p = P.normalise([a * b for a, b in zip(p, cum(q))])
        if g['use'] == 'minimum': p = P.normalise([a * b for a, b in zip(p, cum(q, reverse=True))])
    h = P.hpd(grid, p)
    width = sum(b - a for a, b in h)
    print(f'   used pdf ({",".join(sorted(set(g["use"] for g in grp) - {"listed"}))}): HPD95 ' + ', '.join(f'{a:.0f}-{b:.0f}' for a, b in h)
          + f';  P(NHET window 1452.9-1453.5) {pin(p, 1452.9, 1453.5):.4f};  P(tropical window 1452.0-1453.1) {pin(p, 1452.0, 1453.1):.4f}')
    print(f'   uniform-rate baseline over the HPD: {0.6 / width:.4f} (NHET), {1.1 / width:.4f} (tropical)')
    if any(g['use'] == 'minimum' for g in grp):
        q = P.pdf_14c(ic, grid, ages)
        print(f'   without the minimum-age constraint: HPD95 ' + ', '.join(f'{a:.0f}-{b:.0f}' for a, b in P.hpd(grid, q))
              + f';  P(tropical window) {pin(q, 1452.0, 1453.1):.4f}')

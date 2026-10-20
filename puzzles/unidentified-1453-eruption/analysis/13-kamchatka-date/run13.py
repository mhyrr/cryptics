"""Run the pre-registered date models for 13-kamchatka-date.

Usage: python3 -I run13.py <intcal20.14c> <brackets.csv>
Model: 11's one-event bracket model, reused unchanged (../11-aniakchak-date/bracket_model.py).
"""
import csv, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '11-aniakchak-date'))
import bracket_model as BM  # noqa: E402

m = BM.Model(sys.argv[1])
rows = list(csv.DictReader(open(sys.argv[2], encoding='utf-8')))
for r in rows:
    print(f"  {r['event']:9} {r['age_bp']}±{r['err']:3} {r['position']:6} {r['material'][:60]}")

def d(r, pos=None):
    return (float(r['age_bp']), float(r['err']), pos or r['position'])

k = [r for r in rows if r['event'] == 'KRM-IIKM']
top = [r for r in k if r['age_bp'] == '450'][0]
others = [r for r in k if r is not top]
runs = [
    ('MAIN: 3 soil humic extracts, all below (pre-registered)', [d(r) for r in k]),
    ('S1: soil-top 450 +- 30 as same; older extracts below', [d(top, 'same')] + [d(r) for r in others]),
    ('S2: drop 450 +- 30 (authors flag root contamination)', [d(r) for r in others]),
    ('S3: gap G = 50 for all three', [d(r, 'gap50') for r in k]),
    ('S3: gap G = 200 for all three', [d(r, 'gap200') for r in k]),
]
print('\n== Karymsky, onset of the IIKM (KM3) cycle')
for label, dates in runs:
    s = BM.summary(m, m.posterior(dates), label)
    BM.print_summary(s)
print('\nPost hoc descriptive: P(the 450 +- 30 soil carbon is older than 1454.0), i.e. consistent with a 1453 burial')
p = m.calpdf(450, 30)
grid = m.cal
print(f'  P(t < 1454.0) = {sum(x for t, x in zip(grid, p) if t < 1454.0):.3f};  P(t < 1440.0) = {sum(x for t, x in zip(grid, p) if t < 1440.0):.3f}')
mu, sd = m.ic.at(1453.0)
print(f'  IntCal20 at 1453.0 CE: {mu:.0f} +- {sd:.0f} 14C BP')

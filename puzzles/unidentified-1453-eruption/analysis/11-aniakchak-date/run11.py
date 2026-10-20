"""11-aniakchak-date: date the Half Cone Pink Pumice from its own brackets (pre-registered in README).

Usage: python3 -I run11.py <intcal20.14c> <brackets.csv>

Runs, in order: MAIN (verdict), S1 two proximal ages as `same` (= 06), S2 bulk `above` dates,
S3 drop leave-one-out flags, New Cone alone, S4 joint sequence New Cone <= Half Cone (Bacon 2014 Fig. 5C, pre-registered), and post hoc runs labelled as such:
S5 adding the Ahklun 0.4-ka soil-pit date; S6 gap model; absolute chi-square fit.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bracket_model as BM

m = BM.Model(sys.argv[1])
rows = list(csv.DictReader(open(sys.argv[2], encoding='utf-8')))
D = lambda rs, pos=None: [(float(r['age_bp']), float(r['err']), pos or r['position']) for r in rs]

print('Inputs (brackets.csv):')
for r in rows:
    p1 = m.calpdf(float(r['age_bp']), float(r['err']))
    h = BM.P.hpd(m.cal, p1)
    print(f"  {r['event']:3} {r['lab_code']:24} {r['age_bp']:>4}±{r['err']:<4} {r['position']:6} use={r['use']:7} "
          f"cal HPD95 {BM.fmt_hpd(h)}  [{r['material'][:40]}]")

hc_main = [r for r in rows if r['event'] == 'HC' and r['use'] == 'main']
bulk_above = [r for r in rows if r['event'] == 'HC' and r['use'] == 'S2']

print('\n== MAIN: Half Cone, all admissible brackets (verdict model)')
d = D(hc_main)
n_b = sum(1 for x in d if x[2] == 'below'); n_a = sum(1 for x in d if x[2] == 'above'); n_s = sum(1 for x in d if x[2] == 'same')
print(f'  {len(d)} dates: {n_b} below, {n_a} above, {n_s} same. Prior flat {BM.LO:.0f}-{BM.HI:.0f} CE.')
p_main = m.posterior(d)
s_main = BM.summary(m, p_main, 'MAIN')
BM.print_summary(s_main)
loo = m.loo(d)
flags = [r['lab_code'] for r, v in zip(hc_main, loo) if v < 0.05]
print('  leave-one-out: ' + ', '.join(f"{r['lab_code']}:{v:.2f}" for r, v in zip(hc_main, loo)))
print(f'  flagged (< 0.05): {flags or "none"}')
print(f"  P(T < 1452) = {m.prob(p_main, BM.LO, 1452.0):.3f}; P(T >= 1454) = {m.prob(p_main, 1454.0, BM.HI):.3f}")

print('\n== S1: two proximal wood ages as `same` (Bacon 2014 / 06 treatment; the "two proximal ages only" result)')
s1 = [r for r in hc_main if r['lab_code'] in ('GX-29531', 'B-76809')]
s = BM.summary(m, m.posterior(D(s1, 'same')), 'S1 (GX-29531 + B-76809, same)')
BM.print_summary(s)

print('\n== S2: add bulk/humic dates above the tephra')
if bulk_above:
    s = BM.summary(m, m.posterior(d + D(bulk_above)), 'S2'); BM.print_summary(s)
else:
    print('  no bulk or humic date above the Half Cone tephra was found; S2 = MAIN')

print('\n== S3: drop leave-one-out flags')
print('  no flags; S3 = MAIN' if not flags else '')
if flags:
    s = BM.summary(m, m.posterior(D([r for r in hc_main if r['lab_code'] not in flags])), 'S3'); BM.print_summary(s)

print('\n== Prior-range sensitivity (MAIN dates; upper bound is the 1931 tephra cap vs the pre-registered 1800)')
for hi in (1700.0, 1800.0, 1930.0):
    mm = BM.Model(sys.argv[1], lo=BM.LO, hi=hi)
    s = BM.summary(mm, mm.posterior(d), f'prior {BM.LO:.0f}-{hi:.0f}')
    BM.print_summary(s)

print('\n== New Cone alone (3 Bacon ages as `below`; pre-registered)')
nc = [r for r in rows if r['event'] == 'NC']
p_nc = m.posterior(D(nc))
s_nc = BM.summary(m, p_nc, 'New Cone, below-only')
BM.print_summary(s_nc)
s = BM.summary(m, m.posterior(D(nc, 'same')), 'New Cone, 3 ages as `same` (= 06 combination)')
BM.print_summary(s)

print('\n== S4 (order pre-registered under New Cone): joint sequence, New Cone dates <= T_NC <= T_HC, Half Cone dates <= T_HC')
fh, fn = m.posterior(d), p_nc        # each is a product of below factors (flat prior), normalised
cum_nc, acc = [], 0.0
for x in fn:
    acc += x; cum_nc.append(acc)
p4 = BM.P.normalise([a * b for a, b in zip(fh, cum_nc)])
s4 = BM.summary(m, p4, 'S4 Half Cone marginal'); BM.print_summary(s4)
cum_hc_rev, acc = [], 0.0
for x in reversed(fh):
    acc += x; cum_hc_rev.append(acc)
cum_hc_rev.reverse()
p4n = BM.P.normalise([a * b for a, b in zip(fn, cum_hc_rev)])
BM.print_summary(BM.summary(m, p4n, 'S4 New Cone marginal'))

print('\n== S5 (post hoc): MAIN + Ahklun 0.4-ka soil-pit date (UCIAMS-23856, below; unit not tied to Half Cone)')
q04 = [r for r in rows if r['event'] == 'Q04']
BM.print_summary(BM.summary(m, m.posterior(d + D(q04)), 'S5'))

print(f'\nVERDICT (MAIN, pre-registered rule): {BM.verdict(s_main)}')

print('\n== S6 (POST HOC, added after MAIN was read): gap model. Each below date is T - U(0, G) yr.')
print('   Reason: knowncase.py (a) shows the pre-registered below-only model misses the truth (13/60 coverage).')
WOOD = ('GX-29531', 'B-76809')
print('   The gap applies only to the two wood ages with clear context (wood in soil directly below the Pink')
print('   Pumice, Browne 2022 p. 10). The three older ages (wood with lost data sheet; bulk soil) stay plain `below`.')
for G in (25, 50, 100, 200):
    dg = [(float(r['age_bp']), float(r['err']), f'gap{G}' if r['lab_code'] in WOOD else 'below') for r in hc_main]
    BM.print_summary(BM.summary(m, m.posterior(dg), f'S6 Half Cone, G = {G} yr'))
dg = [(a, e, 'gap50') for a, e, _ in d]
BM.print_summary(BM.summary(m, m.posterior(dg), 'S6x Half Cone, G = 50 yr on all five (shown only to expose the conflict with the older ages)'))

print('\n== Consequence statistic: if T = 1453, every below date must have died before 1454.0')
for r in hc_main + nc:
    p1 = m.calpdf(float(r['age_bp']), float(r['err']))
    F = sum(x for t, x in zip(m.cal, p1) if t < 1454.0)
    print(f"  {r['event']} {r['lab_code']:24} {r['age_bp']}±{r['err']}: P(calendar age < 1454.0) = {F:.3f}")
mu, sg = m.ic.at(1453.0)
print(f'  IntCal20 at 1453.0 CE: {mu:.0f} ± {sg:.0f} 14C BP (a sample that died in 1453 would read about this)')
print('\n   S6 joint with New Cone (post hoc): NC dates T_NC - U(0, G); T_NC <= T_HC')
for G in (50, 100):
    fh = m.posterior([(float(r['age_bp']), float(r['err']), f'gap{G}' if r['lab_code'] in WOOD else 'below') for r in hc_main])
    fn = m.posterior([(a, e, f'gap{G}') for a, e, _ in D(nc)])
    c, acc = [], 0.0
    for x in fn:
        acc += x; c.append(acc)
    BM.print_summary(BM.summary(m, BM.P.normalise([a * b for a, b in zip(fh, c)]), f'S6 joint, Half Cone marginal, G = {G}'))
    BM.print_summary(BM.summary(m, fn, f'S6 New Cone alone, G = {G}'))

print('\n== Absolute fit (POST HOC): chi-square of the two clear-context wood ages against IntCal20,')
print('   if both died g years before an eruption in 1453.0 (df = 2; p from exp(-chi2/2))')
import math
for g in (0, 10, 25, 50, 100):
    mu, sc = m.ic.at(1453.0 - g)
    chi = sum((float(r['age_bp']) - mu) ** 2 / (float(r['err']) ** 2 + sc ** 2) for r in hc_main if r['lab_code'] in WOOD)
    print(f'   g = {g:3d}: curve {mu:.0f}±{sc:.0f} BP; chi2 = {chi:.2f}; p = {math.exp(-chi / 2):.2f}')
w = [(float(r['age_bp']), float(r['err'])) for r in hc_main if r['lab_code'] in WOOD]
wm = sum(a / e ** 2 for a, e in w) / sum(1 / e ** 2 for a, e in w); we = (1 / sum(1 / e ** 2 for a, e in w)) ** 0.5
mu, sc = m.ic.at(1453.0)
print(f'   weighted mean of the two {wm:.0f}±{we:.0f} BP vs curve at 1453.0 {mu:.0f}±{sc:.0f}: offset {(mu - wm) / (we ** 2 + sc ** 2) ** 0.5:.2f} sigma')

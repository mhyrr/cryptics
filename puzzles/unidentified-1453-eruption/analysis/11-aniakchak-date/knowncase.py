"""Known-case tests for the 11 bracket model (pre-registered in README).

Usage: python3 -I knowncase.py <intcal20.14c> <knowncase.csv>

(a) Synthetic: true dates T drawn uniformly in 1350-1750 CE (seed 1453). For each T, brackets are
    made from IntCal20: a date's calendar age is T - U(0, 40) (below) or T + U(0, 40) (above); its
    14C age is the curve mean there + N(0, 40); error 40. Scenarios: 2 below + 2 above; 3 below only.
    Reports coverage of the 95.4% HPD and its mean width.
(b) Real: Loch Portain, North Uist (Dugmore et al. 1995, Radiocarbon 37(2), Fig. 1 p. 380), peat profile
    with a diffuse tephra zone containing Hekla 1510 (eruption began 25 July 1510).
"""
import csv, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bracket_model as BM

m = BM.Model(sys.argv[1])
rng = random.Random(1453)


def synth(T, nb, na):
    out = []
    for k in range(nb + na):
        pos = 'below' if k < nb else 'above'
        t = T - rng.uniform(0, 40) if pos == 'below' else T + rng.uniform(0, 40)
        mu, _ = m.ic.at(t)
        out.append((mu + rng.gauss(0, 40), 40.0, pos))
    return out


print('== (a) synthetic brackets')
for nb, na, n in [(2, 2, 60), (3, 0, 60)]:
    cover, widths, pwin = 0, [], []
    for _ in range(n):
        T = rng.uniform(1350, 1750)
        p = m.posterior(synth(T, nb, na))
        h = m.hpd(p)
        cover += any(a <= T <= b for a, b in h)
        widths.append(sum(b - a for a, b in h))
    print(f'  {nb} below + {na} above, {n} trials: HPD95 covers truth {cover}/{n}; mean HPD width {sum(widths) / n:.0f} yr')

print('\n== (b) Loch Portain, Hekla 1510 (true date 1510.56)')
rows = list(csv.DictReader(open(sys.argv[2], encoding='utf-8')))
for r in rows:
    print(f"  {r['lab_code']:10} {r['age_bp']}±{r['err']}  depth {r['depth_cm']} cm  {r['note']}")
runs = {
    'K1: D below; B and C coincident with the tephra zone (same)': {'GU-3008': 'below', 'GU-3010': 'same', 'GU-3009': 'same'},
    'K2: D and C below; B above (zone order)': {'GU-3008': 'below', 'GU-3009': 'below', 'GU-3010': 'above'},
    'K3: D below only (below-only, like Half Cone)': {'GU-3008': 'below'},
}
for label, spec in runs.items():
    d = [(float(r['age_bp']), float(r['err']), spec[r['lab_code']]) for r in rows if r['lab_code'] in spec]
    p = m.posterior(d)
    s = BM.summary(m, p, label, win=(1510.0, 1511.0))
    h = s['hpd']
    ok = any(a <= 1510.56 <= b for a, b in h)
    print(f"  {label}\n    HPD95 {BM.fmt_hpd(h)} (width {s['W']:.0f}); median {s['median']:.0f}; "
          f"contains 1510.56: {'PASS' if ok else 'FAIL'}")
    lo = m.loo(d)
    print('    leave-one-out P(constraint holds | others): ' +
          ', '.join(f'{lab}:{v:.2f}' for (lab, v) in zip([k for k in spec], lo)))

print('\n== (c) POST HOC (added after the Half Cone MAIN result): below-only data, gap model')
print('  Truth: below dates sit T - U(0, gtrue) before the event. Model: each below date is T - U(0, G).')
for gtrue, G, nb in [(40, 50, 3), (40, 100, 3), (40, 200, 3), (150, 50, 3), (150, 200, 3), (300, 200, 3)]:
    cover, widths, n = 0, [], 60
    for _ in range(n):
        T = rng.uniform(1350, 1750)
        dd = []
        for _k in range(nb):
            t = T - rng.uniform(0, gtrue)
            mu, _ = m.ic.at(t)
            dd.append((mu + rng.gauss(0, 40), 40.0, f'gap{G:.0f}'))
        h = m.hpd(m.posterior(dd))
        cover += any(a <= T <= b for a, b in h)
        widths.append(sum(b - a for a, b in h))
    print(f'  true gap U(0,{gtrue}), model G={G}, {nb} below, {n} trials: HPD95 covers truth {cover}/{n}; mean width {sum(widths) / n:.0f} yr')

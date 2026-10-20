"""Known-case tests for 13-kamchatka-date (pre-registered in README).

Usage: python3 -I knowncase13.py <intcal20.14c> <11 knowncase.csv>

Reuses 11's bracket model (../11-aniakchak-date/bracket_model.py) unchanged.
(a) 11's synthetic tests re-run (2 below + 2 above; 3 below only), seed 1453.
(b) Karymsky-like configuration: ONE soil-top humic date whose calendar age is T - U(0, 100);
    14C = IntCal20 mean + N(0, 30), error 30. Scored as `below` (MAIN) and `same` (S1).
(c) 11's real known case (Loch Portain, Hekla 1510) re-run as a regression check.
"""
import csv, os, random, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '11-aniakchak-date'))
import bracket_model as BM  # noqa: E402  (11's code, credited)

m = BM.Model(sys.argv[1])
rng = random.Random(1453)
N = 60


def cover(h, T):
    return any(a <= T <= b for a, b in h)


print('== (a) 11 synthetic tests, re-run')
for nb, na in [(2, 2), (3, 0)]:
    c, w = 0, []
    for _ in range(N):
        T = rng.uniform(1350, 1750)
        d = []
        for k in range(nb + na):
            pos = 'below' if k < nb else 'above'
            t = T - rng.uniform(0, 40) if pos == 'below' else T + rng.uniform(0, 40)
            d.append((m.ic.at(t)[0] + rng.gauss(0, 40), 40.0, pos))
        h = m.hpd(m.posterior(d))
        c += cover(h, T); w.append(sum(b - a for a, b in h))
    print(f'  {nb} below + {na} above: covers truth {c}/{N} ({"PASS" if c >= 0.9 * N else "FAIL"}); mean width {sum(w) / N:.0f} yr')

print('\n== (b) Karymsky-like: one soil-top date, true offset U(0, 100) yr, err 30')
for scored in ['below', 'same', 'gap50', 'gap200']:
    c, w = 0, []
    r2 = random.Random(1453)
    for _ in range(N):
        T = r2.uniform(1350, 1750)
        t = T - r2.uniform(0, 100)
        d = [(m.ic.at(t)[0] + r2.gauss(0, 30), 30.0, scored)]
        h = m.hpd(m.posterior(d))
        c += cover(h, T); w.append(sum(b - a for a, b in h))
    print(f'  scored as {scored:6}: covers truth {c}/{N} ({"PASS" if c >= 0.9 * N else "FAIL"}); mean width {sum(w) / N:.0f} yr')

print('\n== (c) Loch Portain, Hekla 1510 (11 known case), zone order K2')
rows = list(csv.DictReader(open(sys.argv[2], encoding='utf-8')))
spec = {'GU-3008': 'below', 'GU-3009': 'below', 'GU-3010': 'above'}
d = [(float(r['age_bp']), float(r['err']), spec[r['lab_code']]) for r in rows if r['lab_code'] in spec]
h = m.hpd(m.posterior(d))
print(f'  HPD95 {BM.fmt_hpd(h)}; contains 1510.56: {"PASS" if cover(h, 1510.56) else "FAIL"}')

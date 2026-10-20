"""14-katla-date: apply the pre-registered tests (README) to the Icelandic window rows.

Usage:
  python3 -I katla14.py dates.csv <evolv2k_v4.tab> <abbott_S7_sheet7.tsv> > results/katla14.txt

Inputs are checked in (dates.csv, written by hand from the papers; an LLM read them) or come from
other experiments (eVolv2k v4 from 03, Abbott 2021 Table S7 from 02). This script only computes.
Distance code and the S7 reader follow 09-ice-tracers/particles_s7.py; nothing is imported from it.
"""
import csv, math, statistics, sys

TUNU = (78.04, -33.88)          # Abbott 2021 p. 569
S_1453, S_1453_SD = 9.97, 3.07  # eVolv2k v4
G_1453, A_1453 = 24.8, 5.1      # kg km-2, eVolv2k v4
S_FLOOR = S_1453 - 2 * S_1453_SD  # 3.83 Tg S, the pre-registered size bar
FLOOD_LAVA = {939, 1783}        # Eldgjá and Laki: fissure flood-lava type, not the candidates' type
SYSTEM_OF = {'Katla': 'Katla', 'Hekla': 'Hekla', 'Grímsvötn': 'Grimsvotn', 'Laki': 'Grimsvotn',
             'Veiðivötn': 'Bardarbunga', 'Askja': 'Askja'}
SMALL_KM3 = 0.1                 # IVC 'Small' Katla scenario: tephra < 0.1 km3, column unlikely > 11 km


def gc_km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371.0 * math.asin(math.sqrt(h))


def read_evolv(path):
    rows, body = [], False
    for line in open(path, encoding='utf-8'):
        if line.startswith('*/'):
            body = True
            continue
        if not body or line.startswith('Eruption'):
            continue
        f = line.rstrip('\n').split('\t')
        rows.append(dict(year=int(f[0]), G=float(f[5]), A=float(f[6]), S=float(f[7]), loc=f[10]))
    return rows


def read_s7(path):
    out = {}
    for line in open(path, encoding='utf-8'):
        f = line.rstrip('\n').split('\t')
        try:
            out[round(float(f[1]))] = (float(f[3]), float(f[4]))
        except (ValueError, IndexError):
            pass
    return out


def main(dates_path, evolv_path, s7_path):
    ev = read_evolv(evolv_path)
    ice = [r for r in ev if '(Iceland)' in r['loc'] and 'Unidentifed' not in r['loc']]
    print('== c. Scale: named Icelandic eruptions in eVolv2k v4 (ice-derived, same method as 1453)')
    print(f"{'year':>5} {'source':34} {'G kg/km2':>8} {'A kg/km2':>8} {'S Tg':>6}")
    for r in sorted(ice, key=lambda r: -r['S']):
        print(f"{r['year']:>5} {r['loc']:34} {r['G']:8.1f} {r['A']:8.1f} {r['S']:6.2f}")
    uni = [r for r in ice if r['A'] == 0 and r['G'] > 0]
    ratios = [r['S'] / r['G'] for r in uni]
    k = statistics.median(ratios)
    print(f"\nS/G for unipolar Icelandic rows: median {k:.4f} Tg per kg km-2 (range {min(ratios):.4f}-{max(ratios):.4f}, n={len(uni)})")
    print(f"1453 as a Greenland-only (Icelandic) event: {G_1453} x {k:.4f} = {G_1453 * k:.2f} Tg S "
          f"(eVolv2k bipolar value {S_1453} ± {S_1453_SD}); pre-registered bar {S_FLOOR:.2f} Tg S")
    amax = max(r['A'] for r in ice)
    n_a = sum(1 for r in ice if r['A'] > 0)
    print(f"Icelandic rows with Antarctic deposition > 0: {n_a} of {len(ice)}; max {amax} kg km-2 "
          f"(1453 has {A_1453}). Pattern against: {amax < A_1453}")
    sysmax = {}
    for r in ice:
        name = r['loc'].split(' (')[0].split(',')[0]
        s = SYSTEM_OF.get(name)
        if s and r['year'] not in FLOOD_LAVA:
            sysmax[s] = max(sysmax.get(s, 0), r['S'])
    print('System max S excluding flood-lava fissure events (Eldgjá 939, Laki 1783):',
          ', '.join(f'{s} {v:.2f}' for s, v in sorted(sysmax.items())))
    k1755 = [r for r in ice if r['year'] == 1755][0]
    print(f"Katla 1755 (largest historical Katla tephra, <= 1.5 km3): {k1755['S']:.2f} Tg S; "
          f"1453 Greenland deposition is {G_1453 / k1755['G']:.1f}x Katla 1755's")
    pattern_against = amax < A_1453

    print('\n== d. Distance to TUNU2013 (78.04 N, 33.88 W)')
    rows = list(csv.DictReader(open(dates_path, encoding='utf-8')))
    vref = next(r for r in rows if r['candidate'].startswith('Veiðivötn 1477'))
    dv = gc_km((float(vref['lat']), float(vref['lon'])), TUNU)
    for s in ('Katla', 'Hekla', 'Grimsvotn', 'Bardarbunga'):
        r = next(x for x in rows if x['system'] == s)
        d = gc_km((float(r['lat']), float(r['lon'])), TUNU)
        print(f"  {s:12} {d:6.0f} km  ({d / dv:.2f}x Veiðivötn)")

    s7 = read_s7(s7_path)
    med = statistics.median(v[1] for v in s7.values())
    print(f"\n== d, post hoc. TUNU2013 annual 4.5-9.5 um particles (Abbott 2021 S7), median {med:.4f} ug/g")
    for lab, yrs in (('UE 1453', (1452, 1453, 1454)), ('V1477 (10-11 km3)', (1477, 1478)),
                     ('Katla ~1500 ± 5 (0.5-0.7 km3)', range(1495, 1501)),
                     ('Katla 15th-c layer, IVC 1460-1500', range(1460, 1501))):
        xs = [(y, s7[y][1] / med) for y in yrs if y in s7]
        top = max(xs, key=lambda t: t[1])
        print(f"  {lab:36} max {top[1]:.2f}x median in {top[0]}; years: " +
              ' '.join(f'{y}:{x:.2f}' for y, x in xs))

    smed = statistics.median(v[0] for v in s7.values())
    print(f"  nssS (median {smed:.1f} ng/g) and particles at the largest particle years and 1453:")
    for y in sorted(s7, key=lambda y: -s7[y][1])[:6] + [1453]:
        print(f"    {y}: nssS {s7[y][0]:5.1f} ng/g ({s7[y][0] / smed:.1f}x), particles {s7[y][1] / med:.2f}x")

    print('\n== Verdicts (pre-registered rule)')
    print(f"{'candidate':42} {'basis':28} {'range':>11}  a        b        c        d        verdict")
    for r in rows:
        if '(calibration)' in r['candidate']:
            continue
        lo, hi = r['lo'], r['hi']
        if not lo:
            a, rng = 'neutral', 'none'
        else:
            lo, hi = int(lo), int(hi)
            rng = f'{lo}-{hi}'
            contains = lo <= 1453 and hi >= 1452
            if not contains:
                a = 'fail'
            elif hi - lo <= 30:
                a = 'pass'
            else:
                a = 'neutral'
            if 'unverified' in r['basis']:
                a = f'neutral({a})'  # basis unread: cannot count, report what it would be
        b = 'neutral'  # annals: no 1452-53 record found; the 1431-1472 gap (README b)
        sysok = sysmax.get(r['system'], 0) >= S_FLOOR
        small = r['size_class'] == 'Small'
        c = 'fail' if (not sysok or small) else 'pass'
        if c == 'pass' and pattern_against:
            c = 'weak'
        try:
            vol = float(r['tephra_km3_max'])
        except ValueError:
            vol = None
        d_km = gc_km((float(r['lat']), float(r['lon'])), TUNU)
        d = 'fail' if (d_km <= 1.5 * dv and vol is not None and vol >= 0.5) else 'neutral'
        a0 = a.split('(')[0]
        if a0 == 'fail' or (c == 'fail' and d == 'fail'):
            v = 'refuted'
        elif (c == 'fail') + (d == 'fail') == 1 or (c == 'weak' and d == 'fail'):
            v = 'weakened'
        elif a0 == 'pass' and c == 'pass' and d != 'fail':
            v = 'supported'
        else:
            v = 'open'
        print(f"{r['candidate'][:42]:42} {r['basis'][:28]:28} {rng:>11}  {a:8} {b:8} {c:8} {d:8} {v}")


if __name__ == '__main__':
    main(*sys.argv[1:4])

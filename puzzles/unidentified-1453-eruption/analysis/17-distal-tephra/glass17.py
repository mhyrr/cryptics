"""Screen the 17 hits that have published glass against the reference glass
already in hand. A screen, not a correlation: it says which comparisons are
worth making properly in 07-glass-reference.

Run (from this folder):
    python3 -I glass17.py > results/glass17.txt

Inputs: means typed from the cited tables (sources inline below), plus the
single-shard Tephrabase analyses saved by fetch17.py (Loch Portain B, MOR-T2).

Measure (fixed before running): Borchardt similarity coefficient
SC = mean over oxides of min(a, b) / max(a, b), on analyses normalised to
100% over the oxides used. Two oxide sets:
  SC8: SiO2 TiO2 Al2O3 FeO MgO CaO Na2O K2O
  SC6: SiO2 Al2O3 FeO CaO Na2O K2O (drops the two low-abundance oxides)
Reading rule (fixed before running, the convention in Payne & Blackford 2008
and Riehle 1985): SC >= 0.95 consistent at screening; 0.90-0.95 same family
possible; < 0.90 different.
"""
import html, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OX8 = ['SiO2', 'TiO2', 'Al2O3', 'FeO', 'MgO', 'CaO', 'Na2O', 'K2O']
OX6 = ['SiO2', 'Al2O3', 'FeO', 'CaO', 'Na2O', 'K2O']


def v(*xs):
    return dict(zip(OX8, xs))


# ---------------------------------------------------------------- references in hand
REF = {
    # Kaufman et al. 2012 JQS Table 6 (copy in ../11-aniakchak-date/data/kaufman2012_jqs_ahklun.txt)
    'Aniakchak ref (CFE II) Pop 1 [Kaufman 2012]': v(59.21, 1.35, 16.63, 7.51, 2.76, 6.20, 4.42, 1.59),
    'Aniakchak ref (CFE II) Pop 2 [Kaufman 2012]': v(71.15, 0.49, 15.24, 2.48, 0.51, 1.75, 5.13, 2.95),
    # Mackay et al. 2016 QSR Table 2
    'MSH Wn [Mackay 2016]': v(74.83, 0.19, 14.32, 1.61, 0.30, 1.70, 4.63, 2.32),
    'MSH We [Mackay 2016]': v(75.89, 0.25, 13.51, 1.50, 0.26, 1.44, 4.50, 2.50),
    'MSH layer T [Mackay 2016]': v(70.80, 0.44, 15.69, 2.88, 0.72, 2.89, 4.69, 1.93),
    'Ksudach KS1 [Mackay 2016]': v(73.32, 0.40, 13.97, 2.67, 0.45, 2.22, 5.22, 1.35),
    'Tarumai Ta-c2 [Mackay 2016]': v(76.47, 0.34, 11.94, 2.15, 0.46, 2.27, 3.97, 2.36),
    'WRA east [Mackay 2016]': v(73.89, 0.21, 14.49, 1.52, 0.36, 1.83, 4.13, 3.19),
    'Ceboruco P1 [Mackay 2016]': v(71.44, 0.28, 15.94, 1.96, 0.34, 1.34, 5.13, 3.39),
    # Payne & Blackford 2008 Table 1 comparison data (Begét et al. 1994)
    'Katmai 1912 sk7-3-3p2 [Payne 2008]': v(77.23, 0.32, 12.38, 1.64, 0.27, 1.27, 4.01, 2.87),
    'Augustine 1883 SK11-3-5 [Payne 2008]': v(75.06, 0.32, 13.77, 1.65, 0.40, 1.71, 4.04, 3.04),
    'Crater Peak c.300 BP SK7-3-9 [Payne 2008]': v(59.74, 1.18, 16.24, 7.74, 2.84, 6.27, 4.30, 1.69),
    'Augustine B A88-7-1 [Payne 2008]': v(75.73, 0.39, 13.04, 2.08, 0.49, 2.29, 3.97, 2.01),
}

# ---------------------------------------------------------------- hits with glass
HIT = {
    'AHK04 Ahklun 0.4-ka Pop 1 (andesite) [Kaufman 2012]': v(59.76, 1.28, 16.32, 7.45, 2.62, 6.17, 4.42, 1.66),
    'AHK04 Ahklun 0.4-ka Pop 2 (rhyodacite) [Kaufman 2012]': v(71.08, 0.50, 15.14, 2.53, 0.52, 1.85, 5.08, 2.96),
    'KEN ST24 Sterling c.1480 [Payne 2008]': v(76.89, 0.30, 12.66, 1.48, 0.32, 1.47, 3.84, 3.02),
    'KEN MP39 Moose Pass c.1520 [Payne 2008]': v(60.60, 1.14, 16.05, 7.57, 2.68, 5.95, 4.22, 1.79),
    'NENA SCH10-42 pop 1 (AD 1572-1762) [Mackay 2016]': v(70.12, 0.46, 15.63, 2.89, 0.82, 3.07, 5.07, 1.86),
    'NENA SCH10-42 pop 2 [Mackay 2016]': v(75.89, 0.27, 13.19, 1.44, 0.18, 1.22, 4.20, 3.57),
    'NENA VDB12-42 Villagedale (AD 1517-1750) [Mackay 2016]': v(70.44, 0.48, 15.26, 2.96, 0.80, 3.13, 5.03, 1.83),
    'NENA SCH10-57 (age not in text) [Mackay 2016]': v(70.74, 0.39, 14.94, 2.73, 0.65, 2.75, 4.80, 2.88),
    'NENA VDB12-53 (age not in text, n=2) [Mackay 2016]': v(75.67, 0.38, 12.72, 2.26, 0.33, 2.60, 3.85, 2.12),
    'NENA FBB12-47 (AD 1374-1677, n=2) [Mackay 2016]': v(76.58, 0.21, 12.95, 1.53, 0.25, 1.45, 4.44, 2.55),
}

TB_SHARDS = {
    # Tephrabase single-shard EPMA (Dugmore, Larsen & Newton 1995; Chambers et al. 2004)
    'LPB Loch Portain B, all shards (n=6) [Tephrabase]': 'data/tb_geo97.html',
    'MOR-T2 An Loch Mor, all shards (n=27) [Tephrabase]': 'data/tb_geo3868_MOR-T2.html',
}
TB_ORDER = ['SiO2', 'TiO2', 'Al2O3', 'FeO', 'MnO', 'MgO', 'CaO', 'Na2O', 'K2O', 'Total']


def tb_shards(path):
    t = html.unescape(open(os.path.join(HERE, path), encoding='latin-1').read())
    t = re.sub(r'<[^>]+>', ' ', t)
    out = []
    for m in re.finditer(r'Glass((?:\s+-?\d+\.\d+){10})', t):
        nums = [float(x) for x in m.group(1).split()]
        out.append(dict(zip(TB_ORDER, nums)))
    return out


def norm(d, ox):
    s = sum(d[o] for o in ox)
    return {o: 100 * d[o] / s for o in ox}


def sc(a, b, ox):
    a, b = norm(a, ox), norm(b, ox)
    return sum(min(a[o], b[o]) / max(a[o], b[o]) for o in ox) / len(ox)


def mean(rows, ox):
    return {o: sum(r[o] for r in rows) / len(rows) for o in ox}


def main():
    hits = dict(HIT)
    for name, path in TB_SHARDS.items():
        shards = tb_shards(path)
        hits[name] = mean(shards, OX8)
        print(f'# {name}: {len(shards)} shards parsed from {path}')
        for i, s in enumerate(shards):
            n = norm(s, OX8)
            print('#   shard %d  ' % (i + 1) + ' '.join(f'{o} {n[o]:.2f}' for o in OX8))
        if name.startswith('LPB'):
            # split by normalised FeO (seen in the shard list above, after the first run)
            hi = [s for s in shards if norm(s, OX8)['FeO'] > 2.5]
            lo = [s for s in shards if norm(s, OX8)['FeO'] <= 2.5]
            hits['LPB Loch Portain B, FeO > 2.5 group (n=%d) [Tephrabase]' % len(hi)] = mean(hi, OX8)
            hits['LPB Loch Portain B, FeO <= 2.5 group (n=%d) [Tephrabase]' % len(lo)] = mean(lo, OX8)
    print()
    print('# Half Cone Pink Pumice matrix glass, Browne et al. 2022 p. 40: 68.3-69.8 wt% SiO2 (range only; appendix G not in hand)')
    print('# Each hit: top 4 references by SC6, with SC8.  Reading: >=0.95 consistent; 0.90-0.95 family; <0.90 different.\n')
    for h, hv in hits.items():
        n = norm(hv, OX8)
        print(f'{h}\n   normalised: ' + ' '.join(f'{o} {n[o]:.2f}' for o in OX8))
        pink = 'inside' if 68.3 <= n['SiO2'] <= 69.8 else 'outside'
        print(f'   SiO2 {n["SiO2"]:.2f} is {pink} the Half Cone Pink glass range 68.3-69.8')
        scores = sorted(((sc(hv, rv, OX6), sc(hv, rv, OX8), r) for r, rv in REF.items()), reverse=True)
        for s6, s8, r in scores[:4]:
            tag = 'consistent' if s6 >= 0.95 else 'family' if s6 >= 0.90 else 'different'
            print(f'   SC6 {s6:.3f}  SC8 {s8:.3f}  {tag:10}  {r}')
        print()


if __name__ == '__main__':
    main()

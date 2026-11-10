"""18: is the Ahklun 0.4-ka tephra (Kaufman 2012) Half Cone glass (Browne 2022)?

Run (from this folder):  python3 -I glass18.py > results/glass18.txt
Decision rule: README.md, "Decision rule (frozen 2026-11-10 ...)". Constants
below implement it; do not tune them after looking at results.
"""
import importlib.util, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import load18  # noqa: E402

_spec = importlib.util.spec_from_file_location('glass17', os.path.join(HERE, '..', '17-distal-tephra', 'glass17.py'))
glass17 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(glass17)
sc, norm = glass17.sc, glass17.norm          # unchanged from 17
OX8, OX6 = glass17.OX8, glass17.OX6

# ------------------------------------------------------------- frozen constants
D2_MAX = 20.09            # chi2_8 0.99 quantile, used as a convention
F_CROSS = 0.05            # inter-lab relative allowance (primary)
F_SENS = 0.10             # sensitivity
ABS_FLOOR = 0.05          # wt%, added in quadrature
MATCH_SC, MATCH_FRAC = 0.95, 0.80
NOMATCH_SC, NOMATCH_FRAC = 0.90, 0.20
FISHER_P = 0.01
MIN_HC_SHARDS = 3


# ------------------------------------------------------------- helpers
def n8(s):
    return norm(s['ox'], OX8)


def stats(shards):
    xs = [n8(s) for s in shards]
    mu = {o: sum(x[o] for x in xs) / len(xs) for o in OX8}
    sd = {o: (math.sqrt(sum((x[o] - mu[o]) ** 2 for x in xs) / (len(xs) - 1)) if len(xs) > 1 else 0.0) for o in OX8}
    return mu, sd


class Pop:
    def __init__(self, name, shards, lab):
        assert shards, name
        self.name, self.shards, self.lab = name, shards, lab
        self.mu, self.sd = stats(shards)

    def d2(self, shard, f):
        x = n8(shard)
        return sum((x[o] - self.mu[o]) ** 2 / (self.sd[o] ** 2 + (f * self.mu[o]) ** 2 + ABS_FLOOR ** 2) for o in OX8)


def lab_of(shards):
    labs = {s['lab'] for s in shards}
    return labs.pop() if len(labs) == 1 else 'mixed'


def fval(t, r, f_cross):
    return 0.0 if (t.lab == r.lab and t.lab != 'mixed') else f_cross


def frac(t, r, f_cross):
    f = fval(t, r, f_cross)
    return sum(r.d2(s, f) <= D2_MAX for s in t.shards) / len(t.shards)


def verdict(t, r, f_cross):
    s8 = sc(t.mu, r.mu, OX8)
    s6 = sc(t.mu, r.mu, OX6)
    fr = frac(t, r, f_cross)
    if s8 >= MATCH_SC and fr >= MATCH_FRAC:
        v = 'match'
    elif s8 < NOMATCH_SC or fr < NOMATCH_FRAC:
        v = 'no match'
    else:
        v = 'family only'
    return v, s8, s6, fr


def line(t, r, f_cross=F_CROSS):
    v, s8, s6, fr = verdict(t, r, f_cross)
    f = fval(t, r, f_cross)
    return v, f'  {t.name:>16} (n={len(t.shards):3}) vs {r.name:<14} (n={len(r.shards):3})  f={f:.2f}  SC8 {s8:.3f}  SC6 {s6:.3f}  frac {fr:5.2f}  -> {v}'


def fisher_greater(k1, n1, k2, n2):
    """One-sided Fisher exact p that group 1's rate exceeds group 2's."""
    K, N = k1 + k2, n1 + n2

    def hyp(k):
        return math.comb(K, k) * math.comb(N - K, n1 - k) / math.comb(N, n1)
    return sum(hyp(k) for k in range(k1, min(K, n1) + 1))


def show_mean(p):
    return ' '.join(f'{o} {p.mu[o]:.2f}' for o in OX8)


# ------------------------------------------------------------- data
B = load18.load_browne()
K = load18.load_kaufman()
D = load18.load_davies()


def bsel(*samples):
    return [s for s in B if s['sample'] in samples]


HC_PINK = Pop('HC_PINK', bsel('ANI-02-04', 'ANI-02-06'), 'UAF/UCLA')
HC_PINK_A = Pop('Pink ANI-02-04', bsel('ANI-02-04'), 'UAF/UCLA')
HC_PINK_B = Pop('Pink ANI-02-06', bsel('ANI-02-06'), 'UAF/UCLA')
HC_BROWN_DAC = Pop('HC_BROWN_DAC', bsel('ANI-02-01', 'ANI-02-02a', 'ANI-02-03'), 'UAF/UCLA')
HC_BROWN_AND = Pop('HC_BROWN_AND', bsel('ANI-01-08', 'ANI-01-09'), 'UAF/UCLA')
HC_BAND_A = Pop('Brown ANI-01-08', bsel('ANI-01-08'), 'UAF/UCLA')
HC_BAND_B = Pop('Brown ANI-01-09', bsel('ANI-01-09'), 'UAF/UCLA')
HC_PRE400 = Pop('HC_PRE400', bsel('ANI-06-01'), 'UAF/UCLA')
HC_DISTAL_BROWNE = [s for s in B if s['sample'] in ('ANI-32-01', 'Dumond_BrooksCampAshC-1')]
HC_DISTAL_RIEHLE = [s for s in B if s['lab'].startswith('USGS')]


def kpop(sample, pop, drop=()):
    return [s for s in K if s['sample'] == sample and s['pop'] == pop and s['shard'] not in drop]


CFE2_AND = Pop('CFE2_AND', kpop('UA1602', 1), 'U Alberta (JEOL 8900)')
CFE2_RHY = Pop('CFE2_RHY', kpop('UA1602', 2), 'U Alberta (JEOL 8900)')
d1602 = [s for s in D if s['sample'] == 'UA1602']
CFE2_AND_D = Pop('CFE2_AND Davies', [s for s in d1602 if load18.OX8 and n8(s)['SiO2'] < 65], 'U Alberta (JEOL 8900)')
CFE2_RHY_D = Pop('CFE2_RHY Davies', [s for s in d1602 if n8(s)['SiO2'] >= 65], 'U Alberta (JEOL 8900)')


def dsel(label, pops=None, lo=None, hi=None):
    out = [s for s in D if s['label'] == label and (pops is None or s['pop'] in pops)]
    if lo is not None:
        out = [s for s in out if n8(s)['SiO2'] >= lo]
    if hi is not None:
        out = [s for s in out if n8(s)['SiO2'] < hi]
    return out


UAL = 'U Alberta (JEOL 8900)'
NONANI = [
    Pop('NK1912_RHY', dsel('Novarupta-Katmai 1912', lo=74), UAL),
    Pop('NK1912_DAC', dsel('Novarupta-Katmai 1912', hi=74), UAL),
    Pop('REDOUBT', dsel('Redoubt 1989-90', pops={4}), UAL),
    Pop('HAYES_F2', dsel('Hayes set H - unit F2', pops={23}), UAL),
    Pop('RUPPERT', dsel('Ruppert tephra', pops={14}), UAL),
    Pop('WRA_N', dsel('White River Ash (northern lobe)'), UAL),
    Pop('OPALA', dsel('Opala (1400 cal BP caldera formation)'), UAL),
]
TB = [s for s in K if s['label'] == 'Tephra B' and n8(s)['SiO2'] < 65]
UNNAMED = [
    Pop('TEPHRA_B_AND', TB, UAL),
    Pop('TEPHRA_C', [s for s in K if s['label'] == 'Tephra C'], UAL),
    Pop('LSP_4.7', [s for s in K if s['sample'] == 'UA1965'], UAL),
]

# target: authors' populations, outliers kept for the shard classification
AHK_ALL = [s for s in K if s['sample'] in ('UA1966', 'UA1779', 'UA1974')]
AHK_POP1 = Pop('AHK_POP1', kpop('UA1974', 26, drop=('UA1974-19',)) + kpop('UA1779', 26)
               + kpop('UA1966', 28), UAL)
AHK_POP2 = Pop('AHK_POP2', kpop('UA1779', 27) + kpop('UA1974', 27) + kpop('UA1966', 29), UAL)
AHK_ALLP = Pop('AHK_ALL', AHK_ALL, UAL)

# pre-Half-Cone Ahklun controls (same lab)
TA_SAMPLES = ('UA1780', 'UA1963', 'UA1967', 'UA1968', 'UA1970', 'UA1975', 'UA1976', 'UA1977')
PRE_A = [s for s in K if s['sample'] in TA_SAMPLES and s['label'] != 'Tephra B']
PRE_31 = [s for s in K if s['sample'] in ('UA1964', 'UA1793')]
PRE_58 = [s for s in K if s['sample'] == 'UA1783' and s['label'] != 'Tephra B']

HC_REFS = [HC_PINK, HC_BROWN_DAC, HC_BROWN_AND]
CFE_REFS = [CFE2_AND, CFE2_RHY]


def classify(shard, f_cross):
    """Shards are from a lab; references carry theirs; f applies across labs."""
    def ok(r):
        f = 0.0 if shard['lab'] == r.lab else f_cross
        return r.d2(shard, f) <= D2_MAX
    hc = any(ok(r) for r in HC_REFS)
    cf = any(ok(r) for r in CFE_REFS)
    pre = ok(HC_PRE400)
    cls = 'both' if hc and cf else 'HC-only' if hc else 'CFE2-only' if cf else 'neither'
    return cls, pre


def tally(shards, f_cross):
    t = {'HC-only': 0, 'CFE2-only': 0, 'both': 0, 'neither': 0, 'preHC400': 0}
    for s in shards:
        c, pre = classify(s, f_cross)
        t[c] += 1
        t['preHC400'] += pre
    return t


def main():
    print('# 18 Half Cone vs Ahklun 0.4-ka. Rule frozen in README.md before scoring.')
    print(f'# d2 threshold {D2_MAX}; f cross-lab {F_CROSS} (sensitivity {F_SENS}); abs floor {ABS_FLOOR} wt%')
    print(f'# match: SC8>={MATCH_SC} & frac>={MATCH_FRAC}; no match: SC8<{NOMATCH_SC} or frac<{NOMATCH_FRAC}\n')

    # ---- transcription checks against the authors' own means
    print('## 0. Transcription checks (my normalised means vs the authors\' printed means)')
    for p, ref in ((CFE2_AND, 59.21), (CFE2_RHY, 71.15), (AHK_POP2, 71.08)):
        print(f'  {p.name:10} n={len(p.shards):3}  SiO2 {p.mu["SiO2"]:.2f}  (author {ref})')
    p1a = Pop('x', kpop('UA1974', 26, drop=('UA1974-19',)) + kpop('UA1779', 26), UAL)
    p1b = Pop('x', kpop('UA1966', 28, drop=('UA1974-8',)), UAL)
    print(f'  Cascade pit pop1 n={len(p1a.shards)} SiO2 {p1a.mu["SiO2"]:.2f} (author 60.06, n=16); '
          f'LSP pop1 n={len(p1b.shards)} SiO2 {p1b.mu["SiO2"]:.2f} (author 59.32, n=11)')
    print(f'  AHK_POP1 as used n={len(AHK_POP1.shards)} (authors\' grand mean n=27; includes UA1974-8 "Tephra B?" '
          f'in the LSP block as parsed: {"UA1974-8" in [s["shard"] for s in AHK_POP1.shards]})')
    print(f'  AHK_ALL n={len(AHK_ALL)} shards (all Table S1 rows for UA1966/1779/1974)\n')

    print('## Reference means (normalised, 8 oxides)')
    for p in [HC_PINK, HC_BROWN_DAC, HC_BROWN_AND, HC_PRE400, CFE2_AND, CFE2_RHY, CFE2_AND_D, CFE2_RHY_D,
              AHK_POP1, AHK_POP2] + NONANI + UNNAMED:
        print(f'  {p.name:16} n={len(p.shards):3} {p.lab[:10]:10}  {show_mean(p)}')
    print('  SD of HC_PINK : ' + ' '.join(f'{o} {HC_PINK.sd[o]:.2f}' for o in OX8))
    print('  SD of CFE2_RHY: ' + ' '.join(f'{o} {CFE2_RHY.sd[o]:.2f}' for o in OX8))
    print()

    # ---- inter-lab check
    print('## Inter-lab check: Novarupta 1912 rhyolite, U Alberta (Davies) vs Beget 1994 mean (Payne 2008, in glass17)')
    nk = NONANI[0]
    bg = norm(glass17.REF['Katmai 1912 sk7-3-3p2 [Payne 2008]'], OX8)
    print('  rel. offset (UA - Beget)/Beget: ' + ' '.join(f'{o} {100 * (nk.mu[o] - bg[o]) / bg[o]:+.1f}%' for o in OX8))
    print(f'  SC8 {sc(nk.mu, bg, OX8):.3f}\n')

    for fc in (F_CROSS, F_SENS):
        print(f'================ f cross-lab = {fc:.2f} ================')
        print('## (a) Positive controls')
        res = {}
        for t, r in ((HC_PINK_A, HC_PINK_B), (HC_PINK_B, HC_PINK_A), (HC_BAND_A, HC_BAND_B), (HC_BAND_B, HC_BAND_A),
                     (CFE2_RHY, CFE2_RHY_D), (CFE2_RHY_D, CFE2_RHY), (CFE2_AND, CFE2_AND_D), (CFE2_AND_D, CFE2_AND),
                     (HC_BROWN_DAC, HC_PINK), (HC_PINK, HC_BROWN_DAC)):
            v, s = line(t, r, fc)
            res[(t.name, r.name)] = v
            print(s)
        for nm, sh in (('distal HC, Browne lab (ANI-32-01 + Dumond Ash C)', HC_DISTAL_BROWNE),
                       ('distal HC, Riehle 2000 Ash C (USGS)', HC_DISTAL_RIEHLE)):
            t = tally(sh, fc)
            hit = t['HC-only'] + t['both']
            print(f'  shard rule on {nm}: n={len(sh)}  {t}  -> HC-consistent {hit}/{len(sh)}')
        print('## (c) Discrimination (power)')
        for t, r in ((HC_PINK, CFE2_RHY), (CFE2_RHY, HC_PINK), (HC_BROWN_DAC, CFE2_RHY), (CFE2_RHY, HC_BROWN_DAC),
                     (HC_BROWN_AND, CFE2_AND), (CFE2_AND, HC_BROWN_AND), (HC_PINK, HC_PRE400), (HC_PRE400, HC_PINK),
                     (HC_PINK, NONANI[1]), (NONANI[1], HC_PINK), (HC_BROWN_DAC, NONANI[1])):
            v, s = line(t, r, fc)
            res[(t.name, r.name)] = v
            print(s)
        sil = (res[('Pink ANI-02-04', 'Pink ANI-02-06')] == res[('Pink ANI-02-06', 'Pink ANI-02-04')] == 'match'
               and res[('CFE2_RHY', 'CFE2_RHY Davies')] == 'match' and res[('CFE2_RHY Davies', 'CFE2_RHY')] == 'match'
               and all(res[k] == 'no match' for k in (('HC_PINK', 'CFE2_RHY'), ('CFE2_RHY', 'HC_PINK'),
                                                     ('HC_BROWN_DAC', 'CFE2_RHY'), ('CFE2_RHY', 'HC_BROWN_DAC'))))
        andp = (res[('Brown ANI-01-08', 'Brown ANI-01-09')] == res[('Brown ANI-01-09', 'Brown ANI-01-08')] == 'match'
                and res[('CFE2_AND', 'CFE2_AND Davies')] == 'match' and res[('CFE2_AND Davies', 'CFE2_AND')] == 'match'
                and res[('HC_BROWN_AND', 'CFE2_AND')] == 'no match' and res[('CFE2_AND', 'HC_BROWN_AND')] == 'no match')
        print(f'  POWER silicic end: {"YES" if sil else "NO"};  andesitic end: {"YES" if andp else "NO"};  '
              f'1931 / Vent Mtn / New Cone / Blocky Cone: NO (no reference glass)')

        print('## (b)+(target) AHK populations against every reference')
        tv = {}
        for t in (AHK_POP2, AHK_POP1):
            for r in [HC_PINK, HC_BROWN_DAC, HC_BROWN_AND, HC_PRE400, CFE2_RHY, CFE2_AND] + NONANI + UNNAMED:
                v, s = line(t, r, fc)
                tv[(t.name, r.name)] = v
                if v != 'no match' or r in (HC_PINK, HC_BROWN_DAC, HC_BROWN_AND, HC_PRE400, CFE2_RHY, CFE2_AND):
                    print(s)
            print(f'  ({t.name}: references not printed returned "no match")')

        print('## Shard classification and false-positive base rate')
        rows = [('AHK04 all 0.4-ka shards', AHK_ALL), ('  UA1966 Lone Spruce Pond', [s for s in AHK_ALL if s['sample'] == 'UA1966']),
                ('  UA1779+1974 Cascade pit', [s for s in AHK_ALL if s['sample'] != 'UA1966']),
                ('pre-HC Tephra A (CFE II)', PRE_A), ('pre-HC 3.1-ka', PRE_31), ('pre-HC 5.8-ka', PRE_58)]
        tal = {}
        for nm, sh in rows:
            t = tally(sh, fc)
            tal[nm] = (t, len(sh))
            print(f'  {nm:28} n={len(sh):4}  HC-only {t["HC-only"]:3}  both {t["both"]:3}  CFE2-only {t["CFE2-only"]:4}  '
                  f'neither {t["neither"]:3}   (consistent w/ HC_PRE400: {t["preHC400"]})')
        k1, n1 = tal['AHK04 all 0.4-ka shards'][0]['HC-only'], tal['AHK04 all 0.4-ka shards'][1]
        k2 = sum(tal[n][0]['HC-only'] for n in ('pre-HC Tephra A (CFE II)', 'pre-HC 3.1-ka', 'pre-HC 5.8-ka'))
        n2 = sum(tal[n][1] for n in ('pre-HC Tephra A (CFE II)', 'pre-HC 3.1-ka', 'pre-HC 5.8-ka'))
        p = fisher_greater(k1, n1, k2, n2)
        det = k1 >= MIN_HC_SHARDS and p < FISHER_P
        print(f'  HC-only: AHK04 {k1}/{n1} ({100 * k1 / n1:.1f}%) vs pre-HC pooled {k2}/{n2} ({100 * k2 / n2:.1f}%); '
              f'one-sided Fisher p = {p:.2e} -> minor HC-like component {"DETECTED" if det else "not detected beyond background"}')
        print('  AHK04 shards classed HC-only or both, or HC_PRE400-consistent (normalised):')
        for s in AHK_ALL:
            c, pre = classify(s, fc)
            if c in ('HC-only', 'both') or pre:
                x = n8(s)
                dd = {r.name: r.d2(s, fc) for r in HC_REFS + [HC_PRE400]}
                dd.update({r.name: r.d2(s, 0.0) for r in CFE_REFS})
                best = min(dd, key=dd.get)
                print(f'    {s["shard"]:12} {c:9} preHC400={pre!s:5} ' + ' '.join(f'{x[o]:.2f}' for o in OX8)
                      + f'   nearest {best} d2={dd[best]:.1f}; d2 Pink {dd["HC_PINK"]:.1f}, CFE2_RHY {dd["CFE2_RHY"]:.1f}, '
                        f'pre400 {dd["HC_PRE400"]:.1f}  [{s["desc"][:30]}]')

        print('## Target verdict (pre-registered wording)')
        p2 = AHK_POP2.name
        hc_match = any(tv[(p2, r)] == 'match' for r in ('HC_PINK', 'HC_BROWN_DAC'))
        cfe_match = tv[(p2, 'CFE2_RHY')] == 'match'
        hc_none = all(tv[(p2, r)] == 'no match' for r in ('HC_PINK', 'HC_BROWN_DAC'))
        if not sil:
            vv = 'NO POWER at the silicic end: rule cannot separate Half Cone from CFE II; stop.'
        elif hc_match and not cfe_match:
            vv = 'AHK04 is Half Cone (silicic mode).'
        elif cfe_match and hc_none:
            vv = 'AHK04 is CFE II-composition glass, not Half Cone (silicic mode).'
        else:
            vv = 'unresolved.'
        print(f'  {vv}')
        print(f'  andesitic end: {"has power" if andp else "no power"}; AHK_POP1 vs HC_BROWN_AND {tv[("AHK_POP1", "HC_BROWN_AND")]}, '
              f'vs CFE2_AND {tv[("AHK_POP1", "CFE2_AND")]}')
        print(f'  minor component: {"HC-like post-caldera glass detected (not attributable to Half Cone vs 1931/Vent Mtn/New Cone)" if det else "none beyond background"}')
        print()

    posthoc()


def posthoc():
    """Written AFTER the frozen run above. Not part of the decision rule; it
    only explains why the rule returned what it did."""
    print('================ POST-HOC DIAGNOSTICS (written after the run; not binding) ================')
    print('## Why Pink 02-06 vs Pink 02-04 failed: per-oxide mean difference vs 02-04 SD')
    a, b = HC_PINK_A, HC_PINK_B
    print('  ' + ' '.join(f'{o}: d={b.mu[o] - a.mu[o]:+.2f} sd04={a.sd[o]:.2f} sd06={b.sd[o]:.2f};' for o in OX8))
    print('  d2 of 02-06 shards against 02-04 (f=0): ' + ' '.join(f'{a.d2(s, 0.0):.0f}' for s in b.shards))
    print('## Silicic-only views (SiO2 >= 65), f = 0.05')
    for nm, sh in (('distal HC, Browne lab', HC_DISTAL_BROWNE), ('distal HC, Riehle', HC_DISTAL_RIEHLE)):
        rows = [s for s in sh if n8(s)['SiO2'] >= 65]
        for s in rows:
            c, pre = classify(s, F_CROSS)
            x = n8(s)
            print(f'  {nm:22} {s["sample"][:14]:14} {c:9} pre400={pre!s:5} SiO2 {x["SiO2"]:.2f} FeO {x["FeO"]:.2f} '
                  f'CaO {x["CaO"]:.2f} TiO2 {x["TiO2"]:.2f}  d2 Pink {HC_PINK.d2(s, 0 if s["lab"] == HC_PINK.lab else F_CROSS):.1f} '
                  f'CFE2_RHY {CFE2_RHY.d2(s, F_CROSS):.1f} pre400 {HC_PRE400.d2(s, 0 if s["lab"] == HC_PRE400.lab else F_CROSS):.1f}')
    for nm, sh in (('AHK04', AHK_ALL), ('pre-HC Tephra A', PRE_A), ('pre-HC 3.1-ka', PRE_31), ('pre-HC 5.8-ka', PRE_58)):
        sil = [s for s in sh if n8(s)['SiO2'] >= 65]
        t = tally(sil, F_CROSS)
        print(f'  {nm:16} silicic n={len(sil):4}  HC-only {t["HC-only"]:2}  both {t["both"]:2}  CFE2-only {t["CFE2-only"]:4}  '
              f'neither {t["neither"]:2}  pre400-consistent {t["preHC400"]}')
    k1 = tally([s for s in AHK_ALL if n8(s)['SiO2'] >= 65], F_CROSS)
    n1 = len([s for s in AHK_ALL if n8(s)['SiO2'] >= 65])
    pre = [s for s in PRE_A + PRE_31 + PRE_58 if n8(s)['SiO2'] >= 65]
    k2 = tally(pre, F_CROSS)
    for key in ('HC-only', 'preHC400'):
        p = fisher_greater(k1[key], n1, k2[key], len(pre))
        print(f'  silicic {key}: AHK04 {k1[key]}/{n1} vs pre-HC {k2[key]}/{len(pre)}  one-sided Fisher p = {p:.2e}')
    # split by site
    for site, smp in (('LSP UA1966', ('UA1966',)), ('Cascade pit UA1779/1974', ('UA1779', 'UA1974'))):
        sil = [s for s in AHK_ALL if s['sample'] in smp and n8(s)['SiO2'] >= 65]
        t = tally(sil, F_CROSS)
        print(f'  {site:24} silicic n={len(sil)}  HC-only {t["HC-only"]}  pre400-consistent {t["preHC400"]}')


if __name__ == '__main__':
    main()

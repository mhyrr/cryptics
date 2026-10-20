"""Print the size mapping P(VSSI in [obs/2, 2 obs] | VEI, class) used by the scorer.

Usage: python3 -I size_map.py <gvp_eruptions.csv> <gvp_volcanoes.csv> <evolv2k_v4.tab>
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pipeline as P

rows = P.load_gvp(sys.argv[1], sys.argv[2])
att = P.attribute(P.load_evolv2k(sys.argv[3]), rows)
sm = P.SizeModel(rows, att)
lo, hi = P.SIZE_PERIOD
print(f'eVolv2k v4 named events joined to GVP: {len(att)}')
print('year  eVolv2k location                     GVP row                     VEI  class        VSSI   band')
for a in sorted(att, key=lambda a: a['year']):
    g = a['gvp']
    gs = f'{g["name"][:14]} {g["year"]} ({g["method"][:12]})' if g else 'no GVP row within 2 yr'
    print(f'{a["year"]:>5} {a["loc"][:36]:36} {gs:27} {str(a["vei"]):>4}  {a["sclass"]:11} {a["vssi"]:6.2f}  {a["band"]}')
print(f'\nDenominator: GVP confirmed eruptions with VEI, start {lo}-{hi - 1}, by (VEI, class)')
for k in sorted(sm.den): print(f'   VEI {k[0]} {k[1]:11} n = {sm.den[k]}')
print(f'\nP(VEI | VEI unknown): known-VEI GVP eruptions 1000-1899 dated by 14C or tephrochronology')
print('   ' + '  '.join(f'VEI {v}: {w:.3f}' for v, w in sm.vei_unknown.items()))
obs, sig = 9.97, 3.07
thr = obs - sig
print(f'\nSize likelihood for UE 1453 (eVolv2k v4 9.97 +- 3.07 Tg S).')
print(f'   headline: P(VSSI >= {thr:.2f} | VEI, class) (one-sided, obs - 1 sigma)')
print(f'   sensitivity: P({obs / P.SIZE_FACTOR:.2f} <= VSSI <= {obs * P.SIZE_FACTOR:.2f}) (two-sided, factor {P.SIZE_FACTOR:g})')
print(f'   cells with fewer than {P.SIZE_MIN_N} GVP eruptions pool both classes')
print('   VEI    rift-basalt (1s / 2s)     other (1s / 2s)')
for v in [None, 0, 1, 2, 3, 4, 5, 6, 7]:
    cells = '   '.join(f'{sm.p(v, c, thr):.4f} / {sm.p(v, c, obs / P.SIZE_FACTOR, obs * P.SIZE_FACTOR):.4f}' for c in ['rift-basalt', 'other'])
    print(f'   {str(v) if v is not None else "?":>3}    {cells}')
for c in ['rift-basalt', 'other']:
    for v in range(8):
        k = [a for a in att if a['vei'] is not None and min(a['vei'], 7) == v and a['sclass'] == c and lo <= a['year'] < hi and a['vssi'] >= thr]
        if k: print(f'   numerator VEI {v} {c}: ' + ', '.join(f'{a["key"]} {a["year"]} ({a["vssi"]:.1f})' for a in k))

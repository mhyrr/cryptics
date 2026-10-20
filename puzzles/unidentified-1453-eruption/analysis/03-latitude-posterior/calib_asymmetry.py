"""Calibrate hemispheric asymmetry (ASY = DG/(DG+DA)) as a latitude-band predictor.

Usage: python3 -I calib_asymmetry.py <evolv2k_v4.tab> <gvp_holocene_eruptions.csv> <out_likelihood.json>

Calibration set: eVolv2k v4 rows with a named source volcano. Latitude comes from
GVP (joined by volcano number below), not from eVolv2k. Rows dropped for leakage
are counted and listed. Prints a report to stdout; writes 1453 likelihoods to JSON.
"""
import csv, json, math, re, sys

EV, GVP, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
ASY_1453 = 0.829

# eVolv2k location prefix -> GVP volcano number. Hand-mapped 2026-10-20 from the
# GVP volcano names; comments give the GVP name where it differs.
GVP_NUM = {
    'Okataina-Tarawera': '241050', 'Krakatao': '262000', 'Askja': '373060',
    'Grímsvötn': '373010', 'Makian': '268070',  # GVP "Kie Besi"
    'Hokkaido-Komagatake': '285020', 'Toya': '285030', 'Cosigüina': '344010',
    'Zavaritskii-Simushir': '290180',  # GVP "Zavaritzki Caldera" (Kurils), not Kamchatka "Zavaritsky"
    'Galunggung': '263140', 'Tambora': '264040', 'Laki': '373010',  # Laki is in the Grimsvotn system
    'Hekla': '372070', 'Katla': '372030', 'Shikotsu': '285040',
    'Tarumae': '285040',  # GVP: Shikotsu, area Tarumai
    'Fujisan': '283030', 'Gamkonora': '268040',
    'Mount Parker': '271011',  # GVP "Melebingoy"
    'Huaynaputina': '354030', 'Nevado del Ruiz': '351020', 'Colima': '341040',
    'Veiðivötn': '373030',  # GVP: Bardarbunga, area Veidivotn
    'Kuwae': '257070', 'Samalas': '264030',  # GVP: Rinjani, area Samalas
    'Changbaishan': '305060', 'Churchill': '315030', 'Shiveluch': '300270',
    'Ilopango': '343060', 'Taup': '241070', 'Okmok': '311290',
}
CONTESTED = {'Kuwae'}  # 1458 source disputed (Hartman 2019 vs EGU25-2329); see README

def band3(lat):
    return 'NHET' if lat > 30 else ('SHET' if lat < -30 else 'TROP')

def band4(lat):
    if lat > 30: return 'NHET'
    if lat < -30: return 'SHET'
    return 'NTROP' if lat >= 0 else 'STROP'

# ---- load
gv = {}
for r in csv.DictReader(open(GVP, encoding='utf-8')):
    m = re.match(r'POINT \(([-\d.]+) ([-\d.]+)\)', r['GeoLocation'])
    if m: gv.setdefault(r['Volcano_Number'], (r['Volcano_Name'], float(m.group(1))))
lines = open(EV, encoding='utf-8').read().split('\n')
start = next(i for i, l in enumerate(lines) if l.startswith('*/')) + 2
ev = []
for l in lines[start:]:
    if not l.strip(): continue
    f = l.split('\t')
    ev.append(dict(year=int(f[0]), month=int(f[2]), lat=float(f[4]), dg=float(f[5]), da=float(f[6]),
                   vssi=float(f[7]), asy=float(f[9]), loc=f[10], teph=f[11]))
print(f'eVolv2k v4 rows: {len(ev)}')

cal, dropped = [], []
for e in ev:
    if e['loc'] == 'N/A':
        dropped.append((e, 'default latitude (no source; lat set from ice asymmetry)')); continue
    if e['loc'].startswith('Unidentifed'):
        dropped.append((e, 'no named volcano')); continue
    key = next((k for k in GVP_NUM if e['loc'].startswith(k)), None)
    if key is None: sys.exit('unmapped: ' + e['loc'])
    if key in CONTESTED:
        dropped.append((e, 'attribution contested')); continue
    name, glat = gv[GVP_NUM[key]]
    e.update(gvp=name, glat=glat, b3=band3(glat), b4=band4(glat),
             basis='glass' if e['teph'] == 'Y' else 'documentary')
    cal.append(e)

from collections import Counter
print(f'dropped: {len(dropped)}  ', dict(Counter(why for _, why in dropped)))
for e, why in dropped:
    if why != 'default latitude (no source; lat set from ice asymmetry)':
        print(f'   {e["year"]:>5} {e["loc"][:40]:40} ASY {e["asy"]:.3f}  -- {why}')
print(f'calibration set: {len(cal)}  bands {dict(Counter(e["b3"] for e in cal))}  basis {dict(Counter(e["basis"] for e in cal))}')
print()
print('year  eVolv2k location                         GVP name             GVPlat  evlat  band  basis        DG     DA   VSSI   ASY')
for e in sorted(cal, key=lambda e: (e['b3'], -e['asy'])):
    flag = ' *' if abs(e['glat'] - e['lat']) > 1.0 else ''
    print(f'{e["year"]:>5} {e["loc"][:40]:40} {e["gvp"][:20]:20} {e["glat"]:6.1f} {e["lat"]:6.1f}  {e["b3"]:5} {e["basis"]:11} {e["dg"]:6.1f} {e["da"]:6.1f} {e["vssi"]:6.2f} {e["asy"]:.3f}{flag}')
print('(* = GVP and eVolv2k latitude differ by > 1 degree)')

# ---- threshold classifier: ASY < t1 -> SHET, t1 <= ASY < t2 -> TROP, ASY >= t2 -> NHET
def fit(train):
    vals = sorted(set(e['asy'] for e in train))
    cuts = [vals[0] - 0.01] + [(a + b) / 2 for a, b in zip(vals, vals[1:])] + [vals[-1] + 0.01]
    best = None
    for i, t1 in enumerate(cuts):
        for t2 in cuts[i:]:
            acc = sum(predict(e['asy'], t1, t2) == e['b3'] for e in train)
            if best is None or acc > best[0]: best = (acc, t1, t2)
    return best[1], best[2]

def predict(a, t1, t2):
    return 'SHET' if a < t1 else ('TROP' if a < t2 else 'NHET')

def loo_report(sub, label):
    B = ['NHET', 'TROP', 'SHET']
    conf = {(t, p): 0 for t in B for p in B}
    for i, e in enumerate(sub):
        t1, t2 = fit(sub[:i] + sub[i + 1:])
        conf[(e['b3'], predict(e['asy'], t1, t2))] += 1
    n = len(sub); acc = sum(conf[(b, b)] for b in B)
    t1, t2 = fit(sub)
    print(f'\n== LOO threshold classifier: {label} (n={n})')
    print(f'   full-data thresholds: SHET < {t1:.3f} <= TROP < {t2:.3f} <= NHET ; 1453 ASY {ASY_1453} -> {predict(ASY_1453, t1, t2)}')
    print('   true \\ pred   NHET  TROP  SHET')
    for t in B: print(f'   {t:12} {conf[(t,"NHET")]:5} {conf[(t,"TROP")]:5} {conf[(t,"SHET")]:5}')
    print(f'   LOO accuracy {acc}/{n} = {acc/n:.2f}; majority-class baseline {max(Counter(e["b3"] for e in sub).values())}/{n}')

loo_report(cal, 'all named')
loo_report([e for e in cal if e['basis'] == 'glass'], 'glass-attributed only')
loo_report([e for e in cal if e['vssi'] >= 4], 'VSSI >= 4 Tg S')
loo_report([e for e in cal if 0 < e['asy'] < 1], 'bipolar only, 0 < ASY < 1')

# ---- where 1453 falls: neighbours and window likelihoods
print('\n== Events with 0.70 <= ASY < 1.0 (bipolar but Greenland-heavy), by band')
for e in sorted(cal, key=lambda e: e['asy']):
    if 0.70 <= e['asy'] < 1.0:
        print(f'   {e["year"]:>5} {e["gvp"][:22]:22} lat {e["glat"]:6.1f} {e["b4"]:5} VSSI {e["vssi"]:6.2f} ASY {e["asy"]:.3f}')

def window_lik(sub, lo, hi, bands, bandkey):
    """Jeffreys-smoothed P(lo <= ASY < hi | band). SHET pool adds NHET events mirrored (ASY -> 1-ASY)."""
    out = {}
    for b in bands:
        members = [e['asy'] for e in sub if e[bandkey] == b]
        if b == 'SHET':
            members = members + [1 - e['asy'] for e in sub if e[bandkey] == 'NHET']
        k = sum(lo <= a < hi for a in members); n = len(members)
        out[b] = dict(k=k, n=n, L=(k + 0.5) / (n + 1))
    return out

def kde_lik(sub, h, bands, bandkey):
    out = {}
    for b in bands:
        members = [e['asy'] for e in sub if e[bandkey] == b]
        if b == 'SHET':
            members = members + [1 - e['asy'] for e in sub if e[bandkey] == 'NHET']
        dens = sum(math.exp(-0.5 * ((ASY_1453 - a) / h) ** 2) / (h * math.sqrt(2 * math.pi)) for a in members) / len(members)
        out[b] = dict(n=len(members), L=dens)
    return out

B4 = ['NHET', 'NTROP', 'STROP', 'SHET']
variants = {}
for setname, sub in [('all', cal), ('vssi>=4', [e for e in cal if e['vssi'] >= 4]), ('glass', [e for e in cal if e['basis'] == 'glass'])]:
    for lo, hi in [(0.75, 1.0), (0.78, 0.88), (0.70, 0.95)]:
        variants[f'{setname} window[{lo},{hi})'] = window_lik(sub, lo, hi, B4, 'b4')
    if setname != 'glass':  # glass set has one event per tropical band: KDE degenerate
        variants[f'{setname} kde h=0.05'] = kde_lik(sub, 0.05, B4, 'b4')

print('\n== Likelihood of ASY ~ 0.829 by band (SHET pool includes mirrored NHET; see README)')
print('   variant                         ' + ''.join(f'{b:>16}' for b in B4) + '   LR NHET/NTROP')
for name, v in variants.items():
    cells = ''.join((f'{v[b]["k"]}/{v[b]["n"]} {v[b]["L"]:.3f}' if 'k' in v[b] else f'n{v[b]["n"]} {v[b]["L"]:.3f}').rjust(16) for b in B4)
    lr = v['NHET']['L'] / v['NTROP']['L'] if v['NTROP']['L'] > 0 else float('inf')
    print(f'   {name:31} {cells}   {lr:6.2f}')

json.dump({k: {b: v[b]['L'] for b in B4} for k, v in variants.items()}, open(OUT, 'w'), indent=1)

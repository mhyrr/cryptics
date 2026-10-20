"""Posterior on UE 1453 source-latitude band from calibrated likelihoods.

Usage: python3 -I combine.py <lik_asymmetry.json> <lik_isotope.json> <lik_emulator.json> <gvp_holocene_eruptions.csv>

Bands: NHET (> 30 N), NTROP (0-30 N), STROP (0-30 S), SHET (> 30 S).
The asymmetry likelihood and the emulator likelihood both use the same two deposition
numbers, so they are never multiplied together. Each is combined with the isotope
likelihood, which uses different data (TUNU2013 sulfur isotopes, Burke 2023).
"""
import csv, json, re, sys

LA, LI, LE = (json.load(open(p)) for p in sys.argv[1:4])
GVP = sys.argv[4]
B = ['NHET', 'NTROP', 'STROP', 'SHET']

def band(l):
    return 'NHET' if l > 30 else ('SHET' if l < -30 else ('NTROP' if l >= 0 else 'STROP'))

def gvp_prior(vmin, ymin):
    c = dict.fromkeys(B, 0)
    for r in csv.DictReader(open(GVP, encoding='utf-8')):
        v, y = r['ExplosivityIndexMax'], r['StartDateYear']
        if not v or not y or int(v) < vmin or int(y) < ymin or r['Activity_Type'] != 'Confirmed Eruption': continue
        m = re.match(r'POINT \(([-\d.]+) ', r['GeoLocation'])
        if m: c[band(float(m.group(1)))] += 1
    n = sum(c.values())
    return {b: c[b] / n for b in B}, n, c

priors = {}
priors['uniform (= equal surface area)'] = dict.fromkeys(B, 0.25)
for vmin, ymin in [(5, -10000), (5, 1), (6, -10000)]:
    p, n, c = gvp_prior(vmin, ymin)
    priors[f'GVP VEI>={vmin}, year>={ymin} (n={n})'] = p
priors['eVolv2k v4 class shares 49/28/23 (ice-derived)'] = {'NHET': .49, 'NTROP': .14, 'STROP': .14, 'SHET': .23}
priors['tropics-heavy adversarial 10/40/40/10'] = {'NHET': .1, 'NTROP': .4, 'STROP': .4, 'SHET': .1}

EMU = 'SO2 free (10-100 Tg); obs sigma 26%/12%'
liks = {
    'A1 asym window[0.75,1) all x iso': (LA['all window[0.75,1.0)'], LI['all']),
    'A2 asym window[0.75,1) VSSI>=4 x iso': (LA['vssi>=4 window[0.75,1.0)'], LI['all']),
    'A3 asym KDE all x iso': (LA['all kde h=0.05'], LI['all']),
    'A4 asym KDE VSSI>=4 x iso': (LA['vssi>=4 kde h=0.05'], LI['all']),
    'A6 asym window[0.70,0.95) all x iso': (LA['all window[0.7,0.95)'], LI['all']),
    'A5 asym window all x iso out-of-sample': (LA['all window[0.75,1.0)'], LI['out-of-sample only']),
    'E1 emulator Jan/Jul 50:50 x iso': (LE[f'{EMU}; mix'], LI['all']),
    'E2 emulator Jan x iso': (LE[f'{EMU}; jan'], LI['all']),
    'E3 emulator Jul x iso': (LE[f'{EMU}; jul'], LI['all']),
    'E4 emulator 50:50, obs 50% x iso': (LE['SO2 free (10-100 Tg); obs sigma 50%/50%; mix'], LI['all']),
    'X1 asym window all, no isotope': (LA['all window[0.75,1.0)'], dict.fromkeys(B, 1.0)),
    'X2 emulator 50:50, no isotope': (LE[f'{EMU}; mix'], dict.fromkeys(B, 1.0)),
    'X3 isotope only': (dict.fromkeys(B, 1.0), LI['all']),
}

print('Priors')
for k, p in priors.items():
    print(f'   {k:48} ' + '  '.join(f'{b} {p[b]:.2f}' for b in B))
print('\nNormalised likelihoods (for reading only; the posterior uses the raw products)')
for k, (a, i) in liks.items():
    raw = {b: a[b] * i[b] for b in B}; t = sum(raw.values())
    print(f'   {k:42} ' + '  '.join(f'{b} {raw[b]/t:.2f}' for b in B))

print('\nPosterior P(band | data)   [columns: NHET / NTROP / STROP / SHET ; then P(NHET)/P(NTROP)]')
summary = {}
for lk, (a, i) in liks.items():
    print(f'\n {lk}')
    for pk, p in priors.items():
        raw = {b: p[b] * a[b] * i[b] for b in B}; t = sum(raw.values())
        post = {b: raw[b] / t for b in B}
        summary.setdefault(lk, []).append(post['NHET'])
        odds = post['NHET'] / post['NTROP'] if post['NTROP'] else float('inf')
        print(f'   {pk:48} ' + ' / '.join(f'{post[b]:.2f}' for b in B) + f'   odds {odds:5.2f}')

print('\nRange of P(NHET) across the six priors')
for lk, v in summary.items():
    print(f'   {lk:42} {min(v):.2f} - {max(v):.2f}')

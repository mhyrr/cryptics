"""Query the Marshall et al. 2021 UM-UKCA deposition emulator (CEMAC tool output) for UE 1453.

Usage: python3 -I emulator.py <cemac_data_dir> <evolv2k_v4.tab> <gvp_holocene_eruptions.csv> <out_likelihood.json>

The CEMAC tool ships the emulator mean and SD on a 26 x 26 x 26 grid (latitude -80..80,
injection height 16.5..26.5 km = plume middle, SO2 10..100 Tg) for 1 January and 1 July
eruptions, as JSON. This script:
  1. reproduces Marshall 2021 Table 1 latitude ranges with the tool's own retention rule
     (keep a cell if emulator mean +/- 1 SD overlaps the observed range on both ice sheets);
  2. runs the same query on named eVolv2k v4 events in the emulator's domain (calibration);
  3. runs it for 1453 and writes band likelihoods.
Likelihood per cell: N(DG; mean_G, sqrt(sd_G^2 + obsG^2)) * N(DA; mean_A, sqrt(sd_A^2 + obsA^2)),
averaged over SO2 and height (uniform on the grid) and over latitude within a band
(weighted by grid spacing, i.e. uniform in latitude).
"""
import csv, json, math, os, re, sys

D, EV, GVP, OUT = sys.argv[1:5]
ld = lambda n: json.load(open(os.path.join(D, n)))
ax = ld('data_axes.json')
EM = {s: (ld(f'data_greenland_{s}.json'), ld(f'data_antarctica_{s}.json')) for s in ('jan', 'jul')}
LAT, H, SO2 = ax['lat'], ax['h'], ax['so2']
N = len(LAT)
lats = sorted(set(LAT))
# latitude weight = width of the cell around each grid latitude
wid = {}
for i, l in enumerate(lats):
    lo = lats[i - 1] if i else l
    hi = lats[i + 1] if i + 1 < len(lats) else l
    wid[l] = (hi - lo) / 2
FRAC_G, FRAC_A = 0.26, 0.12  # obs 1-sigma as a fraction; Marshall 2021 Table 1 (Sigl 2015) averages
FLOOR = 1.0                   # kg/km2, so a zero deposition gets a finite obs sigma

def band4(l):
    return 'NHET' if l > 30 else ('SHET' if l < -30 else ('NTROP' if l >= 0 else 'STROP'))
B4 = ['NHET', 'NTROP', 'STROP', 'SHET']

def npdf(x, m, s):
    return math.exp(-0.5 * ((x - m) / s) ** 2) / (s * math.sqrt(2 * math.pi))

def query(dg, sg, da, sa, season, so2rng=(0, 1e9)):
    """Return (retained lat range, per-lat mean likelihood, per-band likelihood)."""
    G, A = EM[season]
    kept_lats, perlat, cnt = set(), {l: 0.0 for l in lats}, {l: 0 for l in lats}
    for j in range(N):
        if not (so2rng[0] <= SO2[j] <= so2rng[1]): continue
        gm, gs, am, as_ = G['mean'][j], G['sd'][j], A['mean'][j], A['sd'][j]
        if (am + as_ > da - sa) and (am - as_ < da + sa) and (gm + gs > dg - sg) and (gm - gs < dg + sg):
            kept_lats.add(LAT[j])
        perlat[LAT[j]] += npdf(dg, gm, math.hypot(gs, sg)) * npdf(da, am, math.hypot(as_, sa))
        cnt[LAT[j]] += 1
    perlat = {l: perlat[l] / cnt[l] for l in lats if cnt[l]}
    band = {}
    for b in B4:
        ls = [l for l in perlat if band4(l) == b]
        band[b] = sum(perlat[l] * wid[l] for l in ls) / sum(wid[l] for l in ls)
    rng = (min(kept_lats), max(kept_lats)) if kept_lats else None
    return rng, perlat, band, kept_lats

def fmt(r): return f'{r[0]:6.1f}..{r[1]:6.1f}' if r else '   none      '

# ---- 1. reproduce Marshall 2021 Table 1 (p. 9 of 21)
print('== Check against Marshall 2021 Table 1 (published lat min..max, Jan | Jul)')
TABLE1 = [('-44', 101, 26, 15, 4, (-9, 40), (6, 75)), ('1458', 39, 10, 64, 7, (-64, -40), (-67, -49)),
          ('540', 61, 16, 34, 4, (-30, -11), (-28, 17)), ('1815', 40, 10, 46, 5, (-56, -22), (-62, -6)),
          ('1230', 56, 15, 23, 3, (-20, -6), (-17, 19)), ('682', 38, 10, 39, 5, (-40, -19), (-54, -4)),
          ('574', 38, 10, 34, 4, (-35, -15), (-49, -1)), ('266', 61, 16, 11, 1, (-11, 11), (2, 36))]
for yr, dg, sg, da, sa, pj, pl in TABLE1:
    rj = query(dg, sg, da, sa, 'jan')[0]; rl = query(dg, sg, da, sa, 'jul')[0]
    print(f'   {yr:>5}  published {pj[0]:4}..{pj[1]:4} | {pl[0]:4}..{pl[1]:4}    this script {fmt(rj)} | {fmt(rl)}')
print('   (grid spacing is 6.5 deg in latitude, so agreement to within one grid step is the best possible)')

# ---- 2. calibration on named eVolv2k events
gv = {}
for r in csv.DictReader(open(GVP, encoding='utf-8')):
    m = re.match(r'POINT \(([-\d.]+) ([-\d.]+)\)', r['GeoLocation'])
    if m: gv.setdefault(r['Volcano_Number'], float(m.group(1)))
lines = open(EV, encoding='utf-8').read().split('\n')
start = next(i for i, l in enumerate(lines) if l.startswith('*/')) + 2
ev = []
for l in lines[start:]:
    if not l.strip(): continue
    f = l.split('\t')
    ev.append(dict(year=int(f[0]), month=int(f[2]), day=int(f[3]), lat=float(f[4]), dg=float(f[5]),
                   da=float(f[6]), vssi=float(f[7]), loc=f[10]))

def season_of(e):
    if e['month'] == 1 and e['day'] == 1: return None  # eVolv2k default date: season unknown
    return 'jan' if e['month'] in (10, 11, 12, 1, 2, 3) else 'jul'

def band_post(e, scale=1.0):
    dg, da = e['dg'] * scale, e['da'] * scale
    sg, sa = max(FRAC_G * dg, FLOOR), max(FRAC_A * da, FLOOR)
    s = season_of(e)
    seasons = [s] if s else ['jan', 'jul']
    res = [query(dg, sg, da, sa, x) for x in seasons]
    band = {b: sum(r[2][b] for r in res) / len(res) for b in B4}
    kept = set().union(*[r[3] for r in res])
    return band, kept, s

print('\n== Calibration: named eVolv2k v4 events inside the emulator domain')
print('   domain: 5 <= VSSI <= 50 Tg S (10-100 Tg SO2) and DG >= 20 or DA >= 5 (Marshall 2021 detection thresholds)')
print('   uniform prior over the four bands by latitude; truth = GVP latitude; Kuwae 1458 excluded (contested)')
for scale, label in [(1.0, 'observed deposition'), (0.5, 'deposition / 2 (Marshall 2021 model-bias variant)')]:
    print(f'\n   -- {label}')
    print('   year  volcano                       lat   true   season  P(NHET) P(NTROP) P(STROP) P(SHET)  argmax  truth-lat-retained')
    hit = n = inret = 0
    for e in ev:
        if e['loc'] == 'N/A' or e['loc'].startswith('Unidentifed') or e['loc'].startswith('Kuwae'): continue
        if not (5 <= e['vssi'] <= 50 and (e['dg'] >= 20 or e['da'] >= 5)): continue
        tl = e['lat']  # eVolv2k latitude for named events equals GVP to < 1 deg (calib_asymmetry.txt)
        band, kept, s = band_post(e, scale)
        tot = sum(band.values())
        post = {b: band[b] / tot for b in B4}
        am = max(post, key=post.get)
        nearest = min(lats, key=lambda l: abs(l - tl))
        ok_ret = nearest in kept
        n += 1; hit += am == band4(tl); inret += ok_ret
        print(f'   {e["year"]:>5} {e["loc"][:28]:28} {tl:6.1f}  {band4(tl):5}  {s or "both":6}  ' +
              '  '.join(f'{post[b]:6.2f}' for b in B4) + f'   {am:5}   {"yes" if ok_ret else "NO"}')
    print(f'   argmax band correct {hit}/{n}; true latitude inside retained set {inret}/{n}')

# ---- 3. UE 1453
DG, DA = 24.8, 5.1
SG, SA = FRAC_G * DG, FRAC_A * DA
print(f'\n== UE 1453: Greenland {DG} +/- {SG:.1f}, Antarctica {DA} +/- {SA:.2f} kg/km2 (1 sigma, assumed fractions)')
out = {}
for so2, slabel in [((0, 1e9), 'SO2 free (10-100 Tg)'), ((0, 32.5), 'SO2 <= 32 Tg (eVolv2k VSSI + 2 sigma, x2)')]:
    for wide, wlabel in [(False, 'obs sigma 26%/12%'), (True, 'obs sigma 50%/50%')]:
        sg, sa = (0.5 * DG, 0.5 * DA) if wide else (SG, SA)
        print(f'\n   -- {slabel}; {wlabel}')
        print('      lat   Jan-kept  Jul-kept   L(Jan)     L(Jul)')
        rj = query(DG, sg, DA, sa, 'jan', so2); rl = query(DG, sg, DA, sa, 'jul', so2)
        for l in lats:
            print(f'   {l:6.1f}   {"x" if l in rj[3] else ".":^8}  {"x" if l in rl[3] else ".":^8}  {rj[1][l]:.2e}   {rl[1][l]:.2e}')
        print(f'      retained latitude range: Jan {fmt(rj[0])}   Jul {fmt(rl[0])}')
        for season, r in [('jan', rj), ('jul', rl)]:
            tot = sum(r[2].values())
            print(f'      {season}: band likelihood normalised  ' + '  '.join(f'{b} {r[2][b]/tot:.2f}' for b in B4))
            out[f'{slabel}; {wlabel}; {season}'] = r[2]
        mix = {b: (rj[2][b] + rl[2][b]) / 2 for b in B4}
        tot = sum(mix.values())
        print('      Jan/Jul 50:50: band likelihood normalised  ' + '  '.join(f'{b} {mix[b]/tot:.2f}' for b in B4))
        out[f'{slabel}; {wlabel}; mix'] = mix
json.dump(out, open(OUT, 'w'), indent=1)

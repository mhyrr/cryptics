"""Rank candidate sources for UE 1453 with the pre-registered score (README).

Usage:
  python3 -I rank1453.py <gvp_eruptions.csv> <gvp_volcanoes.csv> <evolv2k_v4.tab> <intcal20.14c>
                         <posterior_dir_of_03> [lab_ages.csv] [regional.csv]
posterior_dir_of_03: folder holding 03's lik_*.json. lab_ages.csv / regional.csv are optional
(without them this is the GVP-only prior filter).
"""
import csv, json, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pipeline as P

GVP, VOL, EV, IC, D03 = sys.argv[1:6]
LAB = sys.argv[6] if len(sys.argv) > 6 else None
REG = sys.argv[7] if len(sys.argv) > 7 else None
VOV = sys.argv[8] if len(sys.argv) > 8 else None

rows = P.load_gvp(GVP, VOL)
ev = P.load_evolv2k(EV)
att = P.attribute(ev, rows)
ic = P.IntCal(IC)
sm = P.SizeModel(rows, att)
THR = 9.97 - 3.07
grid = P.make_grid(900, 1950)

# ---- band likelihoods from 03 (normalised)
la = json.load(open(os.path.join(D03, 'lik_asymmetry.json')))
li = json.load(open(os.path.join(D03, 'lik_isotope.json')))
le = json.load(open(os.path.join(D03, 'lik_emulator.json')))
def norm(d): s = sum(d.values()); return {k: v / s for k, v in d.items()}
def prod(a, b): return norm({k: a[k] * b[k] for k in P.BANDS})
named = [a for a in att]
asy_only = P.asym_kde_lik(0.829, named)
VARIANTS = {
    'A1': prod(la['all window[0.75,1.0)'], li['all']),
    'A6': prod(la['all window[0.7,0.95)'], li['all']),
    'A5': prod(la['all window[0.7,0.95)'], li['out-of-sample only']),
    'E1': prod(le['SO2 free (10-100 Tg); obs sigma 26%/12%; mix'], li['all']),
    'ASY': asy_only,
}

# ---- candidates: GVP filter + regional rows
cands = P.candidate_filter(rows, 1453)
reg_pdf = {}
if REG:
    byname = {}
    for r in rows: byname.setdefault(r['name'], r)
    for r in csv.DictReader(open(REG, encoding='utf-8')):
        g = byname[r['gvp_name']]
        lo, hi = float(r['lo']), float(r['hi'])
        enum = 'REG-' + r['id']
        cands.append(dict(g, name=r['name'], enum=enum, confirmed=True, vei=P.as_int(r['vei']), method=r['method'],
                          mod='', year=int((lo + hi) / 2), unc=int((hi - lo) / 2), month=0, end=None,
                          unit=r['event'], region=r['catalog']))
        reg_pdf[enum] = (None, lo, hi)
vei_note = {}
if VOV:
    for v in csv.DictReader(open(VOV, encoding='utf-8')):
        for c in cands:
            if c['enum'] == v['enum']:
                vei_note[c['enum']] = (c['vei'], int(v['vei']), v['headline'] == 'yes')
                if v['headline'] == 'yes': c['vei'] = int(v['vei'])

# ---- primary lab ages -> overrides
def lab_pdf(group):
    ages = [(float(g['age_bp']), float(g['err'])) for g in group if g['use'] == 'combine']
    single = [g for g in group if g['use'] == 'event']
    maxima = [g for g in group if g['use'] == 'maximum']
    minima = [g for g in group if g['use'] == 'minimum']
    if single: ages = ages + [(float(g['age_bp']), float(g['err'])) for g in single]
    p = P.pdf_14c(ic, grid, ages) if ages else [1.0] * len(grid)
    for g in maxima:   # eruption is younger than this age: multiply by P(T_sample < t)
        q = P.pdf_14c(ic, grid, [(float(g['age_bp']), float(g['err']))]); c, acc = [], 0.0
        for x in q: acc += x; c.append(acc)
        p = [a * b for a, b in zip(p, c)]
    for g in minima:   # eruption is older than this age
        q = P.pdf_14c(ic, grid, [(float(g['age_bp']), float(g['err']))]); c, acc = [], 0.0
        for x in reversed(q): acc += x; c.append(acc)
        p = [a * b for a, b in zip(p, reversed(c))]
    return P.normalise(p)

overrides, labinfo = {}, {}
for enum, (_, lo, hi) in reg_pdf.items():
    overrides[enum] = (P.pdf_uniform(grid, lo, hi), 'uniform catalog range')
if LAB:
    groups = {}
    for g in csv.DictReader(open(LAB, encoding='utf-8')):
        if g['use'] in ('', 'listed'): continue
        groups.setdefault(g['enum'], []).append(g)
    for enum, grp in groups.items():
        pdf = lab_pdf(grp)
        overrides[enum] = (pdf, 'IntCal20 lab ages (' + ','.join(sorted(set(g['use'] for g in grp))) + ')')
        labinfo[enum] = grp

def show(scored, title, n=25):
    print(f'\n== {title}')
    print('rank volcano                  year±unc  VEI class  band   lat    method                       how                     P(date)   P(band)  P(size)   score     share')
    tot = sum(s['score'] for s in scored)
    for i, s in enumerate(scored[:n], 1):
        print(f'{i:>4} {s["name"][:24]:24} {s["year"]:>5}±{s["unc"]:<4} {str(s["vei"]) if s["vei"] is not None else "?":>3} '
              f'{s["sclass"][:5]:5} {s["band"]:5} {s["lat"]:6.1f}  {s["method"][:28]:28} {s["how"][:22]:22} '
              f'{s["p_date"]:.4f}   {s["p_band"]:.3f}   {s["p_size"]:.4f}   {s["score"]:.2e}  {s["score"] / tot:.3f}')

print(f'UE 1453. Onset {P.ONSET_1453}. Size threshold VSSI >= {THR:.2f} Tg S. Candidates: {len(cands)} '
      f'({sum(1 for c in cands if c["enum"].startswith("REG-"))} regional). Primary-age overrides: {len(overrides)}')
print('Band likelihood variants (normalised): ' + '; '.join(f'{k}: ' + ' '.join(f'{b} {v[b]:.2f}' for b in P.BANDS) for k, v in VARIANTS.items()))

base, dropped = P.score_candidates(cands, grid, ic, P.ONSET_1453, VARIANTS['A1'], sm, THR, overrides=overrides)
if vei_note:
    print('VEI from primary sources (GVP -> paper; headline?): ' + '; '.join(f'{k} {a} -> {b} ({"headline" if h else "sensitivity"})' for k, (a, b, h) in vei_note.items()))
print('\nDropped by the leakage rule:')
for r, why in dropped: print(f'   {r["name"]} {r["year"]}±{r["unc"]} ({r["method"]}): {why}')
show(base, 'Headline: band A1, window on, missing VEI = mixture, size one-sided, ice rows dropped')

runs = {}
for k in VARIANTS:
    runs[f'band {k}'] = P.score_candidates(cands, grid, ic, P.ONSET_1453, VARIANTS[k], sm, THR, overrides=overrides)[0]
runs['window off (wide prior only)'] = P.score_candidates(cands, grid, ic, P.ONSET_1453, VARIANTS['A1'], sm, THR, overrides=overrides, use_window=False)[0]
runs['NHET window 02 ice-only (to 1453.7)'] = P.score_candidates(cands, grid, ic, P.ONSET_1453, VARIANTS['A1'], sm, THR, overrides=overrides, nhet=P.WIN_NHET_ICE)[0]
runs['missing VEI = 4'] = P.score_candidates(cands, grid, ic, P.ONSET_1453, VARIANTS['A1'], sm, THR, overrides=overrides, unknown_as=4)[0]
runs['size two-sided [obs/2, 2obs]'] = P.score_candidates(cands, grid, ic, P.ONSET_1453, VARIANTS['A1'], sm, 9.97 / 2, thr_hi=9.97 * 2, overrides=overrides)[0]
runs['ice-core rows included'] = P.score_candidates(cands, grid, ic, P.ONSET_1453, VARIANTS['A1'], sm, THR, overrides=overrides, include_ice=True)[0]
gvp_only = {k: v for k, v in overrides.items() if k.startswith('REG-')}
cands_gvpvei = [dict(c, vei=vei_note[c['enum']][0]) if c['enum'] in vei_note and vei_note[c['enum']][2] else c for c in cands]
runs['no primary ages (GVP dates)'] = P.score_candidates(cands, grid, ic, P.ONSET_1453, VARIANTS['A1'], sm, THR, overrides=gvp_only)[0]
runs['GVP VEI (no VEI overrides)'] = P.score_candidates(cands_gvpvei, grid, ic, P.ONSET_1453, VARIANTS['A1'], sm, THR, overrides=overrides)[0]
cands_sens = [dict(c, vei=vei_note[c['enum']][1]) if c['enum'] in vei_note else c for c in cands]
runs['all VEI overrides incl. sensitivity-only'] = P.score_candidates(cands_sens, grid, ic, P.ONSET_1453, VARIANTS['A1'], sm, THR, overrides=overrides)[0]

print('\n== Sensitivity: top 8 under each variant (volcano year: share of total score)')
for k, sc in runs.items():
    tot = sum(s['score'] for s in sc)
    print(f'  {k:38} ' + ' | '.join(f'{s["name"][:13]} {s["year"]}: {s["score"] / tot:.2f}' for s in sc[:8]))

print('\n== Regional sums of score share (headline)')
tot = sum(s['score'] for s in base); reg = {}
for s in base:
    key = s['region'] or '?'
    reg[key] = reg.get(key, 0) + s['score'] / tot
for k, v in sorted(reg.items(), key=lambda kv: -kv[1])[:12]: print(f'   {k:45} {v:.3f}')
sub = {}
for s in base: sub[s['subregion'] or '?'] = sub.get(s['subregion'] or '?', 0) + s['score'] / tot
print('   by GVP subregion (top 12):')
for k, v in sorted(sub.items(), key=lambda kv: -kv[1])[:12]: print(f'      {k:45} {v:.3f}')
NPAC = ('Kamchatka', 'Kuril', 'Aleutian', 'Alaska', 'Japan', 'Honshu', 'Hokkaido', 'Kyushu', 'Izu', 'Ryukyu', 'Cascade', 'Canada')
for lab, variant in [('A1', base)] + [(k, v) for k, v in runs.items() if k.startswith('band ')]:
    t2 = sum(s['score'] for s in variant)
    npac = sum(s['score'] for s in variant if any(w in (s['subregion'] + s['region']) for w in NPAC) and s['lat'] > 30) / t2
    ice = sum(s['score'] for s in variant if 'Iceland' in s['subregion'] or s['name'] in ('Jan Mayen',)) / t2
    print(f'   {lab:10} North Pacific rim > 30N: {npac:.3f}   Iceland + Jan Mayen: {ice:.3f}   top candidate share: {variant[0]["score"] / t2:.3f} ({variant[0]["name"]} {variant[0]["year"]})')
bands = {}
for s in base: bands[s['band']] = bands.get(s['band'], 0) + s['score'] / tot
print('   by band: ' + '  '.join(f'{b} {bands.get(b, 0):.3f}' for b in P.BANDS))

if labinfo:
    print('\n== Recalibrated primary dates (IntCal20): P(start in window) and 95.4 % HPD')
    for enum, grp in labinfo.items():
        pdf = overrides[enum][0]
        r = next((c for c in cands if c['enum'] == enum), None)
        if r is None: continue
        b = P.band4(r['lat'])
        pw = P.p_date(pdf, P.window_lik(P.make_grid(900, 1950), P.ONSET_1453, b))
        inwin = sum(p for t, p in zip(grid, pdf) if (P.ONSET_1453 + (P.WIN_NHET if b in ('NHET', 'SHET') else P.WIN_TROP)[0]) <= t <
                    (P.ONSET_1453 + (P.WIN_NHET if b in ('NHET', 'SHET') else P.WIN_TROP)[1]))
        h = P.hpd(grid, pdf)
        print(f'   {r["name"][:22]:22} {", ".join(g["lab_code"] + " " + g["age_bp"] + "±" + g["err"] + " (" + g["use"] + ")" for g in grp)}')
        print(f'      HPD95: ' + ', '.join(f'{a:.0f}-{b:.0f}' for a, b in h) + f'   P(in {b} window) = {inwin:.4f}   P(date|window) = {pw:.4f}')

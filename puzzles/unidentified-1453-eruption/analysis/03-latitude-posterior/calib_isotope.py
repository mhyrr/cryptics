"""Calibrate the Burke sulfur-isotope class (tropical-slope vs extratropical mixing pattern).

Usage: python3 -I calib_isotope.py <isotope_cases.csv> <out_likelihood.json>

isotope_cases.csv is hand-extracted from the papers named in its columns (LLM read,
page/line cites given). This script only counts. Likelihoods use a Jeffreys prior,
(k + 0.5) / (n + 1), because the counts are tiny.
"""
import csv, json, sys

rows = list(csv.DictReader(open(sys.argv[1], encoding='utf-8')))
print(f'known-source events with an isotope class: {len(rows)}')
print('excluded on purpose: Huaynaputina 1600 (which peak is Huaynaputina was itself decided from isotopes),')
print('  1458 (source contested), 536/540/626/1182 (no identified source).')
for r in rows:
    ok = (r['isotope_class'] == 'extratropical') == (r['true_band'] == 'NHET')
    print(f'  {r["event"]:24} lat {float(r["gvp_lat"]):6.1f} {r["true_band"]:5} iso={r["isotope_class"]:13} {r["role"]:28} {"match" if ok else "MISS"}')

def lik(sub):
    out = {}
    for band in ('NHET', 'TROP'):
        m = [r for r in sub if r['true_band'] == band]
        k = sum(r['isotope_class'] == 'extratropical' for r in m)
        out[band] = dict(k=k, n=len(m), L=(k + 0.5) / (len(m) + 1))
    return out

res = {}
for name, sub in [('all', rows), ('out-of-sample only', [r for r in rows if r['role'] == 'out-of-sample'])]:
    v = lik(sub); res[name] = v
    acc = sum((r['isotope_class'] == 'extratropical') == (r['true_band'] == 'NHET') for r in sub)
    print(f'\n== {name}: class matched band {acc}/{len(sub)}')
    for b in v: print(f'   P(extratropical pattern | {b}) = {v[b]["k"]}/{v[b]["n"]} -> {v[b]["L"]:.3f}')
    print(f'   likelihood ratio NHET/TROP for an extratropical pattern: {v["NHET"]["L"]/v["TROP"]["L"]:.2f}')

print('\nAssumptions for the posterior: NTROP and STROP share the TROP value (only Pinatubo is NH-tropical).')
print('SHET also takes the TROP value: SH sulfate can reach Greenland only through the overworld, so a')
print('below-ozone-layer onset in Greenland is at least as unlikely as for a tropical source. No SHET case exists.')
json.dump({k: {'NHET': v['NHET']['L'], 'NTROP': v['TROP']['L'], 'STROP': v['TROP']['L'], 'SHET': v['TROP']['L']}
           for k, v in res.items()}, open(sys.argv[2], 'w'), indent=1)

"""Blind calibration of the candidate scorer on eruptions with a known source (README).

Usage: python3 -I calibrate.py <gvp_eruptions.csv> <gvp_volcanoes.csv> <evolv2k_v4.tab> <intcal20.14c> [draws]

For each eVolv2k v4 named event with VSSI >= 3 Tg S (Kuwae 1458 excluded): build the GVP
candidate list around its Greenland onset, score it the way UE 1453 is scored, and report the
rank of the true volcano. Band likelihood: asymmetry KDE trained leave-one-out. Size model:
refitted without the event. Modes: as-is, degraded (precise dates -> synthetic 14C).
"""
import math, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pipeline as P

GVP, VOL, EV, IC = sys.argv[1:5]
DRAWS = int(sys.argv[5]) if len(sys.argv) > 5 else 200
rows = P.load_gvp(GVP, VOL)
ev = P.load_evolv2k(EV)
att = P.attribute(ev, rows)
ic = P.IntCal(IC)

# NEEM-2011-S1 onsets measured in 02 (results/onset.txt; Huaynaputina from the README lag +13.5 months)
MEASURED_ONSET = {('Laki', 1783): 1782.950, ('Tambora', 1815): 1816.012, ('Krakatao', 1883): 1883.710,
                  ('Huaynaputina', 1600): 1600.13 + 13.5 / 12}

def true_date(e):
    return e['year'] + (max(e['month'], 1) - 1) / 12.0 + (max(e['day'], 1) - 1) / 365.0

cases = [a for a in att if a['vssi'] >= 3.0]
cases.sort(key=lambda a: a['year'])
rng = random.Random(1453)

def rank_of(scored, vnum):
    for i, s in enumerate(scored, 1):
        if s['vnum'] == vnum: return i
    return None

def degraded_scores(base, cands, fc, onset, truth_vnum, t_true, draw_rng, nhet, hide=None):
    """Replace the date term of every precise row by a synthetic 14C draw; others keep as-is p_date.
    hide=(size_model, thr): also blank the true volcano's VEI (post-hoc stress test)."""
    out = []
    for s in base:
        if hide and s['vnum'] == truth_vnum:
            ps = hide[0].p(None, s['sclass'], hide[1])
            s = dict(s, p_size=ps, score=s['p_date'] * s['p_band'] * ps)
        if s['method'] in P.PRECISE and s['unc'] <= 1:
            if s['vnum'] == truth_vnum:
                t = t_true
            elif s['end'] is not None and s['end'] > s['year']:
                t = (s['year'] + s['end'] + 1) / 2
            elif s['month']:
                t = s['year'] + (s['month'] - 0.5) / 12
            else:
                t = s['year'] + 0.5
            mu, _ = ic.at(t)
            age = mu + (draw_rng.gauss(0, P.SIG_LAB_SYNTH) if draw_rng else 0.0)
            pd = fc.p_date(age, P.SIG_LAB_SYNTH, s['band'], nhet)
            out.append(dict(s, p_date=pd, score=pd * s['p_band'] * s['p_size']))
        else:
            out.append(s)
    out.sort(key=lambda x: -x['score'])
    return out

summary = []
print(f'Calibration cases: {len(cases)} eVolv2k v4 named events with VSSI >= 3 Tg S (Kuwae excluded)')
print(f'Degraded mode: {DRAWS} draws, seed 1453, synthetic 14C error {P.SIG_LAB_SYNTH:g} yr')
for e in cases:
    t_true = true_date(e)
    key = (e['key'], e['year'])
    if key in MEASURED_ONSET:
        onset, osrc = MEASURED_ONSET[key], 'measured (02)'
    else:
        onset = t_true - 0.25 if e['band'] in ('NHET', 'SHET') else t_true + 0.5
        osrc = 'synthetic'
    train = [a for a in att if a is not e]
    band_lik = P.asym_kde_lik(e['asy'], train)
    sm = P.SizeModel(rows, att, exclude=e)
    thr = max(e['vssi'] - e['vssi_sd'], 0.0)
    cands = P.candidate_filter(rows, int(math.floor(onset)))
    grid = P.make_grid(math.floor(onset) - 600, min(math.floor(onset) + 600, 1950))
    nhet = P.WIN_NHET_ICE
    base, dropped = P.score_candidates(cands, grid, ic, onset, band_lik, sm, thr, nhet=nhet)
    true_rows_all = [r for r in rows if r['vnum'] == e['vnum']]
    in_list = [r for r in cands if r['vnum'] == e['vnum']]
    dropped_true = [r for r, _ in dropped if r['vnum'] == e['vnum']]
    r1 = rank_of(base, e['vnum'])
    fc = P.FastCal(ic, onset)
    det = degraded_scores(base, cands, fc, onset, e['vnum'], t_true, None, nhet)
    r2det = rank_of(det, e['vnum'])
    ranks = []
    for _ in range(DRAWS):
        sc = degraded_scores(base, cands, fc, onset, e['vnum'], t_true, rng, nhet)
        ranks.append(rank_of(sc, e['vnum']))
    hid_sc = degraded_scores(base, cands, fc, onset, e['vnum'], t_true, None, nhet, hide=(sm, thr))
    hid = rank_of(hid_sc, e['vnum'])
    true_sub = next((r['subregion'] for r in rows if r['vnum'] == e['vnum']), '?')
    def sub_rank(sc):
        acc = {}
        for x in sc: acc[x['subregion']] = acc.get(x['subregion'], 0) + x['score']
        order = sorted(acc, key=lambda k: -acc[k])
        return (order.index(true_sub) + 1 if true_sub in order else None), len(order)
    sr_det, nsub = sub_rank(det)
    sr_hid, _ = sub_rank(hid_sc)
    present = [x for x in ranks if x is not None]
    med = sorted(present)[len(present) // 2] if present else None
    top5 = sum(1 for x in present if x <= 5) / DRAWS if present else 0.0
    top1 = sum(1 for x in present if x == 1) / DRAWS if present else 0.0
    n = len(base)
    print(f'\n== {e["year"]} {e["loc"][:40]}  true band {e["band"]}  lat {e["glat"]:.1f}  VSSI {e["vssi"]:.2f}+-{e["vssi_sd"]:.2f}  ASY {e["asy"]:.3f}')
    print(f'   onset {onset:.2f} ({osrc}); true date {t_true:.2f}; list span {int(math.floor(onset)) + P.LIST_SPAN[0]}-{int(math.floor(onset)) + P.LIST_SPAN[1]}; '
          f'{n} scored, {len(dropped)} dropped (ice core)')
    print(f'   band likelihood (LOO asym KDE): ' + ' '.join(f'{b} {band_lik[b]:.2f}' for b in P.BANDS))
    print(f'   true volcano rows in GVP within list span: {len(in_list)} '
          f'({"; ".join(f"{r["year"]}±{r["unc"]} VEI {r["vei"]} {r["method"]}" for r in in_list) or "none"})'
          + (f'; dropped by leakage rule: {len(dropped_true)}' if dropped_true else ''))
    if not in_list:
        near = sorted(true_rows_all, key=lambda r: abs(r['year'] - e['year']))[:2]
        print(f'   nearest true-volcano GVP rows: ' + '; '.join(f'{r["year"]}±{r["unc"]} VEI {r["vei"]} {r["method"]}' for r in near))
    def fmt(sc, k=3):
        tot = sum(s['score'] for s in sc) or 1
        return ' | '.join(f'{s["name"][:14]} {s["year"]} ({s["score"] / tot:.2f})' for s in sc[:k])
    tr = next((s for s in base if s['vnum'] == e['vnum']), None)
    if tr:
        print(f'   true row as-is: P(date) {tr["p_date"]:.4f}  P(band) {tr["p_band"]:.3f}  P(size) {tr["p_size"]:.4f} ({tr["how"]})')
    print(f'   as-is rank: {r1 if r1 else "absent"} of {n}.  top 3: {fmt(base)}')
    print(f'   degraded rank (no noise): {r2det if r2det else "absent"}; over draws: median {med if med else "absent"}, '
          f'P(rank 1) {top1:.2f}, P(top 5) {top5:.2f}.  top 3 (no noise): {fmt(det)}')
    print(f'   degraded + true VEI hidden (post-hoc stress): rank {hid if hid else "absent"}; chance top-5 rate {min(5, n) / n:.2f}')
    print(f'   true subregion ({true_sub}) rank by summed score: degraded {sr_det}, VEI hidden {sr_hid}, of {nsub} subregions')
    summary.append(dict(year=e['year'], name=e['key'], band=e['band'], n=n, asis=r1, deg=r2det, med=med,
                        top1=top1, top5=top5, hid=hid, srd=sr_det, srh=sr_hid, nsub=nsub, method=(in_list[0]['method'] if in_list else (dropped_true[0]['method'] if dropped_true else '-'))))

print('\n== Summary (rank of true volcano; "absent" = no surviving GVP row in the list)')
print('year   source              band    n  as-is  degraded  deg.median  P(top5)  VEI-hidden  true-row dating method')
for s in summary:
    print(f'{s["year"]:>5}  {s["name"][:18]:18}  {s["band"]:5} {s["n"]:>4}  {str(s["asis"] or "absent"):>6}  {str(s["deg"] or "absent"):>8}  '
          f'{str(s["med"] or "absent"):>10}  {s["top5"]:7.2f}  {str(s["hid"] or "absent"):>10}  {s["method"]}')
def stats(key):
    pres = [s[key] for s in summary if s[key]]
    return len(pres), sum(1 for x in pres if x == 1), sum(1 for x in pres if x <= 5), len(summary) - len(pres)
for key, lab in [('asis', 'as-is'), ('deg', 'degraded (no noise)'), ('med', 'degraded (median over draws)'), ('hid', 'degraded + VEI hidden (post-hoc)')]:
    npres, n1, n5, nabs = stats(key)
    print(f'{lab:30}: present {npres}/{len(summary)}; rank 1 in {n1}; top 5 in {n5} of {npres} present; absent {nabs}')
for era, sel in [('historical era (1477-1883)', lambda s: s['year'] >= 1477), ('pre-1477', lambda s: s['year'] < 1477)]:
    sub = [s for s in summary if sel(s)]
    for key, lab in [('asis', 'as-is'), ('med', 'degraded median'), ('hid', 'VEI hidden')]:
        pres = [s[key] for s in sub if s[key]]
        print(f'   {era:28} {lab:16}: n {len(sub)}, absent {len(sub) - len(pres)}, rank 1 {sum(1 for x in pres if x == 1)}, '
              f'top 5 {sum(1 for x in pres if x <= 5)}, median rank {sorted(pres)[len(pres) // 2] if pres else "-"}')
for key, lab in [('srd', 'true subregion rank, degraded'), ('srh', 'true subregion rank, VEI hidden')]:
    pres = [s[key] for s in summary if s[key]]
    print(f'{lab:34}: rank 1 in {sum(1 for x in pres if x == 1)}, top 3 in {sum(1 for x in pres if x <= 3)} of {len(pres)}; '
          f'median {sorted(pres)[len(pres) // 2]}; median number of subregions {sorted(s["nsub"] for s in summary)[len(summary) // 2]}')
pre = [s for s in summary if s['med']]
crit = sum(1 for s in pre if s['med'] <= 5)
print(f'Pre-registered criterion (degraded median rank <= 5 in at least half of present cases): '
      f'{crit}/{len(pre)} -> {"MET" if pre and crit >= len(pre) / 2 else "NOT MET"}')

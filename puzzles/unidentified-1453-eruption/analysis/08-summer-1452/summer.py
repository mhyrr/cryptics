"""Experiment 08: eruption-year summer response, calibration and UE 1453 (1452-1454).

Standard library only. Method fixed in README.md ("Pre-registration").
Parsing, anomaly and threshold code is imported from 04's fingerprint.py
(experiment 04-cooling-fingerprint), by file path, unchanged.

Usage
  python3 -I summer.py calibrate DATASET VALUES SITES EVENTS EVOLV2K [--parker1641] [--vssi3]
  python3 -I summer.py target    DATASET VALUES SITES EVENTS EVOLV2K
  python3 -I summer.py regional  DATASET VALUES SITES EVENTS EVOLV2K

DATASET: schneider (VALUES schneider2015mxd.txt, SITES sites_schneider2015.tsv)
         ntrend    (VALUES ntrend2015tr.txt, SITES ntrend2015-RecordsUsed_Metadata.txt)
"""
import importlib.util
import math
import os
import random
import statistics
import sys

sys.dont_write_bytecode = True  # do not leave __pycache__ in 04
HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "fingerprint04", os.path.join(HERE, "..", "04-cooling-fingerprint", "fingerprint.py"))
fp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fp)

SEED = 1453
N_PERM = 10000
BG_RANGE = (1260, 1990)
UE_E = 1452            # reference fixed on 1442-1451
UE_YEARS = (1452, 1453, 1454)
CLASSES = ("XE", "XL", "TE", "TL")
DIST_KM = 2000.0
SECTORS = [("NAmerica", -170, -50), ("Europe", -20, 40), ("Urals-WSib", 40, 100), ("EAsia-Sib", 100, 180)]
# Source longitudes from the GVP cache GeoLocation field (extratropical events only).
SRC_LON = {"Veidivotn": -18.3, "Hekla": -19.666, "Laki": -17.316, "Sheveluch": 161.36,
           "Novarupta": -155.1588, "Tarumae": 141.38, "Shikotsu": 141.38, "Katla": -19.083,
           "Zavaritskii": 151.95}


def setup(argv):
    dataset, vpath, spath, epath, evpath = argv[:5]
    flags = set(argv[5:])
    year_col = {"schneider": "age_AD", "ntrend": "Year"}[dataset]
    values = fp.load_table(vpath, year_col)
    sites = fp.load_sites(dataset, spath)
    if dataset == "ntrend":
        values, sites = fp.align_ntrend(values, sites)
    values = {c: s for c, s in values.items() if c in sites}
    sds = {c: fp.site_sd(s) for c, s in values.items()}
    events = list(fp._rows(epath))
    _, starts = fp.exclusion_years(evpath, events)
    return dataset, values, sites, sds, events, starts, flags


def cls(ev):
    if ev["season"] not in ("early", "late"):
        return None
    return ev["label"] + ("E" if ev["season"] == "early" else "L")


def year_stats(values, sites, sds, e, y, starts):
    anom, refs = fp.anomalies(values, sites, sds, e, y, starts)
    if len(anom) < 3:
        return None
    zs = list(anom.values())
    n_cold = sum(z <= -1 for z in zs)
    return {"M": sum(zs) / len(zs), "n": len(zs), "N": n_cold, "anom": anom, "refs": refs}


def background(values, sites, sds, starts):
    out = {}
    blocked = set()
    for s in starts:
        blocked.update({s, s + 1, s + 2})
    for y in range(*BG_RANGE):
        if y in blocked:
            continue
        r = year_stats(values, sites, sds, y, y, starts)
        if r is not None:
            out[y] = r["M"]
    return out


def pct(bg, m):
    v = list(bg.values())
    return 100.0 * sum(x <= m for x in v) / len(v)


def q(vals, p):
    s = sorted(vals)
    return s[int(p * (len(s) - 1))]


def events_table(values, sites, sds, events, starts, flags):
    rows = []
    for ev in events:
        if ev["role"] not in ("cal", "nomonth"):
            continue
        ev = dict(ev)
        if "--parker1641" in flags and ev["name"] == "Parker":
            ev.update({"year": "1641", "month": "1", "season": "early"})
        if "--vssi3" in flags and ev["vssi_tgs"] != "NA" and float(ev["vssi_tgs"]) < 3.0:
            continue
        e = int(ev["year"])
        r0 = year_stats(values, sites, sds, e, e, starts)
        r1 = year_stats(values, sites, sds, e, e + 1, starts)
        rows.append((ev, cls(ev) if ev["role"] == "cal" else None, r0, r1))
    return rows


def calibrate(argv):
    dataset, values, sites, sds, events, starts, flags = setup(argv)
    bg = background(values, sites, sds, starts)
    bgv = list(bg.values())
    p10 = q(bgv, 0.10)
    print(f"# dataset={dataset} sites={len(values)} flags={' '.join(sorted(flags)) or '-'}")
    print(f"# background years={len(bg)} ({BG_RANGE[0]}-{BG_RANGE[1] - 1}, no eruption start in [Y-2,Y])  "
          f"M: min {min(bgv):+.2f}  p5 {q(bgv, 0.05):+.2f}  p10 {p10:+.2f}  median {statistics.median(bgv):+.2f}")
    print("event\tE\tmonth\tclass\tvssi\tn\tM_E\tpctl_E\tN_E(z<=-1)\tM_E1\tpctl_E1\tcooled_in_E")
    rows = events_table(values, sites, sds, events, starts, flags)
    kept = []
    for ev, c, r0, r1 in rows:
        if r0 is None or r1 is None:
            print(f"{ev['name']}\t{ev['year']}\t{ev['month']}\t{c or '-'}\tDROPPED (coverage)")
            continue
        cooled = r0["M"] <= p10
        print(f"{ev['name']}\t{ev['year']}\t{ev['month']}\t{c or '-'}\t{ev['vssi_tgs']}\t{r0['n']}\t{r0['M']:+.2f}\t"
              f"{pct(bg, r0['M']):5.1f}\t{r0['N']}/{r0['n']}\t{r1['M']:+.2f}\t{pct(bg, r1['M']):5.1f}\t{'yes' if cooled else 'no'}")
        if c:
            kept.append((ev, c, r0, r1))
    print("\n## class summary (M_E, M_E1)")
    for c in CLASSES:
        m0 = [r0["M"] for _, k, r0, _ in kept if k == c]
        m1 = [r1["M"] for _, k, _, r1 in kept if k == c]
        if not m0:
            continue
        nc = sum(v <= p10 for v in m0)
        print(f"{c}: n={len(m0)}  median M_E {statistics.median(m0):+.2f}  range [{min(m0):+.2f}, {max(m0):+.2f}]  "
              f"median M_E1 {statistics.median(m1):+.2f}  cooled in E (<= bg p10): {nc}/{len(m0)}")
    rng = random.Random(SEED)
    for title, subset in (("P1: XE vs all other classes", [k for k in kept]),
                          ("P2: XE vs TE", [k for k in kept if k[1] in ("XE", "TE")])):
        vals = [r0["M"] for _, _, r0, _ in subset]
        labels = ["X" if c == "XE" else "T" for _, c, _, _ in subset]
        gx = [v for v, l in zip(vals, labels) if l == "X"]
        gt = [v for v, l in zip(vals, labels) if l == "T"]
        a = fp.auc(gx, gt)
        _, lacc = fp.loo(vals, labels)
        p_a = p_l = 0
        for _ in range(N_PERM):
            pl = rng.sample(labels, len(labels))
            px = [v for v, l in zip(vals, pl) if l == "X"]
            pt = [v for v, l in zip(vals, pl) if l == "T"]
            if fp.auc(px, pt) >= a:
                p_a += 1
            if fp.loo(vals, pl)[1] >= lacc:
                p_l += 1
        t, acc = fp.best_threshold(vals, labels)
        print(f"\n## {title}  (n XE={len(gx)}, n other={len(gt)})")
        print(f"AUC P(M_E[XE] < M_E[other]) = {a:.3f}   one-sided permutation p = {(p_a + 1) / (N_PERM + 1):.4f}")
        print(f"LOO balanced accuracy = {lacc:.3f}   permutation p = {(p_l + 1) / (N_PERM + 1):.4f}")
        print(f"full-data threshold: XE if M_E < {t:+.3f} (in-sample balanced accuracy {acc:.3f})")
        print(f"Hedges g (XE - other) = {fp.hedges_g(gx, gt):+.2f}")


def target(argv):
    dataset, values, sites, sds, events, starts, flags = setup(argv)
    bg = background(values, sites, sds, starts)
    bgv = list(bg.values())
    p10 = q(bgv, 0.10)
    rows = [k for k in events_table(values, sites, sds, events, starts, flags) if k[1] and k[2] and k[3]]
    res = {y: year_stats(values, sites, sds, UE_E, y, starts) for y in UE_YEARS}
    print(f"# dataset={dataset} target=UE1453 reference years={res[1452]['refs']}")
    print(f"# background: n={len(bg)} min {min(bgv):+.2f} p10 {p10:+.2f} median {statistics.median(bgv):+.2f}")
    for y in UE_YEARS:
        r = res[y]
        print(f"{y}: n={r['n']}  M={r['M']:+.2f}  background pctl={pct(bg, r['M']):.1f}  "
              f"years in background at or below: {sum(v <= r['M'] for v in bgv)}/{len(bgv)}  N(z<=-1)={r['N']}/{r['n']}")
    m52 = res[1452]["M"]
    print("\n## where 1452 falls among each class's eruption-year values (M_E)")
    verdict = {}
    for c in CLASSES:
        vals = [r0["M"] for _, k, r0, _ in rows if k == c]
        k_ = sum(v >= m52 for v in vals)
        p = (k_ + 1) / (len(vals) + 1)
        verdict[c] = "disfavored" if k_ == 0 else "allowed"
        print(f"{c}: n={len(vals)}  values {' '.join(f'{v:+.2f}' for v in sorted(vals))}  "
              f"k(as warm or warmer than 1452)={k_}  p={p:.2f}  -> Jan-Jun 1452 for this class: "
              f"{verdict[c] if c.endswith('E') else 'n/a (late class: E summer precedes eruption)'}")
    state = "cooled" if m52 <= p10 else "normal"
    print(f"\n1452 state: {state} (M_1452 {m52:+.2f} vs background p10 {p10:+.2f})")
    m53 = res[1453]["M"]
    below_all = m53 < min(bgv)
    print(f"1453 below every background year: {below_all} (M_1453 {m53:+.2f}, background min {min(bgv):+.2f})")
    print("\n## verdicts for window.py")
    print(f"VERDICT\tXE_1452\t{verdict['XE']}")
    print(f"VERDICT\tTE_1452\t{verdict['TE']}")
    print(f"VERDICT\tlate_1452\t{'disfavored' if state == 'cooled' else 'allowed'}")
    print(f"VERDICT\tlate_1453\t{'disfavored' if below_all else 'allowed'}")
    print("\n## per-site z (reference 1442-1451)")
    print("site\tlat\tlon\tz1452\tz1453\tz1454")
    for c in sorted(res[1452]["anom"], key=lambda k: -sites[k][0]):
        zz = [res[y]["anom"].get(c) for y in UE_YEARS]
        print(f"{sites[c][2]}\t{sites[c][0]:.1f}\t{sites[c][1]:.1f}\t" +
              "\t".join("NA" if v is None else f"{v:+.2f}" for v in zz))


def gc_km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371.0 * math.asin(min(1.0, math.sqrt(h)))


def sector_of(lon):
    for name, a, b in SECTORS:
        if a <= lon < b:
            return name
    return None


def morans_i(z, W):
    n = len(z)
    m = sum(z) / n
    d = [v - m for v in z]
    s0 = sum(sum(r) for r in W)
    num = sum(W[i][j] * d[i] * d[j] for i in range(n) for j in range(n))
    den = sum(v * v for v in d)
    return (n / s0) * num / den if s0 and den else float("nan")


def lowest_sector(z, secs):
    groups = {}
    for v, s in zip(z, secs):
        if s:
            groups.setdefault(s, []).append(v)
    means = {s: sum(v) / len(v) for s, v in groups.items() if len(v) >= 2}
    s = min(means, key=means.get)
    return s, means[s], means


def spatial(anom, sites, rng, label):
    codes = sorted(anom)
    z = [anom[c] for c in codes]
    pos = [(sites[c][0], sites[c][1]) for c in codes]
    secs = [sector_of(sites[c][1]) for c in codes]
    W = [[1.0 if i != j and gc_km(pos[i], pos[j]) < DIST_KM else 0.0 for j in range(len(z))] for i in range(len(z))]
    I = morans_i(z, W)
    s, m, means = lowest_sector(z, secs)
    nI = nS = 0
    null_I = []
    for _ in range(N_PERM):
        zz = rng.sample(z, len(z))
        Ip = morans_i(zz, W)
        null_I.append(Ip)
        _, mp, _ = lowest_sector(zz, secs)
        if mp <= m:
            nS += 1
    e_I = -1 / (len(z) - 1)
    nI = sum(abs(v - e_I) >= abs(I - e_I) for v in null_I)
    print(f"{label}: sites={len(z)}  Moran's I={I:+.3f} (E[I]={e_I:+.3f})  two-sided p={(nI + 1) / (N_PERM + 1):.4f}  "
          f"lowest sector={s} mean {m:+.2f}  one-sided p={(nS + 1) / (N_PERM + 1):.4f}")
    print("    sector means: " + "  ".join(f"{k} {v:+.2f} (n={secs.count(k)})" for k, v in sorted(means.items())))
    return s, (nS + 1) / (N_PERM + 1)


def regional(argv):
    dataset, values, sites, sds, events, starts, flags = setup(argv)
    rng = random.Random(SEED)
    print(f"# dataset={dataset} distance weights < {DIST_KM:.0f} km; sectors {SECTORS}")
    print("## UE 1453, reference 1442-1451")
    for y in UE_YEARS[:2]:
        r = year_stats(values, sites, sds, UE_E, y, starts)
        spatial(r["anom"], sites, rng, f"{y}")
    print("\n## calibration: lowest sector vs source sector (extratropical events)")
    hits = n = 0
    for ev in events:
        if ev["role"] != "cal" or ev["label"] != "X":
            continue
        e = int(ev["year"])
        if ev["season"] == "early":
            y = e
        else:
            r = fp.event_result(values, sites, sds, e, "select", starts)
            y = r["Y"] if r else e + 1
        r = year_stats(values, sites, sds, e, y, starts)
        src = sector_of(SRC_LON[ev["name"]])
        s, p = spatial(r["anom"], sites, rng, f"{ev['name']} {e} (Y={y}, source sector {src})")
        n += 1
        hits += (s == src)
    print(f"\nlowest sector = source sector in {hits}/{n} extratropical events")


if __name__ == "__main__":
    if len(sys.argv) < 7 or sys.argv[1] not in ("calibrate", "target", "regional"):
        print(__doc__)
        sys.exit(2)
    {"calibrate": calibrate, "target": target, "regional": regional}[sys.argv[1]](sys.argv[2:])

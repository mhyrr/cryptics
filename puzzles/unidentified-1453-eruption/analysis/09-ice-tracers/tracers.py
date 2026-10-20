"""Non-sulfur tracers of volcanic events in NEEM-2011-S1, calibrated on known sources.

usage: python3 -I tracers.py NEEM_TAB [--calibration-only] > results/tracers.txt

NEEM_TAB  PANGAEA.940553 tab file (2 cm CFA, NS1-2011 ages).

The method is the pre-registration in README.md. In short:
  nssS = S - 0.084 Na; background [Y-8, Y-0.5), cleaned once of its own
  outliers; onset = first of 3 consecutive samples above median + 3 sMAD in
  [Y-0.5, Y+2); event interval runs until 3 consecutive samples fall below.
  Ratio residuals: OLS log10 X on log10 Z in the background (dust removed).
  Load anomalies: log10 X minus the background median of its two-month bin.
  Both become robust z against the background, then a 3-sample running mean.
UE 1453 is computed last, after the calibration tests are printed.
"""
import math
import random
import statistics
import sys

S_NA = 0.084
EQ_PER_UG_S = 2 / 32.06  # µEq of H2SO4 per µg S

# eVolv2k v4 rows with a named source (year = ice year). Coordinates are
# approximate vent positions used only for the descriptive distance check.
CAL = [
    # ICE
    (751, "Grimsvotn 751", "ICE", 64.42, -17.33),
    (757, "Katla 757", "ICE", 63.63, -19.05),
    (763, "Katla 763", "ICE", 63.63, -19.05),
    (782, "Grimsvotn 782", "ICE", 64.42, -17.33),
    (823, "Katla 823", "ICE", 63.63, -19.05),
    (877, "Veidivotn 877", "ICE", 64.64, -17.53),
    (939, "Eldgja 939", "ICE", 63.97, -18.60),
    (1477, "Veidivotn 1477", "ICE", 64.64, -17.53),
    (1510, "Hekla 1510", "ICE", 63.98, -19.70),
    (1721, "Katla 1721", "ICE", 63.63, -19.05),
    (1755, "Katla 1755", "ICE", 63.63, -19.05),
    (1766, "Hekla 1766", "ICE", 63.98, -19.70),
    (1783, "Laki 1783", "ICE", 64.07, -18.23),
    (1873, "Grimsvotn 1873", "ICE", 64.42, -17.33),
    (1875, "Askja 1875", "ICE", 65.03, -16.75),
    # NHX
    (452, "Shiveluch 452", "NHX", 56.65, 161.36),
    (853, "Churchill 853", "NHX", 61.38, -141.75),
    (946, "Changbaishan 946", "NHX", 41.99, 128.08),
    (1667, "Tarumae 1667", "NHX", 42.69, 141.38),
    (1707, "Fujisan 1707", "NHX", 35.36, 138.73),
    (1739, "Shikotsu 1739", "NHX", 42.69, 141.38),
    (1831, "Zavaritskii 1831", "NHX", 46.93, 151.95),
    (1853, "Toya 1853", "NHX", 42.54, 140.84),
    (1856, "Komagatake 1856", "NHX", 42.06, 140.68),
    # TROP
    (432, "Ilopango 432", "TROP", 13.67, -89.05),
    (1257, "Samalas 1257", "TROP", -8.42, 116.47),
    (1585, "Colima 1585", "TROP", 19.51, -103.62),
    (1595, "Ruiz 1595", "TROP", 4.89, -75.32),
    (1600, "Huaynaputina 1600", "TROP", -16.61, -70.85),
    (1640, "Parker 1640", "TROP", 6.11, 124.89),
    (1673, "Gamkonora 1673", "TROP", 1.38, 127.53),
    (1815, "Tambora 1815", "TROP", -8.25, 118.00),
    (1822, "Galunggung 1822", "TROP", -7.25, 108.06),
    (1835, "Cosiguina 1835", "TROP", 12.98, -87.57),
    (1861, "Makian 1861", "TROP", 0.32, 127.40),
    (1883, "Krakatau 1883", "TROP", -6.10, 105.42),
]
EXTRA = [(1912, "Katmai 1912 (industrial background; not in calibration)", "NHX", 58.27, -155.16)]
NEEM = (77.45, -51.06)

RATIOS = [("Ce", "Ca"), ("Mn", "Ca"), ("Mn", "Ce"), ("Ce", "Sr")]
LOADS = ["Ce", "Mn", "Ca"]
FEATS = ["r_CeCa", "r_MnCa", "r_MnCe", "r_CeSr", "a_Ce", "a_Mn", "a_Ca", "acid", "cond"]

COLS = {"Cond": "Cond [µS/m]", "Acid": "Acidity [µEq/l]", "Na": "Na [µg/kg]", "S": "S [µg/kg]",
        "Ca": "Ca [µg/kg]", "Mn": "Mn [µg/kg]", "Sr": "Sr [µg/kg]", "Ce": "Ce [µg/kg]"}


def load(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        body, hdr = False, None
        for line in f:
            if line.startswith("*/"):
                body = True
                continue
            if not body:
                continue
            p = line.rstrip("\n").split("\t")
            if hdr is None:
                hdr = p
                continue
            rec = dict(zip(hdr, p))
            r = {"age": float(rec["Age [a AD/CE]"]), "depth": float(rec["Depth ice/snow [m]"])}
            for k, c in COLS.items():
                try:
                    r[k] = float(rec[c])
                except (KeyError, ValueError):
                    r[k] = None
            r["nssS"] = r["S"] - S_NA * r["Na"] if r["S"] is not None and r["Na"] is not None else None
            rows.append(r)
    rows.sort(key=lambda r: r["age"])
    return rows


def rob(xs):
    m = statistics.median(xs)
    d = 1.4826 * statistics.median(abs(x - m) for x in xs)
    return m, d


def lg(v):
    return math.log10(v) if v is not None and v > 0 else None


def running(series):
    """series: list of (age, z). 3-sample centred running mean."""
    out = []
    for i in range(1, len(series) - 1):
        out.append((series[i][0], (series[i - 1][1] + series[i][1] + series[i + 1][1]) / 3))
    return out


def gc_km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(h))


def event(rows, Y, force_onset=None):
    """force_onset: used only by null.py for pseudo-events with no sulfate."""
    bg = [r for r in rows if Y - 8 <= r["age"] < Y - 0.5 and r["nssS"] is not None]
    m, d = rob([r["nssS"] for r in bg])
    bg = [r for r in bg if r["nssS"] <= m + 3 * d]
    m, d = rob([r["nssS"] for r in bg])
    thr = m + 3 * d
    res = {"n_bg": len(bg), "bg_med": m, "thr": thr}
    onset_i = None
    for i, r in enumerate(rows):
        if not (Y - 0.5 <= r["age"] < Y + 2) or i < 1 or i + 3 > len(rows):
            continue
        vals = [rows[j]["nssS"] for j in range(i, i + 3)]
        if all(v is not None and v > thr for v in vals):
            onset_i = i
            break
    if force_onset is not None:
        onset_i = next(i for i, r in enumerate(rows) if r["age"] >= force_onset)
    if onset_i is None:
        res["onset"] = None
        return res
    onset = (rows[onset_i - 1]["age"] + rows[onset_i]["age"]) / 2
    res["onset"], res["depth"] = onset, rows[onset_i]["depth"]
    j, below, end_i = onset_i, 0, onset_i
    while j < len(rows) and rows[j]["age"] <= onset + 3:
        v = rows[j]["nssS"]
        if v is not None and v > thr:
            below, end_i = 0, j
        else:
            below += 1
            if below >= 3:
                break
        j += 1
    ev = rows[onset_i:end_i + 1]
    res["end"] = rows[end_i]["age"]
    res["peak"] = max((r["nssS"] for r in ev if r["nssS"] is not None), default=m)
    res["strength"] = (res["peak"] - m) / (thr - m)

    # acid and conductivity ratios over the event interval
    for key, name, scale in (("Acid", "acid", EQ_PER_UG_S), ("Cond", "cond", 1.0)):
        bgv = [r[key] for r in bg if r[key] is not None]
        pairs = [(r[key], r["nssS"]) for r in ev if r[key] is not None and r["nssS"] is not None]
        if len(bgv) < 20 or len(pairs) < 3:
            res[name] = None
            continue
        mb = statistics.median(bgv)
        dS = sum(p[1] - m for p in pairs)
        dX = sum(p[0] - mb for p in pairs)
        res[name] = dX / (scale * dS) if dS > 0 else None
        res[name + "_cov"] = len(pairs) / len(ev)

    win = [r for r in rows if onset - 1.6 <= r["age"] <= onset + 1.6]

    def zseries(fun, bgfun):
        bvals = [v for v in (bgfun(r) for r in bg) if v is not None]
        if len(bvals) < 20:
            return None
        bm, bd = rob(bvals)
        if bd <= 0:
            return None
        s = [(r["age"], (fun(r) - bm) / bd) for r in win if fun(r) is not None]
        return running(s)

    def pick(rm, signed_abs):
        inw = [z for a, z in rm if onset - 1 <= a <= onset + 1]
        if not inw:
            return None
        return max(inw, key=abs) if signed_abs else max(inw)

    for x, z in RATIOS:
        pts = [(lg(r[z]), lg(r[x])) for r in bg if lg(r[z]) is not None and lg(r[x]) is not None]
        key = "r_%s%s" % (x, z)
        if len(pts) < 20:
            res[key] = None
            continue
        mx = statistics.fmean(p[0] for p in pts)
        my = statistics.fmean(p[1] for p in pts)
        sxx = sum((p[0] - mx) ** 2 for p in pts)
        b = sum((p[0] - mx) * (p[1] - my) for p in pts) / sxx
        a = my - b * mx

        def resid(r, x=x, z=z, a=a, b=b):
            lx, lz = lg(r[x]), lg(r[z])
            return lx - (a + b * lz) if lx is not None and lz is not None else None
        rm = zseries(resid, resid)
        res[key] = pick(rm, True) if rm else None
        res[key + "_slope"] = b

    for x in LOADS:
        bins = {}
        for r in bg:
            v = lg(r[x])
            if v is not None:
                bins.setdefault(int((r["age"] % 1) * 6), []).append(v)
        if len(bins) < 6:
            res["a_" + x] = None
            continue
        bmed = {k: statistics.median(v) for k, v in bins.items()}

        def anom(r, x=x, bmed=bmed):
            v = lg(r[x])
            return v - bmed[int((r["age"] % 1) * 6)] if v is not None else None
        rm = zseries(anom, anom)
        res["a_" + x] = pick(rm, False) if rm else None
        if rm:
            first = next((a for a, z in rm if onset - 1 <= a <= onset + 1 and z > 3), None)
            res["lag_" + x] = first - onset if first is not None else None
    return res


def auc(pos, neg):
    s = 0.0
    for p in pos:
        for q in neg:
            s += 1.0 if p > q else 0.5 if p == q else 0.0
    return s / (len(pos) * len(neg))


def perm_auc(vals, labels, n=10000, seed=1453):
    pos = [v for v, l in zip(vals, labels) if l]
    neg = [v for v, l in zip(vals, labels) if not l]
    obs = auc(pos, neg)
    rng = random.Random(seed)
    lab = list(labels)
    hits = 0
    for _ in range(n):
        rng.shuffle(lab)
        a = auc([v for v, l in zip(vals, lab) if l], [v for v, l in zip(vals, lab) if not l])
        if abs(a - 0.5) >= abs(obs - 0.5) - 1e-12:
            hits += 1
    return obs, (hits + 1) / (n + 1)


def standardise(train, test):
    k = len(train[0])
    cols = []
    for j in range(k):
        vals = [t[j] for t in train if t[j] is not None]
        med = statistics.median(vals)
        mu = statistics.fmean(vals)
        sd = statistics.pstdev(vals) or 1.0
        cols.append((med, mu, sd))

    def f(v):
        return [((x if x is not None else c[0]) - c[1]) / c[2] for x, c in zip(v, cols)]
    return [f(t) for t in train], f(test)


def centroid_predict(trainX, trainY, x):
    best = None
    for cls in sorted(set(trainY)):
        pts = [p for p, y in zip(trainX, trainY) if y == cls]
        c = [statistics.fmean(col) for col in zip(*pts)]
        dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(x, c)))
        if best is None or dist < best[1]:
            best = (cls, dist)
    return best[0]


def loo_bacc(X, Y):
    pred = []
    for i in range(len(X)):
        tr = [X[j] for j in range(len(X)) if j != i]
        ty = [Y[j] for j in range(len(X)) if j != i]
        trs, xs = standardise(tr, X[i])
        pred.append(centroid_predict(trs, ty, xs))
    recalls = []
    for cls in sorted(set(Y)):
        idx = [i for i in range(len(Y)) if Y[i] == cls]
        recalls.append(sum(pred[i] == cls for i in idx) / len(idx))
    return statistics.fmean(recalls), pred


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    adj = [0.0] * len(ps)
    run = 0.0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (len(ps) - rank) * ps[i]))
        adj[i] = run
    return adj


def fmt(v, f="%+.2f"):
    return f % v if v is not None else "  n/a"


def contrast(out, evs, posname, negnames, title, nperm_cls=2000):
    sub = [e for e in evs if e["cls"] == posname or e["cls"] in negnames]
    labels = [e["cls"] == posname for e in sub]
    out.append("== %s: %s (n=%d) vs %s (n=%d) ==" % (title, posname, sum(labels), "+".join(negnames),
                                                    len(labels) - sum(labels)))
    ps, rows = [], []
    for f in FEATS:
        pairs = [(e[f], l) for e, l in zip(sub, labels) if e.get(f) is not None]
        if sum(l for _, l in pairs) < 3 or sum(not l for _, l in pairs) < 3:
            rows.append((f, None, None, len(pairs)))
            ps.append(1.0)
            continue
        a, p = perm_auc([v for v, _ in pairs], [l for _, l in pairs])
        pos = [v for v, l in pairs if l]
        neg = [v for v, l in pairs if not l]
        rows.append((f, a, p, len(pairs), statistics.median(pos), statistics.median(neg)))
        ps.append(p)
    adj = holm(ps)
    out.append("  feature   n   AUC   perm-p  Holm-p   median %s / median other" % posname)
    for r, pa in zip(rows, adj):
        if r[1] is None:
            out.append("  %-8s %3d  too few" % (r[0], r[3]))
        else:
            out.append("  %-8s %3d  %.2f  %.4f  %.4f   %+.2f / %+.2f" % (r[0], r[3], r[1], r[2], pa, r[4], r[5]))
    X = [[e.get(f) for f in FEATS] for e in sub]
    Y = [posname if l else "OTHER" for l in labels]
    bacc, pred = loo_bacc(X, Y)
    rng = random.Random(1453)
    hits = 0
    for _ in range(nperm_cls):
        yy = list(Y)
        rng.shuffle(yy)
        if loo_bacc(X, yy)[0] >= bacc - 1e-12:
            hits += 1
    p = (hits + 1) / (nperm_cls + 1)
    out.append("  nearest-centroid, 9 features, LOO balanced accuracy %.3f; permutation p %.4f (%d shuffles)" % (
        bacc, p, nperm_cls))
    wrong = [e["name"] for e, y, pr in zip(sub, Y, pred) if y != pr]
    out.append("  misclassified: " + (", ".join(wrong) if wrong else "none"))
    verdict = "SEPARATES" if bacc >= 0.75 and p < 0.05 else "DOES NOT SEPARATE"
    out.append("  pre-registered rule (bacc >= 0.75 and p < 0.05): %s" % verdict)
    out.append("")
    return X, Y, verdict


def spearman(x, y):
    def rank(v):
        o = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(o):
            j = i
            while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]:
                j += 1
            for k in range(i, j + 1):
                r[o[k]] = (i + j) / 2
            i = j + 1
        return r
    rx, ry = rank(x), rank(y)
    mx, my = statistics.fmean(rx), statistics.fmean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den if den else float("nan")


def line(e):
    return "  %-20s %-4s onset %8.3f str %5.1f  %s  acid %s cond %s  lagCe %s lagMn %s lagCa %s" % (
        e["name"], e["cls"], e["onset"], e["strength"],
        " ".join("%s %s" % (f, fmt(e.get(f))) for f in FEATS[:7]),
        fmt(e.get("acid")), fmt(e.get("cond")),
        fmt(e.get("lag_Ce")), fmt(e.get("lag_Mn")), fmt(e.get("lag_Ca")))


def main():
    rows = load(sys.argv[1])
    out = ["NEEM-2011-S1 (PANGAEA.940553): %d rows; NEEM at %.2fN %.2fE" % (len(rows), *NEEM), ""]
    evs, dropped = [], []
    for Y, name, cls, la, lo in CAL:
        r = event(rows, Y)
        if r.get("onset") is None:
            dropped.append(name)
            continue
        r.update(name=name, cls=cls, year=Y, dist=gc_km(NEEM, (la, lo)))
        evs.append(r)
    out.append("== Calibration events with a sulfate onset (%d); dropped, no onset: %s ==" % (
        len(evs), ", ".join(dropped) if dropped else "none"))
    for e in evs:
        out.append(line(e))
    out.append("")

    contrast(out, evs, "ICE", ["NHX", "TROP"], "Test 1-3, all events")
    late = [e for e in evs if e["year"] > 1500]
    contrast(out, late, "ICE", ["NHX", "TROP"], "Test 4, events after 1500 only")
    contrast(out, evs, "NHX", ["TROP"], "Test 5, NHX vs TROP")

    out.append("== Lithic timing (first running-mean load z > 3 within onset +/- 1 yr; lag in yr, negative = before sulfate) ==")
    for cls in ("ICE", "NHX", "TROP"):
        for k in ("Ce", "Mn", "Ca"):
            lags = [e.get("lag_" + k) for e in evs if e["cls"] == cls]
            got = [v for v in lags if v is not None]
            out.append("  %-4s %-2s detected %2d/%2d; lags %s" % (
                cls, k, len(got), len(lags), ", ".join("%+.2f" % v for v in sorted(got))))
    out.append("")
    out.append("== Distance check (descriptive): Spearman rho of feature vs vent-NEEM distance, all events ==")
    for f in FEATS:
        pr = [(e["dist"], e[f]) for e in evs if e.get(f) is not None]
        out.append("  %-8s n=%2d rho %+.2f" % (f, len(pr), spearman([p[0] for p in pr], [p[1] for p in pr])))
    out.append("")

    for Y, name, cls, la, lo in EXTRA:
        r = event(rows, Y)
        if r.get("onset") is not None:
            r.update(name=name.split(" (")[0], cls=cls)
            out.append("== Extra, not in calibration: %s ==" % name)
            out.append(line(r))
            out.append("")

    if "--calibration-only" in sys.argv:
        print("\n".join(out))
        return
    # ---- UE 1453, only now ----
    u = event(rows, 1453)
    out.append("== UE 1453 (Y = 1453; computed after the tests above) ==")
    if u.get("onset") is None:
        out.append("  no onset")
    else:
        u.update(name="UE 1453", cls="?")
        out.append(line(u))
        out.append("  event interval %.3f-%.3f; peak nssS %.1f; background n %d" % (u["onset"], u["end"], u["peak"], u["n_bg"]))
        for f in FEATS:
            if u.get(f) is None:
                continue
            ranks = []
            for cls in ("ICE", "NHX", "TROP"):
                vals = [e[f] for e in evs if e["cls"] == cls and e.get(f) is not None]
                below = sum(v < u[f] for v in vals)
                ranks.append("%s %d/%d below" % (cls, below, len(vals)))
            out.append("  %-8s %+.2f   %s" % (f, u[f], "; ".join(ranks)))
        X = [[e.get(f) for f in FEATS] for e in evs]
        x = [u.get(f) for f in FEATS]
        for title, lab in (("ICE vs OTHER", ["ICE" if e["cls"] == "ICE" else "OTHER" for e in evs]),
                           ("ICE / NHX / TROP", [e["cls"] for e in evs])):
            trs, xs = standardise(X, x)
            out.append("  nearest centroid (%s): %s" % (title, centroid_predict(trs, lab, xs)))
        trs, xs = standardise(X, x)
        d = sorted(((math.sqrt(sum((a - b) ** 2 for a, b in zip(xs, t))), e["name"], e["cls"]) for t, e in zip(trs, evs)))
        out.append("  five nearest calibration events: " + "; ".join("%s (%s) %.2f" % (n, c, dd) for dd, n, c in d[:5]))
    print("\n".join(out))


if __name__ == "__main__":
    main()

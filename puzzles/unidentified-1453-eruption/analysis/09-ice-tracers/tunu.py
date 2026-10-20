"""The calibrated tracer test of tracers.py, on TUNU2013 (Arctic Data Center).

usage: python3 -I tunu.py TUNU_CSV [--calibration-only] [--deseason-onset] > results/tunu.txt

--deseason-onset  POST-HOC variant (added after the first TUNU run; README):
                  nssS is replaced by its residual from the median of the same
                  two-month NS1-2011 bin within +/-10 yr, before onset
                  detection and before the per-S ratios.

TUNU_CSV  Tunu13_database_111816_Arctic_Data_Center.csv, doi:10.18739/A2ZD34.

Method: README.md, "Pre-registration, part B". Event detection is the same
code as tracers.py (imported). Missing values are -0.999.
"""
import csv
import math
import os
import random
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tracers as T  # noqa: E402

TUNU = (78.035, -33.88)
COLS = {"Acid": "acid_uEq", "Cond": "cond_rel", "Na": "Na_ng_g", "S": "S_ng_g", "Cl": "Cl_ng_g",
        "Br": "Br_ng_g", "Ca": "Ca_ng_g", "Mn": "Mn_ng_g", "Al": "Al_ng_g", "Ce": "Ce_ng_g",
        "Tl": "Tl_ng_g", "Cd": "Cd_ng_g", "Pb": "Pb_ng_g", "Sr": "Sr_ng_g"}
RATIOS = [("Ce", "Al"), ("Mn", "Al"), ("Ca", "Al")]
LOADS = ["Al", "Ce", "Mn"]
VOLS = ["nssCl", "nssBr", "Tl", "Cd", "Pb"]
FEATS = ["r_CeAl", "r_MnAl", "r_CaAl", "a_Al", "a_Ce", "a_Mn"] + ["v_" + v for v in VOLS] + ["acid"]


def load(path):
    rows = []
    with open(path, encoding="utf-8", errors="replace") as f:
        rd = csv.reader(f)
        hdr = next(rd)
        idx = {k: hdr.index(c) for k, c in COLS.items()}
        for p in rd:
            try:
                age = float(p[0])
            except (ValueError, IndexError):
                continue
            r = {"age": age, "depth": float("nan")}
            for k, i in idx.items():
                try:
                    v = float(p[i])
                    r[k] = None if v == -0.999 else v
                except (ValueError, IndexError):
                    r[k] = None
            na = r["Na"]
            r["nssS"] = r["S"] - T.S_NA * na if r["S"] is not None and na is not None else None
            r["nssCl"] = r["Cl"] - 1.80 * na if r["Cl"] is not None and na is not None else None
            r["nssBr"] = r["Br"] - 0.0062 * na if r["Br"] is not None and na is not None else None
            rows.append(r)
    rows.sort(key=lambda r: r["age"])
    if "--deseason-onset" in sys.argv:
        deseason(rows)
    return rows


def deseason(rows):
    import bisect
    ages = [r["age"] for r in rows]
    raw = [r["nssS"] for r in rows]
    for i, r in enumerate(rows):
        if raw[i] is None:
            continue
        lo, hi = bisect.bisect_left(ages, r["age"] - 10), bisect.bisect_right(ages, r["age"] + 10)
        b = int((r["age"] % 1) * 6)
        same = [raw[j] for j in range(lo, hi) if raw[j] is not None and int((ages[j] % 1) * 6) == b]
        r["nssS"] = raw[i] - statistics.median(same)


def event(rows, Y):
    T.RATIOS, T.LOADS = RATIOS, LOADS
    r = T.event(rows, Y)
    if r.get("onset") is None:
        return r
    on, end, m = r["onset"], r["end"], r["bg_med"]
    bg = [x for x in rows if Y - 8 <= x["age"] < Y - 0.5 and x["nssS"] is not None and x["nssS"] <= r["thr"]]
    ev = [x for x in rows if on <= x["age"] <= end]
    for v in VOLS:
        bgv = [x[v] for x in bg if x[v] is not None]
        pairs = [(x[v], x["nssS"]) for x in ev if x[v] is not None and x["nssS"] is not None]
        if len(bgv) < 15 or len(pairs) < 2:
            r["v_" + v] = None
            continue
        mb = statistics.median(bgv)
        dS = sum(p[1] - m for p in pairs)
        r["v_" + v] = sum(p[0] - mb for p in pairs) / dS if dS > 0 else None
    return r


def to_ranks(train, test):
    cols = list(zip(*train))
    out_tr, out_te = [], []
    meds = []
    for c in cols:
        vals = sorted(v for v in c if v is not None)
        meds.append((vals, statistics.median(vals)))

    def pr(v, vals):
        return (sum(x < v for x in vals) + 0.5 * sum(x == v for x in vals)) / len(vals)

    def f(vec):
        return [pr(v if v is not None else md, vals) for v, (vals, md) in zip(vec, meds)]
    return [f(t) for t in train], f(test)


def loo_bacc(X, Y):
    pred = []
    for i in range(len(X)):
        tr = [X[j] for j in range(len(X)) if j != i]
        ty = [Y[j] for j in range(len(X)) if j != i]
        trs, xs = to_ranks(tr, X[i])
        pred.append(T.centroid_predict(trs, ty, xs))
    rec = []
    for cls in sorted(set(Y)):
        ii = [i for i in range(len(Y)) if Y[i] == cls]
        rec.append(sum(pred[i] == cls for i in ii) / len(ii))
    return statistics.fmean(rec), pred


def contrast(out, evs, pos, negs, title, nperm=2000):
    sub = [e for e in evs if e["cls"] == pos or e["cls"] in negs]
    lab = [e["cls"] == pos for e in sub]
    out.append("== %s: %s (n=%d) vs %s (n=%d) ==" % (title, pos, sum(lab), "+".join(negs), len(lab) - sum(lab)))
    ps, rows = [], []
    for f in FEATS:
        pairs = [(e[f], l) for e, l in zip(sub, lab) if e.get(f) is not None]
        if sum(l for _, l in pairs) < 3 or sum(not l for _, l in pairs) < 3:
            rows.append((f, None, None, len(pairs)))
            ps.append(1.0)
            continue
        a, p = T.perm_auc([v for v, _ in pairs], [l for _, l in pairs])
        rows.append((f, a, p, len(pairs), statistics.median([v for v, l in pairs if l]),
                     statistics.median([v for v, l in pairs if not l])))
        ps.append(p)
    adj = T.holm(ps)
    out.append("  feature    n   AUC   perm-p  Holm-p   median %s / median other" % pos)
    for r, pa in zip(rows, adj):
        if r[1] is None:
            out.append("  %-9s %3d  too few" % (r[0], r[3]))
        else:
            out.append("  %-9s %3d  %.2f  %.4f  %.4f   %+.3g / %+.3g" % (r[0], r[3], r[1], r[2], pa, r[4], r[5]))
    X = [[e.get(f) for f in FEATS] for e in sub]
    Y = [pos if l else "OTHER" for l in lab]
    bacc, pred = loo_bacc(X, Y)
    rng = random.Random(1453)
    hits = 0
    for _ in range(nperm):
        yy = list(Y)
        rng.shuffle(yy)
        if loo_bacc(X, yy)[0] >= bacc - 1e-12:
            hits += 1
    p = (hits + 1) / (nperm + 1)
    out.append("  nearest-centroid on fold ranks, 12 features: LOO balanced accuracy %.3f; permutation p %.4f" % (bacc, p))
    out.append("  misclassified: " + ", ".join(e["name"] for e, y, pr in zip(sub, Y, pred) if y != pr))
    out.append("  pre-registered rule: %s" % ("SEPARATES" if bacc >= 0.75 and p < 0.05 else "DOES NOT SEPARATE"))
    out.append("")


def fmt(v):
    return "%+.3g" % v if v is not None else "n/a"


def line(e):
    return "  %-18s %-4s onset %8.3f str %5.1f n/yr %4.1f | " % (e["name"], e["cls"], e["onset"], e["strength"], e["res"]) + \
        " ".join("%s %s" % (f, fmt(e.get(f))) for f in FEATS) + \
        " | lagAl %s lagCe %s" % (fmt(e.get("lag_Al")), fmt(e.get("lag_Ce")))


def resolution(rows, y):
    return sum(1 for r in rows if y - 4 <= r["age"] < y) / 4


def main():
    rows = load(sys.argv[1])
    out = ["TUNU2013 (doi:10.18739/A2ZD34): %d rows, %.0f-%.0f CE" % (len(rows), rows[0]["age"], rows[-1]["age"])]
    out.append("onset on: " + ("DESEASONALISED nssS (post-hoc variant)" if "--deseason-onset" in sys.argv else "raw nssS (pre-registered)"))
    out.append("")
    evs, dropped = [], []
    for Y, name, cls, la, lo in T.CAL:
        if Y < rows[0]["age"] + 9:
            dropped.append(name + " (out of range)")
            continue
        r = event(rows, Y)
        if r.get("onset") is None:
            dropped.append(name)
            continue
        r.update(name=name, cls=cls, year=Y, res=resolution(rows, Y), dist=T.gc_km(TUNU, (la, lo)))
        evs.append(r)
    out.append("== Calibration events with a sulfate onset (%d); dropped: %s ==" % (len(evs), ", ".join(dropped)))
    for e in evs:
        out.append(line(e))
    out.append("")
    contrast(out, evs, "ICE", ["NHX", "TROP"], "All events")
    contrast(out, [e for e in evs if e["year"] > 1500], "ICE", ["NHX", "TROP"], "Events after 1500 only")
    contrast(out, evs, "NHX", ["TROP"], "NHX vs TROP")
    out.append("== Lithic timing (lag yr; negative = before sulfate) ==")
    for cls in ("ICE", "NHX", "TROP"):
        for k in ("Al", "Ce"):
            lags = [e.get("lag_" + k) for e in evs if e["cls"] == cls]
            got = sorted(v for v in lags if v is not None)
            out.append("  %-4s %-2s detected %2d/%2d; lags %s" % (cls, k, len(got), len(lags), ", ".join("%+.2f" % v for v in got)))
    out.append("")
    if "--calibration-only" in sys.argv:
        print("\n".join(out))
        return
    u = event(rows, 1453)
    out.append("== UE 1453 (computed after the tests above) ==")
    if u.get("onset") is None:
        out.append("  no onset")
    else:
        u.update(name="UE 1453", cls="?", res=resolution(rows, 1453))
        out.append(line(u))
        out.append("  event interval %.3f-%.3f" % (u["onset"], u["end"]))
        for f in FEATS:
            if u.get(f) is None:
                continue
            cells = []
            for cls in ("ICE", "NHX", "TROP"):
                vals = [e[f] for e in evs if e["cls"] == cls and e.get(f) is not None]
                cells.append("%s %d/%d below" % (cls, sum(v < u[f] for v in vals), len(vals)))
            out.append("  %-9s %+.3g   %s" % (f, u[f], "; ".join(cells)))
        X = [[e.get(f) for f in FEATS] for e in evs]
        x = [u.get(f) for f in FEATS]
        trs, xs = to_ranks(X, x)
        for title, lab in (("ICE vs OTHER", ["ICE" if e["cls"] == "ICE" else "OTHER" for e in evs]),
                           ("ICE / NHX / TROP", [e["cls"] for e in evs])):
            out.append("  nearest centroid (%s): %s" % (title, T.centroid_predict(trs, lab, xs)))
        d = sorted((math.sqrt(sum((a - b) ** 2 for a, b in zip(xs, t))), e["name"], e["cls"]) for t, e in zip(trs, evs))
        out.append("  five nearest: " + "; ".join("%s (%s) %.2f" % (n, c, dd) for dd, n, c in d[:5]))
    print("\n".join(out))


if __name__ == "__main__":
    main()

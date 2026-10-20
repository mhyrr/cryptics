"""Post-hoc null for the lithic features of tracers.py (added after the first run).

usage: python3 -I null.py NEEM_TAB EVOLV2K_V4_TAB > results/null.txt
       python3 -I null.py TUNU_CSV EVOLV2K_V4_TAB --tunu > results/null_tunu.txt

Question: is a lithic feature at an eruption larger than the same statistic in
a window with no eruption? Pseudo-events: every year Y in 200-1890 with no
eVolv2k v4 row (Greenland deposition > 0) in [Y-9, Y+3]. The onset is forced
to Y + 0.5. Same background and window rules as tracers.py. A calibration
event "has a lithic excess" in a feature if it beats the null 95th percentile.
"""
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tracers as T  # noqa: E402

LITH = ["r_CeCa", "r_MnCa", "r_MnCe", "r_CeSr", "a_Ce", "a_Mn", "a_Ca"]


def evolv_years(path):
    ys = []
    body = False
    hdr = False
    for line in open(path, encoding="utf-8"):
        if line.startswith("*/"):
            body = True
            continue
        if not body:
            continue
        if not hdr:
            hdr = True
            continue
        p = line.rstrip("\n").split("\t")
        try:
            if float(p[5]) > 0:
                ys.append(int(p[0]))
        except (ValueError, IndexError):
            pass
    return ys


def pct(v, null):
    return 100 * sum(x < v for x in null) / len(null)


def main():
    global LITH
    load, event = T.load, T.event
    if "--tunu" in sys.argv:
        import tunu as U
        LITH = ["r_CeAl", "r_MnAl", "r_CaAl", "a_Al", "a_Ce", "a_Mn"]
        load = U.load
        T.RATIOS, T.LOADS = U.RATIOS, U.LOADS
    rows = load(sys.argv[1])
    ev_years = evolv_years(sys.argv[2])
    pseudo = [Y for Y in range(200, 1891) if not any(Y - 9 <= e <= Y + 3 for e in ev_years)]
    null = {f: [] for f in LITH}
    lagnull = {k: 0 for k in T.LOADS}
    n = 0
    for Y in pseudo:
        if not any(abs(r["age"] - (Y + 0.5)) < 0.15 for r in rows if r["Ce"] is not None):
            continue
        r = T.event(rows, Y, force_onset=Y + 0.5)
        if r.get("onset") is None:
            continue
        n += 1
        for f in LITH:
            if r.get(f) is not None:
                null[f].append(abs(r[f]) if f.startswith("r_") else r[f])
        for k in lagnull:
            if r.get("lag_" + k) is not None:
                lagnull[k] += 1
    out = ["Pseudo-events: %d years (of %d candidates) with no eVolv2k event in [Y-9, Y+3]" % (n, len(pseudo)), ""]
    out.append("Null 95th percentile (|z| for ratio residuals, z for loads):")
    p95 = {}
    for f in LITH:
        v = sorted(null[f])
        p95[f] = v[int(0.95 * len(v))]
        out.append("  %-7s n=%d  median %.2f  p95 %.2f" % (f, len(v), statistics.median(v), p95[f]))
    out.append("Null rate of a load z>3 crossing in the +/-1 yr window: " + ", ".join(
        "%s %.0f%%" % (k, 100 * v / n) for k, v in lagnull.items()))
    out.append("")
    evs = []
    for Y, name, cls, la, lo in T.CAL:
        if Y < rows[0]["age"] + 9:
            continue
        r = T.event(rows, Y)
        if r.get("onset") is not None:
            r.update(name=name, cls=cls)
            evs.append(r)
    u = T.event(rows, 1453)
    u.update(name="UE 1453", cls="?")
    out.append("Per event: null percentile of each lithic feature (* = above p95)")
    out.append("  %-18s %-4s " % ("event", "cls") + " ".join("%8s" % f for f in LITH) + "   n>p95")
    for e in evs + [u]:
        cells, k = [], 0
        for f in LITH:
            v = e.get(f)
            if v is None:
                cells.append("%8s" % "n/a")
                continue
            vv = abs(v) if f.startswith("r_") else v
            star = "*" if vv > p95[f] else " "
            k += star == "*"
            cells.append("%7.0f%s" % (pct(vv, null[f]), star))
        out.append("  %-18s %-4s " % (e["name"], e["cls"]) + " ".join(cells) + "   %d" % k)
    out.append("")
    out.append("Share of events above null p95, by class:")
    for cls in ("ICE", "NHX", "TROP"):
        sub = [e for e in evs if e["cls"] == cls]
        cells = []
        for f in LITH:
            vals = [e[f] for e in sub if e.get(f) is not None]
            k = sum((abs(v) if f.startswith("r_") else v) > p95[f] for v in vals)
            cells.append("%s %d/%d" % (f, k, len(vals)))
        out.append("  %-4s " % cls + "; ".join(cells))
    print("\n".join(out))


if __name__ == "__main__":
    main()

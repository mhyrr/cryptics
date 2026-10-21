"""Regional-to-Greenland sulfate ratio test (pre-registered in README Step 2).

Usage:
  python3 -I regional.py DATADIR events.tsv evolv2k_v4.tab sigl2015_t47_sheet2.tsv [--classify]

Without --classify only the calibration events are scored (target years are
never read). With --classify the targets 1453 and 1458 are scored too.
"""
import math
import random
import statistics as st
import sys
from collections import defaultdict

WIN = 3          # event window +/- yr
BG_IN, BG_OUT = 4, 20
NA_RATIO = 0.252
TARGET_WIN = {1453: (1450, 1455), 1458: (1456, 1461)}
TARGET_BG_EXCL = (1450, 1461)
CONTAM_G = 5.0


def read_noaa(path, ycol, so4col, nacol):
    txt = open(path, encoding="latin-1").read().replace("\r\n", "\n").replace("\r", "\n")
    rows = [l.split("\t") for l in txt.split("\n") if l and not l.startswith("#")]
    for i, r in enumerate(rows):
        h = [c.strip() for c in r]
        if ycol in h:
            break
    jy, js = h.index(ycol), h.index(so4col)
    jn = h.index(nacol) if nacol else None
    bins = defaultdict(list)
    for r in rows[i + 1:]:
        try:
            y = float(r[jy]); s = float(r[js])
            v = s - NA_RATIO * float(r[jn]) if jn is not None else s
        except (ValueError, IndexError):
            continue
        bins[math.floor(y)].append(v)
    return {y: st.mean(v) for y, v in bins.items()}


CORES = {
    "Begguya (Denali) DEN-13B [primary]": ("osterberg2017-den13b.txt", "avg_year", "IC_SO4-2", "IC_Na+"),
    "Eclipse core 2 [secondary; 1453-tied dating; leak]": ("eclipse2002core2ion.txt", "year", "SO4", "Na"),
    "Mt Logan PR Col 2-yr [secondary; total SO4; leak]": ("mtlogan2008-2yr-noaa.txt", "age_CE", "SO4^2-", None),
}


def all_greenland_events(evolv, sigl):
    """(year, location) for every eVolv2k / Sigl2015 event with G >= CONTAM_G."""
    ev = []
    lines = open(evolv, encoding="utf-8").read().split("\n")
    k = [i for i, l in enumerate(lines) if l.startswith("*/")][0]
    for l in lines[k + 2:]:
        c = l.split("\t")
        if len(c) < 11:
            continue
        try:
            y, g = int(c[0]), float(c[5])
        except ValueError:
            continue
        if g >= CONTAM_G:
            ev.append((y, c[10].strip()))
    for l in open(sigl, encoding="utf-8").read().split("\n")[2:]:
        c = l.split("\t")
        try:
            y = int(float(c[0])); g = float(c[2])
        except (ValueError, IndexError):
            continue
        if y > 1890 and g >= CONTAM_G:
            ev.append((y, "Sigl2015 class " + c[1].strip()))
    return ev


def read_events(path):
    out = []
    for l in open(path, encoding="utf-8"):
        if l.startswith("#") or l.startswith("year\t") or not l.strip():
            continue
        y, cl, name, g, src = l.rstrip("\n").split("\t")
        out.append((int(y), cl, name, float(g)))
    return out


def contaminated(cal, allev, cal_by_year):
    y, cl, name, _ = cal
    hits = []
    for oy, loc in allev:
        if oy == y or abs(oy - y) > WIN:
            continue
        ocl = cal_by_year.get(oy)
        if ocl == cl:
            continue
        hits.append(f"{oy} {loc or 'N/A'}")
    return hits


def excess(series, E, win=None, bg_excl=None):
    lo, hi = win if win else (E - WIN, E + WIN)
    vals = [series[y] for y in range(lo, hi + 1) if y in series]
    bg = []
    for y in list(range(E - BG_OUT, E - BG_IN + 1)) + list(range(E + BG_IN, E + BG_OUT + 1)):
        if bg_excl and bg_excl[0] <= y <= bg_excl[1]:
            continue
        if y in series:
            bg.append(series[y])
    if not vals or len(bg) < 8:
        return None
    med = st.median(bg)
    mad = st.median([abs(b - med) for b in bg]) * 1.4826
    if mad <= 0:
        return None
    peak = max(vals)
    py = [y for y in range(lo, hi + 1) if y in series and series[y] == peak][0]
    return (peak - med) / mad, py, len(vals), len(bg)


def auc(pos, neg):
    if not pos or not neg:
        return float("nan")
    s = 0.0
    for p in pos:
        for n in neg:
            s += 1.0 if p > n else 0.5 if p == n else 0.0
    return s / (len(pos) * len(neg))


def perm_p(pos, neg, n=10000, seed=15):
    obs = auc(pos, neg)
    allv = pos + neg
    rng = random.Random(seed)
    k = 0
    for _ in range(n):
        rng.shuffle(allv)
        if auc(allv[:len(pos)], allv[len(pos):]) >= obs:
            k += 1
    return (k + 1) / (n + 1)


def youden(pos, neg):
    best = (-1, None)
    for t in sorted(set(pos + neg)):
        tpr = sum(p > t for p in pos) / len(pos)
        fpr = sum(n > t for n in neg) / len(neg)
        # cut between t and the next value: classify > t as positive
        if tpr - fpr > best[0]:
            best = (tpr - fpr, t)
    return best


def main():
    datadir, evpath, evolv, sigl = sys.argv[1:5]
    classify = "--classify" in sys.argv
    events = read_events(evpath)
    cal = [e for e in events if e[1] != "TARGET"]
    cal_by_year = {e[0]: e[1] for e in cal}
    allev = all_greenland_events(evolv, sigl)

    print("== Contamination drops (other G>=5 event within +/-3 yr, different/unknown class)")
    keep = []
    for e in cal:
        h = contaminated(e, allev, cal_by_year)
        if h:
            print(f"  drop {e[0]} {e[1]} {e[2]}: {', '.join(h)}")
        else:
            keep.append(e)
    print("  kept per class:", {c: sum(1 for e in keep if e[1] == c) for c in ("NP", "IS", "TR")})

    for core, (fn, yc, sc, nc) in CORES.items():
        s = read_noaa(f"{datadir}/{fn}", yc, sc, nc)
        print(f"\n== {core}  ({fn}; years {min(s)}-{max(s)})")
        L = {"NP": [], "IS": [], "TR": []}
        Lpre = {"NP": [], "IS": [], "TR": []}
        print("  year class name                          G      z    peakyr  nwin nbg   L")
        for y, cl, name, g in keep:
            r = excess(s, y)
            if r is None:
                print(f"  {y} {cl} {name[:30]:30s} {g:6.1f}   no coverage")
                continue
            z, py, nw, nb = r
            l = math.log10(max(z, 1.0)) - math.log10(g)
            L[cl].append(l)
            if y < 1800:
                Lpre[cl].append(l)
            print(f"  {y} {cl} {name[:30]:30s} {g:6.1f} {z:6.2f}  {py}  {nw:3d} {nb:3d}  {l:+.3f}")
        pos, neg = L["NP"], L["IS"] + L["TR"]
        a = auc(pos, neg); p = perm_p(pos, neg) if pos and neg else float("nan")
        a_is = auc(L["NP"], L["IS"]); p_is = perm_p(L["NP"], L["IS"]) if L["NP"] and L["IS"] else float("nan")
        a_pre = auc(Lpre["NP"], Lpre["IS"] + Lpre["TR"])
        n = {c: len(v) for c, v in L.items()}
        print(f"  n scored: {n}")
        print(f"  AUC NP vs IS+TR = {a:.3f}  perm p = {p:.4f}")
        print(f"  AUC NP vs IS    = {a_is:.3f}  perm p = {p_is:.4f}")
        print(f"  AUC NP vs IS+TR, pre-1800 only = {a_pre:.3f}  n = { {c: len(v) for c, v in Lpre.items()} }")
        for c in L:
            if L[c]:
                print(f"  class {c}: median L {st.median(L[c]):+.3f}, range {min(L[c]):+.3f} .. {max(L[c]):+.3f}")
        gate = a >= 0.80 and p <= 0.05 and min(n.values()) >= 3
        j, t = youden(pos, neg) if pos and neg else (float("nan"), None)
        print(f"  GATE {'PASS' if gate else 'FAIL'}  (Youden J {j:.2f} at L > {t})")
        if not classify:
            continue
        print("  -- targets --")
        res = {}
        for y, cl, name, g in [e for e in events if e[1] == "TARGET"]:
            r = excess(s, y, TARGET_WIN[y], TARGET_BG_EXCL)
            if r is None:
                print(f"  {y} no coverage"); continue
            z, py, nw, nb = r
            l = math.log10(max(z, 1.0)) - math.log10(g)
            res[y] = (z, py, l)
            pct = {c: (100 * sum(v < l for v in L[c]) / len(L[c]) if L[c] else float('nan')) for c in L}
            verdict = ("NP-like" if l > t else "not NP-like") if gate else "unclassified (gate failed)"
            print(f"  {y} {name}: G {g} z {z:.2f} peak yr {py} nwin {nw} nbg {nb} L {l:+.3f}  "
                  f"pct NP {pct['NP']:.0f} IS {pct['IS']:.0f} TR {pct['TR']:.0f}  -> {verdict}")
        # merged-peak check over the joint window
        joint = {yy: s[yy] for yy in range(1450, 1462) if yy in s}
        if joint:
            m = max(joint, key=joint.get)
            print(f"  joint 1450-1461 maximum year: {m}")


if __name__ == "__main__":
    main()

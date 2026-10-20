"""Experiment 12: Alaska near-field tree-ring test for Aniakchak Half Cone and UE 1453.

Standard library only. Method fixed in README.md ("Pre-registration").
Anomaly code is imported from 04's fingerprint.py by file path, unchanged
(site_sd, anomalies, exclusion_years). The group-difference statistic,
background and permutation tests are written here, after 08's pattern.

Usage
  python3 -I nearfield.py depth     SITES RWL_DIR
  python3 -I nearfield.py calibrate SITES RWL_DIR EVENTS EVOLV2K
  python3 -I nearfield.py target    SITES RWL_DIR EVENTS EVOLV2K   (not run: gate failed)
  python3 -I nearfield.py posthoc   SITES RWL_DIR EVENTS EVOLV2K   (not pre-registered)
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
MIN_SERIES = 3
MIN_SITES = 3
WIN = 31
MIN_WIN = 15
BG_RANGE = (1500, 1986)
VOLC = {"Novarupta": (58.27, -155.16), "Aniakchak": (56.9, -158.2), "Spurr": (61.30, -152.25),
        "Augustine": (59.36, -153.43), "Redoubt": (60.49, -152.74), "Okmok": (53.43, -168.13)}


def gc_km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371.0 * math.asin(math.sqrt(h))


# ---------------------------------------------------------------- Tucson .rwl

def read_rwl(path):
    """Return {series_id: {year: width}} from a Tucson-format decadal file."""
    out = {}
    for line in open(path, encoding="latin-1"):
        line = line.rstrip("\r\n")
        if len(line) < 13:
            continue
        sid, ystr = line[:8].strip(), line[8:12]
        try:
            y0 = int(ystr)
        except ValueError:
            continue
        rest = line[12:]
        vals = []
        ok = True
        for i in range(0, len(rest), 6):
            f = rest[i:i + 6].strip()
            if not f:
                continue
            try:
                vals.append(int(f))
            except ValueError:
                ok = False
                break
        if not ok or not vals:
            continue
        s = out.setdefault(sid, {})
        for k, v in enumerate(vals):
            if v in (999, -9999):
                break
            if v < 0:
                continue
            s[y0 + k] = float(v)
    return {k: v for k, v in out.items() if len(v) >= MIN_WIN}


def index_series(s):
    ys = sorted(s)
    out = {}
    h = WIN // 2
    for y in ys:
        w = [s[k] for k in range(y - h, y + h + 1) if k in s]
        if len(w) < MIN_WIN:
            continue
        m = sum(w) / len(w)
        if m > 0:
            out[y] = s[y] / m
    return out


def site_chronology(raw):
    """Mean index over series; years with >= MIN_SERIES series. Also depth and zero-ring counts."""
    idx = [index_series(s) for s in raw.values()]
    years = sorted({y for s in idx for y in s})
    chron, depth, zeros = {}, {}, {}
    for y in years:
        v = [s[y] for s in idx if y in s]
        depth[y] = len(v)
        zeros[y] = sum(1 for s in raw.values() if s.get(y) == 0.0)
        if len(v) >= MIN_SERIES:
            chron[y] = sum(v) / len(v)
    return chron, depth, zeros, len(raw)


def load(sites_path, rwl_dir):
    sites = {}
    for r in fp._rows(sites_path):
        r["lat"], r["lon"] = float(r["lat"]), float(r["lon"])
        sites[r["code"]] = r
    # Deviation 1: composites (e.g. AK096) repeat series from other files.
    # In sites.tsv order, a series identical to one already used is dropped.
    data, seen, dropped = {}, set(), {}
    for code in sites:
        raw = read_rwl(os.path.join(rwl_dir, code.lower() + ".rwl"))
        keep = {}
        for sid, s in raw.items():
            sig = tuple(sorted(s.items()))
            if sig in seen:
                dropped[code] = dropped.get(code, 0) + 1
                continue
            seen.add(sig)
            keep[sid] = s
        data[code] = site_chronology(keep)
    load.dropped = dropped
    return sites, data


# ---------------------------------------------------------------- statistic

def zmap(values, sds, e, y, starts):
    # fp.anomalies expects `sites` only for membership.
    anom, refs = fp.anomalies(values, {k: 1 for k in values}, sds, e, y, starts)
    return anom, refs


def group_mean(anom, codes):
    v = [anom[c] for c in codes if c in anom]
    return (sum(v) / len(v), len(v)) if len(v) >= MIN_SITES else (None, len(v))


def dstat(values, sds, near, ctrl, e, resp, starts):
    """D(Y) = mean z(near) - mean z(control) for each Y in resp."""
    out = []
    for y in resp:
        anom, refs = zmap(values, sds, e, y, starts)
        mn, nn = group_mean(anom, near)
        mc, nc = group_mean(anom, ctrl)
        if mn is None or mc is None:
            return None
        out.append({"Y": y, "D": mn - mc, "near": mn, "ctrl": mc, "nn": nn, "nc": nc, "anom": anom, "refs": refs})
    return out


def background(values, sds, near, ctrl, starts):
    blocked = set()
    for s in starts:
        blocked.update({s, s + 1, s + 2})
    bg = {}
    for y in range(*BG_RANGE):
        if y in blocked or y + 1 in blocked:
            continue
        r = dstat(values, sds, near, ctrl, y, (y, y + 1), starts)
        if r is not None:
            bg[y] = (min(x["D"] for x in r), max(x["D"] for x in r))
    return bg


def pct_low(vals, x):
    return 100.0 * sum(v <= x for v in vals) / len(vals)


def q(vals, p):
    s = sorted(vals)
    return s[int(p * (len(s) - 1))]


def distance_slope(anom_min, sites, src):
    """OLS slope of per-site z on distance (z per 100 km) with permutation p (two-sided)."""
    codes = [c for c in anom_min]
    x = [gc_km(src, (sites[c]["lat"], sites[c]["lon"])) / 100.0 for c in codes]
    yv = [anom_min[c] for c in codes]

    def slope(xs, ys):
        mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
        sxx = sum((a - mx) ** 2 for a in xs)
        return sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / sxx
    b = slope(x, yv)
    rng = random.Random(SEED)
    k = 0
    for _ in range(N_PERM):
        if abs(slope(x, rng.sample(yv, len(yv)))) >= abs(b):
            k += 1
    return b, (k + 1) / (N_PERM + 1), len(codes)


def setup(argv):
    sites_path, rwl_dir, ev_path, evolv = argv[:4]
    sites, data = load(sites_path, rwl_dir)
    values = {c: d[0] for c, d in data.items()}
    sds = {c: fp.site_sd(s) for c, s in values.items()}
    events = list(fp._rows(ev_path))
    _, starts = fp.exclusion_years(evolv, events)
    groups = {g: [c for c, r in sites.items() if r["group"] == g] for g in ("band", "close1912", "control")}
    return sites, data, values, sds, events, starts, groups


# ---------------------------------------------------------------- commands

def depth(argv):
    sites, data = load(argv[0], argv[1])
    print(f"# duplicate series dropped (identical to a series in an earlier site): {load.dropped}")
    print("code\tgroup\tkm_aniakchak\tseries\tfirst_year_depth>=3\tdepth1452\tdepth1453\tdepth1454\tzeros1453\tzeros1454\tdepth1912\tzeros1912\tzeros1913")
    for c, r in sites.items():
        chron, d, z, n = data[c]
        f3 = min(chron) if chron else "NA"
        print(f"{c}\t{r['group']}\t{r['km_aniakchak']}\t{n}\t{f3}\t{d.get(1452, 0)}\t{d.get(1453, 0)}\t{d.get(1454, 0)}\t"
              f"{z.get(1453, 0)}\t{z.get(1454, 0)}\t{d.get(1912, 0)}\t{z.get(1912, 0)}\t{z.get(1913, 0)}")


def report_event(name, e, resp, src, values, sds, groups, starts, sites, bgs):
    for g in ("band", "close1912"):
        r = dstat(values, sds, groups[g], groups["control"], e, resp, starts)
        if r is None:
            print(f"{name}\t{e}\t{g}\tNA (coverage)")
            continue
        dmin = min(x["D"] for x in r)
        dmax = max(x["D"] for x in r)
        bmin = [v[0] for v in bgs[g].values()]
        bmax = [v[1] for v in bgs[g].values()]
        parts = "  ".join(f"{x['Y']}: near {x['near']:+.2f} (n{x['nn']}) ctrl {x['ctrl']:+.2f} (n{x['nc']}) D {x['D']:+.2f}" for x in r)
        print(f"{name}\t{e}\t{g}\tD_min {dmin:+.2f} pctl {pct_low(bmin, dmin):5.1f}\t"
              f"D_max {dmax:+.2f} pctl_high {100.0 * sum(v >= dmax for v in bmax) / len(bmax):5.1f}\t{parts}")
    # distance regression over all sites with z in every response year
    anoms = [zmap(values, sds, e, y, starts)[0] for y in resp]
    common = set(anoms[0])
    for a in anoms[1:]:
        common &= set(a)
    amin = {c: min(a[c] for a in anoms) for c in common}
    if len(amin) >= 6:
        b, p, n = distance_slope(amin, sites, src)
        print(f"{name}\t{e}\tdistance slope of min-z on km from source: {b:+.3f} z/100 km  two-sided perm p {p:.4f}  n {n}")
    return amin


def calibrate(argv):
    sites, data, values, sds, events, starts, groups = setup(argv)
    bgs = {g: background(values, sds, groups[g], groups["control"], starts) for g in ("band", "close1912")}
    for g, bg in bgs.items():
        bmin = [v[0] for v in bg.values()]
        print(f"# background {g}: n years {len(bg)} ({min(bg)}-{max(bg)})  D_min p5 {q(bmin, 0.05):+.2f}  p10 {q(bmin, 0.10):+.2f}  median {statistics.median(bmin):+.2f}")
    print("event\tE\tgroup\tsuppression\trelease\tdetail")
    for ev in events:
        if ev["role"] != "cal":
            continue
        e = int(ev["year"])
        resp = (e + 1, e + 2) if ev.get("resp_shift") == "1" else (e, e + 1)
        src = VOLC[ev["volcano"]]
        amin = report_event(ev["name"], e, resp, src, values, sds, groups, starts, sites, bgs)
        if ev["name"] == "Novarupta":
            print("\n## Novarupta per-site min z (1912, 1913), sorted by distance from Novarupta")
            for c in sorted(amin, key=lambda c: gc_km(src, (sites[c]["lat"], sites[c]["lon"]))):
                print(f"{c}\t{sites[c]['group']}\t{gc_km(src, (sites[c]['lat'], sites[c]['lon'])):.0f} km\t{amin[c]:+.2f}")
            print()
    bmin = [v[0] for v in bgs["band"].values()]
    nov = dstat(values, sds, groups["band"], groups["control"], 1912, (1912, 1913), starts)
    dmin = min(x["D"] for x in nov)
    det = dmin <= q(bmin, 0.05)
    print(f"\nRULE band detects Novarupta (D_min <= background p5 {q(bmin, 0.05):+.2f}): {det}  (D_min {dmin:+.2f})")


def target(argv):
    sites, data, values, sds, events, starts, groups = setup(argv)
    bg = background(values, sds, groups["band"], groups["control"], starts)
    bmin = [v[0] for v in bg.values()]
    print(f"# background band: n years {len(bg)}  D_min p5 {q(bmin, 0.05):+.2f}")
    r = dstat(values, sds, groups["band"], groups["control"], 1452, (1453, 1454), starts)
    print(f"# reference years {r[0]['refs']}")
    for x in r:
        print(f"{x['Y']}: near {x['near']:+.2f} (n{x['nn']})  control {x['ctrl']:+.2f} (n{x['nc']})  D {x['D']:+.2f}")
    dmin = min(x["D"] for x in r)
    print(f"D_min {dmin:+.2f}  background pctl {pct_low(bmin, dmin):.1f}  signal (<= p5): {dmin <= q(bmin, 0.05)}")
    amin = {c: min(x["anom"][c] for x in r if c in x["anom"]) for c in set(r[0]["anom"]) & set(r[1]["anom"])}
    print("\n## per-site z (1453, 1454, min), by distance from Aniakchak")
    for c in sorted(amin, key=lambda c: float(sites[c]["km_aniakchak"])):
        print(f"{c}\t{sites[c]['region']}\t{sites[c]['km_aniakchak']} km\t{r[0]['anom'].get(c, float('nan')):+.2f}\t"
              f"{r[1]['anom'].get(c, float('nan')):+.2f}\t{amin[c]:+.2f}")
    b, p, n = distance_slope(amin, sites, VOLC["Aniakchak"])
    print(f"distance slope (min z on km from Aniakchak): {b:+.3f} z/100 km  two-sided perm p {p:.4f}  n {n}")
    # reverse test: lowest region mean
    regs = {}
    for c in amin:
        regs.setdefault(sites[c]["region"], []).append(c)
    regs = {k: v for k, v in regs.items() if len(v) >= 2}

    def lowest(zs):
        best = None
        for k, cs in regs.items():
            m = sum(zs[c] for c in cs) / len(cs)
            if best is None or m < best[1]:
                best = (k, m)
        return best
    obs = lowest(amin)
    codes = list(amin)
    rng = random.Random(SEED)
    k = 0
    for _ in range(N_PERM):
        sh = dict(zip(codes, rng.sample([amin[c] for c in codes], len(codes))))
        if lowest(sh)[1] <= obs[1]:
            k += 1
    print("\n## reverse test: region means of min z (1453, 1454)")
    for reg, cs in regs.items():
        print(f"{reg}\tn {len(cs)}\tmean {sum(amin[c] for c in cs) / len(cs):+.2f}")
    print(f"lowest region {obs[0]} mean {obs[1]:+.2f}  one-sided perm p {(k + 1) / (N_PERM + 1):.4f}")


def posthoc(argv):
    """NOT pre-registered. Kodiak/Afognak trio (146-183 km from Novarupta) minus control, 1912/13."""
    sites, data, values, sds, events, starts, groups = setup(argv)
    kod = ["AK014", "AK17", "AK108"]
    bg = background(values, sds, kod, groups["control"], starts)
    bmin = [v[0] for v in bg.values()]
    print(f"# POST HOC (not pre-registered). near = {kod}; background n {len(bg)} ({min(bg)}-{max(bg)}) "
          f"p5 {q(bmin, 0.05):+.2f} p1 {q(bmin, 0.01):+.2f}")
    r = dstat(values, sds, kod, groups["control"], 1912, (1912, 1913), starts)
    dmin = min(x["D"] for x in r)
    for x in r:
        print(f"{x['Y']}: near {x['near']:+.2f} control {x['ctrl']:+.2f} D {x['D']:+.2f}")
    print(f"D_min {dmin:+.2f}  background pctl {pct_low(bmin, dmin):.1f}  rank {sum(v <= dmin for v in bmin)}/{len(bmin)}")
    print("lowest 5 background years:", " ".join(f"{y}:{bg[y][0]:+.2f}" for y in sorted(bg, key=lambda y: bg[y][0])[:5]))
    # near-only (no control subtraction): Kodiak trio raw mean z
    for y in (1912, 1913, 1914):
        a, _ = zmap(values, sds, 1912, y, starts)
        print(f"Kodiak trio mean z {y}: {sum(a[c] for c in kod) / 3:+.2f}  ({' '.join(f'{c} {a[c]:+.2f}' for c in kod)})")


if __name__ == "__main__":
    cmd = sys.argv[1]
    {"depth": depth, "calibrate": calibrate, "target": target, "posthoc": posthoc}[cmd](sys.argv[2:])

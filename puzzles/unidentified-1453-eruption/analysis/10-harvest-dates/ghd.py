"""10 -- grape-harvest dates and UE 1453. Pre-registration in README.md.

Usage:
  python3 -I ghd.py calibrate LABBE_TXT EVENTS_TSV EVOLV2K_TAB
  python3 -I ghd.py target    LABBE_TXT EVENTS_TSV EVOLV2K_TAB
  python3 -I ghd.py fillcheck LABBE_TXT CHUINE_TXT
  python3 -I ghd.py secondary CHUINE_TXT DAUX_TXT EVENTS_TSV EVOLV2K_TAB

Standard library only. Positive anomaly = later harvest = colder season.
"""
import random
import re
import statistics
import sys
from collections import Counter

SEED = 1453
N_DRAWS = 10000
VSSI_EXCLUDE = 3.0
LARGE_VSSI = 8.0
VEI6_NO_VSSI = {"Novarupta", "Santa Maria", "Pinatubo"}   # GVP VEI 6, no eVolv2k value
N_REF, MIN_REF, LOOKBACK = 10, 7, 25
BG_RANGE = (1364, 2018)
B_INTERCEPT = 31.59          # Labbe 2019 B_linear: T = 31.59 - 0.061 * GHD
UE_E = 1452
UE_YEARS = (1452, 1453, 1454)
CHECK = ("Kuwae/UE1458", 1458)


# ------------------------------------------------------------------ loading

def load_labbe(path):
    """Return {year: T_Blinear} and the one-day step b."""
    lines = open(path, encoding="latin-1").read().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("YEAR"))
    t = {}
    for l in lines[start + 1:]:
        p = l.split("\t")
        if not p[0].strip().isdigit():
            continue
        if p[7].strip() != "NA":
            t[int(p[0])] = float(p[7])
    vals = sorted(set(round(v, 6) for v in t.values()))
    steps = Counter(round(b - a, 5) for a, b in zip(vals, vals[1:]))
    b = steps.most_common(1)[0][0]
    return t, b, steps


def beaune_ghd(path):
    t, b, steps = load_labbe(path)
    g = {y: (B_INTERCEPT - v) / b for y, v in t.items()}
    return g, b, steps, t


def load_chuine(path):
    """Chuine 2004: section 1 = GHD (days after 1 Sep), section 2 = T anomaly."""
    ghd, temp, sec = {}, {}, 0
    for l in open(path, encoding="latin-1"):
        if l.startswith("Year"):
            sec += 1
            continue
        m = re.match(r"^(\d{4})\s+(-?\d+(?:\.\d+)?)\s*$", l)
        if m and sec:
            (ghd if sec == 1 else temp)[int(m.group(1))] = float(m.group(2))
    return ghd, temp


def load_daux(path):
    """Daux 2012 NOAA file: three fixed-width parts; values right-aligned to code tokens."""
    lines = open(path, encoding="latin-1").read().splitlines()
    series, codes = {}, None
    for l in lines:
        m = re.match(r"^(Year|\d{4})(\s+)([A-Z][A-Za-z]{1,3}\d?)\s", l)
        if m and re.fullmatch(r"(\s+[A-Z][A-Za-z]{1,3}\d?)+\s*", l[4:]):
            codes = [(t.group(), t.end()) for t in re.finditer(r"\S+", l)][1:]
            for c, _ in codes:
                series.setdefault(c, {})
            continue
        if codes is None:
            continue
        m = re.match(r"^(\d{4})(\s|$)", l)
        if not m:
            if l.startswith("Daux et al. 2012 Grape Harvest Date Data, part"):
                codes = None
            continue
        y = int(m.group(1))
        for t in re.finditer(r"-?\d+\.\d", l[4:]):
            end = t.end() + 4
            c = min(codes, key=lambda ce: abs(ce[1] - end))
            if abs(c[1] - end) > 2:
                raise ValueError(f"unaligned value {t.group()} at {y} col {end}")
            series[c[0]][y] = float(t.group())
    return series


def load_events(path):
    rows, header = [], None
    for line in open(path, encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        p = [x.strip() for x in line.rstrip("\n").split("\t")]
        if header is None:
            header = p
            continue
        rows.append(dict(zip(header, p)))
    return rows


def exclusion(evolv_path, events):
    starts, in_data, header = [], False, False
    for line in open(evolv_path, encoding="utf-8", errors="replace"):
        if line.startswith("*/"):
            in_data = True
            continue
        if not in_data:
            continue
        if not header:
            header = True
            continue
        p = line.rstrip("\n").split("\t")
        try:
            if float(p[7]) >= VSSI_EXCLUDE:
                starts.append(int(float(p[0])))
        except (ValueError, IndexError):
            pass
    starts += [int(e["year"]) for e in events]
    years = set()
    for e in starts:
        years.update({e, e + 1, e + 2})
    return years, sorted(set(starts))


# ---------------------------------------------------------------- anomalies

def ref_years(g, e, excl):
    out = []
    for r in range(e - 1, e - LOOKBACK - 1, -1):
        if r in g and r not in excl:
            out.append(r)
            if len(out) == N_REF:
                break
    return out


def anom(g, y, e, excl, min_ref=MIN_REF):
    refs = ref_years(g, e, excl)
    if len(refs) < min_ref or y not in g:
        return None, refs
    return g[y] - statistics.median(g[r] for r in refs), refs


def background(g, excl):
    bg = {}
    for y in range(*BG_RANGE):
        if y in g and y not in excl:
            a, _ = anom(g, y, y, excl)
            if a is not None:
                bg[y] = a
    return bg


def pctile(vals, x):
    """Share of values strictly below x, plus half of ties (percent)."""
    lo = sum(v < x for v in vals)
    eq = sum(v == x for v in vals)
    return 100.0 * (lo + 0.5 * eq) / len(vals)


def quantile(vals, p):
    s = sorted(vals)
    k = (len(s) - 1) * p
    i = int(k)
    return s[i] if i + 1 >= len(s) else s[i] + (s[i + 1] - s[i]) * (k - i)


def null_pairs(g, excl):
    pairs = []
    for y in range(*BG_RANGE):
        if y in excl or (y + 1) in excl or y not in g or (y + 1) not in g:
            continue
        a0, _ = anom(g, y, y, excl)
        a1, _ = anom(g, y + 1, y, excl)
        if a0 is not None and a1 is not None:
            pairs.append((a0, a1))
    return pairs


# ---------------------------------------------------------------- commands

def event_sets(events, g):
    lo, hi = min(g), max(g)
    cal = [e for e in events if e["role"] in ("cal", "nomonth") and lo + LOOKBACK <= int(e["year"]) < hi]
    large = []
    for e in cal:
        v = e["vssi_tgs"]
        if (v != "NA" and float(v) >= LARGE_VSSI) or (v == "NA" and e["name"] in VEI6_NO_VSSI):
            large.append(e)
    return cal, large


def score(g, ev, excl_for):
    e = int(ev["year"])
    excl = excl_for(ev)
    a0, refs = anom(g, e, e, excl)
    a1, _ = anom(g, e + 1, e, excl)
    return a0, a1, refs


def test(label, rows, pairs, p90, rng, out):
    rows = [r for r in rows if r["a0"] is not None and r["a1"] is not None]
    n = len(rows)
    hits = sum(max(r["a0"], r["a1"]) >= p90 for r in rows)
    m0 = statistics.mean(r["a0"] for r in rows)
    m1 = statistics.mean(r["a1"] for r in rows)
    ge_h = ge_0 = ge_1 = 0
    null_h = []
    for _ in range(N_DRAWS):
        s = rng.sample(pairs, n)
        h = sum(max(a, b) >= p90 for a, b in s)
        null_h.append(h)
        ge_h += h >= hits
        ge_0 += statistics.mean(a for a, _ in s) >= m0
        ge_1 += statistics.mean(b for _, b in s) >= m1
    p = lambda k: (k + 1) / (N_DRAWS + 1)
    out(f"{label}: n={n}  hits={hits} ({hits / n:.2f})  null mean hits={statistics.mean(null_h):.2f} "
        f"({statistics.mean(null_h) / n:.2f})  null 95th pct={quantile(null_h, 0.95):.0f}  p={p(ge_h):.4f}")
    out(f"  SEA lag 0: mean A = {m0:+.1f} d  p={p(ge_0):.4f}   lag +1: mean A = {m1:+.1f} d  p={p(ge_1):.4f}")
    return hits, n, p(ge_h)


def setup(argv):
    g, b, steps, t = beaune_ghd(argv[0])
    events = load_events(argv[1])
    excl, starts = exclusion(argv[2], events)
    return g, b, steps, t, events, excl, starts


def calibrate(argv):
    out = print
    g, b, steps, t, events, excl, starts = setup(argv)
    out(f"# Beaune GHD from Labbe 2019 B_linear, GHD = ({B_INTERCEPT} - T) / b, b = {b} degC/day")
    out(f"# most common T steps: {steps.most_common(4)}")
    out(f"# years with T: {len(g)} ({min(g)}-{max(g)}); missing: {[y for y in range(min(g), max(g) + 1) if y not in g]}")
    pre = [g[y] for y in g if 1354 <= y <= 1987]
    out(f"# mean GHD 1354-1987 = DOY {statistics.mean(pre):.1f} (paper: 28 Sep = DOY 271/272); SD {statistics.pstdev(pre):.1f} d")
    frac = Counter(round(v - round(v), 2) for v in g.values())
    out(f"# fractional part of GHD (integer check): {frac.most_common(3)}")
    bg = background(g, excl)
    p90 = quantile(list(bg.values()), 0.90)
    out(f"# background: {len(bg)} years; P50 {quantile(list(bg.values()), .5):+.1f}  P90 {p90:+.1f}  P95 {quantile(list(bg.values()), .95):+.1f} d")
    pairs = null_pairs(g, excl)
    out(f"# null pairs: {len(pairs)}; single-pair hit rate {sum(max(a, c) >= p90 for a, c in pairs) / len(pairs):.3f}")

    def excl_for(ev):
        # every listed start except the event itself stays excluded from its reference
        return excl
    cal, large = event_sets(events, g)
    large_names = {e["name"] for e in large}
    rows = []
    out("\nname\tyear\tmonth\tclass\tvssi\tlarge\tnref\tref_med\tGHD_E\tA_E\tpct_E\tGHD_E1\tA_E1\tpct_E1\thit")
    for ev in cal:
        a0, a1, refs = score(g, ev, excl_for)
        e = int(ev["year"])
        cl = (ev["label"] + ("E" if ev["season"] == "early" else "L" if ev["season"] == "late" else "-"))
        r = dict(name=ev["name"], a0=a0, a1=a1, cls=cl, large=ev["name"] in large_names)
        rows.append(r)
        if a0 is None:
            out(f"{ev['name']}\t{e}\t{ev['month']}\t{cl}\t{ev['vssi_tgs']}\t{r['large']}\t{len(refs)}\tdropped")
            continue
        med = statistics.median(g[x] for x in refs)
        hit = max(a0, a1) >= p90
        out(f"{ev['name']}\t{e}\t{ev['month']}\t{cl}\t{ev['vssi_tgs']}\t{r['large']}\t{len(refs)}\t{med:.0f}\t"
            f"{g[e]:.0f}\t{a0:+.0f}\t{pctile(list(bg.values()), a0):.0f}\t{g[e + 1]:.0f}\t{a1:+.0f}\t"
            f"{pctile(list(bg.values()), a1):.0f}\t{'HIT' if hit else '-'}")
    out("")
    rng = random.Random(SEED)
    test("S_large (primary)", [r for r in rows if r["large"]], pairs, p90, rng, out)
    rng = random.Random(SEED)
    test("S_all (secondary)", rows, pairs, p90, rng, out)

    out("\n# season (descriptive)")
    for lab, sel in (("large early (XE/TE)", lambda r: r["large"] and r["cls"] in ("XE", "TE")),
                     ("large late (XL/TL)", lambda r: r["large"] and r["cls"] in ("XL", "TL")),
                     ("all early (XE/TE)", lambda r: r["cls"] in ("XE", "TE")),
                     ("all late (XL/TL)", lambda r: r["cls"] in ("XL", "TL"))):
        s = [r for r in rows if sel(r) and r["a0"] is not None]
        if s:
            h0 = sum(r["a0"] >= p90 for r in s)
            h1 = sum(r["a1"] >= p90 for r in s)
            out(f"  {lab}: n={len(s)}  lag-0 hits {h0} ({h0 / len(s):.2f})  lag-1 hits {h1} ({h1 / len(s):.2f})  "
                f"median A0 {statistics.median(r['a0'] for r in s):+.0f}  median A1 {statistics.median(r['a1'] for r in s):+.0f}")
    out(f"  background single-year rate at P90 = 0.10 by construction")

    name, e = CHECK
    a0, refs = anom(g, e, e, excl)
    a1, _ = anom(g, e + 1, e, excl)
    out(f"\n# check (no test): {name}: refs {refs}  A({e}) {a0:+.0f} d (pct {pctile(list(bg.values()), a0):.0f})  "
        f"A({e + 1}) {a1:+.0f} d (pct {pctile(list(bg.values()), a1):.0f})")


def doy_to_date(d):
    import datetime
    return (datetime.date(1453, 1, 1) + datetime.timedelta(days=round(d) - 1)).strftime("%d %b")


def target(argv):
    out = print
    g, b, steps, t, events, excl, starts = setup(argv)
    bg = background(g, excl)
    vals = list(bg.values())
    p90 = quantile(vals, 0.90)
    refs = ref_years(g, UE_E, excl)
    med = statistics.median(g[r] for r in refs)
    out(f"# UE 1453 target. Reference (E = {UE_E}): {sorted(refs)}  median GHD DOY {med:.1f} ({doy_to_date(med)})")
    out(f"# reference GHD: {[(r, round(g[r])) for r in sorted(refs)]}")
    out(f"# background {len(bg)} years, P90 = {p90:+.1f} d")
    out("year\tT_AMJJ_Blinear\tGHD_DOY\tdate(approx, Julian)\tA_days\tbg_pct\tlate(>=P90)")
    for y in UE_YEARS:
        a = g[y] - med
        out(f"{y}\t{t[y]:.2f}\t{g[y]:.1f}\t{doy_to_date(g[y])}\t{a:+.1f}\t{pctile(vals, a):.1f}\t{a >= p90}")
    out("\n# context 1440-1465 (GHD DOY, rounded; * = exclusion year)")
    out("  " + "  ".join(f"{y}:{round(g[y])}{'*' if y in excl else ''}" for y in range(1440, 1466) if y in g))
    ranks = sorted(g, key=lambda y: -g[y])
    out(f"\n# rank of 1453 GHD among all {len(g)} years (1 = latest): {ranks.index(1453) + 1}; "
        f"1452: {ranks.index(1452) + 1}; 1454: {ranks.index(1454) + 1}")


def fillcheck(argv):
    out = print
    g, b, steps, t = beaune_ghd(argv[0])
    cg, _ = load_chuine(argv[1])
    d = {y: g[y] - (243 + cg[y]) for y in range(1371, 1507) if y in g and y in cg}
    # Chuine dates are days after 1 Sep; DOY of 1 Sep (non-leap) = 244, so 1 Sep + x = 243 + x + 1 -> use 244
    d = {y: g[y] - (244 + cg[y]) for y in d}
    vals = list(d.values())
    out(f"# Beaune (Labbe 2019) minus Burgundy/Dijon (Chuine 2004), days, 1371-1506: n={len(vals)}")
    out(f"# median {statistics.median(vals):+.1f}  mean {statistics.mean(vals):+.1f}  SD {statistics.pstdev(vals):.1f}")
    out(f"# most common rounded differences: {Counter(round(v) for v in vals).most_common(6)}")
    out("# 1440-1465:")
    for y in range(1440, 1466):
        if y in d:
            out(f"  {y}\tBeaune {g[y]:.1f}\tChuine {244 + cg[y]:.1f}\tD {d[y]:+.1f}")
    # post hoc (see README Deviations): runs of identical rounded D, 1370-1644
    dr = {y: round(g[y] - 244 - cg[y]) for y in range(1370, 1645) if y in g and y in cg}

    def runs(seq):
        out_, start = [], 0
        for i in range(1, len(seq) + 1):
            if i == len(seq) or seq[i][1] != seq[i - 1][1] or seq[i][0] != seq[i - 1][0] + 1:
                if i - start >= 3:
                    out_.append((seq[start][0], seq[i - 1][0], seq[start][1], i - start))
                start = i
        return out_
    seq = sorted(dr.items())
    obs = runs(seq)
    out(f"\n# post hoc: runs of >= 3 consecutive years with identical rounded D, 1370-1644 (n={len(seq)}): {obs}")
    longest = max((r[3] for r in obs), default=0)
    rng = random.Random(SEED)
    vals = [v for _, v in seq]
    k = 0
    for _ in range(N_DRAWS):
        rng.shuffle(vals)
        if max((r[3] for r in runs([(seq[i][0], vals[i]) for i in range(len(seq))])), default=0) >= longest:
            k += 1
    out(f"# P(a run of >= {longest} identical D anywhere in 1370-1644 | D shuffled over years) = {(k + 1) / (N_DRAWS + 1):.4f}")


def secondary(argv):
    out = print
    cg, ct = load_chuine(argv[0])
    daux = load_daux(argv[1])
    events = load_events(argv[2])
    excl, _ = exclusion(argv[3], events)
    out("# Chuine 2004 Burgundy (GHD days after 1 Sep; T = Apr-Aug anomaly degC vs Dijon 1960-89)")
    for name, s, sign in (("Chuine GHD", cg, 1), ("Chuine T", ct, -1)):
        refs = ref_years(s, UE_E, excl)
        med = statistics.median(s[r] for r in refs)
        bg = background(s, excl)
        out(f"  {name}: refs {sorted(refs)} median {med:.2f}")
        for y in UE_YEARS:
            a = s[y] - med
            out(f"    {y}\tvalue {s[y]:.2f}\tA {a:+.2f}\tbg pct {pctile(list(bg.values()), a):.0f}  "
                f"({'higher = later/colder' if sign == 1 else 'lower = colder'})")
    out("\n# Daux 2012 regional composites (days after 31 Aug) with any value 1452-1454")
    for code, s in sorted(daux.items()):
        have = [y for y in UE_YEARS if y in s]
        if not have:
            continue
        refs = ref_years(s, UE_E, excl)
        n15 = sum(1 for y in range(1440, 1466) if y in s)
        med = statistics.median(s[r] for r in refs) if refs else None
        bg = background_loose(s, excl)
        out(f"  {code}: years with data 1440-1465 = {n15}; refs {sorted(refs)}" + ("  FLAG <7 refs" if len(refs) < MIN_REF else ""))
        for y in have:
            a = s[y] - med if med is not None else None
            pc = f"{pctile(bg, a):.0f}" if (a is not None and bg) else "NA"
            out(f"    {y}\tvalue {s[y]:.1f}\tA {a:+.1f}\tbg pct {pc} (n bg {len(bg)})" if a is not None else f"    {y}\t{s[y]}")


def background_loose(s, excl):
    out = []
    for y in s:
        if y in excl:
            continue
        refs = ref_years(s, y, excl)
        if len(refs) >= MIN_REF:
            out.append(s[y] - statistics.median(s[r] for r in refs))
    return out


if __name__ == "__main__":
    cmd, args = sys.argv[1], sys.argv[2:]
    {"calibrate": calibrate, "target": target, "fillcheck": fillcheck, "secondary": secondary}[cmd](args)

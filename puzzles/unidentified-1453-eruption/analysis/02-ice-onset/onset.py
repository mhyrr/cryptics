"""Onset of volcanic sulfur in NEEM-2011-S1, and its place in the annual cycle.

usage: python3 -I onset.py NEEM_TAB [TUNU_S9_TSV]

NEEM_TAB    PANGAEA.940553 tab file (2 cm CFA record, NS1-2011 ages).
TUNU_S9_TSV Abbott et al. 2021 supplement Table S9 as TSV (monthly TUNU2013
            nssS, Ca, Na, 1440-1490), from xlsx2tsv.py. Optional.

Method, stated before looking at 1453 (rule 4):
  nssS = S - 0.084 * Na   (sea-water S/Na mass ratio used by Sigl et al. 2014 SI)
  Background: all samples with age in [Y-8, Y), where Y is the eruption year
  (for 1453, Y = 1452, the earliest year Abbott 2021 allow).
  Threshold: median + k * 1.4826 * MAD of the background.
  Onset: first sample at or after Y whose own value and the next L-1 values
  all exceed the threshold. Reported onset age is the midpoint between that
  sample and the one before it; the half-gap is the resolution error.
  Base case k = 3, L = 3. Sensitivity: k in {2, 3, 4}, L in {2, 3, 4}.
  Second definition ("frac"): first sample whose excess over the background
  median exceeds 20 % of the event's peak excess (peak searched over 2 years).

Seasonal position: the nearest Na, Ca and NH4 maxima before and after the
onset (searched in the 0.9 yr before and after; 3-point smoothed). Na peaks in
winter-spring, Ca in spring, NH4 in summer in Greenland (Abbott 2021; Sigl
2013). The phase is reported in age-model years and as a fraction of the gap
between the bracketing maxima.

Calibration: the same code on eruptions of known date in the same core. Lag =
onset (NS1-2011 decimal age) - eruption date. The NS1-2011 fraction of year is
a layer-counting convention, not a calendar; the lag absorbs that, which is the
point of calibrating in the same core and coordinate.
"""
import statistics
import sys

S_NA = 0.084

# name, eruption decimal date (climactic phase), class, source of date
# Dates: climactic phase where it differs from GVP start (see README).
EVENTS = [
    ("Laki 1783", 1783 + (31 + 28 + 31 + 30 + 31 + 8) / 365, "NH-x", "8 Jun 1783"),
    ("Katmai-Novarupta 1912", 1912 + (31 + 29 + 31 + 30 + 31 + 6) / 366, "NH-x", "6 Jun 1912"),
    ("Hekla 1766", 1766 + (31 + 28 + 31 + 5) / 365, "NH-x", "5 Apr 1766"),
    ("Katla 1755", 1755 + (273 + 17) / 365, "NH-x", "17 Oct 1755"),
    ("Askja 1875", 1875 + (31 + 28 + 29) / 365, "NH-x", "29 Mar 1875"),
    ("Shiveluch 1854", 1854 + (31 + 18) / 365, "NH-x", "18 Feb 1854"),
    ("Tambora 1815", 1815 + (31 + 28 + 31 + 10) / 365, "trop", "10 Apr 1815"),
    ("Krakatau 1883", 1883 + (212 + 27) / 365, "trop", "27 Aug 1883"),
    ("Cosiguina 1835", 1835 + 20 / 365, "trop", "20 Jan 1835"),
    ("Santa Maria 1902", 1902 + (273 + 24) / 365, "trop", "24 Oct 1902"),
    ("Agung 1963", 1963 + (31 + 28 + 17) / 365, "trop", "17 Mar 1963"),
    ("El Chichon 1982", 1982 + (31 + 28 + 31 + 4) / 365, "trop", "4 Apr 1982"),
    ("Pinatubo 1991", 1991 + (31 + 28 + 31 + 30 + 31 + 15) / 365, "trop", "15 Jun 1991"),
    ("Huaynaputina 1600", 1600 + (31 + 19) / 366, "trop", "19 Feb 1600"),
]


def load_neem(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        body = False
        header = None
        for line in f:
            if line.startswith("*/"):
                body = True
                continue
            if not body:
                continue
            parts = line.rstrip("\n").split("\t")
            if header is None:
                header = parts
                continue
            rec = dict(zip(header, parts))
            try:
                age = float(rec["Age [a AD/CE]"])
                s = float(rec["S [µg/kg]"])
                na = float(rec["Na [µg/kg]"])
            except (KeyError, ValueError):
                continue

            def num(key):
                try:
                    return float(rec[key])
                except (KeyError, ValueError):
                    return None

            rows.append({
                "depth": float(rec["Depth ice/snow [m]"]),
                "age": age,
                "nssS": s - S_NA * na,
                "Na": na,
                "Ca": num("Ca [µg/kg]"),
                "NH4": num("[NH4]+ [µmol/l]"),
                "BC": num("BC [µg/kg]"),
            })
    rows.sort(key=lambda r: r["age"])
    return rows


def load_tunu(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) < 6:
                continue
            try:
                age, depth, nss, ca, na = (float(x) for x in p[1:6])
            except ValueError:
                continue
            if min(nss, ca, na) < 0:  # -0.999 = missing
                continue
            rows.append({"depth": depth, "age": age, "nssS": nss, "Na": na, "Ca": ca,
                         "NH4": None, "BC": None})
    rows.sort(key=lambda r: r["age"])
    return rows


def mad(xs):
    m = statistics.median(xs)
    return m, statistics.median(abs(x - m) for x in xs)


def onset_mad(rows, y, k, L, bg_years=8, search_years=2.0):
    bg = [r["nssS"] for r in rows if y - bg_years <= r["age"] < y]
    med, d = mad(bg)
    thr = med + k * 1.4826 * d
    idx = [i for i, r in enumerate(rows) if y <= r["age"] < y + search_years]
    for i in idx:
        if i + L > len(rows):
            break
        if all(rows[j]["nssS"] > thr for j in range(i, i + L)):
            prev = rows[i - 1]["age"]
            return (prev + rows[i]["age"]) / 2, (rows[i]["age"] - prev) / 2, med, thr, i
    return None, None, med, thr, None


def onset_frac(rows, y, frac=0.2, bg_years=8, search_years=2.0):
    bg = [r["nssS"] for r in rows if y - bg_years <= r["age"] < y]
    med, _ = mad(bg)
    win = [(i, r) for i, r in enumerate(rows) if y <= r["age"] < y + search_years]
    pk_i, pk = max(win, key=lambda t: t[1]["nssS"])
    level = med + frac * (pk["nssS"] - med)
    for i, r in win:
        if r["nssS"] > level:
            prev = rows[i - 1]["age"]
            return (prev + r["age"]) / 2, pk["age"], pk["nssS"]
    return None, pk["age"], pk["nssS"]


def onset_deseason(rows, y, k=3, L=3, bg_years=8, search_years=2.0):
    """Residual = nssS minus the background median of the same NS1-2011 month bin."""
    bins = {}
    for r in rows:
        if y - bg_years <= r["age"] < y:
            bins.setdefault(int((r["age"] % 1) * 12), []).append(r["nssS"])
    clim = {b: statistics.median(v) for b, v in bins.items()}
    res = [r["nssS"] - clim.get(int((r["age"] % 1) * 12), 0.0) for r in rows]
    bg = [res[i] for i, r in enumerate(rows) if y - bg_years <= r["age"] < y]
    med, d = mad(bg)
    thr = med + k * 1.4826 * d
    for i, r in enumerate(rows):
        if not (y <= r["age"] < y + search_years) or i + L > len(rows):
            continue
        if all(res[j] > thr for j in range(i, i + L)):
            return (rows[i - 1]["age"] + r["age"]) / 2
    return None


def smooth(rows, key, i):
    vals = [rows[j][key] for j in (i - 1, i, i + 1) if 0 <= j < len(rows) and rows[j][key] is not None]
    return sum(vals) / len(vals) if vals else None


def bracket_max(rows, key, t, span=0.9):
    """Age of the smoothed maximum of `key` in [t-span, t) and in [t, t+span)."""
    out = []
    for lo, hi in ((t - span, t), (t, t + span)):
        best = None
        for i, r in enumerate(rows):
            if lo <= r["age"] < hi and r[key] is not None:
                v = smooth(rows, key, i)
                if v is not None and (best is None or v > best[1]):
                    best = (r["age"], v)
        out.append(best[0] if best else None)
    return out


def phase_report(rows, t):
    parts = []
    for key in ("Na", "Ca", "NH4"):
        if all(r[key] is None for r in rows[:50]) and all(r[key] is None for r in rows[-50:]):
            continue
        before, after = bracket_max(rows, key, t)
        if before is None or after is None:
            parts.append("%s: n/a" % key)
            continue
        frac = (t - before) / (after - before)
        parts.append("%s max %+.2f / %+.2f yr (phase %.2f)" % (key, before - t, after - t, frac))
    return "; ".join(parts)


def run_event(rows, name, y, label=""):
    lines = []
    o, err, med, thr, i = onset_mad(rows, y, 3, 3)
    fo, pk_age, pk_val = onset_frac(rows, y)
    sens = []
    for k in (2, 3, 4):
        for L in (2, 3, 4):
            so = onset_mad(rows, y, k, L)[0]
            if so is not None:
                sens.append(so)
    ds = onset_deseason(rows, y)
    lines.append("%s%s" % (name, label))
    lines.append("  background median %.1f, threshold (k=3) %.1f ng/g; peak %.1f at %.3f" % (med, thr, pk_val, pk_age))
    if o is None:
        lines.append("  onset (k=3, L=3): not detected within 2 yr")
        return lines, None, None, sens, None, ds
    lines.append("  onset (k=3, L=3): %.3f +/- %.3f (sample spacing); depth %.2f m" % (o, err, rows[i]["depth"]))
    lines.append("  onset (20%% of peak): %s; onset (deseasonalised residual, k=3, L=3): %s" % (
        "%.3f" % fo if fo else "n/a", "%.3f" % ds if ds else "n/a"))
    ratio = (pk_val - med) / (thr - med)
    lines.append("  signal strength (peak excess / threshold excess): %.1f" % ratio)
    lines.append("  sensitivity k=2..4, L=2..4: %.3f to %.3f (n=%d)" % (min(sens), max(sens), len(sens)))
    lines.append("  seasonal position: " + phase_report(rows, o))
    return lines, o, fo, sens, ratio, ds


def main():
    neem = load_neem(sys.argv[1])
    out = []
    out.append("NEEM-2011-S1 (PANGAEA.940553), %d samples with S and Na" % len(neem))
    out.append("nssS = S - %.3f Na; background [Y-8, Y); k=3 MAD, L=3 consecutive" % S_NA)
    out.append("")
    out.append("== Calibration events (known eruption date) ==")
    cal = []
    for name, date, cls, datestr in EVENTS:
        lines, o, fo, sens, ratio, ds = run_event(neem, name, int(date), "  [%s, erupted %s = %.3f]" % (cls, datestr, date))
        out.extend(lines)
        if o is not None:
            lag = (o - date) * 12
            # Quality rules, added after the first run (see README):
            #  Q1 event before 1900, so the background is pre-industrial like 1453's
            #  Q2 signal strength (peak excess / threshold excess) >= 1.5
            q = []
            if date >= 1900:
                q.append("industrial background")
            if ratio < 1.5:
                q.append("weak signal")
            out.append("  lag onset - eruption: %+.1f months (20%%-def %s; deseasonalised %s)%s" % (
                lag, "%+.1f" % ((fo - date) * 12) if fo else "n/a",
                "%+.1f" % ((ds - date) * 12) if ds else "n/a",
                ("  [excluded: " + ", ".join(q) + "]") if q else "  [clean]"))
            if not q:
                na_before = bracket_max(neem, "Na", o)[0]
                cal.append((name, cls, lag, (fo - date) * 12 if fo else None, o - na_before, datestr))
        out.append("")
    out.append("== Calibration summary (lag in months, onset - eruption, NS1-2011 age) ==")
    for cls in ("NH-x", "trop"):
        ls = [c[2] for c in cal if c[1] == cls]
        names = ", ".join("%s %+.1f" % (c[0], c[2]) for c in cal if c[1] == cls)
        if ls:
            out.append("%s: n=%d, median %+.1f, range %+.1f to %+.1f  [%s]" % (
                cls, len(ls), statistics.median(ls), min(ls), max(ls), names))
    out.append("")
    out.append("== Onset position in the Na cycle (yr after the preceding Na maximum) ==")
    for c in cal:
        out.append("  %-20s %-5s erupted %-12s onset %.2f yr after Na max" % (c[0], c[1], c[5], c[4]))
    out.append("")
    out.append("== UE 1453 ==")
    lines, o, fo, sens, ratio, ds = run_event(neem, "UE 1453 (search from 1452.0)", 1452)
    out.extend(lines)
    if o is not None:
        out.append("  onset %.2f yr after the preceding Na maximum" % (o - bracket_max(neem, "Na", o)[0]))
        out.append("")
        out.append("Implied eruption date = onset - calibrated lag (NS1-2011 age):")
        for cls in ("NH-x", "trop"):
            ls = [c[2] for c in cal if c[1] == cls]
            if not ls:
                continue
            lo, hi = o - max(ls) / 12 - (max(sens) - o), o - min(ls) / 12 + (o - min(sens))
            out.append("  if %s: median %.2f; range %.2f to %.2f (calibration range widened by onset sensitivity)" % (
                cls, o - statistics.median(ls) / 12, lo, hi))
    if len(sys.argv) > 2:
        tunu = load_tunu(sys.argv[2])
        out.append("")
        out.append("== TUNU2013 (Abbott 2021 Table S9, monthly means; no Laki-type calibration in this file) ==")
        lines, o2, fo2, sens2, r2, ds2 = run_event(tunu, "UE 1453 in TUNU2013 (search from 1452.0)", 1452)
        out.extend(lines)
        if o2 is not None and o is not None:
            out.append("  TUNU2013 - NEEM onset difference: %+.2f yr" % (o2 - o))
    print("\n".join(out))


if __name__ == "__main__":
    main()

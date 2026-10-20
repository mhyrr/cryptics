"""Is the 1453 sulfur in each Antarctic core above background?

usage: python3 -I antarctic.py AVS2K_ANNUAL_TSV WDC_MONTHLY_TSV AVS2K_EVENTS_TSV AVS2K_COMPOSITE_TSV DOMEC_TAB

AVS2K_ANNUAL_TSV    Sigl et al. 2015 SI (MOESM46) sheet "6 - AVS2k_database_annual"
WDC_MONTHLY_TSV     same workbook, sheet "3 - WDC06A_monthly_nssS"
AVS2K_EVENTS_TSV    same workbook, sheet "7 - AVS2k_database_events"
AVS2K_COMPOSITE_TSV same workbook, sheet "8 - AVS2k_composite"
DOMEC_TAB           PANGAEA.895169 (Gautier et al. 2018 Dome C isotopes)

Test, fixed before looking at 1453 values:
  Background years: 1420-1446 and 1464-1476 (excludes the 1447/48 SH event,
  the 1453 and 1458 events with three years of tail, and 1477).
  Statistic per core: robust z = (x - median) / (1.4826 * MAD) over background
  years, for 1453 and 1454 (annual layers on WD2014; cores synchronised to WD
  can be off by a year, so the larger of the two is used).
  Empirical p: fraction of background years whose value reaches max(x1453, x1454),
  doubled for the two-year look (Bonferroni).
  Network test: mean robust z across cores, year by year, 1420-1476; 1453 and
  1454 are ranked against background years.
"""
import statistics
import sys

BG = set(range(1420, 1447)) | set(range(1464, 1477))


def num(x):
    try:
        v = float(x)
    except ValueError:
        return None
    return None if v < -9 else v


def load_annual(path):
    rows = [l.rstrip("\n").split("\t") for l in open(path, encoding="utf-8")]
    names = rows[1]
    data = {}
    for r in rows[2:]:
        try:
            y = int(float(r[0]))
        except (ValueError, IndexError):
            continue
        for j in range(2, len(names)):
            if j < len(r) and names[j]:
                v = num(r[j])
                if v is not None:
                    data.setdefault(names[j], {})[y] = v
    return data


def robust(vals):
    m = statistics.median(vals)
    d = statistics.median(abs(v - m) for v in vals) * 1.4826
    return m, d


def main(annual, monthly, events, composite, domec):
    out = []
    data = load_annual(annual)
    out.append("== Per-core annual nssS (Sigl 2015 SI, AVS2k_database_annual, WD2014 years) ==")
    out.append("Background years: 1420-1446, 1464-1476. z = (x - median)/(1.4826 MAD).")
    out.append("%-9s %4s %6s %6s %6s %6s %6s %6s %6s %7s %7s" % (
        "core", "nBG", "median", "sMAD", "x1453", "x1454", "z1453", "z1454", "z1459", "p(max)", "verdict"))
    zs_by_year = {}
    covered = sig = 0
    for core in sorted(data):
        s = data[core]
        bg = [s[y] for y in BG if y in s]
        if len(bg) < 20 or 1453 not in s or 1454 not in s:
            out.append("%-9s does not cover 1453 with >= 20 background years" % core)
            continue
        covered += 1
        m, d = robust(bg)
        for y in range(1420, 1477):
            if y in s and d > 0:
                zs_by_year.setdefault(y, []).append((s[y] - m) / d)
        x3, x4 = s[1453], s[1454]
        z3, z4 = (x3 - m) / d, (x4 - m) / d
        z9 = (s[1459] - m) / d if 1459 in s else float("nan")
        xm = max(x3, x4)
        p = min(1.0, 2 * sum(1 for v in bg if v >= xm) / len(bg))
        verdict = "above" if p < 0.05 else "no"
        sig += verdict == "above"
        out.append("%-9s %4d %6.1f %6.1f %6.1f %6.1f %6.2f %6.2f %6.1f %7.3f %7s" % (
            core, len(bg), m, d, x3, x4, z3, z4, z9, p, verdict))
    out.append("Cores covering 1453: %d; above background at p < 0.05 (two-year look): %d" % (covered, sig))
    out.append("Chance expectation under the null at p < 0.05: about %.1f" % (0.05 * covered))
    from math import comb
    tail = sum(comb(covered, k) * 0.05 ** k * 0.95 ** (covered - k) for k in range(sig, covered + 1))
    out.append("Binomial P(>= %d of %d by chance, p = 0.05 each, cores treated as independent): %.4f" % (
        sig, covered, tail))
    out.append("")
    out.append("== Network: mean robust z across cores, by year ==")
    means = {y: statistics.mean(v) for y, v in zs_by_year.items() if len(v) >= max(3, covered // 2)}
    bgm = sorted((means[y], y) for y in means if y in BG)
    for y in range(1440, 1477):
        if y in means:
            tag = "BG" if y in BG else "  "
            out.append("  %d %s mean z %+5.2f (n=%d)" % (y, tag, means[y], len(zs_by_year[y])))
    for y in (1453, 1454):
        rank = sum(1 for v, _ in bgm if v >= means[y])
        out.append("%d mean z %+.2f; background years with mean z at least this high: %d of %d" % (
            y, means[y], rank, len(bgm)))
    out.append("")

    out.append("== WDC06A monthly nssS (WD2014), 1451-1456 ==")
    rows = []
    for l in open(monthly, encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        try:
            t, v = float(p[0]), float(p[1])
        except (ValueError, IndexError):
            continue
        if v > -9:  # -10 marks missing months
            rows.append((t, v))
    rows.sort()
    bg = [v for t, v in rows if int(t) in BG]
    m, d = robust(bg)
    thr = m + 3 * d
    out.append("Monthly background median %.1f, sMAD %.1f, threshold (3 sMAD) %.1f ng/g" % (m, d, thr))
    for t, v in rows:
        if 1451 <= t < 1457:
            out.append("  %.3f %6.1f %s" % (t, v, "*" if v > thr else ""))
    first = None
    for i in range(len(rows) - 2):
        t = rows[i][0]
        if 1452 <= t < 1457 and all(rows[j][1] > thr for j in range(i, i + 3)):
            first = t
            break
    out.append("WDC06A first run of 3 months above threshold after 1452.0: %s" % (
        "%.3f" % first if first else "none before 1457"))
    out.append("")

    out.append("== AVS-2k event-only records (Law Dome DSS, Siple, Dyer, Plateau Remote, Dome A) ==")
    for l in open(events, encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        if p and p[0][:3] == "145" or (p and p[0][:4] in ("1447", "1458")):
            out.append("  " + " | ".join(p[:7]))
    out.append("  (a missing 1453 row means none of these five records lists a 1453 event)")
    out.append("")
    out.append("== AVS-2k composite rows 1440-1480 ==")
    for l in open(composite, encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        try:
            y = float(p[0])
        except (ValueError, IndexError):
            continue
        if 1440 <= y <= 1480:
            out.append("  %s: %s kg/km2, s.e.m. %s, rank %s" % (p[0], p[2][:5], p[3][:4], p[4]))
    out.append("")
    out.append("== Dome C isotopes (PANGAEA.895169), rows 1449-1462 ==")
    body = False
    hdr = None
    for l in open(domec, encoding="utf-8"):
        if l.startswith("*/"):
            body = True
            continue
        if not body:
            continue
        p = l.rstrip("\n").split("\t")
        if hdr is None:
            hdr = p
            continue
        try:
            a = float(p[2])
        except (ValueError, IndexError):
            continue
        if 1449 <= a <= 1462:
            out.append("  %s age %s SO4 %s fV %s D33S %s" % (p[0], p[2], p[4], p[5], p[9]))
    print("\n".join(out))


if __name__ == "__main__":
    main(*sys.argv[1:6])

"""One pulse or several? Shape of the 1453 sulfur rise in each core.

usage: python3 -I structure.py NEEM_TAB TUNU_S9_TSV WDC_MONTHLY_TSV NGRIP_5CM_TSV BURKE_TSV

Rule, fixed before counting (H9):
  1. Put each record on a monthly grid (mean of samples in each 1/12-yr bin;
     a single empty bin between two full ones is filled by interpolation).
  2. Remove the seasonal cycle: subtract, for each calendar bin of the
     timescale, the median of that bin over background years (Greenland
     1442-1451, Antarctica WDC 1420-1446). Then 3-month running mean.
  3. Threshold = 3 * 1.4826 * MAD of the background residual.
  4. Episodes = runs of >= 2 months above threshold in 1452.0-1457.9.
  5. Pulses within an episode = local maxima above threshold separated by a
     minimum lower than 50 % of the smaller maximum's residual. One episode with
     one pulse = "one pulse".
NGRIP (about 4 samples a year) is reported raw; it is too coarse for rule 5.
Burke 2023 TUNU2013 Delta33S is listed in time order: one stratospheric pulse
predicts a single positive-then-negative excursion.
"""
import statistics
import sys


def load_neem(path):
    rows, body, hdr = [], False, None
    for line in open(path, encoding="utf-8"):
        if line.startswith("*/"):
            body = True
            continue
        if not body:
            continue
        p = line.rstrip("\n").split("\t")
        if hdr is None:
            hdr = p
            continue
        r = dict(zip(hdr, p))
        try:
            rows.append((float(r["Age [a AD/CE]"]), float(r["S [µg/kg]"]) - 0.084 * float(r["Na [µg/kg]"])))
        except (KeyError, ValueError):
            pass
    return sorted(rows)


def load_cols(path, ti, vi, skip_neg=True):
    rows = []
    for line in open(path, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        try:
            t, v = float(p[ti]), float(p[vi])
        except (ValueError, IndexError):
            continue
        if skip_neg and v < 0:
            continue
        rows.append((t, v))
    return sorted(rows)


def monthly(rows, lo, hi):
    bins = {}
    for t, v in rows:
        if lo <= t < hi:
            bins.setdefault(int(t * 12), []).append(v)
    return {k: statistics.mean(v) for k, v in bins.items()}


def analyse(name, rows, bg_years, lo=1452.0, hi=1458.0):
    out = ["== %s ==" % name]
    m = monthly(rows, min(bg_years), hi)
    clim = {}
    for k, v in m.items():
        if int(k // 12) in bg_years:
            clim.setdefault(k % 12, []).append(v)
    clim = {b: statistics.median(v) for b, v in clim.items()}
    keys = sorted(k for k in m if k % 12 in clim)
    res = {k: m[k] - clim[k % 12] for k in keys}
    # fill single empty month bins (sample spacing can exceed 1/12 yr) by
    # linear interpolation, so a gap does not split an episode
    filled = 0
    for k in range(keys[0] + 1, keys[-1]):
        if k not in res and k - 1 in res and k + 1 in res:
            res[k] = (res[k - 1] + res[k + 1]) / 2
            filled += 1
    keys = sorted(res)
    sm = {}
    for k in keys:
        vals = [res[j] for j in (k - 1, k, k + 1) if j in res]
        sm[k] = sum(vals) / len(vals)
    bg = [sm[k] for k in keys if int(k // 12) in bg_years]
    med = statistics.median(bg)
    thr = med + 3 * 1.4826 * statistics.median(abs(x - med) for x in bg)
    out.append("background months %d, residual threshold %.1f ng/g; single empty bins filled: %d" % (
        len(bg), thr, filled))
    win = [k for k in keys if lo * 12 <= k < hi * 12]
    episodes, cur = [], []
    for k in win:
        if sm[k] > thr and (not cur or k == cur[-1] + 1):
            cur.append(k)
        else:
            if len(cur) >= 2:
                episodes.append(cur)
            cur = [k] if sm[k] > thr else []
    if len(cur) >= 2:
        episodes.append(cur)
    out.append("episodes above threshold (>= 2 months): %d" % len(episodes))
    for ep in episodes:
        peaks = [k for k in ep if sm[k] >= sm.get(k - 1, -1e9) and sm[k] >= sm.get(k + 1, -1e9)]
        # merge maxima not separated by a deep enough minimum
        kept = []
        for pk in peaks:
            if kept:
                prev = kept[-1]
                trough = min(sm[j] for j in range(prev, pk + 1))
                if trough >= 0.5 * min(sm[prev], sm[pk]):
                    if sm[pk] > sm[prev]:
                        kept[-1] = pk
                    continue
            kept.append(pk)
        out.append("  %.3f to %.3f (%d months); pulses: %s" % (
            ep[0] / 12, (ep[-1] + 1) / 12, len(ep),
            ", ".join("%.2f (+%.1f)" % (p / 12, sm[p]) for p in kept)))
    out.append("  monthly smoothed residual 1452.0-1456.0:")
    line = []
    for k in win:
        if k < 1456 * 12:
            line.append("%.2f:%+.0f" % (k / 12, sm[k]))
    for i in range(0, len(line), 8):
        out.append("    " + "  ".join(line[i:i + 8]))
    return out


def main(neem, tunu, wdc, ngrip, burke):
    out = []
    gl_bg = set(range(1442, 1452))
    out += analyse("NEEM-2011-S1 (2 cm, NS1-2011)", load_neem(neem), gl_bg)
    out.append("")
    out += analyse("TUNU2013 (Abbott 2021 S9 monthly, NS1-2011)", load_cols(tunu, 1, 3), gl_bg)
    out.append("")
    out += analyse("WDC06A (Sigl 2015 monthly, WD2014)", load_cols(wdc, 0, 1), set(range(1420, 1447)))
    out.append("")
    out.append("== NGRIP 5 cm discrete S (Sigl 2015 SI; NS1-2011), raw, 1451.5-1456 ==")
    ng = [r for r in load_cols(ngrip, 0, 2) if 1451.5 <= r[0] < 1456]
    out.append("  " + "  ".join("%.2f:%.0f" % r for r in ng))
    out.append("")
    out.append("== Burke 2023 TUNU2013 1453 samples, time order (Age, [S], D33S, fvolc) ==")
    for line in open(burke, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) > 14 and p[1] == "UE 1453":
            out.append("  %s %.3f  S %6.1f  D33S %+.2f +/- %s  fvolc %s" % (
                p[2], float(p[5]), float(p[7]), float(p[12]), p[13], (p[14][:4] if p[14] else "-")))
    print("\n".join(out))


if __name__ == "__main__":
    main(*sys.argv[1:6])

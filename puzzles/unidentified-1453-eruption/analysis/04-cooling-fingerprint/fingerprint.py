"""Experiment 04: latitude gradient of summer cooling after eruptions.

Standard library only. The method is fixed in README.md ("Pre-registration").

Usage
  python3 -I fingerprint.py calibrate DATASET VALUES SITES EVENTS EVOLV2K [--year-rule select|E|E1]
  python3 -I fingerprint.py classify  DATASET VALUES SITES EVENTS EVOLV2K [--year-rule ...] [--target-year Y]

DATASET is one of: schneider, ntrend, grid.
  schneider: VALUES = schneider2015mxd.txt, SITES = sites_schneider2015.tsv
  ntrend:    VALUES = ntrend2015tr.txt,     SITES = ntrend2015-RecordsUsed_Metadata.txt
  grid:      VALUES = out/grid_values.tsv,  SITES = out/grid_sites.tsv
"""
import math
import random
import statistics
import sys

SPLIT_LAT = 60.0
MIN_PER_GROUP = 3
MIN_REF_YEARS = 5
VSSI_EXCLUDE = 3.0
N_PERM = 10000
N_BOOT = 2000
SEED = 1453
SD_WINDOW = (1250, 1990)


# ---------------------------------------------------------------- loading

def _num(s):
    s = s.strip()
    if s == "" or s in ("-9999", "-9999.0", "NA", "NaN", "nan"):
        return None
    v = float(s)
    if v <= -9998:
        return None
    return v


def load_table(path, year_col):
    """Tab table with a header row whose first field is year_col. Skips '#' lines."""
    header = None
    data = {}
    with open(path, encoding="utf-8-sig", errors="replace") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if header is None:
                if parts[0].strip() == year_col:
                    header = [p.strip() for p in parts]
                continue
            try:
                y = int(float(parts[0]))
            except ValueError:
                continue
            for i, col in enumerate(header[1:], start=1):
                v = _num(parts[i]) if i < len(parts) else None
                if v is not None:
                    data.setdefault(col, {})[y] = v
    if header is None:
        raise SystemExit(f"no header starting with {year_col!r} in {path}")
    return data


def load_sites(dataset, path):
    """Return {column_code: (lat, lon, label)}."""
    sites = {}
    if dataset == "schneider":
        for row in _rows(path):
            if row["use"] == "1":
                sites[row["column"]] = (float(row["lat"]), float(row["lon"]), row["code"])
    elif dataset == "grid":
        for row in _rows(path):
            sites[row["code"]] = (float(row["lat"]), float(row["lon"]), row["code"])
    elif dataset == "ntrend":
        meta = {}
        for row in _rows(path, first="regionalGroup"):
            lat = (float(row["latSouth"]) + float(row["latNorth"])) / 2
            lon = (float(row["longEast"]) + float(row["longWest"])) / 2
            meta[row["dataID"].lower()] = (lat, lon, row["dataID"])
        sites = meta  # keyed by lower-case id; matched in align_ntrend
    else:
        raise SystemExit(f"unknown dataset {dataset}")
    return sites


def align_ntrend(values, meta):
    out_vals, out_sites = {}, {}
    for col, series in values.items():
        key = col.lower()
        if key.startswith("ag") and key[2:].isdigit():
            key = "asgrid" + key[2:]
        if key == "manx":
            key = "man"
        if key not in meta:
            raise SystemExit(f"N-TREND column {col} has no metadata row")
        out_vals[col] = series
        out_sites[col] = meta[key]
    return out_vals, out_sites


def _rows(path, first=None):
    header = None
    with open(path, encoding="utf-8-sig", errors="replace") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            parts = [p.strip() for p in line.rstrip("\n").split("\t")]
            if header is None:
                if first is None or parts[0] == first:
                    header = parts
                continue
            yield dict(zip(header, parts))


def load_events(path):
    return list(_rows(path))


def exclusion_years(evolv_path, events):
    """Years [E, E+2] for every eVolv2k event with VSSI >= 3 Tg S and every listed event."""
    years = set()
    starts = []
    with open(evolv_path, encoding="utf-8", errors="replace") as fh:
        in_data = False
        header_seen = False
        for line in fh:
            if line.startswith("*/"):
                in_data = True
                continue
            if not in_data:
                continue
            if not header_seen:
                header_seen = True
                continue
            p = line.rstrip("\n").split("\t")
            try:
                e, vssi = int(float(p[0])), float(p[7])
            except (ValueError, IndexError):
                continue
            if vssi >= VSSI_EXCLUDE:
                starts.append(e)
    starts += [int(ev["year"]) for ev in events]
    for e in starts:
        years.update({e, e + 1, e + 2})
    return years, sorted(set(starts))


# ---------------------------------------------------------------- anomalies

def site_sd(series):
    """SD of (value - centred 11-yr running mean) over SD_WINDOW."""
    res = []
    for y in range(SD_WINDOW[0], SD_WINDOW[1] + 1):
        win = [series.get(k) for k in range(y - 5, y + 6)]
        if None in win:
            continue
        res.append(series[y] - sum(win) / 11)
    return statistics.pstdev(res) if len(res) >= 30 else None


def anomalies(values, sites, sds, e, y, excl_starts):
    """Standardized anomaly per site for response year y of an eruption in year e."""
    blocked = set()
    for s in excl_starts:
        if s != e:
            blocked.update({s, s + 1, s + 2})
    refs = [k for k in range(e - 10, e) if k not in blocked]
    out = {}
    if len(refs) < MIN_REF_YEARS:
        return out, refs
    for code, series in values.items():
        if code not in sites or sds.get(code) is None:
            continue
        if y not in series:
            continue
        rv = [series[k] for k in refs if k in series]
        if len(rv) < MIN_REF_YEARS:
            continue
        out[code] = (series[y] - sum(rv) / len(rv)) / sds[code]
    return out, refs


def stats_for(anom, sites):
    hi = [v for c, v in anom.items() if sites[c][0] >= SPLIT_LAT]
    lo = [v for c, v in anom.items() if sites[c][0] < SPLIT_LAT]
    if len(hi) < MIN_PER_GROUP or len(lo) < MIN_PER_GROUP:
        return None
    mh, ml = sum(hi) / len(hi), sum(lo) / len(lo)
    g = mh - ml
    denom = abs(mh) + abs(ml)
    f = g / denom if denom > 0 else 0.0
    xs = [sites[c][0] for c in anom]
    ys = list(anom.values())
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    slope = 10 * sum((x - mx) * (v - my) for x, v in zip(xs, ys)) / sxx if sxx else 0.0
    return {"G": g, "F": f, "S": slope, "mean_hi": mh, "mean_lo": ml,
            "mean_all": my, "n_hi": len(hi), "n_lo": len(lo)}


def event_result(values, sites, sds, e, rule, excl_starts):
    cands = {"select": [e, e + 1], "E": [e], "E1": [e + 1]}[rule]
    best = None
    for y in cands:
        anom, refs = anomalies(values, sites, sds, e, y, excl_starts)
        st = stats_for(anom, sites) if anom else None
        if st is None:
            continue
        st.update({"Y": y, "refs": refs, "anom": anom})
        if best is None or st["mean_all"] < best["mean_all"]:
            best = st
    return best


# ---------------------------------------------------------------- tests

def auc(gx, gt):
    """P(G_X < G_T), ties count half."""
    s = 0.0
    for a in gx:
        for b in gt:
            s += 1.0 if a < b else 0.5 if a == b else 0.0
    return s / (len(gx) * len(gt))


def best_threshold(vals, labels):
    """Threshold t: predict X if G < t. Maximize balanced accuracy; ties -> median candidate."""
    sv = sorted(set(vals))
    cands = [(a + b) / 2 for a, b in zip(sv, sv[1:])] or [sv[0]]
    scored = [(bal_acc([("X" if v < t else "T") for v in vals], labels), t) for t in cands]
    top = max(s for s, _ in scored)
    ties = [t for s, t in scored if s == top]
    return ties[len(ties) // 2], top


def bal_acc(pred, labels):
    out = []
    for cls in ("X", "T"):
        idx = [i for i, l in enumerate(labels) if l == cls]
        if idx:
            out.append(sum(pred[i] == cls for i in idx) / len(idx))
    return sum(out) / len(out)


def loo(vals, labels):
    pred = []
    for i in range(len(vals)):
        v = vals[:i] + vals[i + 1:]
        l = labels[:i] + labels[i + 1:]
        if len(set(l)) < 2:
            pred.append("T")
            continue
        t, _ = best_threshold(v, l)
        pred.append("X" if vals[i] < t else "T")
    return pred, bal_acc(pred, labels)


def hedges_g(a, b):
    na, nb = len(a), len(b)
    if na < 2 or nb < 2:
        return float("nan")
    sp = math.sqrt(((na - 1) * statistics.variance(a) + (nb - 1) * statistics.variance(b)) / (na + nb - 2))
    d = (statistics.mean(a) - statistics.mean(b)) / sp if sp else float("nan")
    return d * (1 - 3 / (4 * (na + nb) - 9))


# ---------------------------------------------------------------- driver

def setup(argv):
    dataset, vpath, spath, epath, evpath = argv[:5]
    opts = dict(zip(argv[5::2], argv[6::2]))
    rule = opts.get("--year-rule", "select")
    year_col = {"schneider": "age_AD", "ntrend": "Year", "grid": "Year"}[dataset]
    values = load_table(vpath, year_col)
    sites = load_sites(dataset, spath)
    if dataset == "ntrend":
        values, sites = align_ntrend(values, sites)
    values = {c: s for c, s in values.items() if c in sites}
    sds = {c: site_sd(s) for c, s in values.items()}
    events = load_events(epath)
    _, starts = exclusion_years(evpath, events)
    return dataset, values, sites, sds, events, starts, rule, opts


def calibrate(argv):
    dataset, values, sites, sds, events, starts, rule, _ = setup(argv)
    n_hi = sum(1 for c in values if sites[c][0] >= SPLIT_LAT)
    print(f"# dataset={dataset} year_rule={rule} sites={len(values)} (>=60N: {n_hi}, <60N: {len(values) - n_hi})")
    print(f"# split={SPLIT_LAT}N min_per_group={MIN_PER_GROUP} exclusion: eVolv2k VSSI>={VSSI_EXCLUDE} + listed events, years E..E+2")
    print("event\tE\tlabel\tY\tn_hi\tn_lo\tmean_hi\tmean_lo\tG\tF\tS_per10deg\tn_ref")
    kept, dropped = [], []
    for ev in events:
        if ev["role"] != "cal":
            continue
        e = int(ev["year"])
        r = event_result(values, sites, sds, e, rule, starts)
        if r is None:
            dropped.append(ev["name"])
            print(f"{ev['name']}\t{e}\t{ev['label']}\tDROPPED (coverage)")
            continue
        kept.append((ev, r))
        print(f"{ev['name']}\t{e}\t{ev['label']}\t{r['Y']}\t{r['n_hi']}\t{r['n_lo']}\t"
              f"{r['mean_hi']:+.2f}\t{r['mean_lo']:+.2f}\t{r['G']:+.2f}\t{r['F']:+.2f}\t{r['S']:+.2f}\t{len(r['refs'])}")
    labels = [ev["label"] for ev, _ in kept]
    print(f"\n# kept {len(kept)} (X={labels.count('X')}, T={labels.count('T')}); dropped {len(dropped)}: {', '.join(dropped) or '-'}")
    if labels.count("X") < 2 or labels.count("T") < 2:
        print("# too few events per class for a test")
        return
    rng = random.Random(SEED)
    perms = [rng.sample(labels, len(labels)) for _ in range(N_PERM)]
    for stat in ("G", "F", "S"):
        vals = [r[stat] for _, r in kept]
        gx = [v for v, l in zip(vals, labels) if l == "X"]
        gt = [v for v, l in zip(vals, labels) if l == "T"]
        a = auc(gx, gt)
        _, lacc = loo(vals, labels)
        t_full, acc_full = best_threshold(vals, labels)
        p_auc = p_loo = 0
        null_auc = []
        for pl in perms:
            px = [v for v, l in zip(vals, pl) if l == "X"]
            pt = [v for v, l in zip(vals, pl) if l == "T"]
            null_auc.append(auc(px, pt))
            if null_auc[-1] >= a:
                p_auc += 1
            if loo(vals, pl)[1] >= lacc:
                p_loo += 1
        print(f"\n## statistic {stat}{'  (PRIMARY)' if stat == 'G' else ''}")
        print(f"median X = {statistics.median(gx):+.2f}   median T = {statistics.median(gt):+.2f}   "
              f"difference = {statistics.median(gx) - statistics.median(gt):+.2f}   Hedges g = {hedges_g(gx, gt):+.2f}")
        print(f"AUC P(X<T) = {a:.3f}   one-sided permutation p = {(p_auc + 1) / (N_PERM + 1):.4f}")
        null_auc.sort()
        print(f"null AUC 95th percentile = {null_auc[int(0.95 * N_PERM)]:.3f} (AUC needed for p < 0.05 with these class sizes)")
        print(f"LOO balanced accuracy = {lacc:.3f}   permutation p = {(p_loo + 1) / (N_PERM + 1):.4f}")
        print(f"full-data threshold: X if {stat} < {t_full:+.3f} (in-sample balanced accuracy {acc_full:.3f})")


def classify(argv):
    dataset, values, sites, sds, events, starts, rule, opts = setup(argv)
    kept = []
    for ev in events:
        if ev["role"] != "cal":
            continue
        r = event_result(values, sites, sds, int(ev["year"]), rule, starts)
        if r is not None:
            kept.append((ev, r))
    labels = [ev["label"] for ev, _ in kept]
    target = [ev for ev in events if ev["role"] == "target"][0]
    e = int(target["year"])
    if "--target-year" in opts:
        y = int(opts["--target-year"])
        anom, refs = anomalies(values, sites, sds, e, y, starts)
        r = stats_for(anom, sites)
        r.update({"Y": y, "refs": refs, "anom": anom})
    else:
        r = event_result(values, sites, sds, e, rule, starts)
    print(f"# dataset={dataset} year_rule={rule} target={target['name']} E={e} Y={r['Y']} ref years={r['refs']}")
    print("site\tlat\tz_anomaly")
    for c, v in sorted(r["anom"].items(), key=lambda kv: -sites[kv[0]][0]):
        print(f"{sites[c][2]}\t{sites[c][0]:.1f}\t{v:+.2f}")
    print(f"\nn_hi={r['n_hi']} n_lo={r['n_lo']} mean_hi={r['mean_hi']:+.2f} mean_lo={r['mean_lo']:+.2f} mean_all={r['mean_all']:+.2f}")
    rng = random.Random(SEED)
    hi = [c for c in r["anom"] if sites[c][0] >= SPLIT_LAT]
    lo = [c for c in r["anom"] if sites[c][0] < SPLIT_LAT]
    for stat in ("G", "F", "S"):
        vals = [k[stat] for _, k in kept]
        t_full, _ = best_threshold(vals, labels)
        boots = []
        for _ in range(N_BOOT):
            sample = {}
            for i, c in enumerate(rng.choices(hi, k=len(hi)) + rng.choices(lo, k=len(lo))):
                sample[f"{c}#{i}"] = r["anom"][c]
            b_sites = {k: sites[k.split('#')[0]] for k in sample}
            boots.append(stats_for(sample, b_sites)[stat])
        boots.sort()
        lo95, hi95 = boots[int(0.025 * N_BOOT)], boots[int(0.975 * N_BOOT) - 1]
        share_x = sum(b < t_full for b in boots) / N_BOOT
        gx = sorted(v for v, l in zip(vals, labels) if l == "X")
        gt = sorted(v for v, l in zip(vals, labels) if l == "T")
        below_x = sum(v < r[stat] for v in gx)
        below_t = sum(v < r[stat] for v in gt)
        print(f"\n## {stat}{'  (PRIMARY)' if stat == 'G' else ''}: target = {r[stat]:+.2f}  95% bootstrap [{lo95:+.2f}, {hi95:+.2f}]")
        print(f"threshold (all {len(kept)} calibration events): X if < {t_full:+.3f} -> target side: {'X' if r[stat] < t_full else 'T'}; "
              f"bootstrap share on X side = {share_x:.3f}")
        print(f"X events with lower {stat}: {below_x}/{len(gx)}   T events with lower {stat}: {below_t}/{len(gt)}")
        print(f"X values: {' '.join(f'{v:+.2f}' for v in gx)}")
        print(f"T values: {' '.join(f'{v:+.2f}' for v in gt)}")


if __name__ == "__main__":
    if len(sys.argv) < 7 or sys.argv[1] not in ("calibrate", "classify"):
        print(__doc__)
        sys.exit(2)
    {"calibrate": calibrate, "classify": classify}[sys.argv[1]](sys.argv[2:])

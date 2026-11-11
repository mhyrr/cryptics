"""Exp 02: triage Poli's 1,766 long-period detections into classes. Standard library only.

Thresholds were fixed from exp 01 before this script was run on the target:
  R_LOC   = 350 km   (exp 01: known landslides sit 29-317 km from Poli's grid location)
  EQ rule = a ComCat M>=4 event within +-600 s and 1000 km  (exp 01: |dt| up to 394 s)
Flags, none of which is an attribution:
  eq        catalogued earthquake coincident under the EQ rule
  bigeq     any M>=6.5 earthquake worldwide in the preceding 3 h (surface-wave trains)
  known     matches an ESEC v4 attributed mass movement (exp 01 rule)
  region    antarctic | greenland | ocean | land  (from a 37-point sample of the R_LOC disk)
  nbr       other Poli detections within 150 km at any date (repeating source)
Control: the EQ rule re-run with Poli times shifted by whole days gives its chance rate.

Run: python3 fetch.py && python3 triage.py   (writes triage.tsv, result.txt)
"""
import bisect, csv, gzip, json, math, os, statistics, sys
from collections import Counter
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
sys.path.insert(0, os.path.join(HERE, "..", "01-poli-x-esec"))
from crossmatch import hav, load_esec, load_poli, match  # noqa: E402

R_LOC, EQ_DT, EQ_KM, NBR_KM = 350.0, 600.0, 1000.0, 150.0
S2_START = datetime(2015, 7, 1, tzinfo=timezone.utc)


def load_comcat():
    ev = []
    with gzip.open(os.path.join(DATA, "comcat-m4-2010-2023.csv.gz"), "rt") as f:
        for r in csv.DictReader(f):
            t = datetime.strptime(r["time"][:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc).timestamp()
            ev.append((t, float(r["lat"]), float(r["lon"]), float(r["mag"]), r["id"]))
    ev.sort()
    return ev


def load_polys():
    polys = []
    for f in json.load(open(os.path.join(DATA, "ne_110m_admin_0_countries.geojson")))["features"]:
        name = f["properties"]["ADMIN"]
        g = f["geometry"]
        parts = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
        for part in parts:
            ring = part[0]
            xs, ys = [p[0] for p in ring], [p[1] for p in ring]
            polys.append((name, min(xs), max(xs), min(ys), max(ys), ring))
    return polys


def country(polys, lat, lon):
    for name, x0, x1, y0, y1, ring in polys:
        if not (x0 <= lon <= x1 and y0 <= lat <= y1):
            continue
        inside = False
        j = len(ring) - 1
        for i in range(len(ring)):
            xi, yi = ring[i][0], ring[i][1]
            xj, yj = ring[j][0], ring[j][1]
            if (yi > lat) != (yj > lat) and lon < (xj - xi) * (lat - yi) / (yj - yi) + xi:
                inside = not inside
            j = i
        if inside:
            return name
    return None


def dest(lat, lon, km, az):
    d, a = km / 6371.0, math.radians(az)
    p1, l1 = math.radians(lat), math.radians(lon)
    p2 = math.asin(math.sin(p1) * math.cos(d) + math.cos(p1) * math.sin(d) * math.cos(a))
    l2 = l1 + math.atan2(math.sin(a) * math.sin(d) * math.cos(p1), math.cos(d) - math.sin(p1) * math.sin(p2))
    return math.degrees(p2), (math.degrees(l2) + 540) % 360 - 180


def disk_countries(polys, lat, lon):
    pts = [(lat, lon)] + [dest(lat, lon, r, az) for r in (120, 240, R_LOC) for az in range(0, 360, 30)]
    c = Counter(country(polys, la, lo) for la, lo in pts)
    return c


def eq_hits(comcat, times, t, lat, lon):
    i, j = bisect.bisect_left(times, t - EQ_DT), bisect.bisect_right(times, t + EQ_DT)
    best = None
    for k in range(i, j):
        _, la, lo, mag, eid = comcat[k]
        km = hav(lat, lon, la, lo)
        if km <= EQ_KM and (best is None or mag > best[0]):
            best = (mag, km, comcat[k][0] - t, eid)
    return best


def main():
    poli, esec = load_poli(), load_esec()
    comcat = load_comcat(); times = [e[0] for e in comcat]
    big = [e[0] for e in comcat if e[3] >= 6.5]
    polys = load_polys()
    known = {p["id"]: e for e, p, dt, km in match(poli, esec)}
    rows = []
    for p in poli:
        t = p["t"].timestamp()
        eq = eq_hits(comcat, times, t, p["lat"], p["lon"])
        bi = bisect.bisect_left(big, t - 3 * 3600); bj = bisect.bisect_right(big, t)
        c = disk_countries(polys, p["lat"], p["lon"])
        land_pts = sum(v for k, v in c.items() if k)
        names = [k for k, _ in c.most_common() if k]
        if p["lat"] <= -60 or "Antarctica" in names:
            region = "antarctic"
        elif "Greenland" in names:
            region = "greenland"
        elif land_pts == 0:
            region = "ocean"
        else:
            region = "land"
        nbr = sum(1 for q in poli if q["id"] != p["id"] and hav(p["lat"], p["lon"], q["lat"], q["lon"]) <= NBR_KM)
        rows.append(dict(p, eq=eq, bigeq=bj > bi, region=region, land_pts=land_pts, countries=";".join(names[:4]),
                         nbr=nbr, known=known.get(p["id"]), s2=p["t"] >= S2_START))
    # chance rate of the EQ rule
    chance = []
    for s in list(range(-30, 0)) + list(range(1, 31)):
        chance.append(sum(1 for p in poli if eq_hits(comcat, times, p["t"].timestamp() + s * 86400, p["lat"], p["lon"])))

    L = []
    n = len(rows)
    L.append(f"Poli detections: {n}")
    L.append(f"eq flag (ComCat M>=4, +-{EQ_DT:.0f} s, {EQ_KM:.0f} km): {sum(1 for r in rows if r['eq'])}"
             f"   chance (60 day-shifts): mean {statistics.mean(chance):.1f}, max {max(chance)}")
    L.append(f"bigeq flag (M>=6.5 anywhere in prior 3 h): {sum(1 for r in rows if r['bigeq'])}")
    L.append(f"known (ESEC v4 match): {len(known)}")
    L.append("region: " + ", ".join(f"{k} {v}" for k, v in Counter(r["region"] for r in rows).most_common()))
    L.append("")
    L.append("Repeat-source check on the known landslides (nbr = other detections within 150 km):")
    L.append("  " + ", ".join(f"{r['known']['name']}={r['nbr']}" for r in rows if r["known"]))
    L.append("nbr distribution, all detections: " + ", ".join(
        f"{lab} {sum(1 for r in rows if lo <= r['nbr'] <= hi)}" for lab, lo, hi in
        [("0", 0, 0), ("1-2", 1, 2), ("3-9", 3, 9), ("10-29", 10, 29), ("30+", 30, 10**6)]))
    L.append("")
    cand = [r for r in rows if r["region"] == "land" and not r["eq"] and not r["known"]]
    L.append(f"Residual (region=land, no eq flag, not ESEC-known): {len(cand)}")
    L.append(f"  of which no bigeq flag: {sum(1 for r in cand if not r['bigeq'])}")
    for lab, lo, hi in [("nbr 0", 0, 0), ("nbr 1-2", 1, 2), ("nbr 3-9", 3, 9), ("nbr 10+", 10, 10**6)]:
        sub = [r for r in cand if lo <= r["nbr"] <= hi and not r["bigeq"]]
        L.append(f"  {lab}: {len(sub)}  (Sentinel-2 era: {sum(1 for r in sub if r['s2'])})")
    L.append("")
    L.append("Residual by leading country in the disk (no bigeq), top 25:")
    cc = Counter(r["countries"].split(";")[0] for r in cand if not r["bigeq"])
    L.append("  " + ", ".join(f"{k} {v}" for k, v in cc.most_common(25)))
    txt = "\n".join(L) + "\n"
    open(os.path.join(HERE, "result.txt"), "w").write(txt)
    with open(os.path.join(HERE, "triage.tsv"), "w") as f:
        f.write("poli_id\ttime\tlat\tlon\tMw_d\tregion\tland_pts\tcountries\tnbr\ts2_era\tbigeq\teq_mag\teq_km\teq_dt_s\teq_id\tesec_known\n")
        for r in rows:
            e = r["eq"]
            f.write(f"{r['id']}\t{r['t']:%Y-%m-%dT%H:%M:%S}\t{r['lat']}\t{r['lon']}\t{r['mw']:.2f}\t{r['region']}\t{r['land_pts']}\t"
                    f"{r['countries']}\t{r['nbr']}\t{int(r['s2'])}\t{int(r['bigeq'])}\t"
                    + (f"{e[0]}\t{e[1]:.0f}\t{e[2]:.0f}\t{e[3]}" if e else "\t\t\t")
                    + f"\t{r['known']['name'] if r['known'] else ''}\n")
    print(txt)


if __name__ == "__main__":
    main()

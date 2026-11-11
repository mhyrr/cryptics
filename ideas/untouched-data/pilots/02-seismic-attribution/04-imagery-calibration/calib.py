"""Exp 04a: does detector v1 find known scars in their own tile, and what does it fire on when nothing happened?

Positives: ESEC v4 mass movements from 2017-07-01 with volume >= 1e6 m3 (types with 'calving',
'outburst flood', 'snow avalanche' excluded). For each, the Sentinel-2 tile over the ESEC location.
  hit      a blob whose centroid is within 5 km of the ESEC location; its rank among the tile's blobs
Control: the same tile and the same calendar windows one year earlier.
  ctrl_ge  control-year blobs scoring at least as high as the hit (false positives per tile at that score)

Run: uv run python calib.py   (writes calib.tsv, result.txt)
"""
import csv, math, os, sys, traceback
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone

import s2

HERE = os.path.dirname(os.path.abspath(__file__))
SKIP = ("calving", "outburst flood", "snow avalanche", "flume", "lahar")


def hav(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    a = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(lon2 - lon1) / 2) ** 2
    return 6371.0 * 2 * math.asin(math.sqrt(a))


def events():
    rows = list(csv.DictReader(open(os.path.join(HERE, "..", "data", "esec-v4-Events.csv"), encoding="utf-8-sig")))[1:]
    out = []
    for r in rows:
        try:
            t = datetime.strptime(r["StartTime"][:19], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            vol = float(r["Volume"])
        except ValueError:
            continue
        if t < datetime(2017, 7, 1, tzinfo=timezone.utc) or vol < 1e6 or any(s in r["Type"] for s in SKIP):
            continue
        out.append(dict(eid=r["Eid"], name=r["Name"], type=r["Type"], t=t, lat=float(r["Latitude"]), lon=float(r["Longitude"]), vol=vol))
    return out


def run_window(pool, lat, lon, t):
    (a0, a1), (b0, b1) = s2.windows(t)
    tile, pre_items = s2.pick(s2.search(lon, lat, a0, a1))
    post_all = [it for it in s2.search(lon, lat, b0, b1) if s2.tile_of(it) == tile]
    post_items = sorted(post_all, key=lambda it: it["properties"]["eo:cloud_cover"])[:4]
    if not pre_items or not post_items:
        return None
    pre, post = s2.composite(pre_items, pool), s2.composite(post_items, pool)
    return dict(tile=tile, blobs=s2.detect(pre, post), valid=s2.valid_fraction(pre, post), npre=len(pre_items), npost=len(post_items))


def main():
    evs = events()
    only = set(sys.argv[1:])
    if only:
        evs = [e for e in evs if e["eid"] in only]
    pool = ThreadPoolExecutor(12)
    rows = []
    for e in evs:
        try:
            ev = run_window(pool, e["lat"], e["lon"], e["t"])
            ct = run_window(pool, e["lat"], e["lon"], e["t"] - timedelta(days=365))
        except Exception:
            traceback.print_exc(); ev = ct = None
        row = dict(e, status="no-imagery")
        if ev:
            near = [(i + 1, b, hav(e["lat"], e["lon"], b["lat"], b["lon"])) for i, b in enumerate(ev["blobs"])]
            near = [x for x in near if x[2] <= 5.0]
            hit = near[0] if near else None
            row.update(status="hit" if hit else "miss", tile=ev["tile"], valid=ev["valid"], nblobs=len(ev["blobs"]),
                       rank=hit[0] if hit else "", hit_area=hit[1]["area_px"] if hit else "", hit_score=hit[1]["score"] if hit else "",
                       hit_kind=hit[1]["kind"] if hit else "", hit_km=hit[2] if hit else "")
            if ct:
                row.update(ctrl_nblobs=len(ct["blobs"]), ctrl_valid=ct["valid"],
                           ctrl_ge=sum(1 for b in ct["blobs"] if hit and b["score"] >= hit[1]["score"]) if hit else "")
        rows.append(row)
        print(f"{e['eid']:>4} {e['name'][:34]:34} {e['t']:%Y-%m-%d} vol {e['vol']:.1e}  {row['status']:10} "
              f"rank {row.get('rank','')}/{row.get('nblobs','')}  area {row.get('hit_area','')}  valid {row.get('valid',0):.2f}  "
              f"ctrl blobs {row.get('ctrl_nblobs','')} ge {row.get('ctrl_ge','')}", flush=True)
    cols = ["eid", "name", "type", "t", "lat", "lon", "vol", "status", "tile", "valid", "nblobs", "rank", "hit_area", "hit_score",
            "hit_kind", "hit_km", "ctrl_nblobs", "ctrl_valid", "ctrl_ge"]
    if not only:
        with open(os.path.join(HERE, "calib.tsv"), "w") as f:
            f.write("\t".join(cols) + "\n")
            for r in rows:
                f.write("\t".join(str(r.get(c, "")) for c in cols) + "\n")
        img = [r for r in rows if r["status"] != "no-imagery"]
        hits = [r for r in img if r["status"] == "hit"]
        L = [f"Positives: {len(rows)}; with imagery: {len(img)}; hit within 5 km: {len(hits)}",
             f"Hit ranked 1st in its tile: {sum(1 for r in hits if r['rank'] == 1)}; in top 5: {sum(1 for r in hits if r['rank'] <= 5)}; in top 20: {sum(1 for r in hits if r['rank'] <= 20)}",
             f"Blobs per event tile: median {sorted(r['nblobs'] for r in img)[len(img)//2]}",
             f"Blobs per control tile: median {sorted(r.get('ctrl_nblobs', 0) or 0 for r in img)[len(img)//2]}"]
        open(os.path.join(HERE, "result.txt"), "w").write("\n".join(L) + "\n")
        print("\n".join(L))


if __name__ == "__main__":
    main()

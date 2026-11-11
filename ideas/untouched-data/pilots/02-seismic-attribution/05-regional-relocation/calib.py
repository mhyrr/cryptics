"""Exp 05a: location error of locate.py on attributed landslides.

Positives: ESEC v4 events 2010-2025 with volume >= 1e6 m3 (calving, floods, snow avalanches,
lahars and flume tests excluded). The search is centred 1.0 deg N and 1.5 deg E of the true
location, so the truth is never at the centre of the grid. T is the ESEC start time + 110 s
(the median Poli offset from exp 01), so the time is as rough as it will be on the target.

Run: uv run python calib.py   (writes calib.tsv, result.txt)
"""
import csv, os, statistics
from datetime import datetime, timedelta

import locate

HERE = os.path.dirname(os.path.abspath(__file__))
SKIP = ("calving", "outburst flood", "snow avalanche", "flume", "lahar")


def main():
    rows = list(csv.DictReader(open(os.path.join(HERE, "..", "data", "esec-v4-Events.csv"), encoding="utf-8-sig")))[1:]
    out = []
    for r in rows:
        try:
            t = datetime.strptime(r["StartTime"][:19], "%Y-%m-%d %H:%M:%S"); vol = float(r["Volume"])
            lat, lon = float(r["Latitude"]), float(r["Longitude"])
        except ValueError:
            continue
        if t.year < 2010 or vol < 1e6 or any(s in r["Type"] for s in SKIP):
            continue
        res = locate.locate(lat + 1.0, lon + 1.5, (t + timedelta(seconds=110)).isoformat())
        err = float(locate.hav(lat, lon, res["lat"], res["lon"])) if "lat" in res else None
        out.append(dict(eid=r["Eid"], name=r["Name"], t=t, vol=vol, err=err, **res))
        print(f"{r['Eid']:>4} {r['Name'][:32]:32} {t:%Y-%m-%d} nsta {res['nsta']:>2} "
              + (f"err {err:6.0f} km  stack {res['stack']:.2f}  contrast {res['contrast']:.2f}  nearest sta {res['near_km']:.0f} km" if err is not None else "too few stations"), flush=True)
    cols = ["eid", "name", "t", "vol", "nsta", "err", "lat", "lon", "stack", "contrast", "near_km", "t0"]
    with open(os.path.join(HERE, "calib.tsv"), "w") as f:
        f.write("\t".join(cols) + "\n")
        for o in out:
            f.write("\t".join(str(o.get(c, "")) for c in cols) + "\n")
    loc = sorted(o["err"] for o in out if o["err"] is not None)
    L = [f"Positives: {len(out)}; located (>= 5 stations kept): {len(loc)}"]
    if loc:
        L.append(f"Location error km: median {statistics.median(loc):.0f}; within 25 km: {sum(e <= 25 for e in loc)}; within 50 km: {sum(e <= 50 for e in loc)}; within 100 km: {sum(e <= 100 for e in loc)}; max {loc[-1]:.0f}")
        L.append("Start offset imposed on the search centre: 139-190 km depending on latitude")
    open(os.path.join(HERE, "result.txt"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()

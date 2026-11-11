"""Exp 05b: locate.py (method v1, calibrated in 05a) on the exp-02 residual.

Search centre = Poli's grid point; T = Poli's time (calib.py used start + 110 s, the same thing).
Where exp 03b found a TIMED ISC event, the distance from our location to that epicentre is
reported as an independent cross-check.

Run: uv run python target.py   (writes target.tsv)
"""
import csv, os

import locate

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    rows = [r for r in csv.DictReader(open(os.path.join(HERE, "..", "02-triage", "triage.tsv")), delimiter="\t")
            if r["region"] == "land" and not r["eq_id"] and not r["esec_known"]]
    timed = {r["poli_id"]: r for r in csv.DictReader(open(os.path.join(HERE, "..", "03-reference-sweep", "timed.tsv")), delimiter="\t")}
    cols = ["poli_id", "time", "grid_lat", "grid_lon", "Mw_d", "nsta", "lat", "lon", "km_from_grid", "stack", "contrast", "near_km", "t0",
            "isc_lat", "isc_lon", "isc_mag", "km_from_isc"]
    with open(os.path.join(HERE, "target.tsv"), "w") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            glat, glon = float(r["lat"]), float(r["lon"])
            try:
                res = locate.locate(glat, glon, r["time"])
            except Exception as e:
                res = dict(nsta=-1); print("ERR", r["poli_id"], e)
            o = dict(poli_id=r["poli_id"], time=r["time"], grid_lat=glat, grid_lon=glon, Mw_d=r["Mw_d"], **res)
            if "lat" in res:
                o["km_from_grid"] = f"{float(locate.hav(glat, glon, res['lat'], res['lon'])):.0f}"
                for k in ("lat", "lon"):
                    o[k] = f"{res[k]:.2f}"
                for k in ("stack", "contrast"):
                    o[k] = f"{res[k]:.2f}"
                o["near_km"] = f"{res['near_km']:.0f}"
            t = timed.get(r["poli_id"])
            if t:
                o.update(isc_lat=t["isc_lat"], isc_lon=t["isc_lon"], isc_mag=t["isc_mag"])
                if "lat" in res:
                    o["km_from_isc"] = f"{float(locate.hav(float(t['isc_lat']), float(t['isc_lon']), res['lat'], res['lon'])):.0f}"
            f.write("\t".join(str(o.get(c, "")) for c in cols) + "\n"); f.flush()
            print("\t".join(str(o.get(c, "")) for c in cols), flush=True)


if __name__ == "__main__":
    main()

"""Exp 03 (code half): check the exp-02 residual against the ISC bulletin and GVP eruptions.

For each residual detection (region=land, no ComCat match, not ESEC-known):
  isc      ISC bulletin events of any magnitude within +-600 s and 9 degrees (about 1,000 km).
           Same rule as exp 02, fuller catalog. Control: the same query at +-7 and +-14 days.
  gvp      GVP eruptions (1960-) within 350 km that were in progress on the date, and whether
           one of them started within +-30 days of the detection.
  offshore the detection's grid point and a 120 km ring around it are all sea (1:110m mask).
Flags only. Nothing here is an attribution.

Run: python3 sweep.py   (standard library; ISC responses cached in cache/; writes sweep.tsv, result.txt)
"""
import csv, json, os, statistics, sys, time, urllib.request
from collections import Counter
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "02-triage"))
sys.path.insert(0, os.path.join(HERE, "..", "01-poli-x-esec"))
from crossmatch import hav  # noqa: E402
from triage import country, dest, load_polys  # noqa: E402

UA = {"User-Agent": "Mozilla/5.0"}
CACHE = os.path.join(HERE, "cache")
SHIFTS = (-14, -7, 7, 14)


def get(u, tries=5):
    for i in range(tries):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120)
            return r.read().decode(errors="replace")
        except Exception as e:
            err = e; time.sleep(5 * (i + 1))
    raise err


def isc(pid, t, lat, lon, shift):
    f = os.path.join(CACHE, f"isc_{pid}_{shift:+d}.txt")
    if not os.path.exists(f):
        t0 = t + timedelta(days=shift)
        u = ("http://www.isc.ac.uk/fdsnws/event/1/query?format=text"
             f"&starttime={(t0 - timedelta(seconds=600)):%Y-%m-%dT%H:%M:%S}&endtime={(t0 + timedelta(seconds=600)):%Y-%m-%dT%H:%M:%S}"
             f"&latitude={lat}&longitude={lon}&maxradius=9")
        open(f, "w").write(get(u)); time.sleep(1.5)
    ev = []
    for line in open(f):
        p = line.strip().split("|")
        if line.startswith("#") or len(p) < 11:
            continue
        try:
            la, lo = float(p[2]), float(p[3])
        except ValueError:
            continue
        mag = float(p[10]) if p[10] else None
        ev.append(dict(id=p[0], time=p[1], lat=la, lon=lo, mag=mag, magtype=p[9], km=hav(lat, lon, la, lo)))
    return ev


def load_gvp():
    f = os.path.join(CACHE, "gvp_eruptions1960.json")
    if not os.path.exists(f):
        open(f, "w").write(get("https://webservices.volcano.si.edu/geoserver/GVP-VOTW/ows?service=WFS&version=1.0.0"
                               "&request=GetFeature&outputFormat=application/json&typeName=GVP-VOTW:E3WebApp_Eruptions1960"))
    out = []
    for ft in json.load(open(f))["features"]:
        p = ft["properties"]
        def d(y, m, dd, default):
            if not y:
                return default
            return datetime(y, max(m or 1, 1), max(dd or 1, 1), tzinfo=timezone.utc)
        s = d(p["StartDateYear"], p["StartDateMonth"], p["StartDateDay"], None)
        if s is None:
            continue
        cont = str(p.get("ContinuingEruption")) == "True"
        e = datetime(2100, 1, 1, tzinfo=timezone.utc) if cont else d(p["EndDateYear"], p["EndDateMonth"], p["EndDateDay"], s)
        out.append(dict(name=p["VolcanoName"], lat=p["LatitudeDecimal"], lon=p["LongitudeDecimal"], s=s, e=e, vei=p["ExplosivityIndexMax"]))
    return out


def main():
    rows = [r for r in csv.DictReader(open(os.path.join(HERE, "..", "02-triage", "triage.tsv")), delimiter="\t")
            if r["region"] == "land" and not r["eq_id"] and not r["esec_known"]]
    polys, gvp = load_polys(), load_gvp()
    out, chance = [], []
    for r in rows:
        pid, lat, lon = r["poli_id"], float(r["lat"]), float(r["lon"])
        t = datetime.strptime(r["time"], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
        ev = isc(pid, t, lat, lon, 0)
        chance.append(sum(1 for s in SHIFTS if isc(pid, t, lat, lon, s)) / len(SHIFTS))
        best = max(ev, key=lambda e: (e["mag"] or 0, -e["km"])) if ev else None
        near = [(hav(lat, lon, g["lat"], g["lon"]), g) for g in gvp if g["s"] - timedelta(days=30) <= t <= g["e"] + timedelta(days=30)]
        near = sorted([(km, g) for km, g in near if km <= 350], key=lambda x: x[0])
        onset = [(km, g) for km, g in near if abs((g["s"] - t).days) <= 30]
        ring = [(lat, lon)] + [dest(lat, lon, 120, az) for az in range(0, 360, 30)]
        offshore = all(country(polys, la, lo) is None for la, lo in ring)
        out.append(dict(r, isc_n=len(ev), isc=best, gvp=near, gvp_onset=onset, offshore=offshore))
    L = []
    n = len(out)
    L.append(f"Residual detections checked: {n}")
    L.append(f"ISC event within +-600 s and 9 deg: {sum(1 for o in out if o['isc_n'])}   "
             f"chance (mean of 4 shifted windows per detection): {sum(chance):.1f} expected")
    L.append(f"  of which ISC magnitude >= 4: {sum(1 for o in out if o['isc'] and (o['isc']['mag'] or 0) >= 4)}")
    L.append(f"GVP eruption in progress within 350 km: {sum(1 for o in out if o['gvp'])}; started within +-30 d: {sum(1 for o in out if o['gvp_onset'])}")
    L.append(f"Offshore (grid point and 120 km ring all sea): {sum(1 for o in out if o['offshore'])}")
    clean = [o for o in out if not o["isc_n"] and not o["gvp_onset"] and not o["offshore"]]
    L.append(f"Unflagged (no ISC event, no eruption onset, not offshore): {len(clean)}  "
             f"(Sentinel-2 era: {sum(1 for o in clean if o['s2_era'] == '1')})")
    L.append("")
    L.append("Unflagged detections:")
    for o in clean:
        g = f"  [eruption in progress: {o['gvp'][0][1]['name']} {o['gvp'][0][0]:.0f} km]" if o["gvp"] else ""
        L.append(f"  {o['poli_id']:>5}  {o['time']}  {float(o['lat']):6.1f} {float(o['lon']):7.1f}  Mw_d {o['Mw_d']}  nbr {o['nbr']}  {o['countries']}{g}")
    txt = "\n".join(L) + "\n"
    open(os.path.join(HERE, "result.txt"), "w").write(txt)
    with open(os.path.join(HERE, "sweep.tsv"), "w") as f:
        f.write("poli_id\ttime\tlat\tlon\tMw_d\tcountries\tnbr\ts2_era\toffshore\tisc_n\tisc_best_mag\tisc_best_km\tisc_best_time\tisc_best_id\tgvp_in_progress\tgvp_onset_30d\n")
        for o in out:
            b = o["isc"]
            f.write("\t".join([o["poli_id"], o["time"], o["lat"], o["lon"], o["Mw_d"], o["countries"], o["nbr"], o["s2_era"],
                               str(int(o["offshore"])), str(o["isc_n"]),
                               (str(b["mag"]) if b and b["mag"] is not None else ""), (f"{b['km']:.0f}" if b else ""),
                               (b["time"] if b else ""), (b["id"] if b else ""),
                               ";".join(f"{g['name']}({km:.0f}km)" for km, g in o["gvp"][:3]),
                               ";".join(f"{g['name']}({km:.0f}km,{g['s']:%Y-%m-%d})" for km, g in o["gvp_onset"][:3])]) + "\n")
    print(txt)


if __name__ == "__main__":
    main()

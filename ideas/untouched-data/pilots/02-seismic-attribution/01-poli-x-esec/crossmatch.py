"""Exp 01: cross-match Poli's long-period catalog against attributed mass movements (ESEC v4).

Question: when Poli's detector records a landslide whose true place and time are known,
how far off is its 0.5-degree grid location and its origin time? The answer sets the
search radius and time window for every later step.

Control: the same match run with Poli's times shifted by whole days (+-1..+-100). A shift
keeps the catalog's geography and time-of-day structure and destroys real coincidences,
so the shifted match count is the chance rate.

Run: python3 crossmatch.py   (standard library only; writes result.txt and matches.tsv)
"""
import csv, math, os, statistics
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
MAX_DT_S = 600      # generous on purpose; the result reports the observed spread
MAX_KM = 1000.0


def hav(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    a = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(lon2 - lon1) / 2) ** 2
    return 6371.0 * 2 * math.asin(math.sqrt(a))


def load_poli():
    out = []
    for r in csv.DictReader(open(os.path.join(DATA, "poli-2023-catalog.csv"))):
        t = datetime.strptime(r["date"][:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
        out.append(dict(id=int(r[""]), lat=float(r["lat"]), lon=float(r["lon"]), t=t, mw=float(r["Mw_d"])))
    return out


def load_esec():
    rows = list(csv.DictReader(open(os.path.join(DATA, "esec-v4-Events.csv"), encoding="utf-8-sig")))[1:]
    out = []
    for r in rows:
        try:
            t = datetime.strptime(r["StartTime"][:19], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            lat, lon = float(r["Latitude"]), float(r["Longitude"])
        except ValueError:
            continue
        vol = float(r["Volume"]) if r["Volume"] else None
        out.append(dict(eid=r["Eid"], name=r["Name"], type=r["Type"], t=t, lat=lat, lon=lon, vol=vol,
                        nlp=int(r["numLPdet"] or 0), maxlp=r["maxdistLP_km"]))
    return out


def match(poli, esec, shift_days=0):
    hits = []
    d = timedelta(days=shift_days)
    for e in esec:
        for p in poli:
            dt = ((p["t"] + d) - e["t"]).total_seconds()
            if abs(dt) <= MAX_DT_S:
                km = hav(p["lat"], p["lon"], e["lat"], e["lon"])
                if km <= MAX_KM:
                    hits.append((e, p, dt, km))
    return hits


def main():
    poli, esec = load_poli(), load_esec()
    t0, t1 = min(p["t"] for p in poli), max(p["t"] for p in poli)
    pad = timedelta(seconds=MAX_DT_S)
    inwin = [e for e in esec if t0 - pad <= e["t"] <= t1 + pad]
    big = [e for e in inwin if e["vol"] and e["vol"] >= 1e6]
    lp = [e for e in inwin if e["nlp"] > 0]
    hits = match(poli, inwin)
    shifts = [s for s in range(-100, 101) if s != 0]
    chance = [len(match(poli, inwin, s)) for s in shifts]
    L = []
    L.append(f"Poli catalog: {len(poli)} events, {t0:%Y-%m-%d} to {t1:%Y-%m-%d}")
    L.append(f"ESEC v4: {len(esec)} dated events; {len(inwin)} inside Poli's time span; "
             f"{len(big)} of those with volume >= 1e6 m3; {len(lp)} with >=1 long-period detection in ESEC")
    L.append(f"Match rule: |dt| <= {MAX_DT_S} s and distance <= {MAX_KM:.0f} km")
    L.append(f"Matches: {len(hits)}  (distinct ESEC events: {len({h[0]['eid'] for h in hits})})")
    L.append(f"Chance control, {len(shifts)} whole-day shifts: mean {statistics.mean(chance):.3f} matches, "
             f"max {max(chance)}, shifts with any match {sum(1 for c in chance if c)}")
    if hits:
        kms = sorted(h[3] for h in hits); dts = sorted(h[2] for h in hits)
        L.append(f"Location error km: min {kms[0]:.0f}, median {statistics.median(kms):.0f}, max {kms[-1]:.0f}")
        L.append(f"Time offset s (Poli minus ESEC start): min {dts[0]:.0f}, median {statistics.median(dts):.0f}, max {dts[-1]:.0f}")
    matched = {h[0]["eid"] for h in hits}
    L.append(f"Recall on ESEC volume >= 1e6 m3: {sum(1 for e in big if e['eid'] in matched)}/{len(big)}")
    L.append(f"Recall on ESEC events with long-period detections: {sum(1 for e in lp if e['eid'] in matched)}/{len(lp)}")
    L.append("")
    L.append("eid\tname\ttype\tesec_time\tvolume_m3\tpoli_id\tpoli_lat\tpoli_lon\tMw_d\tdt_s\tkm")
    rows = []
    for e, p, dt, km in sorted(hits, key=lambda h: h[0]["t"]):
        rows.append(f"{e['eid']}\t{e['name']}\t{e['type']}\t{e['t']:%Y-%m-%d %H:%M:%S}\t{e['vol'] or ''}\t"
                    f"{p['id']}\t{p['lat']}\t{p['lon']}\t{p['mw']:.2f}\t{dt:.0f}\t{km:.0f}")
    open(os.path.join(HERE, "matches.tsv"), "w").write(L[-1] + "\n" + "\n".join(rows) + "\n")
    L += rows
    L.append("")
    L.append("Largest ESEC events in span NOT matched (volume >= 1e7 m3):")
    for e in sorted(big, key=lambda e: -e["vol"]):
        if e["eid"] not in matched and e["vol"] >= 1e7:
            L.append(f"  {e['eid']}\t{e['name']}\t{e['t']:%Y-%m-%d}\t{e['vol']:.2e}\tnumLPdet={e['nlp']}")
    txt = "\n".join(L) + "\n"
    open(os.path.join(HERE, "result.txt"), "w").write(txt)
    print(txt)


if __name__ == "__main__":
    main()

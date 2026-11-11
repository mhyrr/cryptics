"""Exp 03b: are the small ISC events near the residual detections the same sources?

Exp 01 found that Poli's time is 47-176 s after a known landslide's start. Rule fixed from that:
an ISC event is TIMED if its origin precedes the Poli time by 30-180 s (within 9 degrees).
Chance: the same rule on the four day-shifted windows per detection already cached by sweep.py.
For each TIMED event the ISC epicentre is a regional-network location, far tighter than Poli's grid.

Run after sweep.py: python3 timed.py   (reads cache/, writes timed.tsv, timed-result.txt)
"""
import csv, os, sys
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sweep import SHIFTS, isc  # noqa: E402

LO, HI = 30, 180


def parse(s):
    return datetime.strptime(s[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)


def timed(ev, t):
    out = []
    for e in ev:
        lag = (t - parse(e["time"])).total_seconds()
        if LO <= lag <= HI:
            out.append((lag, e))
    return out


def main():
    rows = list(csv.DictReader(open(os.path.join(HERE, "sweep.tsv")), delimiter="\t"))
    hits, chance, anyhit, lit = [], 0, 0, {}
    f = os.path.join(HERE, "lit", "summary.tsv")
    if os.path.exists(f):
        lit = {r["poli_id"]: r["verdict"].split(" ")[0] for r in csv.DictReader(open(f), delimiter="\t")}
    for r in rows:
        t, lat, lon = parse(r["time"]), float(r["lat"]), float(r["lon"])
        anyhit += bool(isc(r["poli_id"], t, lat, lon, 0))
        for lag, e in timed(isc(r["poli_id"], t, lat, lon, 0), t):
            hits.append((r, lag, e))
        for s in SHIFTS:
            chance += len(timed(isc(r["poli_id"], t, lat, lon, s), t + timedelta(days=s)))
    L = [f"Residual detections: {len(rows)}; with any ISC event in +-600 s: {anyhit}",
         f"TIMED ISC events (origin {LO}-{HI} s before Poli time): {len(hits)} on {len({h[0]['poli_id'] for h in hits})} detections",
         f"Chance: {chance} TIMED events over {len(SHIFTS)} shifted windows per detection = {chance / len(SHIFTS):.2f} expected",
         f"Magnitudes of TIMED events: " + ", ".join(sorted((str(h[2]['mag']) if h[2]['mag'] is not None else 'none') for h in hits)),
         "",
         "poli_id\tpoli_time\tMw_d\toffshore\tisc_time\tlag_s\tisc_mag\tisc_magtype\tisc_lat\tisc_lon\tkm_from_grid\tisc_id\tlit_verdict"]
    for r, lag, e in sorted(hits, key=lambda h: int(h[0]["poli_id"])):
        L.append("\t".join([r["poli_id"], r["time"], r["Mw_d"], r["offshore"], e["time"][:19], f"{lag:.0f}",
                            str(e["mag"] if e["mag"] is not None else ""), e["magtype"], f"{e['lat']:.3f}", f"{e['lon']:.3f}",
                            f"{e['km']:.0f}", e["id"], lit.get(r["poli_id"], "")]))
    open(os.path.join(HERE, "timed.tsv"), "w").write("\n".join(L[5:]) + "\n")
    open(os.path.join(HERE, "timed-result.txt"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()

"""List lunar eclipses 1440-1465 from the NASA Five Millennium Catalog (Espenak & Meeus)
and compute visibility (Moon altitude at umbral contacts) for observing sites.

Usage: python3 -I eclipses.py data/LE1401-1500.html > results/eclipses.tsv

Dates are Julian calendar (the catalog uses Julian before 1582 Oct 15).
UT = TD - DeltaT (catalog DeltaT column). Visibility is computed from the
catalog's sub-lunar point at greatest eclipse, moved west at the Moon's
apparent hour-angle rate (~14.49 deg/h); declination change over the eclipse
(< 0.5 deg) and refraction/parallax (< 1 deg) are ignored.
"""
import math
import re
import sys

SITES = [  # name, lat, lon (E+)
    ("Constantinople", 41.01, 28.98), ("Venice", 45.44, 12.33), ("Rome", 41.90, 12.50),
    ("Krakow", 50.06, 19.94), ("Augsburg", 48.37, 10.90), ("Paris", 48.86, 2.35),
    ("London", 51.51, -0.13), ("Cairo", 30.04, 31.24), ("Seoul", 37.57, 126.98),
    ("Beijing", 39.90, 116.40), ("Nanjing", 32.06, 118.80), ("Kyoto", 35.01, 135.77),
]
RATE = 14.49  # deg of longitude per hour, sub-lunar point moving west

ROW = re.compile(
    r">(\d{5})</a>\s+(\d{4}) (\w{3}) (\d\d)\s+(\d\d):(\d\d):(\d\d)\s+(-?\d+)\s+(-?\d+)\s+<a[^>]*>\s*(\d+)</a>\s+"
    r"(\S+)\s+(\S+)\s+(-?[\d.]+)\s+([\d.]+)\s+(-?[\d.]+)\s+([\d.]+)\s+(\S+)\s+(\S+)\s+(\d+)([NS])\s+(\d+)([EW])"
)


def alt(lat, lon, slat, slon):
    a, b = math.radians(lat), math.radians(slat)
    d = math.radians(lon - slon)
    c = math.sin(a) * math.sin(b) + math.cos(a) * math.cos(b) * math.cos(d)
    return 90 - math.degrees(math.acos(max(-1, min(1, c))))


def main(path, y0=1440, y1=1465):
    html = open(path, encoding="latin-1").read()
    rows = []
    for m in ROW.finditer(html):
        (cat, y, mon, d, hh, mm, ss, dt, luna, saros, typ, qse, gamma, pmag, umag,
         pdur, pardur, tdur, la, ns, lo, ew) = m.groups()
        y = int(y)
        if not (y0 <= y <= y1):
            continue
        td_h = int(hh) + int(mm) / 60 + int(ss) / 3600
        ut_h = td_h - int(dt) / 3600
        slat = int(la) * (1 if ns == "N" else -1)
        slon = int(lo) * (1 if ew == "E" else -1)
        half = float(pardur) / 120 if pardur != "-" else None
        rows.append(dict(cat=cat, date=f"{y} {mon} {d}", ut=ut_h, typ=typ, gamma=float(gamma),
                         umag=float(umag), pardur=pardur, tdur=tdur, slat=slat, slon=slon, half=half))
    hdr = ["cat", "date_julian", "UT_greatest", "type", "umbral_mag", "partial_min", "total_min", "sublunar"]
    hdr += [s[0] for s in SITES]
    print("# NASA Five Millennium Catalog of Lunar Eclipses (Espenak & Meeus), LE1401-1500.html")
    print("# site cells: Moon altitude (deg) at U1/greatest/U4 and local mean time of greatest; '-' = below horizon throughout umbral phase")
    print("\t".join(hdr))
    for r in rows:
        if r["typ"].startswith("N"):
            continue  # penumbral eclipses are not reliably noticed
        h = r["ut"]
        out = [r["cat"], r["date"], f"{round(h * 60) // 60:02d}:{round(h * 60) % 60:02d}", r["typ"], f"{r['umag']:.3f}",
               r["pardur"], r["tdur"], f"{abs(r['slat'])}{'N' if r['slat'] >= 0 else 'S'} {abs(r['slon'])}{'E' if r['slon'] >= 0 else 'W'}"]
        for name, lat, lon in SITES:
            alts = [alt(lat, lon, r["slat"], r["slon"] - RATE * dh) for dh in (-r["half"], 0, r["half"])]
            lmt = round(((h + lon / 15) % 24) * 60) % 1440
            if max(alts) < 0:
                out.append("-")
            else:
                out.append("/".join(f"{a:.0f}" for a in alts) + f" @{lmt // 60:02d}:{lmt % 60:02d}LMT")
        print("\t".join(out))


if __name__ == "__main__":
    main(sys.argv[1])

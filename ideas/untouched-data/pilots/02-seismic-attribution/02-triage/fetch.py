"""Fetch the two reference sets exp 02 needs. Standard library only.

  data/comcat-m4-2010-2023.csv.gz   USGS ComCat, M >= 4.0, 2010-01-01 .. 2023-02-28 (time, lat, lon, depth, mag, id)
  data/ne_110m_admin_0_countries.geojson   Natural Earth 1:110m countries (public domain)
"""
import csv, gzip, io, os, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
UA = {"User-Agent": "Mozilla/5.0"}


def get(u, tries=4):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
        except Exception as e:
            err = e; time.sleep(3 * (i + 1))
    raise err


def month(ym):
    y, m = ym
    y2, m2 = (y + 1, 1) if m == 12 else (y, m + 1)
    u = ("https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&minmagnitude=4"
         f"&starttime={y}-{m:02d}-01&endtime={y2}-{m2:02d}-01&orderby=time-asc")
    rows = list(csv.DictReader(io.StringIO(get(u).decode())))
    assert len(rows) < 20000, ym
    return [(r["time"], r["latitude"], r["longitude"], r["depth"], r["mag"], r["id"]) for r in rows]


def main():
    yms = [(y, m) for y in range(2010, 2024) for m in range(1, 13) if (y, m) <= (2023, 2)]
    with ThreadPoolExecutor(4) as ex:
        chunks = list(ex.map(month, yms))
    n = 0
    with gzip.open(os.path.join(DATA, "comcat-m4-2010-2023.csv.gz"), "wt", newline="") as f:
        w = csv.writer(f); w.writerow(["time", "lat", "lon", "depth", "mag", "id"])
        for c in chunks:
            w.writerows(c); n += len(c)
    print("comcat rows", n)
    b = get("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson")
    open(os.path.join(DATA, "ne_110m_admin_0_countries.geojson"), "wb").write(b)
    print("natural earth bytes", len(b))


if __name__ == "__main__":
    main()

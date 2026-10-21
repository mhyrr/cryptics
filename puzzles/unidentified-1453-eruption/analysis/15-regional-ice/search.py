"""Query NCEI paleo-search for ice-core studies (dataTypeId=7) in a lat/lon box.

Usage: python3 -I search.py OUT.json minLat maxLat minLon maxLon
"""
import sys
import urllib.request

out, a, b, c, d = sys.argv[1:6]
u = ("https://www.ncei.noaa.gov/access/paleo-search/study/search.json?"
     f"dataTypeId=7&minLat={a}&maxLat={b}&minLon={c}&maxLon={d}&limit=500")
req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
data = urllib.request.urlopen(req, timeout=180).read()
open(out, "wb").write(data)
print(u, len(data))

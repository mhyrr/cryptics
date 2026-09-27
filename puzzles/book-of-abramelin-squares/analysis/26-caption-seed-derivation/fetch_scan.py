#!/usr/bin/env python3
"""Download one dictionary page image into the current folder (for locators).

python3 fetch_scan.py <volume> <scan>          full resolution, <volume>_<scan>.jpg
python3 fetch_scan.py <volume> <scan> small    reduced overview, <volume>_<scan>-small.jpg

volume: bsb11762465 (1596, A-S) or bsb10314207 (1595, T-Z).
"""
import sys, time, urllib.request
from pathlib import Path

vol, scan = sys.argv[1], int(sys.argv[2])
small = len(sys.argv) > 3 and sys.argv[3] == "small"
size = "!900,1400" if small else "full"
url = f"https://api.digitale-sammlungen.de/iiif/image/v2/{vol}_{scan:05d}/full/{size}/0/default.jpg"
path = Path.cwd() / f"{vol}_{scan:05d}{'-small' if small else ''}.jpg"
if not path.exists():
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            path.write_bytes(urllib.request.urlopen(req, timeout=120).read())
            break
        except Exception as e:
            if attempt == 3:
                sys.exit(f"failed: {url}: {e}")
            time.sleep(3 * (attempt + 1))
print(path)

"""Download 10's source files into a directory and print size and sha256.

Usage: python3 -I fetch.py data/
"""
import hashlib
import os
import sys
import urllib.request

FILES = {
    "labbe2019-supplement.zip": "https://cp.copernicus.org/articles/15/1485/2019/cp-15-1485-2019-supplement.zip",
    "europe2012ghd.txt": "https://www.ncei.noaa.gov/pub/data/paleo/historical/europe/europe2012ghd.txt",
    "burgundy2004.txt": "https://www.ncei.noaa.gov/pub/data/paleo/historical/europe/france/burgundy2004.txt",
}


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for name, url in FILES.items():
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=120).read()
        with open(os.path.join(out_dir, name), "wb") as fh:
            fh.write(data)
        print(f"{name}\t{len(data)}\t{hashlib.sha256(data).hexdigest()}\t{url}")


if __name__ == "__main__":
    main(sys.argv[1])

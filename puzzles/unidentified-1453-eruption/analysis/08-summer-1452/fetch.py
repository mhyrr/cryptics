"""Download the frost-ring files used in 08's secondary step into a directory; print sha256.

Usage: python3 -I fetch.py data/
"""
import hashlib
import os
import sys
import urllib.request

BASE = "https://paleo.ltrr.arizona.edu/treering/chronologies/colo_frost_rings/"
FILES = {n: BASE + n for n in ("readme_frostring.txt", "colofrlr.txt", "amlfr.txt")}


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for name, url in FILES.items():
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=120).read()
        with open(os.path.join(out_dir, name), "wb") as fh:
            fh.write(data)
        print(f"{name}\t{len(data)}\t{hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main(sys.argv[1])

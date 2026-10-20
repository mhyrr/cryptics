"""Download the inputs for experiment 04 into a directory and print their sha256.

Usage: python3 -I fetch.py data/
Compare the printed hashes with the provenance table in README.md.
"""
import hashlib
import os
import sys
import urllib.request

NOAA = "https://www.ncei.noaa.gov/pub/data/paleo/treering/reconstructions/"
FILES = {
    "schneider2015mxd.txt": NOAA + "schneider2015mxd.txt",
    "ntrend2015tr.txt": NOAA + "n_hem_temp/ntrend2015tr.txt",
    "ntrend2015-RecordsUsed_Metadata.txt": NOAA + "n_hem_temp/ntrend2015-RecordsUsed_Metadata.txt",
    "ntrend2017grid.nc": NOAA + "n_hem_temp/ntrend2017grid.nc",
    "evolv2k_v4.tab": "https://doi.pangaea.de/10.1594/PANGAEA.971968?format=textfile",
    "Esper_2017_BullVolc.pdf": "https://www.climatology.uni-mainz.de/files/2016/03/Esper_2017_BullVolc.pdf",
}


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for name, url in FILES.items():
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=300).read()
        with open(os.path.join(out_dir, name), "wb") as fh:
            fh.write(data)
        print(f"{name}\t{len(data)}\t{hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main(sys.argv[1])

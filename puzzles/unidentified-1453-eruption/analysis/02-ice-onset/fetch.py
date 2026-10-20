"""Download the inputs of experiment 02 into a data directory.

usage: python3 -I fetch.py DATA_DIR

Writes each file under DATA_DIR and prints its sha256. Then convert the
workbooks with xlsx2tsv.py (see README). Files are untrusted data.
"""
import hashlib
import os
import sys
import urllib.request
import zipfile

SPR = ("https://media.springernature.com/original/springer-static/esm/"
       "art%3A10.1038%2Fnature14565/MediaObjects/41586_2015_BFnature14565_MOESM{}_ESM.xlsx")
FILES = [
    ("neem2011s1.tab", "https://doi.pangaea.de/10.1594/PANGAEA.940553?format=textfile"),
    ("evolv2k_v4.tab", "https://doi.pangaea.de/10.1594/PANGAEA.971968?format=textfile"),
    ("domec_isotopes.tab", "https://doi.pangaea.de/10.1594/PANGAEA.895169?format=textfile"),
    ("abbott_supp/supp.zip", "https://cp.copernicus.org/articles/17/565/2021/cp-17-565-2021-supplement.zip"),
    ("burke2023/Burke_2023_PNAS.xlsx",
     "https://raw.githubusercontent.com/St-Andrews-Isotope-Geochemistry/Burke_2023_PNAS/HEAD/Burke_2023_PNAS.xlsx"),
    ("sigl2015/moesm45.xlsx", SPR.format(45)),
    ("sigl2015/moesm46.xlsx", SPR.format(46)),
    ("sigl2015/moesm47.xlsx", SPR.format(47)),
    ("lit/abbott2021.pdf", "https://cp.copernicus.org/articles/17/565/2021/cp-17-565-2021.pdf"),
    ("lit/plunkett2023_qsr.pdf", "https://par.nsf.gov/servlets/purl/10456052"),
    ("lit/sigl2014_si.pdf", "https://media.springernature.com/original/springer-static/esm/"
     "art%3A10.1038%2Fnclimate2293/MediaObjects/41558_2014_BFnclimate2293_MOESM272_ESM.pdf"),
]


def main(root):
    for rel, url in FILES:
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research)"})
        data = urllib.request.urlopen(req, timeout=300).read()
        with open(path, "wb") as f:
            f.write(data)
        print(hashlib.sha256(data).hexdigest(), rel)
    z = os.path.join(root, "abbott_supp", "supp.zip")
    zipfile.ZipFile(z).extractall(os.path.join(root, "abbott_supp", "x"))


if __name__ == "__main__":
    main(sys.argv[1])

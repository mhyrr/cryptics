"""Known-case test for the court-annal channel: how do the Joseon Sillok and Ming Shilu
record total lunar eclipses 3-24 months after known large eruptions (totals and partials with umbral magnitude >= 0.8) (the window in
which Guillet et al. 2023 expect dark eclipses)? If they record them with the same
bare formula as any other eclipse, the channel cannot see darkness.

Usage:
  python3 -I calibration.py data > results/calibration.txt
(needs data/LE1601-1700.html, data/LE1801-1900.html, data/LE1401-1500.html and
data/sillok/parsed/*.tsv written by court_records.py)
"""
import csv
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eclipses import ROW  # noqa: E402

MON = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
# eruption (year, month), calendar of the catalog at that date. Sources in README.
ERUPTIONS = [
    ("Huaynaputina", 1600, 2),
    ("Parker/Komagatake", 1640, 12),
    ("Tambora", 1815, 4),
    ("Krakatau", 1883, 8),
    ("UE 1458 (sulfate onset ~1458.0)", 1458, 1),
    ("UE 1453 (sulfate onset ~1453.0)", 1453, 1),
]


def catalog(data):
    out = []
    for f in sorted(glob.glob(os.path.join(data, "LE*.html"))):
        for m in ROW.finditer(open(f, encoding="latin-1").read()):
            g = m.groups()
            if g[10].startswith("T") or (g[10].startswith("P") and float(g[14]) >= 0.8):
                out.append((int(g[1]), MON[g[2]], int(g[3]), g[10], g[14]))
    return out


def court(data):
    rec = {}
    csv.field_size_limit(10**9)
    for fn, idt, isn, src in (("sillok_hits.tsv", 11, 15, "Sillok"), ("ming_hits.tsv", 10, 14, "Ming")):
        for r in csv.reader(open(os.path.join(data, "sillok", "parsed", fn), encoding="utf-8"), delimiter="\t"):
            if r[0] == "term":
                continue
            rec.setdefault(r[idt], {})[(src, r[1])] = r[isn][:90]
    return rec


def main(data):
    cat, rec = catalog(data), court(data)
    for name, y, mo in ERUPTIONS:
        print(f"== {name}: {y}-{mo:02d}")
        for (ey, em, ed, typ, umag) in cat:
            lag = (ey - y) * 12 + (em - mo)
            if 3 <= lag <= 24:
                key = f"{ey}-{em:02d}-{ed:02d}"
                hits = {}
                for k in rec:  # +-1 day for local-date shifts
                    if k[:8] == key[:8] and abs(int(k[8:10]) - ed) <= 1:
                        hits.update(rec[k])
                print(f"  {key} {typ} umag {umag} lag {lag:2d} mo: " +
                      ("; ".join(f"{s}: {t}" for (s, _), t in hits.items()) if hits else "no court record"))


if __name__ == "__main__":
    main(sys.argv[1])

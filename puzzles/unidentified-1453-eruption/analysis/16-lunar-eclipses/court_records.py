"""Date Joseon Sillok and Ming Shilu lunar-eclipse hits (月食, 月蝕) and match them
to the NASA catalog.

Reuses 05-documentary-onset/parse.py (calendar conversion, page parsers) and
05's cached Sillok month lists for leap months.

Usage:
  python3 -I ../05-documentary-onset/fetch.py data/sillok search w 月食 月蝕
  python3 -I ../05-documentary-onset/fetch.py data/sillok search m 月食 月蝕
  python3 -I court_records.py data/sillok ../05-documentary-onset/data results/eclipses.tsv > results/court_records.tsv
  python3 -I court_records.py data/sillok ../05-documentary-onset/data results/eclipses.tsv colour > results/colour_terms.txt
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "05-documentary-onset"))
import parse  # noqa: E402  (our own 05 script)

MON = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}


def main(data, months_data, cat_tsv, y0=1440, y1=1465):
    reign, leaps = parse.load_months(months_data)
    tmp = os.path.join(data, "parsed")
    os.makedirs(tmp, exist_ok=True)
    srows, _ = parse.parse_sillok(data, reign, leaps, tmp)
    mrows, _ = parse.parse_ming(data, leaps, tmp)
    cat = {}
    for line in open(cat_tsv, encoding="utf-8"):
        if line[0].isdigit():
            f = line.rstrip("\n").split("\t")
            y, mo, d = f[1].split()
            cat[parse.julian_to_jdn(int(y), MON[mo], int(d))] = (f[1], f[2], f[3], f[4])
    print("\t".join(["source", "id", "lunar_year", "month", "day", "jdn", "date_julian", "nasa_match",
                     "nasa_offset_days", "nasa_type", "nasa_umag", "title_or_lead", "snippet"]))
    seen = set()
    for src, rows, iy, imo, idy, ijd, idate, ititle, isnip in (
            ("Sillok", srows, 9, 5, 6, 10, 11, 14, 15), ("MingShilu", mrows, 8, 5, 6, 9, 10, 13, 14)):
        for r in rows:
            wy = int(r[iy])
            if not (y0 <= wy <= y1) or (src, r[1]) in seen:
                continue
            seen.add((src, r[1]))
            jd = int(r[ijd])
            near = min(cat, key=lambda k: abs(k - jd))
            off = jd - near
            m = cat[near] if abs(off) <= 2 else ("", "", "", "")
            print("\t".join([src, r[1], r[iy], r[imo], r[idy], str(jd), r[idate], m[0],
                             str(off) if m[0] else "", m[2], m[3], r[ititle], r[isnip]]))


COLOUR = ["赤", "紅", "血", "色", "無光", "不見", "黑", "暗", "昏", "晦", "白"]


def colour_scan(data, months_data):
    """All years: how many eclipse hits carry any colour/brightness/visibility word."""
    reign, leaps = parse.load_months(months_data)
    tmp = os.path.join(data, "parsed")
    os.makedirs(tmp, exist_ok=True)
    srows, _ = parse.parse_sillok(data, reign, leaps, tmp)
    mrows, _ = parse.parse_ming(data, leaps, tmp)
    for src, rows, iy, isnip in (("Sillok", srows, 9, 15), ("MingShilu", mrows, 8, 14)):
        uniq = {r[1]: r for r in rows}
        # an eclipse notice: the eclipse term sits in a short record (< 60 chars)
        short = [r for r in uniq.values() if len(r[isnip]) < 60 and ("月食" in r[isnip] or "月蝕" in r[isnip])]
        print(f"{src}: {len(uniq)} hits, {len(short)} short eclipse notices")
        for w in COLOUR:
            hits = [r for r in short if w in r[isnip]]
            print(f"  {w}: {len(hits)}" + "".join(f"\n    {r[iy]} {r[isnip]}" for r in hits[:12]))


if __name__ == "__main__":
    if len(sys.argv) > 4 and sys.argv[4] == "colour":
        colour_scan(*sys.argv[1:3])
    else:
        main(*sys.argv[1:4])

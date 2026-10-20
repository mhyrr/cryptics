"""Experiment 12, step 1: tree-ring coverage near Aniakchak from a NOAA paleo search dump.

Reads the JSON returned by the NCEI paleo-search API (dataTypeId=18, tree ring)
and prints one row per data table: code, site, lat, lon, species, span,
great-circle distance from Aniakchak (56.9 N, 158.2 W), and file URLs for
raw measurements (.rwl) and chronologies (.crn).

Usage: python3 -I coverage.py data/search_ak.json [MAX_START_YEAR]
"""
import json
import math
import sys

ANIAKCHAK = (56.9, -158.2)


def gc_km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371.0 * math.asin(math.sqrt(h))


def rows(path):
    j = json.load(open(path, encoding="utf-8"))
    for st in j.get("study", []):
        for site in st.get("site", []):
            c = site["geo"]["geometry"]["coordinates"]
            lat, lon = float(c[0]), float(c[1])
            for pd in site.get("paleoData", []):
                sp = ",".join(s.get("speciesCode") or "?" for s in pd.get("species", []))
                urls = [f["fileUrl"] for f in pd.get("dataFile", [])]
                rwl = [u for u in urls if u.endswith(".rwl")]
                crn = [u for u in urls if u.endswith(".crn")]
                yield {
                    "code": pd.get("dataTableName") or st.get("studyCode") or "?",
                    "site": site.get("siteName", "?"), "lat": lat, "lon": lon, "sp": sp,
                    "start": pd.get("earliestYearCE"), "end": pd.get("mostRecentYearCE"),
                    "km": gc_km(ANIAKCHAK, (lat, lon)), "rwl": rwl, "crn": crn,
                    "study": st.get("studyName", "")}


def main(path, max_start=None):
    rs = sorted(rows(path), key=lambda r: r["km"])
    print(f"# source: {path}; distance from Aniakchak {ANIAKCHAK}")
    print("code\tsite\tlat\tlon\tspecies\tstart\tend\tkm\tfiles")
    for r in rs:
        if r["start"] is None:
            continue
        if max_start is not None and r["start"] > max_start:
            continue
        files = " ".join(u.rsplit("/", 1)[-1] for u in r["rwl"] + r["crn"])
        print(f"{r['code']}\t{r['site']}\t{r['lat']:.2f}\t{r['lon']:.2f}\t{r['sp']}\t{r['start']}\t{r['end']}\t{r['km']:.0f}\t{files}")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else None)

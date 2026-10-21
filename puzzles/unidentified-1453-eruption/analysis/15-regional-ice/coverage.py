"""List ice-core studies from NCEI search dumps: site, coords, earliest/latest year, files.

Usage: python3 -I coverage.py data/ncei/*.json
"""
import json
import sys

seen = set()
for p in sys.argv[1:]:
    j = json.load(open(p, encoding="utf-8"))
    for st in j.get("study", []):
        sid = st.get("NOAAStudyId") or st.get("xmlId")
        if sid in seen:
            continue
        seen.add(sid)
        e = st.get("earliestYearCE"); l = st.get("mostRecentYearCE")
        for site in st.get("site", []):
            g = site.get("geo", {}).get("geometry", {}).get("coordinates", [])
            files = [f["fileUrl"].rsplit("/", 1)[-1] for pd in site.get("paleoData", []) for f in pd.get("dataFile", [])]
            vars_ = set()
            for pd in site.get("paleoData", []):
                for f in pd.get("dataFile", []):
                    for v in f.get("variables", []):
                        vars_.add(str(v.get("cvShortName") or v.get("cvWhat") or ""))
            print(f"{sid}\t{site.get('siteName')}\t{g}\t{e}\t{l}\t{st.get('studyName')[:90]}\t{','.join(sorted(vars_))[:200]}\t{';'.join(files)[:200]}")

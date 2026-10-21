"""Download named data files listed in NCEI search dumps; print size + sha256.

Usage: python3 -I fetch.py OUTDIR name1 name2 ... -- dump1.json dump2.json
"""
import hashlib, json, os, sys, urllib.request

args = sys.argv[1:]
i = args.index("--")
out, names, dumps = args[0], args[1:i], args[i + 1:]
urls = {}
for p in dumps:
    for st in json.load(open(p, encoding="utf-8")).get("study", []):
        for s in st.get("site", []):
            for pd in s.get("paleoData", []):
                for f in pd.get("dataFile", []):
                    urls[f["fileUrl"].rsplit("/", 1)[-1]] = f["fileUrl"]
os.makedirs(out, exist_ok=True)
for n in names:
    u = urls[n] if n in urls else n
    dest = os.path.join(out, u.rsplit("/", 1)[-1])
    if not os.path.exists(dest):
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        open(dest, "wb").write(urllib.request.urlopen(req, timeout=180).read())
    d = open(dest, "rb").read()
    print(f"{os.path.basename(dest)}\t{len(d)}\t{hashlib.sha256(d).hexdigest()}\t{u}")

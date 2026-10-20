"""Download the ITRDB raw-measurement files named in sites.tsv; print sha256.

URLs are taken from the NCEI paleo-search dump (data/search_ak.json).
Usage: python3 -I fetch.py data/search_ak.json sites.tsv data/
"""
import hashlib
import json
import os
import sys
import urllib.request


def rwl_urls(search_path):
    j = json.load(open(search_path, encoding="utf-8"))
    out = {}
    for st in j.get("study", []):
        for site in st.get("site", []):
            for pd in site.get("paleoData", []):
                for f in pd.get("dataFile", []):
                    u = f["fileUrl"]
                    name = u.rsplit("/", 1)[-1]
                    if name.endswith(".rwl"):
                        out[name.lower()] = u
    return out


def main(search_path, sites_path, out_dir):
    urls = rwl_urls(search_path)
    os.makedirs(out_dir, exist_ok=True)
    for line in open(sites_path, encoding="utf-8"):
        if line.startswith("#") or line.startswith("code\t"):
            continue
        code = line.split("\t")[0].strip()
        name = code.lower() + ".rwl"
        dest = os.path.join(out_dir, name)
        if os.path.exists(dest):
            data = open(dest, "rb").read()
        else:
            req = urllib.request.Request(urls[name], headers={"User-Agent": "Mozilla/5.0"})
            data = urllib.request.urlopen(req, timeout=120).read()
            open(dest, "wb").write(data)
        print(f"{name}\t{len(data)}\t{hashlib.sha256(data).hexdigest()}\t{urls[name]}")


if __name__ == "__main__":
    main(*sys.argv[1:4])

"""fetch.py - fetch the Gonzaga to Cosimo images (ASF, Mediceo avanti il Principato XI) at the server's maximum.

    python3 -I fetch.py

The ASF IIIF server's native size is 1272 px wide (info.json, checked 2026-11-19); nothing larger exists online.
Writes cache/<name>.jpg (gitignored) and prints one PROVENANCE.md row per image.
No credentials and no personal details are sent.
"""
import hashlib, os, urllib.request

BASE = ("https://archiviodistatofirenze.cultura.gov.it/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/"
        "mediceo_avanti_principato/00100011/A{:07d}.ptif/full/full/0/default.jpg")
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
IMAGES = {  # name: viewer image number in filza XI
    "2946-c215": 432,     # 24 Jan 1439, bare cipher with clear Italian (catalogue 2946)
    "2946-433": 433,      # the leaf after, for the address or a verso
    "2947-690": 690,      # address leaf, to Cosimo
    "2947-691": 691,      # 31 Dec 1439, glossed between the lines
    "2947-692": 692,
    "2947-693": 693,
    "2947-694": 694,      # ends with the dateline and signature
    "2947-695": 695,      # a clear letter of 3 Jan 1440 by another writer (context only)
}


def main():
    os.makedirs(CACHE, exist_ok=True)
    for name, n in IMAGES.items():
        url, path = BASE.format(n), os.path.join(CACHE, name + ".jpg")
        if os.path.exists(path):
            data = open(path, "rb").read()
        else:
            req = urllib.request.Request(url, headers={"User-Agent": "cryptics-research-script"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            if not data.startswith(b"\xff\xd8"):
                raise ValueError(f"{name}: not a JPEG")
            open(path, "wb").write(data)
        print(f"| {name}.jpg | {url} | {len(data)} | {hashlib.sha256(data).hexdigest()} |", flush=True)


if __name__ == "__main__":
    main()

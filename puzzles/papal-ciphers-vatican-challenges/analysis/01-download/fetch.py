"""Download every page image of a DigiVatLib manuscript over IIIF.

Usage: python3 -I fetch.py <shelfmark> <outdir> [width]
Example: python3 -I fetch.py Barb.lat.6960 ../../sources/cache/barb-lat-6960 1600
"""
import json, sys, time, urllib.request
from pathlib import Path

shelf, out = sys.argv[1], Path(sys.argv[2])
width = sys.argv[3] if len(sys.argv) > 3 else "1600"
out.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (cryptics research)"}

def get(url):
    for attempt in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()
        except Exception as e:
            if attempt == 3:
                raise
            time.sleep(3 * (attempt + 1))

manifest = json.loads(get(f"https://digi.vatlib.it/iiif/MSS_{shelf}/manifest.json"))
(out / "manifest.json").write_text(json.dumps(manifest, indent=1))
canvases = manifest["sequences"][0]["canvases"]
index = []
for n, cv in enumerate(canvases, 1):
    svc = cv["images"][0]["resource"]["service"]["@id"]
    name = f"{n:04d}_{cv['label'].replace('/', '-').replace(' ', '_')}.jpg"
    index.append((n, cv["label"], name))
    dest = out / name
    if dest.exists() and dest.stat().st_size > 1000:
        continue
    size = "full" if width == "full" else f"{width},"
    dest.write_bytes(get(f"{svc}/full/{size}/0/native.jpg"))
(out / "index.tsv").write_text("".join(f"{n}\t{l}\t{f}\n" for n, l, f in index))
print(f"{shelf}: {len(canvases)} canvases -> {out}")

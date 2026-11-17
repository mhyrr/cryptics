"""Fetch the inspected Ambrosiana G 275 inf. folios from public IIIF."""
import hashlib
from pathlib import Path
import urllib.request

# Folio-to-image numbers verified in the Ambrosiana manifest (see PROVENANCE.md).
PAGES = {"9r": 19, "9v": 20, "10r": 21, "10v": 22, "11r": 23, "11v": 24, "35r": 71, "35v": 72}
BASE = (
    "https://digitallibrary.unicatt.it/iiif/3/"
    "veneranda&SEPdata&SEPpublic&SEPcontents&SEP0b&SEP02&SEPda&SEP82&SEP80&SEP27&SEPc8&SEPd4&SEP"
)
CACHE = Path(__file__).resolve().parent / "cache"


def main():
    CACHE.mkdir(exist_ok=True)
    for folio, sequence in PAGES.items():
        url = f"{BASE}{sequence:04d}_G275inf._c.{folio}.jp2/full/max/0/default.jpg"
        path = CACHE / f"{folio}.jpg"
        if path.exists():
            data = path.read_bytes()
        else:
            request = urllib.request.Request(url, headers={"User-Agent": "cryptics-research"})
            with urllib.request.urlopen(request, timeout=20) as response:
                data = response.read()
        if not data.startswith(b"\xff\xd8"):
            raise ValueError(f"{folio}: response is not a JPEG")
        if not path.exists():
            path.write_bytes(data)
        print(f"| {path.name} | {url} | {len(data)} | {hashlib.sha256(data).hexdigest()} |",
              flush=True)


if __name__ == "__main__":
    main()

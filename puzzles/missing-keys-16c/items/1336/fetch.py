"""Fetch the Speciano–Borromeo scans linked from the public Ambrosiana OPAC."""
import hashlib
from pathlib import Path
import urllib.request


BASE = "https://ambrosiana.comperio.it/clavisng/index.php?file="
CACHE = Path(__file__).resolve().parent / "cache"
PAGES = {
    "F47-269r": 12041,
    "F47-269v": 12040,
    "F47-270r": 12042,
    "F47-270v": 12043,
    "F131-14r": 89421,
    "F131-14v": 89422,
    "F131-15r": 89423,
    "F131-15v": 89424,
    "F49-44r": 12529,
    "F49-44v": 12530,
}


def main():
    CACHE.mkdir(exist_ok=True)
    for folio, file_id in PAGES.items():
        url = BASE + str(file_id)
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

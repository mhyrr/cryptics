#!/usr/bin/env python3
"""Download per-scan hOCR for both dictionary volumes into out/hocr/ (gitignored).

Source: Bayerische Staatsbibliothek OCR endpoint, one request per scan, four
workers. Resumable: existing non-empty files are skipped.
After the run, `manifest` writes hocr-manifest.tsv (scan, bytes, sha256), which
is checked in so a later re-download can be compared.
"""
import hashlib, pathlib, sys, time, urllib.request

VOLUMES = {"bsb11762465": 1158, "bsb10314207": 276}  # canvas counts from IIIF manifests, 2026-09-20
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "out" / "hocr"
UA = {"User-Agent": "cryptics-research/0.1 (single pass, rate limited)"}


def fetch_one(job):
    vid, i = job
    p = OUT / vid / f"{i:05d}.hocr"
    if p.exists() and p.stat().st_size > 0:
        return
    url = f"https://api.digitale-sammlungen.de/ocr/{vid}/{i}"
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            p.write_bytes(urllib.request.urlopen(req, timeout=60).read())
            return
        except Exception as e:  # logged, retried, then recorded as a miss
            print(f"{vid}/{i} attempt {attempt}: {e}", flush=True)
            time.sleep(5 * (attempt + 1))
    (OUT / vid / f"{i:05d}.MISSING").write_text(url)


def fetch():
    from concurrent.futures import ThreadPoolExecutor
    jobs = []
    for vid, n in VOLUMES.items():
        (OUT / vid).mkdir(parents=True, exist_ok=True)
        jobs += [(vid, i) for i in range(1, n + 1)]
    with ThreadPoolExecutor(4) as ex:  # four workers; the endpoint takes ~2 s per scan
        for k, _ in enumerate(ex.map(fetch_one, jobs)):
            if k % 100 == 0:
                print(k, len(jobs), flush=True)


def manifest():
    rows = []
    for vid in VOLUMES:
        for p in sorted((OUT / vid).glob("*.hocr")):
            b = p.read_bytes()
            rows.append(f"{vid}\t{int(p.stem)}\t{len(b)}\t{hashlib.sha256(b).hexdigest()}")
    (HERE / "hocr-manifest.tsv").write_text("volume\tscan\tbytes\tsha256\n" + "\n".join(rows) + "\n")
    print(len(rows), "files")


if __name__ == "__main__":
    {"fetch": fetch, "manifest": manifest}[sys.argv[1]]()

#!/usr/bin/env python3
"""Fetch Dresden N 111 physical pages 246-297 from the pinned page index. See PROTOCOL.md."""
import argparse, hashlib, json, time, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIVE = HERE.parents[1]
INDEX = DIVE / "sources" / "dresden-n111" / "page-index.json"
CACHE = DIVE / "sources" / "cache" / "dresden-n111"
COHORT = range(246, 298)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    pages = {p["physical_page"]: p for p in json.load(open(INDEX))["pages"]}
    manifest_path = HERE / "image-manifest.json"
    if args.check:
        for item in json.load(open(manifest_path))["images"]:
            if sha(CACHE / item["filename"]) != item["sha256"]:
                raise ValueError(f"Image changed: {item['filename']}")
        print("image hashes verify")
        return
    if not args.fetch:
        parser.error("use --fetch or --check")
    CACHE.mkdir(parents=True, exist_ok=True)
    images = []
    for n in COHORT:
        page = pages[n]
        path = CACHE / f"p{n:03d}.jpg"
        if not path.exists():
            with urllib.request.urlopen(page["original_image"], timeout=60) as response:
                body = response.read()
            if not body.startswith(b"\xff\xd8"):
                raise ValueError(f"page {n}: expected JPEG; refusing a challenge or error page")
            path.write_bytes(body)
            time.sleep(0.5)
        images.append({"physical_page": n, "page_label": page["page_label"].strip(),
                       "original_image": page["original_image"], "filename": path.name,
                       "bytes": path.stat().st_size, "sha256": sha(path)})
        print("saved", path.name, path.stat().st_size, flush=True)
    manifest_path.write_text(json.dumps({"source": "PRIMARY SLUB manuscript images, Mscr.Dresd.N.111",
                                         "page_index_sha256": sha(INDEX), "images": images}, indent=2) + "\n")


if __name__ == "__main__":
    main()

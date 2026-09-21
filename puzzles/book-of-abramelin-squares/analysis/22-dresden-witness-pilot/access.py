#!/usr/bin/env python3
"""Index pinned SLUB METS and fetch only cover plus the frozen three-page pilot."""
import argparse
import hashlib
import json
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "sources/dresden-n111"
CACHE = HERE.parents[1] / "sources/cache/dresden-n111"
OAI = "https://digital.slub-dresden.de/oai/?verb=GetRecord&metadataPrefix=mets&identifier=oai%3Ade%3Aslub-dresden%3Adb%3Aid-364474017"
NS = {"m": "http://www.loc.gov/METS/", "mods": "http://www.loc.gov/mods/v3"}
XLINK = "{http://www.w3.org/1999/xlink}href"
PILOT = (243, 244, 245)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def index():
    root = ET.parse(SOURCE / "mets.xml").getroot()
    files = {}
    for group in root.findall(".//m:fileGrp", NS):
        for file in group.findall("m:file", NS):
            loc = file.find("m:FLocat", NS)
            if loc is not None:
                files[file.get("ID")] = (group.get("USE"), loc.get(XLINK))
    pages = []
    for page in root.findall('.//m:structMap[@TYPE="PHYSICAL"]//m:div[@TYPE="page"]', NS):
        links = dict(files[ptr.get("FILEID")] for ptr in page.findall("m:fptr", NS))
        pages.append({"physical_page": int(page.get("ORDER")), "page_label": page.get("ORDERLABEL"),
                      "original_image": links["ORIGINAL"], "medium_image": links["DEFAULT"]})
    pages.sort(key=lambda p: p["physical_page"])
    return {"source_url": OAI, "tier": "PRIMARY metadata", "metadata_sha256": sha(SOURCE / "mets.xml"),
            "title": root.find(".//mods:title", NS).text,
            "shelfmark": root.find(".//mods:shelfLocator", NS).text,
            "catalogue_extent": root.find(".//mods:extent", NS).text,
            "physical_images": len(pages), "pages": pages}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = index()
    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    output = SOURCE / "page-index.json"
    if args.check:
        if output.read_text() != text:
            raise ValueError("Metadata index differs")
        manifest = json.loads((HERE / "image-manifest.json").read_text())
        for item in manifest["images"]:
            path = CACHE / item["filename"]
            if sha(path) != item["sha256"]:
                raise ValueError(f"Image changed: {path}")
        print("Metadata index and image hashes verify")
        return
    output.write_text(text)
    if args.fetch:
        CACHE.mkdir(parents=True, exist_ok=True)
        images = []
        for page in data["pages"]:
            if page["physical_page"] not in (1,) + PILOT:
                continue
            path = CACHE / f"p{page['physical_page']:03d}.jpg"
            if not path.exists():
                with urllib.request.urlopen(page["original_image"], timeout=30) as response:
                    body = response.read()
                    if not body.startswith(b"\xff\xd8"):
                        raise ValueError("Expected JPEG; refusing a challenge/error page")
                    path.write_bytes(body)
            images.append({**page, "filename": path.name, "bytes": path.stat().st_size,
                           "sha256": sha(path), "role": "cover access check" if page["physical_page"] == 1 else "frozen pilot"})
            print("Saved", path.name, path.stat().st_size, "bytes", flush=True)
        (HERE / "image-manifest.json").write_text(json.dumps({"source": "PRIMARY SLUB manuscript images",
            "metadata_sha256": data["metadata_sha256"], "images": images}, indent=2) + "\n")
    print(data["shelfmark"], data["physical_images"], "physical image records")


if __name__ == "__main__":
    main()

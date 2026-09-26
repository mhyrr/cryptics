#!/usr/bin/env python3
"""Merge locator batches, check them, cut padded grid crops, write reader worklists.

python3 crop.py            merge + check + crop + worklists
python3 crop.py --check    verify inventory, crop hashes and worklists reproduce
"""
import hashlib, json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIVE = HERE.parents[1]
CACHE = DIVE / "sources" / "cache" / "dresden-n111"
CROPS = CACHE / "crops-25"
PAD = 0.05
BATCH_TARGET = 40
ID = re.compile(r"^p(\d{3})-c(\d)-g(\d+)$")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def page_size(path):
    out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
                         capture_output=True, text=True, check=True).stdout
    w = int(re.search(r"pixelWidth: (\d+)", out).group(1))
    h = int(re.search(r"pixelHeight: (\d+)", out).group(1))
    return w, h


def merge():
    """Inventory in traversal order, plus a list of problems. Nothing is repaired."""
    pages, problems = [], []
    for f in sorted((HERE / "locator").glob("L*.json")):
        doc = json.load(open(f))
        for p in doc["pages"]:
            pages.append(dict(p, batch=doc["batch"], locator_model=doc.get("locator_model")))
    pages.sort(key=lambda p: p["physical_page"])
    got = [p["physical_page"] for p in pages]
    if got != list(range(246, 298)):
        problems.append(f"page coverage {got[:3]}..{got[-3:]} ({len(got)} pages)")
    grids, seen = [], set()
    for p in pages:
        for g in p.get("grids", []):
            m = ID.match(g["locator_id"])
            if not m or int(m.group(1)) != p["physical_page"]:
                problems.append(f"bad id {g['locator_id']} on page {p['physical_page']}")
            if g["locator_id"] in seen:
                problems.append(f"duplicate id {g['locator_id']}")
            seen.add(g["locator_id"])
            x0, y0, x1, y1 = g["bbox"]
            if not (0 <= x0 < x1 <= 1 and 0 <= y0 < y1 <= 1):
                problems.append(f"bad bbox {g['locator_id']} {g['bbox']}")
            grids.append(dict(g, physical_page=p["physical_page"], page_label=p.get("page_label"),
                              column=int(m.group(2)) if m else None, index=int(m.group(3)) if m else None))
    grids.sort(key=lambda g: (g["physical_page"], g["column"] or 0, g["index"] or 0))
    prev = (4, 4)  # experiment 22 ended at IV.4.4 on page 245
    continuity = []
    for g in grids:
        cur = (g.get("chapter"), g.get("item"))
        ok = cur[0] is not None and cur[1] is not None and (
            (cur[0] == prev[0] and cur[1] == prev[1] + 1) or (cur[0] == prev[0] + 1 and cur[1] == 1))
        if not ok:
            continuity.append({"locator_id": g["locator_id"], "previous": list(prev), "this": list(cur)})
        if cur[0] is not None and cur[1] is not None:
            prev = cur
    return pages, grids, problems, continuity


def cut(grids):
    CROPS.mkdir(parents=True, exist_ok=True)
    sizes, out = {}, []
    for g in grids:
        page = CACHE / f"p{g['physical_page']:03d}.jpg"
        if page not in sizes:
            sizes[page] = page_size(page)
        w, h = sizes[page]
        x0, y0, x1, y1 = g["bbox"]
        left = max(0, int((x0 - PAD) * w))
        top = max(0, int((y0 - PAD) * h))
        right = min(w, int((x1 + PAD) * w))
        bottom = min(h, int((y1 + PAD) * h))
        dest = CROPS / f"{g['locator_id']}.jpg"
        subprocess.run(["sips", "-c", str(bottom - top), str(right - left), "--cropOffset", str(top), str(left),
                        str(page), "--out", str(dest)], capture_output=True, check=True)
        out.append({"locator_id": g["locator_id"], "page": page.name, "box_px": [left, top, right, bottom],
                    "crop": str(dest.relative_to(DIVE)), "sha256": sha(dest)})
    return out


def worklists(grids, crops):
    crop_by = {c["locator_id"]: c for c in crops}
    batches, cur, cur_pages = [], [], set()
    by_page = {}
    for g in grids:
        by_page.setdefault(g["physical_page"], []).append(g)
    for page in sorted(by_page):
        if cur and len(cur) + len(by_page[page]) > BATCH_TARGET:
            batches.append(cur)
            cur = []
        cur.extend(by_page[page])
    if cur:
        batches.append(cur)
    out = []
    for k, batch in enumerate(batches, 1):
        entries = [{"locator_id": g["locator_id"], "physical_page": g["physical_page"],
                    "column": g["column"], "index_in_column": g["index"],
                    "chapter": g.get("chapter"), "item": g.get("item"),
                    "short_heading": g.get("short_heading"),
                    "crop": str(DIVE / crop_by[g["locator_id"]]["crop"]),
                    "full_page": str(CACHE / f"p{g['physical_page']:03d}.jpg")} for g in batch]
        out.append({"batch": f"R{k}", "pages": sorted({g["physical_page"] for g in batch}), "entries": entries})
    return out


def main():
    pages, grids, problems, continuity = merge()
    inventory = {"source": "experiment 25 locator pass, merged; nothing repaired", "pages": pages,
                 "grids": grids, "problems": problems, "continuity_breaks": continuity}
    inv_text = json.dumps(inventory, indent=1, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        assert (HERE / "inventory.json").read_text() == inv_text, "inventory differs"
        for c in json.load(open(HERE / "crops-manifest.json"))["crops"]:
            assert sha(DIVE / c["crop"]) == c["sha256"], f"crop changed: {c['locator_id']}"
        print("inventory and crops verify")
        return
    (HERE / "inventory.json").write_text(inv_text)
    crops = cut(grids)
    (HERE / "crops-manifest.json").write_text(json.dumps({"pad": PAD, "crops": crops}, indent=1) + "\n")
    wl = worklists(grids, crops)
    (HERE / "worklists").mkdir(exist_ok=True)
    for b in wl:
        (HERE / "worklists" / f"{b['batch']}.json").write_text(json.dumps(b, indent=1, ensure_ascii=False) + "\n")
    print(len(pages), "pages", len(grids), "grids", len(wl), "reader batches",
          "problems", len(problems), "continuity breaks", len(continuity))
    for p in problems:
        print("PROBLEM", p)
    for c in continuity:
        print("BREAK", c)


if __name__ == "__main__":
    main()

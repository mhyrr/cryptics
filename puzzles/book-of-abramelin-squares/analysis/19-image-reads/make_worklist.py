#!/usr/bin/env python3
"""Build the image-reading worklist and fetch the crops. See PROTOCOL.md."""
import csv, hashlib, json, pathlib, random, sys, urllib.request

HERE = pathlib.Path(__file__).resolve().parent
A = HERE.parent
sys.path.insert(0, str(A / "12-dictionary-index"))
sys.path.insert(0, str(A / "14-caption-seed-test"))
import build_index as b12
import run as e14            # skeleton(); not modified

IIIF = "https://api.digitale-sammlungen.de/iiif/image/v2/{vol}_{scan:05d}/{x},{y},{w},{h}/full/0/default.jpg"


def sk(token):
    """Skeletons of a token's experiment 14 forms (OCR f may be long s)."""
    return {e14.skeleton(f) for f in e14.forms(token)}


def main():
    lookups = json.load(open(A / "14-caption-seed-test" / "lookups.json"))
    hits = json.load(open(A / "14-caption-seed-test" / "results.json"))["mathers_seed_hits_skeleton"]
    ent = {}
    with open(A / "12-dictionary-index" / "entries.tsv", encoding="utf8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            ent[(r["volume"], int(r["scan"]), r["headword_ocr"])] = r
    work, in_hit = [], set()
    for ch, rows in hits.items():
        for row in rows:
            for l in lookups:
                if l["chapter"] == int(ch) and any(e14.skeleton(row) in sk(c) for c in l["candidates_ocr"]):
                    for vol, scan, head in l["entries"]:
                        r = ent.get((vol, scan, head))
                        if r and any(e14.skeleton(row) in sk(t) for t in r["hebrew_adjacent"].split()):
                            in_hit.add((vol, scan, head))
                            work.append({"kind": "hit", "chapter": int(ch), "label_number": l["number"], "german": l["german"],
                                         "top_row": row, "volume": vol, "scan": scan, "headword_ocr": head})
    pool = sorted({(vol, scan, head, l["chapter"], l["number"], l["german"]) for l in lookups
                   if l["tier"] in ("exact_key", "frame_stripped") for vol, scan, head in l["entries"]
                   if (vol, scan, head) not in in_hit and (vol, scan, head) in ent})
    seen, uniq = set(), []
    for p in pool:
        if p[:3] not in seen:
            seen.add(p[:3])
            uniq.append(p)
    rng = random.Random(20260920)
    for vol, scan, head, ch, num, ger in rng.sample(uniq, 30):
        work.append({"kind": "gap_sample", "chapter": ch, "label_number": num, "german": ger, "top_row": None,
                     "volume": vol, "scan": scan, "headword_ocr": head})
    done = {}
    for k, w in enumerate(work):
        key = (w["volume"], w["scan"], w["headword_ocr"])
        if key in done:
            w.update(done[key])
            continue
        r = ent[key]
        text = (b12.HOCR / w["volume"] / f'{w["scan"]:05d}.hocr').read_text(encoding="utf8", errors="replace")
        m = b12.PAGE.search(text)
        width, height = int(m.group(1)), int(m.group(2))
        g = b12.gutter(b12.words_of(text), width)
        x0, x1 = (0, g + 15) if r["column"] == "0" else (g - 15, width)
        y0 = max(int(r["y"]) - 30, 0)
        h = min(680, height - y0)
        url = IIIF.format(vol=w["volume"], scan=w["scan"], x=x0, y=y0, w=x1 - x0, h=h)
        name = f'{len(done):02d}.jpg'            # opaque name: tells a reader nothing
        path = HERE / "out" / name
        if not path.exists():
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            path.write_bytes(urllib.request.urlopen(req, timeout=120).read())
        done[key] = {"crop": name, "url": url, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        w.update(done[key])
    (HERE / "worklist.json").write_text(json.dumps(work, indent=1, ensure_ascii=False) + "\n")
    reader = [{"crop": v["crop"], "headword_ocr": k[2]} for k, v in done.items()]
    (HERE / "out" / "reader-list.json").write_text(json.dumps(reader, indent=1, ensure_ascii=False) + "\n")
    print(len(work), "work items;", len(done), "crops;", sum(w["kind"] == "hit" for w in work), "hit items")


if __name__ == "__main__":
    main()

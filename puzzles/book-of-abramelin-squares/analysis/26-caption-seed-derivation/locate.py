#!/usr/bin/env python3
"""Locate dictionary entries for every nominated headword and cut the reading crops.

Every rule is in PROTOCOL.md ("Locating entries, code first"). No seed and no
square is read here.

python3 locate.py lookup     lookups.json with the locator worklist, and the tables of contents
python3 locate.py merge-locations   locations.json from the locators' raw files
python3 locate.py manifest   entries-manifest.json, crops in out/crops, reader worklists
python3 locate.py --fetch    restore the crops from the manifest's URLs
python3 locate.py --check    verify crop hashes and that lookups.json reproduces
"""
import collections, hashlib, json, re, sys, time, unicodedata, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
A = HERE.parent
sys.path.insert(0, str(A / "12-dictionary-index"))
sys.path.insert(0, str(A / "14-caption-seed-test"))
import build_index as b12      # parse_page, gutter, words_of, PAGE: unchanged
import lookup as l14           # Index.find: unchanged

IIIF = "https://api.digitale-sammlungen.de/iiif/image/v2/{vol}_{scan:05d}/{x},{y},{w},{h}/full/0/default.jpg"
PAGE_URL = "https://api.digitale-sammlungen.de/iiif/image/v2/{vol}_{scan:05d}/full/full/0/default.jpg"
VOL_AS, VOL_TZ = "bsb11762465", "bsb10314207"
OUT = HERE / "out"
BATCH = 60


# ---------------------------------------------------------------- lookup

def headwords():
    """Distinct nominated headwords, with the captions that nominated them."""
    use = collections.defaultdict(list)
    for it in json.load(open(HERE / "nominations.json", encoding="utf8"))["items"]:
        for n in it["nominations"]:
            use[n["german"].strip()].append(f"D:{it['key']}")
    for c in json.load(open(A / "18-german-captions" / "nominations-de.json", encoding="utf8"))["captions"]:
        for n in c["nominations"]:
            use[n["german"].strip()].append(f"W:{c['chapter']}/{c['number']}")
    return dict(sorted(use.items()))


def running_head(e):
    return int(e["y"]) < 200 and len(re.sub(r"[^A-Za-zÄÖÜäöüſß]", "", e["headword_ocr"])) <= 3


def collate(w):
    """Alphabetical position key: case, diacritics, long s, j/i and v/u folded."""
    w = unicodedata.normalize("NFKD", w.lower().replace("ſ", "s").replace("ß", "ss"))
    w = "".join(c for c in w if "a" <= c <= "z")
    return w.replace("j", "i").replace("v", "u")


def scan_medians(ix):
    """Per volume, scans in order with the median collation key of their German headword lines.

    A line counts when it begins with its column's two-letter running head; Latin
    lines (POETICE epithets, lemma lines) mostly do not, and would scramble the order.
    """
    heads = {}
    for e in ix.rows:
        if running_head(e):
            k = collate(e["headword_ocr"])
            if 2 <= len(k) <= 3:
                heads[(e["volume"], int(e["scan"]), int(e["column"]))] = k
    keys = collections.defaultdict(list)
    for e in ix.rows:
        if running_head(e):
            continue
        first = e["headword_ocr"].split("/")[0].strip()
        k = collate(first)
        rh = heads.get((e["volume"], int(e["scan"]), int(e["column"])))
        if len(k) >= 3 and rh and k.startswith(rh):
            keys[(e["volume"], int(e["scan"]))].append(k)
    out = collections.defaultdict(list)
    for (vol, scan), ks in sorted(keys.items()):
        ks.sort()
        out[vol].append((scan, ks[len(ks) // 2]))
    return out


def bracket(word, medians):
    k = collate(word)
    vol = VOL_TZ if k[:1] >= "t" else VOL_AS
    seq = medians[vol]
    # the split that best separates medians <= k (before) from medians > k (after); robust to stray lines
    below = [med <= k for _, med in seq]
    score, best, at = sum(not b for b in below), -1, 0
    for i, b in enumerate(below):
        score += 1 if b else -1
        if score > best:
            best, at = score, i
    lo, hi = max(at - 2, 0), min(at + 2, len(seq) - 1)
    return vol, [seq[i][0] for i in range(lo, hi + 1)]


def toc(ix):
    """Table of contents per volume: scan, column, running head, first and last German headword (OCR)."""
    heads, lines = {}, collections.defaultdict(list)
    for e in ix.rows:
        loc = (e["volume"], int(e["scan"]), int(e["column"]))
        if running_head(e):
            heads[loc] = e["headword_ocr"].strip(" .")
        else:
            lines[loc].append(e["headword_ocr"].strip(" ."))
    out = collections.defaultdict(list)
    for loc in sorted(set(heads) | set(lines)):
        vol, scan, col = loc
        rh = heads.get(loc, "")
        ok = [h for h in lines.get(loc, []) if rh and collate(h).startswith(collate(rh))] or lines.get(loc, [])
        out[vol].append(f"{scan}\t{col + 1}\t{rh}\t{ok[0] if ok else ''}\t{ok[-1] if ok else ''}")
    for vol, rows in out.items():
        (HERE / f"toc-{vol}.tsv").write_text("scan\tcolumn\trunning_head\tfirst_headword_ocr\tlast_headword_ocr\n"
                                             + "\n".join(rows) + "\n", encoding="utf8")


def fetch(url, path):
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            path.write_bytes(urllib.request.urlopen(req, timeout=120).read())
            return
        except Exception:
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"fetch failed: {url}")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def do_lookup(write=True):
    ix = l14.Index()
    medians = scan_medians(ix)
    out, work = [], []
    for word, users in headwords().items():
        tier, ents = ix.find(word)
        kept, seen = [], set()
        for e in ents:
            loc = (e["volume"], int(e["scan"]), int(e["column"]), int(e["y"]))
            if running_head(e) or loc in seen:
                continue
            seen.add(loc)
            kept.append({"volume": e["volume"], "scan": int(e["scan"]), "column": int(e["column"]),
                         "y": int(e["y"]), "headword_ocr": e["headword_ocr"]})
        rec = {"headword": word, "tier": tier if kept else "none", "entries": kept, "used_by": users}
        if tier != "none" and not kept:
            rec["note"] = "only running-head lines matched"
        out.append(rec)
        if not kept:
            vol, scans = bracket(word, medians)
            work.append({"headword": word, "volume": vol, "scans": scans})
    data = {"lookups": out, "locator_worklist": work}
    text = json.dumps(data, indent=1, ensure_ascii=False) + "\n"
    if write:
        (HERE / "lookups.json").write_text(text, encoding="utf8")
        toc(ix)
    return text, out, work


# ---------------------------------------------------------------- crops

def page(vol, scan):
    text = (b12.HOCR / vol / f"{scan:05d}.hocr").read_text(encoding="utf8", errors="replace")
    m = b12.PAGE.search(text)
    width, height = int(m.group(1)), int(m.group(2))
    g = b12.gutter(b12.words_of(text), width)
    lines = b12.parse_page(text)
    for L in lines:
        L["running"] = L["y"] < 200 and len(re.sub(r"[^A-Za-zÄÖÜäöüſß]", "", L["text"])) <= 3
    return width, height, g, lines


def xspan(col, g, width):
    return (0, g + 15) if col == 0 else (g - 15, width)


def boxes(vol, scan, col, y_head, last_scan):
    """Crop parts for an entry whose headword line is centred at y_head. PROTOCOL.md, crop rule."""
    width, height, g, lines = page(vol, scan)
    x0, x1 = xspan(col, g, width)
    in_col = [L for L in lines if L["col"] == col and not L["running"]]
    nxt = [L["y"] for L in in_col if L["head"] and L["y"] > y_head + 150]
    y0 = max(y_head - 40, 0)
    if nxt:
        y1 = nxt[0] - 15
    else:
        y1 = max([L["y"] for L in in_col] + [y_head]) + 40
    h = min(max(y1 - y0, 600), 1400, height - y0)
    parts = [{"volume": vol, "scan": scan, "box": [x0, y0, x1 - x0, h]}]
    if not nxt:
        if col == 0:
            vol2, scan2, col2 = vol, scan, 1
        else:
            vol2, scan2, col2 = vol, scan + 1, 0
        if scan2 <= last_scan:
            w2, h2, g2, lines2 = page(vol2, scan2)
            c2 = [L for L in lines2 if L["col"] == col2 and not L["running"]]
            if c2:
                top = max(c2[0]["y"] - 20, 0)
                heads2 = [L["y"] for L in c2 if L["head"] and L["y"] > c2[0]["y"] - 5]
                end = min((heads2[0] - 15) if heads2 else top + 900, top + 900, h2)
                if end - top >= 60:
                    a0, a1 = xspan(col2, g2, w2)
                    parts.append({"volume": vol2, "scan": scan2, "box": [a0, top, a1 - a0, end - top]})
    return parts


def last_scans():
    out = collections.defaultdict(int)
    for p in b12.HOCR.iterdir():
        if p.is_dir():
            out[p.name] = max(int(f.stem) for f in p.glob("*.hocr"))
    return out


def do_manifest():
    lookups = json.load(open(HERE / "lookups.json", encoding="utf8"))["lookups"]
    located = json.load(open(HERE / "locations.json", encoding="utf8")) if (HERE / "locations.json").exists() else {"items": []}
    last = last_scans()
    entries = {}                           # (vol, scan, col, y) -> record

    def add(vol, scan, col, y, head, source, word):
        key = (vol, scan, col, y)
        if key not in entries:
            entries[key] = {"volume": vol, "scan": scan, "column": col + 1, "y": y, "headword_ocr": head,
                            "sources": [], "headwords": []}
        if source not in entries[key]["sources"]:
            entries[key]["sources"].append(source)
        if word not in entries[key]["headwords"]:
            entries[key]["headwords"].append(word)

    for l in lookups:
        for e in l["entries"]:
            add(e["volume"], e["scan"], e["column"], e["y"], e["headword_ocr"], f"lookup:{l['tier']}", l["headword"])
    for it in located["items"]:
        if it.get("found"):
            vol = it["volume"]
            _, height, _, _ = page(vol, it["scan"])
            add(vol, it["scan"], it["column"] - 1, int(round(it["y"] * height)), it["headword_printed"],
                f"locator:{it['locator']}", it["headword"])
    manifest = []
    for i, key in enumerate(sorted(entries), 1):
        rec = entries[key]
        rec["entry_id"] = f"e{i:04d}"
        parts = boxes(rec["volume"], rec["scan"], rec["column"] - 1, rec["y"], last[rec["volume"]])
        for j, p in enumerate(parts, 1):
            x, y, w, h = p["box"]
            p["url"] = IIIF.format(vol=p["volume"], scan=p["scan"], x=x, y=y, w=w, h=h)
            p["file"] = f"{rec['entry_id']}-{j}.jpg"
            path = OUT / "crops" / p["file"]
            fetch(p["url"], path)
            p["sha256"] = sha(path)
        rec["parts"] = parts
        manifest.append(rec)
    by_word = collections.defaultdict(list)
    for rec in manifest:
        for w in rec["headwords"]:
            by_word[w].append(rec["entry_id"])
    data = {"source": "PRIMARY, BSB IIIF; Sylvae quinquelinguis 1596 A-S (bsb11762465), 1595 T-Z (bsb10314207)",
            "crop_rule": "PROTOCOL.md, Locating entries, step 4", "entries": manifest,
            "headword_entries": dict(sorted(by_word.items()))}
    (HERE / "entries-manifest.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf8")
    wl = HERE / "worklists"
    wl.mkdir(exist_ok=True)
    nb = (len(manifest) + BATCH - 1) // BATCH
    for b in range(nb):
        chunk = manifest[b * BATCH:(b + 1) * BATCH]
        items = [{"crop": r["entry_id"], "parts": [p["file"] for p in r["parts"]], "headword_ocr": r["headword_ocr"]}
                 for r in chunk]
        (wl / f"R{b + 1:02d}.json").write_text(json.dumps({"batch": f"R{b + 1:02d}", "items": items},
                                                          indent=1, ensure_ascii=False) + "\n", encoding="utf8")
    print(len(manifest), "entries;", sum(len(r["parts"]) for r in manifest), "crop parts;", nb, "batches")


def merge_locations():
    """Merge locations-raw/locations-L*.json without edits; check each item against the worklist."""
    work = {w["headword"]: w for w in json.load(open(HERE / "lookups.json", encoding="utf8"))["locator_worklist"]}
    items = []
    for f in sorted((HERE / "locations-raw").glob("locations-L*.json")):
        raw = json.load(open(f, encoding="utf8"))
        for it in raw["items"]:
            assert it["headword"] in work, (f.name, it["headword"])
            items.append(dict(it, locator=raw["locator"]))
    missing = sorted(set(work) - {i["headword"] for i in items})
    assert not missing, missing
    for it in items:
        if it.get("found"):
            assert it["volume"] in (VOL_AS, VOL_TZ) and it["column"] in (1, 2) and 0 <= it["y"] <= 1, it
    (HERE / "locations.json").write_text(json.dumps({"items": items}, indent=1, ensure_ascii=False) + "\n", encoding="utf8")
    print(len(items), "items;", sum(1 for i in items if i.get("found")), "found")


def check():
    text, _, _ = do_lookup(write=False)
    assert (HERE / "lookups.json").read_text(encoding="utf8") == text, "lookups.json differs"
    m = json.load(open(HERE / "entries-manifest.json", encoding="utf8"))
    for rec in m["entries"]:
        for p in rec["parts"]:
            assert sha(OUT / "crops" / p["file"]) == p["sha256"], p["file"]
    print("lookups reproduce;", len(m["entries"]), "entries, crop hashes match")


def restore():
    m = json.load(open(HERE / "entries-manifest.json", encoding="utf8"))
    for rec in m["entries"]:
        for p in rec["parts"]:
            fetch(p["url"], OUT / "crops" / p["file"])
    check()


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "lookup":
        _, out, work = do_lookup()
        print(len(out), "headwords;", collections.Counter(o["tier"] for o in out), ";", len(work), "to locators")
    elif arg == "merge-locations":
        merge_locations()
    elif arg == "manifest":
        do_manifest()
    elif arg == "--fetch":
        restore()
    elif arg == "--check":
        check()
    else:
        print(__doc__)

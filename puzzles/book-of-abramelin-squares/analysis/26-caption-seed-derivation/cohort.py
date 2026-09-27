#!/usr/bin/env python3
"""Build the caption cohort for experiment 26. Reads captions and headings only, never a letter.

Inputs: experiment 25's locator inventory (pages 246-272) and experiment 22's
source-only locator audit (pages 243-245). Output: cohort.json, and the
nominators' input, nominator-input.json, which holds captions and chapter
headings and nothing else.

python3 cohort.py           write both files
python3 cohort.py --check   verify both reproduce
"""
import collections, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
A = HERE.parent
BARE = re.compile(r"^\s*\d+\s*[.:]?\s*$")
CAP = re.compile(r"Cap(?:ut)?\s*[:.]?\s*(\d+)", re.I)


def headings():
    """Chapter number -> heading as written. Pages 243-245 from experiment 22, the rest from 25."""
    out = {}
    for g in json.load(open(A / "22-dresden-witness-pilot" / "locator-audit.json"))["grids"]:
        out.setdefault(g["source_chapter"], g["chapter_heading"]["literal"])
    for p in json.load(open(A / "25-dresden-blind-test" / "inventory.json"))["pages"]:
        for h in p["headings"]:
            m = CAP.search(h["text"])
            if m:
                out.setdefault(int(m.group(1)), h["text"])
    return out


def build():
    heads = headings()
    grids = []
    for g in json.load(open(A / "22-dresden-witness-pilot" / "locator-audit.json"))["grids"]:
        cap = g["literal_short_heading"]
        grids.append({"key": g["id"], "source": "dresden-243-245", "chapter": g["source_chapter"],
                      "item": g["item_number"], "caption": cap,
                      "cohort": "A-bare" if BARE.match(cap) else "A"})
    for g in json.load(open(A / "25-dresden-blind-test" / "inventory.json"))["grids"]:
        cap = g["short_heading"]
        if g["item"] is None:
            cohort = "excluded-unnumbered"
        elif BARE.match(cap):
            cohort = "P-bare"
        else:
            cohort = "P"
        grids.append({"key": g["locator_id"], "source": "dresden-246-272", "chapter": g["chapter"],
                      "item": g["item"], "caption": cap, "cohort": cohort,
                      "shape": [g["rows"], g["columns"]]})
    counts = collections.Counter(g["cohort"] for g in grids)
    cohort = {"source": "captions and headings only; no letters are read by this script",
              "chapter_headings": {str(k): v for k, v in sorted(heads.items())},
              "counts": dict(sorted(counts.items())), "grids": grids}
    chapters = []
    for ch in sorted({g["chapter"] for g in grids}):
        items = [{"key": g["key"], "item": g["item"], "caption": g["caption"]}
                 for g in grids if g["chapter"] == ch and g["cohort"] != "excluded-unnumbered"]
        if items:
            chapters.append({"chapter": ch, "heading": heads.get(ch, ""), "items": items})
    nominator = {"note": "Book IV of a German manuscript, one caption per item, in manuscript order. "
                         "'„' and '-' inside a word mark a line break; [a/b] marks a reading the "
                         "transcriber could not decide between.",
                 "chapters": chapters}
    return cohort, nominator


def main():
    cohort, nominator = build()
    files = {"cohort.json": cohort, "nominator-input.json": nominator}
    for name, data in files.items():
        text = json.dumps(data, indent=1, ensure_ascii=False) + "\n"
        if "--check" in sys.argv:
            assert (HERE / name).read_text(encoding="utf8") == text, f"{name} differs"
        else:
            (HERE / name).write_text(text, encoding="utf8")
    print(json.dumps(cohort["counts"]), "chapters", len(nominator["chapters"]),
          "reproduce" if "--check" in sys.argv else "written")


if __name__ == "__main__":
    main()

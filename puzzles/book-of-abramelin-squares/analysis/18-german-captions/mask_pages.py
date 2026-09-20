#!/usr/bin/env python3
"""Cut the Warburg pages into caption-only and square-only page images.

Input: out/bands.json (bands.py) and the layout-*.json files written by the
layout subagents (band numbers and x ranges, no letters). For every page this
pastes the kept blocks onto a white canvas at their own position and writes a
label (chapter.item) in a left margin:

  out/captions/pNNN.png  chapter headings and captions only
  out/squares/pNNN.png   letter squares and the row lists printed under a
                         caption ("list of names under caption"), nothing else

A caption transcriber never sees a square letter; a square reader never sees a
caption. The main thread looks at neither square output before the experiment
20 freeze.
"""
import glob, json, pathlib, subprocess
import bands as bandlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "out"
PAD, MARGIN = 5, 110


def is_rows(b):
    n = b.get("note", "").lower()
    return b["type"] == "square" or (b["type"] == "prose" and ("list of names" in n or "numbered item" in n))


def split_row(page, y0, y1):
    """A band that holds a caption line on top of a row line (one case, p364):
    split at the row with least ink in the middle 40 % of the band."""
    w, h, px = bandlib.read_pgm(OUT / "pages" / f"p{int(page):03d}.pgm")
    lo, hi = y0 + int(0.3 * (y1 - y0)), y0 + int(0.7 * (y1 - y0))
    return min(range(lo, hi), key=lambda y: sum(1 for v in px[y * w:(y + 1) * w] if v < bandlib.DARK))


def main():
    bands = json.load(open(OUT / "bands.json"))
    pages = {}
    for f in sorted(glob.glob(str(HERE / "layout-*.json"))):
        pages.update(json.load(open(f))["pages"])
    index = {"captions": [], "squares": []}
    for kind, keep in (("captions", lambda b: b["type"] in ("caption", "chapter_heading")), ("squares", is_rows)):
        (OUT / kind).mkdir(exist_ok=True)
        for page, info in sorted(pages.items(), key=lambda kv: int(kv[0])):
            blocks = [b for b in info["blocks"] if keep(b)]
            if not blocks:
                continue
            W, H, bd = bands[page]["width"], bands[page]["height"], bands[page]["bands"]
            cmd = ["magick", "-size", f"{W + MARGIN}x{H}", "xc:white"]
            last_item = None
            for b in blocks:
                y0 = max(bd[b["bands"][0]][0] - PAD, 0)
                y1 = min(bd[b["bands"][1]][1] + PAD, H)
                for o in info["blocks"]:       # a caption and a row list sharing one band
                    if o is not b and is_rows(o) != is_rows(b) and o["type"] in ("caption", "square", "prose") and (is_rows(o) or o["type"] == "caption"):
                        if o["bands"][1] == b["bands"][0] and not is_rows(o):      # caption above, inside my first band
                            y0 = split_row(page, *bd[b["bands"][0]])
                        if o["bands"][0] == b["bands"][1] and is_rows(o):          # rows below, inside my last band
                            y1 = split_row(page, *bd[b["bands"][1]])
                x0, x1 = int(b["x"][0] * W), int(b["x"][1] * W)
                if kind == "captions" or b["type"] != "square":
                    x0, x1 = 0, W              # text lines: full width, the band holds nothing else
                cmd += ["(", str(OUT / "pages" / f"p{int(page):03d}.png"), "-crop", f"{x1 - x0}x{y1 - y0}+{x0}+{y0}", "+repage", ")",
                        "-geometry", f"+{x0 + MARGIN}+{y0}", "-composite"]
                items = b.get("items") or []
                label = f'c{b["chapter"]}' + (f'.{items[0]}' if items else "")
                if kind == "squares" and not items:
                    label = f'c{b["chapter"]}.after{last_item}' if last_item else label
                if items:
                    last_item = items[0]
                cmd += ["-fill", "blue", "-pointsize", "20", "-draw", f"text 2,{(y0 + y1) // 2 + 7} '{label}'"]
                index[kind].append({"page": int(page), "chapter": b["chapter"], "items": items, "type": b["type"], "label": label})
            cmd.append(str(OUT / kind / f"p{int(page):03d}.png"))
            subprocess.run(cmd, check=True)
    (HERE / "mask-index.json").write_text(json.dumps(index, indent=0) + "\n")
    print({k: len(v) for k, v in index.items()})


if __name__ == "__main__":
    main()

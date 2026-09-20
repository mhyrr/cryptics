#!/usr/bin/env python3
"""Render Warburg PDF pages and cut each into horizontal ink bands.

The main thread must not look at the square letters before the experiment 20
freeze, so page layout is labelled by a subagent. To make its labels exact,
this script renders each page (Poppler, 300 dpi, grey), finds horizontal bands
of ink from the row projection, writes them to bands.json, and draws the band
numbers in the left margin of a copy of the page (ImageMagick). The subagent
answers in band numbers; crops are then cut by code.

usage: bands.py FIRST LAST
"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
PDF = HERE.parents[1] / "sources" / "warburg-1853.pdf"
OUT = HERE / "out"
DPI, DARK, MIN_INK, GAP, MIN_H = 300, 128, 6, 5, 8


def read_pgm(path):
    data = path.read_bytes()
    parts, pos = [], 0
    while len(parts) < 4:
        end = pos
        while data[end:end + 1] not in (b" ", b"\n", b"\t"):
            end += 1
        tok = data[pos:end]
        pos = end + 1
        if tok.startswith(b"#"):
            pos = data.index(b"\n", pos) + 1
            continue
        if tok:
            parts.append(tok)
    w, h = int(parts[1]), int(parts[2])
    return w, h, data[pos:pos + w * h]


def bands_of(w, h, px):
    ink = [sum(1 for v in px[y * w:(y + 1) * w] if v < DARK) >= MIN_INK for y in range(h)]
    out, y = [], 0
    while y < h:
        if ink[y]:
            y0 = y
            gap = 0
            while y < h and gap <= GAP:
                gap = 0 if ink[y] else gap + 1
                y += 1
            y1 = y - gap
            if y1 - y0 >= MIN_H:
                out.append([y0, y1])
        else:
            y += 1
    return out


def main():
    first, last = int(sys.argv[1]), int(sys.argv[2])
    p = OUT / "bands.json"
    doc = json.loads(p.read_text()) if p.exists() else {}
    for page in range(first, last + 1):
        stem = OUT / "pages" / f"p{page:03d}"
        subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(DPI), "-gray", "-singlefile", str(PDF), str(stem)], check=True)
        w, h, px = read_pgm(stem.with_suffix(".pgm"))
        bands = bands_of(w, h, px)
        doc[str(page)] = {"width": w, "height": h, "bands": bands}
        draw = []
        for k, (y0, y1) in enumerate(bands):
            draw += ["-fill", "none", "-stroke", "red", "-draw", f"line 60,{y0} {w + 60},{y0}",
                     "-fill", "red", "-stroke", "none", "-draw", f"text 4,{(y0 + y1) // 2 + 8} '{k}'"]
        subprocess.run(["magick", str(stem.with_suffix(".pgm")), "-colorspace", "sRGB", "-background", "white",
                        "-splice", "60x0", "-pointsize", "22", *draw, str(OUT / "banded" / f"p{page:03d}.png")], check=True)
        subprocess.run(["magick", str(stem.with_suffix(".pgm")), str(stem.with_suffix(".png"))], check=True)
    p.write_text(json.dumps(doc, indent=0) + "\n")
    print("pages", first, last, "bands", sum(len(doc[str(k)]["bands"]) for k in range(first, last + 1)))


if __name__ == "__main__":
    main()

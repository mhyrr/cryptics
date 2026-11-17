"""kcrop.py - cut a rectangle from a VI/82 key-sheet image for the outside-check agent to look at.

    python3 kcrop.py <page> <x> <y> <w> <h> <out.jpg> [scale]

<page> is the middle of the file name in ../cache/keysheets/ (e.g. 04_2r). Pixels are of the 300 dpi master.
Uses ../crop.py's BMP reader and `sips`. The crops are scratch views, not checked in: they show key values.
"""
import os, sys, subprocess
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import crop

def main(page, x, y, w, h, out, scale=1.0):
    src = os.path.join(crop.CACHE, "keysheets", "VI_82_%s.jpg" % page)
    bmp = out + ".full.bmp"
    cache = os.path.join(os.path.dirname(out), "full_%s.bmp" % page)
    if not os.path.exists(cache):
        crop.sips("-s", "format", "bmp", src, "--out", cache)
    W, H, rows = crop.read_bmp(cache)
    x, y = max(0, x), max(0, y)
    x1, y1 = min(W, x + w), min(H, y + h)
    tmp = out + ".bmp"
    crop.write_bmp(tmp, rows, x, y, x1, y1)
    args = ["-s", "format", "jpeg", "-s", "formatOptions", "90"]
    if scale != 1.0:
        args += ["-z", str(int((y1 - y) * scale)), str(int((x1 - x) * scale))]
    crop.sips(*args, tmp, "--out", out)
    os.remove(tmp)

if __name__ == "__main__":
    a = sys.argv
    main(a[1], int(a[2]), int(a[3]), int(a[4]), int(a[5]), a[6], float(a[7]) if len(a) > 7 else 1.0)

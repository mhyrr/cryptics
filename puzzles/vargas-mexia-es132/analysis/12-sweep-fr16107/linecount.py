"""Estimate text lines per page in the 900 px spreads of fr. 16107.
Method: row ink profile of each half-spread; line pitch from the autocorrelation
peak (lags 7-30 px); lines = height of inked block / pitch.
Usage: uv run --with pillow python3 linecount.py FIRST LAST > linecounts.tsv
Rough: an estimate to +-20%; blank pages give 0; bleed-through can add lines."""
import sys
from PIL import Image
CACHE = "../../sources/cache/fr16107/v{}.jpg"
def page_lines(im):
    g = im.convert("L"); w, h = g.size; px = g.load()
    x0, x1, y0, y1 = int(w*.12), int(w*.88), int(h*.05), int(h*.95)
    vals = [px[x, y] for y in range(y0, y1, 4) for x in range(x0, x1, 4)]
    vals.sort(); paper = vals[int(len(vals)*.8)]
    cut = paper - 60
    prof = [sum(1 for x in range(x0, x1, 2) if px[x, y] < cut) / ((x1-x0)/2) for y in range(y0, y1)]
    sm = [sum(prof[max(0,i-3):i+4])/7 for i in range(len(prof))]
    ink = [i for i, v in enumerate(sm) if v > .04]
    if len(ink) < 20 or ink[-1] - ink[0] < 60: return 0
    a, b = ink[0], ink[-1]
    seg = prof[a:b+1]; m = sum(seg)/len(seg); d = [s-m for s in seg]
    best, pitch = -1e9, None
    for lag in range(7, 31):
        c = sum(d[i]*d[i+lag] for i in range(len(d)-lag)) / (len(d)-lag)
        if c > best: best, pitch = c, lag
    if best <= 0: return 0
    covered = sum(1 for v in sm[a:b+1] if v > .04)
    return round(covered / pitch)
if __name__ == "__main__":
    a, b = int(sys.argv[1]), int(sys.argv[2])
    print("view\tleft\tright")
    for v in range(a, b+1):
        im = Image.open(CACHE.format(v)); w, h = im.size
        print(f"{v}\t{page_lines(im.crop((0,0,w//2,h)))}\t{page_lines(im.crop((w//2,0,w,h)))}")

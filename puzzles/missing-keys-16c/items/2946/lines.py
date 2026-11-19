"""lines.py - find the text lines on a page from its ink components, with one slope per page.

    python3 -I lines.py cache/2947-691.jpg --box W,H,X,Y [--hmin 7] [--amin 30] [--slope S] [--overlay out.png]

Binarizes the box at Otsu's threshold (line/sign_height.py) and keeps components 7-22 px high with area 30 or
more: cipher signs and clear letters. The faint small gloss between the lines mostly falls under that size,
which is why components work here (on the glossed pages raise --hmin and --amin until the gloss drops out) and a row profile did not (the profile put peaks on gloss rows and on the
large initial). For each slope from -0.012 to 0.012 (step 0.001; --slope fixes it) the component centres are projected to
y - slope * x; the slope whose histogram is sharpest wins. Lines are the histogram's peaks (smoothed over 5 px,
at least 0.6 of the median pitch apart, holding at least 6 components).

Prints: n, y of the line centre at x = 0 in page pixels, slope, components on the line, x span.
The overlay draws each line in red with its number. It is the check; corrections go in lines.tsv by hand.
"""
import os, statistics, subprocess, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "line"))
from sign_height import load_pgm, otsu, components  # noqa: E402


def comps(path, box, hmin=7, amin=30):
    w, h, px = load_pgm(path, box)
    t = otsu(px)
    ink = [v <= t for v in px]
    out = []
    for c in components(w, h, ink):
        x0, y0, x1, y1, area = c
        hh = y1 - y0 + 1
        if hmin <= hh <= 22 and area >= amin and x1 - x0 < 60:
            out.append(((x0 + x1) / 2 + box[2], (y0 + y1) / 2 + box[3]))
    return out


def hist(cs, s, lo, hi):
    hgt = [0.0] * (hi - lo + 1)
    for x, y in cs:
        k = round(y - s * x) - lo
        if 0 <= k < len(hgt):
            hgt[k] += 1
    return [sum(hgt[max(0, i - 2):i + 3]) for i in range(len(hgt))]


def main(a):
    path = a[0]
    box = tuple(int(v) for v in a[a.index("--box") + 1].split(","))
    hmin = int(a[a.index("--hmin") + 1]) if "--hmin" in a else 7
    amin = int(a[a.index("--amin") + 1]) if "--amin" in a else 30
    cs = comps(path, box, hmin, amin)
    lo, hi = box[3] - 60, box[3] + box[1] + 60
    if "--slope" in a:
        s = float(a[a.index("--slope") + 1])
    else:
        s = max((sum(v * v for v in hist(cs, k / 1000, lo, hi)), k / 1000) for k in range(-12, 13))[1]
    hg = hist(cs, s, lo, hi)
    raw = [i for i in range(len(hg)) if hg[i] >= 6 and hg[i] == max(hg[max(0, i - 8):i + 9])]
    pitch = statistics.median(b - a_ for a_, b in zip(raw, raw[1:])) if len(raw) > 2 else 25
    pk = []
    for i in raw:
        if pk and i - pk[-1] < 0.6 * pitch:
            if hg[i] > hg[pk[-1]]:
                pk[-1] = i
            continue
        pk.append(i)
    lines = [p + lo for p in pk]
    for n, y in enumerate(lines, 1):
        on = [x for x, yy in cs if abs(yy - s * x - y) <= pitch / 2]
        print(f"{n}\t{y}\t{s:.3f}\t{len(on)}\t{min(on):.0f}-{max(on):.0f}" if on else f"{n}\t{y}\t{s:.3f}\t0\t-")
    if "--overlay" in a:
        out = a[a.index("--overlay") + 1]
        draw = []
        for n, y in enumerate(lines, 1):
            draw += ["-draw", f"line 0,{y:.0f} 1400,{y + s * 1400:.0f}", "-draw", f"text 2,{y - 3:.0f} '{n}'"]
        subprocess.run(["magick", path, "-stroke", "red", "-strokewidth", "1", "-fill", "red", "-pointsize", "13",
                        *draw, out], check=True)


if __name__ == "__main__":
    main(sys.argv[1:])

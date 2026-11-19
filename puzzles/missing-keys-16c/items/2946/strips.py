"""strips.py - cut the reading strips for item 2946 / 2947 from cache/*.jpg (ImageMagick `magick`).

    python3 -I strips.py

Each page gets a ruler: a white column at the left with the page's y in pixels every 20 px. Then bands of
the text block, 150 px high every 110 px (about five lines, each band repeating the last line or two of the
band before), each cut in a left and a right half that overlap by 80 px, enlarged 3x. The ruler is pasted to
the left of both halves, so a reader can name a line by its y.
Out: cache/strips/<page>-b<NN><L|R>.png. Per-line cuts were tried (lines.py) and failed on the glossed pages:
the gloss between the lines and curved lines defeat one slope per page; the line frame comes from the
clear-word readers instead (METHOD step 2).
"""
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
C, S = os.path.join(HERE, "cache"), os.path.join(HERE, "cache", "strips")
RW = 46            # ruler width, page px
PAGES = {          # page: (top, bottom) of the text block in page px; x is 80-1240 on all
    "2946-c215": (190, 760),
    "2947-691": (220, 1680),
    "2947-692": (190, 1660),
    "2947-693": (170, 1640),
    "2947-694": (170, 800),
}
XL, XR, XM = (80, 700), (620, 1240), 0


def ruled(page):
    out = os.path.join(S, f"_{page}-ruled.png")
    src = os.path.join(C, page + ".jpg")
    h = int(subprocess.run(["magick", "identify", "-format", "%h", src], capture_output=True, text=True,
                           check=True).stdout)
    draw = []
    for y in range(0, h, 20):
        draw += ["-draw", f"line {RW - 8},{y} {RW},{y}", "-draw", f"text 2,{y + 4} '{y}'"]
    subprocess.run(["magick", src, "-strip", "-background", "white", "-gravity", "west", "-splice", f"{RW}x0",
                    "-gravity", "northwest", "-fill", "black", "-stroke", "none", "-pointsize", "10", *draw, out],
                   check=True)
    return out


def cut(img, y0, y1, xs, out):
    h = y1 - y0
    subprocess.run(["magick", "(", img, "-crop", f"{RW}x{h}+0+{y0}", "+repage", ")",
                    "(", img, "-crop", f"{xs[1] - xs[0]}x{h}+{xs[0] + RW}+{y0}", "+repage", ")",
                    "+append", "-resize", "300%", "-unsharp", "0x1", out], check=True)


def main():
    os.makedirs(S, exist_ok=True)
    for f in os.listdir(S):
        os.remove(os.path.join(S, f))
    n = 0
    for page, (top, bottom) in PAGES.items():
        img = ruled(page)
        b, y = 1, top
        while y < bottom:
            y1 = min(y + 150, bottom + 20)
            cut(img, y, y1, XL, os.path.join(S, f"{page}-b{b:02d}L.png"))
            cut(img, y, y1, XR, os.path.join(S, f"{page}-b{b:02d}R.png"))
            n += 2
            b, y = b + 1, y + 110
    print(n, "strips")


if __name__ == "__main__":
    main()

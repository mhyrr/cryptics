"""strips.py - cut the reading strips for item 2351 from cache/orig/*.png (ImageMagick `magick`).

    python3 strips.py
Clear copy, c. 233 (79572.png): bands p233-01 … of about four lines, each sharing about one and a half lines
with the band before, enlarged 2x.
Round 2 of the clear copy (2026-11-18, after two readers left over half the words unread): the red channel
only, which drops the red-brown show-through, levels stretched, enlarged 3x. Bands q233-<nn><L|R> of about
three lines, left and right halves overlapping by a fifth of the width.
Cipher strips are added below once the sign guide is frozen.
"""
import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
C, S = os.path.join(HERE, "cache", "orig"), os.path.join(HERE, "cache", "strips")


def cut(src, box, scale, out):
    w, h, x, y = box
    subprocess.run(["magick", os.path.join(C, src), "-crop", f"{w}x{h}+{x}+{y}", "+repage", "-resize",
                    f"{scale}%", "-unsharp", "0x1", os.path.join(S, out)], check=True)


def cut_red(src, box, out):
    w, h, x, y = box
    subprocess.run(["magick", os.path.join(C, src), "-crop", f"{w}x{h}+{x}+{y}", "+repage", "-channel", "R",
                    "-separate", "+channel", "-filter", "Mitchell", "-resize", "300%", "-level", "12%,88%",
                    "-unsharp", "0x1.5+0.6+0.02", "-strip", os.path.join(S, out)], check=True)


def main():
    os.makedirs(S, exist_ok=True)
    for f in os.listdir(S):
        os.remove(os.path.join(S, f))
    for n, y in enumerate(range(20, 1060, 125), 1):
        cut("79572.png", (1375, 200, 0, y), 200, f"p233-{n:02d}.jpg")
    for n, y in enumerate(range(20, 1100, 85), 1):
        cut_red("79572.png", (780, 150, 0, y), f"q233-{n:02d}L.jpg")
        cut_red("79572.png", (780, 150, 595, y), f"q233-{n:02d}R.jpg")
    print(len(os.listdir(S)), "strips")


if __name__ == "__main__":
    main()

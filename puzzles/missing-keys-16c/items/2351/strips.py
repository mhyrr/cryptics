"""strips.py - cut the reading strips for item 2351 from cache/orig/*.png (ImageMagick `magick`).

    python3 strips.py
Clear copy, c. 233 (79572.png): bands p233-01 … of about four lines, each sharing about one and a half lines
with the band before, enlarged 2x.
Round 2 of the clear copy (2026-11-18, after two readers left over half the words unread): the red channel
only, which drops the red-brown show-through, levels stretched, enlarged 3x. Bands q233-<nn><L|R> of about
three lines, left and right halves overlapping by a fifth of the width.
Letter A in cipher (c. 232 recto = 79570-a/-b, its end = 79571): grey, levels stretched, enlarged 4x. Bands
A01 … A13 of about three lines, each repeating the last line of the band before; each band in thirds a, b, c
(left to right, overlapping). A01–A07 are cut from 79570-a, A08–A10 from 79570-b below the lines 79570-a
already shows, A11–A13 from 79571. A<nn>-all.jpg shows the band's whole width at 1.5x for orientation.
Letter B the same way: B01–B07 from 79574-a, B08–B12 from 79574-b, B13–B17 from 79575-a, B18–B22 from 79575-b.
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


def cut_grey(src, box, scale, out):
    w, h, x, y = box
    subprocess.run(["magick", os.path.join(C, src), "-crop", f"{w}x{h}+{x}+{y}", "+repage", "-colorspace",
                    "Gray", "-filter", "Mitchell", "-resize", f"{scale}%", "-level", "10%,85%", "-unsharp",
                    "0x1.5+0.6+0.02", "-strip", os.path.join(S, out)], check=True)


def bands(src, ys, first, height, x0s, width, total, letter="A"):
    for k, y in enumerate(ys):
        n = first + k
        for name, x in zip("abc", x0s):
            cut_grey(src, (width, height, x, y), 400, f"{letter}{n:02d}{name}.jpg")
        cut_grey(src, (total, height, 0, y), 150, f"{letter}{n:02d}-all.jpg")


def main():
    os.makedirs(S, exist_ok=True)
    for f in os.listdir(S):
        os.remove(os.path.join(S, f))
    for n, y in enumerate(range(20, 1060, 125), 1):
        cut("79572.png", (1375, 200, 0, y), 200, f"p233-{n:02d}.jpg")
    for n, y in enumerate(range(20, 1100, 85), 1):
        cut_red("79572.png", (780, 150, 0, y), f"q233-{n:02d}L.jpg")
        cut_red("79572.png", (780, 150, 595, y), f"q233-{n:02d}R.jpg")
    bands("79570-a.png", (195, 333, 471, 609, 747, 885, 951), 1, 215, (40, 400, 764), 470, 1234)
    bands("79570-b.png", (345, 483, 621), 8, 215, (40, 395, 750), 470, 1220)
    bands("79571.png", (130, 255, 380), 11, 190, (90, 440, 774), 470, 1244)
    # letter B: c. 234 (79574-a/-b), its continuation (79575-a/-b)
    bands("79574-a.png", (110, 248, 386, 524, 662, 800, 869), 1, 215, (110, 470, 830), 470, 1307, "B")
    bands("79574-b.png", (135, 273, 411, 549, 641), 8, 215, (130, 480, 836), 470, 1310, "B")
    bands("79575-a.png", (125, 263, 401, 539, 630), 13, 215, (60, 395, 725), 470, 1198, "B")
    bands("79575-b.png", (5, 160, 298, 436, 520), 18, 215, (70, 430, 788), 470, 1261, "B")
    print(len(os.listdir(S)), "strips")


if __name__ == "__main__":
    main()

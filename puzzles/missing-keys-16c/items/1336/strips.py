"""strips.py - cut the reading strips for item 1336 from cache/*.jpg (ImageMagick `magick`; geometry here).

    python3 strips.py
Cipher slip F 47 inf. c. 269r: 13 lines in a drawn frame. Seven bands down the slip, each about four lines
high and sharing about two lines with the band before; each band in thirds a, b, c (left to right,
overlapping), enlarged 5x: cache/strips/c269-<band><a|b|c>.jpg. The right thirds are cut lower because the
lines slope. c269-all-<1..3>.jpg show the whole width for orientation (3x).
Cipher slip F 49 inf. c. 44r: c44-L.jpg, c44-R.jpg (6x, all three lines, overlapping).
Cipher line F 131 inf. c. 14r: c14-a.jpg, c14-b.jpg, c14-c.jpg (6x).
Clear text F 47 inf. c. 270r: p270-<nn>.jpg, bands of about three lines, each repeating the last line of the
band before (3x). Clear note under the slip on c. 44r: p44-a.jpg, p44-b.jpg (4x).
"""
import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
C, S = os.path.join(HERE, "cache"), os.path.join(HERE, "cache", "strips")


def cut(src, box, scale, out):
    w, h, x, y = box
    subprocess.run(["magick", os.path.join(C, src), "-crop", f"{w}x{h}+{x}+{y}", "+repage", "-resize",
                    f"{scale}%", "-unsharp", "0x1", os.path.join(S, out)], check=True)


def main():
    os.makedirs(S, exist_ok=True)
    for f in os.listdir(S):
        os.remove(os.path.join(S, f))
    thirds = {"a": (15, 0.0), "b": (200, 0.5), "c": (385, 1.0)}
    for b in range(7):
        for name, (x0, f) in thirds.items():
            y = 196 + 41 * b + int(f * (4 + 4.5 * b))          # the lines slope down to the right, more so lower
            cut("F47-269r.jpg", (227, 100, x0, y), 500, f"c269-{b + 1}{name}.jpg")
    for n, y in enumerate((195, 290, 395), 1):
        cut("F47-269r.jpg", (597, 135, 15, y), 300, f"c269-all-{n}.jpg")
    cut("F49-44r.jpg", (310, 140, 55, 450), 600, "c44-L.jpg")
    cut("F49-44r.jpg", (320, 140, 340, 450), 600, "c44-R.jpg")
    for name, x0 in (("a", 60), ("b", 205), ("c", 350)):
        cut("F131-14r.jpg", (190, 44, x0, 193), 600, f"c14-{name}.jpg")
    for n, y in enumerate(range(190, 740, 80), 1):
        cut("F47-270r.jpg", (580, 135, 20, y), 300, f"p270-{n:02d}.jpg")
    cut("F49-44r.jpg", (330, 80, 60, 625), 400, "p44-a.jpg")
    cut("F49-44r.jpg", (330, 80, 330, 625), 400, "p44-b.jpg")
    print(len(os.listdir(S)), "strips")


if __name__ == "__main__":
    main()

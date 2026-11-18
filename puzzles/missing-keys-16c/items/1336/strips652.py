"""strips652.py - reading strips for F 46 inf. n. 275, c. 652r (image 11447 in cache/more/). ImageMagick.

    python3 strips652.py
A memorandum of 13 lines, clear Italian with runs of cipher in lines 4-7 and 10-12.
c652-<line><a|b|c>.jpg: one manuscript line (with a little of its neighbours), in thirds left to right,
overlapping, 6x. c652-<line>-all.jpg: the whole line, 3x. p652-<n>.jpg: three lines at a time, whole width,
3x, for the clear words. All go to cache/strips652/ (not checked in).
"""
import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
SRC, S = os.path.join(HERE, "cache", "more", "11447.jpg"), os.path.join(HERE, "cache", "strips652")
LINES = {1: 212, 2: 248, 3: 285, 4: 322, 5: 355, 6: 388, 7: 420, 8: 455, 9: 490, 10: 525, 11: 560, 12: 592, 13: 645}


def cut(box, scale, out):
    w, h, x, y = box
    subprocess.run(["magick", SRC, "-crop", f"{w}x{h}+{x}+{y}", "+repage", "-filter", "Mitchell", "-resize",
                    f"{scale}%", "-unsharp", "0x1", os.path.join(S, out)], check=True)


def main():
    os.makedirs(S, exist_ok=True)
    for f in os.listdir(S):
        os.remove(os.path.join(S, f))
    for n in (4, 5, 6, 7, 10, 11, 12):
        y = LINES[n] - 26
        for name, x in zip("abc", (15, 215, 415)):
            cut((245, 50, x, y), 600, f"c652-{n:02d}{name}.jpg")
        cut((645, 50, 15, y), 300, f"c652-{n:02d}-all.jpg")
    for k, y in enumerate((190, 290, 395, 500, 570), 1):
        cut((645, 125, 15, y), 300, f"p652-{k}.jpg")
    print(len(os.listdir(S)), "strips")


if __name__ == "__main__":
    main()

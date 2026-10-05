"""Cut exp 07 spreads (spreads/cNNN.jpg) into folio pages, locally. Map checked on the images: canvas c shows f. (c+3)r on
its right page and f. (c+2)v on its left page (c197 R = f. 200, c200 R = f. 203). Each page keeps 400 px past the gutter.
    python3 split_spreads.py  -> exp07/fNNNr.jpg, exp07/fNNNv.jpg"""
import os, subprocess, glob, re
os.makedirs("exp07", exist_ok=True)
for p in sorted(glob.glob("spreads/c*.jpg")):
    c = int(re.findall(r"c(\d+)", p)[0])
    W, H = map(int, subprocess.check_output(["magick", "identify", "-format", "%w %h", p]).split())
    for name, x0, x1 in ((f"f{c+2:03d}v", 0, W // 2 + 400), (f"f{c+3:03d}r", W // 2 - 400, W)):
        out = f"exp07/{name}.jpg"
        if not os.path.exists(out):
            subprocess.run(["magick", p, "-crop", f"{x1-x0}x{H}+{x0}+0", "+repage", "-quality", "92", out], check=True)

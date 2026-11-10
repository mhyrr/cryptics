"""Second cut of the 23 Dec 1579 letter: half-width strips at native resolution, show-through suppressed.

Reader A reported that full-width strips (about 3,900 px, downscaled on display) left dense lines unresolved.
Each page is cut into a left (a) and right (b) half overlapping by 6% of the page width, in the same nine
vertical bands as crop.py. A gamma curve washes out the faint mirrored show-through.
Output: sources/cache/fr16106/halves/<page>-<nn><a|b>.jpg
Run   : uv run --with pillow python3 crop_half.py
"""
import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "..", "..", "sources", "cache", "fr16106")
OUT = os.path.join(CACHE, "halves")
os.makedirs(OUT, exist_ok=True)
PAGES = [("363r", 373, "R"), ("363v", 374, "L"), ("364r", 374, "R"), ("364v", 375, "L"),
         ("365r", 375, "R"), ("365v", 376, "L"), ("366r", 376, "R")]
X = {"L": (0.03, 0.51), "R": (0.49, 0.98)}
Y0, Y1, H, STEP = 0.03, 0.97, 0.13, 0.105
LUT = [min(255, int(255 * (min(v, 200) / 200) ** 2.2)) for v in range(256)]
n_out = 0
for page, view, side in PAGES:
    im = Image.open(os.path.join(CACHE, "full", f"v{view}.jpg")).convert("L")
    w, h = im.size
    x0, x1 = X[side]
    xm = (x0 + x1) / 2
    y, n = Y0, 1
    while y < Y1 - 0.03:
        ya, yb = y, min(y + H, Y1)
        for tag, (xa, xb) in {"a": (x0, xm + 0.03), "b": (xm - 0.03, x1)}.items():
            c = im.crop((int(w * xa), int(h * ya), int(w * xb), int(h * yb))).point(LUT)
            c.save(os.path.join(OUT, f"{page}-{n:02d}{tag}.jpg"), quality=90)
            n_out += 1
        y += STEP
        n += 1
print(n_out, "half strips")

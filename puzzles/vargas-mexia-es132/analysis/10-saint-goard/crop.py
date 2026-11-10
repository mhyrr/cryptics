"""Cut the 23 Dec 1579 cipher letter (BnF fr. 16106 ff. 363r-366v, Gallica views 373-377)
into overlapping horizontal strips for glyph reading.

Input : sources/cache/fr16106/full/vNNN.jpg  (full-resolution Gallica IIIF spreads, not in git)
Output: sources/cache/fr16106/strips/<page>-<nn>.jpg and strips/manifest.tsv
Run   : uv run --with pillow python3 crop.py
"""
import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "..", "..", "sources", "cache", "fr16106")
OUT = os.path.join(CACHE, "strips")
os.makedirs(OUT, exist_ok=True)
# page id -> (view, side). L = verso of previous folio, R = recto.
PAGES = [("363r", 373, "R"), ("363v", 374, "L"), ("364r", 374, "R"), ("364v", 375, "L"),
         ("365r", 375, "R"), ("365v", 376, "L"), ("366r", 376, "R"), ("366v", 377, "L")]
X = {"L": (0.03, 0.51), "R": (0.49, 0.98)}
Y0, Y1, H, STEP = 0.03, 0.97, 0.13, 0.105
rows = []
for page, view, side in PAGES:
    im = Image.open(os.path.join(CACHE, "full", f"v{view}.jpg")).convert("L")
    w, h = im.size
    x0, x1 = X[side]
    y, n = Y0, 1
    while y < Y1 - 0.03:
        ya, yb = y, min(y + H, Y1)
        name = f"{page}-{n:02d}.jpg"
        im.crop((int(w * x0), int(h * ya), int(w * x1), int(h * yb))).save(os.path.join(OUT, name), quality=88)
        rows.append(f"{name}\t{page}\t{view}\t{side}\t{ya:.3f}\t{yb:.3f}")
        y += STEP
        n += 1
with open(os.path.join(OUT, "manifest.tsv"), "w") as f:
    f.write("strip\tpage\tview\tside\ty0\ty1\n" + "\n".join(rows) + "\n")
print(len(rows), "strips")

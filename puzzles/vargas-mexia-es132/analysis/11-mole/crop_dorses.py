"""Crop the half-spreads that carry dorses / royal notes / countersignatures, enlarged 2x.
Input : sources/cache/fr16106/vNNN.jpg (1,800 px spreads). Output: sources/cache/fr16106/crops/mole-vNNN-S.jpg
Run   : uv run --with pillow python3 crop_dorses.py
"""
import os
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "..", "..", "sources", "cache", "fr16106")
OUT = os.path.join(CACHE, "crops"); os.makedirs(OUT, exist_ok=True)
# (view, side): L = left half, R = right half
JOBS = [(235, "L"), (369, "L"), (368, "L"), (384, "L"), (381, "L"), (271, "L"), (246, "R"), (285, "L"), (219, "R"), (239, "R")]
for v, s in JOBS:
    im = Image.open(os.path.join(CACHE, f"v{v}.jpg"))
    w, h = im.size
    box = (0, 0, w // 2 + 20, h) if s == "L" else (w // 2 - 20, 0, w, h)
    c = im.crop(box); c = c.resize((c.width * 2, c.height * 2), Image.LANCZOS)
    c.save(os.path.join(OUT, f"mole-v{v}-{s}.jpg"), quality=90)
    print(v, s, c.size)

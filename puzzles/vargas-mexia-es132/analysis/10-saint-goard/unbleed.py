"""Suppress show-through on one page by subtracting the mirrored image of the leaf's other side.

Usage: uv run --with pillow --with numpy python3 unbleed.py <page> <view> <side> <other_view> <other_side>
  e.g. 363v 374 L 373 R   (363v is the left page of view 374; its other side, 363r, is the right page of 373)
Method: a whole-page shift is found first (FFT at 1/8 scale). Then both pages are cropped by fixed fractions, the other side is flipped left-right, and the page is cut
into a 12x6 grid of tiles. For each tile the shift (within +-180 px, at 1/2 scale) that maximises the correlation
of ink darkness is found by FFT; out = page + ALPHA * ink(other, shifted). Tiles with weak correlation are
left unchanged. Output: sources/cache/fr16106/unbleed/<page>.png and nine half-strip pairs like crop_half.py.
This is an image aid, not evidence: a reading made from it is checked against the untouched strip.
"""
import os, sys
import numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "..", "..", "sources", "cache", "fr16106")
OUT = os.path.join(CACHE, "unbleed"); os.makedirs(OUT, exist_ok=True)
X = {"L": (0.03, 0.51), "R": (0.49, 0.98)}
ALPHA = 1.15
page, view, side, oview, oside = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), sys.argv[5]

def load(v, s):
    im = Image.open(os.path.join(CACHE, "full", f"v{v}.jpg")).convert("L")
    w, h = im.size
    return np.asarray(im.crop((int(w * X[s][0]), 0, int(w * X[s][1]), h)), dtype=np.float32)

P = load(view, side)
O = load(oview, oside)[:, ::-1]
h = min(P.shape[0], O.shape[0]); w = min(P.shape[1], O.shape[1])
P, O = P[:h, :w], O[:h, :w]
ink = lambda a: np.clip(200 - a, 0, 200)          # darkness, paper = 0
# coarse field first: unbounded FFT shifts on a 4x3 grid at 1/4 scale, then a least-squares affine fit
# (the two exposures differ by a small rotation, so one global shift is not enough)
def shift_of(pa, pb, R=None):
    a0, b0 = pa - pa.mean(), pb - pb.mean()
    cc = np.fft.fftshift(np.fft.irfft2(np.fft.rfft2(a0) * np.conj(np.fft.rfft2(b0)), s=a0.shape))
    cy, cx = cc.shape[0] // 2, cc.shape[1] // 2
    if R is not None:
        R = min(R, cy - 1, cx - 1)
        cc = cc[cy - R:cy + R + 1, cx - R:cx + R + 1]; cy = cx = R
    dy, dx = np.unravel_index(np.argmax(cc), cc.shape)
    return dy - cy, dx - cx, cc.max() / (np.sqrt((a0 ** 2).sum() * (b0 ** 2).sum()) + 1e-9)
pts = []
for r in range(4):
    for c in range(3):
        y0, y1, x0, x1 = r * h // 4, (r + 1) * h // 4, c * w // 3, (c + 1) * w // 3
        dy, dx, sc = shift_of(ink(P[y0:y1:4, x0:x1:4]), ink(O[y0:y1:4, x0:x1:4]))
        pts.append(((y0 + y1) / 2, (x0 + x1) / 2, dy * 4, dx * 4, sc))
pts = np.array(pts)
med = np.median(pts[:, 2:4], axis=0)
keep = (np.abs(pts[:, 2] - med[0]) < 150) & (np.abs(pts[:, 3] - med[1]) < 150)
A = np.c_[np.ones(keep.sum()), pts[keep, 0], pts[keep, 1]]
cy_, *_ = np.linalg.lstsq(A, pts[keep, 2], rcond=None)
cx_, *_ = np.linalg.lstsq(A, pts[keep, 3], rcond=None)
print('coarse tiles kept', int(keep.sum()), 'of 12; centre shift', int(cy_ @ [1, h / 2, w / 2]), int(cx_ @ [1, h / 2, w / 2]))
out = P.copy()
ROWS, COLS, S, PAD = 12, 6, 2, 160
log = []
for r in range(ROWS):
    for c in range(COLS):
        y0, y1 = r * h // ROWS, (r + 1) * h // ROWS
        x0, x1 = c * w // COLS, (c + 1) * w // COLS
        py = int(round(cy_ @ [1, (y0 + y1) / 2, (x0 + x1) / 2])); px = int(round(cx_ @ [1, (y0 + y1) / 2, (x0 + x1) / 2]))
        ys, xs = np.mgrid[y0:y1, x0:x1]
        Ot = O[np.clip(ys - py, 0, h - 1), np.clip(xs - px, 0, w - 1)]
        dy, dx, score = shift_of(ink(P[y0:y1:S, x0:x1:S]), ink(Ot[::S, ::S]), R=20)
        dy, dx = py + dy * S, px + dx * S
        log.append((r, c, dy, dx, round(float(score), 3)))
        if score < 0.08:
            continue
        sy, sx = np.clip(ys - dy, 0, h - 1), np.clip(xs - dx, 0, w - 1)
        out[y0:y1, x0:x1] = P[y0:y1, x0:x1] + ALPHA * ink(O[sy, sx]) * 0.45
out = np.clip(out, 0, 255).astype(np.uint8)
Image.fromarray(out).save(os.path.join(OUT, f"{page}.png"))
Y0, Y1, H, STEP = 0.03, 0.97, 0.13, 0.105
y, n = Y0, 1
im = Image.fromarray(out)
while y < Y1 - 0.03:
    ya, yb = int(h * y), int(h * min(y + H, Y1))
    im.crop((0, ya, int(w * 0.56), yb)).save(os.path.join(OUT, f"{page}-{n:02d}a.jpg"), quality=90)
    im.crop((int(w * 0.44), ya, w, yb)).save(os.path.join(OUT, f"{page}-{n:02d}b.jpg"), quality=90)
    y += STEP; n += 1
import collections
print('tiles', len(log), 'weak', sum(1 for l in log if l[4] < 0.08), 'median score', sorted(l[4] for l in log)[len(log)//2])

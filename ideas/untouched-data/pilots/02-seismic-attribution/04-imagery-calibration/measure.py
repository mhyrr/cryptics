"""Measure a dark-on-snow change between two named Sentinel-2 scenes around a point.

usage: uv run python measure.py LAT LON HALF_KM PRE_ID POST_ID [CONTROL_ID ...]
Reads the 10 m red band in a (2*HALF_KM)^2 window. A pixel is CHANGED if pre red >= 0.5 and
post red <= pre - 0.25 (the detector-v1 snow rule, at full resolution). Reports the largest
8-connected component: area, centroid, bounding length. For each CONTROL scene, reports the
share of that component's pixels that were already dark (red < 0.35) in the control.
"""
import json, sys, urllib.request

import numpy as np
import rasterio
from rasterio.warp import transform as wt
from rasterio.windows import from_bounds
from scipy import ndimage

import s2


def item(i):
    return json.load(urllib.request.urlopen(f"https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/{i}", timeout=60))


def red(it, lat, lon, half):
    off = 0.0 if it["properties"].get("earthsearch:boa_offset_applied", False) or float(it["properties"].get("s2:processing_baseline", "0") or 0) < 4 else -0.1
    with rasterio.Env(**s2.ENV):
        with rasterio.open(it["assets"]["red"]["href"]) as src:
            x, y = wt("EPSG:4326", src.crs, [lon], [lat]); h = half * 1000
            w = from_bounds(x[0] - h, y[0] - h, x[0] + h, y[0] + h, src.transform).round_offsets().round_lengths()
            a = src.read(1, window=w).astype("float32") / 10000 + off
            return a, src.window_transform(w), src.crs


lat, lon, half = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
pre, tr, crs = red(item(sys.argv[4]), lat, lon, half)
post, _, _ = red(item(sys.argv[5]), lat, lon, half)
ch = (pre >= 0.5) & (post <= pre - 0.25)
lab, n = ndimage.label(ch, structure=np.ones((3, 3)))
sizes = ndimage.sum(ch, lab, range(1, n + 1))
k = int(np.argmax(sizes)) + 1
comp = lab == k
rr, cc = np.where(comp)
cx, cy = tr * (cc.mean(), rr.mean())
clon, clat = wt(crs, "EPSG:4326", [cx], [cy])
print(f"pre {sys.argv[4]}  post {sys.argv[5]}")
print(f"changed pixels in window: {int(ch.sum())} ({ch.sum()*1e-4:.2f} km2); components: {n}")
print(f"largest component: {sizes[k-1]*1e-4:.2f} km2, centroid {clat[0]:.4f}, {clon[0]:.4f}, "
      f"extent {(rr.max()-rr.min())*0.01:.1f} km N-S x {(cc.max()-cc.min())*0.01:.1f} km E-W; "
      f"second largest {sorted(sizes)[-2]*1e-4:.2f} km2")
print(f"mean red in component: pre {pre[comp].mean():.2f}, post {post[comp].mean():.2f}")
for cid in sys.argv[6:]:
    c, _, _ = red(item(cid), lat, lon, half)
    print(f"control {cid}: mean red in component {c[comp].mean():.2f}; share already dark (<0.35): {(c[comp] < 0.35).mean():.2f}")

# Seasonal-melt filter: keep only changed pixels that were still bright (red >= 0.5) in every control scene.
if len(sys.argv) > 6:
    keep = ch.copy()
    for cid in sys.argv[6:]:
        c, _, _ = red(item(cid), lat, lon, half)
        keep &= c >= 0.5
    lab2, n2 = ndimage.label(keep, structure=np.ones((3, 3)))
    s2z = ndimage.sum(keep, lab2, range(1, n2 + 1))
    order = np.argsort(s2z)[::-1]
    print(f"after seasonal filter: {keep.sum()*1e-4:.2f} km2 in {n2} components")
    for o in order[:3]:
        m = lab2 == o + 1
        r2, c2 = np.where(m)
        x2, y2 = tr * (c2.mean(), r2.mean())
        lo2, la2 = wt(crs, "EPSG:4326", [x2], [y2])
        print(f"  component {s2z[o]*1e-4:.2f} km2  centroid {la2[0]:.4f}, {lo2[0]:.4f}  extent {(r2.max()-r2.min())*0.01:.1f} km N-S x {(c2.max()-c2.min())*0.01:.1f} km E-W  "
              f"red pre {pre[m].mean():.2f} post {post[m].mean():.2f}")

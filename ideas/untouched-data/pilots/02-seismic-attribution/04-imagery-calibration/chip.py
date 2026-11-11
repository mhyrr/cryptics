"""Before/after Sentinel-2 true-colour chips around a point, for visual review.

usage: uv run python chip.py NAME LAT LON PRE_START PRE_END POST_START POST_END [HALF_KM]
Picks the least-cloudy L2A scene in each window (tile that covers the point), reads a
(2*HALF_KM)^2 km window of the 'visual' asset and writes chips/NAME.png (pre | post).
A viewing aid only: nothing here is a measurement.
"""
import sys
from datetime import datetime, timezone

import numpy as np
import rasterio
from PIL import Image, ImageDraw
from rasterio.warp import transform as warp_transform
from rasterio.windows import from_bounds

import s2


def d(s):
    return datetime.strptime(s, "%Y-%m-%d").replace(tzinfo=timezone.utc)


def chip(it, lat, lon, half_km, px=900):
    with rasterio.Env(**s2.ENV):
        with rasterio.open(it["assets"]["visual"]["href"]) as src:
            x, y = warp_transform("EPSG:4326", src.crs, [lon], [lat])
            h = half_km * 1000
            w = from_bounds(x[0] - h, y[0] - h, x[0] + h, y[0] + h, src.transform)
            a = src.read(window=w, out_shape=(3, px, px), boundless=True, fill_value=0)
    return np.transpose(a, (1, 2, 0))


def main():
    name, lat, lon = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
    wins = [(d(sys.argv[4]), d(sys.argv[5])), (d(sys.argv[6]), d(sys.argv[7]))]
    half = float(sys.argv[8]) if len(sys.argv) > 8 else 12.0
    panels, labels = [], []
    for t0, t1 in wins:
        items = sorted(s2.search(lon, lat, t0, t1, max_cloud=70), key=lambda it: it["properties"]["eo:cloud_cover"])
        best = None
        for it in items[:10]:
            a = chip(it, lat, lon, half)
            frac = float((a.sum(axis=2) > 0).mean())
            bright = float((a.min(axis=2) > 235).mean())
            if frac > 0.6 and (best is None or bright < best[2]):
                best = (it, a, bright)
        if best is None:
            print("no usable scene", t0, t1); sys.exit(1)
        panels.append(best[1]); labels.append(f"{best[0]['id']}  cloud {best[0]['properties']['eo:cloud_cover']:.0f}%")
        print(labels[-1])
    img = Image.fromarray(np.concatenate([panels[0], np.zeros((panels[0].shape[0], 8, 3), "uint8"), panels[1]], axis=1))
    dr = ImageDraw.Draw(img)
    n = panels[0].shape[0]
    for k, lab in enumerate(labels):
        ox = k * (n + 8)
        dr.text((ox + 6, 6), lab, fill=(255, 255, 0))
        c = n // 2
        dr.line((ox + c - 14, c, ox + c - 5, c), fill=(255, 255, 0)); dr.line((ox + c + 5, c, ox + c + 14, c), fill=(255, 255, 0))
        dr.line((ox + c, c - 14, ox + c, c - 5), fill=(255, 255, 0)); dr.line((ox + c, c + 5, ox + c, c + 14), fill=(255, 255, 0))
    img.save(f"chips/{name}.png")
    print(f"chips/{name}.png  {2*half:.0f} km square; cross = input point")


if __name__ == "__main__":
    main()

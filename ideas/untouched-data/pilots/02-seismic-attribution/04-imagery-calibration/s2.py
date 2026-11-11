"""Sentinel-2 L2A access and the frozen change detector (v1) for pilot 02.

Detector v1, fixed before any run on Poli's residual:
  scenes     up to 4 least-cloudy L2A scenes per window, scene cloud cover < 70 %
  windows    pre = [t-60 d, t-1 d], post = [t+1 d, t+60 d]
  grid       80 m (overview 8 of the 10 m bands; SCL resampled to match)
  valid      SCL in {4 vegetation, 5 bare, 7 unclassified, 11 snow/ice}
  composite  per-pixel median of valid red and NIR reflectance
  veg flag   pre NDVI >= 0.5 and post NDVI <= pre NDVI - 0.25
  snow flag  pre red >= 0.5 and post red <= pre red - 0.25
  blobs      8-connected flagged pixels, area >= 6 px (0.04 km2); score = area_px * mean drop
"""
import json, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta

import numpy as np
import rasterio
from rasterio.enums import Resampling
from rasterio.warp import transform as warp_transform
from scipy import ndimage

STAC = "https://earth-search.aws.element84.com/v1/search"
N = 1372  # 10980 / 8
VALID = (4, 5, 7, 11)
ENV = dict(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR", AWS_NO_SIGN_REQUEST="YES", GDAL_HTTP_MAX_RETRY="4", GDAL_HTTP_RETRY_DELAY="2")


def search(lon, lat, t0, t1, max_cloud=70):
    q = {"collections": ["sentinel-2-l2a"], "intersects": {"type": "Point", "coordinates": [lon, lat]},
         "datetime": f"{t0:%Y-%m-%dT%H:%M:%SZ}/{t1:%Y-%m-%dT%H:%M:%SZ}", "limit": 200,
         "query": {"eo:cloud_cover": {"lt": max_cloud}}}
    req = urllib.request.Request(STAC, data=json.dumps(q).encode(), headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=90))["features"]


def tile_of(item):
    p = item["properties"]
    return f"{p['mgrs:utm_zone']}{p['mgrs:latitude_band']}{p['mgrs:grid_square']}"


def pick(items, k=4):
    """Least-cloudy k scenes of the most frequent tile among the items."""
    if not items:
        return None, []
    tiles = {}
    for it in items:
        tiles.setdefault(tile_of(it), []).append(it)
    tile = max(tiles, key=lambda t: len(tiles[t]))
    return tile, sorted(tiles[tile], key=lambda it: it["properties"]["eo:cloud_cover"])[:k]


def _read(href, resampling):
    with rasterio.Env(**ENV):
        with rasterio.open(href) as src:
            a = src.read(1, out_shape=(N, N), resampling=resampling)
            return a, src.transform * src.transform.scale(src.width / N, src.height / N), src.crs


def load_scene(it):
    off = 0.0 if it["properties"].get("earthsearch:boa_offset_applied", False) or \
        float(it["properties"].get("s2:processing_baseline", "0") or 0) < 4 else -0.1
    red, tr, crs = _read(it["assets"]["red"]["href"], Resampling.average)
    nir, _, _ = _read(it["assets"]["nir"]["href"], Resampling.average)
    scl, _, _ = _read(it["assets"]["scl"]["href"], Resampling.nearest)
    ok = np.isin(scl, VALID) & (red > 0)
    r = np.where(ok, red / 10000.0 + off, np.nan).astype("float32")
    n = np.where(ok, nir / 10000.0 + off, np.nan).astype("float32")
    return r, n, tr, crs


def composite(items, pool=None):
    if not items:
        return None
    ex = pool or ThreadPoolExecutor(4)
    sc = list(ex.map(load_scene, items))
    with np.errstate(all="ignore"):
        red = np.nanmedian(np.stack([s[0] for s in sc]), axis=0)
        nir = np.nanmedian(np.stack([s[1] for s in sc]), axis=0)
    return dict(red=red, nir=nir, transform=sc[0][2], crs=sc[0][3], ids=[it["id"] for it in items])


def windows(t):
    return (t - timedelta(days=60), t - timedelta(days=1)), (t + timedelta(days=1), t + timedelta(days=60))


def detect(pre, post):
    with np.errstate(all="ignore"):
        nd0 = (pre["nir"] - pre["red"]) / (pre["nir"] + pre["red"])
        nd1 = (post["nir"] - post["red"]) / (post["nir"] + post["red"])
        veg = (nd0 >= 0.5) & (nd1 <= nd0 - 0.25)
        snow = (pre["red"] >= 0.5) & (post["red"] <= pre["red"] - 0.25)
        drop = np.where(veg, nd0 - nd1, 0) + np.where(snow, pre["red"] - post["red"], 0)
    flag = veg | snow
    lab, n = ndimage.label(flag, structure=np.ones((3, 3)))
    if n == 0:
        return []
    idx = np.arange(1, n + 1)
    area = ndimage.sum(flag, lab, idx)
    mean = ndimage.mean(np.nan_to_num(drop), lab, idx)
    com = ndimage.center_of_mass(flag, lab, idx)
    vfrac = ndimage.mean(veg, lab, idx)
    blobs = []
    for a, m, (r, c), vf in zip(area, mean, com, vfrac):
        if a >= 6:
            x, y = pre["transform"] * (c + 0.5, r + 0.5)
            lon, lat = warp_transform(pre["crs"], "EPSG:4326", [x], [y])
            blobs.append(dict(area_px=int(a), score=float(a * m), lat=lat[0], lon=lon[0], kind="veg" if vf >= 0.5 else "snow"))
    return sorted(blobs, key=lambda b: -b["score"])


def valid_fraction(pre, post):
    return float(np.mean(np.isfinite(pre["red"]) & np.isfinite(post["red"])))

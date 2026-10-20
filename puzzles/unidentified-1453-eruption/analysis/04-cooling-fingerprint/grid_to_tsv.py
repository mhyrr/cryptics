"""Flatten the N-TREND 2017 grid (t_filtered) into a site table and a value table.

Usage: uv run python -I grid_to_tsv.py data/ntrend2017grid.nc out/
Writes out/grid_sites.tsv (code, lat, lon) and out/grid_values.tsv (Year, codes...).
Missing values (-9999, NaN, or RE <= 0 already masked by the authors) are left blank.
"""
import os
import sys

import h5py
import numpy as np


def main(nc_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    f = h5py.File(nc_path, "r")
    lats = f["latitude"][:]
    lons = f["longitude"][:]
    years = f["time"][:].astype(int)
    t = f["t_filtered"][:]  # (lon, lat, time)
    t = np.where((t <= -9998) | ~np.isfinite(t), np.nan, t)
    cells = []
    for i, lo in enumerate(lons):
        for j, la in enumerate(lats):
            if np.isfinite(t[i, j, :]).sum() > 0:
                cells.append((f"g{la:+.1f}_{lo:+.1f}", la, lo, i, j))
    with open(os.path.join(out_dir, "grid_sites.tsv"), "w") as fh:
        fh.write("code\tlat\tlon\n")
        for c, la, lo, _, _ in cells:
            fh.write(f"{c}\t{la}\t{lo}\n")
    with open(os.path.join(out_dir, "grid_values.tsv"), "w") as fh:
        fh.write("Year\t" + "\t".join(c[0] for c in cells) + "\n")
        for k, y in enumerate(years):
            row = []
            for _, _, _, i, j in cells:
                v = t[i, j, k]
                row.append("" if not np.isfinite(v) else f"{v:.4f}")
            fh.write(f"{y}\t" + "\t".join(row) + "\n")
    print(f"{len(cells)} cells with data; years {years[0]}-{years[-1]}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

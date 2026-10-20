"""Addendum to 09: annual TUNU2013 insoluble particles (4.5-9.5 um), Abbott 2021 Table S7.

Post hoc (added 2026-10-20 after 09 closed). Ranks each year's particle mass
among 1450-1500 and reports the 1453 value against the one Icelandic
calibration event in range (Veidivotn 1477, tephra found by Abbott 2021).
Usage: python3 -I particles_s7.py <sheet7.tsv>
"""
import statistics
import sys

rows = []
for line in open(sys.argv[1], encoding="utf-8"):
    parts = line.rstrip("\n").split("\t")
    try:
        year, depth, nss, part = (float(x) for x in parts[1:5])
    except (ValueError, IndexError):
        continue
    rows.append((round(year), depth, nss, part))

rows.sort()
parts = [r[3] for r in rows]
med = statistics.median(parts)
mad = statistics.median(abs(p - med) for p in parts)
ranked = sorted(rows, key=lambda r: -r[3])
rank = {r[0]: i + 1 for i, r in enumerate(ranked)}

print(f"TUNU2013 annual insoluble particles 4.5-9.5 um, {rows[0][0]}-{rows[-1][0]}, n={len(rows)}")
print(f"median {med:.4f} ug/g, MAD {mad:.4f}")
print("year  depth_m  nssS_ng/g  particles_ug/g  x_median  robust_z  rank_of_n")
for y in (1452, 1453, 1454, 1458, 1459, 1477, 1479):
    r = next(r for r in rows if r[0] == y)
    z = (r[3] - med) / (1.4826 * mad)
    print(f"{y}  {r[1]:7.3f}  {r[2]:9.1f}  {r[3]:14.4f}  {r[3]/med:8.2f}  {z:8.2f}  {rank[y]:>3}/{len(rows)}")
print("top 5 particle years:", ", ".join(f"{r[0]} ({r[3]:.4f})" for r in ranked[:5]))

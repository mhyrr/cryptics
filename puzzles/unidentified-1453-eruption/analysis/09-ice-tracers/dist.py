"""Great-circle distance ranges from NEEM and TUNU2013 to the calibration vents.

usage: python3 -I -B dist.py > results/dist.txt
Vent coordinates are the approximate ones in tracers.py (descriptive only).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tracers as T  # noqa: E402

for site, c in (("NEEM-2011-S1", T.NEEM), ("TUNU2013", (78.035, -33.88))):
    for cls in ("ICE", "NHX", "TROP"):
        d = [T.gc_km(c, (la, lo)) for _, _, k, la, lo in T.CAL if k == cls]
        print("%-13s %-4s %5.0f-%5.0f km" % (site, cls, min(d), max(d)))

"""Print header lines and column layout of a NOAA text file, plus per-century
sample counts by a named year column. Prints NO data values (pre-registration guard).

Usage: python3 -I inspect.py FILE YEARCOL [maxheader]
"""
import sys
from collections import Counter

path, ycol = sys.argv[1], sys.argv[2]
maxh = int(sys.argv[3]) if len(sys.argv) > 3 else 60
txt = open(path, encoding="latin-1").read().replace("\r\n", "\n").replace("\r", "\n")
lines = txt.split("\n")
hdr = [l for l in lines if l.startswith("#")]
for l in hdr[:maxh]:
    if l.strip("# ").strip():
        print(l[:220])
rows = [l.split("\t") for l in lines if l and not l.startswith("#")]
head = None
for i, r in enumerate(rows):
    if ycol in [c.strip() for c in r]:
        head = [c.strip() for c in r]; start = i + 1; break
if head is None:
    print("NO HEADER with", ycol); sys.exit()
print("COLUMNS:", head)
j = head.index(ycol)
yrs = []
for r in rows[start:]:
    try:
        yrs.append(float(r[j]))
    except (ValueError, IndexError):
        pass
print("N rows", len(yrs), "year range", min(yrs), max(yrs))
c = Counter(int(y // 100) * 100 for y in yrs)
for k in sorted(c):
    print(f"  {k}s: {c[k]} samples ({c[k]/100:.1f}/yr)")

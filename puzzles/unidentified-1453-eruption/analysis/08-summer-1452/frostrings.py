"""Rank years in the Brunstein (1995) Colorado bristlecone frost-ring table by the Almagre Mountain (AM)
share of sampled trees with the event, and print the 1440-1470 rows. Standard library only.

Usage: python3 -I frostrings.py data/colofrlr.txt
Only rows whose first triple sits in the AM column (character offset < 20) are scored for AM.
Year suffix: none = latewood frost ring, L = light ring, E = earlywood frost ring (per the file header).
"""
import re
import sys

ROW = re.compile(r"^(\s*)(\d{1,4})([LE]?)\s+(.*)$")
TRIPLE = re.compile(r"(\d+)-(\d+)\s*-\s*(\d+)")


def parse(path):
    rows, era = [], "BC"
    for line in open(path, encoding="latin-1"):
        if line.strip().startswith("A.D."):
            era = "AD"
        m = ROW.match(line.rstrip("\n"))
        if not m or line.strip().startswith(("Year", "FIRST")):
            continue
        year = int(m.group(2)) * (1 if era == "AD" else -1)
        kind = {"": "latewood frost", "L": "light ring", "E": "earlywood frost"}[m.group(3)]
        rest = line.rstrip("\n")
        am = None
        t = TRIPLE.search(rest, len(m.group(1)) + len(m.group(2)) + len(m.group(3)))
        if t and t.start() < 20:
            am = (int(t.group(1)), int(t.group(2)), int(t.group(3)))
        others = re.findall(r"\b([BGSWXY](?:-[BGSWXY])*)\s*$", rest)
        rows.append((year, kind, am, others[0] if others else "", rest.strip()))
    return rows


def main(path):
    rows = parse(path)
    print(f"# rows parsed: {len(rows)}")
    print("## rows 1440-1470 (as in file)")
    for y, k, am, o, raw in rows:
        if 1440 <= y <= 1470:
            print(f"{y}\t{k}\t{raw}")
    print("\n## years 1250-1993 ranked by AM share of trees (latewood frost rings only, AM n >= 10)")
    lw = [(am[2], y, am, o) for y, k, am, o, _ in rows
          if k == "latewood frost" and am and am[0] >= 10 and 1250 <= y]
    lw.sort(reverse=True)
    for i, (p, y, am, o) in enumerate(lw[:12], 1):
        print(f"{i}\t{y}\tAM {am[1]}/{am[0]} = {p}%\tother sites: {o or '-'}")
    print(f"latewood frost-ring years at AM 1250-1993 (n>=10): {len(lw)}")
    print("\n## 1452 present in table: " + str(any(y == 1452 for y, *_ in rows)) +
          "   1454 present: " + str(any(y == 1454 for y, *_ in rows)))


if __name__ == "__main__":
    main(sys.argv[1])

"""Filter Bourdeau's open catalogue to desk-workable items of 1550-1620.

Usage: python3 gaps.py <catalogue.json> > gaps.tsv
Input: https://raw.githubusercontent.com/dbourdeau/cyphersolver/main/catalogue.json
Classes are Bourdeau's: A sibling deciphered, B partial key in print, C no key.
Scores (importance, solvability, difficulty) are his, 1-5, unvalidated.
"""
import json, sys

FIELDS = ["id", "year", "cls", "importance", "solvability", "difficulty",
          "region", "language", "reserved", "title", "shelfmark"]

def main(path):
    entries = json.load(open(path))["entries"]
    rows = []
    for e in entries:
        try:
            year = int(e["year"])
        except (TypeError, ValueError):
            continue
        desk = e.get("access") == "online" or e.get("needs_archive_scan") == "no"
        if 1550 <= year <= 1620 and desk:
            rows.append(e)
    rows.sort(key=lambda e: (e["cls"], -e["solvability"], e["difficulty"], e["id"]))
    print("\t".join(FIELDS))
    for e in rows:
        vals = [("yes" if e.get("reserved") else "no") if f == "reserved"
                else str(e.get(f, "")).replace("\t", " ").replace("\n", " ") for f in FIELDS]
        print("\t".join(vals))
    by = {}
    for e in rows:
        by[e["cls"]] = by.get(e["cls"], 0) + 1
    print(f"# {len(rows)} rows of {len(entries)} open entries; by class {dict(sorted(by.items()))}",
          file=sys.stderr)

if __name__ == "__main__":
    main(sys.argv[1])

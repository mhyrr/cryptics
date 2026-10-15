"""Pick the pilot batch from candidates.tsv: every edge case, plus bound < 10^5 with a PARI/Python program.
Usage: python3 -I prioritize.py candidates.tsv > batch.tsv"""
import csv, sys
rows = list(csv.DictReader(open(sys.argv[1]), delimiter="\t"))
pick = [r for r in rows if r["edge"] == "Y" or (int(r["bound"]) < 10**5 and any(p in r["programs"] for p in ("PARI", "Python")))]
seen, out = set(), []
for r in pick:
    if r["anum"] in seen: continue
    seen.add(r["anum"]); out.append(r)
w = csv.DictWriter(sys.stdout, fieldnames=["id"] + list(rows[0].keys()), delimiter="\t", lineterminator="\n")
w.writeheader()
for i, r in enumerate(out, 1):
    w.writerow({"id": i, **r})
print(f"# {len(out)} entries picked from {len(rows)} lines", file=sys.stderr)

"""Tally results/batch-*.tsv. Usage: python3 -I tally.py results"""
import csv, collections, sys
from pathlib import Path
rows = [r for f in sorted(Path(sys.argv[1]).glob("batch-*.tsv")) for r in csv.DictReader(open(f), delimiter="\t")]
print(f"rows: {len(rows)}  unique entries: {len({r['anum'] for r in rows})}")
print("triage:", dict(collections.Counter(r["triage"] for r in rows)))
res = collections.Counter(("COUNTEREXAMPLE" if r["result"].startswith("COUNTER") else r["result"]) for r in rows if r["triage"] == "checkable")
print("checkable results:", dict(res))
print("checkers disagree:", [r["anum"] for r in rows if r.get("agree") == "N"])
def num(x):
    try: return float(x)
    except (TypeError, ValueError): return None
gain = [num(r["new_bound"]) / num(r["old_bound"]) for r in rows if r["result"] == "holds" and num(r["new_bound"]) and num(r["old_bound"])]
gain.sort()
if gain: print(f"holds with numeric bounds: {len(gain)}; extension factor median {gain[len(gain)//2]:.1f}x, >=10x: {sum(g >= 10 for g in gain)}")
for r in rows:
    if r["result"].startswith("COUNTER"): print("COUNTEREXAMPLE", r["anum"], r["result"])

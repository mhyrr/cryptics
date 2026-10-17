"""A3, like for like. scan.py compares each plant's calibrated p (1,000 shuffles, floor 1/1001) with the
target's p from 10,000 shuffles (floor 1/10001). When the target sits below 1/1001, no plant can reach it,
so the 'reach' column there is empty by construction. This script reads the per-plant rows and compares them
with the target's p under the plant procedure (1,000 shuffles from the same bank), parsed from result-scan.txt.

Usage (from this folder, after scan.py): python3 -I a3_summary.py > a3-summary.txt
"""
import json, os, re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
txt = open(os.path.join(HERE, "result-scan.txt")).read()
tgt = {m[0]: (float(m[1]), float(m[2])) for m in
       re.findall(r"\n(T[12]): target calibrated p.*?plant procedure \(1,000\): A1 ([\d.]+), A2 ([\d.]+)", txt)}
rows = [json.loads(l) for l in open(os.path.join(HERE, "out", "a3_plants.jsonl"))]
cells = defaultdict(list)
for r in rows:
    cells[(r["tel"], f"{r['system']} {r['conv']} {r['letter']}")].append(r)
    cells[(r["tel"], "all cells pooled")].append(r)
floor = 1 / 1001 + 1e-12
print("# A3 like for like: plant calibrated p vs target calibrated p, both from 1,000 shuffles")
for tel in ("T1", "T2"):
    a1, a2 = tgt[tel]
    print(f"\n{tel}: target (plant procedure) A1 {a1:.4f}, A2 {a2:.4f}; floor = 1/1001 = {1 / 1001:.4f}")
    print(f"  {'cell':20} {'N':>5} {'A1 <= tgt':>10} {'A2 <= tgt':>10} {'A2 at floor':>12} {'both':>6}")
    for (t, name), rs in sorted(cells.items(), key=lambda kv: (kv[0][1] == "all cells pooled", kv[0][1])):
        if t != tel:
            continue
        n1 = sum(r["A1"] <= a1 + 1e-12 for r in rs)
        n2 = sum(r["A2"] <= a2 + 1e-12 for r in rs)
        nf = sum(r["A2"] <= floor for r in rs)
        nb = sum(r["A1"] <= a1 + 1e-12 and r["A2"] <= a2 + 1e-12 for r in rs)
        N = len(rs)
        print(f"  {name:20} {N:>5} {n1:>4} {n1 / N:.3f} {n2:>4} {n2 / N:.3f} {nf:>6} {nf / N:.3f} {nb:>6}")

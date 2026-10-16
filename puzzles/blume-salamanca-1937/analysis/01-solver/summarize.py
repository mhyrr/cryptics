"""Per-band recovery rates and score distributions from control logs.
Usage: python3 summarize.py out/bandA.jsonl [...]  -> markdown table on stdout
Bands are labelled by max(w1, w2)."""
import json, sys
from collections import defaultdict
rows = [json.loads(l) for f in sys.argv[1:] for l in open(f)]
print("| n (+n2) | secs | w1 × w2 | trials | full recoveries (acc ≥ 0.95) | rate | solver score, recovered | solver score, failed | true-plaintext score |")
print("|---|---|---|---|---|---|---|---|---|")
def rng(v): return f"{min(v):.3f} to {max(v):.3f}" if v else "—"
bands = defaultdict(list)
for r in rows:
    m = max(r["w1"], r["w2"])
    band = "12–13" if m <= 13 else "14–15" if m <= 15 else "16–17" if m <= 17 else "18–20" if m <= 20 else "21–25"
    bands[(r["n"], r.get("n2", 0), r["secs"], band)].append(r)
for (n, n2, secs, band), rs in sorted(bands.items()):
    ok = [r for r in rs if r["acc"] >= 0.95]; bad = [r for r in rs if r["acc"] < 0.95]
    print(f"| {n}{'+'+str(n2) if n2 else ''} | {secs} | ≤ {band} | {len(rs)} | {len(ok)} | {len(ok)/len(rs):.0%} | "
          f"{rng([r['score'] for r in ok])} | {rng([r['score'] for r in bad])} | {rng([r['true_score'] for r in rs])} |")
fails = [r["score"] for r in rows if r["acc"] < 0.95]; oks = [r["score"] for r in rows if r["acc"] >= 0.95]
if fails and oks:
    print(f"\nHighest failed-run score {max(fails):.3f}; lowest recovered-run score {min(oks):.3f}.")

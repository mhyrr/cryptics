"""Summarise a target run against the frozen threshold (-5.10). Usage: python3 summarize_target.py out/TAG.jsonl"""
import json, sys
THRESH = -5.10
r = [json.loads(l) for l in open(sys.argv[1])]
r.sort(key=lambda x: -x["score"])
cand = [x for x in r if x["score"] > THRESH]
s = [x["score"] for x in r]
print(f"runs {len(r)}; best {max(s):.3f}; median {sorted(s)[len(s)//2]:.3f}; worst {min(s):.3f}; candidates above {THRESH}: {len(cand)}")
for x in r[:5]:
    print(f"  {x['w1']}x{x['w2']} {x['conv']} {x['score']:.3f} {x['pt'][:70]}")

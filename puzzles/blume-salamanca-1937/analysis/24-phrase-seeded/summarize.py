"""Recompute the holdout/target report from checked-in JSONL. No search.

python3 -I summarize.py > results/summary.md
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read(tag):
    path=HERE / "results" / f"{tag}.jsonl"
    return [json.loads(l) for l in path.read_text().splitlines()] if path.exists() else []


def main():
    print("# Phrase-seeded results\n")
    rr=read("holdout24")
    print("## Holdout controls\n")
    print("615 letters; first width 12–22, second length 18–28; 5,284 contextual second-key seeds.")
    print("Recovery criterion: >=95% agreement allowing a cyclic shift <=40. Exact is separately counted.\n")
    print("| rank swaps from list key | trials | recovered | exact in-place | process CPU seconds |")
    print("|---|---|---|---|---|")
    for d in range(3):
        ss=[r for r in rr if r["distance"]==d]
        print(f"| {d} | {len(ss)} | {sum(r['recovered'] for r in ss)} | "
              f"{sum(r['exact'] for r in ss)} | {sum(r['cpu'] for r in ss):.3f} |")
    print("\nThese are synthetic literary-proxy controls. They do not identify the historical system or key.")
    print("\n## Full T1 and own-letter shuffle\n")
    print("| body | best quadgram score | candidate above -5.10 | process CPU seconds | seeds refined |")
    print("|---|---|---|---|---|")
    for r in read("target24"):
        print(f"| {r['body']} | {r['best']['score']:.4f} | {r['candidate']} | {r['cpu']:.3f} | {r['seeds_tried']} |")
    print("\nAll returned texts/keys and control accuracies are retained in the JSONL files.")
    print("A single shuffle is a false-positive check, not a p-value estimate.")


if __name__=="__main__":
    main()

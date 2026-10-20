"""Recompute compact results from recorded JSONL; no search.

python3 -I summarize.py > results/summary.md
"""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent


def rows(tag):
    p=HERE / "results" / f"{tag}.jsonl"
    return [json.loads(x) for x in p.read_text().splitlines()] if p.exists() else []


def main():
    print("# Direct-neighbour results\n")
    dev=json.loads((HERE / "results/development.json").read_text())
    print("## Assisted development diagnostic\n")
    print("| old stratum/trial | base-key rank at true width | assisted exact recovery |")
    print("|---|---|---|")
    for r in dev: print(f"| {r['distance']}/{r['trial']} | {r['rank_at_true_width']} | {r['assisted_exact']} |")
    print("\nBoth the true first width and base phrase were supplied. These are not blind controls.")
    print("\n## Development benchmark\n")
    print("| supplied first width | score | CPU seconds | role |")
    print("|---|---|---|---|")
    for r in json.loads((HERE / "results/benchmark.json").read_text()):
        role="exact old-plant recovery" if r["first_width_hypothesis"]==22 else "cost check"
        print(f"| {r['first_width_hypothesis']} | {r['best']['score']:.4f} | {r['cpu']:.3f} | {role} |")
    print("\nThese development rows are excluded from the fresh gate.")
    print("\n## Fresh per-width controls\n")
    print("The first width is supplied. Keys/plaintext are not supplied. Minimum distances are from the original list.")
    print("\n| stratum | trials | recovered (>=95%, shift<=40) | exact | false candidates | scan CPU seconds | total CPU seconds |")
    print("|---|---|---|---|---|---|---|")
    cr=rows("holdout25")
    for s in ("exact","one","two","random"):
        rr=[r for r in cr if r["stratum"]==s]
        print(f"| {s} | {len(rr)} | {sum(r['recovered'] for r in rr)} | {sum(r['exact'] for r in rr)} | "
              f"{sum(r['candidate'] and not r['recovered'] for r in rr)} | {sum(r['scan']['cpu'] for r in rr):.3f} | "
              f"{sum(r['cpu'] for r in rr):.3f} |")
    expected={(s,i) for s in ("exact","one","two","random") for i in range(10)}
    complete=len(cr)==40 and {(r["stratum"],r["trial"]) for r in cr}==expected
    passed=None
    if not complete: print(f"\nINCOMPLETE: {len(cr)}/40 controls; no target gate can pass.")
    else:
        passed=all(sum(r["recovered"] for r in cr if r["stratum"]==s)>=8 for s in ("exact","one"))
        passed=passed and not any(r["candidate"] and not r["recovered"] for r in cr)
        print(f"\nControl gate: {'PASS' if passed else 'FAIL'} (>=8/10 exact and one, zero false candidates across all 40).")
    print("\nThese controls use literary-proxy plaintext. Near-list success does not establish arbitrary-key coverage.")
    diagnostic=HERE / "results/gate-diagnostic.json"
    if diagnostic.exists():
        print("\n## Post-search acceptance diagnostic\n")
        print("| control | score | true-text score | shifted agreement | exact K2 | exact K1 |")
        print("|---|---|---|---|---|---|")
        for r in json.loads(diagnostic.read_text())["false_candidates"]:
            print(f"| {r['stratum']}/{r['trial']} | {r['score']:.4f} | {r['true_plaintext_score']:.4f} | "
                  f"{r['acc']:.4f} | {r['second_key_exact']} | {r['first_key_exact']} |")
        print("\nThis explains a failed control. It is not a fresh test or a target result. No settings changed.")
    print("\n## Exploratory T1 grid and matched shuffle\n")
    print("| body | widths complete | best quadgram score | candidates | scan CPU seconds | total CPU seconds |")
    print("|---|---|---|---|---|---|")
    tr=rows("target25")
    for body in ("T1","T1-shuffle"):
        rr=[r for r in tr if r["body"]==body]
        if rr:
            print(f"| {body} | {len(rr)}/11 | {max(r['best']['score'] for r in rr):.4f} | "
                  f"{sum(r['candidate'] for r in rr)} | {sum(r['scan']['cpu'] for r in rr):.3f} | "
                  f"{sum(r['cpu'] for r in rr):.3f} |")
    if not tr and passed is False:
        print("\nNOT RUN: the complete control gate failed. No target protocol was frozen.")
    elif len(tr)!=22: print(f"\nINCOMPLETE: {len(tr)}/22 target width/body cells.")
    print(f"\nRecorded fresh-control CPU seconds: {sum(r['cpu'] for r in cr):.3f}; "
          f"target/shuffle CPU seconds: {sum(r['cpu'] for r in tr):.3f}.")
    print("\nOne shuffle is not a p-value. All target widths must complete. A candidate still needs independent T2 validation.")


if __name__=="__main__": main()

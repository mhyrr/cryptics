"""Summarize recorded experiment26 results without invoking a search.

python3 -I summarize.py > results/summary.md
"""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent


def rows(tag):
    p=HERE / "results" / f"{tag}.jsonl"
    return [json.loads(s) for s in p.read_text().splitlines()] if p.exists() else []


def gate(rr,isolated):
    strata=("low","middle","high","wrong-width","shuffle") if isolated else ("exact","one","two","random")
    expected={(s,i) for s in strata for i in range(10)}
    if len(rr)!=len(expected) or {(r["stratum"],r["trial"]) for r in rr}!=expected: return "INCOMPLETE"
    required=strata[:3] if isolated else strata[:2]
    recovered=all(sum(r["recovered"] for r in rr if r["stratum"]==s)>=8 for s in required)
    false=any(r["candidate"] and (not r["recovered"] or (isolated and not r["positive"])) for r in rr)
    return "PASS" if recovered and not false else "FAIL"


def main():
    print("# Full-neighbourhood K1 results\n")
    dev=json.loads((HERE / "results/development.json").read_text())
    print(f"Assisted old-failure development: exact={dev['exact']}, score={dev['best']['score']:.4f}, "
          f"recorded CPU seconds={dev['cpu']:.1f}. True K2/width supplied; excluded from fresh gates.\n")
    iso,controls=rows("iso26"),rows("holdout26")
    for label,rr,isolated,strata in [
        ("Isolated K1",iso,True,("low","middle","high","wrong-width","shuffle")),
        ("Fresh end-to-end",controls,False,("exact","one","two","random"))]:
        print(f"## {label}\n")
        print("| stratum | records | recovered | exact | candidates | false candidates | recorded CPU seconds |")
        print("|---|---|---|---|---|---|---|")
        for s in strata:
            ss=[r for r in rr if r["stratum"]==s]
            false=sum(r["candidate"] and (not r["recovered"] or (isolated and not r["positive"])) for r in ss)
            print(f"| {s} | {len(ss)}/10 | {sum(r['recovered'] for r in ss)} | {sum(r['exact'] for r in ss)} | "
                  f"{sum(r['candidate'] for r in ss)} | {false} | {sum(r['cpu'] for r in ss):.3f} |")
        print(f"\nGate: **{gate(rr,isolated)}**.\n")
    print("Isolated positives receive true K2 and first width; negatives are wrong-width/shuffled. "
          "End-to-end controls receive first width only, with K1/K2/plaintext withheld. "
          "Recovery permits a cyclic shift <=40 and requires >=95% agreement.\n")
    print("## Target and matched shuffle\n")
    target=rows("target26")
    if not target:
        failed=gate(iso,True)=="FAIL" or gate(controls,False)=="FAIL"
        print("NOT RUN: a control gate failed.\n" if failed else "No target records yet; both complete gates and a frozen protocol are required.\n")
    else:
        print("| body | widths complete | best score | candidates | recorded CPU seconds |")
        print("|---|---|---|---|---|")
        for body in ("T1","T1-shuffle"):
            ss=[r for r in target if r["body"]==body]
            if ss:
                print(f"| {body} | {len(ss)}/11 | {max(r['best']['score'] for r in ss):.4f} | "
                      f"{sum(r['candidate'] for r in ss)} | {sum(r['cpu'] for r in ss):.3f} |")
        if len(target)!=22: print(f"\nINCOMPLETE target grid: {len(target)}/22 cells.")
    print(f"\nRecorded CPU seconds: isolated={sum(r['cpu'] for r in iso):.3f}; "
          f"end-to-end={sum(r['cpu'] for r in controls):.3f}; target/shuffle={sum(r['cpu'] for r in target):.3f}.")
    print("\nLiterary-proxy controls do not establish historical preparation. Per-width calibration is conditional. "
          "One shuffle is not a p-value. A score-qualified candidate still needs independent historical/T2 validation.")


if __name__=="__main__": main()

"""Summarize recorded27 JSONL; no search or plaintext scoring is performed."""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent


def rows(tag):
    p=HERE / "results" / (tag+".jsonl")
    return [json.loads(s) for s in p.read_text().splitlines()] if p.exists() else []


def main():
    control=rows("holdout27"); target=rows("target27")
    lines=["# Experiment27 recorded results", "", "| Stratum | Completed | Recovered | Exact | Candidates | CPU seconds |",
           "|---|---:|---:|---:|---:|---:|"]
    for s in ("exact","one","two","random"):
        rr=[r for r in control if r["stratum"]==s]
        lines.append(f"| {s} | {len(rr)}/10 | {sum(r['recovered'] for r in rr)} | {sum(r['exact'] for r in rr)} | "
                     f"{sum(r['candidate'] for r in rr)} | {sum(r['cpu'] for r in rr):.3f} |")
    false=[r for r in control if r["candidate"] and not r["recovered"]]
    complete=len(control)==40 and {(r['stratum'],r['trial']) for r in control}=={(s,i) for s in ('exact','one','two','random') for i in range(10)}
    passed=complete and not false and all(sum(r['recovered'] for r in control if r['stratum']==s)>=8 for s in ('exact','one'))
    status="PASS" if passed else "FAIL" if complete else "INCOMPLETE"
    lines.extend(["",f"Control gate: **{status}**. False candidates: {len(false)}. True first width supplied.","",
                  "| Target | Widths | Best score | Candidates | CPU seconds |", "|---|---:|---:|---:|---:|"])
    for body in ('T1','T1-shuffle'):
        rr=[r for r in target if r['body']==body]
        best=f"{max(r['best']['score'] for r in rr):.4f}" if rr else 'not run'
        lines.append(f"| {body} | {len(rr)}/7 | {best} | {sum(r['candidate'] for r in rr)} | {sum(r['cpu'] for r in rr):.3f} |")
    total=sum(r['cpu'] for r in control+target)
    lines.extend(["",f"Total recorded solver CPU seconds: {total:.3f} ({total/60:.3f} minutes).",
                  "Preparation, build, hashing and independent verification excluded. CPU time is summed over workers.",
                  "No target run is permitted if the complete control gate fails. One shuffle is not a p-value estimate.",
                  "Controls are modified literary Spanish, not authentic trade telegrams. A finite, fallible phrase search cannot exclude arbitrary keys."])
    (HERE / 'results/summary.md').write_text('\n'.join(lines)+'\n')
    print('\n'.join(lines))


if __name__=='__main__': main()

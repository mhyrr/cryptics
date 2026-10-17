"""Summaries of 21-dc-method runs (out/*.jsonl) as markdown tables, written to results/.

  python3 -I summ21.py probe TAG [TAG ...]   -> fitness-distance and basin table
  python3 -I summ21.py k2 TAG [TAG ...]      -> K2-stage hit rates, evaluations per hit
  python3 -I summ21.py solve TAG [TAG ...]   -> full-solve recoveries under 01's rule
Each call prints the table and appends it to results/<first TAG>.md (or results/summary-<kind>.md with out=NAME).

Hit-rate model for the K2 stage: restarts are independent, so evaluations-to-hit are roughly exponential;
lambda = hits / evaluations spent (censored runs count their whole budget). B80 = ln 5 / lambda is the budget at
which 80% of runs would hit. It is an extrapolation, labelled as such, never a pass.
"""
import json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load(tag):
    return [json.loads(l) for l in open(os.path.join(HERE, "out", f"{tag}.jsonl"))]


def probe_table(tags):
    rows = ["| tag | plants | true IDP | D1/Dr | D2/Dr | D3/Dr | D4/Dr | Dr ± sd | climb optima D (mean) | basin 1 | 2 | 3 | 4 | 5 | 6 |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for t in tags:
        R = load(t)
        def m(f):
            v = [f(r) for r in R]
            return sum(v) / len(v)
        dr = m(lambda r: r["random"][0])
        cell = lambda x: f"{m(lambda r: r['D'][str(x)][0] / r['random'][0]):.2f}" if all(str(x) in r["D"] for r in R) else "—"
        bas = []
        for x in (1, 2, 3, 4, 5, 6):
            if all(str(x) in r["basin"] for r in R):
                b = sum(r["basin"][str(x)][0] for r in R); n = sum(r["basin"][str(x)][1] for r in R)
                bas.append(f"{b}/{n}")
            else:
                bas.append("—")
        clim = m(lambda r: sum(c[0] for c in r["climbs"]) / max(1, len(r["climbs"])))
        rows.append(f"| {t} | {len(R)} | {m(lambda r: r['true']):.2f} | {cell(1)} | {cell(2)} | {cell(3)} | {cell(4)} | "
                    f"{dr:.2f} ± {m(lambda r: r['random'][1]):.2f} | {clim:.2f} | " + " | ".join(bas) + " |")
    return "\n".join(rows)


def k2_table(tags):
    rows = ["| tag | w1×w2 | runs | hits | hits exact K2 | evals spent (M) | lambda per M evals | B80 extrapolated (M evals) | median evals to hit (M) |",
            "|---|---|---|---|---|---|---|---|---|"]
    for t in tags:
        R = load(t)
        hits = [r for r in R if r["hit"]]
        spent = sum(r["n_idp"] for r in R) / 1e6
        lam = len(hits) / spent if spent else 0
        b80 = f"{math.log(5) / lam:.1f}" if lam else "∞ (no hit)"
        med = sorted(r["hit_at"] / 1e6 for r in hits)
        medv = f"{med[len(med) // 2]:.2f}" if med else "—"
        ws = sorted({f"{r['w1']}x{r['w2']}" for r in R})
        rows.append(f"| {t} | {','.join(ws) if len(ws) < 4 else ws[0] + '…' + ws[-1]} | {len(R)} | {len(hits)} | "
                    f"{sum(r['k2same'] == r['w2'] for r in hits)} | {spent:.1f} | {lam:.3f} | {b80} | {medv} |")
    return "\n".join(rows)


def solve_table(tags):
    rows = ["| tag | runs | full (≥ 95%, shift ≤ 40) | K2 hit | budget (M IDP evals) | cpu s (median) |", "|---|---|---|---|---|---|"]
    for t in tags:
        R = load(t)
        cpu = sorted(r["cpu"] for r in R)
        rows.append(f"| {t} | {len(R)} | {sum(r['full'] for r in R)} | {sum(r['hit'] for r in R)} | "
                    f"{max(r['n_idp'] for r in R) / 1e6:.1f} | {cpu[len(cpu) // 2]:.0f} |")
    return "\n".join(rows)


def main():
    kind, tags = sys.argv[1], [a for a in sys.argv[2:] if not a.startswith("out=")]
    name = next((a[4:] for a in sys.argv[2:] if a.startswith("out=")), None)
    tab = {"probe": probe_table, "k2": k2_table, "solve": solve_table}[kind](tags)
    print(tab)
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    with open(os.path.join(HERE, "results", f"{name or tags[0]}.md"), "a") as f:
        f.write(tab + "\n\n")


if __name__ == "__main__":
    main()

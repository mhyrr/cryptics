"""Tables and the mechanical application of the pre-registered readings, from out/<family>.jsonl.
Usage (from this folder): python3 -I summarize.py > result.txt
"""
import json, os, statistics
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
FAMS = [("single", "1. Single columnar, forward, incomplete last row (colsolve.py)"),
        ("double", "2. Double columnar CC (01-solver/out/dtsolve, 90 s per run)"),
        ("periodic", "3. Letters permuted within sets of n (05 periodic.solve)"),
        ("nihilist", "4. Nihilist read by rows (05 nihilist_control path, periodic.solve)"),
        ("grille", "5. 4 x 4 turning grille, 160 letters (06 exhaustive search)")]
ORDER = [(0, "none"), (5, "end"), (10, "end"), (15, "end"), (20, "end"), (5, "start"), (10, "start"), (15, "start")]


def frac(rs):
    return sum(r["ok"] for r in rs), len(rs)


def main():
    print("Recovery = plants whose body reads >= 90% in place (control.py shift_acc, |shift| <= 40), of plants.")
    print("Cells: k/N (uniform fill k/n; T1-tail fill k/n); median body accuracy in brackets.\n")
    for fam, title in FAMS:
        p = os.path.join(HERE, "out", f"{fam}.jsonl")
        if not os.path.exists(p):
            print(f"## {title}\n(not run)\n"); continue
        recs = [json.loads(l) for l in open(p)]
        bands = list(dict.fromkeys(r["band"] for r in recs))
        cell = defaultdict(list)
        for r in recs:
            cell[r["band"], r["t"], r["end"]].append(r)
        print(f"## {title}")
        print("| t, end | " + " | ".join(bands) + " |")
        print("|---|" + "---|" * len(bands))
        for t, end in ORDER:
            if not any(cell.get((b, t, end)) for b in bands):
                continue
            row = []
            for b in bands:
                rs = cell.get((b, t, end))
                if not rs:
                    row.append("not run"); continue
                k, n = frac(rs); med = statistics.median(r["acc"] for r in rs)
                if t == 0:
                    row.append(f"{k}/{n} [{med:.2f}]")
                else:
                    ku, nu = frac([r for r in rs if r["fill"] == "uniform"])
                    kt, nt = frac([r for r in rs if r["fill"] == "t1tail"])
                    row.append(f"{k}/{n} ({ku}/{nu}; {kt}/{nt}) [{med:.2f}]")
            label = "0 (baseline)" if t == 0 else f"{t}, {end}"
            print(f"| {label} | " + " | ".join(row) + " |")
        secs = [r["secs"] for r in recs]
        print(f"\nplants {len(recs)}, solver seconds per plant: median {statistics.median(secs):.1f}, "
              f"max {max(secs):.1f}, total {sum(secs):.0f}")
        t0 = [r for r in recs if r["t"] == 0 and not r["ok"]]
        if t0:
            below = sum(r["score"] < r["true_score"] - 0.005 for r in t0)
            print(f"t = 0 failures: {len(t0)}; in {below} of them the solver's best scores below the true text "
                  f"(a search failure, not a model failure)")
        print("\nPre-registered readings, applied mechanically per band and end:")
        for b in bands:
            k0, n0 = frac(cell[b, 0, "none"]); r0 = k0 / n0
            if r0 < 0.8:
                print(f"- {b}: not measured (t = 0 control {k0}/{n0}, below the 80% pass rule)"); continue
            for end in ("end", "start"):
                ts = [t for t, e in ORDER if e == end and cell.get((b, t, e))]
                if not ts:
                    continue
                ratio = {t: (frac(cell[b, t, end])[0] / frac(cell[b, t, end])[1]) / r0 for t in ts}
                desc = ", ".join(f"t {t}: {ratio[t]:.2f}" for t in ts)
                if all(v >= 0.8 for v in ratio.values()):
                    verdict = "tail-robust"
                elif any(v < 0.5 for v in ratio.values()):
                    verdict = "void for bodies with untransposed letters at this end"
                else:
                    verdict = "partly robust; re-enters for t = " + ", ".join(str(t) for t in ts if ratio[t] < 0.8)
                print(f"- {b}, {end}: ratio to t = 0 ({desc}) -> {verdict}")
        print()


if __name__ == "__main__":
    main()

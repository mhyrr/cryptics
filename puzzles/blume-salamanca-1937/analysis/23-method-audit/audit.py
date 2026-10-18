"""Summarize checked-in experiment 21/22 logs. No target search or new plants.

Run from any directory: python3 -I path/to/audit.py > path/to/result.txt
Standard library only. CPU time is process CPU time, not elapsed time.
"""
import json
import math
from pathlib import Path
from statistics import median

HERE = Path(__file__).resolve().parent
ANALYSIS = HERE.parent


def rows(relative):
    return [json.loads(line) for line in (ANALYSIS / relative).read_text().splitlines() if line.strip()]


def main():
    target21 = rows("21-dc-method/results/target21.jsonl")
    target22 = rows("22-dc-trimmed/results/target22.jsonl")
    controls21 = rows("21-dc-method/results/ctlA.jsonl") + rows("21-dc-method/results/ctlA2.jsonl")
    controls22 = rows("22-dc-trimmed/results/controls22.jsonl")
    expected_pairs = {(a, b) for a in range(2, 16) for b in (16, 17)}
    print("AUDIT 2026-10-18: existing logs only; candidate threshold -5.10")
    print("\nTarget searches (50 M IDP evaluations per pair):")
    print("body | pairs | CPU hours | best score | candidates")
    groups = [("T1 full", target21)]
    groups += [(body, [r for r in target22 if r["body"] == body]) for body in sorted({r["body"] for r in target22})]
    for label, rr in groups:
        assert len(rr) == 28 and {(r["w1"], r["w2"]) for r in rr} == expected_pairs
        assert all(r["n_idp"] >= 50_000_000 for r in rr)
        print(f"{label} | {len(rr)} | {sum(r['cpu'] for r in rr)/3600:.3f} | "
              f"{max(r['score'] for r in rr):.4f} | {sum(r['score'] > -5.10 for r in rr)}")
    tt = target21 + target22
    print(f"Total target CPU hours (21 + 22 only): {sum(r['cpu'] for r in tt)/3600:.3f}")
    hard = [r for r in tt if r["w1"] >= 12]
    print(f"w1 12-15, w2 16-17: CPU minutes per 50 M run "
          f"min/median/max = {min(r['cpu'] for r in hard)/60:.2f}/"
          f"{median(r['cpu'] for r in hard)/60:.2f}/{max(r['cpu'] for r in hard)/60:.2f}")

    print("\nControls (same budget, synthetic telegraph-style Spanish):")
    for label, rr in [("21 ctlA", controls21[:10]), ("21 ctlA2", controls21[10:])]:
        print(f"{label}: {sum(r['full'] for r in rr)}/{len(rr)} full recovery")
    for n in sorted({r["n"] for r in controls22}):
        rr = [r for r in controls22 if r["n"] == n]
        assert len(rr) == 10
        ok = [r for r in rr if r["full"]]
        print(f"22 N={n}: {len(ok)}/{len(rr)}; slowest first recovery = "
              f"{max(r['first_ok_nidp'] for r in ok)/1e6:.2f} M evaluations")
    print("\nExact two-sided 95% binomial lower limits for all-success samples:")
    for n in (10, 20):
        print(f"{n}/{n}: lower success probability = {0.025 ** (1/n):.4f}")
    print("These limits assume iid trials from the specified plant distribution.")
    print("They are not target probabilities, nor guarantees for each width or plaintext.")
    print("Pooling ctlA with its harder-corner ctlA2 does not make a uniform 20-trial band sample.")

    print("\nExhaustive second-key enumeration, one first width, no other uncertainties:")
    print("Illustrative speed: 1,000,000 complete key evaluations/s; NOT a measured rate.")
    for w in (17, 20, 23, 25):
        print(f"w2={w}: {math.factorial(w):,} keys; full enumeration at illustrative speed "
              f"{math.factorial(w)/1e6/(365.25*86400):,.1f} years")
    print("Heuristic IDP evaluations are not exhaustive coverage of this key space.")


if __name__ == "__main__":
    main()

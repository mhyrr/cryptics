"""Sensitivity: rerun g0, g1, g2, g3, g6a, g8 (Spanish) with held-out book 27738 (Jose, which ends in an
English-Spanish glossary; found by experiment 09) removed from the word stream. Same seeds as fit.py.
The exclusion is patched into plaintext's EXCLUDE inside this process only; 01-solver is not edited.
Usage (from this folder): python3 -I sensitivity_27738.py > sensitivity_27738.txt
"""
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import fit, conventions as cv, plaintext   # fit chdirs into 01-solver

GENS = ["g0", "g1", "g2", "g3", "g6a", "g8"]
SEEDS = [fit.SEED, fit.SEED + 1, fit.SEED + 2]


def run(tel):
    return {s: {g: fit.fit(cv.GENERATORS[g][0], "es", cv.GENERATORS[g][1], s, tel) for g in GENS} for s in SEEDS}


def main():
    tel = {"T1": fit.load("../../sources/telegram-1.txt"), "T2": fit.load("../../sources/telegram-2.txt")}
    before = run(tel)
    letters = lambda: sum(len(t) for t in plaintext.heldout_words("es") if t != ".")
    n0, l0 = len(plaintext.heldout_words("es")), letters()
    plaintext.EXCLUDE = set(plaintext.EXCLUDE) | {27738}
    plaintext._cache.clear()
    n1, l1 = len(plaintext.heldout_words("es")), letters()
    after = run(tel)
    print("# Sensitivity: book 27738 excluded from the Spanish held-out word stream\n")
    print(f"Spanish held-out tokens: {n0} with the book, {n1} without ({100 * (n0 - n1) / n0:.1f}% removed); "
          f"letters {l0} -> {l1} ({100 * (l0 - l1) / l0:.1f}% removed)\n")
    print(f"chi2 observed (plants median, plants 90th percentile), seed {SEEDS[0]}, with book -> without\n")
    print("| gen | T1 | T2 |\n|---|---|---|")
    for g in GENS:
        c = lambda r, k: f"{r[k]['chi']:.0f} ({r[k]['chi_med']:.0f}, {r[k]['chi_90']:.0f})" if k in r else "–"
        a, b = before[SEEDS[0]][g], after[SEEDS[0]][g]
        print(f"| {g} | {c(a, 'T1')} → {c(b, 'T1')} | {c(a, 'T2')} → {c(b, 'T2')} |")
    print()
    for s in SEEDS:
        print(f"## seed {s} (with book -> without)\n")
        print("| gen | T1 p | T1 z X | T1 z P | T1 z U | T2 p | T2 z F | T2 z X | T2 z P | T2 z U |")
        print("|---|---|---|---|---|---|---|---|---|---|")
        for g in GENS:
            row = []
            for name, zs in (("T1", "XPU"), ("T2", "FXPU")):
                a, b = before[s][g].get(name), after[s][g].get(name)
                if not a:
                    row += ["–"] * (1 + len(zs)); continue
                row.append(f"{a['p']:.3f} → {b['p']:.3f}")
                row += [f"{a['z'][x]:+.1f} → {b['z'][x]:+.1f}" for x in zs]
            print(f"| {g} | " + " | ".join(row) + " |")
        print("\nPass rule without the book (explains T1 X / T2 F): " +
              ", ".join(f"{g} {'/'.join(fit.verdicts(after[s][g]))}" for g in GENS) + "\n")


if __name__ == "__main__":
    main()

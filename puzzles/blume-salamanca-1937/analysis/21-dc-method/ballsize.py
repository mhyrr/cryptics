"""Share of all K2 keys within b swaps of the true key (Cayley distance <= b), for key lengths w.

The number of permutations of w elements at Cayley distance k from the identity is the unsigned Stirling
number of the first kind c(w, w - k) (permutations with w - k cycles). The probes in this folder show that a
climb returns to the true K2 only from within about b = 2-3 swaps; a search that has no gradient outside that
ball has to land in it, so its cost grows like 1 / (ball share). Exact integers, standard library only.
Usage: python3 -I ballsize.py > results/ballsize.md
"""
from math import factorial, log10


def stirling1_row(n):
    """c(n, k) for k = 0..n, unsigned Stirling numbers of the first kind."""
    row = [1]
    for m in range(1, n + 1):
        new = [0] * (m + 1)
        for k in range(1, m + 1):
            new[k] = row[k - 1] + (m - 1) * (row[k] if k < len(row) else 0)
        row = new
    return row


def main():
    print("| w | w! | log10 share within 2 swaps | within 3 | within 4 | within 6 |")
    print("|---|---|---|---|---|---|")
    for w in range(12, 25):
        c = stirling1_row(w)
        cells = []
        for b in (2, 3, 4, 6):
            ball = sum(c[w - k] for k in range(0, b + 1))
            cells.append(f"{log10(ball / factorial(w)):.1f}")
        print(f"| {w} | {factorial(w):.2e} | " + " | ".join(cells) + " |")


if __name__ == "__main__":
    main()

"""Nihilist transposition read by columns, in n x n squares, reduced to 18's problem.

Each full square of n*n letters (from offset p) is written in rows, its rows reordered (any order; the classic
system uses the column key), its columns permuted by k, and read out column by column. Output column j holds
plaintext column k[j], with the rows in the square's row order, the same for every column. So grid row (s, i) =
cipher letters s*n*n + j*n + i for j = 0..n-1 is one plaintext row with its columns permuted by k. Rearranging every
square this way gives a text that 18's setsolve.solve reads at offset 0, as the Nihilist rectangle read by rows.
Letters before p and after the last full square are not scored (their handling is unknown).
Self-test: python3 -I nihcols.py
"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "18-periodic-solver"))
import setsolve  # noqa: E402


def rearrange(ct, n, p, idx=None):
    """Rows of the full squares from offset p, concatenated. With idx (cipher index -> body index or None), also
    returns the matching index list."""
    sq = n * n; S = (len(ct) - p) // sq
    pos = [p + s * sq + j * n + i for s in range(S) for i in range(n) for j in range(n)]
    out = "".join(ct[q] for q in pos)
    return (out, [idx[q] for q in pos]) if idx is not None else out


def plant(body, k, rnd, pre="", post=""):
    """Nihilist by columns on the full squares of body (rows shuffled per square), partial last square in clear,
    then pre and post added untransposed. Returns (ct, idx)."""
    n = len(k); sq = n * n; S = len(body) // sq
    src = []
    for s in range(S):
        rho = rnd.sample(range(n), n)
        src += [s * sq + rho[i] * n + k[j] for j in range(n) for i in range(n)]
    src += list(range(S * sq, len(body)))
    ct = pre + "".join(body[i] for i in src) + post
    return ct, [None] * len(pre) + src + [None] * len(post)


def solve_scan(ct, n, seed, offsets=range(21), **kw):
    """Every preamble length p in offsets. Returns (score, p, order)."""
    rnd = random.Random(seed); best = (-99.0, None, None)
    for p in offsets:
        s, o = setsolve.solve(rearrange(ct, n, p), n, 0, rnd.randrange(1 << 30), **kw)
        if s > best[0]:
            best = (s, p, o)
    return best


def _selftest():
    rnd = random.Random("20-selftest")
    body = "".join(rnd.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(300))
    for n in (5, 7, 12):
        k = rnd.sample(range(n), n)
        ct, idx = plant(body, k, rnd, pre="QQQ", post="ZZ")
        assert all(ct[i] == body[j] for i, j in enumerate(idx) if j is not None)
        assert sorted(j for j in idx if j is not None) == list(range(300))
        r, ridx = rearrange(ct, n, 3, idx)
        true = [k.index(t) for t in range(n)]
        assert setsolve.adjacency_acc(ridx, true, 0) == 1.0
        rows = setsolve.dec_rows(r, true, 0)
        assert all(row in body for row in rows)
    print("nihcols self-test passed")


if __name__ == "__main__":
    _selftest()

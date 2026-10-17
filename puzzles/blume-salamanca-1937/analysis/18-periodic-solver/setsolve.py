"""Solver for letters permuted within sets of n, and for the Nihilist rectangle read by rows.

Both families put the plaintext in rows of n and permute the columns by one key. Sets of n read the rows in order;
the Nihilist rectangle read by rows also reorders the rows. In both, cipher position a + r*n + j is row r, cipher
column j, so the columns are known without any search. Two cipher columns that are neighbours in the plaintext
make a plaintext bigram in every row, and this does not depend on the row order. The key is therefore the
heaviest path through an n x n table of column-pair bigram scores (an asymmetric travelling-salesman path).

Convention (as 05-periodic): cipher set c[j] = p[k[j]], so plaintext column k[j] is cipher column j. The path is
the plaintext order of cipher columns, order = k^-1. Only the full rows from offset a are used; letters before a
and after the last full row are left out (their handling is unknown).

Stage 1: simulated annealing on the column-pair table (bigram log10 scores summed over rows); moves insert a
         segment of the path elsewhere. Several restarts; the distinct best paths go on.
Stage 2: hill climb on the within-row Spanish quadgram score (log10 per quadgram, quadgrams that cross a row
         boundary left out, so the score does not depend on the row order), from each stage-1 path.
Self-test: python3 -I setsolve.py
"""
import array, math, os, random

HERE = os.path.dirname(os.path.abspath(__file__))
LM = os.path.join(HERE, "..", "01-solver", "out")
Q4 = array.array("f"); Q4.fromfile(open(os.path.join(LM, "lm_es_4.bin"), "rb"), 26 ** 4)
B2 = array.array("f"); B2.fromfile(open(os.path.join(LM, "lm_es_2.bin"), "rb"), 26 ** 2)


# ---------------------------------------------------------------- the two families
def enc_sets(pt, k, a=0):
    """Sets of n from offset a; the letters before a and the partial last set stay in clear."""
    n = len(k); f = a + (len(pt) - a) // n * n
    return pt[:a] + "".join(pt[b + k[j]] for b in range(a, f, n) for j in range(n)) + pt[f:]


def enc_nihilist_rows(pt, k, rnd, a=0):
    """Full rows of n from offset a, reordered at random, then each row permuted by k."""
    n = len(k); f = a + (len(pt) - a) // n * n
    rows = [pt[b:b + n] for b in range(a, f, n)]; rnd.shuffle(rows)
    return enc_sets(pt[:a] + "".join(rows) + pt[f:], k, a)


def dec_rows(ct, order, a=0):
    """The full rows from offset a, each read in plaintext order. Returns a list of row strings."""
    n = len(order)
    return ["".join(ct[b + j] for j in order) for b in range(a, a + (len(ct) - a) // n * n, n)]


def plant(body, k, family, rnd, pre="", post=""):
    """Encrypt body (sets from its first letter; Nihilist rows reordered at random), then add untransposed
    letters before and after. Returns (ct, idx): idx[i] is the body index of cipher letter i, or None for a
    letter that is not body text (preamble, tail)."""
    n = len(k); f = len(body) // n * n
    rows = list(range(0, f, n))
    if family == "nihilist":
        rnd.shuffle(rows)
    src = [b + k[j] for b in rows for j in range(n)] + list(range(f, len(body)))
    ct = pre + "".join(body[i] for i in src) + post
    return ct, [None] * len(pre) + src + [None] * len(post)


def adjacency_acc(idx, order, a):
    """Share of within-row neighbours in the decryption that are neighbours in the body (body index + 1).
    Pairs with a non-body letter are left out. Free of row order, of the offset's labelling and (but for one
    pair per row) of the row's starting column."""
    n = len(order); good = tot = 0
    for b in range(a, a + (len(idx) - a) // n * n, n):
        v = [idx[b + j] for j in order]
        for x, y in zip(v, v[1:]):
            if x is not None and y is not None:
                tot += 1; good += (y == x + 1)
    return good / tot if tot else 0.0


# ---------------------------------------------------------------- scores
def columns(ct, n, a):
    R = (len(ct) - a) // n
    return [[ord(ct[a + r * n + j]) - 65 for r in range(R)] for j in range(n)]


def pair_table(cols):
    n = len(cols)
    return [[sum(B2[x * 26 + y] for x, y in zip(cols[i], cols[j])) if i != j else -1e9 for j in range(n)]
            for i in range(n)]


def qrows(cols, order):
    """Within-row quadgram score per quadgram."""
    R, n = len(cols[0]), len(order)
    seq = [cols[j] for j in order]
    s = 0.0
    for r in range(R):
        v = [c[r] for c in seq]
        s += sum(Q4[((v[t] * 26 + v[t + 1]) * 26 + v[t + 2]) * 26 + v[t + 3]] for t in range(n - 3))
    return s / (R * (n - 3))


# ---------------------------------------------------------------- stage 1: path annealing
def path_score(E, p):
    return sum(E[x][y] for x, y in zip(p, p[1:]))


def _seg_move(p, rnd):
    """Remove p[i..j] and insert it at position k of the remainder. Returns (i, j, k). Half the segments are
    short (mean 2.5), half of any length, so a rotation or a large block move is one move."""
    n = len(p)
    i = rnd.randrange(n)
    ln = int(rnd.expovariate(1 / 2.5)) if rnd.random() < 0.5 else rnd.randrange(n)
    j = min(n - 1, i + ln)
    k = rnd.randrange(n - (j - i + 1) + 1)
    return i, j, k


def _seg_delta(E, p, i, j, k):
    def e(x, y):
        return 0.0 if x is None or y is None else E[x][y]
    n = len(p)
    pre = p[i - 1] if i > 0 else None
    post = p[j + 1] if j + 1 < n else None
    rest = p[:i] + p[j + 1:]
    left = rest[k - 1] if k > 0 else None
    right = rest[k] if k < len(rest) else None
    return (-e(pre, p[i]) - e(p[j], post) + e(pre, post)
            - e(left, right) + e(left, p[i]) + e(p[j], right))


def _apply(p, i, j, k):
    seg, rest = p[i:j + 1], p[:i] + p[j + 1:]
    return rest[:k] + seg + rest[k:]


def anneal_path(E, n, rnd, iters, t0, t1):
    p = rnd.sample(range(n), n); s = path_score(E, p)
    best, bs = p[:], s
    for it in range(iters):
        T = t0 * (t1 / t0) ** (it / iters)
        i, j, k = _seg_move(p, rnd)
        d = _seg_delta(E, p, i, j, k)
        if d >= 0 or rnd.random() < math.exp(d / T):
            p = _apply(p, i, j, k); s += d
            if s > bs:
                best, bs = p[:], s
    return bs, best


# ---------------------------------------------------------------- stage 2: quadgram hill climb
def climb(cols, order, rnd, patience):
    n = len(order); s = qrows(cols, order); stale = 0
    while stale < patience:
        i, j, k = _seg_move(order, rnd)
        m = _apply(order, i, j, k)
        if m == order:
            continue
        t = qrows(cols, m)
        if t > s:
            order, s, stale = m, t, 0
        else:
            stale += 1
    for r in range(1, n):  # a row read from the wrong starting column is one segment move away; check all
        m = order[r:] + order[:r]; t = qrows(cols, m)
        if t > s:
            order, s = m, t
    return s, order


# ---------------------------------------------------------------- driver
PARAMS = dict(restarts=8, iters_per_n=4000, t0_per_row=0.25, t1_per_row=0.01, keep=3, patience_per_n=60)


def solve(ct, n, a, seed, **kw):
    """Best (score, order) for width n, offset a. order is the plaintext order of cipher columns."""
    P = dict(PARAMS, **kw)
    rnd = random.Random(seed)
    cols = columns(ct, n, a); R = len(cols[0]); E = pair_table(cols)
    found = {}
    for _ in range(P["restarts"]):
        s, p = anneal_path(E, n, rnd, P["iters_per_n"] * n, P["t0_per_row"] * R, P["t1_per_row"] * R)
        found[tuple(p)] = s
    starts = sorted(found, key=found.get, reverse=True)[:P["keep"]]
    best = (-99.0, None)
    for p in starts:
        s, o = climb(cols, list(p), rnd, P["patience_per_n"] * n)
        if s > best[0]:
            best = (s, o)
    return best


def solve_scan(ct, n, seed, **kw):
    """Every offset a in [0, n): a preamble of any length leaves the sets starting at one of them.
    Returns (score, a, order) for the best offset. Offset a's solver seed is drawn from the run's seed."""
    rnd = random.Random(seed); best = (-99.0, None, None)
    for a in range(n):
        s, o = solve(ct, n, a, rnd.randrange(1 << 30), **kw)
        if s > best[0]:
            best = (s, a, o)
    return best


def key_of(order):
    k = [0] * len(order)
    for t, j in enumerate(order):
        k[j] = t
    return k


def _selftest():
    rnd = random.Random("18-selftest")
    pt = "".join(rnd.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(103))
    for n, a in ((7, 0), (10, 3), (13, 5)):
        k = rnd.sample(range(n), n)
        ct = enc_sets(pt, k, a)
        assert len(ct) == len(pt) and sorted(ct) == sorted(pt)
        rows = dec_rows(ct, [k.index(t) for t in range(n)], a)
        f = a + (len(pt) - a) // n * n
        assert "".join(rows) == pt[a:f], (n, a)
        assert key_of([k.index(t) for t in range(n)]) == k
        # Nihilist rows: every decrypted row is a plaintext row
        ctn = enc_nihilist_rows(pt, k, rnd, a)
        prow = {pt[b:b + n] for b in range(a, f, n)}
        assert set(dec_rows(ctn, [k.index(t) for t in range(n)], a)) == prow
    # plant(): the index map decrypts; adjacency is 1 for the true key at the true offset
    body = "".join(rnd.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(97))
    for fam in ("sets", "nihilist"):
        k = rnd.sample(range(12), 12)
        ct, idx = plant(body, k, fam, rnd, pre="QQQQQQQ", post="ZZZ")
        assert all(ct[i] == body[j] for i, j in enumerate(idx) if j is not None)
        assert sorted(j for j in idx if j is not None) == list(range(97))
        assert adjacency_acc(idx, [k.index(t) for t in range(12)], 7) == 1.0
        if fam == "sets":
            assert ct == "QQQQQQQ" + enc_sets(body, k) + "ZZZ"
    # segment-move delta agrees with a full rescore
    E = [[rnd.random() for _ in range(9)] for _ in range(9)]
    p = list(range(9))
    for _ in range(2000):
        i, j, k = _seg_move(p, rnd)
        m = _apply(p, i, j, k)
        assert abs(path_score(E, m) - path_score(E, p) - _seg_delta(E, p, i, j, k)) < 1e-9
        p = m
    print("setsolve self-test passed")


if __name__ == "__main__":
    _selftest()

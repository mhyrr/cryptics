"""align_log.py - line/align.py with the E-step done in log space (same model, same numbers; no underflow).

    python3 align_log.py build|heldout|decode ...        (arguments exactly as line/align.py)
    python3 align_log.py --selftest

Why. align.py's forward pass keeps each row of the lattice as plain floats scaled to sum 1. With a plain side
that is half lacunae, paths that lag far behind in the plaintext are cheap for a long time (a unit lost in a
lacuna costs 0.5, a unit that emits a letter costs about 0.03 before training), so nearly all of a row's mass
sits on states that cannot reach the end, and the states that can fall below the smallest float. The first
build of the primary run stopped with "alignment band lost at unit 3417" at the last unit, on the first pass.
This file changes the arithmetic only: probabilities are carried as logarithms. Emission table, priors, band,
skip and lacuna costs, Viterbi, key rules and the held-out procedure are align.py's, untouched.
--selftest runs both E-steps on a stretch where the plain one does not underflow and prints the largest
difference in log-likelihood, centres and expected counts.
"""
import math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "line"))
import align  # noqa: E402

NEG = float("-inf")
_log, _exp = math.log, math.exp


def lse(xs):
    m = max(xs)
    if m == NEG:
        return NEG
    return m + _log(sum(_exp(x - m) for x in xs))


class LogSegment(align.Segment):
    def estep(self, table, new):
        n, lo, hi = self.n, self.lo, self.hi
        lskip = _log(align.SKIP)
        A = [[NEG] * (hi[i] - lo[i] + 1) for i in range(n + 1)]
        A[0][0] = 0.0
        for j in range(lo[0] + 1, hi[0] + 1):
            A[0][j - lo[0]] = A[0][j - 1 - lo[0]] + lskip
        opts = [None] * (n + 1)
        for i in range(1, n + 1):
            row, prev, plo, l = A[i], A[i - 1], lo[i - 1], lo[i]
            ro = []
            for j in range(l, hi[i] + 1):
                o = [(j0, s, _log(p)) for j0, s, p in self.options(i, j, table) if p > 0]
                ro.append(o)
                ts = [prev[j0 - plo] + lp for j0, s, lp in o]
                if j > l:
                    ts.append(row[j - 1 - l] + lskip)
                row[j - l] = lse(ts) if ts else NEG
            opts[i] = ro
            if max(row) == NEG:
                raise ValueError(f"alignment band lost at unit {i}; widen --band or add anchors")
        ll = A[n][0]
        if ll == NEG:
            raise ValueError(f"alignment band lost at unit {n}; widen --band or add anchors")
        B = [[NEG] * (hi[i] - lo[i] + 1) for i in range(n + 1)]
        B[n][0] = 0.0
        centers = [0.0] * (n + 1)
        centers[n] = float(self.m)
        for i in range(n, 0, -1):
            row, l = B[i], lo[i]
            for j in range(hi[i] - 1, l - 1, -1):          # skips inside row i
                a, b = row[j - l], row[j + 1 - l] + lskip
                if b != NEG:
                    row[j - l] = b if a == NEG else max(a, b) + math.log1p(_exp(-abs(a - b)))
            prev, plo = B[i - 1], lo[i - 1]
            a_prev = A[i - 1]
            u = self.units[i - 1]
            acc = {}
            post = []
            for j in range(l, hi[i] + 1):
                b = row[j - l]
                if b == NEG:
                    continue
                for j0, s, lp in opts[i][j - l]:
                    v = lp + b
                    acc.setdefault(j0 - plo, []).append(v)
                    a = a_prev[j0 - plo]
                    if a != NEG:
                        post.append((s, a + v, j0))
            for k, vs in acc.items():
                prev[k] = lse(vs)
            if post:
                gm = max(g for _, g, _ in post)
                ws = [(s, _exp(g - gm), j0) for s, g, j0 in post]
                z = sum(w for _, w, _ in ws)
                cen = 0.0
                for s, w, j0 in ws:
                    w /= z
                    cen += w * j0
                    if w > 0 and s is not None and u.kind == "sign" and u.sym != "?":
                        new.add(u.sym, s, w, (id(self), j0))
                centers[i - 1] = cen
        return ll, centers


def selftest():
    import random
    rng = random.Random(3)
    letters = "abcdefghilmnopqrstuz"
    plain = "".join(rng.choice(letters) for _ in range(400))
    toks = []
    for k, ch in enumerate(plain):
        toks.append("s" + ch)
        if rng.random() < 0.1:
            toks.append("nul")
    ctext = "\n".join(" ".join(toks[i:i + 40]) for i in range(0, len(toks), 40))
    ptext = " ".join(plain[i:i + 5] for i in range(0, len(plain), 5))
    units, _, _ = align.parse_cipher(ctext)
    P, wb, lac, _ = align.parse_plain(ptext)
    worst = dict(ll=0.0, centre=0.0, count=0.0)
    ta, tb = align.Table(), align.Table()
    for it in range(3):
        na, nb = align.Table(), align.Table()
        la, ca = align.Segment(units, P, wb, lac).estep(ta, na)
        lb, cb = LogSegment(units, P, wb, lac).estep(tb, nb)
        worst["ll"] = max(worst["ll"], abs(la - lb))
        worst["centre"] = max(worst["centre"], max(abs(x - y) for x, y in zip(ca, cb)))
        for sym in na.cnt:
            for s, w in na.cnt[sym].items():
                worst["count"] = max(worst["count"], abs(w - nb.cnt[sym].get(s, 0.0)))
        ta, tb = na, nb
    for k, v in worst.items():
        print("largest difference in %s over 3 passes\t%.3g" % (k, v))
    assert worst["ll"] < 1e-6 and worst["centre"] < 1e-6 and worst["count"] < 1e-6
    print("log-space E-step agrees with align.py's")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    else:
        align.Segment = LogSegment
        align.main()

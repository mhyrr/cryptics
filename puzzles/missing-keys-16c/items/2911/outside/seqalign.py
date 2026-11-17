"""seqalign.py - affine-gap global alignment of a decoded letter string to a plain text (Gotoh), standard library.

Used by diagnose.py. The decode (D) is longer than the plain text (P) wherever the cipher letter has matter the
copy left out, so a run of D letters with no partner must be cheap once opened: opening a gap costs GO, each
further letter GEX (D letters left over) or GEY (P letters left over). A match scores MA, a mismatch MM. With
MA=2, GO=-5 an isolated island needs three matching letters in a row to pay for leaving a gap and re-entering.
Ends are free on the D side (leading and trailing cipher text costs nothing).

    align(D, P) -> list of (i, j) pairs, i index in D or None, j index in P or None, in order.
"""
MA, MM, GO, GEX, GEY = 2.0, -1.0, -5.0, -0.05, -0.5
NEG = -1e18


def align(D, P):
    n, m = len(D), len(P)
    W = m + 1
    tb = bytearray((n + 1) * W)
    Mp = [NEG] * W; Xp = [NEG] * W; Yp = [NEG] * W
    Mp[0] = 0.0
    for j in range(1, W):
        Yp[j] = GO + GEY * (j - 1)
        tb[j] = 2 << 4
    for i in range(1, n + 1):
        Mc = [NEG] * W; Xc = [NEG] * W; Yc = [NEG] * W
        Xc[0] = 0.0                                   # free leading D letters
        base = i * W
        tb[base] = 1 << 2
        di = D[i - 1]
        mprev, xprev, yprev = Mp[0], Xp[0], Yp[0]     # values at j-1 of the previous row
        mleft, xleft, yleft = NEG, 0.0, NEG           # values at j-1 of this row
        for j in range(1, W):
            # M
            if mprev >= xprev:
                if mprev >= yprev: b, pm = mprev, 0
                else: b, pm = yprev, 2
            else:
                if xprev >= yprev: b, pm = xprev, 1
                else: b, pm = yprev, 2
            mv = b + (MA if di == P[j - 1] else MM)
            # X: D letter i against nothing
            a0, a1, a2 = Mp[j] + GO, Xp[j] + GEX, Yp[j] + GO
            if a1 >= a0:
                if a1 >= a2: xv, px = a1, 1
                else: xv, px = a2, 2
            else:
                if a0 >= a2: xv, px = a0, 0
                else: xv, px = a2, 2
            # Y: P letter j against nothing
            c0, c1, c2 = mleft + GO, xleft + GO, yleft + GEY
            if c2 >= c0:
                if c2 >= c1: yv, py = c2, 2
                else: yv, py = c1, 1
            else:
                if c0 >= c1: yv, py = c0, 0
                else: yv, py = c1, 1
            Mc[j] = mv; Xc[j] = xv; Yc[j] = yv
            tb[base + j] = pm | (px << 2) | (py << 4)
            mprev, xprev, yprev = Mp[j], Xp[j], Yp[j]
            mleft, xleft, yleft = mv, xv, yv
        Mp, Xp, Yp = Mc, Xc, Yc
    # free trailing D letters: best over last column is reached by X with extension only; take best state at (n, m)
    best = max((Mp[m], 0), (Xp[m], 1), (Yp[m], 2))
    # allow trailing D letters free: scan column m upward is not stored; approximate by GEX being near zero
    st = best[1]
    i, j, out = n, m, []
    while i > 0 or j > 0:
        t = tb[i * W + j]
        if st == 0:
            out.append((i - 1, j - 1)); st = t & 3; i -= 1; j -= 1
        elif st == 1:
            out.append((i - 1, None)); st = (t >> 2) & 3; i -= 1
            if j == 0 and i > 0:
                st = 1
        else:
            out.append((None, j - 1)); st = (t >> 4) & 3; j -= 1
            if i == 0 and j > 0:
                st = 2
    out.reverse()
    return out


if __name__ == "__main__":
    a = align("xxxxintendesicomeparezzzzzzzzzzchepapa", "intendesicomeparechelpapa")
    print("".join(("=" if i is not None and j is not None else "-") for i, j in a))

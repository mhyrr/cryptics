"""v1: unmatched cipher goes into a gap; null is rare.

Two changes to the pilot's model (H6).
1. A gap state. A run of units may match no plain text at all (the decipherment is an abridgement). Entering a
   gap costs OPEN, each further unit EXT. Units in a gap teach the table nothing.
2. Null is rare. The empty emission has prior weight NULL0 (align.py: 0.04) and a plain letter that no unit
   accounts for costs SKIP (align.py: 0.02). In the pilot "every sign is null, the letters ride on a few rare
   signs or are skipped" cost about as much as a real alignment, and every pass moved toward it.
Arithmetic is in log space. The emission table, priors, word spans, key rules are line/align.py's.
Parameters can be set from the environment for trials: V1_OPEN, V1_EXT, V1_NULL0, V1_SKIP, V1_ITERS, V1_BAND,
V1_NULLFROM (the empty emission is forbidden before that pass; a null prior alone did not stop the drift).
"""
import math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "..", "line"))
import align  # noqa: E402

NEG = float("-inf")
OPEN = float(os.environ.get("V1_OPEN", -10.0))
EXT = float(os.environ.get("V1_EXT", -1.0))
NULL0 = float(os.environ.get("V1_NULL0", 0.002))
SKIP = float(os.environ.get("V1_SKIP", 0.002))
ITERS = int(os.environ.get("V1_ITERS", 14))
BAND = os.environ.get("V1_BAND")
NULLFROM = int(os.environ.get("V1_NULLFROM", 0))    # first pass (0-based) in which the empty emission is allowed
_log, _exp, _log1p = math.log, math.exp, math.log1p


def la(a, b):
    if a < b:
        a, b = b, a
    if b == NEG:
        return a
    return a + _log1p(_exp(b - a))


class GapSegment(align.Segment):
    def lopts(self, table):
        """options for every (i, j) with log probabilities: opts[i][j - lo[i]] = [(j0, s, logp)]."""
        out = [None]
        for i in range(1, self.n + 1):
            row = []
            for j in range(self.lo[i], self.hi[i] + 1):
                row.append([(j0, s, _log(p)) for j0, s, p in self.options(i, j, table) if p > 0 and s is not None])
            out.append(row)
        return out

    def forward(self, opts, viterbi=False):
        n, lo, hi = self.n, self.lo, self.hi
        lskip = _log(SKIP)
        comb = max if viterbi else la
        M = [[NEG] * (hi[i] - lo[i] + 1) for i in range(n + 1)]
        G = [[NEG] * (hi[i] - lo[i] + 1) for i in range(n + 1)]
        bp = [[None] * (hi[i] - lo[i] + 1) for i in range(n + 1)] if viterbi else None
        bg = [[None] * (hi[i] - lo[i] + 1) for i in range(n + 1)] if viterbi else None
        M[0][0] = 0.0
        for j in range(lo[0] + 1, hi[0] + 1):
            M[0][j - lo[0]] = M[0][j - 1 - lo[0]] + lskip
            if viterbi:
                bp[0][j - lo[0]] = ("skip",)
        for i in range(1, n + 1):
            Mi, Gi, Mp, Gp, l, pl, ph = M[i], G[i], M[i - 1], G[i - 1], lo[i], lo[i - 1], hi[i - 1]
            ro = opts[i]
            for j in range(l, hi[i] + 1):
                best, arg = NEG, None
                for j0, s, lp in ro[j - l]:
                    a, b = Mp[j0 - pl], Gp[j0 - pl]
                    if viterbi:
                        t = (a if a >= b else b) + lp
                        if t > best:
                            best, arg = t, ("emit", j0, s, "M" if a >= b else "G")
                    else:
                        t = la(a, b)
                        if t > NEG:
                            best = la(best, t + lp)
                if j > l:
                    t = Mi[j - 1 - l] + lskip
                    if viterbi:
                        if t > best:
                            best, arg = t, ("skip",)
                    else:
                        best = la(best, t)
                Mi[j - l] = best
                if viterbi:
                    bp[i][j - l] = arg
                if pl <= j <= ph:
                    a, b = Mp[j - pl] + OPEN, Gp[j - pl] + EXT
                    Gi[j - l] = comb(a, b)
                    if viterbi:
                        bg[i][j - l] = "M" if a >= b else "G"
        return M, G, bp, bg

    def estep(self, table, new):
        n, lo, hi, m = self.n, self.lo, self.hi, self.m
        lskip = _log(SKIP)
        opts = self.lopts(table)
        M, G, _, _ = self.forward(opts)
        Z = la(M[n][m - lo[n]], G[n][m - lo[n]])
        if Z == NEG:
            raise ValueError("no path through the band")
        BM = [[NEG] * (hi[i] - lo[i] + 1) for i in range(n + 1)]
        BG = [[NEG] * (hi[i] - lo[i] + 1) for i in range(n + 1)]
        BM[n][m - lo[n]] = 0.0
        BG[n][m - lo[n]] = 0.0
        gapped = 0.0
        for i in range(n - 1, -1, -1):
            l, nl, nh = lo[i], lo[i + 1], hi[i + 1]
            E = [NEG] * (hi[i] - l + 1)
            u = self.units[i]
            Mi, Gi, BMn = M[i], G[i], BM[i + 1]
            learn = u.kind == "sign" and u.sym != "?"
            ro = opts[i + 1]
            for j in range(nl, nh + 1):
                b = BMn[j - nl]
                if b == NEG:
                    continue
                for j0, s, lp in ro[j - nl]:
                    t = lp + b
                    k = j0 - l
                    E[k] = la(E[k], t)
                    if learn:
                        w = la(Mi[k], Gi[k]) + t - Z
                        if w > -30:
                            new.add(u.sym, s, _exp(w), (id(self), j0))
            BMi, BGi, BGn = BM[i], BG[i], BG[i + 1]
            for j in range(hi[i], l - 1, -1):
                k = j - l
                g = BGn[j - nl] if nl <= j <= nh else NEG
                bm = la(E[k], g + OPEN) if g > NEG else E[k]
                if j < hi[i]:
                    bm = la(bm, BMi[k + 1] + lskip)
                BMi[k] = bm
                BGi[k] = la(E[k], g + EXT) if g > NEG else E[k]
                if g > NEG:
                    w1 = Mi[k] + OPEN + g - Z
                    w2 = Gi[k] + EXT + g - Z
                    if w1 > -30:
                        gapped += _exp(w1)
                    if w2 > -30:
                        gapped += _exp(w2)
        return Z, gapped

    def viterbi(self, table):
        n, lo, m = self.n, self.lo, self.m
        opts = self.lopts(table)
        M, G, bp, bg = self.forward(opts, viterbi=True)
        state = "M" if M[n][m - lo[n]] >= G[n][m - lo[n]] else "G"
        spans, skipped = [None] * n, []
        i, j = n, m
        while i > 0 or j > 0:
            if state == "G":
                spans[i - 1] = (j, j, None)
                state = bg[i][j - lo[i]]
                i -= 1
                continue
            b = bp[i][j - lo[i]]
            if b is None:
                raise ValueError("no path")
            if b[0] == "skip":
                skipped.append(j - 1)
                j -= 1
            else:
                spans[i - 1] = (b[1], j, b[2])
                i, j, state = i - 1, b[1], b[3]
        return spans, skipped


def build(cipher, plain, log):
    old = (align.P_LEN[0], align.SKIP)
    align.P_LEN[0], align.SKIP = NULL0, SKIP
    try:
        units, P, wb, lac, pairs = align.load_pair(cipher, plain)
        band = int(BAND) if BAND else None
        segs = [(a, c, GapSegment(s.units, s.P, s.wb, s.lac, band))
                for a, c, s in align.make_segments(units, P, wb, lac, pairs, band)]
        table = align.Table()
        for it in range(ITERS):
            align.P_LEN[0] = NULL0 if it >= NULLFROM else 0.0
            table._cache = {}
            new, ll, gp = align.Table(), 0.0, 0.0
            for a, c, seg in segs:
                z, g = seg.estep(table, new)
                ll += z
                gp += g
            table = new
            nul = sum(v.get("", 0.0) for v in table.cnt.values()) / max(1e-9, sum(table.tot.values()))
            log(f"pass {it + 1}: ll {ll:.1f} units in gaps {gp:.0f} of {len(units)} null share {nul:.3f}")
        align.P_LEN[0] = NULL0
        table._cache = {}
        path, skipped = align.best_path(segs, table)
        gaps = sum(1 for u, a, b, s in path if s is None)
        log(f"best path: {gaps} units in gaps, {len(skipped)} letters unaccounted")
        return align.key_from_path(path, skipped)
    finally:
        align.P_LEN[0], align.SKIP = old

"""v2: bootstrap from the anchored start, then grow.

Why. v0 and v1 give every unit a window of about +-7*sqrt(n) letters (275 on the first page). A sign's true
drift from a steady pace is about sqrt(distance from the nearest anchor) letters. In a window that wide a sign
seen 10-30 times shows no signal, and the passes drift (to nulls in v0/v1, to nothing sharp with nulls
forbidden). Calibration did not show it because Cp.30's units each occur a hundred times or more.

Method.
 1. Pace. For each trial pace rho (plain letters per unit) take the first N0 units against the start of the
    plain text, the end left free, each unit's position held near rho*i with a width that grows as sqrt(i).
    A few passes each; keep the pace with the highest log-likelihood.
 2. Grow. Double the stretch of units. Units already placed keep a narrow window round their place on the
    best path. New units may run ahead of the pace only a little but may lag without limit, because a stretch
    of cipher may have no plain text (the gap state of v1_gap). Passes carry the table forward.
 3. The empty emission is forbidden until the table is sharp (stage NULL_STAGE on); gaps are allowed from
    stage GAP_STAGE on.
Everything else (emission table, priors, word spans, key rules) is line/align.py's. Positions, never values.
Environment for trials: V2_N0, V2_RHOS, V2_SIG0, V2_SIGK, V2_PASSES0, V2_PASSES, V2_GAP_STAGE, V2_NULL_STAGE.
"""
import math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "..", "line"))
import align, v1_gap  # noqa: E402
from v1_gap import la, NEG, GapSegment  # noqa: E402

N0 = int(os.environ.get("V2_N0", 250))
RHOS = [float(x) for x in os.environ.get("V2_RHOS", "0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7").split(",")]
SIG0 = float(os.environ.get("V2_SIG0", 6.0))
SIGK = float(os.environ.get("V2_SIGK", 1.0))
PASSES0 = int(os.environ.get("V2_PASSES0", 8))
PASSES = int(os.environ.get("V2_PASSES", 6))
GAP_STAGE = int(os.environ.get("V2_GAP_STAGE", 1))
NULL_STAGE = int(os.environ.get("V2_NULL_STAGE", 2))
OPEN, EXT, NULL0, SKIP = -10.0, -1.0, 0.002, 0.002
_log, _exp = math.log, math.exp


class Stretch(GapSegment):
    """Units 0..n against letters 0..m; start fixed at (0, 0), end free unless `closed`."""

    def __init__(self, units, P, wb, lac, mu, sig, lag_from=None, closed=False):
        align.Segment.__init__(self, units, P, wb, lac, band=10 ** 9)
        n, m = self.n, self.m
        self.mu, self.sig, self.closed = mu, sig, closed
        for i in range(n + 1):
            lo = int(mu[i] - 4 * sig[i])
            if lag_from is not None and i >= lag_from[0]:
                lo = min(lo, lag_from[1] - 20)          # new units may lag as far back as the old end
            self.lo[i] = max(0, min(m, lo))
            self.hi[i] = max(0, min(m, int(mu[i] + 4 * sig[i]) + 1))
        self.lo[0] = 0
        if closed:
            self.lo[n] = self.hi[n] = m
        for i in range(1, n + 1):
            self.lo[i] = max(self.lo[i], self.lo[i - 1])
            self.hi[i] = max(self.hi[i], self.hi[i - 1]) if not closed else self.hi[i]
        if closed:
            for i in range(n - 1, -1, -1):
                self.hi[i] = min(self.hi[i], self.hi[i + 1])
        for i in range(n + 1):
            if self.lo[i] > self.hi[i]:
                self.lo[i] = self.hi[i]
        self.lag_from = lag_from
        self.gap_ok = False

    def lopts(self, table):
        out = [None]
        mu, sig, lf = self.mu, self.sig, self.lag_from
        for i in range(1, self.n + 1):
            row = []
            inv = 0.5 / (sig[i] * sig[i])
            lagfree = lf is not None and i >= lf[0]
            for j in range(self.lo[i], self.hi[i] + 1):
                d = j - mu[i]
                pen = 0.0 if (lagfree and d < 0) else -d * d * inv
                row.append([(j0, s, _log(p) + pen) for j0, s, p in self.options(i, j, table) if p > 0 and s is not None])
            out.append(row)
        return out

    # free end: every state of the last row may finish
    def end_scores(self, M, G):
        n = self.n
        if self.closed:
            k = self.m - self.lo[n]
            return [(self.m, M[n][k], G[n][k])]
        return [(self.lo[n] + k, M[n][k], G[n][k]) for k in range(len(M[n]))]

    def estep(self, table, new):
        n, lo, hi = self.n, self.lo, self.hi
        lskip = _log(SKIP)
        op = OPEN if self.gap_ok else NEG
        opts = self.lopts(table)
        M, G, _, _ = self.forward(opts, op=op)
        Z = NEG
        for j, a, b in self.end_scores(M, G):
            Z = la(Z, la(a, b))
        if Z == NEG:
            raise ValueError("no path through the window")
        BM = [[NEG] * (hi[i] - lo[i] + 1) for i in range(n + 1)]
        BG = [[NEG] * (hi[i] - lo[i] + 1) for i in range(n + 1)]
        for j, a, b in self.end_scores(M, G):
            BM[n][j - lo[n]] = 0.0
            BG[n][j - lo[n]] = 0.0
        if not self.closed:                      # letters after the last unit are simply outside the stretch
            pass
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
                    k = j0 - l
                    if k < 0 or k >= len(E):
                        continue
                    t = lp + b
                    E[k] = la(E[k], t)
                    if learn:
                        w = la(Mi[k], Gi[k]) + t - Z
                        if w > -30:
                            new.add(u.sym, s, _exp(w), (id(self.P), j0))
            BMi, BGi, BGn = BM[i], BG[i], BG[i + 1]
            for j in range(hi[i], l - 1, -1):
                k = j - l
                g = BGn[j - nl] if (nl <= j <= nh and op > NEG) else NEG
                bm = la(E[k], g + op) if g > NEG else E[k]
                if j < hi[i]:
                    bm = la(bm, BMi[k + 1] + lskip)
                BMi[k] = bm
                BGi[k] = la(E[k], g + EXT) if g > NEG else E[k]
                if g > NEG:
                    w1, w2 = Mi[k] + op + g - Z, Gi[k] + EXT + g - Z
                    if w1 > -30:
                        gapped += _exp(w1)
                    if w2 > -30:
                        gapped += _exp(w2)
        return Z, gapped

    def forward(self, opts, viterbi=False, op=None):
        saved = v1_gap.OPEN
        v1_gap.OPEN = (OPEN if self.gap_ok else NEG) if op is None else op
        try:
            return self._forward(opts, viterbi)
        finally:
            v1_gap.OPEN = saved

    def _forward(self, opts, viterbi):
        n, lo, hi = self.n, self.lo, self.hi
        lskip = _log(SKIP)
        op = v1_gap.OPEN
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
                    if j0 < pl or j0 > ph:
                        continue
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
                if pl <= j <= ph and op > NEG:
                    a, b = Mp[j - pl] + op, Gp[j - pl] + EXT
                    Gi[j - l] = comb(a, b)
                    if viterbi:
                        bg[i][j - l] = "M" if a >= b else "G"
        return M, G, bp, bg

    def viterbi(self, table):
        n, lo = self.n, self.lo
        opts = self.lopts(table)
        M, G, bp, bg = self.forward(opts, viterbi=True)
        best, j, state = NEG, None, "M"
        for jj, a, b in self.end_scores(M, G):
            if a > best:
                best, j, state = a, jj, "M"
            if b > best:
                best, j, state = b, jj, "G"
        if j is None:
            raise ValueError("no path")
        end = j
        spans, skipped = [None] * n, []
        i = n
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
        return spans, skipped, end


def passes(st, table, k, log, tag):
    z = g = 0.0
    for it in range(k):
        table._cache = {}
        new = align.Table()
        z, g = st.estep(table, new)
        table = new
    log(f"{tag}: units {st.n} window letters {st.m} ll {z:.1f} per unit {z / max(1, st.n):.3f} in gaps {g:.0f}")
    return table, z


def build(cipher, plain, log):
    old = (align.P_LEN[0], align.SKIP)
    align.SKIP = SKIP
    try:
        units, P, wb, lac, _ = align.load_pair(cipher, plain)
        n_all, m_all = len(units), len(P)

        def stretch(n, mu, sig, lag_from=None, closed=False):
            m = m_all if closed else min(m_all, int(max(mu[i] + 4 * sig[i] for i in range(n + 1))) + 2)
            return Stretch(units[:n], P[:m], wb[:m + 1], lac[:m + 1], mu, sig, lag_from, closed)

        # 1. pace
        align.P_LEN[0] = 0.0
        n0 = min(N0, n_all)
        best = None
        for rho in RHOS:
            mu = [rho * i for i in range(n0 + 1)]
            sig = [SIG0 + SIGK * math.sqrt(i) for i in range(n0 + 1)]
            st = stretch(n0, mu, sig)
            table, z = passes(st, align.Table(), PASSES0, log, f"pace {rho:.2f}")
            if best is None or z > best[0]:
                best = (z, rho, table, st)
        _, rho, table, st = best
        log(f"pace chosen: {rho:.2f} letters per unit")
        # 2. grow
        n, stage = n0, 0
        while True:
            table._cache = {}
            spans, _, end = st.viterbi(table)
            if n >= n_all:
                break
            stage += 1
            n2 = min(n_all, 2 * n)
            ends = [0] + [sp[1] for sp in spans]
            placed = [u for u, sp in zip(units[:n], spans) if sp[2] is not None]
            pace = (end / max(1, len(placed))) if placed else rho      # pace over units not in gaps
            mu = ends + [end + pace * (i - n) for i in range(n + 1, n2 + 1)]
            sig = [8.0] * (n + 1) + [8.0 + SIGK * math.sqrt(i - n) for i in range(n + 1, n2 + 1)]
            align.P_LEN[0] = NULL0 if stage >= NULL_STAGE else 0.0
            st = stretch(n2, mu, sig, lag_from=(n + 1, end) if stage >= GAP_STAGE else None)
            st.gap_ok = stage >= GAP_STAGE
            table, z = passes(st, table, PASSES, log, f"stage {stage} (pace {pace:.2f})")
            n = n2
        # 3. final passes over everything, nulls and gaps allowed, then the table
        align.P_LEN[0] = NULL0
        st.gap_ok = True
        table, z = passes(st, table, 3, log, "final")
        table._cache = {}
        spans, skipped, end = st.viterbi(table)
        path = [(u, sp[0], sp[1], sp[2]) for u, sp in zip(units, spans)]
        gaps = sum(1 for sp in spans if sp[2] is None)
        log(f"best path: ends at letter {end} of {m_all}; {gaps} units in gaps; {len(skipped)} letters unaccounted")
        return align.key_from_path(path, skipped)
    finally:
        align.P_LEN[0], align.SKIP = old

"""Exact fit of shared runs to one single-columnar geometry (experiment 16, candidate K3).

Model. Each telegram is s untransposed letters, a body of L letters, then e untransposed letters.
The body is written in rows of width w and read by columns in key order (forward single columnar).
The column of rank k has h = L // w letters, plus one if it is long. One key serves both telegrams,
so the same plaintext columns are long-eligible in both; the counts x1 = L1 % w and x2 = L2 % w differ.
  S1(k) = s1 + k*h1 + n1(k),  S2(k) = s2 + k*h2 + n2(k),  n(k) = long columns among ranks < k.
A run (a, b, len) of T1 position a and T2 position b sits at rank k, row r (T2 frame) iff
  b = S2(k) + r,  a = S1(k) + r + dr,  0 <= r <= colLen2(k) - len,  0 <= r + dr <= colLen1(k) - len,
with one row offset dr for every run ("top" alignment: a shared phrase whose plaintext offsets agree
mod w). With bottoms allowed, a run may instead sit at equal distance from the bottom of the column in
both telegrams (a shared closing). That needs L1 = L2 (mod w): no column is long in one telegram and
short in the other, every column has colLen1 - colLen2 = h1 - h2, and the run's row offset is h1 - h2.

Drift form. Put c1(k) = s1 + n1(k) and c2(k) = s2 + n2(k). Each rank is one step of a lattice path.
Its type is B (long in both), O (long only in the telegram with more long columns) or N (short in both).
  mode 1 (x1 >= x2): B = (+1, +1), O = (+1, 0), N = (0, 0)
  mode 2 (x2 >= x1): B = (+1, +1), O = (0, +1), N = (0, 0)
  mode 0 (x1 == x2): B and N only (used for the bottoms variant)
Any sequence with the right type counts is realised by some key, so "realisable for some common key"
is exactly "a lattice path with these steps exists". Ends: c1(0) = s1, c2(0) = s2,
c1(w) = 615 - e1 - h1*w, c2(w) = 160 - e2 - h2*w. We let x run to w (all columns long). That is the
same geometry as (h + 1, x = 0), so no geometry is added or lost, and the start and end boxes decouple.

Search. For each (w, h1, h2, mode) a cheap relaxation (pairwise edges in a DAG of (run, rank) nodes)
bounds the chain length. Only when the bound can beat (or, when collecting, reach) the best so far
does the exact chain DP run, once per dr. The DP is over events (run, rank, step type, offset), each
with an interval of c2 values; it keeps, for each event and c2 value, the longest consistent chain.
Consecutive events must be joined by a feasible path segment whose first step is the earlier event's
column type; runs on one rank must share the column (same c1, c2 and type). Nothing is approximated.
"""

N1, N2 = 615, 160
TYPES = {1: ("B", "O", "N"), 2: ("B", "O", "N"), 0: ("B", "N")}
LEN = {(1, "B"): (1, 1), (1, "O"): (1, 0), (1, "N"): (0, 0),
       (2, "B"): (1, 1), (2, "O"): (0, 1), (2, "N"): (0, 0),
       (0, "B"): (1, 1), (0, "N"): (0, 0)}


def d1_range(mode, dk, d2, t):
    """Range of c1 increments over dk steps with c2 increment d2, first step of type t (None: any)."""
    tb, to, tn = t == "B", t == "O", t == "N"
    if mode == 1:
        if d2 < tb or d2 > dk:
            return None
        lo, hi = d2 + to, dk - tn
    elif mode == 2:
        if d2 < 0 or d2 > dk - tn:
            return None
        lo, hi = int(tb), d2 - to
    else:
        if d2 < tb or d2 > dk - tn:
            return None
        lo = hi = d2
    return (lo, hi) if lo <= hi else None


def seg_range(mode, dk, dd, t):
    """Range of c2 increments over dk >= 1 steps given dd = (c1 - c2) increment, first step type t."""
    tb, to, tn = t == "B", t == "O", t == "N"
    if mode == 1:
        if dd < to:
            return None
        lo, hi = int(tb), dk - tn - dd
    elif mode == 2:
        if -dd < to:
            return None
        lo, hi = tb - dd, dk - tn
    else:
        if dd != 0:
            return None
        lo, hi = int(tb), dk - tn
    return (lo, hi) if lo <= hi else None


def start_ok(mode, k, c1, c2, bx):
    s1lo, s1hi, s2lo, s2hi = bx[0], bx[1], bx[2], bx[3]
    for c20 in range(max(s2lo, c2 - k), min(s2hi, c2) + 1):
        r = d1_range(mode, k, c2 - c20, None)
        if r and max(s1lo, c1 - r[1]) <= min(s1hi, c1 - r[0]):
            return True
    return False


def end_points(mode, dk, c1, c2, t, bx):
    """End points (c1w, c2w) in the end box reachable in dk steps whose first step has type t."""
    out = []
    c1wlo, c1whi, c2wlo, c2whi = bx[4], bx[5], bx[6], bx[7]
    for c2w in range(max(c2wlo, c2), min(c2whi, c2 + dk) + 1):
        r = d1_range(mode, dk, c2w - c2, t)
        if r:
            for c1w in range(max(c1wlo, c1 + r[0]), min(c1whi, c1 + r[1]) + 1):
                out.append((c1w, c2w))
    return out


def end_ok(mode, dk, c1, c2, t, bx):
    c1wlo, c1whi, c2wlo, c2whi = bx[4], bx[5], bx[6], bx[7]
    for c2w in range(max(c2wlo, c2), min(c2whi, c2 + dk) + 1):
        r = d1_range(mode, dk, c2w - c2, t)
        if r and max(c1wlo, c1 + r[0]) <= min(c1whi, c1 + r[1]):
            return True
    return False


def _cdiv(x, y):
    return -((-x) // y)


def make_box(w, h1, h2, S1, S2, E1, E2):
    """Start/end box for drift coordinates, or None if the T1 or T2 side cannot close."""
    bx = (S1[0], S1[1], S2[0], S2[1],
          N1 - E1[1] - h1 * w, N1 - E1[0] - h1 * w, N2 - E2[1] - h2 * w, N2 - E2[0] - h2 * w)
    if bx[5] < bx[0] or bx[4] > bx[1] + w or bx[7] < bx[2] or bx[6] > bx[3] + w:
        return None
    return bx


def _bands(w, k, bx):
    return (max(bx[0], bx[4] - (w - k)), min(bx[1] + k, bx[5]),
            max(bx[2], bx[6] - (w - k)), min(bx[3] + k, bx[7]))


# ------------------------------------------------------------------ relaxation (upper bound)
def bound(runs, w, h1, h2, mode, bx, DR, bottoms):
    """Longest chain in a DAG whose nodes and edges are necessary conditions of the exact model.
    mode 1 or 2: top alignment, dr anywhere in DR. mode 0: top (dr in DR) or bottom (offset H)."""
    H = h1 - h2
    kinds = (0, 1) if (mode == 0 and bottoms) else (0,)
    nodes = []
    for idx, (a, b, L) in enumerate(runs):
        rmax, pmax = h2 + 1 - L, h1 + 1 - L
        if rmax < 0:
            continue
        d = a - b
        klo = max(0, _cdiv(b - rmax - bx[7], h2), _cdiv(a - pmax - bx[5], h1))
        khi = min(w - 1, (b - bx[2]) // h2, (a - bx[0]) // h1)
        for k in range(klo, khi + 1):
            C1lo, C1hi, C2lo, C2hi = _bands(w, k, bx)
            c2lo, c2hi = max(b - k * h2 - rmax, C2lo), min(b - k * h2, C2hi)
            c1lo, c1hi = max(a - k * h1 - pmax, C1lo), min(a - k * h1, C1hi)
            if c2lo > c2hi or c1lo > c1hi:
                continue
            for kind in kinds:
                if kind == 0:
                    elo, ehi = d - k * H - DR[1], d - k * H - DR[0]
                else:
                    elo = ehi = d - k * H - H
                if max(elo, c1lo - c2hi) <= min(ehi, c1hi - c2lo):
                    nodes.append((k, b, a, idx, L, kind))
    if not nodes:
        return 0
    nodes.sort()
    n = len(nodes)
    best = [1] * n
    top = 1
    for j in range(n):
        kj, bj, aj, ij, Lj, uj = nodes[j]
        for i in range(j):
            if best[i] + 1 <= best[j]:
                continue
            ki, bi, ai, ii, Li, ui = nodes[i]
            if ii == ij:
                continue
            dk = kj - ki
            dd0 = (aj - bj) - (ai - bi) - dk * H
            # admissible dd values: top-top / bottom-bottom: dd0; mixed: dd0 -/+ (H - dr)
            if ui == uj:
                dds = [(dd0, dd0)]
            elif ui == 0:   # top -> bottom: o_j - o_i = H - dr
                dds = [(dd0 - H + DR[0], dd0 - H + DR[1])]
            else:           # bottom -> top: o_j - o_i = dr - H
                dds = [(dd0 + H - DR[1], dd0 + H - DR[0])]
            lo_dd, hi_dd = dds[0]
            emin, emax = -(h2 + 1 - Li), h2 + 1 - Lj
            ok = False
            if dk == 0:
                if lo_dd <= 0 <= hi_dd and emin <= bj - bi <= emax:
                    ok = True
            else:
                if mode == 1:
                    lo_dd = max(lo_dd, 0); hi_dd = min(hi_dd, dk)
                    if lo_dd <= hi_dd:
                        g = (0, dk - lo_dd)
                        ok = True
                elif mode == 2:
                    lo_dd = max(lo_dd, -dk); hi_dd = min(hi_dd, 0)
                    if lo_dd <= hi_dd:
                        g = (-hi_dd, dk)
                        ok = True
                else:
                    if lo_dd <= 0 <= hi_dd:
                        g = (0, dk)
                        ok = True
                if ok:
                    base = bj - bi - dk * h2           # eps = base - d2, eps in [emin, emax]
                    ok = max(g[0], base - emax) <= min(g[1], base - emin)
            if ok:
                best[j] = best[i] + 1
                if best[j] > top:
                    top = best[j]
    return top


# ------------------------------------------------------------------ exact chain DP
def dp(runs, w, h1, h2, mode, offs, bx, target=None, want_chain=False):
    """Exact longest consistent chain for one (w, h1, h2, mode, offsets) and box.
    offs: row offsets allowed for this pass, e.g. (dr,) or (dr, h1 - h2) for the bottoms variant.
    Returns (best, chain, ends): chain = [(run index, rank, type, offset)] for one optimum (if asked);
    ends = sorted end points (c1w, c2w) reachable by some chain of length >= target (if target given)."""
    H = h1 - h2
    ev = []
    for idx, (a, b, L) in enumerate(runs):
        d = a - b
        for o in offs:
            for t in TYPES[mode]:
                l1, l2 = LEN[(mode, t)]
                rlo = -o if o < 0 else 0
                rhi = min(h2 + l2 - L, h1 + l1 - L - o)
                if rlo > rhi:
                    continue
                klo = max(0, _cdiv(b - rhi - bx[7], h2), _cdiv(a - rhi - o - bx[5], h1))
                khi = min(w - 1, (b - rlo - bx[2]) // h2, (a - rlo - o - bx[0]) // h1)
                for k in range(klo, khi + 1):
                    C1lo, C1hi, C2lo, C2hi = _bands(w, k, bx)
                    de = d - k * H - o
                    lo = max(b - k * h2 - rhi, C2lo, C1lo - de)
                    hi = min(b - k * h2 - rlo, C2hi, C1hi - de)
                    if lo <= hi:
                        ev.append((k, b, idx, t, o, de, lo, hi))
    if not ev:
        return 0, [], []
    ev.sort()
    n = len(ev)
    vals, pred = [], []
    for (k, b, idx, t, o, de, lo, hi) in ev:
        vals.append([1 if start_ok(mode, k, de + v, v, bx) else 0 for v in range(lo, hi + 1)])
        pred.append([None] * (hi - lo + 1))
    for j in range(n):
        kj, bj, ij, tj, oj, dj, loj, hij = ev[j]
        vj, pj = vals[j], pred[j]
        for i in range(j):
            ki, bi, ii, ti, oi, di, loi, hii = ev[i]
            if ii == ij:
                continue
            vi = vals[i]
            if ki == kj:
                if di != dj or ti != tj:
                    continue
                for v in range(max(loi, loj), min(hii, hij) + 1):
                    x = vi[v - loi]
                    if x and x + 1 > vj[v - loj]:
                        vj[v - loj] = x + 1; pj[v - loj] = (i, v)
                continue
            rng = seg_range(mode, kj - ki, dj - di, ti)
            if rng is None:
                continue
            glo, ghi = rng
            for v in range(loj, hij + 1):
                lo_, hi_ = max(loi, v - ghi), min(hii, v - glo)
                if lo_ > hi_:
                    continue
                seg = vi[lo_ - loi: hi_ - loi + 1]
                m = max(seg)
                if m and m + 1 > vj[v - loj]:
                    vj[v - loj] = m + 1; pj[v - loj] = (i, lo_ + seg.index(m))
    best, arg, ends = 0, None, set()
    for j in range(n):
        k, b, idx, t, o, de, lo, hi = ev[j]
        vj = vals[j]
        for v in range(lo, hi + 1):
            x = vj[v - lo]
            if x == 0:
                continue
            if target is not None and x >= target:
                pts = end_points(mode, w - k, de + v, v, t, bx)
                ends.update(pts)
                if pts and x > best:
                    best, arg = x, (j, v)
            elif x > best and end_ok(mode, w - k, de + v, v, t, bx):
                best, arg = x, (j, v)
    chain = []
    if want_chain and arg is not None:
        j, v = arg
        while j is not None:
            k, b, idx, t, o, de, lo, hi = ev[j]
            chain.append((idx, k, t, o))
            p = pred[j][v - lo]
            j, v = (p if p else (None, None))
        chain.reverse()
    return best, chain, sorted(ends)


# ------------------------------------------------------------------ driver
def search(runs, W=(5, 60), S1=(0, 20), S2=(0, 20), E1=(0, 20), E2=(0, 20), DR=(-10, 10),
           bottoms=False, collect=False, want_chain=False, stats=None, nobound=False):
    """Best count over all geometries. runs: [(a, b, len)].
    collect: also return every (w, h1, h2, mode, dr) pass that reaches the best, with a witness chain.
    bottoms: also allow shared-closing runs (mode 0 passes with offsets (dr, h1 - h2)).
    nobound: skip the relaxation and run the exact DP on every pass (used to check the pruning)."""
    best, hits = 0, []
    if not runs:
        return 0, []
    Lmin1, Lmax1 = N1 - S1[1] - E1[1], N1 - S1[0] - E1[0]
    Lmin2, Lmax2 = N2 - S2[1] - E2[1], N2 - S2[0] - E2[0]
    modes = (1, 2, 0) if bottoms else (1, 2)
    for w in range(W[0], W[1] + 1):
        for h1 in range(max(1, Lmin1 // w - 1), Lmax1 // w + 1):
            for h2 in range(max(1, Lmin2 // w - 1), Lmax2 // w + 1):
                bx = make_box(w, h1, h2, S1, S2, E1, E2)
                if bx is None:
                    continue
                H = h1 - h2
                for mode in modes:
                    bnd = len(runs) if nobound else bound(runs, w, h1, h2, mode, bx, DR, bottoms)
                    if stats is not None:
                        stats["bound"] = stats.get("bound", 0) + 1
                    if bnd < best or (bnd == best and not collect) or bnd == 0:
                        continue
                    for dr in range(DR[0], DR[1] + 1):
                        offs = (dr, H) if (mode == 0 and H != dr) else (dr,)
                        if stats is not None:
                            stats["dp"] = stats.get("dp", 0) + 1
                        v, chain, _ = dp(runs, w, h1, h2, mode, offs, bx, want_chain=want_chain or collect)
                        if v > best:
                            best, hits = v, []
                        if v == best and v > 0 and (collect or not hits):
                            hits.append((w, h1, h2, mode, dr, chain))
                        if v >= bnd and not collect:
                            break
    return best, hits


def geometries(runs, hit, best, S1=(0, 20), S2=(0, 20), E1=(0, 20), E2=(0, 20)):
    """Every (w, s1, s2, e1, e2, dr) of one hit pass that reaches `best`."""
    w, h1, h2, mode, dr, _ = hit
    H = h1 - h2
    offs = (dr, H) if (mode == 0 and H != dr) else (dr,)
    out = set()
    for s1 in range(S1[0], S1[1] + 1):
        for s2 in range(S2[0], S2[1] + 1):
            bx = make_box(w, h1, h2, (s1, s1), (s2, s2), E1, E2)
            if bx is None:
                continue
            v, _, ends = dp(runs, w, h1, h2, mode, offs, bx, target=best)
            for c1w, c2w in ends:
                out.add((w, s1, s2, N1 - h1 * w - c1w, N2 - h2 * w - c2w, dr))
    return out

"""v2_soft: v1_free's beam reading, then soft passes with the SAME tying, in a corridor round the beam's path.

align.build_abridged follows its beam with forward-backward passes in which every sign has its own value, so
`x+4` and `x+3` share nothing. Here the passes use a table in which a base with a vowel mark spells
consonant(base) + vowel(mark): each base and each mark is learnt from all its places. An unmarked sign, and
any sign that never takes a vowel mark, has its own value as in align (0-3 letters or a word).
The corridor is BAND letters each side of the path (align uses 15), and the last unit need not sit on the last
letter of the plain text: an end unit after the last sign takes the letters left over at no cost.
Rows are marked by evidence on the last best path: hits and misses of each base, mark and sign against the
chance that its value turns up anyway.
"""
import math, os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "..", "line"))
import align, tied, v1_free  # noqa: E402

BAND = 40
ITERS, ROUNDS, SETTLE = 6, 8, 0.2
EPS = 0.05            # share of a marked sign's places that do not spell consonant + vowel
SEED = {"certain": 6.0, "probable": 3.0, "unknown": 1.0}
CONS = "bcdfghlmnpqrstxz"
VOW = "aeiou"


class TiedTable(align.Table):
    """align.Table with the emission of a marked sign tied: p(cv | base+mark) = p(c | base) p(v | mark)."""

    def __init__(self, mk):
        super().__init__()
        self.mk = mk
        self.cb = defaultdict(lambda: defaultdict(float))
        self.cm = defaultdict(lambda: defaultdict(float))
        self.tb, self.tm = defaultdict(float), defaultdict(float)
        self._parts = {}

    def parts(self, sym):
        p = self._parts.get(sym)
        if p is None:
            p = self._parts[sym] = tied.parts(sym, self.mk)
        return p

    def add(self, sym, s, w, place=None):
        kind, a, b = self.parts(sym)
        if kind != "BM":
            return super().add(sym, s, w, place)
        if len(s) == 2 and s[0] not in VOW and s[1] in VOW:
            self.cb[a][s[0]] += w
            self.tb[a] += w
            self.cm[b][s[1]] += w
            self.tm[b] += w

    def seed(self, entry, value, w):
        k, name = entry[0], entry[2:]
        if k == "B":
            self.cb[name][value] += w
            self.tb[name] += w
        elif k == "M":
            self.cm[name][value] += w
            self.tm[name] += w
        else:
            for i in range(3):
                super().add(name, value, w / 3, i)

    def p(self, sym, s):
        k = (sym, s)
        v = self._cache.get(k)
        if v is not None:
            return v
        kind, a, b = self.parts(sym)
        if kind != "BM":
            return super().p(sym, s)
        v = EPS * align.prior(s)
        if len(s) == 2 and s[0] not in VOW and s[1] in VOW:
            pb = (self.cb[a].get(s[0], 0.0) + align.ALPHA / len(CONS)) / (self.tb.get(a, 0.0) + align.ALPHA)
            pm = (self.cm[b].get(s[1], 0.0) + align.ALPHA / len(VOW)) / (self.tm.get(b, 0.0) + align.ALPHA)
            v += (1 - EPS) * pb * pm
        self._cache[k] = v
        return v


class FreeEnd(align.GapSegment):
    """GapSegment whose last unit (kind 'end') takes whatever letters are left, at no cost: the plain side may
    run on after the cipher stops, and a beam that fell behind must not force the corridor shut."""

    def options(self, i, j, table):
        if self.units[i - 1].kind != "end":
            return super().options(i, j, table)
        if j != self.m:
            return []
        return [(j0, "", 1.0) for j0 in range(self.lo[i - 1], self.hi[i - 1] + 1)]


def chance(P):
    n = {}
    for ln in (1, 2, 3):
        for j in range(len(P) - ln + 1):
            n[P[j:j + ln]] = n.get(P[j:j + ln], 0) + 1
    return lambda v: min(0.5, 3.0 * n.get(v, 0) / len(P))


def status(h, x, pc, hit=tied.HIT):
    ev = h * math.log(hit / max(pc, 1e-4)) + x * math.log((1 - hit) / (1 - pc))
    return ("certain" if ev >= 10 and h >= 5 else "probable" if ev >= 4 and h >= 3 else "unknown"), ev


def tied_rows(path, P, mk):
    """rows B:, M:, W: from a best path [(unit, j0, j, span)], marked by evidence."""
    pc = chance(P)
    seen = defaultdict(lambda: defaultdict(int))
    places = defaultdict(int)
    for u, j0, j, s in path:
        if u.kind != "sign" or u.sym == "?" or s is None:
            continue
        kind, a, b = tied.parts(u.sym, mk)
        if kind == "BM":
            places["B:" + a] += 1
            places["M:" + b] += 1
            if len(s) == 2 and s[0] not in VOW and s[1] in VOW:
                seen["B:" + a][s[0]] += 1
                seen["M:" + b][s[1]] += 1
        else:
            places["W:" + u.sym] += 1
            seen["W:" + u.sym][s] += 1
    rows = []
    for k, vals in seen.items():
        v, h = max(vals.items(), key=lambda kv: (kv[1], kv[0]))
        x = places[k] - h
        if not v or len(v) > 3 and h < 2:
            continue
        st, ev = status(h, x, pc(v))
        rows.append(dict(unit=k, value=v, type=align.unit_type(v), support=h, conflict=x,
                         share=round(h / max(1, h + x), 3), status=st, alts=f"ev {ev:.1f}", positions=""))
    rows.sort(key=lambda r: (-r["support"], r["unit"]))
    return rows


def soften(units, P, wb, lac, mk, rows, centers, log, band=None):
    """soft passes from the table `rows` in a corridor round `centers` -> (rows, path)."""
    band = band or BAND
    old = align.P_LEN[0]
    align.P_LEN[0] = 0.0
    try:
        table = TiedTable(mk)
        for r in rows:
            table.seed(r["unit"], r["value"], SEED[r["status"]])
        path = None
        units = list(units) + [align.Unit("$", units[-1].line, units[-1].tok + 1, "end")]
        for rnd in range(ROUNDS):
            seg = FreeEnd(units, P, wb, lac, band, centers)
            for _ in range(ITERS):
                new = TiedTable(mk)
                z, g = seg.estep(table, new)
                table = new
            path, skipped = align.best_path([(0, 0, seg)], table)
            end = path[-1][1]
            path = path[:-1]
            moved = sum(abs(c - j0) for c, (u, j0, j, s) in zip(centers, path)) / max(1, len(path))
            log(f"round {rnd + 1}: ll per unit {z / len(units):.3f}; units in gaps "
                f"{sum(1 for u, a, b, s in path if s is None)}; path moved {moved:.1f} letters a unit")
            centers = [float(j0) for u, j0, j, s in path] + [float(end), float(len(P))]
            if moved < SETTLE:
                break
        log(f"last sign ends at letter {end} of {len(P)}")
        return tied_rows(path, P, mk), path
    finally:
        align.P_LEN[0] = old


def marked_kinds(rows):
    st = {}
    for r in rows:
        if r["status"] != "unknown":
            st[r["unit"][0]] = st.get(r["unit"][0], 0) + 1
    return st


def build(cipher, plain, log):
    units, P, wb, lac, _ = align.load_pair(cipher, plain)
    old = tied.BARE_FREE[0]
    tied.BARE_FREE[0] = True
    try:
        mk = tied.markable(units)
        known = {}
        for k in range(tied.PASSES):
            score, tab, ops = tied.search(units, P, lac, mk, known)
            rows = tied.rows_from(P, tab, ops)
            known = {r["unit"]: r["value"] for r in rows if r["status"] == "certain"}
        log(f"beam: score {score:.1f}; pointer ends at {ops[-1][2]} of {len(P)}; marked {marked_kinds(rows)}")
        centers = [float(o[1]) for o in ops] + [float(ops[-1][2]), float(len(P))]
        rows, path = soften(units, P, wb, lac, mk, rows, centers, log)
        log(f"soft: marked {marked_kinds(rows)}")
        return v1_free.sign_rows(rows, mk, units)
    finally:
        tied.BARE_FREE[0] = old

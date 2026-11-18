"""align.py - build a key table from a pair (cipher transcription + period decipherment), test it, decode with it.

    python3 align.py build   <cipher.txt> <plain.txt> --out key-v0.tsv [--aligned aligned.txt] [--abridged]
    python3 align.py heldout <cipher.txt> <plain.txt> [--folds 5] [--perms 20] [--out heldout.tsv]
    python3 align.py decode  <cipher.txt> <key.tsv> [--min probable]

Formats.
Cipher file: one manuscript line per row; '#' starts a comment row; tokens are separated by spaces.
  token     base[:after][^above...]   e.g. 25  25:curl  20:hook^v  -> units '25', ':curl', '^v'
            a trailing '?' marks doubt (kept); 'a|b' takes a; a bare '?' is an unread sign
  [[text]]  clear text written in the cipher letter
  @name     anchor; the same '@name' in the plain file ties the two positions
Plain file: running text. '@name' anchors. '[...]' or '[…]' marks a lacuna. Other brackets are dropped,
their letters kept. Letters are lower-cased, accents stripped, v->u and j->i merged (--no-merge turns that off).

Method. Each unit emits 0-3 plaintext letters, or one to three whole words (a code). A banded
forward-backward pass over (units x letters) gives expected counts unit -> span; the counts become the
emission table; repeat. A code span counts only for the support it has beyond its single best
place in the plaintext, so a span seen in one place is worth nothing (without this, every sign drifts to null and a few
rare signs swallow whole phrases: the failure of the first real calibration run). The final table comes from the best single path (Viterbi). No value is typed in
by hand: anchors are positions, never values.
"""
import argparse, math, random, re, sys, unicodedata
from collections import defaultdict

MAXLEN = 3            # longest letter/syllable span
WORD_MAX = 26         # longest code span, letters
WORD_MAXWORDS = 3
SKIP = 0.02           # a plaintext letter no unit accounts for
ALPHA = 0.5           # smoothing weight of the prior
P_LEN = {0: 0.04, 1: 0.56, 2: 0.25, 3: 0.10}
P_WORD = 0.05
NLET = 21.0
WORDS_FROM = 0        # training pass at which code-length spans are switched on


# ---------------------------------------------------------------- parsing
def norm_letters(s, merge=True):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("ß", "ss").replace("æ", "ae").replace("œ", "oe")
    if merge:
        s = s.replace("v", "u").replace("j", "i")
    return re.sub(r"[^a-z]", "", s)


def split_token(tok):
    """'20:hook^v^bar?' -> (['20', ':hook', '^v', '^bar'], doubt)."""
    doubt = tok.endswith("?") and tok != "?"
    t = tok.rstrip("?") if tok != "?" else "?"
    if "|" in t:
        t, doubt = t.split("|")[0], True
    if t in ("", "?"):
        return ["?"], True
    m = re.match(r"^([^:^]+)((?::[^:^]+)?)((?:\^[^:^]+)*)$", t)
    if not m:
        return [t], doubt
    units = [m.group(1)]
    if m.group(2):
        units.append(m.group(2))
    units += re.findall(r"\^[^:^]+", m.group(3))
    return units, doubt


class Unit:
    __slots__ = ("sym", "line", "tok", "kind", "text", "doubt", "raw")

    def __init__(self, sym, line, tok, kind="sign", text="", doubt=False, raw=""):
        self.sym, self.line, self.tok, self.kind, self.text, self.doubt, self.raw = sym, line, tok, kind, text, doubt, raw


def parse_cipher(text, merge=True):
    """-> (units, anchors{name: unit index}, nlines). Line numbers count non-comment rows from 1."""
    units, anchors, ln, tk = [], {}, 0, 0
    for row in text.splitlines():
        if not row.strip() or row.lstrip().startswith("#"):
            continue
        ln += 1
        for part in re.split(r"(\[\[.*?\]\])", row):
            if part.startswith("[["):
                for w in part[2:-2].split():
                    n = norm_letters(w, merge)
                    if n:
                        units.append(Unit("[[" + n + "]]", ln, tk, "clear", n, raw=w))
                        tk += 1
                continue
            for tok in part.split():
                if tok.startswith("@"):
                    anchors[tok] = len(units)
                    continue
                syms, doubt = split_token(tok)
                for s in syms:
                    units.append(Unit(s, ln, tk, "sign", doubt=doubt, raw=tok))
                tk += 1
    return units, anchors, ln


def parse_plain(text, merge=True):
    """-> (letters, wb, lac, anchors{name: letter index}). wb[j]: boundary j is a word boundary."""
    letters, wb_at, lac_at, anchors = [], {0}, set(), {}
    text = re.sub(r"(?m)^#.*$", " ", text)
    for piece in re.split(r"(\[(?:\.\.\.|…)[^\]]*\]|@\w[\w.-]*|\s+)", text):
        if not piece:
            continue
        if piece.startswith("@"):
            anchors[piece] = len(letters)
            wb_at.add(len(letters))
        elif re.match(r"\[(?:\.\.\.|…)", piece):
            lac_at.add(len(letters))
            wb_at.add(len(letters))
        elif piece.isspace():
            wb_at.add(len(letters))
        else:
            for sub in re.split(r"([^\w\[\]'’]+)", piece):
                n = norm_letters(sub, merge)
                if n:
                    letters.extend(n)
                else:
                    wb_at.add(len(letters))
    m = len(letters)
    wb_at.add(m)
    wb = [j in wb_at for j in range(m + 1)]
    lac = [j in lac_at for j in range(m + 1)]
    return "".join(letters), wb, lac, anchors


# ---------------------------------------------------------------- model
def prior(s):
    n = len(s)
    if n <= MAXLEN:
        return P_LEN[n] / (NLET ** n)
    return P_WORD / (NLET ** n)


class Table:
    def __init__(self):
        self.cnt = defaultdict(lambda: defaultdict(float))
        self.tot = defaultdict(float)
        self._cache = {}
        self.mx = {}           # (sym, code span) -> {place in the plaintext: weight}
        self.words = True      # False: no code-length spans (first phase of training)

    def add(self, sym, s, w, place=None):
        self.cnt[sym][s] += w
        self.tot[sym] += w
        if len(s) > MAXLEN:
            d = self.mx.setdefault((sym, s), {})
            d[place] = d.get(place, 0.0) + w

    def p(self, sym, s):
        k = (sym, s)
        v = self._cache.get(k)
        if v is None:
            if sym == "?":
                v = prior(s)
            else:
                c = self.cnt[sym].get(s, 0.0)
                if len(s) > MAXLEN and c:          # a code span counts only beyond its best single place
                    c = max(0.0, c - max(self.mx[(sym, s)].values()))
                v = (c + ALPHA * prior(s)) / (self.tot.get(sym, 0.0) + ALPHA)
            self._cache[k] = v
        return v


def clear_p(text, span):
    """A clear word either is absent from the decipherment or appears as (nearly) itself."""
    if not span:
        return 0.3
    if abs(len(span) - len(text)) > 1:
        return 0.0
    return 0.7 * math.exp(-1.6 * edit(text, span)) * (0.8 if len(span) == len(text) else 0.1)


def edit(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


class Segment:
    """Units a..b against letters c..d, both ends fixed."""

    def __init__(self, units, P, wb, lac, band=None, centers=None):
        self.units, self.P, self.wb, self.lac = units, P, wb, lac
        n, m = len(units), len(P)
        self.n, self.m = n, m
        w = band if band is not None else max(30, int(7 * math.sqrt(n + 1)))
        self.lo, self.hi = [0] * (n + 1), [0] * (n + 1)
        for i in range(n + 1):
            c = centers[i] if centers else (i * m / n if n else 0)
            self.lo[i] = max(0, int(c - w))
            self.hi[i] = min(m, int(c + w))
        self.lo[0] = 0
        self.lo[n], self.hi[n] = m, m
        for i in range(1, n + 1):             # monotone
            self.lo[i] = max(self.lo[i], self.lo[i - 1])
        for i in range(n - 1, -1, -1):
            self.hi[i] = min(self.hi[i], self.hi[i + 1])
        for i in range(n + 1):
            if self.lo[i] > self.hi[i]:
                self.lo[i] = self.hi[i]
        # word starts reachable from each word-end boundary
        self.wstarts = {}
        bounds = [j for j in range(m + 1) if wb[j]]
        for bi, j in enumerate(bounds):
            self.wstarts[j] = [j0 for j0 in bounds[max(0, bi - WORD_MAXWORDS):bi] if MAXLEN < j - j0 <= WORD_MAX]

    def options(self, i, j, table):
        """Emissions of unit i (1-based) ending at boundary j: list of (j0, span, prob)."""
        u = self.units[i - 1]
        lo, hi, P = self.lo[i - 1], self.hi[i - 1], self.P
        out = []
        if u.kind == "clear":
            for ln in sorted({0, len(u.text) - 1, len(u.text), len(u.text) + 1}):
                j0 = j - ln
                if ln >= 0 and lo <= j0 <= hi:
                    p = clear_p(u.text, P[j0:j])
                    if p > 0:
                        out.append((j0, P[j0:j], p))
            return out
        for ln in range(0, MAXLEN + 1):
            j0 = j - ln
            if j0 < lo:
                break
            if j0 <= hi:
                s = P[j0:j]
                out.append((j0, s, table.p(u.sym, s)))
        if u.sym != "?" and table.words:
            for j0 in self.wstarts.get(j, ()):
                if lo <= j0 <= hi:
                    s = P[j0:j]
                    out.append((j0, s, table.p(u.sym, s)))
        if self.lac[j] and lo <= j <= hi:      # unit lost in a lacuna of the plaintext
            out.append((j, None, 0.5))
        return out

    def estep(self, table, new):
        n, lo, hi = self.n, self.lo, self.hi
        A = [[0.0] * (hi[i] - lo[i] + 1) for i in range(n + 1)]
        A[0][0] = 1.0
        for j in range(lo[0] + 1, hi[0] + 1):
            A[0][j - lo[0]] = A[0][j - 1 - lo[0]] * SKIP
        opts = [None] * (n + 1)
        ll = 0.0
        for i in range(1, n + 1):
            row, prev, plo, l = A[i], A[i - 1], lo[i - 1], lo[i]
            ro = []
            for j in range(l, hi[i] + 1):
                o = self.options(i, j, table)
                ro.append(o)
                t = 0.0
                for j0, s, p in o:
                    t += prev[j0 - plo] * p
                if j > l:
                    t += row[j - 1 - l] * SKIP
                row[j - l] = t
            opts[i] = ro
            z = sum(row)
            if z <= 0:
                raise ValueError(f"alignment band lost at unit {i}; widen --band or add anchors")
            ll += math.log(z)
            inv = 1.0 / z
            for k in range(len(row)):
                row[k] *= inv
        B = [[0.0] * (hi[i] - lo[i] + 1) for i in range(n + 1)]
        B[n][0] = 1.0
        centers = [0.0] * (n + 1)
        centers[n] = float(self.m)
        for i in range(n, 0, -1):
            row, l = B[i], lo[i]
            for j in range(hi[i] - 1, l - 1, -1):          # skips inside row i
                row[j - l] += row[j + 1 - l] * SKIP
            prev, plo = B[i - 1], lo[i - 1]
            a_prev = A[i - 1]
            u = self.units[i - 1]
            post, z, cen = [], 0.0, 0.0
            for j in range(l, hi[i] + 1):
                b = row[j - l]
                if b == 0.0:
                    continue
                for j0, s, p in opts[i][j - l]:
                    prev[j0 - plo] += p * b
                    g = a_prev[j0 - plo] * p * b
                    if g > 0:
                        post.append((s, g, j0))
                        z += g
            if z > 0:
                for s, g, j0 in post:
                    w = g / z
                    cen += w * j0
                    if s is not None and u.kind == "sign" and u.sym != "?":
                        new.add(u.sym, s, w, (id(self), j0))
            centers[i - 1] = cen
            zz = sum(prev)
            if zz > 0:
                inv = 1.0 / zz
                for k in range(len(prev)):
                    prev[k] *= inv
        return ll, centers

    def viterbi(self, table):
        n, lo, hi = self.n, self.lo, self.hi
        NEG = -1e300
        V = [[NEG] * (hi[i] - lo[i] + 1) for i in range(n + 1)]
        bp = [[None] * (hi[i] - lo[i] + 1) for i in range(n + 1)]
        lskip = math.log(SKIP)
        V[0][0] = 0.0
        for j in range(lo[0] + 1, hi[0] + 1):
            V[0][j - lo[0]] = V[0][j - 1 - lo[0]] + lskip
            bp[0][j - lo[0]] = "skip"
        for i in range(1, n + 1):
            row, prev, plo, l = V[i], V[i - 1], lo[i - 1], lo[i]
            for j in range(l, hi[i] + 1):
                best, arg = NEG, None
                for j0, s, p in self.options(i, j, table):
                    v = prev[j0 - plo]
                    if v > NEG and p > 0:
                        v += math.log(p)
                        if v > best:
                            best, arg = v, (j0, s)
                if j > l and row[j - 1 - l] + lskip > best:
                    best, arg = row[j - 1 - l] + lskip, "skip"
                row[j - l], bp[i][j - l] = best, arg
        spans = [None] * n
        i, j = n, self.m
        skipped = []
        while i > 0 or j > 0:
            b = bp[i][j - lo[i]]
            if b is None:
                raise ValueError("no path; widen --band or add anchors")
            if b == "skip":
                skipped.append(j - 1)
                j -= 1
            else:
                spans[i - 1] = (b[0], j, b[1])
                i, j = i - 1, b[0]
        return spans, skipped


def make_segments(units, P, wb, lac, pairs, band=None):
    """pairs: sorted (unit index, letter index) ties, including (0,0) and (n,m)."""
    segs = []
    for (a, c), (b, d) in zip(pairs, pairs[1:]):
        if b > a:                              # letters between two ties with no unit stay unaccounted
            segs.append((a, c, Segment(units[a:b], P[c:d], wb[c:d + 1], lac[c:d + 1], band)))
    return segs


def tie_pairs(units, P, c_anch, p_anch):
    pairs = {(0, 0), (len(units), len(P))}
    for name, ui in c_anch.items():
        if name in p_anch:
            pairs.add((ui, p_anch[name]))
    pairs = sorted(pairs)
    for (a, c), (b, d) in zip(pairs, pairs[1:]):
        if b < a or d < c:
            raise ValueError(f"anchors out of order near unit {a}/{b}")
    return pairs


def train(segs, iters=12, log=None, start=None, merge=True):
    table = start or Table()
    for it in range(iters):
        table.words = it >= WORDS_FROM
        new, ll = Table(), 0.0
        for k, (a, c, seg) in enumerate(segs):
            try:
                l, centers = seg.estep(table, new)
            except ValueError:                  # a narrowed band lost the path: go back to the wide one
                seg = Segment(seg.units, seg.P, seg.wb, seg.lac)
                segs[k] = (a, c, seg)
                l, centers = seg.estep(table, new)
            ll += l
            if it >= 4 and seg.n > 60:          # narrow the band round the current path
                w = max(40, int((seg.hi[seg.n // 2] - seg.lo[seg.n // 2]) / 2 * 0.7))
                segs[k] = (a, c, Segment(seg.units, seg.P, seg.wb, seg.lac, w, centers))
        table = new
        if log:
            log(f"iter {it + 1}: log-likelihood {ll:.1f}")
    table.words = True
    if merge:
        for _ in range(3):                      # a kept proposal frees letters for the next one
            table, ll, kept = merge_codes(segs, table, ll, log)
            if not kept:
                break
    return table


def merge_codes(segs, table, ll, log=None):
    """A code sign and a mark on it can split one word between them ('madre' as mad + re), and the
    passes do not leave that state by themselves. Propose: a sign that sits inside the same longer word
    at two places or more, and at 60% of its places, stands for that word. Keep the proposal only if
    the log-likelihood after four more passes is higher."""
    path, _ = best_path(segs, table)
    off = {id(seg): c for a, c, seg in segs}
    inside = defaultdict(lambda: defaultdict(set))
    occ = defaultdict(int)
    k = 0
    for a, c, seg in segs:
        for u in seg.units:
            _, j0, j, s = path[k]
            k += 1
            if u.kind != "sign" or u.sym == "?":
                continue
            occ[u.sym] += 1
            if not s or len(s) > MAXLEN:
                continue
            lo, hi = j0 - c, j - c
            while lo > 0 and not seg.wb[lo]:
                lo -= 1
            while hi < seg.m and not seg.wb[hi]:
                hi += 1
            if any(seg.wb[x] for x in range(j0 - c + 1, j - c)):
                continue                                   # the span crosses a word boundary
            if MAXLEN < hi - lo <= WORD_MAX:
                inside[u.sym][seg.P[lo:hi]].add((id(seg), lo))
    props = {}
    for sym, words in inside.items():
        w, places = max(words.items(), key=lambda kv: len(kv[1]))
        if len(places) >= 2 and len(places) >= 0.6 * occ[sym]:
            props[sym] = (w, len(places))
    if not props:
        return table, ll, False
    trial = Table()
    for sym, vals in table.cnt.items():
        if sym in props:
            w, n = props[sym]
            for i in range(n):
                trial.add(sym, w, 1.0, i)
        else:
            for v, c in vals.items():
                trial.add(sym, v, c, None)
            for (s2, v), d in table.mx.items():
                if s2 == sym:
                    trial.mx[(s2, v)] = dict(d)
    ll2 = None
    for _ in range(4):
        new, ll2 = Table(), 0.0
        for a, c, seg in segs:
            l, _ = seg.estep(trial, new)
            ll2 += l
        trial = new
    if log:
        log(f"code proposals {props}: log-likelihood {ll:.1f} -> {ll2:.1f} ({'kept' if ll2 > ll else 'dropped'})")
    return (trial, ll2, True) if ll2 > ll else (table, ll, False)


def best_path(segs, table):
    """-> list of (unit, j0, j, span) over the whole pair, and skipped letter indices."""
    out, skipped = [], []
    for a, c, seg in segs:
        spans, sk = seg.viterbi(table)
        for u, sp in zip(seg.units, spans):
            out.append((u, c + sp[0], c + sp[1], sp[2]))
        skipped += [c + x for x in sk]
    return out, skipped


# ---------------------------------------------------------------- key table
def unit_type(v):
    return "null" if v == "" else "letter" if len(v) == 1 else "syllable" if len(v) <= MAXLEN else "word"


def key_from_path(path, skipped=()):
    """Rows: dict(unit, value, type, support, conflict, share, status, alts, positions).
    A value whose places mostly touch plaintext letters that no unit accounts for is a piece of
    something longer (a code met in varying spellings); it stays unknown."""
    sk = set(skipped)
    by = defaultdict(lambda: defaultdict(list))
    ragged = defaultdict(lambda: defaultdict(int))
    for u, j0, j, s in path:
        if u.kind == "sign" and u.sym != "?" and s is not None:
            by[u.sym][s].append(f"{u.line}")
            if s and ((j0 - 1) in sk or j in sk):
                ragged[u.sym][s] += 1
    rows = []
    for sym, vals in by.items():
        ranked = sorted(vals.items(), key=lambda kv: (-len(kv[1]), kv[0]))
        v, pos = ranked[0]
        total = sum(len(p) for _, p in ranked)
        sup = len(pos)
        share = sup / total
        status = "certain" if sup >= 5 and share >= 0.8 else "probable" if sup >= 4 and share >= 0.6 else "unknown"
        if ragged[sym][v] * 2 >= sup:
            status = "unknown"
        alts = " ".join(f"{a or '∅'}×{len(p)}" for a, p in ranked[1:4])
        rows.append(dict(unit=sym, value=v, type=unit_type(v), support=sup, conflict=total - sup,
                         share=round(share, 3), status=status, alts=alts, positions=",".join(pos[:8])))
    rows.sort(key=lambda r: (-r["support"], r["unit"]))
    return rows


KEY_COLS = ["unit", "value", "type", "support", "conflict", "share", "status", "alts", "positions"]


def write_key(rows, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(KEY_COLS) + "\n")
        for r in rows:
            f.write("\t".join(str(r[c]) for c in KEY_COLS) + "\n")


def read_key(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        head = f.readline().rstrip("\n").split("\t")
        for line in f:
            if line.strip():
                r = dict(zip(head, line.rstrip("\n").split("\t")))
                r["support"], r["conflict"] = int(r["support"]), int(r["conflict"])
                rows.append(r)
    return rows


def key_map(rows, minimum="probable"):
    ok = {"certain"} if minimum == "certain" else {"certain", "probable"}
    return {r["unit"]: r["value"] for r in rows if r["status"] in ok}


def decode_units(units, kmap):
    """-> list of pieces, one per unit: a value, '' for a null, None for an unknown unit."""
    out = []
    for u in units:
        if u.kind == "clear":
            out.append("[" + u.text + "]")
        else:
            out.append(kmap.get(u.sym))
    return out


def render(units, pieces):
    lines, cur, ln = [], [], None
    for u, p in zip(units, pieces):
        if u.line != ln:
            if cur:
                lines.append((ln, "".join(cur)))
            cur, ln = [], u.line
        cur.append("?" if p is None else (" " + p + " " if p.startswith("[") else p))
    if cur:
        lines.append((ln, "".join(cur)))
    return lines


# ---------------------------------------------------------------- abridged pairs
# For a pair whose plain side leaves out stretches of the cipher and rewords the rest (no. 2911: Machiavelli's
# copy of the Dieci's letter). Developed on items/2911/bench (variants v7-v11); the record is its README.
# 1. beam_read: read the cipher in order with a pointer in the plain text, the table carried in each hypothesis.
# 2. GapSegment passes in a corridor round the beam's path, no null value, repeated until the path settles.
# 3. mark_by_evidence: a row is marked by hits and misses against the chance rate of its value.
NEG = float("-inf")
GAP_OPEN, GAP_EXT = -4.0, -4.0       # log cost of entering a gap and of each unit in it (the passes)
AB_BEAM, AB_PERJ = 4000, 40          # hypotheses kept per unit; of them at one pointer
AB_OPEN, AB_EXT, AB_MISS = 3.0, 0.1, 0.4   # the beam's costs, in letters: gap, unit in a gap, a miss
AB_DMAX = 2                          # plain letters that may be skipped before a known sign
AB_PASSES = 3                        # beam readings; each holds the certain rows of the one before
AB_BAND, AB_ITERS, AB_ROUNDS, AB_SETTLE = 15, 8, 12, 0.2
AB_HIT = 0.55                        # share of places where a right value spells a loose plain side
AB_CHANCE = {1: 0.08, 2: 0.015, 3: 0.003}
AB_VOWELS = set("aeiou")
AB_UNREAD = {1: 0.3, 2: 0.5, 0: 1.0}
AB_SEED = {"certain": 6.0, "probable": 3.0, "unknown": 1.0}
_log, _exp, _log1p = math.log, math.exp, math.log1p


def la(a, b):
    if a < b:
        a, b = b, a
    if b == NEG:
        return a
    return a + _log1p(_exp(b - a))


class GapSegment(Segment):
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
                    a, b = Mp[j - pl] + GAP_OPEN, Gp[j - pl] + GAP_EXT
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
                bm = la(E[k], g + GAP_OPEN) if g > NEG else E[k]
                if j < hi[i]:
                    bm = la(bm, BMi[k + 1] + lskip)
                BMi[k] = bm
                BGi[k] = la(E[k], g + GAP_EXT) if g > NEG else E[k]
                if g > NEG:
                    w1 = Mi[k] + GAP_OPEN + g - Z
                    w2 = Gi[k] + GAP_EXT + g - Z
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


def new_cost(v, inv):
    """Cost of giving a new sign the value v. Letters and open syllables are the common kinds."""
    if len(v) == 1:
        c = 0.0
    elif len(v) == 2:
        c = 0.2 if (v[0] not in AB_VOWELS and v[1] in AB_VOWELS) else 1.0
    else:
        c = 1.5
    return c + (0.7 if v in inv else 0.0)


def beam_read(units, P, lac, log=None, known=None):
    """-> (score, table, ops). ops[i] = (kind, j0, j1) for unit i; kind: M match, A assign, S other spelling,
    I no counterpart, G in a gap, Q unread, C clear word. known: a table to start from (signs fixed)."""
    m = len(P)
    start_tab = dict(known or {})
    start_inv = frozenset(start_tab.values())
    hyps = [(0.0, 0, 0, start_tab, start_inv, 0, None), (-AB_EXT, 0, 1, start_tab, start_inv, 0, None)]
    for i, u in enumerate(units):
        new = {}

        def put(sc, j, g, tab, inv, sig, hist):
            k = (j, g, sig)
            h = new.get(k)
            if h is None or sc > h[0]:
                new[k] = (sc, j, g, tab, inv, sig, hist)

        sym, kind = u.sym, u.kind
        for sc, j, g, tab, inv, sig, hist in hyps:
            if g:                                              # stay in the gap
                put(sc - AB_EXT, j, 1, tab, inv, sig, (hist, "G", j, j))
            if kind == "clear":
                t = u.text
                put(sc, j, 0, tab, inv, sig, (hist, "C", j, j))
                if P.startswith(t, j):
                    put(sc + len(t), j + len(t), 0, tab, inv, sig, (hist, "C", j, j + len(t)))
                continue
            if sym == "?":
                for ln, c in AB_UNREAD.items():
                    if j + ln <= m:
                        put(sc - c, j + ln, 0, tab, inv, sig, (hist, "Q", j, j + ln))
                if not g:
                    put(sc - AB_OPEN, j, 1, tab, inv, sig, (hist, "G", j, j))
                continue
            v = tab.get(sym)
            if v is not None:
                ln = len(v)
                hit = False
                for d in range(AB_DMAX + 1):
                    if P.startswith(v, j + d):
                        put(sc + ln - d * AB_MISS, j + d + ln, 0, tab, inv, sig, (hist, "M", j + d, j + d + ln))
                        hit = d == 0
                        break
                if hit:
                    continue
                if j + ln <= m:
                    put(sc - AB_MISS, j + ln, 0, tab, inv, sig, (hist, "S", j, j + ln))
                put(sc - AB_MISS, j, 0, tab, inv, sig, (hist, "I", j, j))
            else:
                for ln in (1, 2, 3):
                    if j + ln > m:
                        break
                    val = P[j:j + ln]
                    t2 = dict(tab)
                    t2[sym] = val
                    put(sc - new_cost(val, inv), j + ln, 0, t2, inv | {val}, sig ^ hash((sym, val)),
                        (hist, "A", j, j + ln))
                put(sc - AB_MISS, j, 0, tab, inv, sig, (hist, "I", j, j))
            if not g:
                put(sc - (1.0 if lac[j] else AB_OPEN), j, 1, tab, inv, sig, (hist, "G", j, j))
        ranked = sorted(new.values(), key=lambda h: -h[0])
        hyps, per = [], {}
        for h in ranked:
            c = per.get(h[1], 0)
            if c < AB_PERJ:
                per[h[1]] = c + 1
                hyps.append(h)
                if len(hyps) >= AB_BEAM:
                    break
        if log and (i + 1) % 200 == 0:
            b = hyps[0]
            log(f"unit {i + 1}: best score {b[0]:.1f} pointer {b[1]} of {m} table {len(b[3])} "
                f"{'in gap' if b[2] else ''}")
    best = hyps[0]
    ops, h = [], best[6]
    while h is not None:
        ops.append(h[1:])
        h = h[0]
    ops.reverse()
    return best[0], best[3], ops


def beam_rows(units, P, tab, ops, known=()):
    """Key rows with the support each value has on the path."""
    hit, miss, gap, first = {}, {}, {}, {s: "" for s in known}
    for u, (kind, j0, j1) in zip(units, ops):
        s = u.sym
        if u.kind != "sign" or s == "?":
            continue
        if kind == "M":
            hit[s] = hit.get(s, 0) + 1
        elif kind == "A":
            first[s] = u.line
        elif kind in ("S", "I"):
            if s in first:
                miss[s] = miss.get(s, 0) + 1
        else:
            gap[s] = gap.get(s, 0) + 1
    rows = []
    for s, v in tab.items():
        h, x = hit.get(s, 0), miss.get(s, 0)
        if s in known:                 # no first place on this path: every place had to spell the value
            h -= 1
        share = (h + 1) / max(1, h + 1 + x)
        pc = AB_CHANCE[min(3, len(v))]
        llr = h * math.log(AB_HIT / pc) + x * math.log((1 - AB_HIT) / (1 - pc))
        status = "certain" if llr >= 8 and h >= 3 else "probable" if llr >= 3.5 else "unknown"
        rows.append(dict(unit=s, value=v, type=unit_type(v), support=h + 1, conflict=x,
                         share=round(share, 3), status=status, alts=f"gap×{gap.get(s, 0)}",
                         positions=str(first.get(s, ""))))
    rows.sort(key=lambda r: (-r["support"], r["unit"]))
    return rows


def beam_summary(units, ops):
    c = {}
    for kind, j0, j1 in ops:
        c[kind] = c.get(kind, 0) + 1
    return " ".join(f"{k}={c[k]}" for k in sorted(c))


def mark_by_evidence(rows, P, cert=10.0, prob=4.0):
    """Mark rows of key_from_path by evidence against chance instead of by share. pc = 3 x the share of plain
    positions where the value stands (the path may choose among neighbouring places), capped at 0.5."""
    n = {}
    for ln in (1, 2, 3):
        for j in range(len(P) - ln + 1):
            s = P[j:j + ln]
            n[s] = n.get(s, 0) + 1
    for r in rows:
        v, h, x = r["value"], r["support"], r["conflict"]
        if not v or len(v) > 3:
            continue
        ragged = r["status"] == "unknown" and h >= 5 and r["share"] >= 0.8
        pc = min(0.5, 3.0 * n.get(v, 0) / len(P))
        ev = h * math.log(AB_HIT / pc) + x * math.log((1 - AB_HIT) / (1 - pc))
        r["status"] = ("unknown" if ragged else "certain" if ev >= cert and h >= 5
                       else "probable" if ev >= prob and h >= 3 else "unknown")
    return rows


def build_abridged(units, P, wb, lac, log=None):
    """-> key rows for a pair whose plain side is an abridgement. No null value is built."""
    global SKIP
    known = {}
    for _ in range(AB_PASSES):
        score_, tab, ops = beam_read(units, P, lac, None, known)
        rows = beam_rows(units, P, tab, ops, known)
        known = {r["unit"]: r["value"] for r in rows if r["status"] == "certain"}
    if log:
        log(f"beam: score {score_:.1f}; table {len(tab)} signs; path: {beam_summary(units, ops)}")
    centers = [float(j0) for kind, j0, j1 in ops] + [float(len(P))]
    old = P_LEN[0]
    P_LEN[0] = 0.0
    try:
        table = Table()
        for r in rows:
            for k in range(3):
                table.add(r["unit"], r["value"], AB_SEED[r["status"]] / 3, k)
        for rnd in range(AB_ROUNDS):
            seg = GapSegment(units, P, wb, lac, AB_BAND, centers)
            for _ in range(AB_ITERS):
                new = Table()
                z, g = seg.estep(table, new)
                table = new
            path, skipped = best_path([(0, 0, seg)], table)
            rows = key_from_path(path, skipped)
            moved = sum(abs(c - j0) for c, (u, j0, j, s) in zip(centers, path)) / max(1, len(path))
            if log:
                log(f"round {rnd + 1}: ll per unit {z / len(units):.3f}; units in gaps "
                    f"{sum(1 for u, a, b, s in path if s is None)}; path moved {moved:.1f} letters a unit")
            centers = [float(j0) for u, j0, j, s in path] + [float(len(P))]
            if moved < AB_SETTLE:
                break
    finally:
        P_LEN[0] = old
    return mark_by_evidence(rows, P)


def null_share(rows):
    """Share of valued places whose value is null: over 0.5 the table is degenerate (no. 2911, stage 4)."""
    tot = sum(r["support"] for r in rows)
    return sum(r["support"] for r in rows if r["value"] == "") / max(1, tot)



# ---------------------------------------------------------------- scoring
def score(pieces, truth):
    """Edit-distance alignment of a decode to the truth. '?' (unknown unit) absorbs any letters free.
    -> (matched letters, decoded letters, truth letters)."""
    d = []
    for p in pieces:
        if p is None:
            d.append("?")
        elif p.startswith("["):
            d.extend(p[1:-1])
        else:
            d.extend(p)
    n, m = len(d), len(truth)
    INF = 10 ** 9
    cost = [[INF] * (m + 1) for _ in range(n + 1)]
    mat = [[0] * (m + 1) for _ in range(n + 1)]
    cost[0][0] = 0
    for i in range(n + 1):
        ci, q = cost[i], (i > 0 and d[i - 1] == "?")
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            best, bm = INF, 0
            if i > 0:
                c = cost[i - 1][j] + (0 if q else 1)
                if c < best:
                    best, bm = c, mat[i - 1][j]
            if j > 0:
                c = ci[j - 1] + (0 if q else 1)
                if c < best or (c == best and mat[i][j - 1] > bm):
                    best, bm = c, mat[i][j - 1]
            if i > 0 and j > 0:
                eq = d[i - 1] == truth[j - 1]
                c = cost[i - 1][j - 1] + (0 if (q or eq) else 1)
                mm = mat[i - 1][j - 1] + (1 if eq else 0)
                if c < best or (c == best and mm > bm):
                    best, bm = c, mm
            ci[j], mat[i][j] = best, bm
    return mat[n][m], sum(1 for c in d if c != "?"), m


def permuted(kmap, rng):
    """Shuffle values among units of the same type (letter, syllable, word); nulls stay."""
    by = defaultdict(list)
    for u, v in kmap.items():
        by[unit_type(v)].append(u)
    out = dict(kmap)
    for t, us in by.items():
        if t == "null" or len(us) < 2:
            continue
        vals = [kmap[u] for u in us]
        for _ in range(20):
            sh = vals[:]
            rng.shuffle(sh)
            if sum(a == b for a, b in zip(sh, vals)) <= len(vals) // 10:
                break
        for u, v in zip(us, sh):
            out[u] = v
    return out


def line_spans(path, nlet):
    """Plaintext extent of each cipher line on the best path -> {line: (c, d)}; spans tile 0..nlet."""
    first = {}
    for u, j0, j, s in path:
        first.setdefault(u.line, j0)
    lines = sorted(first)
    return {ln: (first[ln], first[lines[k + 1]] if k + 1 < len(lines) else nlet) for k, ln in enumerate(lines)}


def heldout(units, P, wb, lac, pairs, folds=5, perms=20, iters=10, seed=1, log=None, minimum="probable"):
    """Full alignment fixes where each cipher line sits in the plaintext; nothing else is carried over.
    For each fold the table is rebuilt from the other lines and decodes the fold's lines."""
    segs = make_segments(units, P, wb, lac, pairs)
    table = train(segs, log=log)
    path, _ = best_path(segs, table)
    spans = line_spans(path, len(P))
    by_line = defaultdict(list)
    for u in units:
        by_line[u.line].append(u)
    lines = sorted(by_line)
    rng = random.Random(seed)
    res = []
    for f in range(folds):
        test = [ln for k, ln in enumerate(lines) if k % folds == f]
        tsegs = []
        for ln in lines:
            if ln in test:
                continue
            c, d = spans[ln]
            tsegs.append((0, c, Segment(by_line[ln], P[c:d], wb[c:d + 1], lac[c:d + 1],
                                        band=max(12, len(P[c:d]) // 2 + 6))))
        tpath, tsk = best_path(tsegs, train(tsegs, iters=iters))
        kmap = key_map(key_from_path(tpath, tsk), minimum)
        tot = dict(mat=0, dec=0, tru=0, cov=0, signs=0, cmat=0.0, cdec=0.0)
        ctrl = [permuted(kmap, rng) for _ in range(perms)]
        for ln in test:
            c, d = spans[ln]
            us = by_line[ln]
            signs = [u for u in us if u.kind == "sign"]
            tot["signs"] += len(signs)
            tot["cov"] += sum(1 for u in signs if u.sym in kmap)
            a, b, t = score(decode_units(us, kmap), P[c:d])
            tot["mat"] += a
            tot["dec"] += b
            tot["tru"] += t
            for km in ctrl:
                a, b, _ = score(decode_units(us, km), P[c:d])
                tot["cmat"] += a / perms
                tot["cdec"] += b / perms
        res.append(tot)
        if log:
            log(f"fold {f + 1}: acc {tot['mat'] / max(1, tot['dec']):.3f} cov {tot['cov'] / max(1, tot['signs']):.3f} "
                f"control {tot['cmat'] / max(1e-9, tot['cdec']):.3f}")
    S = {k: sum(r[k] for r in res) for k in res[0]}
    return dict(accuracy=S["mat"] / max(1, S["dec"]), recall=S["mat"] / max(1, S["tru"]),
                coverage=S["cov"] / max(1, S["signs"]), control=S["cmat"] / max(1e-9, S["cdec"]),
                units=S["signs"], letters=S["tru"], folds=res)


# ---------------------------------------------------------------- CLI
def load_pair(cpath, ppath, merge=True):
    units, ca, _ = parse_cipher(open(cpath, encoding="utf-8").read(), merge)
    P, wb, lac, pa = parse_plain(open(ppath, encoding="utf-8").read(), merge)
    return units, P, wb, lac, tie_pairs(units, P, ca, pa)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("cipher"), b.add_argument("plain"), b.add_argument("--out", required=True)
    b.add_argument("--aligned"), b.add_argument("--iters", type=int, default=12)
    b.add_argument("--abridged", action="store_true",
                   help="the plain side leaves out stretches of the cipher and rewords the rest")
    h = sub.add_parser("heldout")
    h.add_argument("cipher"), h.add_argument("plain"), h.add_argument("--folds", type=int, default=5)
    h.add_argument("--perms", type=int, default=20), h.add_argument("--out")
    d = sub.add_parser("decode")
    d.add_argument("cipher"), d.add_argument("key"), d.add_argument("--min", default="probable")
    for p in (b, h, d):
        p.add_argument("--no-merge", action="store_true")
    a = ap.parse_args(argv)
    log = lambda s: print(s, file=sys.stderr)
    if a.cmd == "build" and a.abridged:
        units, P, wb, lac, pairs = load_pair(a.cipher, a.plain, not a.no_merge)
        rows = build_abridged(units, P, wb, lac, log)
        write_key(rows, a.out)
        st = defaultdict(int)
        for r in rows:
            st[r["status"]] += 1
        print(f"units {len(units)}, letters {len(P)}, unit types {len(rows)}: {dict(st)}")
    elif a.cmd == "build":
        units, P, wb, lac, pairs = load_pair(a.cipher, a.plain, not a.no_merge)
        segs = make_segments(units, P, wb, lac, pairs)
        table = train(segs, a.iters, log)
        path, skipped = best_path(segs, table)
        rows = key_from_path(path, skipped)
        write_key(rows, a.out)
        if a.aligned:
            with open(a.aligned, "w", encoding="utf-8") as f:
                ln = None
                for u, j0, j, s in path:
                    if u.line != ln:
                        ln = u.line
                        f.write(f"\n# line {ln}\n")
                    f.write(f"{u.sym}={'∅' if s == '' else '[lacuna]' if s is None else s} ")
                f.write(f"\n\n# plaintext letters no unit accounts for: {len(skipped)} of {len(P)}\n")
        st = defaultdict(int)
        for r in rows:
            st[r["status"]] += 1
        print(f"units {len(units)}, letters {len(P)}, unit types {len(rows)}: {dict(st)}; "
              f"letters unaccounted {len(skipped)}")
        if null_share(rows) > 0.5:
            sys.exit(f"STOP: {null_share(rows):.0%} of valued places are null. The table is degenerate; the "
                     f"plain side is probably an abridgement. Rebuild with --abridged.")
    elif a.cmd == "heldout":
        units, P, wb, lac, pairs = load_pair(a.cipher, a.plain, not a.no_merge)
        r = heldout(units, P, wb, lac, pairs, a.folds, a.perms, log=log)
        line = (f"accuracy\t{r['accuracy']:.3f}\nrecall\t{r['recall']:.3f}\ncoverage\t{r['coverage']:.3f}\n"
                f"control\t{r['control']:.3f}\nunits\t{r['units']}\nletters\t{r['letters']}\n")
        print(line, end="")
        if a.out:
            open(a.out, "w").write(line)
    else:
        units, _, _ = parse_cipher(open(a.cipher, encoding="utf-8").read(), not a.no_merge)
        kmap = key_map(read_key(a.key), a.min)
        for ln, s in render(units, decode_units(units, kmap)):
            print(f"{ln:4d}  {s}")


if __name__ == "__main__":
    main()

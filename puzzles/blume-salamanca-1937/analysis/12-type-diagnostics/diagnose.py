"""12-type-diagnostics: ACA/BION-style type statistics of T1 and T2 against plants of 12 cipher types.

Plants are telegraph-style held-out Spanish (01-solver/plaintext.py) at the telegrams' lengths, 615 and 160.
Statistics, classifier and length rules are defined in README.md. No decipherment or key search is attempted.
Usage (from this folder): python3 -I diagnose.py > result.txt      (--quick: 40 plants per variant)
Heavy output: out/plants_615.tsv and out/plants_160.tsv (one row per plant, all statistics).
"""
import array, math, os, random, sys, time
from collections import Counter, defaultdict

here = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(here, "..", "01-solver")
sys.path.insert(0, SOLVER); os.chdir(SOLVER)
import plaintext, transpo

AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
AZ25 = AZ.replace("W", "")
VOW, CONS = "AEIOU", "".join(c for c in AZ if c not in "AEIOU")
SEED = 20261016
NPLANT = 40 if "--quick" in sys.argv else 500
STATS = ["IC", "MIC", "MKA", "DIC", "EDI", "LR", "ROD", "LDI", "SDD", "CHI", "NDL", "DBL", "DBLE"]
INTEGER = {"NDL", "DBLE"}
FMT = {"IC": 1, "MIC": 1, "MKA": 1, "DIC": 1, "EDI": 1, "LR": 2, "ROD": 3, "LDI": 3, "SDD": 3, "CHI": 0,
       "NDL": 0, "DBL": 3, "DBLE": 0}

# ---------------------------------------------------------------- Spanish reference tables
_lp = array.array("f"); _lp.fromfile(open("out/lm_es_2.bin", "rb"), 676)   # log10 P(ab), training corpus
_p = [10.0 ** x for x in _lp]; _s = sum(_p); _p = [x / _s for x in _p]
_row = [sum(_p[a * 26:(a + 1) * 26]) for a in range(26)]
_col = [sum(_p[a * 26 + b] for a in range(26)) for b in range(26)]
LDI_T = list(_lp)                                                                   # log10 P(ab)
SDD_T = [math.log10(_p[a * 26 + b] / (_row[a] * _col[b])) for a in range(26) for b in range(26)]  # log10 P(ab)/P(a)P(b)
_ref = Counter(); _rr = random.Random(SEED)
for _ in range(40):                       # as 08-letter-fit: 40 chunks of 10,000 telegraph-style letters
    _ref.update(plaintext.telegram(10000, _rr))
F_ES = [_ref[c] / sum(_ref.values()) for c in AZ]

# ---------------------------------------------------------------- statistics
def _ic(cnt, n):
    return sum(v * (v - 1) for v in cnt.values()) / (n * (n - 1)) if n > 1 else 0.0

def stats(t):
    n = len(t); v = [ord(c) - 65 for c in t]; c1 = Counter(v)
    mic = max(sum(_ic(Counter(v[j::p]), len(v[j::p])) for j in range(p)) / p for p in range(2, 16))
    mka = max(sum(1 for i in range(n - s) if v[i] == v[i + s]) / (n - s) for s in range(1, 16))
    dg = [v[i] * 26 + v[i + 1] for i in range(n - 1)]
    ed = [v[2 * i] * 26 + v[2 * i + 1] for i in range(n // 2)]
    tri = Counter(t[i:i + 3] for i in range(n - 2))
    pos = defaultdict(list)
    for i, d in enumerate(dg):
        pos[d].append(i)
    allp = odd = 0
    for L in pos.values():
        for a in range(len(L)):
            for b in range(a + 1, len(L)):
                allp += 1; odd += (L[b] - L[a]) & 1
    return {
        "IC": 1000 * _ic(c1, n), "MIC": 1000 * mic, "MKA": 1000 * mka,
        "DIC": 10000 * _ic(Counter(dg), n - 1), "EDI": 10000 * _ic(Counter(ed), n // 2),
        "LR": 1000 * math.sqrt(sum(1 for x in tri.values() if x >= 2)) / n,
        "ROD": odd / allp if allp else 0.5,
        "LDI": sum(LDI_T[d] for d in dg) / (n - 1), "SDD": sum(SDD_T[d] for d in dg) / (n - 1),
        "CHI": sum((c1[i] - n * F_ES[i]) ** 2 / (n * F_ES[i] + 0.5) for i in range(26)),
        "NDL": len(c1), "DBL": sum(1 for i in range(n - 1) if v[i] == v[i + 1]) / (n - 1),
        "DBLE": sum(1 for i in range(n // 2) if v[2 * i] == v[2 * i + 1]),
    }

# ---------------------------------------------------------------- plaintext
def words(rnd, letters=None, count=None):
    """plaintext.telegram's word stream, same RNG calls; stops at `letters` letters or `count` words."""
    w = plaintext.heldout_words("es"); i = rnd.randrange(len(w) - 5000); out = []; tot = 0
    while (letters is not None and tot < letters) or (count is not None and len(out) < count):
        t = w[i]; i += 1
        if t == ".":
            if out and out[-1] != plaintext.STOP["es"]:
                out.append(plaintext.STOP["es"]); tot += 5
            continue
        if t in plaintext.DROP["es"] and rnd.random() < 0.7:
            continue
        if rnd.random() < 0.03:
            q = rnd.choice(plaintext.QTY["es"]) + rnd.choice(plaintext.UNIT["es"]); out.append(q); tot += len(q)
        out.append(t); tot += len(t)
    return out[:count] if count is not None else out

def pt(n, rnd):
    return plaintext.telegram(n, rnd, "es", "telegraph")

_vc = Counter(t for t in plaintext.heldout_words("es") if t != ".")
VOCAB = sorted(t for t, k in _vc.items() if k >= 5)            # jargon replacement words

def homophone_counts():
    q = [26 * f for f in F_ES]; k = [int(x) for x in q]
    for i in sorted(range(26), key=lambda i: q[i] - k[i], reverse=True)[:26 - sum(k)]:
        k[i] += 1
    return k
KH = homophone_counts()

# ---------------------------------------------------------------- ciphers
def perm(p, rnd):
    l = list(p); rnd.shuffle(l); return "".join(l)

def single_col(p, rnd):
    w = rnd.randint(5, 30); return transpo.col_enc(p, rnd.sample(range(w), w))

def double_col(p, rnd):
    a, b = rnd.randint(8, 25), rnd.randint(8, 25)
    return transpo.double_enc(p, rnd.sample(range(a), a), rnd.sample(range(b), b), "CC")

def with_nulls(N, rnd, rate, alphabet):
    m = round(rate * N); l = list(pt(N - m, rnd))
    for q in sorted(rnd.sample(range(N), m)):       # ascending, so each null lands at its sampled position
        l.insert(q, rnd.choice(alphabet))
    return double_col("".join(l), rnd)

def rand_word(rnd, k=5):
    return "".join(rnd.choice(AZ) for _ in range(k))

def cv_word(rnd):
    return "".join(rnd.choice(VOW if x == "V" else CONS) for x in rnd.choice(("CVCVC", "VCVCV")))

def mixed(N, rnd):
    cw = {}; parts = []
    for tok in words(rnd, letters=2 * N):
        if rnd.random() < 0.10:
            cw.setdefault(tok, rand_word(rnd)); parts.append(cw[tok])
        else:
            parts.append(tok)
    s = "".join(parts); assert len(s) >= N; return double_col(s[:N], rnd)

def mono(p, rnd):
    k = dict(zip(AZ, rnd.sample(AZ, 26))); return "".join(k[c] for c in p)

def vigenere(p, rnd, key=None):
    key = key or [rnd.randrange(26) for _ in range(rnd.randint(3, 12))]
    return "".join(AZ[(ord(c) - 65 + key[i % len(key)]) % 26] for i, c in enumerate(p))

def bifid(p, rnd, period, sq=None):
    sq = sq or rnd.sample(AZ25, 25); pos = {c: divmod(i, 5) for i, c in enumerate(sq)}
    p = p.replace("W", "V"); step = period or len(p); out = []
    for s in range(0, len(p), step):
        blk = p[s:s + step]; seq = [pos[c][0] for c in blk] + [pos[c][1] for c in blk]
        out += [sq[seq[2 * i] * 5 + seq[2 * i + 1]] for i in range(len(blk))]
    return "".join(out)

def bifid_dec(c, sq, period):
    pos = {x: divmod(i, 5) for i, x in enumerate(sq)}; step = period or len(c); out = []
    for s in range(0, len(c), step):
        blk = c[s:s + step]; L = len(blk); seq = [y for x in blk for y in pos[x]]
        out += [sq[seq[i] * 5 + seq[L + i]] for i in range(L)]
    return "".join(out)

def fractionate(p, sq, sym):
    k = len(sym); pos = {c: i for i, c in enumerate(sq)}
    return "".join(sym[pos[c] // k] + sym[pos[c] % k] for c in p)

def adfgvx(N, rnd, six, ret_key=False):
    sym = "ADFGVX" if six else "ADFGX"; sq = rnd.sample(AZ + "0123456789" if six else AZ25, 36 if six else 25)
    p = pt(N // 2, rnd)
    if not six:
        p = p.replace("W", "V")
    w = rnd.randint(10, 25); key = rnd.sample(range(w), w)
    c = transpo.col_enc(fractionate(p, sq, sym), key)
    return (c, p, sq, key, sym) if ret_key else c

def playfair_prep(src, npairs):
    pairs = []; i = 0
    while len(pairs) < npairs:
        a = src[i]; b = src[i + 1] if i + 1 < len(src) else "X"
        if a == b:
            b = "X" if a != "X" else "Q"; i += 1
        else:
            i += 2
        pairs.append((a, b))
    return pairs

def playfair_pairs(pairs, sq, dec=False):
    pos = {c: divmod(i, 5) for i, c in enumerate(sq)}; d = -1 if dec else 1; out = []
    for a, b in pairs:
        (ra, ca), (rb, cb) = pos[a], pos[b]
        if ra == rb:
            out += [sq[ra * 5 + (ca + d) % 5], sq[rb * 5 + (cb + d) % 5]]
        elif ca == cb:
            out += [sq[((ra + d) % 5) * 5 + ca], sq[((rb + d) % 5) * 5 + cb]]
        else:
            out += [sq[ra * 5 + cb], sq[rb * 5 + ca]]
    return "".join(out)

def playfair(N, rnd, ret_key=False):
    sq = rnd.sample(AZ25, 25); pairs = playfair_prep(pt(N, rnd).replace("W", "V"), N // 2)
    c = playfair_pairs(pairs, sq)
    return (c, pairs, sq) if ret_key else c

def homophonic(p, rnd, ret_key=False):
    outs = rnd.sample(AZ, 26); sets = {}; j = 0
    for i, c in enumerate(AZ):
        if KH[i]:
            sets[c] = outs[j:j + KH[i]]; j += KH[i]
    have = sorted(sets)
    for c in AZ:
        if c not in sets:                  # letters with k = 0 borrow another letter's homophones
            sets[c] = sets[rnd.choice(have)]
    out = "".join(rnd.choice(sets[c]) for c in p)
    return (out, sets) if ret_key else out

def nomenclator(N, rnd):
    key = dict(zip(AZ, rnd.sample(AZ, 26))); code = {}; parts = []
    for tok in words(rnd, letters=2 * N):
        if rnd.random() < 0.15:
            code.setdefault(tok, rand_word(rnd, rnd.choice((2, 3)))); parts.append(code[tok])
        else:
            parts.append("".join(key[c] for c in tok))
    s = "".join(parts); assert len(s) >= N; return s[:N]

def codebook(N, rnd, cv):
    ws = words(rnd, count=N // 5); cw = {}
    for t in ws:
        if t not in cw:
            cw[t] = cv_word(rnd) if cv else rand_word(rnd)
    return "".join(cw[t] for t in ws)

def jargon(N, rnd, transpose):
    m = {}; parts = []
    for tok in words(rnd, letters=2 * N):
        if tok not in m:
            m[tok] = rnd.choice(VOCAB)
        parts.append(m[tok])
    s = "".join(parts); assert len(s) >= N; s = s[:N]
    return double_col(s, rnd) if transpose else s

EVEN = lambda N: N - (N % 2)
VARIANTS = [
    ("1a", 1, "random permutation", lambda N, r: perm(pt(N, r), r)),
    ("1b", 1, "single columnar w 5-30", lambda N, r: single_col(pt(N, r), r)),
    ("1c", 1, "double columnar 8-25", lambda N, r: double_col(pt(N, r), r)),
    ("2a", 2, "uniform nulls 3% + DC", lambda N, r: with_nulls(N, r, 0.03, AZ)),
    ("2b", 2, "uniform nulls 8% + DC", lambda N, r: with_nulls(N, r, 0.08, AZ)),
    ("2c", 2, "X nulls 1% + DC", lambda N, r: with_nulls(N, r, 0.01, "X")),
    ("3", 3, "10% words codewords + DC", mixed),
    ("4", 4, "monoalphabetic", lambda N, r: mono(pt(N, r), r)),
    ("5", 5, "Vigenere p 3-12", lambda N, r: vigenere(pt(N, r), r)),
    ("6a", 6, "bifid p 5", lambda N, r: bifid(pt(N, r), r, 5)),
    ("6b", 6, "bifid p 7", lambda N, r: bifid(pt(N, r), r, 7)),
    ("6c", 6, "bifid p 10", lambda N, r: bifid(pt(N, r), r, 10)),
    ("6d", 6, "bifid unperiodic", lambda N, r: bifid(pt(N, r), r, None)),
    ("7a", 7, "ADFGX + columnar 10-25", lambda N, r: adfgvx(EVEN(N), r, False)),
    ("7b", 7, "ADFGVX + columnar 10-25", lambda N, r: adfgvx(EVEN(N), r, True)),
    ("8", 8, "Playfair", lambda N, r: playfair(EVEN(N), r)),
    ("9", 9, "homophonic, 26 outputs", lambda N, r: homophonic(pt(N, r), r)),
    ("10", 10, "nomenclator 15% 2-3-letter", nomenclator),
    ("11a", 11, "codebook, uniform 5-letter", lambda N, r: codebook(N, r, False)),
    ("11b", 11, "codebook, CVCVC/VCVCV", lambda N, r: codebook(N, r, True)),
    ("12a", 12, "jargon words", lambda N, r: jargon(N, r, False)),
    ("12b", 12, "jargon words + DC", lambda N, r: jargon(N, r, True)),
]
TYPES = {1: "transposition", 2: "transposition + nulls", 3: "transposition of mixed text", 4: "monoalphabetic",
         5: "Vigenere", 6: "bifid", 7: "ADFGX/ADFGVX", 8: "Playfair", 9: "homophonic", 10: "nomenclator",
         11: "codebook", 12: "jargon code"}
TRANSPO = {1, 2, 3}

# ---------------------------------------------------------------- self-tests (round trips)
def selftest():
    r = random.Random(7)
    p = pt(400, r)
    assert "".join(words(random.Random(3), letters=615))[:615] == pt(615, random.Random(3))
    assert len(words(random.Random(3), count=123)) == 123
    k = [r.randrange(26) for _ in range(7)]
    assert "".join(AZ[(ord(c) - 65 - k[i % 7]) % 26] for i, c in enumerate(vigenere(p, r, k))) == p
    for per in (5, 7, 10, None):
        sq = r.sample(AZ25, 25); assert bifid_dec(bifid(p, r, per, sq), sq, per) == p.replace("W", "V")
    # hand-worked bifid (square rows BGWKZ QPNDS IOAXE FCLUM THYVR): rows 4433353243, cols 1355312325
    assert bifid("FLEEATONCE", None, None, list("BGWKZQPNDSIOAXEFCLUMTHYVR")) == "UAEOLWRINS"
    # textbook Playfair, key PLAYFAIR EXAMPLE (I/J square): HI DE TH EG OL DI NT HE TR EX ES TU MP
    pf = playfair_prep("HIDETHEGOLDINTHETREESTUMP", 13)
    assert "".join(a + b for a, b in pf) == "HIDETHEGOLDINTHETREXESTUMP"
    assert playfair_pairs(pf, list("PLAYFIREXMBCDGHKNOQSTUVWZ")) == "BMODZBXDNABEKUDMUIXMMOUVIF"
    for six in (False, True):
        c, pp, sq, key, sym = adfgvx(614, r, six, ret_key=True)
        f = transpo.col_dec(c, key); k6 = len(sym)
        assert "".join(sq[sym.index(f[2 * i]) * k6 + sym.index(f[2 * i + 1])] for i in range(len(f) // 2)) == pp
        assert len(c) == 614 and set(c) <= set(sym)
    c, pairs, sq = playfair(614, r, ret_key=True)
    assert len(c) == 614 and "W" not in c
    assert playfair_pairs([(c[2 * i], c[2 * i + 1]) for i in range(307)], sq, dec=True) == "".join(a + b for a, b in pairs)
    assert all(c[2 * i] != c[2 * i + 1] for i in range(307))
    h, sets = homophonic(p, r, ret_key=True)
    assert sum(KH) == 26 and all(h[i] in sets[p[i]] for i in range(len(p)))
    for N in (615, 160):
        for vid, _, _, f in VARIANTS:
            x = f(N, random.Random(vid)); assert len(x) == (EVEN(N) if vid in ("7a", "7b", "8") else N), (vid, len(x))
            assert set(x) <= set(AZ), vid
    # statistic spot checks against hand computation
    s = stats("AB" * 20)
    assert abs(s["IC"] - 1000 * (2 * 20 * 19) / (40 * 39)) < 1e-9 and s["DBL"] == 0 and s["NDL"] == 2
    assert abs(s["MKA"] - 1000) < 1e-9 and s["ROD"] == 0.0     # AB and BA recur only at even distances
    s = stats("AABBCCDD" * 3); assert s["DBLE"] == 12 and abs(s["DBL"] - 12 / 23) < 1e-12
    print("self-tests pass")

# ---------------------------------------------------------------- summaries
def quant(xs, q):
    xs = sorted(xs); h = (len(xs) - 1) * q; lo = int(math.floor(h)); hi = min(lo + 1, len(xs) - 1)
    return xs[lo] + (xs[hi] - xs[lo]) * (h - lo)

def pctile(xs, x):
    return 100.0 * (sum(1 for y in xs if y < x) + 0.5 * sum(1 for y in xs if y == x)) / len(xs)

def f(v, s):
    return f"{v:.{FMT[s]}f}"

class Gauss:
    """Diagonal Gaussian per variant; sd floored (see README)."""
    def __init__(self, rows_by_var):
        self.n, self.S, self.Q = {}, {}, {}
        for v, rows in rows_by_var.items():
            self.n[v] = len(rows)
            self.S[v] = {s: sum(r[s] for r in rows) for s in STATS}
            self.Q[v] = {s: sum(r[s] ** 2 for r in rows) for s in STATS}
        sd = {s: sorted(self._sd(v, s) for v in rows_by_var) for s in STATS}
        self.floor = {s: 0.5 if s in INTEGER else 0.1 * sd[s][len(sd[s]) // 2] for s in STATS}
        self.P = {v: {s: (self.S[v][s] / self.n[v], max(self._sd(v, s), self.floor[s])) for s in STATS}
                  for v in rows_by_var}

    def _sd(self, v, s, drop=None):
        n, S, Q = self.n[v], self.S[v][s], self.Q[v][s]
        if drop is not None:
            n, S, Q = n - 1, S - drop[s], Q - drop[s] ** 2
        mu = S / n; var = max((Q - n * mu * mu) / (n - 1), 0.0)
        return math.sqrt(var)

    def params(self, v, s, drop=None):
        if drop is None:
            return self.P[v][s]
        return (self.S[v][s] - drop[s]) / (self.n[v] - 1), max(self._sd(v, s, drop), self.floor[s])

    def ll(self, v, x, drop=None, only=None):
        tot = 0.0
        for s in (only or STATS):
            mu, sd = self.params(v, s, drop)
            tot += -0.5 * ((x[s] - mu) / sd) ** 2 - math.log(sd) - 0.5 * math.log(2 * math.pi)
        return tot

def lse(xs):
    m = max(xs); return m + math.log(sum(math.exp(x - m) for x in xs))

VOFT = defaultdict(list)
for vid, ty, _, _ in VARIANTS:
    VOFT[ty].append(vid)
TYPE_OF = {vid: ty for vid, ty, _, _ in VARIANTS}

def type_ll(G, x, drop_var=None, drop=None, only=None, types=None):
    out = {}
    for ty in (types or TYPES):
        out[ty] = lse([G.ll(v, x, drop if v == drop_var else None, only) for v in VOFT[ty]]) - math.log(len(VOFT[ty]))
    return out

# ---------------------------------------------------------------- lengths
def factor(n):
    out, p = [], 2
    while p * p <= n:
        while n % p == 0:
            out.append(p); n //= p
        p += 1
    if n > 1:
        out.append(n)
    c = Counter(out); return " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(c.items()))

def length_section(name, N, words_on_form):
    divs = [d for d in range(1, N + 1) if N % d == 0]
    print(f"\n{name}: N = {N} = {factor(N)}; N-1 = {N - 1} = {factor(N - 1)}; N+1 = {N + 1} = {factor(N + 1)}")
    print(f"  divisors: {divs}")
    print(f"  form words {words_on_form} - 2 address words = {words_on_form - 2}; N/5 = {N / 5:g} -> "
          f"{'each five-letter group counted as one word' if words_on_form - 2 == N / 5 else 'MISMATCH'}")
    print(f"  even (Playfair, ADFGX/ADFGVX, any digraphic output): {'yes' if N % 2 == 0 else 'NO'}")
    print(f"  multiple of 25 (a whole number of 5x5 blocks): {'yes' if N % 25 == 0 else 'no'} (N mod 25 = {N % 25})")
    g = []
    for n in range(2, 26):
        for cells, lab in ((n * n, f"{n}x{n}"),) + (((n * n - 1, f"{n}x{n} no centre"),) if n % 2 else ()):
            if cells <= N and N % cells == 0:
                g.append(f"{lab} ({cells} cells) x {N // cells}")
    print(f"  complete turning grilles (N a multiple of n^2, or of n^2-1 for odd n without centre): {g or 'none'}")
    print(f"  complete single-columnar rectangles, width 2-45: {[d for d in divs if 2 <= d <= 45] or 'none'}")
    print(f"  complete double columnar, both widths 2-45 dividing N: "
          f"{[(a, b) for a in divs for b in divs if 2 <= a <= 45 and 2 <= b <= 45 and a <= b] or 'none'} (either order)")
    print(f"  bifid / Vigenere periods 2-15 giving complete blocks or key cycles: {[d for d in divs if 2 <= d <= 15] or 'none'}")
    print(f"  codeword lengths 2-10 dividing N: {[k for k in range(2, 11) if N % k == 0]}")
    print(f"  ADFGX/ADFGVX: plaintext letters = N/2 = {N / 2:g}" + ("" if N % 2 == 0 else " (impossible)"))

# ---------------------------------------------------------------- main
def main():
    t0 = time.time()
    selftest()
    load = lambda q: "".join(c for c in open(os.path.join(here, q)).read().upper() if c.isalpha())
    TEL = {615: ("T1", load("../../sources/telegram-1.txt")), 160: ("T2", load("../../sources/telegram-2.txt"))}
    assert len(TEL[615][1]) == 615 and len(TEL[160][1]) == 160
    print(f"plants per variant per length: {NPLANT}; seed {SEED}; types {len(TYPES)}, variants {len(VARIANTS)}")
    print(f"homophone counts k (sum 26): " + " ".join(f"{c}{k}" for c, k in zip(AZ, KH) if k))
    print(f"letters with k = 0 (borrow another letter's set): {''.join(c for c, k in zip(AZ, KH) if not k)}")
    print("statistics: " + " ".join(STATS))
    for N, (nm, t) in TEL.items():
        st = stats(t); print(f"{nm} ({N}): " + "  ".join(f"{s} {f(st[s], s)}" for s in STATS))
        kap = [sum(1 for i in range(N - s) if t[i] == t[i + s]) / (N - s) for s in range(1, 16)]
        mic = [sum(_ic(Counter(t[j::p]), len(t[j::p])) for j in range(p)) / p for p in range(2, 16)]
        print(f"   kappa x1000 by shift 1-15: " + " ".join(f"{1000 * k:.0f}" for k in kap)
              + f"; MKA at shift {1 + kap.index(max(kap))}; MIC at period {2 + mic.index(max(mic))}")
        print(f"   doubled letters: {sum(t[i] == t[i + 1] for i in range(N - 1))} in all, "
              f"{sum(t[2 * i] == t[2 * i + 1] for i in range(N // 2))} at even-aligned pairs, "
              f"{sum(t[2 * i + 1] == t[2 * i + 2] for i in range((N - 1) // 2))} at odd-aligned pairs")
    summary = {}
    for N in (615, 160):
        nm, tel = TEL[N]; x = stats(tel)
        rows = {}
        for vid, ty, lab, fn in VARIANTS:
            r = random.Random(f"{SEED}-{vid}-{N}")
            rows[vid] = [stats(fn(N, r)) for _ in range(NPLANT)]
        with open(os.path.join(here, "out", f"plants_{N}.tsv"), "w") as fo:
            fo.write("variant\ttype\t" + "\t".join(STATS) + "\n")
            for vid in rows:
                for rr in rows[vid]:
                    fo.write(f"{vid}\t{TYPE_OF[vid]}\t" + "\t".join(f"{rr[s]:.6g}" for s in STATS) + "\n")
        bytype = {ty: [rr for v in VOFT[ty] for rr in rows[v]] for ty in TYPES}
        print(f"\n{'=' * 100}\nLENGTH {N} ({nm}); {time.time() - t0:.0f} s elapsed")
        for title, groups, label in (("TYPE", bytype, lambda k: f"{k:>2} {TYPES[k][:22]}"),
                                     ("VARIANT", rows, lambda k: f"{k:>3} {dict((a, c) for a, _, c, _ in VARIANTS)[k][:22]}")):
            print(f"\n{title} median [5%, 95%] at N = {N}; {nm} first")
            print(f"{'':27}" + "".join(f"{s:>24}" for s in STATS))
            print(f"{nm:27}" + "".join(f"{f(x[s], s):>24}" for s in STATS))
            for k, rr in groups.items():
                cells = [f"{f(quant([q[s] for q in rr], .5), s)} [{f(quant([q[s] for q in rr], .05), s)},{f(quant([q[s] for q in rr], .95), s)}]" for s in STATS]
                print(f"{label(k):27}" + "".join(f"{c:>24}" for c in cells))
        print(f"\n{nm} percentile within each type's plants (* outside 5-95%, ** outside 1-99%)")
        print(f"{'':27}" + "".join(f"{s:>8}" for s in STATS))
        out599, out199 = {}, {}
        for ty, rr in bytype.items():
            cells = []
            for s in STATS:
                xs = [q[s] for q in rr]; pc = pctile(xs, x[s])
                o5 = not (quant(xs, .05) <= x[s] <= quant(xs, .95)); o1 = not (quant(xs, .01) <= x[s] <= quant(xs, .99))
                out599.setdefault(ty, set()); out199.setdefault(ty, set())
                if o5: out599[ty].add(s)
                if o1: out199[ty].add(s)
                cells.append(f"{pc:.0f}{'**' if o1 else '*' if o5 else ''}")
            print(f"{ty:>2} {TYPES[ty][:24]:24}" + "".join(f"{c:>8}" for c in cells))
        # classifier
        G = Gauss(rows)
        print("\nsd floors: " + " ".join(f"{s} {G.floor[s]:.3g}" for s in STATS))
        tl = type_ll(G, x); best = max(tl.values())
        print(f"\nCLASSIFIER ranking for {nm} (natural-log likelihood, type = equal mixture of its variants)")
        print(f"{'rank':>4} {'type':28} {'logL':>12} {'minus best':>12}   worst statistics (z vs nearest variant)")
        ranked = sorted(tl, key=lambda k: -tl[k])
        for i, ty in enumerate(ranked):
            vbest = max(VOFT[ty], key=lambda v: G.ll(v, x))
            zs = sorted(((x[s] - G.params(vbest, s)[0]) / G.params(vbest, s)[1], s) for s in STATS)
            worst = sorted(zs, key=lambda z: -abs(z[0]))[:3]
            print(f"{i + 1:>4} {ty:>2} {TYPES[ty][:25]:25} {tl[ty]:12.1f} {tl[ty] - best:12.1f}   [{vbest}] "
                  + ", ".join(f"{s} {z:+.1f}" for z, s in worst))
        vl = {v: G.ll(v, x) for v in rows}; vb = max(vl.values())
        print("variants, top 8: " + "; ".join(f"{v} {vl[v] - vb:.1f}" for v in sorted(vl, key=lambda v: -vl[v])[:8]))
        # LOO
        conf = defaultdict(Counter); vconf = defaultdict(Counter)
        for vid in rows:
            for rr in rows[vid]:
                tll = type_ll(G, rr, drop_var=vid, drop=rr); pred = max(tll, key=lambda k: tll[k])
                conf[TYPE_OF[vid]][pred] += 1
                if TYPE_OF[vid] in TRANSPO:
                    vll = {v: G.ll(v, rr, rr if v == vid else None) for v in rows}
                    vconf[vid][max(vll, key=lambda k: vll[k])] += 1
        tot = sum(sum(c.values()) for c in conf.values()); acc = sum(conf[t][t] for t in TYPES) / tot
        bin_ok = sum(n for t in TYPES for p, n in conf[t].items() if (t in TRANSPO) == (p in TRANSPO))
        print(f"\nLEAVE-ONE-OUT confusion at N = {N} (rows true type, columns predicted); accuracy {100 * acc:.1f}%")
        print("    " + "".join(f"{t:>6}" for t in TYPES))
        for t in TYPES:
            print(f"{t:>3} " + "".join(f"{conf[t][p]:>6}" for p in TYPES))
        print(f"binary 'transposition (1-3) vs everything else': {bin_ok}/{tot} = {100 * bin_ok / tot:.2f}%")
        errs = Counter((t, p) for t in TYPES for p in conf[t] for _ in range(conf[t][p]) if (t in TRANSPO) != (p in TRANSPO))
        print("  binary errors (true -> predicted: count): " + (", ".join(f"{a}->{b}: {n}" for (a, b), n in errs.most_common()) or "none"))
        bin_x12 = sum(n for t in TYPES if t != 12 for p, n in conf[t].items() if (t in TRANSPO) == (p in TRANSPO))
        tot_x12 = sum(sum(conf[t].values()) for t in TYPES if t != 12)
        print(f"  (supplementary, not the pre-registered test) same with type-12 plants left out: {100 * bin_x12 / tot_x12:.2f}%")
        print(f"\nmutual confusion of transposition variants (LOO over all 22 variants; rows true)")
        tv = [v for v in rows if TYPE_OF[v] in TRANSPO]; others = [v for v in rows if v not in tv]
        print("     " + "".join(f"{v:>6}" for v in tv) + f"{'other':>7}")
        for v in tv:
            print(f"{v:>4} " + "".join(f"{vconf[v][p]:>6}" for p in tv) + f"{sum(vconf[v][p] for p in others):>7}")
        sub = sum(conf[t][p] for t in TRANSPO for p in TRANSPO); diag = sum(conf[t][t] for t in TRANSPO)
        print(f"types 1-3 among themselves: {diag}/{sub} on the diagonal = {100 * diag / sub:.1f}% (chance about 33%)")
        print("single-statistic LOO accuracy among types 1-3 only (3-way; then 1v2, 1v3, 2v3):")
        best1 = (0, "")
        for s in STATS:
            def acc_of(ts):
                ok = n = 0
                for vid in rows:
                    if TYPE_OF[vid] not in ts:
                        continue
                    for rr in rows[vid]:
                        tll = type_ll(G, rr, drop_var=vid, drop=rr, only=[s], types=ts)
                        ok += max(tll, key=lambda k: tll[k]) == TYPE_OF[vid]; n += 1
                return 100 * ok / n
            a3 = acc_of((1, 2, 3)); prs = ((1, 2), (1, 3), (2, 3)); pw = [acc_of(p) for p in prs]
            best1 = max(best1, (a3, s))
            print(f"  {s:5} {a3:6.1f}%   {pw[0]:6.1f}% {pw[1]:6.1f}% {pw[2]:6.1f}%")
            for p, a in zip(prs, pw):
                if a >= 90:
                    tll = type_ll(G, x, only=[s], types=p)
                    print(f"        pairwise split >= 90%: {s} on {p[0]} v {p[1]}; {nm}'s {s} favours type "
                          f"{max(tll, key=lambda k: tll[k])} by {abs(tll[p[0]] - tll[p[1]]):.2f} log units")
        print(f"  best single statistic (3-way): {best1[1]} {best1[0]:.1f}%")
        # supplementary: how often plants pass the band test of the first pre-registered reading (bands not LOO)
        bands = {t: {s: (quant([q[s] for q in bytype[t]], .05), quant([q[s] for q in bytype[t]], .95)) for s in STATS}
                 for t in TRANSPO}
        passes = lambda rr: all(any(bands[t][s][0] <= rr[s] <= bands[t][s][1] for t in TRANSPO) for s in STATS)
        print("\n(supplementary) share of plants with every statistic inside the 5-95% band of at least one type 1-3: "
              + "; ".join(f"type {t} {100 * sum(map(passes, bytype[t])) / len(bytype[t]):.0f}%" for t in TYPES))
        # supplementary: the exclusion rule applied per variant (bands and likelihood of the variant itself)
        vexcl = []
        for vid in rows:
            o1 = [s for s in STATS if not (quant([q[s] for q in rows[vid]], .01) <= x[s] <= quant([q[s] for q in rows[vid]], .99))]
            if o1 and vl[vid] < vb - 10:
                vexcl.append(vid)
        print(f"\n(supplementary) exclusion rule applied per variant, {nm}: excluded {vexcl}; "
              f"not excluded {[v for v in rows if v not in vexcl]}")
        # supplementary: sensitivity of the type-1 bands to the plaintext style (prose instead of telegraphese)
        r = random.Random(f"{SEED}-prose-{N}")
        pr = [stats(perm(plaintext.telegram(N, r, "es", "prose"), r)) for _ in range(NPLANT)]
        print(f"(supplementary) random permutation of PROSE-style Spanish, {NPLANT} plants: " + "; ".join(
            f"{s} {f(quant([q[s] for q in pr], .5), s)} [{f(quant([q[s] for q in pr], .05), s)},"
            f"{f(quant([q[s] for q in pr], .95), s)}] {nm} pct {pctile([q[s] for q in pr], x[s]):.0f}"
            for s in ("IC", "MIC", "LR", "CHI", "LDI")))
        summary[N] = dict(nm=nm, x=x, tl=tl, ranked=ranked, out599=out599, out199=out199,
                          binacc=100 * bin_ok / tot, acc=100 * acc, best1=best1, bytype=bytype)
    # pre-registered checks
    print(f"\n{'=' * 100}\nPRE-REGISTERED CHECKS")
    for N, S in summary.items():
        nm = S["nm"]; top = S["ranked"][0]
        print(f"\n{nm}: top type {top} ({TYPES[top]}); transposition type first: {top in TRANSPO}")
        miss = [s for s in STATS if all(s in S["out599"][t] for t in TRANSPO)]
        print(f"  statistics outside the 5-95% band of every transposition type (1-3): {miss or 'none'}")
        for s in miss:
            ins = [t for t in TYPES if t not in TRANSPO and s not in S["out599"][t]]
            print(f"    {s}: inside the 5-95% band of types {ins or 'none'}")
        print(f"  one transposition type containing every statistic in its 5-95% band: "
              f"{[t for t in TRANSPO if not S['out599'][t]] or 'none'}")
        print(f"  LOO binary accuracy {S['binacc']:.2f}% (needs >= 95%): {S['binacc'] >= 95}")
        print(f"  best single statistic separating 1/2/3: {S['best1'][1]} {S['best1'][0]:.1f}% (needs >= 90% to name a winner)")
        best = max(S["tl"].values())
        excl = [t for t in TYPES if S["out199"][t] and S["tl"][t] < best - 10]
        print(f"  excluded under the rule (outside a 1-99% band AND > 10 below the best): "
              + ", ".join(f"{t} {TYPES[t]} [{','.join(s for s in STATS if s in S['out199'][t])}; {S['tl'][t] - best:.0f}]" for t in excl))
        print(f"  not excluded: {[t for t in TYPES if t not in excl]}")
    ok = all(summary[N]["ranked"][0] in TRANSPO and summary[N]["binacc"] >= 95 and
             not [s for s in STATS if all(s in summary[N]["out599"][t] for t in TRANSPO)] for N in summary)
    print(f"\nfirst pre-registered reading ('plaintext letters in a new order' stands): {'MET' if ok else 'NOT MET'}")
    print(f"\n{'=' * 100}\nLENGTH CONSTRAINTS")
    length_section("T1", 615, 125); length_section("T2", 160, 34)
    print(f"\ntotal time {time.time() - t0:.0f} s")

if __name__ == "__main__":
    main()

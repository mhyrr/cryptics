"""Shared pieces for 09-odd-positions: the telegrams, the surprisal reference, plant generators, and a
rank-based null with min-p calibration. Imported by scan.py (A1-A3) and residues.py (A4-A5).

Imports 01-solver the way 08-letter-fit/fit.py does: its folder goes on sys.path and becomes the working
directory, because plaintext.py opens relative paths.
"""
import math, os, random, sys
from bisect import bisect_left, bisect_right
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(HERE, "..", "01-solver")
sys.path.insert(0, SOLVER); os.chdir(SOLVER)
import plaintext, transpo  # noqa: E402

AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def _load(p):
    return "".join(c for c in open(os.path.join(HERE, p)).read().upper() if c.isalpha())


TEL = {"T1": _load("../../sources/telegram-1.txt"), "T2": _load("../../sources/telegram-2.txt")}
assert len(TEL["T1"]) == 615 and len(TEL["T2"]) == 160


def surprisal():
    """Per-letter surprisal s(c) = -log10 p_es(c). Reference as in 08: 40 chunks of 10,000 letters of
    plaintext.telegram, Spanish, telegraph style, same seed as 08 (so the same 40 chunks). Floor: add one
    to every count, so W and K are finite. Returns (counts, s, s_int) with s_int = round(1000 * s), used
    so window sums are exact integers and ties compare exactly."""
    rnd = random.Random(20261016)
    ref = Counter()
    for _ in range(40):
        ref.update(plaintext.telegram(10000, rnd, "es", "telegraph"))
    N = sum(ref.values())
    s = {c: -math.log10((ref[c] + 1) / (N + 26)) for c in AZ}
    return ref, s, {c: round(1000 * s[c]) for c in AZ}


def spanish(n, rnd, stop="PUNTO"):
    """n letters of Spanish telegraph-style plaintext; the stop word is `stop` (PUNTO, or a single letter)."""
    old = plaintext.STOP["es"]
    plaintext.STOP["es"] = stop
    try:
        return plaintext.telegram(n, rnd, "es", "telegraph")
    finally:
        plaintext.STOP["es"] = old


def encipher(pt, rnd, system):
    """single: one columnar, width 5-45, random key, rows left to right, columns in key order, incomplete
    last row allowed. double: forward double columnar (CC), widths 8-25, two independent random keys."""
    if system == "single":
        w = rnd.randint(5, 45)
        return transpo.col_enc(pt, rnd.sample(range(w), w))
    w1, w2 = rnd.randint(8, 25), rnd.randint(8, 25)
    return transpo.double_enc(pt, rnd.sample(range(w1), w1), rnd.sample(range(w2), w2), "CC")


def plant(n, rnd, system, conv, letter):
    """conv 'stop': the stop word PUNTO is replaced by `letter`, so the letter occurs in the body.
    conv 'fill': ordinary PUNTO stops; 1-4 copies of `letter` appended to the plaintext before
    transposition (fillers completing the table)."""
    if conv == "stop":
        pt = spanish(n, rnd, stop=letter)
    else:
        f = rnd.randint(1, 4)
        pt = spanish(n - f, rnd) + letter * f
    ct = encipher(pt, rnd, system)
    assert len(ct) == n
    return ct


class Null:
    """Rank-based null from K rows of statistics (larger = more extreme).
    p of an observed value x in column i: (1 + #{rows >= x}) / (K + 1).
    p of a null row's own value (leave-one-out): #{rows >= x_j} / K, which counts itself.
    Calibrated min-p of a group of columns: (1 + #{null rows whose own min-p <= observed min-p}) / (K + 1).
    Ties count as at least as extreme, so every p here is conservative."""

    def __init__(self, rows, groups):
        self.K = K = len(rows)
        self.groups = groups
        self.cols = [sorted(c) for c in zip(*rows)]
        nullp = [[(K - bisect_left(col, x)) / K for col, x in zip(self.cols, r)] for r in rows]
        self.minp = {g: sorted(min(p[i] for i in idx) for p in nullp) for g, idx in groups.items()}

    def p(self, obs):
        K = self.K
        return [(1 + K - bisect_left(col, x)) / (K + 1) for col, x in zip(self.cols, obs)]

    def cal(self, obs):
        ps = self.p(obs)
        out = {}
        for g, idx in self.groups.items():
            m = min(ps[i] for i in idx)
            out[g] = (m, (1 + bisect_right(self.minp[g], m)) / (self.K + 1))
        return ps, out

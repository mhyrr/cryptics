"""Single columnar transposition solver (forward: write rows, read columns in key order; incomplete last row;
the first len % w columns are one letter longer). Same convention as 01-solver/transpo.col_enc.

A key is a rank list: key[c] = reading rank of plaintext column c. The solver is told the width and decrypts
the whole text it is given, as an exclusion run on the full telegram would.
  w <= 8: exhaustive over all w! keys.
  w >= 9: simulated annealing on the total Spanish quadgram score (log10), RESTARTS runs of ITERS_PER_W * w
          steps each, temperature geometric from T0 to T1; moves are a swap, a single move, or a block of
          2..w/2 adjacent plaintext columns moved elsewhere. The best key seen over all runs is returned.
Pilot (scratch, before the frozen run): plain hill climbing recovered w 9-15 but failed from w = 20; this
annealing schedule recovered 9/9 at w 20-30 and 1/6 at w 35-45 (one run of 10,000 w steps).
Self-test: python3 -I colsolve.py
"""
import itertools, math, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

RESTARTS, ITERS_PER_W, T0, T1 = 2, 10000, 30.0, 1.0


def decrypt_vals(ctv, key):
    """ctv: list of letter values. Returns the plaintext values for key under length len(ctv)."""
    n, w = len(ctv), len(key)
    rows, extra = divmod(n, w)
    order = sorted(range(w), key=key.__getitem__)
    out = [0] * n; pos = 0
    for c in order:
        ln = rows + (c < extra)
        out[c::w] = ctv[pos:pos + ln]
        pos += ln
    return out


def score(ctv, key):
    return common.qscore(decrypt_vals(ctv, key))


def exhaustive(ctv, w):
    best = (-99.0, None)
    for p in itertools.permutations(range(w)):
        s = score(ctv, p)
        if s > best[0]:
            best = (s, list(p))
    return best


def _move(k, rnd):
    w = len(k); m = k[:]; r = rnd.random()
    if r < 0.4:
        i, j = rnd.sample(range(w), 2); m[i], m[j] = m[j], m[i]
    elif r < 0.7:
        i, j = rnd.sample(range(w), 2); m.insert(j, m.pop(i))
    else:
        ln = rnd.randint(2, max(2, w // 2)); i = rnd.randrange(w - ln + 1)
        blk = m[i:i + ln]; rest = m[:i] + m[i + ln:]; j = rnd.randrange(len(rest) + 1)
        m = rest[:j] + blk + rest[j:]
    return m


def anneal(ctv, w, rnd):
    q = len(ctv) - 3; iters = ITERS_PER_W * w
    k = rnd.sample(range(w), w); s = score(ctv, k) * q; best = (s, k)
    for i in range(iters):
        T = T0 * (T1 / T0) ** (i / iters)
        m = _move(k, rnd); t = score(ctv, m) * q
        if t >= s or rnd.random() < math.exp((t - s) / T):
            k, s = m, t
            if s > best[0]:
                best = (s, k)
    return best[0] / q, best[1]


def solve(ct, w, seed):
    ctv = [ord(c) - 65 for c in ct]
    if w <= 8:
        return exhaustive(ctv, w)
    rnd = random.Random(seed ^ 0x2545F491)  # the caller passes a seed drawn apart from the plant's
    return max((anneal(ctv, w, rnd) for _ in range(RESTARTS)), key=lambda r: r[0])


def decrypt(ct, key):
    return "".join(chr(65 + v) for v in decrypt_vals([ord(c) - 65 for c in ct], key))


if __name__ == "__main__":
    rnd = random.Random(3)
    for _ in range(500):
        n, w = rnd.randint(20, 700), rnd.randint(2, 45)
        t = "".join(rnd.choice(common.AZ) for _ in range(n)); k = rnd.sample(range(w), w)
        ct = common.transpo.col_enc(t, k)
        assert decrypt(ct, k) == common.transpo.col_dec(ct, k) == t
    print("colsolve.py: decrypt agrees with transpo.col_dec (500/500)")

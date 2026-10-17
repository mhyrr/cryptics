"""Periodic transposition: letters permuted within consecutive sets of n by one n-letter key
(Givierge 1925, the 4-2-6-3-7-1-5 example). The one survey family that 04 could not exclude.

Cipher set c[j] = p[k[j]]. A partial last set is left out of the score (its handling is unknown).
Search: hill climb on the Spanish quadgram score of the full sets, with swap and insertion moves,
random restarts. Controls: planted held-out telegraph Spanish, same code path, same budget.
Usage (from this folder): python3 -I periodic.py > result.txt
"""
import array, os, random, sys
from concurrent.futures import ProcessPoolExecutor
here = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(here, "..", "01-solver")
sys.path.insert(0, SOLVER); os.chdir(SOLVER)
import plaintext

Q = array.array("f"); Q.fromfile(open("out/lm_es_4.bin", "rb"), 26 ** 4)
RESTARTS, PATIENCE = 12, 1500

def enc(pt, k):
    n = len(k); f = len(pt) // n * n
    return "".join(pt[b + k[j]] for b in range(0, f, n) for j in range(n)) + pt[f:]
def dec(ct, k):
    n = len(k); f = len(ct) // n * n; out = list(ct)
    for b in range(0, f, n):
        for j in range(n): out[b + k[j]] = ct[b + j]
    return "".join(out)
def qscore(texts, k):
    s = c = 0
    for t in texts:
        f = len(t) // len(k) * len(k); v = [ord(x) - 65 for x in dec(t[:f], k)]
        for i in range(len(v) - 3):
            s += Q[((v[i] * 26 + v[i + 1]) * 26 + v[i + 2]) * 26 + v[i + 3]]
        c += len(v) - 3
    return s / c
def solve(texts, n, seed):
    rnd = random.Random(seed); best = (-99, None)
    for _ in range(RESTARTS):
        k = rnd.sample(range(n), n); s = qscore(texts, k); stale = 0
        while stale < PATIENCE:
            m = k[:]; i, j = rnd.sample(range(n), 2) if n > 1 else (0, 0)
            if rnd.random() < 0.5: m[i], m[j] = m[j], m[i]
            else: m.insert(j, m.pop(i))
            t = qscore(texts, m)
            if t > s: k, s, stale = m, t, 0
            else: stale += 1
        if s > best[0]: best = (s, k)
    return best

def job(a):
    kind, n, seed, texts = a
    if kind == "plant":
        rnd = random.Random(seed); k = rnd.sample(range(n), n)
        pts = [plaintext.telegram(L, rnd) for L in texts]
        s, kk = solve([enc(p, k) for p in pts], n, seed)
        f = len(pts[0]) // n * n
        acc = sum(x == y for x, y in zip(dec(enc(pts[0], k), kk)[:f], pts[0][:f])) / f
        return kind, n, len(texts), s, acc, ""
    s, kk = solve(texts, n, seed)
    return kind, n, len(texts), s, None, dec(texts[0], kk)[:80]

def main():
    def load(p): return "".join(c for c in open(os.path.join(here, p)).read().upper() if c.isalpha())
    t1, t2 = load("../../sources/telegram-1.txt"), load("../../sources/telegram-2.txt")
    rnd = random.Random(20261016); jobs = []
    for n in range(2, 41):
        for lens in ((615,), (615, 160)):
            jobs.append(("plant", n, rnd.randrange(10 ** 9), lens))
        jobs.append(("target", n, rnd.randrange(10 ** 9), (t1,)))
        jobs.append(("target", n, rnd.randrange(10 ** 9), (t1, t2)))
    with ProcessPoolExecutor() as ex:
        res = list(ex.map(job, jobs))
    print("| n | plant T1 (score, acc) | plant joint (score, acc) | target T1 | target joint | T1 joint reading, first 80 |")
    print("|---|---|---|---|---|---|")
    by = {(r[0], r[1], r[2]): r for r in res}
    for n in range(2, 41):
        p1, pj, x1, xj = by["plant", n, 1], by["plant", n, 2], by["target", n, 1], by["target", n, 2]
        print(f"| {n} | {p1[3]:.2f}, {p1[4]:.2f} | {pj[3]:.2f}, {pj[4]:.2f} | {x1[3]:.2f} | {xj[3]:.2f} | {xj[5]} |")

if __name__ == "__main__":
    main()

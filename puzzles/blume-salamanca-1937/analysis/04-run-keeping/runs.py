"""Does either telegram keep runs of plaintext? One test for every run-keeping family in the survey.

A transposition that keeps short plaintext runs together leaves the plaintext's letter-pair statistics
in the ciphertext. Statistic: mean Spanish bigram log10 probability per adjacent pair, read forward
and reversed (routes may reverse rows). Each text is compared with 2,000 shuffles of its own letters
(5,000 for the telegrams), so letter frequency does not matter. Plants: telegraph-style held-out
Spanish (01-solver/plaintext.py) under each family, at 615 and 160 letters.
Usage (from this folder): python3 -I runs.py > result.txt
"""
import array, os, random, sys
here = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(here, "..", "01-solver")
sys.path.insert(0, SOLVER)
os.chdir(SOLVER)  # plaintext.py reads its corpus by relative path
import plaintext, transpo

LM = array.array("f"); LM.fromfile(open("out/lm_es_2.bin", "rb"), 26 * 26)
def score(t):
    v = [ord(c) - 65 for c in t]
    return sum(LM[v[i] * 26 + v[i + 1]] for i in range(len(v) - 1)) / (len(v) - 1)
def stat(t): return max(score(t), score(t[::-1]))

def pvalue(t, rnd, sims):
    obs, L, hits = stat(t), list(t), 0
    for _ in range(sims):
        rnd.shuffle(L); hits += stat("".join(L)) >= obs
    return obs, (hits + 1) / (sims + 1)

# --- families (encryption only; each takes plaintext, length-preserving, and a Random) ---
def word_tr(n, rnd):
    w = plaintext.heldout_words("es"); i = rnd.randrange(len(w) - 5000); out = []
    while sum(map(len, out)) < n:
        if w[i] != ".": out.append(w[i])
        i += 1
    rnd.shuffle(out); return "".join(out)[:n]
def rows(pt, w):
    return [pt[i:i + w] for i in range(0, len(pt), w)]
def row_perm(pt, rnd, w):
    r = rows(pt, w); rnd.shuffle(r); return "".join(r)
def serpentine_perm(pt, rnd, w):
    r = [x if k % 2 == 0 else x[::-1] for k, x in enumerate(rows(pt, w))]; rnd.shuffle(r); return "".join(r)
def block_move(pt, rnd, n):
    r = rows(pt, n); full = r[:-1] if len(r[-1]) < n else r; rnd.shuffle(full)
    return "".join(full + (r[-1:] if len(r[-1]) < n else []))
def block_inner(pt, rnd, n):
    k = rnd.sample(range(n), n)
    return "".join("".join(b[j] for j in k if j < len(b)) if len(b) == n else b for b in rows(pt, n))
def grille(pt, rnd, s):
    """Turning grille of side s (even). Text is padded with random letters to whole blocks, then cut."""
    cells = [(i, j) for i in range(s // 2) for j in range(s // 2)]
    rot = lambda p, k: [p, (p[1], s - 1 - p[0]), (s - 1 - p[0], s - 1 - p[1]), (s - 1 - p[1], p[0])][k]
    holes = [rot(c, rnd.randrange(4)) for c in cells]
    order = []
    for k in range(4):
        order += sorted(rot(h, k) for h in holes)
    blk = s * s; padded = pt + "".join(rnd.choice("EAOSNR") for _ in range(-len(pt) % blk)); out = []
    for b in range(0, len(padded), blk):
        g = {}
        for c, p in zip(padded[b:b + blk], order): g[p] = c
        out.append("".join(g[(i, j)] for i in range(s) for j in range(s)))
    return "".join(out)[:len(pt)]
def single_col(pt, rnd, w): return transpo.col_enc(pt, rnd.sample(range(w), w))
def double_col(pt, rnd, w):
    return transpo.double_enc(pt, rnd.sample(range(w), w), rnd.sample(range(w + 1), w + 1))

FAMILIES = [  # (name, encipher(n, rnd), parameter range)
    ("word transposition", lambda n, r, p: word_tr(n, r), [0]),
    ("row permutation, width w", lambda n, r, p: row_perm(plaintext.telegram(n, r), r, p), range(5, 31)),
    ("serpentine rows permuted, width w", lambda n, r, p: serpentine_perm(plaintext.telegram(n, r), r, p), range(5, 31)),
    ("block move, sets of n", lambda n, r, p: block_move(plaintext.telegram(n, r), r, p), range(3, 13)),
    ("letters permuted within sets of n", lambda n, r, p: block_inner(plaintext.telegram(n, r), r, p), range(3, 13)),
    ("turning grille, side s", lambda n, r, p: grille(plaintext.telegram(n, r), r, p), [4, 6, 8]),
    ("NEG CONTROL single columnar, w", lambda n, r, p: single_col(plaintext.telegram(n, r), r, p), range(5, 31)),
    ("NEG CONTROL double columnar, w x w+1", lambda n, r, p: double_col(plaintext.telegram(n, r), r, p), range(8, 16)),
]

def main():
    rnd = random.Random(20261016); TRIALS, SIMS = 20, 2000
    def load(p): return "".join(c for c in open(os.path.join(here, p)).read().upper() if c.isalpha())
    t1, t2 = load("../../sources/telegram-1.txt"), load("../../sources/telegram-2.txt")
    print(f"Statistic: max(forward, reversed) mean Spanish bigram log10 p. Plants: {TRIALS} per family per length,")
    print(f"parameter drawn uniformly; detected = own-shuffle p < 0.01 ({SIMS} shuffles).\n")
    print("| family | n | detected | median p |"); print("|---|---|---|---|")
    for name, enc, prm in FAMILIES:
        for n in (615, 160):
            ps = sorted(pvalue(enc(n, rnd, rnd.choice(list(prm))), rnd, SIMS)[1] for _ in range(TRIALS))
            print(f"| {name} | {n} | {sum(p < 0.01 for p in ps)}/{TRIALS} | {ps[TRIALS // 2]:.4f} |", flush=True)
    print()
    for name, t in (("T1", t1), ("T2", t2)):
        obs, p = pvalue(t, rnd, 5000)
        print(f"{name}: forward {score(t):.4f}, reversed {score(t[::-1]):.4f}, stat {obs:.4f}, p = {p:.4f} (5000 shuffles)")

if __name__ == "__main__":
    main()

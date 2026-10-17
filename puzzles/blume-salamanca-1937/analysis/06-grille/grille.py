"""Turning grille, side 4, on T2 (160 = 10 blocks of 16). Exhaustive: 4^4 = 256 hole patterns
(every starting orientation is itself one of them) x 2 turning directions x grid read by rows or
by columns = 1,024 keys. Each block is enciphered alike. Score: Spanish quadgrams per letter.
The best T2 key is also applied to T1's first 608 letters (38 blocks).
Controls: planted held-out telegraph Spanish, 160 letters, random key, same code path.
Also the inverse use: text written into the grid by rows and read out through the holes.
Usage (from this folder): python3 -I grille.py > result.txt
"""
import array, itertools, os, random, sys
here = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(here, "..", "01-solver")
sys.path.insert(0, SOLVER); os.chdir(SOLVER)
import plaintext

Q = array.array("f"); Q.fromfile(open("out/lm_es_4.bin", "rb"), 26 ** 4)
S = 4
def qscore(t):
    v = [ord(c) - 65 for c in t]
    return sum(Q[((v[i] * 26 + v[i + 1]) * 26 + v[i + 2]) * 26 + v[i + 3]] for i in range(len(v) - 3)) / (len(v) - 3)

def rot(p, k, cw):
    for _ in range(k):
        p = (p[1], S - 1 - p[0]) if cw else (S - 1 - p[1], p[0])
    return p
CELLS = [(i, j) for i in range(S // 2) for j in range(S // 2)]
def keys():
    for choice in itertools.product(range(4), repeat=len(CELLS)):
        for cw in (True, False):
            holes = [rot(c, k, True) for c, k in zip(CELLS, choice)]
            order = []
            for k in range(4):
                order += sorted(rot(h, k, cw) for h in holes)
            for bycol in (False, True):
                yield (choice, cw, bycol), order, bycol

def cell_index(p, bycol): return p[1] * S + p[0] if bycol else p[0] * S + p[1]
def enc(pt, order, bycol):
    out = []
    for b in range(0, len(pt) // 16 * 16, 16):
        g = [None] * 16
        for c, p in zip(pt[b:b + 16], order): g[cell_index(p, bycol)] = c
        out.append("".join(g))
    return "".join(out)
def dec(ct, order, bycol):
    return "".join(ct[b + cell_index(p, bycol)] for b in range(0, len(ct) // 16 * 16, 16) for p in order)

ALL = list(keys())
def best(ct, n=3, f=None):
    f = f or dec
    return sorted(((qscore(f(ct, o, bc)), name, o, bc) for name, o, bc in ALL), key=lambda r: -r[0])[:n]

def main():
    def load(p): return "".join(c for c in open(os.path.join(here, p)).read().upper() if c.isalpha())
    t1, t2 = load("../../sources/telegram-1.txt"), load("../../sources/telegram-2.txt")
    rnd = random.Random(20261016)
    print(f"{len(ALL)} keys. Controls (160 letters):")
    ok = 0
    for i in range(10):
        pt = plaintext.telegram(160, rnd); _, o, bc = rnd.choice(ALL); ct = enc(pt, o, bc)
        s, name, o2, bc2 = best(ct, 1)[0]; hit = dec(ct, o2, bc2) == pt; ok += hit
        print(f"  plant {i}: best {s:.2f}, recovered {hit}, true-text score {qscore(pt):.2f}")
    print(f"controls recovered {ok}/10\n")
    print("T2 top 3:")
    for s, name, o, bc in best(t2):
        print(f"  {s:.3f} {name}  {dec(t2, o, bc)[:64]}  | same key on T1: {qscore(dec(t1, o, bc)):.3f}")
    r = best(t2, len(ALL)); sc = [x[0] for x in r]
    print(f"T2 score distribution over all keys: max {sc[0]:.3f}, median {sc[len(sc)//2]:.3f}, min {sc[-1]:.3f}")
    print("\nInverse use (text written by rows, read through the holes), T2 top 3:")
    for s_, name, o, bc in best(t2, 3, enc):
        print(f"  {s_:.3f} {name}  {enc(t2, o, bc)[:64]}")
    print("\nT1 alone (first 608 letters), top 3:")
    for s, name, o, bc in best(t1[:608]):
        print(f"  {s:.3f} {name}  {dec(t1[:608], o, bc)[:64]}")

if __name__ == "__main__":
    main()

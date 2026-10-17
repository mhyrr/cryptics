"""Could any untested family produce the shared strings of 02? Plant a common opening (or closing)
of L letters in a 615- and a 160-letter telegram, encipher both with one key, and count the distinct
4-grams the two ciphertexts share. Observed (02): 9; letter shuffles give 2.2.

Families: double columnar with long keys (the named wall), single columnar (yardstick; excluded for T1
by Bourdeau), Nihilist on a rectangle (one column key for both messages, rows permuted per message,
read by rows or by columns). Usage (from this folder): python3 -I model.py > result.txt
"""
import os, random, sys
here = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(here, "..", "01-solver")
sys.path.insert(0, SOLVER); os.chdir(SOLVER)
import plaintext, transpo

def shared4(x, y):
    s = {x[i:i + 4] for i in range(len(x) - 3)}
    return len({y[i:i + 4] for i in range(len(y) - 3)} & s)

def nihilist(pt, ck, rnd, bycol):
    w = len(ck); rows = [pt[i:i + w] for i in range(0, len(pt), w)]
    full = [r for r in rows if len(r) == w]; tail = rows[len(full):]
    rnd.shuffle(full)
    grid = ["".join(r[k] for k in ck) for r in full] + tail
    if not bycol:
        return "".join(grid)
    return "".join(r[j] for j in range(w) for r in grid if j < len(r))

def families(rnd):
    def dc(lo, hi):
        def f(a, b):
            w1, w2 = rnd.randint(lo, hi), rnd.randint(lo, hi)
            k1, k2 = rnd.sample(range(w1), w1), rnd.sample(range(w2), w2)
            return transpo.double_enc(a, k1, k2), transpo.double_enc(b, k1, k2)
        return f
    def sc(lo, hi):
        def f(a, b):
            w = rnd.randint(lo, hi); k = rnd.sample(range(w), w)
            return transpo.col_enc(a, k), transpo.col_enc(b, k)
        return f
    def nh(bycol):
        def f(a, b):
            w = rnd.randint(5, 25); ck = rnd.sample(range(w), w)
            return nihilist(a, ck, rnd, bycol), nihilist(b, ck, rnd, bycol)
        return f
    return [("double columnar 16-25 x 16-25", dc(16, 25)), ("double columnar 8-15 x 8-15", dc(8, 15)),
            ("single columnar 5-45 (yardstick)", sc(5, 45)),
            ("Nihilist, read by rows, w 5-25", nh(False)), ("Nihilist, read by columns, w 5-25", nh(True))]

def main():
    rnd = random.Random(20261016); TRIALS, OBS = 60, 9
    print(f"Distinct shared 4-grams between the two ciphertexts; {TRIALS} trials per cell; observed {OBS}.\n")
    print("| family | common text | L | mean | share >= 9 |"); print("|---|---|---|---|---|")
    for name, enc in families(rnd):
        for where in ("opening", "closing"):
            for L in (0, 30, 60, 100):
                if L == 0 and where == "closing": continue
                vals = []
                for _ in range(TRIALS):
                    p2 = plaintext.telegram(160, rnd); p1 = plaintext.telegram(615 - L, rnd)
                    if where == "opening": p1 = p2[:L] + p1
                    else: p1 = p1 + p2[160 - L:] if L else p1
                    c1, c2 = enc(p1, p2); vals.append(shared4(c1, c2))
                lab = "none" if L == 0 else where
                print(f"| {name} | {lab} | {L} | {sum(vals) / TRIALS:.1f} | {sum(v >= OBS for v in vals)}/{TRIALS} |", flush=True)

if __name__ == "__main__":
    main()

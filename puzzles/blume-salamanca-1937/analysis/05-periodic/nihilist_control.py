"""Does periodic.py's solver also recover a Nihilist key read by rows (each row's letters permuted by one
column key, then the rows reordered)? 07 shows this family reproduces the shared strings. If the solver
recovers it, the 05 target result (no candidate, n 2-40) excludes it too.
Score: fraction of full rows whose decrypted letters match the plaintext row they came from.
Usage (from this folder): python3 -I nihilist_control.py > nihilist_control.txt
"""
import os, random, sys
from concurrent.futures import ProcessPoolExecutor
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import periodic  # changes directory to 01-solver
import plaintext

def one(a):
    n, seed, joint = a
    rnd = random.Random(seed); k = rnd.sample(range(n), n)
    pts = [plaintext.telegram(615, rnd)] + ([plaintext.telegram(160, rnd)] if joint else [])
    cts = []
    for p in pts:
        f = len(p) // n * n; rows = [p[i:i + n] for i in range(0, f, n)]; rnd.shuffle(rows)
        cts.append(periodic.enc("".join(rows) + p[f:], k))
    s, kk = periodic.solve(cts, n, seed)
    return n, joint, s, kk == k

def main():
    rnd = random.Random(7); jobs = [(n, rnd.randrange(10 ** 9), j) for n in range(5, 41) for j in (False, True)]
    with ProcessPoolExecutor() as ex:
        res = list(ex.map(one, jobs))
    print("| n | T1-length plant (score, key exact) | joint plant (score, key exact) |"); print("|---|---|---|")
    by = {(r[0], r[1]): r for r in res}
    for n in range(5, 41):
        a, b = by[n, False], by[n, True]
        print(f"| {n} | {a[2]:.2f}, {a[3]} | {b[2]:.2f}, {b[3]} |")
    print(f"\nexact keys: alone {sum(by[n, False][3] for n in range(5, 41))}/36, joint {sum(by[n, True][3] for n in range(5, 41))}/36")

if __name__ == "__main__":
    main()

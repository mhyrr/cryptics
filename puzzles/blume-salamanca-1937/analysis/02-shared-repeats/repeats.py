"""Shared and repeated n-grams in the two telegrams, against letter shuffles.

Bean (cyphersolver issue 37, 15 Oct 2026) argues the telegrams share too many repeated strings for a
double transposition. A double columnar transposition scatters plaintext neighbours, so shared
ciphertext n-grams should occur at the rate of shuffled letters. Usage: python3 repeats.py > result.txt
"""
import os, random
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
def load(p): return "".join(c for c in open(os.path.join(here, p)).read().upper() if c.isalpha())
a, b = load("../../sources/telegram-1.txt"), load("../../sources/telegram-2.txt")

def shared(x, y, n):
    s = {x[i:i + n] for i in range(len(x) - n + 1)}
    return sorted({y[i:i + n] for i in range(len(y) - n + 1) if y[i:i + n] in s})
def selfrep(x, n):
    c = Counter(x[i:i + n] for i in range(len(x) - n + 1)); return sorted(k for k, v in c.items() if v > 1)

rnd = random.Random(20261016); SIMS = 5000
print(f"T1 {len(a)} letters, T2 {len(b)} letters; {SIMS} independent shuffles of each")
for n in (3, 4, 5, 6):
    obs, obs1 = len(shared(a, b, n)), len(selfrep(a, n))
    sim, sim1 = [], []
    for _ in range(SIMS):
        A, B = list(a), list(b); rnd.shuffle(A); rnd.shuffle(B); A, B = "".join(A), "".join(B)
        sim.append(len(shared(A, B, n))); sim1.append(len(selfrep(A, n)))
    p = sum(s >= obs for s in sim) / SIMS; p1 = sum(s >= obs1 for s in sim1) / SIMS
    print(f"n={n}: T1xT2 distinct shared {obs} (shuffle mean {sum(sim)/SIMS:.2f}, p={p:.4f}); "
          f"T1 self-repeats {obs1} (shuffle mean {sum(sim1)/SIMS:.2f}, p={p1:.4f})")
print()
for n in (4,):
    for j in range(len(b) - n + 1):
        for i in range(len(a) - n + 1):
            if a[i:i + n] == b[j:j + n]:
                print(f"{b[j:j+n]}  T2@{j}  T1@{i}")
print("\nNote: APMOEP contributes three overlapping 4-grams (APMO, PMOE, MOEP). Counting runs, not")
print("distinct 4-grams, the independent 4+-letter coincidences are NOCU, APMOEP, OEPM, LNDN, TRSP, RAEA, ISEE.")

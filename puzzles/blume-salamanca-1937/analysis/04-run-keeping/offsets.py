"""Are the T1 - T2 offsets of the shared runs (02) aligned to a common modulus? Look-elsewhere corrected.
Usage: python3 -I offsets.py > offsets.txt
"""
import math, random
PAIRS = [(0, 17), (5, 263), (8, 42), (38, 569), (87, 274), (128, 164), (138, 464)]  # (T2, T1) from 02/result.txt
def best(dd):
    n = len(dd); out = []
    for m in range(2, 41):
        k = sum(x % m == 0 for x in dd)
        out.append((sum(math.comb(n, j) * m ** -j * (1 - 1 / m) ** (n - j) for j in range(k, n + 1)), m, k))
    return min(out)
d = [q - p for p, q in PAIRS]; obs = best(d)
rnd = random.Random(1); S = 20000
hit = sum(best([rnd.randrange(612) - p for p, _ in PAIRS])[0] <= obs[0] for _ in range(S))
print("offsets", d)
print(f"best modulus {obs[1]}: {obs[2]} of {len(d)} offsets divisible, binomial tail {obs[0]:.4f}")
print(f"look-elsewhere p (moduli 2-40, T1 positions uniform, {S} draws): {hit / S:.4f}")

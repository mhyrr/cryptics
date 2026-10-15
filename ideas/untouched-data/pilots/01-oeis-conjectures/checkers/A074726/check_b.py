# A074726 method b: no primitive parts, no PARI factor(). F(n) is split by gcd with the product of all primes
# < B = 10^6 (exact exponents by repeated division); the cofactor C is a BPSW probable prime, 1, or a composite whose
# prime factors all exceed B (abundancy factor < (B/(B-1))^(log C/log B)).
# Abundant (lower bound > 2) cases: Zumkeller witnessed by a unitary divisor u = prefix (ascending primes) of the
# smooth part with an explicit equal-sum divisor split found by bitset subset-sum DP (sigma(u) <= 2^27) or DFS.
# Non-Zumkeller certificate: dominance lemma (see check_a header) with u = prefix of the smooth part, sigma(u) odd.
import time; T0 = time.time()
import sys, os, math; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import gmpy2, cypari2; pari = cypari2.Pari(); pari.allocatemem(10**9)
from sympy import primerange, divisors
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3710
DEADLINE = float(sys.argv[2]) if len(sys.argv) > 2 else 270
T, off = terms("A074726")
B = 10 ** 6
small = list(primerange(2, B)); PB = gmpy2.mpz(1)
for p in small: PB *= p
def split(Fn):
    g = gmpy2.gcd(Fn, PB); K = {}; C = gmpy2.mpz(Fn)
    if g > 1:
        for p in small:
            if p > g: break
            if g % p == 0:
                e = 0
                while C % p == 0: C //= p; e += 1
                K[p] = e
    comp = None
    if C > 1:
        if pari.ispseudoprime(int(C)): K[int(C)] = K.get(int(C), 0) + 1
        else: comp = int(C)
    return K, comp
sg = lambda p, e: (p ** (e + 1) - 1) // (p - 1)
def split_exists(u, su):
    if su % 2 or su < 2 * u: return False
    ds = sorted(divisors(u))
    if su <= 1 << 27:
        bs = 1
        for d in ds: bs |= bs << d
        return (bs >> (su // 2)) & 1 == 1
    ds.reverse(); suf = [0] * (len(ds) + 1)
    for i in range(len(ds) - 1, -1, -1): suf[i] = suf[i + 1] + ds[i]
    stack = [(0, su // 2)]; nodes = 0
    while stack:
        i, r = stack.pop(); nodes += 1
        if nodes > 200000: return None
        if r == 0: return True
        if i == len(ds) or suf[i] < r: continue
        stack.append((i + 1, r))
        if ds[i] <= r: stack.append((i + 1, r - ds[i]))
    return False
a, b = gmpy2.mpz(0), gmpy2.mpz(1)
status = {}; inconclusive = []; cex = []; last = 0; bad = None
for n in range(1, N + 1):
    if time.time() - T0 > DEADLINE: break
    a, b = b, a + b                     # a = F(n)
    K, comp = split(a)
    comps = sorted(K.items()); Kv = 1; sK = 1
    for p, e in comps: Kv *= p ** e; sK *= sg(p, e)
    lower = sK / Kv; upper = lower
    if comp: upper *= (B / (B - 1)) ** (math.log(comp) / math.log(B))
    if upper < 2 - 1e-12: status[n] = (False, False)
    elif lower > 2 + 1e-12:
        z = None; u = 1; su = 1
        for p, e in comps:
            u *= p ** e; su *= sg(p, e)
            if su % 2 == 0 and su >= 2 * u and len(divisors(u)) <= 50000:
                r = split_exists(u, su)
                if r: z = True; break
        if z is None and comp is None and sK % 2 == 1: z = False      # sigma(F) odd
        if z is None:                                                  # dominance certificate
            u = 1; su = 1
            for k, (p, e) in enumerate(comps):
                u *= p ** e; su *= sg(p, e)
                if su % 2 == 0: continue
                rest_ub = 1.0
                for q, f in comps[k + 1:]: rest_ub *= q / (q - 1)
                if comp: rest_ub *= (B / (B - 1)) ** (math.log(comp) / math.log(B))
                if su * (rest_ub - 1) < 1 - 1e-9:
                    z = False; print("n=%d abundant, NOT Zumkeller (dominance, u=%d)" % (n, u), flush=True); break
        status[n] = (True, z)
        if z is None: inconclusive.append(n)
        elif (z is False) != (n == 12): cex.append(n); bad = bad or n
    else:
        status[n] = (None, None); inconclusive.append(n)
    last = n
ab = [n for n in range(1, last + 1) if status[n][0]]
assert ab[:len(T)] == T[:len(ab)]; print("terms OK", min(len(T), len(ab)))
print("n=12:", status.get(12), " abundant count:", len(ab), " inconclusive:", inconclusive[:50], len(inconclusive))
print("all counterexamples (abundant, not Zumkeller, n != 12):", cex)
print("RESULT", ("holds to %d" % last if not inconclusive else "holds to %d except inconclusive n" % last) if bad is None else "COUNTEREXAMPLE n=%d" % bad)

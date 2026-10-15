# A074726: k with sigma(F(k)) > 2 F(k). Conjecture (Farrokhi): sigma(F(n)) > 2F(n) iff F(n) is Zumkeller, except
# n = 12. Verified n <= 371.
# Facts used (stated for audit):
#  * Zumkeller => sigma >= 2F; sigma = 2F (perfect) would be Zumkeller, so a "deficient-or-perfect" proof is only
#    accepted when the abundancy upper bound is < 2 (strict), which also excludes perfect.
#  * If F = u*v with gcd(u, v) = 1 and u is Zumkeller, F is Zumkeller (take A x div(v), B x div(v)).
#  * Practical u with sigma(u) even is Zumkeller (Peng & Bhaskara Rao 2013); else search small unitary divisors u
#    (products of <= 10 of the 12 smallest prime-power components) for an explicit equal-sum divisor partition.
#  * Non-Zumkeller certificate (dominance): if F = u*Q, gcd(u,Q) = 1, sigma(u) odd and sigma(u)*(sigma(Q)-Q) < Q,
#    F is not Zumkeller: a split picks s_q in S(u) for each q | Q with sum q*s_q = sigma(u)sigma(Q)/2, i.e.
#    sum q*t_q = 0 with t_q = 2s_q - sigma(u) odd, |t_q| <= sigma(u); the q = Q term (>= Q) cannot be cancelled.
#  * Primitive part Phi_d = prod_{e|d} F(e)^mu(d/e); its primitive prime factors are == +-1 (mod d) (so >= d-1).
# Method a: factor primitive parts (PARI factor fully if < 10^45, else trial division to 2^24 + BPSW on cofactor);
# unfactored composite cofactors C contribute at most (1 + 1/(L-1))^(log C / log L), L = max(2^24, d-1).
import time; T0 = time.time()
import sys, os, math; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import cypari2; pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
from sympy import divisors, mobius
from fractions import Fraction
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3710
DEADLINE = float(sys.argv[2]) if len(sys.argv) > 2 else 270
T, off = terms("A074726")
F = [0, 1]
while len(F) <= N: F.append(F[-1] + F[-2])
LIM = 1 << 24
prim = {}                      # d -> (dict prime->exp, list of (composite C, L))
def primitive(d):
    if d in prim: return prim[d]
    num, den = 1, 1
    for e in divisors(d):
        m = mobius(d // e)
        if m == 1: num *= F[e]
        elif m == -1: den *= F[e]
    Phi = num // den; assert Phi * den == num
    fac = {}; comps = []
    if Phi > 1:
        if Phi < 10 ** 45:
            M = pari.factor(Phi)
            for p, e in zip(M[0], M[1]): fac[int(p)] = fac.get(int(p), 0) + int(e)
        else:
            M = pari.factor(Phi, LIM)
            for p, e in zip(M[0], M[1]):
                p, e = int(p), int(e)
                if p < LIM or pari.ispseudoprime(p): fac[p] = fac.get(p, 0) + e
                else: comps.append((p ** e, max(LIM, d - 1)))
    prim[d] = (fac, comps); return prim[d]
def sig(fac):
    s = 1
    for p, e in fac.items(): s *= (p ** (e + 1) - 1) // (p - 1)
    return s
def practical(fac):
    ps = sorted(fac)
    if not ps or ps[0] != 2: return False
    s = 1
    for p in ps:
        if p > 1 + s: return False
        s *= (p ** (fac[p] + 1) - 1) // (p - 1)
    return True
def partition_dfs(u, budget=300000):
    """True if divisors of u split into two equal-sum halves, False if exhaustively impossible, None if budget hit."""
    ds = sorted(divisors(u), reverse=True); tot = sum(ds)
    if tot % 2 or tot < 2 * u: return False
    suf = [0] * (len(ds) + 1)
    for i in range(len(ds) - 1, -1, -1): suf[i] = suf[i + 1] + ds[i]
    stack = [(0, tot // 2)]; nodes = 0
    while stack:
        i, r = stack.pop(); nodes += 1
        if nodes > budget: return None
        if r == 0: return True
        if i == len(ds) or suf[i] < r: continue
        stack.append((i + 1, r))                          # skip ds[i] (explored second)
        if ds[i] <= r: stack.append((i + 1, r - ds[i]))   # take ds[i] (explored first: greedy)
    return False
def zumkeller_unitary(fac):
    """Search unitary divisors u of the known part for a Zumkeller one. Returns True, False (only when u = whole
    known part was exhaustively refuted), or None."""
    comps = sorted(fac.items())
    full = None
    from itertools import combinations
    cand = []
    for k in range(1, min(len(comps), 10) + 1):
        for sub in combinations(comps[:12], k):
            tau = 1; u = 1; sg = 1
            for p, e in sub: tau *= e + 1; u *= p ** e; sg *= (p ** (e + 1) - 1) // (p - 1)
            if tau <= 6000 and sg >= 2 * u and sg % 2 == 0: cand.append((tau, u))
    cand.sort()
    for tau, u in cand[:200]:
        if partition_dfs(u, 20000): return True
    return None
def dominance_not_zumkeller(fac, comps):
    comp = sorted(fac.items()); u = 1; su = 1
    for k in range(len(comp)):
        p, e = comp[k]; u *= p ** e; su *= (p ** (e + 1) - 1) // (p - 1)
        if su % 2 == 0: continue
        rest = comp[k + 1:]
        if not comps:
            Q = 1; sQ = 1
            for q, f in rest: Q *= q ** f; sQ *= (q ** (f + 1) - 1) // (q - 1)
            if su * (sQ - Q) < Q: return u
        else:
            ub = 1.0
            for q, f in rest: ub *= q / (q - 1)
            for C, L in comps: ub *= (1 + 1 / (L - 1)) ** (math.log(C) / math.log(L))
            if su * (ub - 1) < 1 - 1e-9: return u
    return None
status = {}; inconclusive = []; bad = None; last = 0; cex = []
for n in range(1, N + 1):
    if time.time() - T0 > DEADLINE: break
    K = {}; comps = []
    for d in divisors(n):
        if d <= 2: continue
        fac, cs = primitive(d)
        for p, e in fac.items(): K[p] = K.get(p, 0) + e
        comps += cs
    Kval = 1
    for p, e in K.items(): Kval *= p ** e
    lower = Fraction(sig(K), Kval)
    upper_f = float(lower)
    for C, L in comps: upper_f *= (1 + 1 / (L - 1)) ** (math.log(C) / math.log(L))
    if not comps: assert Kval == F[n]
    if upper_f < 2 - 1e-12:
        status[n] = (False, False)                    # deficient => not Zumkeller
    elif lower > 2:
        if practical(K) and sig(K) % 2 == 0: z = True
        elif not comps and sig(K) % 2: z = False         # whole F(n) known, sigma odd: not Zumkeller
        else:
            z = zumkeller_unitary(K)
            if z is None:
                z = dominance_not_zumkeller(K, comps)
                if z: print("n=%d: abundant (sigma/F >= %.4f) and NOT Zumkeller by dominance, u=%d" % (n, float(lower), z), flush=True)
                z = False if z else None
        if z is None: inconclusive.append(n)
        status[n] = (True, z)
        if z is False and n != 12:
            bad = n if bad is None else bad; cex.append(n)
        if z is True and n == 12: bad = n; break
        if z is False and n == 12: pass
    else:
        inconclusive.append(n); status[n] = (None, None)
    last = n
ab = [n for n in range(1, last + 1) if status[n][0]]
assert ab[:len(T)] == T[:len(ab)] and (ab[-1] >= T[-1] or last < T[-1]), (ab[:60], T); print("terms OK", len(T))
print("n=12:", status.get(12), " abundant count:", len(ab), " inconclusive:", inconclusive[:50], len(inconclusive))
print("all counterexamples (abundant, not Zumkeller, n != 12):", cex)
print("RESULT", ("holds to %d" % last if not inconclusive else "holds to %d except inconclusive n" % last) if bad is None else "COUNTEREXAMPLE n=%d" % bad)

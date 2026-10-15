"""A242585 check_a: a(n) = tau(A001110(n)) = tau(X^2), X = P_{2n}/2 = P_n*Q_n (Pell numbers), so a(n) = prod (2e+1).
Conjecture: 9 | a(n) for n != 1, 7. Certify 9 | a(n) by exhibiting primes q with exact exponent e = v_q(X) where
(2e+1) carries a factor 3 (e == 1 mod 3; 9 if e == 4 mod 9), until the 3-adic total reaches 2.
Candidate primes: trial division of X by primes < 2*10^5, and the cofactor of each cyclotomic piece
Phi_d = prod_{e|d} P_e^mu(d/e) (d | 2n) after removing small factors: the cofactor if BPSW-prime, else (if < 10^80)
the BPSW-prime pieces of its full PARI factorization (MPQS/ECM).
Exponents are measured directly on X (gmpy2.remove). n not certified are reported (undecided, not counterexamples).
Terms: full factorization of X with sympy for listed n."""
import sys, time; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import gmpy2
from sympy import factorint, divisors, mobius, primerange
import cypari2
pari = cypari2.Pari(); pari.allocatemem(10**9)
ECMDIG = int(sys.argv[3]) if len(sys.argv) > 3 else 75
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
TL = float(sys.argv[2]) if len(sys.argv) > 2 else 280
t0 = time.time()
Pc = {}
def P(k):
    if k not in Pc:
        a, b = gmpy2.mpz(0), gmpy2.mpz(1)
        for _ in range(k): a, b = b, 2 * b + a
        Pc[k] = a
    return Pc[k]
# Pell numbers by iteration once
PP = [gmpy2.mpz(0), gmpy2.mpz(1)]
for k in range(2, 2 * N + 1): PP.append(2 * PP[-1] + PP[-2])
t, off = terms('A242585')
def tau_sq(x):
    r = 1
    for p, e in factorint(int(x)).items(): r *= 2 * e + 1
    return r
assert [tau_sq(PP[2 * n] // 2) for n in range(1, len(t) + 1)] == t; print('terms ok', len(t), flush=True)
SMALL = [gmpy2.mpz(p) for p in primerange(2, 2 * 10**5)]
def v3(x):
    c = 0
    while x % 3 == 0: x //= 3; c += 1
    return c
undec = []; viol_known = []; cert = {}
lastn = 0
for n in range(2, N + 1):
    if time.time() - t0 > TL: break
    lastn = n
    if n == 7: continue
    X = PP[2 * n] // 2; score = 0; used = set()
    Y = X
    for q in SMALL:
        if Y % q == 0:
            Y, e = gmpy2.remove(Y, q)
            score += v3(2 * e + 1); used.add(int(q)); cert.setdefault(n, []).append((int(q), int(e)))
            if score >= 2: break
        if q * q > Y: break
    if score < 2:
        for d in divisors(2 * n):
            if d < 3: continue
            phi = gmpy2.mpz(1); den = gmpy2.mpz(1)
            for e in divisors(d):
                mu = mobius(d // e)
                if mu == 1: phi *= PP[e]
                elif mu == -1: den *= PP[e]
            phi //= den
            for q in used: phi, _ = gmpy2.remove(phi, q)
            pieces = [phi] if phi > 1 else []
            if phi > 1 and not gmpy2.is_bpsw_prp(phi) and phi < gmpy2.mpz(10)**ECMDIG:
                fm = pari.factor(int(phi))
                fs = set(int(x) for x in fm[0])
                rest = phi; pieces = []
                for f in sorted(fs):
                    f = gmpy2.mpz(f); rest, _ = gmpy2.remove(rest, f); pieces.append(f)
                if rest > 1: pieces.append(rest)
            for q in pieces:
                if q > 1 and gmpy2.is_bpsw_prp(q) and int(q) not in used:
                    _, e = gmpy2.remove(X, q)
                    score += v3(2 * e + 1); used.add(int(q)); cert.setdefault(n, []).append((int(q), int(e)))
                    if score >= 2: break
            if score >= 2: break
    if score < 2: undec.append(n)
import json; json.dump({'lastn': lastn, 'cert': {str(k): [[str(q), e] for q, e in v] for k, v in cert.items()}, 'undecided': undec},
                       open(__file__.rsplit('/', 1)[0] + '/cert.json', 'w'))
print('first undecided n:', undec[0] if undec else None)
print('n checked 2..%d (excluding 7); certified all but %d undecided n' % (lastn, len(undec)), undec[:20])

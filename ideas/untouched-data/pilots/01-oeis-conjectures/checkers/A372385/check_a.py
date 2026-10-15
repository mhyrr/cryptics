# A372385: a(n) = det[Jacobi(i-j,2n+1)]_{0<i,j<n}. Sun's conjectures (checked n<=1000, i.e. p=2n+1<=2001):
# Conj 1 (p==1 mod 4): det[x+(i-j/p)]_{0<i,j<n} = r-2s+(-1)^(n/2) x(2r-ps), det[x+(i-j/p)]_{0<=i,j<=n} = -r+(-1)^(n/2) p s x,
#   where eps^((2-(2/p))h) = r+s*sqrt(p), eps/h = fundamental unit / class number of Q(sqrt p).
# Conj 2 (p>3): with eps^h = a+b*sqrt(p): det[x+(i+j/p)]_{0<i,j<n} = (-1)^(n/2)2^(n-1)(b-ax) (p==1 mod 4), 2^(n-1)x (p==3 mod 4);
#   det[x+(i+j/p)]_{0<=i,j<n} = (-1)^(n/2)2^(n-1)(2b-a+x(pb-2a)) (p==1 mod 4), -2^(n-1)(2x+1) (p==3 mod 4).
# det(M+xJ) is linear in x, so each identity is checked through det(M) and det(M+J).
# Method a: python-flint nmod_mat determinants mod a 62-bit prime (mismatch = proof of failure; agreement = evidence);
# eps from the continued fraction of (1+sqrt p)/2 (first convergent with X^2-pY^2=+-4); h from the analytic class number
# formula (mpmath, rounded, asserted near-integral).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import flint, mpmath
from sympy import jacobi_symbol, primerange
from math import isqrt
mpmath.mp.dps = 40
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2300
PMIN = int(sys.argv[2]) if len(sys.argv) > 2 else 2001
q = (1 << 62) - 57; i2 = pow(2, -1, q)
_tab = {}
def J(a, m):   # Jacobi symbol; for prime m a table of squares mod m (cached), else sympy
    t = _tab.get(m)
    if t is None:
        from sympy import isprime
        if isprime(m):
            t = [-1] * m; t[0] = 0
            for x in range(1, m): t[x * x % m] = 1
        else: t = [int(jacobi_symbol(r, m)) for r in range(m)]
        _tab[m] = t
    return t[a % m]
def unit(p):   # p == 1 mod 4: returns (X, Y) with eps = (X + Y sqrt p)/2
    P, Q = 1, 2; h0, h1 = 1, 0; k0, k1 = 0, 1; s = isqrt(p)
    while True:
        a = (P + s) // Q
        h0, h1 = a * h0 + h1, h0; k0, k1 = a * k0 + k1, k0
        X, Y = 2 * h0 - k0, k0
        if X * X - p * Y * Y in (4, -4): return X, Y
        P = a * Q - P; Q = (p - P * P) // Q
def classno(p, X, Y):
    leps = mpmath.log((X + Y * mpmath.sqrt(p)) / 2)
    S = -sum(J(a, p) * mpmath.log(mpmath.sin(mpmath.pi * a / p)) for a in range(1, p)) / (2 * leps)
    h = int(mpmath.nint(S)); assert abs(S - h) < 1e-10, (p, S); return h
def powq(X, Y, e, p):   # ((X+Y sqrt p)/2)^e mod q as (A, B) meaning A + B sqrt p
    A, B = 1, 0; bA, bB = X * i2 % q, Y * i2 % q
    while e:
        if e & 1: A, B = (A * bA + p * B * bB) % q, (A * bB + B * bA) % q
        bA, bB = (bA * bA + p * bB * bB) % q, (2 * bA * bB) % q; e >>= 1
    return A, B
def lin(rows):   # (det M, det(M+J) - det M) mod q
    d0 = int(flint.nmod_mat(rows, q).det()); d1 = int(flint.nmod_mat([[v + 1 for v in r] for r in rows], q).det())
    return d0, (d1 - d0) % q
T, off = terms("A372385")
assert [int(flint.fmpz_mat([[J(i - j, 2 * n + 1) for j in range(1, n)] for i in range(1, n)]).det()) for n in range(2, 2 + len(T))] == T; print("terms OK", len(T))
bad = []; cnt = 0
for p in primerange(max(5, PMIN), PMAX):
    n = (p - 1) // 2; sg = 1 if (n // 2) % 2 == 0 else -1
    m1a = [[J(i - j, p) for j in range(1, n)] for i in range(1, n)]
    m2a = [[J(i + j, p) for j in range(1, n)] for i in range(1, n)]
    m2b = [[J(i + j, p) for j in range(0, n)] for i in range(0, n)]
    tw = pow(2, n - 1, q)
    if p % 4 == 1:
        X, Y = unit(p); h = classno(p, X, Y)
        r, s = powq(X, Y, (2 - J(2, p)) * h, p); a, b = powq(X, Y, h, p)
        m1b = [[J(i - j, p) for j in range(0, n + 1)] for i in range(0, n + 1)]
        ok = lin(m1a) == ((r - 2 * s) % q, sg * (2 * r - p * s) % q) and lin(m1b) == ((-r) % q, sg * p * s % q)
        ok = ok and lin(m2a) == (sg * tw * b % q, (-sg * tw * a) % q) and lin(m2b) == (sg * tw * (2 * b - a) % q, sg * tw * (p * b - 2 * a) % q)
    else:
        ok = lin(m2a) == (0, tw) and lin(m2b) == ((-tw) % q, (-2 * tw) % q)
    if not ok: bad.append(p); print("FAIL", p, flush=True)
    cnt += 1
print("tested %d primes in [%d,%d)" % (cnt, PMIN, PMAX))
print("RESULT", "holds (mod q) for p<%d" % PMAX if not bad else "COUNTEREXAMPLE p=%s" % bad[:5])

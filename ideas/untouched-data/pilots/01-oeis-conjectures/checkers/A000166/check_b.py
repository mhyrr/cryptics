# A000166 method b: power-residue sieve. For each prime exponent k <= log2 a(n), pick primes q == 1 (mod k);
# if a(n) mod q is nonzero and not a k-th power residue (r^((q-1)/k) != 1 mod q) then a(n) is not a k-th power.
# Residues a(n) mod q are carried by the recurrence a(n) = n a(n-1) + (-1)^n (from round(n!/e) definition check).
# Any exponent not excluded is settled by an exact integer k-th root (gmpy2.iroot) of the exact a(n).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import numpy as np, gmpy2, math
from sympy import primerange, isprime
import mpmath
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
T, off = terms("A000166")
mpmath.mp.dps = 80
chk = [1] + [int(mpmath.nint(mpmath.factorial(n) / mpmath.e)) for n in range(1, len(T))]
assert chk == T; print("terms OK", len(T))
KMAX = int(sum(math.log2(i) for i in range(1, N + 1))) + 2
Q, E, Kof = [], [], []
for k in primerange(2, KMAX + 1):
    need = 24 if k == 2 else (6 if k < 50 else 3); m = 1; got = 0
    while got < need:
        q = m * k + 1
        if q > 2**31: break
        if q > 3 and isprime(q): Q.append(q); E.append((q - 1) // k); Kof.append(k); got += 1
        m += 1
Q = np.array(Q, np.int64); E = np.array(E, np.int64); Kof = np.array(Kof, np.int64)
ks, starts = np.unique(Kof, return_index=True)
def vpow(b, e, m):
    r = np.ones_like(b); b = b % m; e = e.copy()
    while e.any():
        odd = (e & 1).astype(bool)
        r = np.where(odd, (r * b) % m, r); b = (b * b) % m; e >>= 1
    return r
R = np.ones_like(Q)          # a(0) = 1 mod q
a = gmpy2.mpz(1); hits = []; exact_checks = 0
for n in range(1, N + 1):
    R = (n * R + (1 if n % 2 == 0 else -1)) % Q
    a = n * a + (-1) ** n
    if n < 3: continue
    bits = int(a).bit_length()
    sel = Kof <= bits
    t = vpow(R[sel], E[sel], Q[sel])
    excl = (t != 1) & (R[sel] != 0)
    ex_k = np.logical_or.reduceat(excl, starts[ks <= bits]) if sel.any() else np.array([])
    for k in ks[ks <= bits][~ex_k]:
        exact_checks += 1
        if gmpy2.iroot(a, int(k))[1]: hits.append(n); break
print("perfect powers at n =", hits, "exact root checks:", exact_checks)
bad = [n for n in hits if n != 4]
print("RESULT", "holds to %d" % N if not bad else "COUNTEREXAMPLE n=%d" % bad[0])

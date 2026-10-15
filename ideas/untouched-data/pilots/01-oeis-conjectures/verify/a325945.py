# Third check, main thread: smallest q forming a "pure idempotent product" with the n-th composite squarefree p.
# Definition (A325945/A306330): p, q coprime, squarefree, composite, non-Carmichael, and lambda(pq) | (p-1)(q-1).
# Brute force over q from 2, using sympy's carmichael lambda (reduced_totient).
import sympy
from sympy.ntheory import reduced_totient as lam
def sqf(n): return all(e == 1 for e in sympy.factorint(n).values())
def carm(n): return n > 2 and not sympy.isprime(n) and sqf(n) and (n - 1) % lam(n) == 0
def pure_ok(n): return n > 3 and not sympy.isprime(n) and sqf(n) and not carm(n)
P = [n for n in range(4, 200) if pure_ok(n)][:18]
data = [217,21,265,91,10,217,217,4537,91,65,703,9685,703,7885,133,217,21,10]
for i, (p, d) in enumerate(zip(P, data), 1):
    q = next(q for q in range(4, 10**6) if sympy.gcd(p, q) == 1 and pure_ok(q) and ((p-1)*(q-1)) % lam(p*q) == 0)
    print(f"n={i} p={p} data={d} brute={q}" + ("" if q == d else "   <-- MISMATCH"))

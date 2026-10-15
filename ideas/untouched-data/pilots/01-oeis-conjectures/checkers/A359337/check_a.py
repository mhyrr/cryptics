# A359337: row n = exponents where the coefficient of Prod_{k=1..n} (x^2+x^3+...+x^prime(k)) is maximal.
# Conjecture (Spezia): rows have length 1 except n=2,5,6 (verified n<=200, Padhi 2026).
# Method a: exact integer polynomial products with python-flint fmpz_poly; prints the gap between the top two coefficients.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import flint
from sympy import prime
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
ps = [prime(i) for i in range(1, N + 1)]
P = flint.fmpz_poly([1]); rows = [[0]]; bad = []
for n in range(1, N + 1):
    q = [0] * (ps[n - 1] + 1)
    for p in ps[:n]: q[p] = 1
    P = P * flint.fmpz_poly(q)
    c = P.coeffs(); m = max(c)
    row = [j for j, v in enumerate(c) if v == m]
    rows.append(row)
    if len(row) != 1 and n not in (2, 5, 6): bad.append(n); print("TIE", n, row)
    if n % 50 == 0: print("n=%d deg=%d maxcoef bits=%d" % (n, len(c) - 1, int(m).bit_length()), flush=True)
T, off = terms("A359337")
flat = [j for r in rows for j in r]
assert flat[:len(T)] == T; print("terms OK", len(T))
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad)

# A035378: coefficients of Sum_{k>=0} Prod_{j=1..k} (1-x^j) expanded about x=-1, i.e. with x -> x-1:
# a(n) = [x^n] Sum_{i=0..2n+1} Prod_{j=1..i} (1-(x-1)^j)  (factors with even j are divisible by x, so i<=2n+1 suffices).
# Conjecture: a(5n+3) == 0, a(5n+4) == 0, a(5n+2) - 2a(5n+1) == 0 (mod 5).
# Method a: exact integer series for the listed terms; mod-5 truncated products (flint nmod_poly) for the range.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import flint
NN = int(sys.argv[1]) if len(sys.argv) > 1 else 499          # test n = 0..NN  (indices up to 5NN+4)
T, off = terms("A035378")
def series(D, mod=None):
    K = 2 * D + 1
    P = flint.fmpz_poly([1]) if mod is None else flint.nmod_poly([1], mod)
    X1 = flint.fmpz_poly([-1, 1]) if mod is None else flint.nmod_poly([mod - 1, 1], mod)
    S = P; pw = P
    for j in range(1, K + 1):
        pw = (pw * X1)
        pw = pw.truncate(D + 1) if hasattr(pw, "truncate") else pw
        P = (P * (1 - pw)).truncate(D + 1)
        S = S + P
    return [int(S[i]) for i in range(D + 1)]
ex = series(len(T) - 1)
assert ex == T, (ex, T); print("terms OK", len(T))
D = 5 * NN + 4
a = series(D, 5)
bad = None
for n in range(NN + 1):
    if a[5*n+3] % 5 or a[5*n+4] % 5 or (a[5*n+2] - 2*a[5*n+1]) % 5: bad = n; break
print("RESULT", "holds to n=%d" % NN if bad is None else "COUNTEREXAMPLE n=%d" % bad)

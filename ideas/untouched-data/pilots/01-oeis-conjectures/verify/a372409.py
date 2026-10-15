# Third check, main thread: A372409 Conjecture 2, exact integer determinants (sympy), small primes.
# S(p): [J(i+j,p)] for 1<=i,j<=(p-3)/2; T(p): same for 0<=i,j<=(p-3)/2; first row replaced by 1s.
# Prints det S, det T and the stated value 2^((p-5)/2)*s(p).
import sympy
from sympy import Matrix, jacobi_symbol as J
def M(lo, hi, p):
    r = range(lo, hi + 1)
    return Matrix([[1 if i == lo else J(i + j, p) for j in r] for i in r])
def s(p):
    if p % 4 == 1: return (-1) ** ((p + 3) // 4)
    h = sympy.ntheory.residue_ntheory  # class number h(-p) for p == 3 mod 4, p > 3: h = (sum of non-residues - sum of residues)/p
    res = sum(a for a in range(1, p) if J(a, p) == 1); non = sum(a for a in range(1, p) if J(a, p) == -1)
    return (-1) ** (((non - res) // p - 1) // 2)
for p in sympy.primerange(5, 60):
    k = (p - 3) // 2
    dS, dT = M(1, k, p).det(), M(0, k, p).det()
    print(f"p={p} detS={dS} detT={dT} stated={2**((p-5)//2)*s(p)}  S==-T:{dS==-dT}  T==-2S:{dT==-2*dS}")

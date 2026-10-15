# A182372 checker b: A182372 by scanning elements 0,1,2,... with state (k-1 in S, k in S), adding k to the perimeter
# when k in S and not both neighbours are; A227134/A227135 from Hanna's g.f.s
#   1/(1-x) + Sum_{m>=2} x^q(m+1) / Prod_{k<=m}(1-x^k),   1/(1-x) + Sum_{m>=2} x^(q(m+2)-1) / Prod_{k<=m}(1-x^k),
# q(j) = floor(j/2)*ceil(j/2).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import numpy as np, hashlib
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 12000
def zeros(): return np.array([0] * (N + 1), dtype=object)
def shift(X, c):
    Y = zeros()
    if c <= N: Y[c:] = X[:N + 1 - c]
    return Y
# state[(p,c)] : p = (k-1 in S), c = (k in S); start k=0: -1 not in S, 0 in S or not
st = {(0, 0): zeros(), (0, 1): zeros()}
st[(0, 0)][0] = 1; st[(0, 1)][0] = 1
for k in range(0, N + 1):
    new = {(0, 0): zeros(), (0, 1): zeros(), (1, 0): zeros(), (1, 1): zeros()}
    last = (k == N)
    for (p, c), W in st.items():
        for nx in ((0,) if last else (0, 1)):  # nx = (k+1 in S); elements > N cannot occur
            add = k if (c and not (p and nx)) else 0
            new[(c, nx)] = new[(c, nx)] + (shift(W, add) if add else W)
    st = new
A = sum(st.values(), zeros())
check_terms("A182372", lambda n: int(A[n]))
q = lambda j: (j // 2) * ((j + 1) // 2)
def hanna(off):
    S = zeros(); S[:] = 1                     # 1/(1-x)
    P = zeros(); P[0] = 1
    P = np.cumsum(P)                          # 1/(1-x)
    m = 2
    while True:
        P = P.copy()
        for i in range(m, N + 1): P[i] += P[i - m]   # divide by (1-x^m)
        e = q(m + 1) if off == 134 else q(m + 2) - 1
        if e > N: break
        S = S + shift(P, e); m += 1
    return S
P134 = hanna(134); P135 = hanna(135)
check_terms("A227134", lambda n: int(P134[n])); check_terms("A227135", lambda n: int(P135[n]))
bad = [n for n in range(N + 1) if A[n] != P134[n] + P135[n]]
print("N =", N, "mismatches:", bad[:10], "| md5 A182372(0..N):", hashlib.md5(str(list(A)).encode()).hexdigest())

"""check_b engine: same e.g.f. but binomial rows mod M built by Pascal's rule (numpy), g_k from exact
big-integer factorials reduced mod M."""
import numpy as np
from egf_common import gdict

def run(anum, M, N):
    g = {k: v % M for k, v in gdict(anum, N + 1).items()}
    idx = np.array(sorted(k for k in g if g[k]), dtype=np.int64)   # k1 values
    gv = np.array([g[k] for k in idx], dtype=np.int64)
    a = np.zeros(N + 1, dtype=np.int64); a[0] = 1
    row = np.zeros(N + 2, dtype=np.int64); row[0] = 1  # C(n, .) for n = 0
    for n in range(N):
        sel = idx - 1 <= n
        ks = idx[sel] - 1
        a[n + 1] = int(np.sum(row[ks] * gv[sel] % M * a[n - ks] % M) % M)
        row[1:n + 2] = (row[1:n + 2] + row[0:n + 1]) % M   # -> C(n+1, .)
    return a.tolist()

def exact_terms(anum, L):
    """Exact a(n) via ordinary series exp: n*b_n = sum_k k*G_k*b_{n-k} with G_k = g_k/k! (Fractions), a(n)=n!*b_n."""
    from fractions import Fraction
    from math import factorial
    g = gdict(anum, L); G = {k: Fraction(v, factorial(k)) for k, v in g.items()}
    b = [Fraction(1)]
    for n in range(1, L):
        b.append(sum(k * G[k] * b[n - k] for k in G if k <= n) / n)
    out = [x * factorial(i) for i, x in enumerate(b)]
    assert all(x.denominator == 1 for x in out)
    return [int(x) for x in out]

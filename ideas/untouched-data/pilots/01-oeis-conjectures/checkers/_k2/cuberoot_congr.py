"""Shared engine for A111984, A193236, A193237 (batch 2).
A(x) = S(x)^alpha, S(x) = sum_k c_k x^(k(k+1)/2), alpha = +1/3 or -1/3.
method 'a': for each modulus m in (5,7) compute A mod m from A^3 = S^(3*alpha) by solving 3*a_n = R_n - (...)
            with numpy dot products (3 invertible mod 5, 7); exact data terms via the same scheme in Python ints.
method 'b': exact big integers from the logarithmic-derivative recurrence n*a_n = sum_j ((alpha+1)j - n) s_j a_{n-j}.
Conjecture tested: a(5n+4) == 0 mod 5 and (if asked) a(7n+5) == 0 mod 7.
"""
import sys, os
from fractions import Fraction
sys.path.insert(0, os.path.dirname(__file__))
from k2common import terms, offset

def S_coeffs(coef, N):
    s = [0] * (N + 1); k = 0
    while k * (k + 1) // 2 <= N:
        s[k * (k + 1) // 2] = coef(k); k += 1
    return s

def method_a_exact(s, sign, N):
    # sign=+1: A^3 = S ; sign=-1: A^3 = 1/S
    R = s[:]
    if sign < 0:
        inv = [0] * (N + 1); inv[0] = 1
        nz = [j for j in range(1, N + 1) if s[j]]
        for n in range(1, N + 1):
            inv[n] = -sum(s[j] * inv[n - j] for j in nz if j <= n)
        R = inv
    a = [1] + [0] * N; B = [1] + [0] * N
    for n in range(1, N + 1):
        t = R[n] - sum(a[i] * a[n - i] for i in range(1, n)) - sum(a[i] * B[n - i] for i in range(1, n))
        assert t % 3 == 0
        a[n] = t // 3
        B[n] = 2 * a[n] + sum(a[i] * a[n - i] for i in range(1, n))
    return a

def method_a_mod(s, sign, N, m):
    import numpy as np
    s = np.array([x % m for x in s], dtype=np.int64)
    if sign < 0:
        inv = np.zeros(N + 1, dtype=np.int64); inv[0] = 1
        nz = np.nonzero(s[1:])[0] + 1
        for n in range(1, N + 1):
            js = nz[nz <= n]
            inv[n] = (-int(np.dot(s[js], inv[n - js]))) % m
        R = inv
    else:
        R = s
    i3 = pow(3, -1, m)
    a = np.zeros(N + 1, dtype=np.int64); B = np.zeros(N + 1, dtype=np.int64); a[0] = B[0] = 1
    for n in range(1, N + 1):
        aa = int(np.dot(a[1:n], a[n - 1:0:-1])) if n > 1 else 0
        ab = int(np.dot(a[1:n], B[n - 1:0:-1])) if n > 1 else 0
        a[n] = ((int(R[n]) - aa - ab) * i3) % m
        B[n] = (2 * int(a[n]) + aa) % m
    return a

def method_b(s, alpha, N):
    # exact: 3n a_n = sum_j (3(alpha+1) j - 3n) s_j a_{n-j}, with 3*alpha in {+1,-1}
    th = int(3 * alpha)  # +1 or -1
    nz = [j for j in range(1, N + 1) if s[j]]
    a = [1] + [0] * N
    for n in range(1, N + 1):
        t = 0
        for j in nz:
            if j > n: break
            t += ((th + 3) * j - 3 * n) * s[j] * a[n - j]
        q, r = divmod(t, 3 * n); assert r == 0
        a[n] = q
    return a

def run(anum, coef, sign, method, N, mods):
    T = terms(anum); o = offset(anum); assert o == 0
    s_small = S_coeffs(coef, len(T) - 1)
    if method == "a":
        exact = method_a_exact(s_small, sign, len(T) - 1)
    else:
        exact = method_b(s_small, Fraction(sign, 3), len(T) - 1)
    assert exact == T, "data mismatch"
    print(f"{anum} method {method}: reproduced all {len(T)} data terms")
    s = S_coeffs(coef, N)
    res = {}
    if method == "b":
        A = method_b(s, Fraction(sign, 3), N)
    for (m, r) in mods:
        am = method_a_mod(s, sign, N, m) if method == "a" else [x % m for x in A]
        idx = list(range(r, N + 1, m))
        bad = [n for n in idx if am[n] % m]
        res[(m, r)] = bad
        print(f"  a({m}n+{r}) == 0 mod {m} for indices <= {N}: tested {len(idx)} indices (n <= {(N - r)//m}); failures: {bad[:10]}")
        import hashlib
        print("  hash of residues mod", m, hashlib.md5(bytes(int(x) % m for x in am)).hexdigest())
    return res

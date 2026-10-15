"""A293462 check_b: A_n (n x n, A(i,j)=1 iff i+j is a perfect power) is the leading block of A_N (Hankel), so
det(A_n - phi*I) for ALL n <= N comes from one elimination of A_N - phi*I over GF(p), p = 1 or 4 mod 5 so sqrt(5) and
phi = (1+sqrt5)/2 live in GF(p). Elimination without row exchange, using an s x s block pivot when leading minors vanish.
det_n != 0 mod p proves phi is not an eigenvalue of A_n (phi and its conjugate are eigenvalues together since A_n is
integral). n with det_n == 0 mod p for two different primes are reported as candidates; terms reproduced by counting."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from sympy import sqrt_mod, isprime, perfect_power
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 5000

def is_pp(k):  # perfect power incl. 1
    return k == 1 or perfect_power(k) is not False
PP = np.array([1 if is_pp(k) else 0 for k in range(2 * N + 3)], dtype=np.int64)
t, off = terms('A293462')
cnt = [sum(PP[i + j] for i in range(1, n + 1) for j in range(1, n + 1)) for n in range(1, len(t) + 1)]
assert cnt == t; print('terms ok', len(t))

@nb.njit(cache=True)
def inv(a, p):
    r = 1; e = p - 2; a %= p
    while e:
        if e & 1: r = r * a % p
        a = a * a % p; e >>= 1
    return r

@nb.njit(cache=True)
def minors_zero(PP, N, phi, p):
    S = np.empty((N, N), np.int64)
    for i in range(N):
        for j in range(N):
            S[i, j] = PP[i + j + 2]
        S[i, i] = (S[i, i] - phi) % p
    zero = np.zeros(N + 1, np.uint8)
    k = 0
    while k < N:
        # find smallest s with det(S[k:k+s, k:k+s]) != 0, via elimination on a copy of growing blocks
        s = 1
        while True:
            B = S[k:k + s, k:k + s].copy()
            d = 1
            for c in range(s):
                r = -1
                for q in range(c, s):
                    if B[q, c] != 0: r = q; break
                if r < 0: d = 0; break
                if r != c:
                    for q in range(s): B[c, q], B[r, q] = B[r, q], B[c, q]
                    d = (p - d) % p
                d = d * B[c, c] % p
                iv = inv(B[c, c], p)
                for q in range(c + 1, s):
                    f = B[q, c] * iv % p
                    if f:
                        for w in range(c, s): B[q, w] = (B[q, w] - f * B[c, w]) % p
            if d != 0: break
            zero[k + s] = 1   # leading minor of size k+s is 0
            s += 1
            if k + s > N: return zero
        # eliminate with s x s pivot block: Binv via Gauss-Jordan
        Bm = S[k:k + s, k:k + s].copy(); Binv = np.zeros((s, s), np.int64)
        for q in range(s): Binv[q, q] = 1
        for c in range(s):
            r = c
            while Bm[r, c] == 0: r += 1
            for q in range(s):
                Bm[c, q], Bm[r, q] = Bm[r, q], Bm[c, q]; Binv[c, q], Binv[r, q] = Binv[r, q], Binv[c, q]
            iv = inv(Bm[c, c], p)
            for q in range(s): Bm[c, q] = Bm[c, q] * iv % p; Binv[c, q] = Binv[c, q] * iv % p
            for q in range(s):
                if q != c and Bm[q, c]:
                    f = Bm[q, c]
                    for w in range(s): Bm[q, w] = (Bm[q, w] - f * Bm[c, w]) % p; Binv[q, w] = (Binv[q, w] - f * Binv[c, w]) % p
        # W = Binv * S[k:k+s, k+s:]
        m0 = k + s
        W = np.zeros((s, N - m0), np.int64)
        for a in range(s):
            for b in range(s):
                if Binv[a, b]:
                    for c in range(N - m0): W[a, c] = (W[a, c] + Binv[a, b] * S[k + b, m0 + c]) % p
        for i in range(m0, N):
            for b in range(s):
                f = S[i, k + b]
                if f:
                    for c in range(N - m0): S[i, m0 + c] = (S[i, m0 + c] - f * W[b, c]) % p
        k += s
    return zero

res = []
for p in (2147483629, 2147483579):
    assert isprime(p) and p % 5 in (1, 4)
    r5 = sqrt_mod(5, p); phi = (1 + r5) * pow(2, -1, p) % p
    z = minors_zero(PP, N, phi, p)
    res.append(set(int(n) for n in np.nonzero(z)[0] if n >= 1))
cand = sorted(res[0] & res[1])
print('N', N, 'n with det(A_n - phi I) == 0 mod both primes:', cand, '| only one prime:', sorted(res[0] ^ res[1]))

# A364332, method b: segmented. For each block of n=p-1, divide out every prime q<=sqrt(X) (trial division by sieve),
# take the max of f(q); the leftover cofactor (a prime > sqrt X, < p) is looked up in a dense f-table indexed by odd numbers.
# Primality of p from a separate segmented Eratosthenes sieve.
import sys, os, math; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
X = int(sys.argv[1]) if len(sys.argv) > 1 else 1432349099
A082449, _ = terms("A082449")
@njit(cache=True)
def run(X, nfirst):
    R = int(math.sqrt(X)) + 2
    small = np.ones(R + 1, np.bool_); small[:2] = False
    for i in range(2, int(math.sqrt(R)) + 1):
        if small[i]:
            for j in range(i * i, R + 1, i): small[j] = False
    sp = np.nonzero(small)[0]
    fodd = np.zeros(X // 2 + 2, np.uint8)      # f(q)+1 for odd q, index q//2 ; f(2)=0 kept separately
    least = np.zeros(64, np.int64); firstf = np.zeros(nfirst, np.int64); cnt = 0
    least[0] = 2; firstf[0] = 0; cnt = 1
    BS = 1 << 22
    L = 3
    while L <= X:                            # block of p in [L, H); block length <= L so every prime factor of p-1 is < L
        H = min(L + min(BS, L), X + 1)
        isp = np.ones(H - L, np.bool_)
        for q in sp:
            if q * q >= H: break
            st = max(q * q, ((L + q - 1) // q) * q)
            for j in range(st, H, q): isp[j - L] = False
        # factor n = p-1 for n in [L-1, H-1)
        rem = np.arange(L - 1, H - 1).astype(np.int64)
        mx = np.zeros(H - L, np.int64)
        for q in sp:
            if q > H: break
            fq = 0 if q == 2 else np.int64(fodd[q // 2]) - 1
            st = ((L - 1 + q - 1) // q) * q
            for j in range(st, H - 1, q):
                k = j - (L - 1)
                while rem[k] % q == 0: rem[k] //= q
                if fq > mx[k]: mx[k] = fq
        for k in range(H - L):
            p = L + k
            if not isp[k] or p % 2 == 0: continue
            m = mx[k]
            r = rem[k]
            if r > 1:
                fr = 0 if r == 2 else np.int64(fodd[r // 2]) - 1
                if fr > m: m = fr
            f = m + 1
            # p-1 >= 2 always has a prime factor, so f>=1 for odd p
            fodd[p // 2] = f + 1
            if least[f] == 0: least[f] = p
            if cnt < nfirst: firstf[cnt] = f; cnt += 1
        L = H
    return least, firstf
least, firstf = run(X, 200)
T, off = terms("A364332")
assert list(firstf[:len(T)]) == T; print("terms OK", len(T))
for m in range(0, 30):
    if least[m]: print("m=%d least prime %d  A082449(m)=%s" % (m, least[m], A082449[m] if m < len(A082449) else "?"))
ms = [m for m in range(len(A082449)) if A082449[m] <= X]
bad = [m for m in ms if least[m] != A082449[m]]
print("decided for m <=", max(ms))
print("RESULT", "holds for m<=%d" % max(ms) if not bad else "COUNTEREXAMPLE m=%s (least p=%d vs A082449=%d)" % (bad[0], least[bad[0]], A082449[bad[0]]))

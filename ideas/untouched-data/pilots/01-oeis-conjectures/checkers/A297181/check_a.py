"""A297181 check_a (base 11): certify a(n) = least x>0 of word length n w.r.t. {+-11^k} for every n <= N, where a(n) comes from
Colin Barker's conjectured recurrence; certification: L(a(n)) = n and max_{x<a(n)} L(x) = n-1 (see _k3/cayley_a.py)."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np
from oeisterms import terms
from cayley_a import L, maxL_below
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
b = 11; k = b // 2
t, off = terms('A297181')
a = [None] + t[:k + 1]
while len(a) <= N: n = len(a); a.append(a[n - 1] + b * a[n - k] - b * a[n - k - 1])
assert a[1:len(t) + 1] == t, 'recurrence does not reproduce data'
# brute-force least x with L(x)=n for small n, from the definition
small = {}
x = 1
while x < a[min(len(t), 22)] + 1 and x < 3 * 10**6:
    l = L(x, b)
    if l not in small: small[l] = x
    x += 1
assert all(small[n] == t[n - 1] for n in small if n <= len(t)), 'brute force disagrees'
print('terms ok', len(t), '(brute force for n <=', max(small), ')')
bad = []
for n in range(1, N + 1):
    X = a[n]; dig = []
    while X: X, d = divmod(X, b); dig.append(d)
    if not (L(a[n], b) == n and maxL_below(np.array(dig, np.int64), b) == n - 1): bad.append(n)
print('N', N, 'failures', bad[:10])

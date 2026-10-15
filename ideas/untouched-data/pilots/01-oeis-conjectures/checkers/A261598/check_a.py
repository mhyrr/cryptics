"""A261598 check_a: a(n) = product of base-60 digits of Fibonacci(n). Conjecture: a(n)=0 for n>3329.
Fibonacci pairs kept mod 60^K (K=200) to find a zero digit among the low K base-60 digits; if none
(or F(n) < 60^K) look at the low 2000 digits of the exact F(n), then all digits (pure-Python divmod)."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 360000
K = 200; MK = 60**K; M2 = 60**2000

def digits60(x):
    d = []
    while x: x, r = divmod(x, 60); d.append(r)
    return d
def fib_exact(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a
t, off = terms('A261598')
def a(n):
    if n == 0: return 0
    p = 1
    for d in digits60(fib_exact(n)): p *= d
    return p
assert [a(n) for n in range(len(t))] == t; print('terms ok', len(t))
lo0, lo1 = 0, 1          # F(n) mod 60^K
ex0, ex1 = 0, 1          # exact F(n) (kept for fallback sizes and full check)
nonzero = []; fallbacks = 0
for n in range(1, N + 1):
    lo0, lo1 = lo1, (lo0 + lo1) % MK
    ex0, ex1 = ex1, ex0 + ex1
    # now lo0 = F(n) mod 60^K, ex0 = F(n)
    if ex0 >= MK:
        x = lo0; z = False
        for _ in range(K):
            x, r = divmod(x, 60)
            if r == 0: z = True; break
        if z: continue
    fallbacks += 1
    if ex0 >= M2:   # second tier: low 2000 base-60 digits of the exact value
        x = ex0 % M2; z = False
        for _ in range(2000):
            x, r = divmod(x, 60)
            if r == 0: z = True; break
        if z: continue
    if 0 not in digits60(ex0): nonzero.append(n)
print('N', N, 'fallbacks', fallbacks, 'n with a(n)!=0 (n>=1):', len(nonzero), 'max', max(nonzero), 'any >3329:', [n for n in nonzero if n > 3329][:10])

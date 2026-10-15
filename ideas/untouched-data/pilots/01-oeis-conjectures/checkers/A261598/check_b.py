"""A261598 check_b: exact Fibonacci via gmpy2 (fib2 to seed, then additions); zero-digit test with gmpy2's
base-60 string conversion, first on F mod 60^64 (when F >= 60^64), otherwise on the whole number."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import gmpy2
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 360000
B = gmpy2.mpz(60)**64
DIG = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def prod60(x):
    s = x.digits(60); p = 1
    for ch in s: p *= DIG.index(ch)
    return p
t, off = terms('A261598')
assert [0] + [prod60(gmpy2.fib(n)) for n in range(1, len(t))] == t; print('terms ok', len(t))
nonzero = []
f0, f1 = gmpy2.fib2(1)[::-1]  # f0=F(0)? fib2(1) = (F1, F0)
f0, f1 = gmpy2.mpz(0), gmpy2.mpz(1)
for n in range(1, N + 1):
    f0, f1 = f1, f0 + f1    # f0 = F(n)
    if f0 >= B and '0' in (f0 % B).digits(60).rjust(64, '0'):
        continue
    if '0' not in f0.digits(60): nonzero.append(n)
assert gmpy2.fib(N) == f0
print('N', N, 'n with a(n)!=0 (n>=1):', len(nonzero), 'max', max(nonzero), 'any >3329:', [n for n in nonzero if n > 3329][:10])

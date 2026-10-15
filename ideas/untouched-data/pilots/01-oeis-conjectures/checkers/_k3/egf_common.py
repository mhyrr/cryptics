"""Shared spec for A226838/A226839/A226890: e.g.f. exp(sum_k g_k x^k/k!) with integer g_k (only definitions here)."""
from math import factorial
from sympy import divisor_sigma
def gdict(anum, L):
    g = {}
    if anum == 'A226838':
        m = 1
        while m * m <= L: g[m*m] = factorial(m*m) // m**m; m += 1
    elif anum == 'A226839':
        m = 1
        while m * (m + 1) // 2 <= L: T = m*(m+1)//2; g[T] = factorial(T) // factorial(m); m += 1
    elif anum == 'A226890':
        m = 1
        while m * m <= L: g[m*m] = int(divisor_sigma(m, m)) * factorial(m*m) // m**m; m += 1
    return g

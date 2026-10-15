"""check_a engine: a(n+1) = sum_k C(n,k) g_{k+1} a(n-k), mod M, binomials via Lucas per prime + CRT.
g_k mod M computed from p-adic valuations (Legendre) without forming factorials."""
import sys
from sympy import factorint, divisor_sigma
from egf_common import gdict

def vfact(n, p):
    v = 0
    while n: n //= p; v += n
    return v

def fact_mod_unit(n, p, e):  # n! with all p-factors removed, mod p^e (direct product; n small enough)
    M = p**e; r = 1
    for i in range(2, n + 1):
        while i % p == 0: i //= p
        r = r * i % M
    return r

def g_mod(anum, L, M):
    # g_k mod M via CRT over prime powers; uses valuations
    fac = factorint(M); out = {}
    ks = []
    if anum in ('A226838', 'A226890'):
        m = 1
        while m*m <= L: ks.append((m*m, m)); m += 1
    else:
        m = 1
        while m*(m+1)//2 <= L: ks.append((m*(m+1)//2, m)); m += 1
    for k, m in ks:
        res = 0; mod = 1
        for p, e in fac.items():
            if anum == 'A226839':
                v = vfact(k, p) - vfact(m, p)
                num = fact_mod_unit(k, p, e) if v < e else 0
                den = fact_mod_unit(m, p, e)
                val = 0 if v >= e else num * pow(den, -1, p**e) * p**v % p**e
            else:
                vm = 0; mm = m
                while mm % p == 0: mm //= p; vm += 1
                v = vfact(k, p) - m * vm
                if v >= e: val = 0
                else:
                    val = fact_mod_unit(k, p, e) * pow(pow(mm, m, p**e), -1, p**e) * p**v % p**e
                if anum == 'A226890': val = val * (int(divisor_sigma(m, m)) % p**e) % p**e
            # CRT combine
            pe = p**e
            res = res + mod * ((val - res) * pow(mod, -1, pe) % pe); mod *= pe
        out[k] = res % mod
    return out

def lucas(n, k, p):
    r = 1
    while n or k:
        a, b = n % p, k % p
        if b > a: return 0
        from math import comb
        r = r * comb(a, b) % p; n //= p; k //= p
    return r

def binom_mod(n, k, primes):  # M squarefree here
    res = 0; mod = 1
    for p in primes:
        v = lucas(n, k, p)
        res = res + mod * ((v - res) * pow(mod, -1, p) % p); mod *= p
    return res

def run(anum, M, N):
    primes = sorted(factorint(M)); assert all(e == 1 for e in factorint(M).values())
    g = g_mod(anum, N + 1, M); gk = sorted(g)
    a = [1]
    for n in range(N):
        s = 0
        for k1 in gk:
            k = k1 - 1
            if k > n: break
            if g[k1]: s += binom_mod(n, k, primes) * g[k1] * a[n - k]
        a.append(s % M)
    return a

def exact_terms(anum, L):
    from math import comb
    g = gdict(anum, L); a = [1]
    for n in range(L - 1):
        a.append(sum(comb(n, k1 - 1) * g[k1] * a[n - k1 + 1] for k1 in g if k1 - 1 <= n))
    return a

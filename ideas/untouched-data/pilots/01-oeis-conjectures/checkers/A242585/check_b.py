"""A242585 check_b: independent verification of check_a's certificates (cert.json). X = P_n * Q_n recomputed with
the Pell / Pell-Lucas (A001333) recurrences (not via P_2n/2); for each certified n: each witness q is prime (sympy
isprime), q^e || X exactly, and sum v_3(2e+1) >= 2, hence 9 | tau(X^2) = a(n). Reports the range [2, B] in which every
n except 7 is certified. Terms re-derived with PARI factorization of P_n*Q_n."""
import sys, json; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import cypari2
from sympy import isprime
from oeisterms import terms
pari = cypari2.Pari()
c = json.load(open(__file__.rsplit('/', 1)[0] + '/cert.json'))
cert = {int(k): [(int(q), e) for q, e in v] for k, v in c['cert'].items()}
M = max(cert) + 2
Pn = [0, 1]; Qn = [1, 1]
for k in range(2, M + 1): Pn.append(2 * Pn[-1] + Pn[-2]); Qn.append(2 * Qn[-1] + Qn[-2])
t, off = terms('A242585')
def tau_sq(x):
    f = pari.factor(x); r = 1
    for e in f[1]: r *= 2 * int(e) + 1
    return r
assert [tau_sq(Pn[n] * Qn[n]) for n in range(1, len(t) + 1)] == t; print('terms ok', len(t))
def v3(x):
    k = 0
    while x % 3 == 0: x //= 3; k += 1
    return k
good = set()
for n, ws in cert.items():
    X = Pn[n] * Qn[n]; score = 0; ok = True
    for q, e in ws:
        if not isprime(q): ok = False; break
        if X % q**e or X % q**(e + 1) == 0: ok = False; break
        score += v3(2 * e + 1)
    if ok and score >= 2: good.add(n)
B = 1
while B + 1 == 7 or (B + 1) in good: B += 1
print('certificates verified: every n in [2, %d] except 7 has 9 | a(n)' % B, '| verified n total', len(good))

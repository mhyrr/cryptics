"""A325945 check_b: verify every witness pair (p, q) from check_a with sympy, directly from the definition:
p composite squarefree, q composite squarefree, gcd(p,q)=1, q not Carmichael (Korselt), and lambda(pq) | (p-1)(q-1)
(Carmichael function via sympy.reduced_totient). Also checks that every composite squarefree p < PMAX has a witness, and
re-derives the listed terms by brute force over ALL q (first 20 p) (not just q == 1 mod D(p)) and compares with check_a."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np
from math import gcd
from sympy import factorint, reduced_totient
from oeisterms import terms
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 327680
W = np.load(__file__.rsplit('/', 1)[0] + '/witnesses.npy')
def sqfree_comp(x):
    f = factorint(x); return all(e == 1 for e in f.values()) and len(f) >= 2, f
def carmichael(x, f): return all((x - 1) % (p - 1) == 0 for p in f)
def idem(p, q): return ((p - 1) * (q - 1)) % int(reduced_totient(p * q)) == 0
def ok(p, q):
    sp, fp = sqfree_comp(p); sq, fq = sqfree_comp(q)
    return sp and sq and gcd(p, q) == 1 and not carmichael(q, fq) and idem(p, q)
t, off = terms('A325945')
P = [p for p in range(4, 10**6) if sqfree_comp(p)[0]][:len(t)]
def least(p):
    q = 4
    while not ok(p, q): q += 1
    return q
NB = 20
br = [least(p) for p in P[:NB]]
print('terms (brute force over all q): mismatches with data (p, brute q, listed q):', [(p, b, x) for p, b, x in zip(P, br, t) if b != x])
assert [int(x) for x in W[:NB, 1]] == br, 'check_a witnesses differ from brute force least q'
allp = [p for p in range(4, PMAX) if sqfree_comp(p)[0]]
assert [int(x) for x in W[:, 0]] == allp
bad = [(int(p), int(q)) for p, q in W if q <= 0 or not ok(int(p), int(q))]
print('PMAX', PMAX, 'pairs verified', len(W) - len(bad), 'of', len(W), 'failures', bad[:10])

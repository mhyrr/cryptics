"""A182088 / A182132: C(n) = product of linear forms in n. Data = Carmichael numbers of that form (ascending).
Conjecture: if all the linear factors are prime then C(n) is a Carmichael number.
method 'a': factor C via sympy.factorint, Korselt's criterion (squarefree, composite, p-1 | C-1).
method 'b': Carmichael function via sympy.reduced_totient(C) | C-1 and C composite (definition of Carmichael:
            b^(C-1) == 1 mod C for all b coprime to C  <=>  lambda(C) | C-1); for the prime-factor case lambda is
            computed directly as lcm(q_i - 1) from the known factors.
"""
from sympy import factorint, isprime, reduced_totient
from math import lcm

def is_carm_a(C):
    if C < 3 or isprime(C): return False
    f = factorint(C)
    return all(e == 1 and (C - 1) % (p - 1) == 0 for p, e in f.items())

def is_carm_b(C):
    if C < 3 or isprime(C): return False
    return (C - 1) % int(reduced_totient(C)) == 0

def run(anum, forms, n0, method, N, terms_fn, check_terms):
    T = terms_fn(anum)
    isc = is_carm_a if method == "a" else is_carm_b
    C = lambda n: eval_prod(forms, n)
    got = []; n = n0
    while len(got) < len(T):
        c = C(n)
        if isc(c): got.append(c)
        n += 1
    got.sort()
    assert got == T, (got[:5], T[:5])
    print(f"{anum} method {method}: reproduced all {len(T)} data terms (Carmichael numbers of the form)")
    bad = []; hits = []
    for n in range(n0, N + 1):
        fs = [a * n + b for a, b in forms]
        if all(x > 1 and isprime(x) for x in fs):
            c = C(n); hits.append(n)
            ok = ((c - 1) % lcm(*[x - 1 for x in fs]) == 0) if method == "b" else isc(c)
            if not ok: bad.append(n)
    print(f"  n={n0}..{N}: {len(hits)} n with all factors prime (first: {hits[:6]}); non-Carmichael among them: {bad[:10]}")

def eval_prod(forms, n):
    r = 1
    for a, b in forms: r *= a * n + b
    return r

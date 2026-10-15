# Third check, main thread: is F(372) abundant but not Zumkeller?
# Not-Zumkeller argument: write F = 144*Q with gcd(144,Q)=1. A Zumkeller split is a sign choice
# e(d) = +-1 on the divisors with sum 0. Group divisors d*q (d|144, q|Q): sum_q t_q*q = 0 with
# t_q = sum_d e(d,q)*d odd (sigma(144) = 403 is odd) and |t_q| <= 403. The q = Q term has
# |t_Q*Q| >= Q; all others sum to at most 403*(sigma(Q) - Q). If that is < Q, no split exists.
import sympy
from math import prod
def fib(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a
F = fib(372)
fac = {2: 4, 3: 2, 557: 1, 2417: 1, 63799: 1, 3010349: 1, 15917507: 1, 35510749: 1,
       3020733700601: 1, 4531100550901: 1, 859886421593527043: 1}   # the agent's factorization, checked below
assert prod(p**e for p, e in fac.items()) == F, "product != F(372)"
assert all(sympy.isprime(p) for p in fac), "a factor is not prime"
sigma = prod((p**(e+1) - 1) // (p - 1) for p, e in fac.items())
Q = F // 144; assert Q % 2 and Q % 3
sQ = prod((p**(e+1) - 1) // (p - 1) for p, e in fac.items() if p > 3)
print("F(372) digits", len(str(F)), "abundant", sigma > 2*F, "sigma/F", round(sigma / F, 4), "sigma even", sigma % 2 == 0)
print("403*(sigma(Q)-Q)/Q =", 403 * (sQ - Q) / Q, "-> not Zumkeller" if 403 * (sQ - Q) < Q else "-> argument inconclusive")

# A103959: a(n) = least prime q with prime(n)*q - 2 prime. Conjecture: a(n) <= prime(n). gmpy2 next_prime / is_prime.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import gmpy2
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
def a_of_p(p):
    q = 2
    while not gmpy2.is_prime(p * q - 2): q = int(gmpy2.next_prime(q))
    return q
P = [2]
while len(P) < N: P.append(int(gmpy2.next_prime(P[-1])))
check_terms("A103959", lambda n: a_of_p(P[n - 1]))
bad = []; worst = (0, 0)
for n in range(1, N + 1):
    p = P[n - 1]; q = a_of_p(p)
    if q > p: bad.append((n, p, q))
    if q / p > worst[0] and n > 5: worst = (q / p, n)
print("N =", N, "violations:", bad[:10], "max q/p for n>5:", worst)

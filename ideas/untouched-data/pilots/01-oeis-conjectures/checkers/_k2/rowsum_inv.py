"""A127750 (c=2) / A127752 (c=3): row sums of the inverse of A(n,k) = 1/(c*n+1) for k<=n<=2k, else 0 (n,k>=0).
Row sums r = A^{-1} 1 solve A r = 1, i.e. sum_{k=ceil(n/2)..n} r_k = c*n+1.
method 'a': prefix-sum recurrence O(N).
method 'b': per-row literal slice sums O(N^2), plus an explicit exact inverse (python-flint fmpq_mat) for n < 300
            to confirm the row sums of the inverse matrix itself.
"""
def method_a(c, N):
    r = [0] * (N + 1); P = [0] * (N + 2)   # P[i] = r_0 + ... + r_{i-1}
    for n in range(N + 1):
        lo = (n + 1) // 2
        r[n] = c * n + 1 - (P[n] - P[lo])
        P[n + 1] = P[n] + r[n]
    return r

def method_b(c, N):
    r = []
    for n in range(N + 1):
        lo = (n + 1) // 2
        r.append(c * n + 1 - sum(r[lo:n]))
    from flint import fmpq_mat, fmpq
    m = 300
    A = fmpq_mat(m, m, [fmpq(1, c * n + 1) if k <= n <= 2 * k else 0 for n in range(m) for k in range(m)])
    X = A.inv()
    for n in range(m):
        s = sum((X[n, k] for k in range(m)), fmpq(0))
        assert s == r[n], (n, s, r[n])
    print("  explicit inverse (flint) row sums agree for n < 300")
    return r

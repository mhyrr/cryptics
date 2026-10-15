# Main-thread third checks (step 4)

Written on the main thread without reading the agents' checkers.
Env: `uv venv venv && uv pip install sympy python-flint` (Python 3.13).

- `a281648.py n`: numerator(B_2n) mod n by sympy and by FLINT. Output: `a281648.out`
  (n = 3330 → 3329 = n−1 in both; controls n = 6 true, n = 12 false, matching %S).
- `a371113.py N`: Hasler's own OEIS Python program, ported with a membership set;
  asserts it reproduces %S, then lists k with a(3k+1) − a(3k) ∉ {1,2}. Output: `a371113.out`.

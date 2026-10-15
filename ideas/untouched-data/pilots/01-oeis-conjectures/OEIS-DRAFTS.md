# Draft OEIS comments: for Greg's review, NOT posted

OEIS submissions must come from a registered human editor account, under that
person's name. These drafts follow the house style (`%C` comment, author line,
date). Before posting, re-run the matching `verify/` script, and check that the
entry has not changed since oeisdata commit `955686d5`.

---

**A074726**
> The conjecture of M. Farrokhi D. G. above fails at n = 372: F(372) = 2^4 * 3^2 * 557 * 2417 * 63799 * 3010349 * 15917507 * 35510749 * 3020733700601 * 4531100550901 * 859886421593527043 is abundant (sigma(F)/F = 2.8048...) but not Zumkeller. Writing F = 144*Q, any partition of the divisors into two equal-sum sets would give Sum_{q|Q} t_q*q = 0 with every t_q odd and |t_q| <= sigma(144) = 403, impossible since 403*(sigma(Q) - Q) < Q. [UNVERIFIED on main thread, check or cut:] Further failures below n = 1300 include n = 732, 996, 1212, 1284. - _[name]_, [date]

**A281648**
> The conjecture above fails at n = 3330 = 2*3^2*5*37: numerator(B(6660)) == -1 (mod 3330). Here n+1 = 3331 is prime, as for n = 6 and n = 10. For n <= 10240 the solutions are exactly n = 6, 10, 3330 and n = 2^k. - _[name]_, [date]

**A371113**
> Conjecture 3 (and the corresponding %F bound) fails at k = 16170: a(48510) = 32631 and a(48511) = 32634, because 32632 = a(338) and 32633 = a(4958) were used earlier as palindrome completions. Further failures at k = 26850 and k = 27047 (k < 33333). - _[name]_, [date]

**A325945**: data correction
> a(6) = 21, not 217: for p = 22, q = 21 is coprime, squarefree, composite and non-Carmichael, and lambda(462) = 30 divides (22-1)*(21-1) = 420.

**A372409**: comment correction
> In Conjecture 2, det T(p) = -2*det S(p) (not -det S(p)); e.g. p = 5: det S = 1, det T = -2. With that correction both parts hold for primes p < 80 (exact) [agent only, modular: p <= 2297].

**A123721**
> The smallest n with a(n) = k appears to be A123720(k+1) = 2^(k+1) + 2^k - k - 1, not A123720(k): e.g. a(n) = 2 first at n = 9 = A123720(3). Confirmed for k <= 25.

**A138670**
> In the formula, m >= 0 (m = 0 gives the multiples of 3, e.g. 0, 3, 6).

**A261524**
> Conjecture 1 should exclude d = 2: Zs(2,2,1) = A064078(2) = 3 is a term.

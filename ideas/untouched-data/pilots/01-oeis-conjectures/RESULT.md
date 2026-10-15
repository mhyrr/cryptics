# Pilot 01 result: OEIS conjectures checked only to a stated bound

*2026-10-15. Data: oeisdata commit `955686d5`. Counts from `tally.py` → `tally.out`.
Main-thread third checks in `verify/`.*

## Answer

Of 152 conjectures with a stated checked bound, picked from 730 extracted lines,
**three were false a short way past their bound**. Each is confirmed on the main
thread by code written without reading the agents' checkers:

| Entry | Conjecture (author, year) | Stated bound | Fails at | Main-thread check |
|---|---|---|---|---|
| A074726 | σ(F(n)) > 2F(n) ⇔ F(n) Zumkeller, except n = 12 (Farrokhi, 2020) | n ≤ 371 | **n = 372** | `verify/a074726.py`: factorization proved (all factors < 2⁶⁴), σ/F = 2.80, not-Zumkeller bound 0.897 < 1 |
| A281648 | num(B₂ₙ) ≡ −1 (mod n) iff n = 6, 10 or 2^k (Manyama, 2017) | n ≤ 1024 | **n = 3330** | `verify/a281648.py`: sympy and FLINT agree; controls n = 6, 12 behave |
| A371113 | a(3k+1) − a(3k) ∈ {1, 2} (Hasler, 2024; also the %F line) | k ≤ 3333 | **k = 16170** (also 26850, 27047) | `verify/a371113.py`: the entry's own Python program, reproduces %S |

That is the A173419 pattern three more times. A074726 fails at the next index
after its bound.

**Errors in entries** (statement or data, not mathematics):

| Entry | Error | Check |
|---|---|---|
| A325945 | a(6) (p = 22) is 21, not 217: λ(462) = 30 divides 21·20 | `verify/a325945.py` brute force; the other 17 terms reproduce |
| A372409 | Conj. 2 "det S(p) = −det T(p)" should be det T = −2·det S; the det S formula holds | `verify/a372409.py`, exact determinants for p = 5…59 |
| A123721 | Conjecture's index is off by one: least n with a(n) = k is A123720(k+1), not A123720(k) | by hand from %S (first 2 at n = 9, first 3 at n = 20) |
| A138670 | %F set formula needs m ≥ 0, not m ≥ 1 (else 0, 3, 6 are excluded) | by hand from %S |
| A261524 | Conj. 1 is literally false at d = 2 (Zs(2,2,1) = 3 is a term); exclude d = 2 | by hand from %S and A064078 |

## Counts

```
rows 152 · triage: checkable 129, already-settled 16, not-checkable 7
checkable: holds 105 · timeout 20 · counterexample 4 (3 real + A261524 statement slip)
two checkers disagreed on: none
holds: median extension 10×, 72 of 105 pushed ≥ 10× the stated bound
```

The agents also sketched short proofs for about a dozen conjectures. These are in
the `note` column of `results/`, for example A219562, A226838/9/90, A197654/5 and
A092674. **Those proofs are not checked**; they are leads, not results.

## What this says about the survey's thesis

- **The verifier made this cheap.** Four agents, a few hours, CPU only, and three
  disproofs that need no expert's judgement. This is the property the survey
  weights double, and it worked as predicted.
- **Base rate.** About 2% of bounded OEIS conjectures fail within ~10× their bound
  (3 of 129 checkable). Across all 730 extracted lines, that suggests ~10–15 more
  are waiting. The other 578 lines are the obvious next run.
- **Payoff is modest, as file 06 said** (`payoff 2`). These are corrections to a
  reference work, not new mathematics. The value is in being right, and in the method.

## Caveats

- Probable-prime tests (BPSW) underlie some "holds" rows (A069923, A051451,
  A095017, A242585, A321766). A074726's counterexample does not depend on them.
- Some "holds" rows use a checker-specific reading of an ambiguous statement
  (A016777, A047211, A389148). Each says so in its note.
- A372385 and A372409 agreements are modular determinant checks: evidence, not proof.
- 20 timeouts were left unreached; their rows say what it would take.

## Next

1. `OEIS-DRAFTS.md`: drafted comments for Greg to review. **Nothing has been posted.**
2. Run the remaining 578 candidates (`candidates.tsv` minus `batch.tsv`), same brief.
3. Check A074726's other ~31 failures below n = 3710 (batch 1's check_b) on the main thread.

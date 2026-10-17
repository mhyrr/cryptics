# 08-letter-fit — do the letter counts fit the candidate languages?

**Question.** The dive has assumed "a transposition of Spanish" from the index of coincidence. Do the letter
counts themselves fit Spanish, Italian or Portuguese, in telegraph style or prose?

**Method.** `fit.py`. Reference: 40 chunks of 10,000 letters from random points of the held-out corpus
(`01-solver/plaintext.py`), per language and style. A single long window is not stable, because it is dominated by
a few books, and a first inline look used one. Chi-square against the reference, with its null from 500 plants of
the same length and style. Per-letter z for the largest misfits. Telegraph style spells stops as PUNTO / STOP /
PONTO. X as a stop sign, spelled numbers beyond the generator's few, and code letters are not modelled.
Run: `python3 -I fit.py > result.txt` (about 1 minute). The p values were stable across three seeds (±0.03).

**Result** (`result.txt`, telegraph style; prose is similar or worse). **Corrected 2026-10-17**: held-out book
27738 ends in an English–Spanish glossary (found by `09`), which fattened the plants' tails. It is now excluded in
`01-solver/plaintext.py`. The first run's p values (Spanish T1 0.08, T2 0.11; Portuguese T1 0.03) were inflated.

| | Spanish | Italian | Portuguese |
|---|---|---|---|
| T1 | **p = 0.014** | **p = 0.004** | p = 0.022 |
| T2 | p = 0.024 | p = 0.074 | p = 0.108 |

Largest misfits against Spanish telegraph style:
- T1: **X 6 vs 1 expected (z +5.0)**; P 35 vs 23 (z +2.5); M 24 vs 16 (z +1.9); U 16 vs 28 (z −2.2); A 58 vs 74
  (z −1.9).
- T2: **F 7 vs 1 expected (z +4.7)**; no X at all.

**Reading.** No candidate language fits T1 in our telegraph style. Spanish and Portuguese are closest; Italian is
furthest. Spanish fits best but not well. The misfit sits in two letters that do not belong to ordinary prose, a different one in each
telegram: X in T1 and F in T2. Possible causes, tested in `09` and `10`: X as a stop or separator sign in T1; spelled numbers
or a code letter; nulls; a plaintext that is not plain Spanish (names, code words, mixed language); or T1 and T2
under different conventions. `10` finds that only X nulls (T1) and F as a stop sign (T2) fit, and neither has a period source; `09` finds
that position cannot tell X-as-stop from X-as-null.

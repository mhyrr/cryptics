# 08-letter-fit — do the letter counts fit the candidate languages?

**Question.** The dive has assumed "a transposition of Spanish" from the index of coincidence. Do the letter
counts themselves fit Spanish, Italian or Portuguese, in telegraph style or prose?

**Method.** `fit.py`. Reference: 40 chunks of 10,000 letters from random points of the held-out corpus
(`01-solver/plaintext.py`), per language and style. A single long window is not stable, because it is dominated by
a few books, and a first inline look used one. Chi-square against the reference, with its null from 500 plants of
the same length and style. Per-letter z for the largest misfits. Telegraph style spells stops as PUNTO / STOP /
PONTO. X as a stop sign, spelled numbers beyond the generator's few, and code letters are not modelled.
Run: `python3 -I fit.py > result.txt` (about 1 minute). The p values were stable across three seeds (±0.03).

**Result** (`result.txt`, telegraph style; prose is similar or worse).
| | Spanish | Italian | Portuguese |
|---|---|---|---|
| T1 | p = 0.08 | **p = 0.004** | p = 0.03 |
| T2 | p = 0.11 | p = 0.09 | p = 0.10 |

Largest misfits against Spanish telegraph style:
- T1: **X 6 vs 1 expected (z +5.3)**; U 16 vs 30 (z −2.5); M 24 vs 16 and P 35 vs 25 (z +2.0 each).
- T2: **F 7 vs 1 expected (z +4.6)**; no X at all.

**Reading.** Italian does not fit T1. That narrows H3, whose control assumed Italian was a live option. Spanish fits
best but not well. The misfit sits in two letters that do not belong to ordinary prose, a different one in each
telegram: X in T1 and F in T2. Possible causes (none tested): X as a stop or separator sign in T1; spelled numbers
or a code letter; nulls; a plaintext that is not plain Spanish (names, code words, mixed language); or T1 and T2
under different conventions. Each predicts something checkable, which is the job of `PROMPT-diagnose.md`.

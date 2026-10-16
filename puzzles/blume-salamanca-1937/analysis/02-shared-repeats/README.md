# 02-shared-repeats — do the two telegrams share more strings than chance?

**Question.** Richard Bean (cyphersolver issue 37, 15 Oct 2026, CLAIMANT/POPULAR tier) says the two telegrams
share too many repeated strings for a double transposition. Is the excess real?

**Method.** `repeats.py` counts distinct n-grams (n = 3–6) shared between T1 and T2, and repeated within T1,
and compares each count with 5,000 independent letter shuffles of each telegram (seed 20261016).
Run: `python3 repeats.py > result.txt`.

**Result** (`result.txt`).
| n | T1 × T2 shared | shuffle mean | p | T1 self-repeats | shuffle mean | p |
|---|---|---|---|---|---|---|
| 3 | 37 | 26.1 | 0.011 | 45 | 50.2 | 0.85 |
| 4 | 9 | 2.2 | 0.001 | 3 | 4.3 | 0.79 |
| 5 | 2 | 0.15 | 0.017 | 1 | 0.30 | 0.24 |
| 6 | 1 (APMOEP) | 0.01 | 0.011 | 0 | 0.02 | 1.0 |

**Reading.** The cross-telegram excess is real at about the 1% level, after allowing for the choice of n made
after looking. Seven independent coincidences of four or more letters, against about two expected. Three of the
nine shared 4-grams come from one 6-gram, APMOEP: T2 groups 2–3 (`APMOE P…`) and T1 groups 53–54 (`…EAP MOEPA`).
T2's opening `NOCUOAPMOEPM` has NOCU at T1 position 17 and OEPM at T1 position 42.
Repeats within T1 alone are at chance, as any letter transposition requires.

**What it bears on.** Under a double columnar transposition the shared strings are chance (p ≈ 0.001–0.01).
They are what a common opening or closing would produce under a system that keeps short runs of plaintext
together, or under a single transposition whose geometry puts the shared plaintext at matching positions.
This weakens H1/H2 (double columnar) without refuting them, and it motivates H5. Positions do not share a
constant offset, so no simple alignment is visible.

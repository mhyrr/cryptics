# 05-periodic — letters permuted within sets of n

**Question.** `04` could not test one survey family: the letters of each consecutive set of n are permuted by one
n-place key (Givierge 1925, worked example with key 4-2-6-3-7-1-5; `sources/key-type-survey.md`). Three of the seven
shared-run offsets in `02` are multiples of 17, which this family would explain if both telegrams share a key
(look-elsewhere p = 0.054, `04/offsets.py`). Is either telegram, or both under one key, such a cipher with
n = 2–40?

**Method.** `periodic.py`. Cipher set c[j] = p[k[j]], sets aligned from the first letter. A partial last set is
left out of the score because its handling is unknown (T1 = 615 leaves 615 mod n letters out; none for n = 3, 5,
15, 41). Hill climb on the Spanish quadgram score (`01-solver/out/lm_es_4.bin`) with swap and insertion moves,
12 restarts, patience 1,500. For each n: one plant of 615 letters, one joint plant of 615 + 160 under one key
(telegraph-style held-out Spanish), the target T1, and the target T1 + T2 under one key, all in the same run with
the same code. Run: `python3 -I periodic.py > result.txt` (about 7 minutes on 10 cores).

**Pass rule.** As in `01-solver`: a full recovery reads at least 95% of the scored letters correctly; a band
passes at 80%. The candidate threshold is the `01` value, −5.10 per letter.

**Result** (`result.txt`).
- Controls: 39/39 single and 39/39 joint plants recovered at 100%, every n from 2 to 40.
- Target: no candidate. T1 alone best −5.86 (n = 39, 40); joint best −5.87 (n = 40). Target scores rise slowly
  with n (−6.81 at n = 2) because a longer key fits noise better. No reading shows Spanish.
- Caveat on the threshold: two perfect plant recoveries scored −5.22 (n = 24) and −4.92 (n = 35). A true reading
  can fall below −5.10. The target's best is 0.64 below the lowest perfect plant, and its readings are visibly
  noise, so the verdict does not rest on the threshold alone.

**Reading.** A periodic within-set transposition with n ≤ 40, set alignment from the first letter, is excluded for
T1 alone and for both telegrams under one key. The mod-17 alignment of the shared runs is therefore chance or comes
from some other mechanism. Not covered: sets that start after a preamble, nulls inserted before the transposition,
and n > 40.

## Nihilist read by rows (added 2026-10-16, session 3)
`nihilist_control.py` plants the Nihilist rectangle read by rows: each row's letters are permuted by one column
key, then the rows are reordered. `07` shows this is the one tested family that reproduces the shared strings.
The same `solve` recovers the exact column key in 36/36 plants of 615 letters and 36/36 joint plants (615 + 160,
one column key, rows reordered separately), n = 5–40, scoring −4.03 to −4.47 (`nihilist_control.txt`). Row order
costs the solver almost nothing, because most quadgrams sit inside a row. The target's best under this solver is
−5.86, so **Nihilist read by rows is excluded for widths 5–40**, alone and jointly.

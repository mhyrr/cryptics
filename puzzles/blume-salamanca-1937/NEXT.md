# NEXT — handoff for the next session

**Last session:** 2026-10-16 (session 2: key-type survey, `04`, `05`)
**Where it stopped:** Every transposition family we can test with a passing control is excluded. No candidate
in any run.

| family | region | controls | target | where |
|---|---|---|---|---|
| double columnar CC | w1 2–15 × w2 12–15 (with Bourdeau, w2 ≤ 15) | 30/30 | best −6.00 | `03` |
| CC, one key on both telegrams | w1 8–15 × w2 16–17 | 8/10 | best −6.09 | `03` |
| double columnar CR | w1 2–15 × w2 12–15 | 8/10 | best −6.02 | `03` |
| word, row and serpentine routes, block moves | widths 5–30, sets 3–12 | 20/20 | no bigram structure (p 0.53, 0.61) | `04` |
| letters permuted within sets of n | n 2–40, alone and joint | 78/78 | best −5.86 | `05` |

The survey (`sources/key-type-survey.md`) found no period source that ties any transposition to the Oswalds or to
Spain 1937. The 2020 attempt (Heinzmann et al.) is not online.

The shared strings (`02`, p ≈ 0.001) now lack a mechanism. They are not surviving plaintext runs (`04`), and
periodic sets under one key do not explain them (`05`). Three of the seven offsets are multiples of 17, but the
look-elsewhere p is only 0.054.

## Do first
1. **Turning grille on T2.** 160 = 10 blocks of 4 × 4, and a 4 × 4 grille has only 4⁴ = 256 hole patterns.
   Enumerate all of them, in both turning directions, with the grid read by rows and by columns. Score each on
   quadgrams, and run a planted control in the same script. It takes minutes, and it settles the one family
   that `04` could not test at 160 letters. T1 (615 = 3 × 5 × 41) fits no square without nulls, so a grille that
   reads T2 then needs a separate explanation for T1.
2. **Model the shared strings directly.** Plant a common opening (20–60 letters, one key on both) under double
   columnar with w2 ≥ 16, and under Nihilist (rows and columns of a square permuted by one key). Count the shared
   4-grams. This shows whether any untested family could produce 9 of them, or whether we should treat them as a
   chance event (p ≈ 0.001 with n chosen after looking).
3. Ask Greg whether he wants to write to Bochsler (note 44) for the 2020 report. That is an external action.

## Open questions
- Who or what is "Blume"? Probably a registered telegraphic address. Fuentes has a BNE *Anuario* 1936 lead (unread).
- What does the "Cde" stamp on telegram 2 mean, and why 14.00 rather than 15.98?
- Do the two w1 = 2 CR control "failures" read correctly with a long displacement? (They score as their true texts.)
- Not tested: disrupted columnar, Nihilist, nulls before transposition, periodic sets offset by a preamble, n > 40.

## Named wall
**Double columnar, w2 ≥ 16 (alone) or ≥ 18 (jointly), or w1 ≥ 16.** At 615 + 160 letters the IDP has no gradient
beyond 3–4 swaps of the true key, so hill climbing cannot find it (`analysis/01-solver`, probe; Bourdeau saw the
same). Breach: a crib of 60–100 letters (Lasry's hybrid attack), the key phrases, a third message in the same keys,
or a new method that passes a control there. Do not widen this search without one of these.
If the grille and the shared-string model (items 1–2) come back empty, this wall is where the dive stops.

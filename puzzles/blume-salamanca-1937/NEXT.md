# NEXT — handoff for the next session

**Last session:** 2026-10-16 (session 4: letter fit `08`; `PROMPT-diagnose.md` written)
**Where it stopped:** at the named wall. Every family we can test with a passing control is excluded, and no run
gave a candidate.

| family | region | controls | target | where |
|---|---|---|---|---|
| double columnar CC | w1 2–15 × w2 12–15 (with Bourdeau, w2 ≤ 15) | 30/30 | best −6.00 | `03` |
| CC, one key on both telegrams | w1 8–15 × w2 16–17 | 8/10 | best −6.09 | `03` |
| double columnar CR | w1 2–15 × w2 12–15 | 8/10 | best −6.02 | `03` |
| word, row and serpentine routes, block moves | widths 5–30, sets 3–12 | 20/20 | no bigram structure (p 0.53, 0.61) | `04` |
| letters permuted within sets of n | n 2–40, alone and joint | 78/78 | best −5.86 | `05` |
| Nihilist read by rows | w 5–40, alone and joint | 72/72 | best −5.86 | `05` |
| 4 × 4 turning grille, T2 | all 1,024 keys, both uses | 10/10 | best −6.30 | `06` |

The shared strings (`02`, p ≈ 0.001) have no mechanism among the tested families. `07` shows that a shared phrase
produces them only under single columnar or Nihilist read by rows, and both are excluded. Under double columnar of
any tested length they stay at chance, which confirms Bean.

## Do first
0. **Run `PROMPT-diagnose.md`** in a fresh session. It restarts from diagnosis: the letter fit (`08`) shows
   misfits the dive never explained (X in T1, F in T2).
1. **Greg: send or drop the Bochsler letter** (`sources/outreach-bochsler.md`, German with English, through the
   publisher). The 2020 report could hold a key, a plaintext or a third message, which would breach the wall.
2. Only if something breaches the wall: the families still open are disrupted columnar, Nihilist read by columns,
   nulls before transposition, periodic sets offset by a preamble, and larger grilles with nulls. None has a period
   source tying it to the Oswalds. Do not start them without one.

## Open questions
- Who or what is "Blume"? Probably a registered telegraphic address. Fuentes has a BNE *Anuario* 1936 lead (unread).
- What does the "Cde" stamp on telegram 2 mean, and why 14.00 rather than 15.98?
- Do the two w1 = 2 CR control "failures" read correctly with a long displacement? (They score as their true texts.)
- Are the shared strings chance? The 1% level was set on a statistic chosen after looking, and a system that keeps
  row or column runs across messages without keeping letter pairs inside one is hard to construct.

## Named wall
**Double columnar, w2 ≥ 16 (alone) or ≥ 18 (jointly), or w1 ≥ 16.** At 615 + 160 letters the IDP has no gradient
beyond 3–4 swaps of the true key, so hill climbing cannot find it (`analysis/01-solver`, probe; Bourdeau saw the
same). Breach: a crib of 60–100 letters (Lasry's hybrid attack), the key phrases, a third message in the same keys,
the 2020 report, or a new method that passes a control there. Do not widen this search without one of these.

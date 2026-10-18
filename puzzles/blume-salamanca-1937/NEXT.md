# NEXT — handoff for the next session

**Last session:** 2026-10-17 (session 6: periodic and Nihilist solvers; tier 2 of `17`; double columnar method
research)
**Where it stopped:** every family we have a solver for is excluded, and the double columnar wall has moved and
been sharpened. Forward double columnar on T1 is now excluded for w1 ≤ 15 and w2 ≤ 17, at full length (`21`)
and on three trimmed bodies (`22`). The wall
is **w2 ≥ 18, or w1 ≥ 16 with w2 ≥ 16**. There, a climb finds the key only from within 2–4 swaps, and no tested
change widens that basin (`21`). Trimmed bodies (head, tail, both; `17` tiers 1–2) read nothing.

## What session 6 found (details in `research.md`, session 6, and each experiment's README)
- **`18`, `20`: periodic and Nihilist families.** Cipher position mod n gives the plaintext column, so the key is a
  path through a column-pair bigram table. Sets of n and Nihilist by rows are excluded for T1 n 8–50 and T2 n 8–15,
  with any preamble or tail. Nihilist by columns (squares) is excluded for T1 n 5–24 and T2 n 5–11. H5 is refuted for
  every tested family.
- **`17` tier 2.** Head and two-sided trims of 5–20 letters: no candidate for T1 single or double columnar (w ≤ 15),
  or T2 single columnar. The joint attack at w2 16–17 gives none either.
- **`21`: the double columnar wall.**
  - Lasry's thesis does not say how his 60% at 19 × 20 was measured. Our notes' "599 letters, English" was an
    inference; it is now corrected.
  - Our IDP reproduces his fitness-distance curve, and finds nothing in his presumed setting (0 of 6).
  - Lasry's full-neighbourhood climb at 50 M IDP evaluations passes w2 16–17 at 615 letters (20/20). T1 there: best
    −6.00, no candidate.
  - `01`'s K2 climb stops at about 17% of the neighbourhood (noted in `01`'s README; `03` stands).
- **Withdrawn post hoc lead.** T1 seemed to beat long-key double columnar plants under `18`'s solver. The cause was
  the offset scan leaving T1's poor end unscored (`18`, checks 1–4; `19`: no lag association).

## Exclusions, as they stand
| family | region | controls | target | where |
|---|---|---|---|---|
| double columnar CC, T1 full length | w1 2–15 × w2 12–15 (with Bourdeau, w2 ≤ 15) | 30/30 | best −6.00 | `03` |
| **double columnar CC, T1 full length** | **w1 2–15 × w2 16–17 (50 M IDP evaluations)** | 20/20 | best −6.00 | `21` |
| **same, T1[0:595], T1[5:615], T1[10:615]** | **w1 2–15 × w2 16–17** | 29/30 | best −5.94 | `22` |
| CC, one key on both, full length | w1 8–15 × w2 16–17 | 8/10; 9/10 | −6.09; −6.08 (T2[0:155]) | `03`, `17` |
| double columnar CR, full length | w1 2–15 × w2 12–15 | 8/10 | best −6.02 | `03` |
| **any columnar exclusion at full length** | **void if 5–20 letters at an end are not transposed** | `15`: 0/40, 0/10 | — | `15` |
| single columnar, T1 trimmed (a, b ∈ {0, 5, 10, 15, 20}; tail 1–4) | w 5–30 (w 31–45 where controls pass) | pass per band | ≤ −0.46 below | `17` |
| double columnar CC, T1 trimmed, same bodies | w1 2–15 × w2 2–15 | pass per band | best −5.92 vs −5.10 | `17` |
| single columnar, T2 trimmed (23 bodies + last group) | w 5–8; w 9–30 where controls pass | pass per band | below every true text | `17` |
| single columnar, one key, shared phrase, trimmed ends | w 5–30 | 99.6% | best 2 runs, chance | `16` |
| word, row and serpentine routes, block moves | widths 5–30, sets 3–12 | 20/20 | no bigram structure | `04` |
| sets of n; Nihilist read by rows | T1 n 8–50, T2 n 8–15, any preamble or tail | 117/120; 35/40 | 0.36–1.08 below | `18` |
| Nihilist read by columns, n × n squares | T1 n 5–24, T2 n 5–11, preamble 0–20 | 65/70 | 0.57–1.09 below | `20` |
| 4 × 4 turning grille, T2 | all keys; with an end tail; after a 1–15 preamble | 10/10; 20/20; 30/30 | −6.30; —; −5.86 | `06`, `15`, `17` |
| short-distance systems (sets 5–12, row routes) | any alignment | power 0.78–0.98 | no contact structure | `14` |

## Do first
1. **Greg: send or drop the Bochsler letter** (`sources/outreach-bochsler.md`; the cnlab route is noted there,
   identity unconfirmed). The 2020 report is still the best breach.
2. **Done overnight: w2 16–17 on trimmed T1 bodies** (`22`): no candidate on T1[0:595], T1[5:615], T1[10:615]. Other
   trims at w2 16–17 (two-sided, T2) remain unrun at about 5.7 CPU-hours per body; low priority.
3. **A context key list for K2** (`21`'s breach). Bourdeau already ran 6.6 M dictionary words and phrases, in
   several languages, for w1 8–40. What is new would be a small list built from the dossier: Oswald, Viktor, Werner,
   Blume, Salamanca, Burgos, Zürich, Bahnhofstrasse, Hisma, wool and credit terms, and combinations of 18–25 letters.
   Score each candidate and its neighbours within 2 swaps by the IDP; the true K2 stands 14–20 sd above random keys.
   Plant a list key first to confirm the scan finds it.
4. Lower: w1 ≤ 10 × w2 18–20 at 70–200 M evaluations per pair (needs its own control, multi-night). Disrupted
   columnar, nulls before transposition, a 9 × 9 grille on T2 (H11).

## Open questions
- Where does T1's P excess come from (35 vs 16 without a P-bearing stop word)? No modelled convention fits P, U and S
  together.
- What are T2's seven F's? No sourced convention produces them.
- Are the REF.. final groups (`REFLX`, `REFUD`) a convention or chance? Post hoc p 0.02–0.17.
- Does T1's poor end run past its last 20 letters? `18`'s solver also left T1[577:595] unscored once those 20 were
  cut (check 3). Not measured directly; bears on H6.
- Who or what is "Blume"? Probably a registered telegraphic address. Fuentes's BNE *Anuario* 1936 lead is unread.
- The "Cde" stamp: why 14.00 rather than 15.98?

## Named walls
- **Double columnar with w2 ≥ 18 at any w1, or w1 ≥ 16 with w2 ≥ 16, on 615 letters** (`21`).
  - The IDP brings a climb back to the true K2 only from within 2–4 swaps, and shows no gradient outside.
  - The share of keys inside that basin falls about tenfold per unit of w2.
  - Measured: 16 × 17, no hit in 48 M evaluations; 10 × 20, one hit in 114 M.
  - Breach: K2 candidates from outside the search (item 3), a crib of 60–100 letters, more text under the same
    keys, the 2020 report, or for w1 ≤ 10 × w2 18–20 only, 70–200 M evaluations per pair after a control.
- **Sets of n and Nihilist on T2 at n 16–30** (`18`). At 160 letters a wrong key fits better than the true one. No
  budget breaches it; only T1 or a shared key can test those widths.

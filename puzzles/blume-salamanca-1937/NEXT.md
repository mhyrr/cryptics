# NEXT — handoff for the next session

**Last session:** 2026-10-17 (session 6: a structural solver for the periodic and Nihilist families; tier 2 of `17`)
**Where it stopped:** the cheap families are now all excluded. `18` built a solver that passes controls for sets of n
and the Nihilist rectangle read by rows. `20` reused it for Nihilist read by columns. Neither telegram reads under
any of them. H5 (the shared strings come from a shared phrase under one key) is refuted for every tested family. Tier
2 of `17` (head and two-sided trims, T2 bodies, the joint attack) was **running when the session closed** (started
about 11:20 EDT on 2026-10-17, about 9 h on 5 workers). The top-ranked family, double columnar with long keys, still
sits behind the named wall.

## What session 6 found (details in `research.md`, session 6, and each experiment's README)
- **`18-periodic-solver`.** In sets of n and in the Nihilist rectangle read by rows, the cipher position mod n gives the
  plaintext column, so the key is a path through a column-pair bigram table. Controls: T1 117/120 (n 8–50), T2 35/40
  (n 8–15). The target is below every threshold by 0.36–1.08. Both families are excluded for T1 n 8–50 and T2 n 8–15,
  with any preamble or tail. T2 at n 16–30 is not testable: at 160 letters a wrong key outscores the right one.
- **`20-nihilist-columns`.** n × n squares read by columns, rearranged, are `18`'s problem. Controls 65/70. Excluded
  for T1 n 5–24 and T2 n 5–11, with a preamble of 0–20.
- **A post hoc lead, withdrawn.** T1 beat its own shuffles under `18`'s offset scan, and beat long-key double columnar
  plants (p ≈ 0.05). `19-lag-profile` found no letter-pair association at any lag. The cause: the offset scan leaves
  T1's rare-letter end unscored, and a shuffle spreads those letters everywhere. With the end kept, T1 lies inside its
  shuffles. Lesson (in `18`'s README): a solver that may choose which letters not to score needs fixed-offset
  controls.

## Exclusions, as they stand
| family | region | controls | target | where |
|---|---|---|---|---|
| double columnar CC, full length | w1 2–15 × w2 12–15 (with Bourdeau, w2 ≤ 15) | 30/30 | best −6.00 | `03` |
| CC, one key on both, full length | w1 8–15 × w2 16–17 | 8/10 | best −6.09 | `03` |
| double columnar CR, full length | w1 2–15 × w2 12–15 | 8/10 | best −6.02 | `03` |
| **any columnar exclusion at full length** | **void if 5–20 letters at an end are not transposed** | `15`: 0/40, 0/10 | — | `15` |
| single columnar, T1 end cut 1–5, 10, 15, 20 | w 5–30 (w 31–45 for 10–20 cut) | pass per band | best −5.50 vs ≈ −4.9 | `17` |
| double columnar CC, T1 end cut 1–5, 10, 15, 20 | w1 2–15 × w2 2–15 | 39/40 | best −5.94 vs −5.10 | `17` |
| single columnar, T2 last group cut | w 5–30 | pass | best −4.79 vs −4.41 | `17` |
| single columnar, one key, shared phrase, trimmed ends | w 5–30 | 99.6% | best 2 runs, chance | `16` |
| word, row and serpentine routes, block moves | widths 5–30, sets 3–12 | 20/20 | no bigram structure | `04` |
| **sets of n; Nihilist read by rows** | **T1 n 8–50, T2 n 8–15, any preamble or tail** | 117/120; 35/40 | 0.36–1.08 below | `18` |
| **Nihilist read by columns, n × n squares** | **T1 n 5–24, T2 n 5–11, preamble 0–20** | 65/70 | 0.57–1.09 below | `20` |
| 4 × 4 turning grille, T2 | all keys; with an end tail; after a 1–15 preamble | 10/10; 20/20; 30/30 | −6.30; —; −5.86 | `06`, `15`, `17` |
| short-distance systems (sets 5–12, row routes) | any alignment | power 0.78–0.98 | no contact structure | `14` |

## Do first
1. **Greg: send or drop the Bochsler letter** (`sources/outreach-bochsler.md`). Its exclusion list is accurate again
   after `18`. A possible shorter route is in the same file: Prof. Peter Heinzmann (cnlab, formerly HSR Rapperswil),
   identity not confirmed. The 2020 report is still the best breach of the wall.
2. **Read tier 2 of `17`.** From `analysis/17-truncated-bodies/`: `python3 -I step_t2.py summary` (the chain writes
   `summary-T2.txt` when it finishes). If the chain stopped, rerun the commands in `stepT2.md` in order; each resumes.
   Judge against `thresholds-T2A/B/J.md`, and weigh the agent's three flags in `stepT2.md`. (a) T2's single columnar
   thresholds are set by noise at w 45, a failed band, and overlap weak true texts at six lengths. (b) T1 w 31–45 and
   T2 w 9–30 pass or fail near the 80% line. (c) Only b = 0 is testable for the joint attack. Then record the result in
   `17`'s README, canon, H1 and H6.
3. **Then the wall, or stop.** Every family with a solver is excluded. What remains open: double columnar with
   w2 ≥ 16 or w1 ≥ 16 (the wall), disrupted columnar, nulls inserted before transposition, sets of n > 50, a 9 × 9
   grille on T2 (H11). The only internal route to the wall is a double columnar method that passes a control at
   w2 16–20 on 615 letters. Lasry reports over 60% at 19 × 20 on 599 letters; our implementation fails there
   (`01-solver`). A session on that is method research, not a run.

## Open questions
- Where does T1's P excess come from (35 vs 16 without a P-bearing stop word)? No modelled convention fits P, U and S
  together.
- What are T2's seven F's? No sourced convention produces them.
- Are the REF.. final groups (`REFLX`, `REFUD`) a convention or chance? Post hoc p 0.02–0.17.
- Does T1's poor end run past its last 20 letters? With those cut, `18`'s solver again chose to leave T1[577:595]
  unscored (check 3). Not measured directly; bears on H6.
- Who or what is "Blume"? Probably a registered telegraphic address. Fuentes's BNE *Anuario* 1936 lead is unread.
- The "Cde" stamp: why 14.00 rather than 15.98?

## Named walls
- **Double columnar, w2 ≥ 16 (alone) or ≥ 18 (jointly), or w1 ≥ 16.** At 615 + 160 letters the IDP has no gradient
  beyond 3–4 swaps of the true key (`01-solver`). This is the top-ranked family (K1). Breach: a crib of 60–100
  letters, the key phrases, a third message in the same keys, the 2020 report, or a method that passes a control.
- **Sets of n and Nihilist on T2 at n 16–30** (`18`). At 160 letters a wrong key fits better than the true one, so no
  search budget breaches it. Only T1, or a shared key, can test those widths.

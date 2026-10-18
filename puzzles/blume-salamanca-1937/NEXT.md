# NEXT — handoff for the next session

**Last session:** 2026-10-18 (session 7: feasibility and method audit, `analysis/23-method-audit`).
**Where it stopped:** no solution, no new target search. Transposition remains the best working hypothesis;
its exact system and preparation are unidentified. Existing searches produced useful conditional negative
results. The four 21/22 target sweeps cost 26.278 CPU hours; longer-key recovery is not established.

**Read the audit first.** Earlier “excluded/refuted” labels below mean negative results under the specified
model, plant distribution, budget and recovery rule. They are not proofs over every key or historical variant.
Experiment 12 does not refute all non-transposition systems; H12 is weakened. Similar letter counts do not
establish one system or shared keys. The controls are modified literary text, not independent period trade
telegrams. Werner's wool account is testimony, not known plaintext.

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
1. **Outside evidence before a wider blind sweep.** The 2020 attempt reported in Bochsler's note 44 remains
   the best lead. Greg can send the existing draft (`sources/outreach-bochsler.md`); nothing has been sent.
   Seek the note/report, its system tests, and any source material not in our file. Identify BLUME through
   registered telegraphic-address lists, Salamanca business directories, and receiving records. Seek Oswald
   drafts, replies, more traffic or key instructions in BAR/PARES. No new evidence was acquired by this audit.
2. **Calibrate before another long search.** Freeze independent period telegram plaintexts and a clean
   baseline. Test recognition with the correct key separately from blind recovery, at 615 and 160 letters.
   Vary STOP/X, abbreviations/names, nulls before transposition, and transmission errors one at a time. Keep
   target edits out of this exercise. Full proposed protocol is in `23`; it has not been run.
3. **Then choose a bounded computational test.** A dossier-built second-key list, with a planted list key and
   fixed phrase/ranking conventions, or a crib supported by external material. Bourdeau already tried 6.6 M
   generic dictionary words/phrases; extending that list is not itself a new lead. New priors or budgets must
   pass controls in the failing region before a target campaign. Longer-key sweeps and new cipher families
   have no demonstrated recovery budget and are lower priority.

These are the audit's recommendations; no new target campaign was started. If evidence and calibration
produce no way forward, pause at the named wall instead of defaulting to longer keys.

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
- **System and preparation unidentified.** More traffic, key instructions, the reported 2020 study, or a
  historically grounded model with passing controls would breach this wall. Better hardware alone does not.
  The long-key difficulty below is measured for our IDP implementation, not a universal impossibility result.
- **Double columnar with w2 ≥ 18 at any w1, or w1 ≥ 16 with w2 ≥ 16, on 615 letters** (`21`).
  - The IDP brings a climb back to the true K2 only from within 2–4 swaps, and shows no gradient outside.
  - The share of keys inside that basin falls about tenfold per unit of w2.
  - Measured: 16 × 17, no hit in 48 M evaluations; 10 × 20, one hit in 114 M.
  - Breach: K2 candidates from outside the search (item 3), a crib of 60–100 letters, more text under the same
    keys, the 2020 report, or for w1 ≤ 10 × w2 18–20 only, 70–200 M evaluations per pair as a pilot extrapolation, requiring a control first.
- **Sets of n and Nihilist on T2 at n 16–30** (`18`). At 160 letters a wrong key fits better than the true one. No
  budget breaches it; only T1 or a shared key can test those widths.

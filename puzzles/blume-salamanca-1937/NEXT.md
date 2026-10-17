# NEXT — handoff for the next session

**Last session:** 2026-10-17 (session 5: the diagnosis restart, `PROMPT-diagnose.md`, stages 1–4)
**Where it stopped:** at a sharper version of the old wall. Diagnosis says these are letters of a natural-letter
text in a new order (`12`), one system for both telegrams (`11`), with odd letters no sourced convention explains
(X and P in T1, F in T2; `10`). Every family we can solve is excluded, at full length and on bodies with the end cut
off (`17`). The top-ranked family, double columnar with long keys, is the one we cannot attack at this length.

## What the diagnosis found (details in `sources/key-type-ranking.md` and `research.md`, session 5)
- **Type.** Transposition family only. Substitution, Vigenère, bifid, ADFGX, Playfair, homophonic, nomenclator and
  codebooks are refuted (H12). A jargon code under transposition cannot be told apart by letters (H10).
- **Odd letters.** X at every stop overshoots (12.5 vs 6). X nulls fit, but only at T1's own rate. Position cannot
  tell stop from null (`09`). Without PUNTO, P is T1's largest misfit (35 vs 16). T2's F fits only F-as-stop, which
  has no source. The German army used X as a stop by 1930 (survey).
- **Two suggestive anomalies, neither established.** T1's last 20 letters are rare-letter rich (p = 0.019 after
  location correction; H6). The shared strings: family-wise p 0.008–0.052 (`13`). Plus one found after looking:
  the telegrams' bigram profiles overlap beyond their letter counts (p ≈ 0.003 under long-key plants; `14`).
- **Corrections to earlier work.** `08`'s p values were inflated by an English glossary in one held-out book (now
  excluded; Spanish T1 0.08 → 0.014). `05`'s controls reused the plant's seed, so the solver started at the planted
  key: sets of n are excluded only for n ≤ 10, and Nihilist by rows is untested (`15`).

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
| single columnar, one key, shared phrase, trimmed ends | w 5–30 (no geometry fits the shared runs) | 99.6% | best 2 runs, chance | `16` |
| word, row and serpentine routes, block moves | widths 5–30, sets 3–12 | 20/20 | no bigram structure | `04` |
| letters permuted within sets of n | **n ≤ 10 only** (n ≥ 20 untested) | n 5: 20/20, n 10: 18/20 | best −5.86 | `05`, `15` |
| 4 × 4 turning grille, T2 | all keys; with an end tail; after a 1–15 preamble | 10/10; 20/20; 30/30 | −6.30; —; −5.86 | `06`, `15`, `17` |
| short-distance systems (sets 5–12, row routes) | any alignment | power 0.78–0.98 | no contact structure | `14` |

## Do first
1. **Greg: send or drop the Bochsler letter** (`sources/outreach-bochsler.md`). The 2020 report could hold a key, a
   plaintext or a third message. It is still the best breach of the wall.
2. **Overnight run: tier 2 of `17`.** Head trims and two-sided trims (a, b ∈ {0, 5, 10, 15, 20}), and the joint
   double columnar attack T1[0 : 615 − b] + T2[0 : 155] under shared keys. Reuse `step_a.py`, `step_b.py` (seed
   streams fixed); controls first at each new length. Cost: about 196 × 30 s per body for double columnar.
3. **A working solver for sets of n ≥ 20 and Nihilist read by rows.** Without one these families are untested, not
   excluded (`15`). Nihilist by rows is `07`'s remaining mechanism for the shared strings, though under `07`'s model
   it gives 22–74 shared 4-grams against 9 observed. Start with annealing plus block moves, as `colsolve.py` does.
4. Lower: a 9 × 9 turning grille on T2 (H11; 160 = 2 × 80), only if one system for both stops being the reading.

## Open questions
- Where does T1's P excess come from (35 vs 16 without a P-bearing stop word)? No convention we modelled fits P, U
  and S together.
- What are T2's seven F's? No sourced convention produces them.
- Are the REF.. final groups (`REFLX`, `REFUD`) a convention or chance? No source found; post hoc p 0.02–0.17.
- Who or what is "Blume"? Probably a registered telegraphic address. Fuentes's BNE *Anuario* 1936 lead is unread.
- The "Cde" stamp is the code-language rate class, which five-letter cipher groups qualify for (Art. 10); the two
  fees per word agree within 3%. Why 14.00 rather than 15.98 is still open.

## Named walls
- **Double columnar, w2 ≥ 16 (alone) or ≥ 18 (jointly), or w1 ≥ 16.** At 615 + 160 letters the IDP has no gradient
  beyond 3–4 swaps of the true key (`01-solver`, probe). This is now the top-ranked family (K1), so the wall sits
  where the answer most likely is. Breach: a crib of 60–100 letters (Lasry's hybrid attack), the key phrases, a third
  message in the same keys, the 2020 report, or a method that passes a control there.
- **No solver for sets of n ≥ 20 or Nihilist by rows at these lengths** (`15`). Breach: a solver that passes an
  independently seeded control.

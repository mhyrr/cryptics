# 29-rowcol-table — the one-table row-and-column transposition (H14, HE-P01) on complete rectangles

**Question.** Givierge (1925) and Hitt (1916) use "double transposition" for one table with a keyed column order
and one keyed row order, whole text, no filler (`sources/historical-evidence/`, HE-P01). On a complete rectangle a
fixed rearrangement turns it into `18`'s sets-of-n problem (one within-set key, sets in any order); `28` checked
this on 200/200 keys. `18` ran on the raw text, not on the rearranged text. Is T1 (615 = 15 × 41 = 41 × 15) or T2
(160 = 8 × 20 = 10 × 16 = 16 × 10 = 20 × 8) this system at those shapes?

## Method (`rowcol.py`, `run29.py`)
Two writing directions (as in `28/check.py`):
- **D1, write rows / read columns.** The cipher is the columns in column-key order, each column's letters in
  row-key order. Cut the ciphertext into w chunks of h and read across: h sets of n = w (plaintext rows).
- **D2, write columns / read rows.** The plaintext goes down the columns; the cipher is the rows in row-key order,
  each row's letters in column-key order. Take every w-th letter: w sets of n = h (plaintext blocks of h).

Cells (telegram, w, direction → n): T1 w15 D1 (15), w15 D2 (41), w41 D1 (41), w41 D2 (15); T2 w8 D1 (8),
w8 D2 (20), w10 D1 (10), w10 D2 (16), w16 D1 (16), w16 D2 (10), w20 D1 (20), w20 D2 (8). Twelve cells.

The rearranged text is solved by `18-periodic-solver/setsolve.solve(rt, n, 0, seed)`, imported unchanged (same
PARAMS, same Spanish model). `rowcol.encrypt` builds the table and shares no code with `rowcol.rearrange`; the
self-test asserts the cipher equals `28`'s simulation, that rearrange inverts, that the rearranged text is `18`'s
family (`28`'s `is_sets_family` and regrouping), and that the true order gives adjacency 1 under `18`'s measure.

## Plan (written 2026-10-20, before any control, noise, calibration or target run in this folder; committed before the run)
The steps below are the pre-registration. Results go under "Result"; this section is not edited afterwards.

- **Fixed offset 0, every letter scored** (`solve`, not `solve_scan`). Complete rectangles have no preamble; an
  offset scan would let the solver leave T1's poor end unscored (the selection effect `18`'s fourth post hoc check
  found).
- **Plants.** Held-out Spanish telegraph text (`01-solver/plaintext.py`, glossary book excluded, as `18`), exactly
  615 (T1 cells) or 160 (T2 cells) letters, encrypted in the row-and-column system itself with independent random
  column and row keys, then rearranged. 10 plants per cell (120).
- **Seeds.** String-keyed streams "29-plant", "29-control-solver", "29-noise", "29-noise-solver",
  "29-calib-plant", "29-calib-solver", "29-target-shuffle", "29-target-solver", drawn in a fixed order. The
  control code asserts the solver's first stage-1 start is not the planted order.
- **Recovery.** At least 90% within-row neighbour accuracy on the rearranged text (`setsolve.adjacency_acc`,
  a = 0).
- **Gate.** A cell passes at ≥ 8/10 recovered. A failing cell is "not testable"; its target is not run or read.
  `18` found T2 n 16–30 not testable at 160 letters; those cells are included and the gate decides.
- **Noise.** 3 own-letter shuffles per (telegram, n), each rearranged identically by every cell with that n
  (T1 n 15, 41; T2 n 8, 10, 16, 20; 36 runs), same solver at offset 0. A cell's noise maximum is the maximum over
  its (telegram, n) group.
- **Threshold per cell, fixed after controls and noise and before the target:** midpoint between the group's
  highest noise score and the cell's lowest recovered-plant score; if they overlap, the noise maximum, and a target
  above it is read by hand. Written to `thresholds.json` and into this README, and committed, before any target run.
  `run29.py target` refuses to run without it.
- **Target.** T1 and T2 in passing cells, plus one own-letter shuffle per cell (descriptive). Record best score,
  order and the first 80 letters of the decryption.
- **Secondary, descriptive only (not part of the gate).** 5 plants per T1 cell from the real 1937 telegrams P1
  and M1 in `sources/historical-evidence/calibration-telegrams.md` (accents stripped, Ñ → N, letters only; plants
  0, 2, 4 from P1 (1,654 letters), 1, 3 from M1 (903); 615 consecutive letters from a seeded random start; P1's
  service lines and signatories are left in, as printed). Report recovery and scores against the cell threshold.
- **Candidate rule.** A telegram score above its cell threshold is read. A candidate must read as Spanish across the
  whole text under one stated system, with independent re-decryption (`verify29.py`). Nothing is tuned after a
  target score is seen.

### Not covered
- Incomplete rectangles (615 or 160 not divisible by w): unequal columns whose lengths depend on the column key,
  needing a long-column assignment search and their own design.
- Other complete shapes (T1 3 × 205, 5 × 123, …; T2 5 × 32, 32 × 5): set sizes outside `18`'s tested band.
- Preambles, trimmed ends, nulls; plants are literary proxies, not commercial telegrams.
- A negative excludes only these shapes under `18`'s model and budget.

## Run
```
python3 -I rowcol.py                   # self-test
python3 -I run29.py controls           # -> controls.jsonl
python3 -I run29.py noise              # -> noise.jsonl
python3 -I run29.py calib              # -> calibration.jsonl (descriptive)
python3 -I run29.py thresholds         # -> thresholds.json
python3 -I run29.py target             # -> target.jsonl (refuses without thresholds.json)
python3 -I run29.py summary > result.txt
python3 -I verify29.py                 # independent re-decryption and re-scoring
```

## Result

### Controls, noise and thresholds (2026-10-20, fixed before any target run)
`controls.jsonl` (120 plants), `noise.jsonl` (36 runs), `thresholds.json`.

| cell | recovered | recovered plants' scores | noise max | threshold | verdict |
|---|---|---|---|---|---|
| T1 w15 D1 n15 | 10/10 | −4.244 to −3.991 | −6.265 | −5.255 | pass |
| T1 w15 D2 n41 | 10/10 | −4.250 to −4.015 | −5.599 | −4.924 | pass |
| T1 w41 D1 n41 | 10/10 | −4.156 to −3.996 | −5.599 | −4.878 | pass |
| T1 w41 D2 n15 | 10/10 | −4.202 to −3.943 | −6.265 | −5.234 | pass |
| T2 w8 D1 n8 | 10/10 | −4.207 to −3.834 | −5.811 | −5.009 | pass |
| T2 w8 D2 n20 | 9/10 | −4.379 to −3.985 | −4.960 | −4.669 | pass |
| T2 w10 D1 n10 | 10/10 | −4.326 to −4.097 | −5.728 | −5.027 | pass |
| T2 w10 D2 n16 | 6/10 | — | −5.277 | — | not testable |
| T2 w16 D1 n16 | 9/10 | −4.330 to −3.876 | −5.277 | −4.803 | pass |
| T2 w16 D2 n10 | 10/10 | −4.072 to −3.862 | −5.728 | −4.900 | pass |
| T2 w20 D1 n20 | 8/10 | −4.198 to −3.978 | −4.960 | −4.579 | pass |
| T2 w20 D2 n8 | 10/10 | −4.229 to −3.892 | −5.811 | −5.020 | pass |

Every threshold is a midpoint (no overlap). Of the 8 failed plants, 7 score below their own true key (a search
miss) and one (T2 w10 D2) scores just above it. T2 w10 D2 (n 16, 10 sets) fails the gate, so its target is not run.
T2 w16 D1 (n 16, 10 sets) and w8 D2 / w20 D1 (n 20, 8 sets) pass, unlike `18`'s T2 16–20 band (3–4/10 with an
offset scan and random preamble and tail): here every letter is in a full set at a known offset. Margins at
T2 n 20 are narrow (noise −4.96, lowest recovered −4.38).

**Calibration plants (`calibration.jsonl`, run before the thresholds were computed, descriptive):** 20/20
recovered (19 at adjacency 1.0, one at 0.925). Scores −4.06 to −4.37, every one above its cell threshold by 0.71 or
more; P1's signatory-list stretches score lowest (−4.34, −4.37). Real 1937 telegraphese sits where the literary-proxy
plants sit under this model.

### Target (`target.jsonl`, `result.txt`, verified by `verify29.py`)
**No candidate.** Every telegram score is below its cell threshold by 0.45–1.04. No reading shows Spanish.

| cell | telegram best | threshold | margin | own-letter shuffle (descriptive) |
|---|---|---|---|---|
| T1 w15 D1 n15 | −6.146 | −5.255 | −0.891 | −6.222 |
| T1 w15 D2 n41 | −5.619 | −4.924 | −0.694 | −5.668 |
| T1 w41 D1 n41 | −5.615 | −4.878 | −0.738 | −5.677 |
| T1 w41 D2 n15 | −6.119 | −5.234 | −0.886 | −6.252 |
| T2 w8 D1 n8 | −6.053 | −5.009 | −1.044 | −5.711 |
| T2 w8 D2 n20 | −5.220 | −4.669 | −0.551 | −5.147 |
| T2 w10 D1 n10 | −5.473 | −5.027 | −0.446 | −5.661 |
| T2 w10 D2 n16 | not run (gate 6/10) | — | — | — |
| T2 w16 D1 n16 | −5.386 | −4.803 | −0.583 | −5.328 |
| T2 w16 D2 n10 | −5.473 | −4.900 | −0.573 | −5.729 |
| T2 w20 D1 n20 | −5.196 | −4.579 | −0.617 | −5.224 |
| T2 w20 D2 n8 | −5.906 | −5.020 | −0.886 | −5.943 |

`verify29.py` (own encryption, rearrangement and quadgram score; no shared code): 120 controls and 20 calibration
plants re-encrypted from their stored keys and re-scored, 36 noise and 22 target runs re-decrypted from the stored
orders, 0 mismatches.

**Seen after the run, not foreseen by the plan: the cells come in identical pairs.** D1 at width w and D2 at width
L/w give the same rearranged text (D2 is D1 on the transposed table: chunk k, letter i = ct[k·h + i] in both).
So T1 w15 D1 ≡ T1 w41 D2, T1 w15 D2 ≡ T1 w41 D1, T2 w8 D1 ≡ w20 D2, w8 D2 ≡ w20 D1, w10 D1 ≡ w16 D2,
w10 D2 ≡ w16 D1. Each pair was run with independent plants and solver seeds; the target readings agree where the
solver converged (T2 w10 D1 and w16 D2 give the same order and score, −5.473; three pairs differ by ≤ 0.03, a
search spread; T2 w8 D1 / w20 D2 differ by 0.15, −6.053 vs −5.906, so the n 8 run at w8 D1 stopped short of the
pair's best, still 0.89 below either threshold). Consequence for the gate: the not-testable cell T2 w10 D2 is the same rearranged problem as
T2 w16 D1, which passed 9/10 and whose target was read (−5.386 vs −4.803). Pooled over the pair, controls are 15/20,
below the 8/10 rule. Under the frozen plan T2 w10 D2 stays "not testable"; the pairing is reported, not used to
change a verdict.

Descriptive: under the fixed offset, T1 lies above its single own shuffle in all four cells (by 0.05–0.13), and T2
in four of seven. One shuffle per cell cannot price this; `18`'s fourth post hoc check found T1 at its shuffles' 90th
percentile at fixed offsets. Not pursued.

**Excluded now (controls pass, complete rectangles, no preamble or tail):** the one-table row-and-column
transposition (keyed columns, one keyed row order, both writing directions) for T1 at 15 × 41 and 41 × 15, and for
T2 at 8 × 20 and 20 × 8 (both directions), 10 × 16 (D1) and 16 × 10 (D2), under `18`'s model and budget. T2 w16 D1
passed its own gate (9/10) and is below threshold, but it is the same rearranged problem as the not-testable w10 D2
(pooled 15/20), so the n 16 rearrangement of T2 is reported as below threshold with a weak gate, not as excluded.

**CPU time.** 343 s recorded solver CPU over 198 runs (controls 174, noise 68, calibration 54, target 47); about
3.5 min wall on 6 workers.

### Limits
- Complete rectangles only. Incomplete widths (unequal columns, long columns set by the column key) are not covered
  and need a long-column assignment search with its own design.
- No preamble, trimmed end or nulls; one stated key per axis; row and column keys independent.
- Plants are literary-proxy telegraphese; the 20 calibration plants from two real 1937 telegrams (P1, M1; not
  commercial, two sources) are the only check on real telegraphese, and they behave like the proxy plants.
- Narrow margins at T2 n 20 (noise −4.96 vs lowest recovered −4.38) and three noise shuffles per (telegram, n).
- A negative excludes only these shapes under `18`'s model and budget; it says nothing about double columnar or other
  preparation.

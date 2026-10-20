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

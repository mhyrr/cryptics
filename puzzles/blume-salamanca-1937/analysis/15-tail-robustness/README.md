# 15-tail-robustness — do the exclusions survive untransposed letters at an end?

## Question
Every exclusion so far ran its solver on all 615 (or 160) letters. If a few letters at one end were never
transposed, do those solvers still recover the body?

## Candidate
**K2: the telegrams carry untransposed groups at an end** (an indicator, a reference, or nulls appended after
transposition). `09` found T1's last 20 letters rich in rare letters (location-corrected p = 0.019), and both
final groups begin REF (T1 `REFLX`, T2 `REFUD`; seen after looking). A columnar transposition's column lengths
depend on the exact body length, so a few letters outside the body may break those searches. K2 matters only if
it does. This experiment measures that.

## Pre-registered readings
Copied verbatim from the dispatch before anything was run. Not edited afterwards.

- For each family and end: if recovery at t ≥ 5 is at least 80% of recovery at t = 0, that exclusion is tail-robust, and K2 does not reopen the family at that end.
- If recovery at some t ≥ 5 falls below 50% of recovery at t = 0, that exclusion is void for bodies with untransposed letters at that end. The family re-enters stage 4 on truncated bodies T1[a : 615 − b] and T2[a : 160 − b], with a and b in steps of 5 up to 20, each with its own planted control.
- Between 50% and 80%: "partly robust". The family re-enters stage 4 only for the t values where recovery fell below 80%.
- A family whose t = 0 control fails at this budget is "not measured" here and the reading does not apply to it.

## Method
Python 3 standard library and the existing C solver, `python3 -I`, fixed seeds. `common.py` imports
`01-solver` the way `08-letter-fit/fit.py` does. `run.py` imports `05-periodic/periodic.py` and
`06-grille/grille.py` and calls their code unchanged. No solver here sees a real telegram. The only telegram
letters read are T1's last 20, used as a bag of letters for one fill.

**Plants (`run.py`).** Spanish telegraph plaintext (`plaintext.telegram`, held-out books, 27738 excluded) of
L − t letters is enciphered. Then t untransposed letters go at the end (t = 5, 10, 15, 20) or at the start
(t = 5, 10, 15), so the total is L. L = 615 for families 1–4 and 160 for family 5. The t letters are uniform
random letters, or letters drawn from T1's last 20 (`AXLNKIPLANFTULXREFLX`). Within a cell the plants
alternate between the two fills. t = 0 is the baseline. A cell is (family, width band, t, end).

**Solvers, each run as its exclusion ran:** on all L letters, told the true width, same budget.
1. Single columnar, forward, incomplete last row (`colsolve.py`, new). w ≤ 8: exhaustive over w! keys.
   w ≥ 9: simulated annealing on the total Spanish quadgram score, 2 runs of 10,000 · w steps, temperature
   30 → 1 (log10 units). Moves: swap, single move, block move. In a scratch pilot, plain hill climbing
   failed from w = 20. One annealing run of 10,000 · w steps recovered 9/9 at w 20–30 but only 1/6 at w 35–45.
   So the band w 31–45 first ran its t = 0 control alone. It passed (9/10), and its tail cells were then added
   with `run.py single 8 --resume` (the band is last in the seed stream, so no earlier seed moved). Bands:
   w 5–8 (20 plants per cell), w 9–30 (10), w 31–45 (10). The width is drawn uniformly within the band.
2. Double columnar CC, `01-solver/out/dtsolve solve`, 90 s per run, 8 runs in parallel (as `03`). Bands
   w1 × w2 = 10 × 13 and 14 × 14. 5 plants per cell (3 uniform fill, 2 T1-tail fill).
3. Letters permuted within sets of n: `periodic.solve` unchanged (12 restarts, patience 1,500), n = 5, 10, 20,
   35. 20 plants per cell.
4. Nihilist read by rows: the `nihilist_control.py` plant (full rows reordered, each row permuted by one column
   key), solved by `periodic.solve`, n = 8, 15, 25. 20 plants per cell. The solver does not restore row order,
   so the reference is the row-reordered text: a letter is "in place" when it sits at its place within its row.
5. 4 × 4 turning grille, 160 letters: `grille.best` over all 1,024 keys, standard use, as `06`'s controls.
   A 160 − t body is not a multiple of 16. Its full blocks go through the grille and the partial last block
   stays in clear, as `periodic.enc` treats a partial set. t = 5, 10 at either end. 20 plants per cell.

**Seeds.** Every plant gets a plant seed and a separate solver seed from its family's master stream. This
matters for families 3 and 4. 05's controls seeded the solver with the plant's own seed, so the first
restart drew the planted key: 78/78 periodic and 72/72 Nihilist plants (`check05_seed.py`,
`check05-seed.txt`). Here the solver starts from keys of its own.

**Recovery.** The body's window of the full decryption (positions 0 … L − t − 1 for an end tail, t … L − 1
for a start tail) is compared with the body reference by `control.py`'s `shift_acc` (cyclic shift up to 40). A
plant is recovered at ≥ 90% of body letters in place. At t = 0 this is `control.py`'s measure on the whole
text. The 01 controls used 95%. `summarize.py` applies the pre-registered readings per band and end. A band
whose t = 0 recovery is below 80% (the 01 pass rule) is "not measured".

## Run
From this folder. Family 2 ran alone, so that dtsolve had 8 cores as in `03`.
```
python3 -I run.py double 8      # 80 runs x 90 s, 15 min wall
python3 -I run.py grille 8      # 2 s
python3 -I run.py periodic 8    # 7.5 min
python3 -I run.py nihilist 8    # 5 min
python3 -I run.py single 8      # 10.5 min (w 31-45 at t = 0 only, as first frozen)
python3 -I run.py single 8 --resume   # w 31-45 tail cells, 12 min
python3 -I summarize.py > result.txt
python3 -I check05_seed.py > check05-seed.txt   # no solving; replays 05's seed streams
python3 -I colsolve.py          # self-test: decryption agrees with transpo.col_dec
```
Total about 50 minutes of wall time on 8 cores (2026-10-17). Per-plant records, with the first 60 letters of
each body decryption, are in `out/<family>.jsonl` (gitignored). The tables below are `result.txt`.

## Result
Recovery is k/N plants with ≥ 90% of body letters in place. In brackets: (uniform fill; T1-tail fill), then
the median body accuracy.

### 1. Single columnar, forward, incomplete last row (`colsolve.py`)
| t, end | w 5–8 | w 9–30 | w 31–45 |
|---|---|---|---|
| 0 (baseline) | 20/20 [1.00] | 10/10 [1.00] | 9/10 [1.00] |
| 5, end | 0/20 (0/10; 0/10) [0.42] | 0/10 (0/5; 0/5) [0.41] | 0/10 (0/5; 0/5) [0.14] |
| 10, end | 0/20 (0/10; 0/10) [0.22] | 0/10 (0/5; 0/5) [0.19] | 0/10 (0/5; 0/5) [0.11] |
| 15, end | 0/20 (0/10; 0/10) [0.21] | 0/10 (0/5; 0/5) [0.12] | 0/10 (0/5; 0/5) [0.11] |
| 20, end | 0/20 (0/10; 0/10) [0.25] | 0/10 (0/5; 0/5) [0.14] | 0/10 (0/5; 0/5) [0.11] |
| 5, start | 0/20 (0/10; 0/10) [0.39] | 0/10 (0/5; 0/5) [0.21] | 0/10 (0/5; 0/5) [0.24] |
| 10, start | 0/20 (0/10; 0/10) [0.26] | 0/10 (0/5; 0/5) [0.21] | 0/10 (0/5; 0/5) [0.11] |
| 15, start | 0/20 (0/10; 0/10) [0.22] | 0/10 (0/5; 0/5) [0.15] | 0/10 (0/5; 0/5) [0.13] |

The best tail plant read 76% of its body. The one t = 0 failure scored below its true text, so it is a search
failure.

### 2. Double columnar CC (`dtsolve`, 90 s per run)
| t, end | 10 × 13 | 14 × 14 |
|---|---|---|
| 0 (baseline) | 5/5 [1.00] | 5/5 [1.00] |
| 5, end | 0/5 (0/3; 0/2) [0.11] | 0/5 (0/3; 0/2) [0.10] |
| 10, end | 0/5 (0/3; 0/2) [0.11] | 0/5 (0/3; 0/2) [0.10] |
| 15, end | 0/5 (0/3; 0/2) [0.10] | 0/5 (0/3; 0/2) [0.10] |
| 20, end | 0/5 (0/3; 0/2) [0.10] | 0/5 (0/3; 0/2) [0.10] |
| 5, start | 0/5 (0/3; 0/2) [0.11] | 0/5 (0/3; 0/2) [0.10] |
| 10, start | 0/5 (0/3; 0/2) [0.10] | 0/5 (0/3; 0/2) [0.10] |
| 15, start | 0/5 (0/3; 0/2) [0.10] | 0/5 (0/3; 0/2) [0.10] |

The best tail plant read 12% of its body, which is the noise level.

### 3. Letters permuted within sets of n (`05` `periodic.solve`)
| t, end | n 5 | n 10 | n 20 | n 35 |
|---|---|---|---|---|
| 0 (baseline) | 20/20 [1.00] | 18/20 [1.00] | 1/20 [0.50] | 0/20 [0.26] |
| 5, end | 20/20 (10/10; 10/10) [1.00] | 19/20 (9/10; 10/10) [1.00] | 0/20 (0/10; 0/10) [0.50] | 0/20 (0/10; 0/10) [0.27] |
| 10, end | 20/20 (10/10; 10/10) [1.00] | 17/20 (7/10; 10/10) [0.99] | 1/20 (0/10; 1/10) [0.50] | 0/20 (0/10; 0/10) [0.30] |
| 15, end | 20/20 (10/10; 10/10) [1.00] | 16/20 (7/10; 9/10) [1.00] | 0/20 (0/10; 0/10) [0.49] | 0/20 (0/10; 0/10) [0.29] |
| 20, end | 20/20 (10/10; 10/10) [1.00] | 17/20 (9/10; 8/10) [0.99] | 0/20 (0/10; 0/10) [0.52] | 0/20 (0/10; 0/10) [0.29] |
| 5, start | 20/20 (10/10; 10/10) [1.00] | 2/20 (0/10; 2/10) [0.54] | 0/20 (0/10; 0/10) [0.39] | 0/20 (0/10; 0/10) [0.23] |
| 10, start | 20/20 (10/10; 10/10) [1.00] | 16/20 (8/10; 8/10) [1.00] | 0/20 (0/10; 0/10) [0.29] | 0/20 (0/10; 0/10) [0.21] |
| 15, start | 20/20 (10/10; 10/10) [1.00] | 2/20 (1/10; 1/10) [0.44] | 0/20 (0/10; 0/10) [0.36] | 0/20 (0/10; 0/10) [0.18] |

All 41 t = 0 failures scored below their true text, so all are search failures.

### 4. Nihilist read by rows (`05` `nihilist_control` plant, `periodic.solve`)
| t, end | n 8 | n 15 | n 25 |
|---|---|---|---|
| 0 (baseline) | 14/20 [1.00] | 2/20 [0.60] | 0/20 [0.43] |
| 5, end | 13/20 (8/10; 5/10) [1.00] | 3/20 (0/10; 3/10) [0.65] | 0/20 (0/10; 0/10) [0.42] |
| 10, end | 15/20 (8/10; 7/10) [0.99] | 2/20 (2/10; 0/10) [0.60] | 0/20 (0/10; 0/10) [0.38] |
| 15, end | 16/20 (10/10; 6/10) [1.00] | 3/20 (2/10; 1/10) [0.58] | 0/20 (0/10; 0/10) [0.40] |
| 20, end | 15/20 (5/10; 10/10) [0.99] | 4/20 (2/10; 2/10) [0.68] | 0/20 (0/10; 0/10) [0.39] |
| 5, start | 0/20 (0/10; 0/10) [0.54] | 0/20 (0/10; 0/10) [0.44] | 0/20 (0/10; 0/10) [0.30] |
| 10, start | 0/20 (0/10; 0/10) [0.64] | 0/20 (0/10; 0/10) [0.37] | 0/20 (0/10; 0/10) [0.25] |
| 15, start | 2/20 (0/10; 2/10) [0.65] | 4/20 (2/10; 2/10) [0.60] | 0/20 (0/10; 0/10) [0.23] |

All 44 t = 0 failures scored below their true text, so all are search failures.

### 5. 4 × 4 turning grille, 160 letters (`06` exhaustive search)
| t, end | 4 × 4 |
|---|---|
| 0 (baseline) | 20/20 [1.00] |
| 5, end | 20/20 (10/10; 10/10) [0.94] |
| 10, end | 20/20 (10/10; 10/10) [0.97] |
| 5, start | 0/20 (0/10; 0/10) [0.27] |
| 10, start | 0/20 (0/10; 0/10) [0.26] |

### The pre-registered readings, applied mechanically (`summarize.py`)
| family | band | end | t = 0 | reading |
|---|---|---|---|---|
| 1 single columnar | w 5–8, 9–30, 31–45 | end | 39/40 | **void** (0/40 at each t) |
| 1 single columnar | w 5–8, 9–30, 31–45 | start | 39/40 | **void** (0/40 at each t) |
| 2 double columnar CC | 10 × 13, 14 × 14 | end | 10/10 | **void** (0/10 at each t) |
| 2 double columnar CC | 10 × 13, 14 × 14 | start | 10/10 | **void** (0/10 at each t) |
| 3 within sets of n | n 5 | end, start | 20/20 | tail-robust at both ends |
| 3 within sets of n | n 10 | end | 18/20 | tail-robust (ratios 0.89–1.06) |
| 3 within sets of n | n 10 | start | 18/20 | **void** (t 5 and 15: ratio 0.11; t 10: 0.89) |
| 3 within sets of n | n 20, 35 | both | 1/20, 0/20 | not measured (control fails) |
| 4 Nihilist by rows | n 8, 15, 25 | both | 14/20, 2/20, 0/20 | not measured (control fails) |
| 5 turning grille 4 × 4 | — | end | 20/20 | tail-robust |
| 5 turning grille 4 × 4 | — | start | 20/20 | **void** |

## Reading (script author's reading)
The main thread judges. This is how the author reads the pre-registered rules against the numbers.

**The columnar exclusions do not survive K2.** Single columnar (Bourdeau, w 5–45) and double columnar CC
(`03`, at 10 × 13 and 14 × 14) recover 39/40 and 10/10 plants at t = 0. They recover none with 5 or more
letters outside the body, at either end. The reason is structural. These solvers take column lengths from the total length, so t extra
letters mislabel columns as long or short and shift every chunk read after them. A start tail also offsets
every chunk. Fill letters make no difference. By the first void rule, both families re-enter stage 4 on
truncated bodies T1[a : 615 − b] and T2[a : 160 − b], a and b in steps of 5 up to 20, each with its own planted
control. The double columnar reading was measured only at two bands. The mechanism does not depend on the
band, so the author expects it to hold for every w1 × w2 that `03` excluded. That is an inference, not a
measurement.

**Block families split by end.** For sets of n and the 4 × 4 grille, the solver cuts the text into blocks
from the first letter and leaves a partial last block out of the score. End letters touch at most the last
scored block, so those exclusions are tail-robust at the end. Start letters shift every block boundary
unless t is a multiple of the block size. For n = 5 every tested t is a multiple, and recovery stays at 20/20.
For n = 10, t = 10 recovers (16/20), and t = 5 and 15 collapse (2/20). For the grille, t = 5 and 10 collapse
(0/20). So those exclusions are void for a preamble whose length is not a multiple of the block size. The
grille and the sets-of-n family at the start re-enter stage 4 on truncated bodies.

**The surprise: 05's controls started at the true key.** `periodic.py` and `nihilist_control.py` seeded the
solver with the plant's own seed. The plant drew its key first from that stream, so the solver's first
restart was the planted key in all 150 controls (`check05-seed.txt`). With the solver seeded apart, the same
`periodic.solve` at the same budget recovers:
- sets of n: n 5 20/20, n 10 18/20, n 20 1/20, n 35 0/20;
- Nihilist by rows: n 8 14/20, n 15 2/20, n 25 0/20.

Every failure scores below its own true text, so the method is not at fault: the 12 × 1,500 hill climb does
not find the key. The canon entries "letters permuted within sets of n (n 2–40) excluded" and "Nihilist read
by rows (w 5–40) excluded" therefore rest on controls that did not test the search. Here they are tested
only at n ≤ 10 for sets of n, and nowhere for Nihilist by rows (n 8 is 70%). This also touches `07`.
Nihilist by rows is one of the two families that explain the shared strings, and its exclusion is not
established at any width tested here. Under the fourth pre-registered rule, families 3 (n 20, 35) and 4 are
"not measured" for K2. The end-tail rows above still show the same structural split as family 3. Tails at
the end leave recovery where it was (n 8: 13–16/20 against 14/20), and tails at the start collapse it.

**What K2 changes, if the main thread accepts this.** The exclusions that matter for the shared strings
(single columnar, and Nihilist by rows) and the double columnar band no longer cover a body with a few
untransposed letters at either end. The grille and sets-of-n exclusions still cover an appended tail, but
not a preamble.

## Caveats
- **The solvers are told the true width and run at full L.** They do not search over the body length or
  offset. That search is the truncated-body re-entry the readings call for. This experiment only shows that
  the old runs did not do it.
- **Family 2 used 5 plants per cell and 90 s**, against 180 s in `03`. The collapse is total (0/70, median
  accuracy 0.10, the noise level), so the author does not expect a longer budget to change it. Only two
  bands were run.
- **Threshold.** The brief set 90%. The 01 controls used 95%. At 95%, periodic n = 10 has t = 0 at 16/20
  and end cells at 12–16/20 (ratios 0.75–1.0), so its end reading would be "partly robust". But for t = 5 at
  the end, the scored sets are the body's own sets, which is the same scored input as t = 0. The spread is
  solver noise between different plants, not an effect of the tail. The grille's end cells read 93–97% by
  construction (the partial block in clear is scrambled), so they pass at 90% and would fail at 95%.
- **Grille convention.** A 160 − t body has a partial block. Here it stays in clear. A sender who padded it
  would have a body of 160 letters and no tail, so the convention is forced by the brief's arithmetic.
- **Nihilist recovery is within-row placement.** The solver does not restore row order (as in `05`), so
  "in place" is measured against the row-reordered text. Some plants pass at 90–95% without the exact key.
  At Nihilist n = 15 every pass is of this kind; no plant there had the exact key at t = 0. The start-tail
  passes at Nihilist n = 8 (t 15) and periodic n = 10 (t 5, 15) are partial readings of a shifted alignment.
- **The T1-tail fill draws letters at random** from the 20-letter bag. It is not T1's actual sequence.
- **Families 1–4 used T1-length bodies only**, and family 5 used T2 length only. No joint (one key on both
  telegrams) plant was run.
- **`colsolve.py` is new and is not Bourdeau's solver.** Its t = 0 control is 39/40 over w 5–45. Bourdeau's
  exclusion rests on his own solver, which this experiment did not run. The tail failure is structural, so
  the author expects any full-length columnar solver to show it.
- **The w 31–45 band ran in two invocations.** Its tail cells were added after its control passed, which the
  brief allows ("report only where it passes"). The decision rule did not depend on tail results.
- **`05` was not edited.** The seed coincidence and the honest recovery rates are reported here for the main
  thread.

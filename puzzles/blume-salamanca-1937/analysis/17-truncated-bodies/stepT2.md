# 17-truncated-bodies — tier 2: controls, noise and thresholds (run 2026-10-17); target not yet run

Plan: `README.md`, "Bodies" (tier 2) and "Steps" A and B, executed as tier 1 ran them (`stepAC.md`, `stepB.md`),
plus the joint double columnar attack. README.md is not edited. Script: `step_t2.py` (new). Not changed: `step_a.py`,
`step_b.py`, anything in `01-solver` or `15-tail-robustness`. This file reports numbers; the main thread judges.

**Status.** Controls, noise ceilings and all three thresholds files are done and were written before any tier-2
target run. Each target subcommand passed a smoke test (below). **The target run has not been launched.**
No `result-T2*.jsonl` file exists yet.

## Bodies
- **T1[a : 615 − b]**, a ∈ {5, 10, 15, 20}, b ∈ {0, 5, 10, 15, 20}: 20 bodies, 575–610 letters. Groups: `t1-head`
  (b = 0, 4 bodies), `t1-two` (a, b > 0, 16 bodies).
- **T2[a : 160 − b]**, every (a, b) in the grid except (0, 0) and (0, 5), which are done: 23 bodies, 120–155 letters.
  Groups: `t2-head` (b = 0, 4), `t2-tail` (a = 0, b = 10, 15, 20; 3), `t2-two` (16).
- **Joint**: T1[0 : 615 − b] + T2[0 : 155] under one pair of keys, b ∈ {0, 5, 10, 15, 20}.

## Method as run
**Step A, single columnar** (`15-tail-robustness/colsolve.py`, unchanged, called through `step_a.run_control`,
unchanged). Bands w 5–8, 9–30, 31–45. Controls: 10 plants per band at **every distinct body length** (T1 610, 605,
…, 575; T2 155, 150, …, 120). Each body uses its own length's controls; tier 1 instead mapped bodies to the nearest of
four control lengths. Pass: ≥ 8/10 plants with ≥ 90% of letters in place (`control.shift_acc`). Noise ceiling per
length: shuffles of one body of that length (the first in run order), widths 5, 8, 12, 20, 30, 45, three shuffles
each. Threshold per length: halfway between the highest noise score at that length (all six widths, as tier 1) and
the lowest true-text score among recovered plants of the passing bands at that length. A band that fails is not run
on the target.

**Step B, double columnar CC** (`01-solver/out/dtsolve`, unchanged). w1 2–15 × w2 2–15 on the 20 T1 bodies, 30 s per
pair. Controls at every T1 body length (610 … 575, including 595, which tier 1 controlled with other seeds): bands
w2 2–11 and w2 12–15, 10 plants each, w1 drawn from 8–15, 30 s. Pass and fallback as in tier 1: a band failing at 30 s
is rerun at 90 s on the same plants and solver seeds. If it then passes, its target runs use 90 s; if it fails at
90 s, it is not testable. Threshold −5.10, unless a control's true text at that length scores at or below −5.10 (then
halfway between that lowest true text and −5.19).

**Joint attack.** `dtsolve solve` with T2[0:155] as CT2 (the joint mode `03-target-h1/target.py` uses: both texts'
IDP and quadgram scores, weighted by length). **Region: w1 8–15 × w2 16–17, 180 s per pair** (16 pairs per body).
*Why this region, which narrows the README's wording "the joint double columnar attack T1[0 : 615 − b] + T2[0 : 155]":*
on these bodies T1 alone is already excluded at w1 2–15 × w2 2–15. Tier 1 covered b = 5–20, and `01`/`03` searched
b = 0. A shared-key joint search there would add no power. T2 adds power only where T1 alone fails. At 615 + 160,
`01`'s joint controls passed w1 8–15 × w2 16–17 (8/10, where T1 alone gave 7/10) and failed w2 18–20 (1/5). w1 < 8
at w2 16–17 was never controlled. So the joint search runs only where it has shown power.
- Controls: 10 plants per joint length (615, 610, 605, 600, 595, each + 155 letters under the same keys), w1 8–15,
  w2 16–17, 180 s. Plants are drawn as `01-solver/control.py` draws them: plaintext 1, K1, K2, plaintext 2.
- Recovery: measured on the T1-length plaintext (dtsolve reports only that decryption), ≥ 90% in place as in tier 1
  (`01` used 95%). Pass ≥ 8/10. A length that fails is not testable and its target is not run.
- Threshold: −5.10 on the joint per-letter score (`03`'s H2), with the step-B fallback rule.

**Seeds.** Separate `random.Random(<string>)` streams per step and role, all beginning `17-T2-`:
- A: `-A-plant`, `-A-solver-controls`, `-A-shuffle`, `-A-solver-noise`, `-A-solver-target`
- B: `-B-plant`, `-B-control-solver`, `-B-target-solver`
- Joint: `-J-plant`, `-J-control-solver`, `-J-target-solver`

Target seeds are drawn in one fixed order over every body and width of the step (bodies in run order, then w, or
w1 × w2), so a seed does not depend on which bodies are run.

**Start checks.** `python3 -I step_t2.py precheck` ran before any control, and every check also runs inside each
control.
- **A, w ≥ 9.** colsolve's first annealing key, replayed from the solver seed (`step_a.first_restart_key`), differs
  from the planted key in all 480 plants.
- **B and joint.** dtsolve's first K2 candidate is the first random draw of its step 1. `step_t2.dts_k2_draws`
  replays dtsolve's xorshift64* stream. `python3 -I step_t2.py check-replay` builds an instrumented scratch copy of
  `dtsolve.c` (in `out/t2/dtcheck`; `01-solver` untouched) that prints its first 200 draws. The replay matched it on
  30/30 random seeds and widths.
- **The check.** The first draw differs from the planted K2 in every plant with w2 ≥ 6 (asserted). For w2 ≤ 5
  (≤ 120 keys), step 1's 200 draws span the key space for any seed, so no start can avoid the planted K2. That holds
  for target runs too (31 B plants have w2 ≤ 5).
- **By chance.** One B plant at w2 ≥ 6 (plant 45, 14 × 9, L 600) has its planted K2 among the 200 first-iteration
  draws: draw 48, not the first. About 1.66 such plants are expected for independent draws. Its band passes
  without it (10/10 → 9/10).

**Compute.** 5 worker processes: a process pool for colsolve, and a thread pool driving one dtsolve process per
thread. The main thread held the other ~3 cores throughout (load spiked to 47 around 09:30). dtsolve's budget is
wall-clock, so the target should run under similar load. Wall times: B 30 s 16 min (08:16–08:32), joint 30 min
(08:33–09:03), A controls 43 min, A noise 24 min, B 90 s 3 min (10:09–10:12).

## Controls
Per-plant tables, with every failure listed: `python3 -I step_t2.py report-controls` (from `controls-T2A.jsonl`,
`noise-T2A.jsonl`, `controls-T2B.jsonl`, `controls-T2J.jsonl`).

### Step A (recovered / 10)
| length | w 5–8 | w 9–30 | w 31–45 |
|---|---|---|---|
| 610 | 10 pass | 10 pass | 7 **fail** |
| 605 | 10 pass | 10 pass | 8 pass |
| 600 | 10 pass | 10 pass | 7 **fail** |
| 595 | 10 pass | 10 pass | 10 pass |
| 590 | 10 pass | 10 pass | 6 **fail** |
| 585 | 10 pass | 10 pass | 8 pass |
| 580 | 10 pass | 10 pass | 7 **fail** |
| 575 | 10 pass | 10 pass | 8 pass |
| 155 | 10 pass | 7 **fail** | 0 **fail** |
| 150 | 10 pass | 8 pass | 0 **fail** |
| 145 | 10 pass | 6 **fail** | 0 **fail** |
| 140 | 10 pass | 6 **fail** | 0 **fail** |
| 135 | 10 pass | 8 pass | 0 **fail** |
| 130 | 10 pass | 7 **fail** | 0 **fail** |
| 125 | 10 pass | 9 pass | 0 **fail** |
| 120 | 10 pass | 8 pass | 0 **fail** |

Facts for the reader:
- **Borderline bands.** Pooled over lengths, T1 w 31–45 recovers 61/80 (76%) and T2 w 9–30 recovers 59/80 (74%).
  Both sit at the 80% line, so the per-length verdicts in those two bands alternate between pass and fail.
- **155 differs from tier 1.** At 155, w 9–30 failed 7/10 here; tier 1's 155 controls (other plants) gave 10/10.
- **Failures that outscored their true text.** 4 failed plants scored above their own true text, so these are model
  failures, not search failures. All four are in w 31–45 at 120–135 letters (2–4 letters per column), a band that
  failed anyway. Every other failure scored below its true text.

### Step B (recovered / 10)
| length | w2 2–11, 30 s | w2 12–15, 30 s | w2 12–15, 90 s | budget (2–11 / 12–15) |
|---|---|---|---|---|
| 610 | 10 pass | 9 pass | — | 30 / 30 |
| 605 | 10 pass | 9 pass | — | 30 / 30 |
| 600 | 10 pass | 10 pass | — | 30 / 30 |
| 595 | 10 pass | 9 pass | — | 30 / 30 |
| 590 | 10 pass | 10 pass | — | 30 / 30 |
| 585 | 10 pass | 10 pass | — | 30 / 30 |
| 580 | 10 pass | 9 pass | — | 30 / 30 |
| 575 | 10 pass | 7 **fail** | 9 pass | 30 / **90** |

Failures at 30 s: 7 of 160 plants, all with w1 ≥ 12 and w2 ≥ 12 (e.g., 15 × 15 at 580 and 575). True texts
−4.53 to −3.91, all above −5.10.

### Joint, w1 8–15 × w2 16–17, 180 s (recovered / 10)
| joint length | recovered | verdict |
|---|---|---|
| 615 + 155 | 9 | pass |
| 610 + 155 | 7 | **fail (not testable)** |
| 605 + 155 | 5 | **fail (not testable)** |
| 600 + 155 | 6 | **fail (not testable)** |
| 595 + 155 | 6 | **fail (not testable)** |

Of the 17 failures, 15 are at w1 13–15; the other two are 10 × 17 (615) and 11 × 17 (600). All read ≤ 34% in place and score −5.79 to −6.08.
Recoveries came at up to 120 s of the 180 s budget.

## Thresholds (files written before any target run; each target subcommand checks its file line by line)
- **`thresholds-T2A.md`.** Per length:

  | length | threshold | length | threshold |
  |---|---|---|---|
  | 610 | −4.9439 | 155 | −4.3855 |
  | 605 | −4.9557 | 150 | −4.4608 |
  | 600 | −4.9150 | 145 | −4.2458 |
  | 595 | −4.8948 | 140 | −4.2755 |
  | 590 | −4.8512 | 135 | −4.2984 |
  | 585 | −4.8146 | 130 | −4.3278 |
  | 580 | −4.8209 | 125 | −4.2451 |
  | 575 | −4.9427 | 120 | −4.1629 |

  The T1 noise ceilings are −5.43 to −5.64 (all at w 45), and T1 true texts (passing) −4.19 to −4.42.
  **At T2 lengths the formula overlaps.** The noise ceiling comes from w 45, a band that failed. It lies at or above
  the lowest passing true text at 150, 140, 135, 130, 125 and 120. So the threshold sits above some true texts
  (e.g., 120: threshold −4.163, weakest true text −4.278). It is applied as written; the main thread judges. For
  scale, the noise reached at widths inside passing bands only: −4.68 (150), −4.66 (135), −4.35 (125), −4.46 (120),
  and −5.70 to −5.88 where only w 5–8 passed.
- **`thresholds-T2B.md`.** −5.10 at every length (lowest true text −4.53). Budget 30 s everywhere except
  T1[20:595] w2 12–15: 90 s.
- **`thresholds-T2J.md`.** −5.10 at 615 + 155 (lowest true text −4.15); the other four lengths are not testable.

**Widths run per body (step A).** T1 at 605, 595, 585, 575: w 5–45. T1 at 610, 600, 590, 580: w 5–30. T2 at 150,
135, 125, 120 (10 bodies): w 5–30. T2 at 155, 145, 140, 130 (13 bodies): w 5–8 only.

## Smoke tests (written to `out/t2/smoke-*.jsonl`; the real results files do not exist yet)
- **target-a.** T1[5:615] at w 5, 8, 9 (3 runs, 13 s) and T2[20:140] at w 5, 9. It refused with
  `thresholds-T2A.md` moved aside. With `--deadline-min 0.05` it left all jobs out. A rerun skipped all 3 runs
  (resume).
- **target-b.** T1[5:615] at 2 × 2, 8 × 9, 15 × 15 (30 s each, scores −6.82, −6.27, −6.12). It refused when one
  threshold line was altered (file restored afterwards). The deadline and resume behaved as in target-a. The budget
  assignment was checked without running: 56 pairs at 90 s (T1[20:595], w2 12–15) and 3,864 at 30 s.
- **target-j.** b = 0 at 8 × 16 and 15 × 17 (180 s; −6.21, −6.08). Resume behaved as in target-a. The stored T2
  re-decryption (`transpo.double_dec` from dtsolve's keys) reproduces dtsolve's joint score exactly in both runs.

No smoke run scored above its threshold. The smoke seeds are the real jobs' seeds, so the real run repeats these
jobs into the real files.

## Target commands (run order; from this folder; one at a time, since each uses 5 workers)
```
python3 -I step_t2.py target-a t1-head                  # A, T1 head trims           134 runs   ~0.3 h
python3 -I step_t2.py target-b t1-head                  # B, T1 head trims           784 runs   ~1.3 h
python3 -I step_t2.py target-a t1-two                   # A, T1 two-sided            536 runs   ~1.3 h
python3 -I step_t2.py target-b t1-two                   # B, T1 two-sided          3,136 runs   ~5.5 h
python3 -I step_t2.py target-a t2-head,t2-tail,t2-two   # A, T2 bodies               312 runs   ~0.15 h
python3 -I step_t2.py target-j                          # joint, b = 0 only            16 runs   ~0.2 h
python3 -I step_t2.py summary                           # tables for the main thread
```
Chained: join the six lines with `&&`. Each line accepts `--deadline-min M` and resumes where it stopped. Estimated
wall time at 5 workers: **about 8.8 h** (`python3 -I step_t2.py plan`; A from the measured control and noise
timings, B and joint at budget + 0.5 s per run). Outputs: `result-T2A.jsonl`, `result-T2B.jsonl`,
`result-T2J.jsonl`, with full decryptions for B and joint in `out/t2/target-T2*.jsonl`.

## Not run, and why
- **Joint at b = 5, 10, 15, 20.** Not testable (controls 7, 5, 6 and 6 of 10). These cells are open, not excluded.
- **Step A bands that failed** (open, not excluded):
  - w 31–45 at T1 lengths 610, 600, 590 and 580.
  - w 9–30 at T2 lengths 155, 145, 140 and 130.
  - w 31–45 at every T2 length.

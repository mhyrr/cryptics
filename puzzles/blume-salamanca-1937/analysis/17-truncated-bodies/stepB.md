# Step B — double columnar CC on T1 bodies with the tail cut off (tier 1)

Run 2026-10-17 by a dispatched agent, as README.md, Step B, says. README.md is not edited.

## Method as run
- **Solver.** `01-solver/out/dtsolve solve`, unchanged (built 2026-10-16 18:16 from `dtsolve.c` of the same
  minute, commit 13ea045). Convention CC, Spanish model (`out/lm_es_*.bin`), one seed per run.
- **Driver.** `step_b.py` in this folder. It imports `01-solver` as `08-letter-fit/fit.py` does (path and working
  directory), and drives `dtsolve` as `03-target-h1/target.py` does. `python3 -I` (Python 3.14.6), standard library.
- **Workers.** 5 at a time (`ThreadPoolExecutor`, one `dtsolve` process per thread). The machine has 8 cores
  (4 performance, 4 efficiency) and another agent held about 3. `dtsolve`'s budget is wall-clock, so a run on an
  efficiency core does fewer iterations. Controls and target ran under the same load.
- **Seeds.** Three separate streams, each `random.Random(<string>)`: `"17-B-plant"` (plant widths and plant seed),
  `"17-B-control-solver"` (control solver seeds), `"17-B-target-solver"` (target seeds, drawn in the fixed order
  b = 5, 10, 15, 20, 1, 2, 3, 4 × w1 2–15 × w2 2–15). No solver seed comes from its plant's stream.
- **B3 controls.** 40 plants: lengths 611 and 595; bands w2 2–11 and w2 12–15; w1 drawn from 8–15; 10 plants per
  band per length. Plaintext: `01-solver/plaintext.telegram` (held-out books, 27738 excluded), Spanish. Random keys,
  encrypted by `01-solver/transpo.py`. 30 s each. Recovered = `control.shift_acc` ≥ 0.90 (cyclic shift ≤ 40). Band
  pass = ≥ 8 of 10. `dtsolve` got the true plaintext only to report accuracy; it does not steer the search.
- **B4 threshold.** Fixed in `thresholds-B.md` after the controls and before any target run.
- **B5 target.** Bodies T1[0 : 615 − b] (letters only), b in the README's order. All 196 pairs w1 2–15 × w2 2–15
  per body, 30 s each. A body started only if it could finish inside the deadline (122 min from the target start).

Commands (from this folder):
```
python3 -I step_b.py controls 30
python3 -I step_b.py ctable
python3 -I step_b.py target 30 30 -5.10 5,10,15,20,1,2,3,4 --deadline-min 122
python3 -I step_b.py summary -5.10
```
Outputs: `controls-B.jsonl`, `result-B.jsonl` (one line per run: body, b, n, w1, w2, seconds, seed, score, idp,
iters, k1, k2), `summary-B.txt`. Full decryptions: `out/target-B.jsonl` (gitignored); any run can also be
re-decrypted with `dtsolve decrypt` from its keys.

## Controls (B3, 30 s)
| length | band | recovered | verdict | true-text score, all plants | solver score, recovered plants |
|---|---|---|---|---|---|
| 611 | w2 2–11 | 10/10 | pass | −4.2224 to −3.9944 | −4.2224 to −3.9944 |
| 611 | w2 12–15 | 10/10 | pass | −4.2227 to −3.9822 | −4.2227 to −3.9822 |
| 595 | w2 2–11 | 10/10 | pass | −4.1752 to −4.0099 | −4.1752 to −4.0099 |
| 595 | w2 12–15 | 9/10 | pass | −4.2042 to −3.9798 | −4.2042 to −4.0434 |

39 of 40 recovered. The failure: 595 letters, 15 × 15, 10.2% in place, solver score −5.8543. Two recoveries were
not exact (595, 12 × 15: 98.2%; 595, 13 × 14: 98.0%). The slowest recovery came at 22.6 s (595, 12 × 15); most
came within 1 s. No band needed the 90 s rerun.

## Threshold (B4)
**−5.10**, unchanged from `01`. The lowest true-text score among the 40 controls is −4.2227, above −5.10, so the
fallback rule does not apply. Written to `thresholds-B.md` before the first target run.

## Target (B5)
Run 01:08–03:06 EDT (7,082 s), 1,176 runs, all at 30 s (wall 30.0–30.1 s each), 1,176 distinct seeds. Threshold
−5.10. Table from `summary-B.txt`.

| body | b | runs | best | at w1 × w2 | median | worst | above −5.10 |
|---|---|---|---|---|---|---|---|
| T1[0:610] | 5 | 196 | −6.0689 | 13 × 15 | −6.2716 | −6.8252 | 0 |
| T1[0:605] | 10 | 196 | −6.0409 | 15 × 10 | −6.2339 | −6.8606 | 0 |
| T1[0:600] | 15 | 196 | −5.9401 | 15 × 15 | −6.2721 | −6.7507 | 0 |
| T1[0:595] | 20 | 196 | −6.0559 | 3 × 15 | −6.2161 | −6.9180 | 0 |
| T1[0:614] | 1 | 196 | −6.0595 | 14 × 14 | −6.2725 | −6.9177 | 0 |
| T1[0:613] | 2 | 196 | −6.0429 | 15 × 10 | −6.2725 | −6.9222 | 0 |
| T1[0:612] | 3 | 0 | not run | | | | |
| T1[0:611] | 4 | 0 | not run | | | | |

Best per band: w2 2–11, −5.9826 (T1[0:600], 15 × 11); w2 12–15, −5.9401 (T1[0:600], 15 × 15).
Overall best run: T1[0:600], 15 × 15, seed 782042179, score −5.9401, 0.84 below the threshold
(k1 11,7,8,12,0,3,13,9,4,1,2,6,5,10,14; k2 13,9,4,14,12,7,3,6,2,10,11,5,1,8,0).

Facts for the reader, not interpreted here:
- The six best of the 1,176 runs are all T1[0:600] with w1 = 15 (w2 15, 13, 11, 12, 14, 7). 600 = 15 × 40, so
  K1's rectangle is complete for that body.
- Every target run scores below the one failed control's noise reading (−5.8543, a 15 × 15 plant at 595 letters).
- Recovered controls scored −4.2227 to −3.9822. The gap to the best target run is 1.7 units per letter.

**Left out (budget).** b = 3 and b = 4 (T1[0:612], T1[0:611]): 392 runs, about 40 minutes at 5 workers. The driver
stopped before them by its deadline. Seeds for them are already fixed in the `"17-B-target-solver"` stream, so
`python3 -I step_b.py target 30 30 -5.10 3,4` runs exactly the pre-drawn jobs. Tier 2 bodies and the joint
T1 + T2 attack were not run (outside this dispatch).

## Candidates
None. No run scored above −5.10.

## Completed by the main thread (2026-10-17)
b = 3 and 4 were run afterwards with the command above (`python3 -I step_b.py target 30 30 -5.10 3,4`), using their
pre-drawn seeds: 392 runs in 2,371 s. Best T1[0:612] −6.043 (12 × 13), T1[0:611] −6.052 (13 × 14). No run passed
−5.10. `summary-B.txt` is regenerated over all 1,568 runs. Every tier-1 body is now covered.

# 17-truncated-bodies — steps A and C, tier 1 (run 2026-10-17)

Plan: `README.md` steps A and C, tier 1 only. Thresholds were fixed in `thresholds-AC.md` before any target ran.
Full tables: `result-A.txt`, `result-C.txt`. Per-run records: `out/a_*.jsonl`, `out/c_*.jsonl` (gitignored).
This file reports numbers. It does not interpret them; the main thread judges.

## Method as run

**Step A: single columnar, forward, incomplete last row.** `step_a.py` imports `15-tail-robustness/colsolve.py`
and calls `colsolve.solve` unchanged: exhaustive for w ≤ 8, annealing for w ≥ 9 (2 restarts × 10,000·w steps,
temperature 30 → 1). The script asserts this schedule at import. Score: Spanish quadgrams, log10 per quadgram
(`01-solver/out/lm_es_4.bin`). Recovery: `control.py`'s `shift_acc` (cyclic shift ≤ 40), pass at ≥ 90% of letters in
place, band pass at ≥ 8/10.
1. **A2 controls.** 10 plants per band (w 5–8, 9–30, 31–45) per length (611, 600, 595, 155). The width was drawn
   uniformly within the band. Plaintext: `plaintext.telegram`, held-out books, 27738 excluded (asserted). The key was
   random, and the cipher was `transpo.col_enc`.
2. **A3 noise ceiling.** Shuffles of T1[0:600] and T2[0:155], widths 5, 8, 12, 20, 30, 45, a fresh shuffle for each
   of three runs per width.
3. **A4 thresholds**, per control length: halfway between the highest noise score for that telegram (over all
   widths) and the lowest true-text score among the recovered plants of the passing bands at that length.
4. **A5 target.** Bodies T1[0 : 615 − b] for b = 5, 10, 15, 20, 1, 2, 3, 4, then T2[0:155], in that order. Every
   width 5–45 whose band passed at the body's control length. Each body takes the nearest control length:
   b = 1–5 → 611, b = 10 and 15 → 600, b = 20 → 595, T2 → 155. This mapping was set in code before the controls
   ran.

**Step C: 4 × 4 turning grille on T2 with a preamble.** `step_c.py` imports `06-grille/grille.py` and calls
`grille.best` over all 1,024 keys in both uses (`grille.dec` standard, `grille.enc` inverse), scored by
`grille.qscore`. The body is T2[a : a + 144], nine blocks of 16.
1. **C2 controls.** 10 plants per offset class a = 5, 10, 15. A plant is a random preamble of a uniform letters,
   then 144 plaintext letters through a random grille key in the standard use (as `06`'s controls), then 16 − a
   plaintext letters in clear. The search sees letters a … a + 143. Pass: ≥ 8/10 exact.
2. **C3 threshold**: halfway between the lowest true-key score and the highest wrong-key score over all 30 plants.
   A wrong key is any key and use whose decryption differs from the planted body.
3. **C4 target**: a = 1–15.

**Seeds.** Plant, shuffle and solver seeds come from separate named streams (`17-A-plant`, `17-A-shuffle`,
`17-A-solver-controls`, `17-A-solver-noise`, `17-A-solver-target`, `17-C-plant`). For every annealing control
(w ≥ 9), `step_a.py` replays colsolve's first restart key from the solver seed. It asserts that this key differs
from the planted key, and that the plant and solver seeds differ. It also checks colsolve's source for the seed
expression it replays. No collision occurred (checked for all 120 controls before the run). The exhaustive
searches (A at w ≤ 8, all of C) take no seed and visit every key, so a seed cannot start them at the plant.

**Compute.** 3 worker processes; step B ran dtsolve on the other cores throughout. A2 took 20 min, A3 5 min, C a
few seconds, and A5 56 min (01:31–02:27).

**Choices the README left open** (made before the runs they affect):
- "Passing controls" in A4 means recovered plants in passing bands.
- Body-to-control-length mapping, as above. b = 10 (605 letters) takes the 600 controls, where w 31–45 passed at
  exactly 8/10. At 611 that band failed at 7/10.
- C wrong key: decryption ≠ body, over both uses.

## Controls

### A2 (recovered / 10; all failures scored below their own true text, so they are search failures)
| length | w 5–8 | w 9–30 | w 31–45 |
|---|---|---|---|
| 611 | 10/10 pass | 10/10 pass | 7/10 **fail** |
| 600 | 10/10 pass | 10/10 pass | 8/10 pass |
| 595 | 10/10 pass | 10/10 pass | 10/10 pass |
| 155 | 10/10 pass | 10/10 pass | 2/10 **fail** |

Exact keys: 104/120. At 155 letters, w 31–45 leaves 3–5 letters per column. Its eight failures found
decryptions that score −4.17 to −4.73, against true texts of −3.99 to −4.24.

### C2 (exact / 10)
| a | exact | true-key score | best wrong-key score |
|---|---|---|---|
| 5 | 10/10 pass | −4.327 … −3.914 | −4.321 |
| 10 | 10/10 pass | −4.274 … −3.963 | −4.209 |
| 15 | 10/10 pass | −4.511 … −3.956 | −4.239 |

In every plant the true key ranks first. In 30/30 the best wrong key is the true grille started at another
quarter-turn (rotated by 1, 2 or 3 in 11, 9 and 10 plants). It puts 2–14% of letters in place but keeps each block's
4-letter runs, so it scores −4.21 to −4.89. Across plants the true-key and wrong-key ranges overlap: 4/30 true-key
scores lie below the highest wrong-key score.

## Noise ceiling (A3; best of 3 shuffles per width)
| body | w 5 | w 8 | w 12 | w 20 | w 30 | w 45 |
|---|---|---|---|---|---|---|
| T1[0:600] | −6.636 | −6.492 | −6.285 | −6.022 | −5.754 | **−5.547** |
| T2[0:155] | −6.053 | −5.908 | −5.537 | −5.025 | −4.711 | **−4.414** |

The ceiling rises with width: more columns give the annealer more freedom on letters with no order.

## Threshold
| step | length / class | noise or wrong-key ceiling | lowest true text | threshold |
|---|---|---|---|---|
| A | 611 (b = 1–5) | −5.5469 | −4.3353 | **−4.9411** |
| A | 600 (b = 10, 15) | −5.5469 | −4.2058 | **−4.8764** |
| A | 595 (b = 20) | −5.5469 | −4.2282 | **−4.8876** |
| A | 155 (T2) | −4.4137 | −4.4104 | **−4.4121** |
| C | a = 5, 10, 15 | −4.2090 | −4.5107 | **−4.3598** |

Two thresholds separate little. At 155 the noise ceiling (w 45) meets the worst true text; at the widths run on T2
(5–30) noise reached −4.711. In C the formula as written lands inside the overlap: 1/30 true-key scores (−4.511)
lies below −4.3598. The wrong keys above it are rotated starts of a true key, which only a real grille text has.

## Target

### A5: best per body
| body | widths run | threshold | best score | at w | margin | best key (rank list) |
|---|---|---|---|---|---|---|
| T1[0:610] (b 5) | 5–30 (26) | −4.9411 | −5.8242 | 29 | −0.8831 | 14,16,5,10,4,12,11,13,28,17,7,24,27,23,3,1,25,26,18,2,19,21,22,15,6,0,20,9,8 |
| T1[0:605] (b 10) | 5–45 (41) | −4.8764 | −5.5055 | 45 | −0.6291 | 12,33,10,22,6,14,3,39,2,7,21,28,34,30,44,4,41,42,43,8,25,29,15,9,1,5,24,31,32,17,35,11,40,18,20,37,26,16,36,13,0,23,27,19,38 |
| T1[0:600] (b 15) | 5–45 (41) | −4.8764 | −5.5241 | 45 | −0.6477 | 10,6,34,3,21,32,27,38,11,41,2,39,22,33,30,42,17,25,12,40,24,43,31,20,4,18,26,16,8,0,19,28,1,14,44,36,29,13,23,35,5,7,9,37,15 |
| T1[0:595] (b 20) | 5–45 (41) | −4.8876 | −5.5040 | 45 | −0.6164 | 24,1,21,37,18,43,4,35,7,5,28,12,25,20,34,41,26,15,36,16,19,33,23,44,30,3,27,11,13,29,9,40,39,10,32,17,42,14,8,31,2,38,6,22,0 |
| T1[0:614] (b 1) | 5–30 (26) | −4.9411 | −5.8581 | 28 | −0.9170 | 9,4,25,10,24,20,21,23,22,13,5,0,19,14,18,17,15,2,12,1,27,7,16,6,11,3,8,26 |
| T1[0:613] (b 2) | 5–30 (26) | −4.9411 | −5.8554 | 29 | −0.9143 | 15,26,21,28,1,25,24,27,17,7,20,9,8,23,13,3,6,22,0,19,18,2,14,16,5,10,4,12,11 |
| T1[0:612] (b 3) | 5–30 (26) | −4.9411 | −5.8338 | 29 | −0.8927 | 7,23,0,28,17,9,26,6,4,14,8,2,19,18,13,25,24,21,22,1,12,15,20,10,5,16,3,27,11 |
| T1[0:611] (b 4) | 5–30 (26) | −4.9411 | −5.8441 | 29 | −0.9030 | 10,26,2,19,18,1,12,15,28,0,11,13,25,27,17,7,20,9,8,14,21,22,4,6,5,16,3,23,24 |
| T2[0:155] (T2 b 5) | 5–30 (26) | −4.4121 | −4.7896 | 26 | −0.3775 | 21,8,17,18,22,15,20,14,13,9,6,5,24,2,3,12,16,4,0,1,19,25,10,11,23,7 |

### A5: best score per body and width (keys for every cell in `result-A.txt`)
| w | b 5 | b 10 | b 15 | b 20 | b 1 | b 2 | b 3 | b 4 | T2 b 5 |
|---|---|---|---|---|---|---|---|---|---|
| 5 | −6.797 | −6.605 | −6.715 | −6.598 | −6.698 | −6.746 | −6.757 | −6.772 | −6.277 |
| 6 | −6.610 | −6.554 | −6.636 | −6.494 | −6.672 | −6.631 | −6.604 | −6.604 | −6.176 |
| 7 | −6.570 | −6.514 | −6.538 | −6.458 | −6.485 | −6.482 | −6.492 | −6.564 | −6.139 |
| 8 | −6.547 | −6.395 | −6.472 | −6.394 | −6.497 | −6.489 | −6.459 | −6.459 | −6.087 |
| 9 | −6.531 | −6.457 | −6.476 | −6.378 | −6.532 | −6.583 | −6.520 | −6.514 | −5.896 |
| 10 | −6.550 | −6.413 | −6.524 | −6.425 | −6.464 | −6.468 | −6.482 | −6.498 | −5.800 |
| 11 | −6.423 | −6.361 | −6.416 | −6.347 | −6.380 | −6.376 | −6.403 | −6.410 | −5.695 |
| 12 | −6.333 | −6.299 | −6.272 | −6.277 | −6.361 | −6.327 | −6.316 | −6.321 | −5.535 |
| 13 | −6.324 | −6.261 | −6.320 | −6.287 | −6.330 | −6.304 | −6.306 | −6.285 | −5.566 |
| 14 | −6.286 | −6.163 | −6.209 | −6.234 | −6.248 | −6.260 | −6.269 | −6.250 | −5.579 |
| 15 | −6.251 | −6.142 | −6.249 | −6.192 | −6.222 | −6.214 | −6.231 | −6.253 | −5.429 |
| 16 | −6.228 | −6.193 | −6.173 | −6.140 | −6.158 | −6.165 | −6.208 | −6.190 | −5.328 |
| 17 | −6.174 | −6.159 | −6.144 | −6.165 | −6.198 | −6.218 | −6.245 | −6.204 | −5.332 |
| 18 | −6.159 | −6.125 | −6.093 | −6.062 | −6.161 | −6.145 | −6.131 | −6.160 | −5.337 |
| 19 | −6.141 | −6.029 | −6.102 | −6.050 | −6.117 | −6.123 | −6.115 | −6.115 | −5.173 |
| 20 | −6.092 | −6.091 | −6.136 | −6.064 | −6.094 | −6.065 | −6.093 | −6.106 | −5.240 |
| 21 | −6.062 | −5.996 | −6.038 | −5.971 | −6.099 | −6.058 | −6.059 | −6.048 | −4.997 |
| 22 | −5.997 | −5.989 | −5.972 | −6.026 | −6.062 | −6.012 | −6.026 | −6.041 | −5.068 |
| 23 | −5.981 | −5.951 | −5.993 | −5.953 | −5.987 | −5.993 | −6.055 | −5.928 | −4.993 |
| 24 | −5.945 | −5.942 | −5.958 | −5.923 | −6.096 | −6.038 | −5.942 | −5.958 | −4.939 |
| 25 | −5.983 | −5.954 | −5.974 | −5.919 | −6.009 | −5.985 | −5.990 | −5.995 | −4.881 |
| 26 | −5.990 | −5.849 | −5.898 | −5.874 | −5.967 | −6.031 | −5.961 | −5.992 | −4.790 |
| 27 | −5.934 | −5.878 | −5.864 | −5.870 | −5.953 | −6.004 | −5.978 | −6.017 | −4.851 |
| 28 | −5.897 | −5.876 | −5.952 | −5.926 | −5.858 | −5.890 | −5.917 | −5.931 | −4.829 |
| 29 | −5.824 | −5.854 | −5.820 | −5.846 | −5.869 | −5.855 | −5.834 | −5.844 | −4.841 |
| 30 | −5.835 | −5.792 | −5.931 | −5.776 | −5.935 | −5.884 | −5.837 | −5.889 | −4.809 |
| 31 | — | −5.835 | −5.782 | −5.803 | — | — | — | — | — |
| 32 | — | −5.771 | −5.825 | −5.835 | — | — | — | — | — |
| 33 | — | −5.736 | −5.699 | −5.681 | — | — | — | — | — |
| 34 | — | −5.761 | −5.732 | −5.741 | — | — | — | — | — |
| 35 | — | −5.693 | −5.646 | −5.644 | — | — | — | — | — |
| 36 | — | −5.716 | −5.688 | −5.699 | — | — | — | — | — |
| 37 | — | −5.627 | −5.739 | −5.655 | — | — | — | — | — |
| 38 | — | −5.713 | −5.657 | −5.692 | — | — | — | — | — |
| 39 | — | −5.637 | −5.659 | −5.657 | — | — | — | — | — |
| 40 | — | −5.648 | −5.568 | −5.625 | — | — | — | — | — |
| 41 | — | −5.635 | −5.632 | −5.623 | — | — | — | — | — |
| 42 | — | −5.580 | −5.589 | −5.588 | — | — | — | — | — |
| 43 | — | −5.580 | −5.625 | −5.547 | — | — | — | — | — |
| 44 | — | −5.576 | −5.541 | −5.515 | — | — | — | — | — |
| 45 | — | −5.505 | −5.524 | −5.504 | — | — | — | — | — |

### C4: best key per offset (both uses)
| a | body | best score | use | key | second | median |
|---|---|---|---|---|---|---|
| 1 | T2[1:145] | −6.2391 | standard | `((2, 2, 2, 0), True, False)` | −6.2445 | −6.7691 |
| 2 | T2[2:146] | −6.1786 | inverse | `((1, 1, 0, 1), False, True)` | −6.2208 | −6.8461 |
| 3 | T2[3:147] | −6.1724 | inverse | `((3, 2, 3, 3), False, True)` | −6.2525 | −6.7999 |
| 4 | T2[4:148] | −6.3673 | inverse | `((0, 0, 3, 1), False, True)` | −6.3688 | −6.9129 |
| 5 | T2[5:149] | −6.1499 | inverse | `((3, 0, 0, 2), False, True)` | −6.2294 | −6.8653 |
| 6 | T2[6:150] | −6.1828 | inverse | `((0, 0, 3, 0), False, True)` | −6.1850 | −6.7971 |
| 7 | T2[7:151] | −5.9695 | inverse | `((2, 1, 3, 2), True, True)` | −6.0347 | −6.6678 |
| 8 | T2[8:152] | −6.0584 | standard | `((3, 2, 2, 0), True, False)` | −6.0604 | −6.7346 |
| 9 | T2[9:153] | −5.8909 | inverse | `((3, 1, 3, 2), True, True)` | −5.8977 | −6.6745 |
| 10 | T2[10:154] | −5.8641 | inverse | `((1, 2, 2, 0), True, True)` | −5.9699 | −6.6670 |
| 11 | T2[11:155] | −5.8921 | standard | `((3, 3, 3, 1), True, True)` | −5.9752 | −6.7109 |
| 12 | T2[12:156] | −6.1009 | inverse | `((2, 3, 2, 2), True, True)` | −6.1069 | −6.7697 |
| 13 | T2[13:157] | −6.1063 | standard | `((3, 2, 1, 3), True, True)` | −6.1719 | −6.7692 |
| 14 | T2[14:158] | −5.9458 | inverse | `((2, 2, 3, 0), False, True)` | −6.0518 | −6.7356 |
| 15 | T2[15:159] | −6.1139 | inverse | `((2, 2, 0, 0), True, False)` | −6.1519 | −6.7136 |

Best over all offsets: −5.8641 at a = 10, threshold −4.3598, margin −1.5043. The C2 true keys scored −4.511 to
−3.914.

### Comparison with the noise ceiling at the A3 widths (same solver, same body length)
| body | w 5 | w 8 | w 12 | w 20 | w 30 | w 45 |
|---|---|---|---|---|---|---|
| T1[0:600], target | −6.715 | −6.472 | −6.272 | −6.136 | −5.931 | −5.524 |
| T1[0:600], best shuffle | −6.636 | −6.492 | −6.285 | −6.022 | −5.754 | −5.547 |
| T2[0:155], target | −6.277 | −6.087 | −5.535 | −5.240 | −4.809 | not run |
| T2[0:155], best shuffle | −6.053 | −5.908 | −5.537 | −5.025 | −4.711 | −4.414 |

## Candidates
None. No target score in step A or step C passed its threshold, so no decryption was recorded or read.

## Left out, and why
- **Not testable by the A2 pass rule, so not run:** w 31–45 on b = 1–5 (611 controls 7/10) and on T2[0:155]
  (155 controls 2/10). These cells are open, not excluded.
- **Tier 2:** not run (every other (a, b) with a, b ∈ {0, 5, 10, 15, 20}, and the joint T1 + T2 double columnar).
- **Step C plants used the standard use only**, as `06`'s controls did. The search covered both uses. No inverse-use
  plant was run.
- Every tier-1 body in steps A and C ran. Nothing was cut for budget.

## Run
From this folder, 2026-10-17 (wall times with step B's dtsolve on the other cores):
```
python3 -I step_a.py controls 3                  # A2, 120 plants, 20 min
python3 -I step_a.py noise 3                     # A3, 36 runs, 5 min
python3 -I step_a.py thresholds                  # A4 lines, copied into thresholds-AC.md
python3 -I step_c.py controls                    # C2 + C3, 4 s
                                                 # thresholds-AC.md written here, before any target
python3 -I step_c.py target                      # C4, 4 s
python3 -I step_a.py target 3                    # A5, 279 runs, 56 min
python3 -I step_a.py summary > result-A.txt
python3 -I step_c.py summary > result-C.txt
```


# Thresholds for steps A and C, fixed before any target run

Written 2026-10-17, about 01:30, after the A2 controls, the A3 noise runs and the C2 controls, and before any
target body went through either solver. Steps A4 and C3 of `README.md` give the rule. The numbers come from
`out/a_controls.jsonl`, `out/a_noise.jsonl` and `out/c_controls.jsonl`, printed by `python3 -I step_a.py
thresholds` and `python3 -I step_c.py controls`. `step_a.py target` and `step_c.py target` refuse to run unless the
`THRESHOLD-` lines below are in this file, character for character.

## Step A (single columnar, `colsolve.py` unchanged)

### A2 controls: recovery (plants with ≥ 90% of letters in place, cyclic shift ≤ 40)
| length | w 5–8 | w 9–30 | w 31–45 |
|---|---|---|---|
| 611 | 10/10 pass | 10/10 pass | 7/10 **fail** (not testable) |
| 600 | 10/10 pass | 10/10 pass | 8/10 pass |
| 595 | 10/10 pass | 10/10 pass | 10/10 pass |
| 155 | 10/10 pass | 10/10 pass | 2/10 **fail** (not testable) |

All 13 failed controls scored below their own true text (`result-A.txt`), so they are search failures.

### A3 noise ceiling: best score on shuffles of the body (3 shuffles per width)
| body | w 5 | w 8 | w 12 | w 20 | w 30 | w 45 |
|---|---|---|---|---|---|---|
| T1[0:600] | −6.636 | −6.492 | −6.285 | −6.022 | −5.754 | **−5.547** |
| T2[0:155] | −6.053 | −5.908 | −5.537 | −5.025 | −4.711 | **−4.414** |

(Each cell is the highest of its three shuffles.)

### A4 thresholds
Halfway between the highest noise score for that telegram (all widths) and the lowest true-text score among the
recovered controls of the passing bands at that length.

| control length | noise ceiling | lowest true text (passing) | threshold |
|---|---|---|---|
| 611 | −5.5469 | −4.3353 | −4.9411 |
| 600 | −5.5469 | −4.2058 | −4.8764 |
| 595 | −5.5469 | −4.2282 | −4.8876 |
| 155 | −4.4137 | −4.4104 | −4.4121 |

```
THRESHOLD-A L=611: -4.9411
THRESHOLD-A L=600: -4.8764
THRESHOLD-A L=595: -4.8876
THRESHOLD-A L=155: -4.4121
```

**Body to control length** (set in `step_a.py` before the controls ran: nearest control length):
T1[0:614], [0:613], [0:612], [0:611], [0:610] (b = 1–5) → 611; T1[0:605] (b = 10) and T1[0:600] (b = 15) → 600;
T1[0:595] (b = 20) → 595; T2[0:155] → 155.

**Widths run on the target**, by the A2 pass rule: b = 1–5 and T2, w 5–30; b = 10, 15, 20, w 5–45.

**Notes.**
- At 155 letters the noise ceiling (−4.414, at w 45) almost meets the worst true text (−4.410). The T2 threshold
  therefore separates almost nothing at w 45. At the widths run on T2 (5–30) the noise reached −4.711 at most.
- b = 10 (605 letters) takes the 600 controls, where w 31–45 passed at 8/10, the minimum. At 611 that band failed at
  7/10. Its w 31–45 target runs sit at the edge of what the controls support.

## Step C (4 × 4 grille, `06-grille/grille.py` code path)

### C2 controls (standard use, preamble of a random letters, search over 1,024 keys × 2 uses)
| a | exact | true-key score | best wrong-key score |
|---|---|---|---|
| 5 | 10/10 pass | −4.327 … −3.914 | −4.321 |
| 10 | 10/10 pass | −4.274 … −3.963 | −4.209 |
| 15 | 10/10 pass | −4.511 … −3.956 | −4.239 |

"Wrong key" = any key and use whose decryption differs from the planted body.

### C3 threshold
Halfway between the lowest true-key score (−4.5107) and the highest wrong-key score (−4.2090):

```
THRESHOLD-C: -4.3598
```

**The two ranges overlap, which the README did not expect.** Within every plant the true key ranks first. But in
30/30 plants the best wrong key is the true grille started at another quarter-turn (rotated by 1, 2 or 3: 11, 9 and
10 plants). It puts only 2–14% of letters in place. It keeps each block's four 4-letter runs, though, so it scores
−4.21 to −4.89. Such a variant exists only when the body is a real grille text. So a target above −4.3598 would be
a reading or a rotated start of one. The cost: 1 of 30 true-key scores (−4.511) lies below the threshold, so a
reading as weak as that one would be missed. The formula is applied as written; the main thread judges.
For scale (not a control): `06` found −6.30 as the best of all keys on the full 160 letters of T2.

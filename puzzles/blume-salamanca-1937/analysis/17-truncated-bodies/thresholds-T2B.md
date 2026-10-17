# Tier 2, step B: thresholds and budgets, fixed before any tier-2 target run

Generated 2026-10-17 10:12 EDT by `python3 -I step_t2.py thresholds-b` from `controls-T2B.jsonl`. Rule (README steps B3, B4): a band passes at ≥ 8/10 plants with ≥ 90% of letters in place; a band that fails at 30 s is rerun at 90 s (same plants, same solver seeds) and, if it passes, its target runs use 90 s; a band that fails at 90 s is not testable (`skip`). Threshold −5.10 unless a control's true text scores at or below −5.10 at that length; then halfway between the lowest true text and −5.19. `step_t2.py target-b` refuses to run unless every check line below is in this file.

| length | band | 30 s | 90 s | budget | lowest true text (all plants at L) | threshold |
|---|---|---|---|---|---|---|
| 610 | w2 2-11 | 10/10 pass | not run | 30 | −4.2290 | −5.1000 |
| 610 | w2 12-15 | 9/10 pass | not run | 30 | −4.2290 | −5.1000 |
| 605 | w2 2-11 | 10/10 pass | not run | 30 | −4.1995 | −5.1000 |
| 605 | w2 12-15 | 9/10 pass | not run | 30 | −4.1995 | −5.1000 |
| 600 | w2 2-11 | 10/10 pass | not run | 30 | −4.2145 | −5.1000 |
| 600 | w2 12-15 | 10/10 pass | not run | 30 | −4.2145 | −5.1000 |
| 595 | w2 2-11 | 10/10 pass | not run | 30 | −4.2320 | −5.1000 |
| 595 | w2 12-15 | 9/10 pass | not run | 30 | −4.2320 | −5.1000 |
| 590 | w2 2-11 | 10/10 pass | not run | 30 | −4.3195 | −5.1000 |
| 590 | w2 12-15 | 10/10 pass | not run | 30 | −4.3195 | −5.1000 |
| 585 | w2 2-11 | 10/10 pass | not run | 30 | −4.2095 | −5.1000 |
| 585 | w2 12-15 | 10/10 pass | not run | 30 | −4.2095 | −5.1000 |
| 580 | w2 2-11 | 10/10 pass | not run | 30 | −4.5290 | −5.1000 |
| 580 | w2 12-15 | 9/10 pass | not run | 30 | −4.5290 | −5.1000 |
| 575 | w2 2-11 | 10/10 pass | not run | 30 | −4.2269 | −5.1000 |
| 575 | w2 12-15 | 7/10 **fail** | 9/10 pass | 90 | −4.2269 | −5.1000 |

Check lines:
```
BUDGET-B L=610 w2 2-11: 30 (30 s 10/10 pass)
BUDGET-B L=610 w2 12-15: 30 (30 s 9/10 pass)
THRESHOLD-B L=610: -5.1000
BUDGET-B L=605 w2 2-11: 30 (30 s 10/10 pass)
BUDGET-B L=605 w2 12-15: 30 (30 s 9/10 pass)
THRESHOLD-B L=605: -5.1000
BUDGET-B L=600 w2 2-11: 30 (30 s 10/10 pass)
BUDGET-B L=600 w2 12-15: 30 (30 s 10/10 pass)
THRESHOLD-B L=600: -5.1000
BUDGET-B L=595 w2 2-11: 30 (30 s 10/10 pass)
BUDGET-B L=595 w2 12-15: 30 (30 s 9/10 pass)
THRESHOLD-B L=595: -5.1000
BUDGET-B L=590 w2 2-11: 30 (30 s 10/10 pass)
BUDGET-B L=590 w2 12-15: 30 (30 s 10/10 pass)
THRESHOLD-B L=590: -5.1000
BUDGET-B L=585 w2 2-11: 30 (30 s 10/10 pass)
BUDGET-B L=585 w2 12-15: 30 (30 s 10/10 pass)
THRESHOLD-B L=585: -5.1000
BUDGET-B L=580 w2 2-11: 30 (30 s 10/10 pass)
BUDGET-B L=580 w2 12-15: 30 (30 s 9/10 pass)
THRESHOLD-B L=580: -5.1000
BUDGET-B L=575 w2 2-11: 30 (30 s 10/10 pass)
BUDGET-B L=575 w2 12-15: 90 (30 s 7/10 FAIL; 90 s 9/10 pass)
THRESHOLD-B L=575: -5.1000
```

# Tier 2, joint attack: verdicts and thresholds, fixed before any joint target run

Generated 2026-10-17 09:03 EDT by `python3 -I step_t2.py thresholds-j` from `controls-T2J.jsonl`. Plants: T1-length plaintext plus 155 letters under the same keys, w1 8–15, w2 16–17, 180 s, 10 per length. Pass: ≥ 8/10 with ≥ 90% of the T1-length letters in place. A failing length is not testable and its target is not run. Threshold −5.10 (joint per-letter score, as `03`'s H2) unless a control's joint true text scores at or below −5.10; then halfway between the lowest true text and −5.19. `step_t2.py target-j` refuses to run unless every check line below is in this file.

| joint length | recovered | verdict | lowest true text | threshold |
|---|---|---|---|---|
| 615 + 155 | 9/10 | pass | −4.1507 | −5.1000 |
| 610 + 155 | 7/10 | **fail** (not testable) | −4.1444 | −5.1000 |
| 605 + 155 | 5/10 | **fail** (not testable) | −4.4451 | −5.1000 |
| 600 + 155 | 6/10 | **fail** (not testable) | −4.1897 | −5.1000 |
| 595 + 155 | 6/10 | **fail** (not testable) | −4.1733 | −5.1000 |

Check lines:
```
JOINT L=615+155: 9/10 pass
THRESHOLD-J L=615+155: -5.1000
JOINT L=610+155: 7/10 FAIL (not testable)
THRESHOLD-J L=610+155: -5.1000
JOINT L=605+155: 5/10 FAIL (not testable)
THRESHOLD-J L=605+155: -5.1000
JOINT L=600+155: 6/10 FAIL (not testable)
THRESHOLD-J L=600+155: -5.1000
JOINT L=595+155: 6/10 FAIL (not testable)
THRESHOLD-J L=595+155: -5.1000
```

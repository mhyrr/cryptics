# Step B threshold and budget, fixed after the B3 controls and before any target run

Written 2026-10-17, 01:08 EDT. No Step B target run had started. The rule is README.md, Step B, items 3 and 4.

## The controls it rests on (B3)
`step_b.py controls 30`; log `controls-B.jsonl` (40 plants). CC, Spanish model, 30 s per plant, 5 workers.
Plants: telegraph Spanish from `01-solver/plaintext.py` (book 27738 excluded), random keys, w1 drawn from 8–15.
Solver seeds come from a stream separate from the plant stream. A plant counts as recovered at ≥ 90% of letters in
place, with `control.py`'s `shift_acc` (cyclic shift up to 40).

| length | band | recovered | verdict | true-text score, all plants | solver score, recovered plants |
|---|---|---|---|---|---|
| 611 | w2 2–11 | 10/10 | pass | −4.2224 to −3.9944 | −4.2224 to −3.9944 |
| 611 | w2 12–15 | 10/10 | pass | −4.2227 to −3.9822 | −4.2227 to −3.9822 |
| 595 | w2 2–11 | 10/10 | pass | −4.1752 to −4.0099 | −4.1752 to −4.0099 |
| 595 | w2 12–15 | 9/10 | pass | −4.2042 to −3.9798 | −4.2042 to −4.0434 |

The one failure: 595 letters, 15 × 15, 10.2% in place, solver score −5.8543 (true text −4.1256).

## Budget
Every band passed at 30 s at both lengths. So no 90 s rerun, and every target run uses **30 s**.

## Threshold
The lowest true-text score among the 40 controls (passing or not) is **−4.2227**. That is above −5.10, so the
fallback rule does not apply. **Threshold: −5.10.** A target run with a per-letter score above −5.10 is a candidate
and goes to the dive README's criteria. A run at or below −5.10 is noise.

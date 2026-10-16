# 03-target-h1 — forward double columnar, telegram 1, the frozen region

**Question (H1).** Is telegram 1 a forward double columnar transposition (CC) of Spanish with w1 2–15 and
w2 12–15, the region where the `01-solver` controls pass?

**Frozen before the run** (`01-solver/README.md`, commit 3379632): region w1 2–15 × w2 12–15, CC, Spanish model,
180 s per (w1, w2) pair, one seed (1000), candidate threshold −5.10. Controls in the region: 30 of 30 recovered.

**Run.** `python3 target.py h1_cc CC es 180 8 2-15 12-15 1` (56 runs, ~21 min on 8 cores, 2026-10-16).
Log with every best decryption and key: `h1_cc.jsonl`. Summary: `python3 summarize_target.py h1_cc.jsonl`
→ `summary_h1_cc.txt`. `verify.py` is the independent re-decrypt (pure Python), for any candidate.

**Result.** No candidate. Best −6.004 (15 × 15), median −6.156, worst −6.456. The planted controls in the same
region scored −4.89 to −3.98 when recovered, and none failed.

**Conclusion.** Forward double columnar transposition with w1 2–15 and w2 12–15 is excluded for telegram 1 with a
Spanish plaintext, at a control recovery rate of 30/30 (one-sided 95% lower bound on the rate: 90%). With
Bourdeau's exhaustive w2 ≤ 11, forward double columnar is now excluded for w2 ≤ 15 whenever w1 ≤ 15.
Still open: w2 ≥ 16 (not testable with this method at 615 letters), w1 ≥ 16 with w2 12–15 (the K1 stage is
unreliable there in 180 s), the CR convention with w2 ≥ 11, and non-Spanish plaintexts unless the H3 control
shows the Spanish model reads them.

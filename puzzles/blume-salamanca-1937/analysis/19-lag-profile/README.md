# 19-lag-profile — does T1 carry letter-pair association at some lag, and does K1 give it?

**Why.** `18`'s solver scores T1 above all 20 of its own shuffles at n = 20 and 30 (excess +0.106 at n = 20),
while long-key double columnar plants (K1) exceed their own shuffles by a median of +0.013; T1 is above all 20 of
them (p ≈ 0.05, post hoc; `18`, second post hoc check). The solver gains from Spanish-like letter pairs between
cipher columns, that is, at lags 1 … n − 1. This experiment measures that directly, without a solver, and with
200 K1 plants instead of 20. `14` tested vowel/consonant class at lags 1–40 (nothing); full letter pairs are new.

## Plan (written 2026-10-17, before any run; committed before the run)
**Statistic.** For a text x and lag d, G(d) = mean over i of PMI(x_i, x_{i+d}), where PMI(a, b) =
log10 P(ab) − log10 P(a) − log10 P(b) from the Spanish bigram table (`01-solver/out/lm_es_2.bin`; P(a) from its
row sums). z(d) = (G(d) − mean over the text's own shuffles) / SD over those shuffles.
- **(a) Single lag.** M = max over d of z(d), d = 1–100 for T1 and 1–50 for T2. Family-wise p = share of the
  text's own shuffles whose M (computed the same way, against the other shuffles) is at least the text's M.
- **(b) Multi-lag sums.** S(D) = sum of z(d) for d = 1 … D − 1, D = 20 and 30 (the lags `18`'s solver uses at
  n = 20 and 30). p against own shuffles, and the text's S(D) against the K1 plants' S(D), each plant scored
  against its own shuffles.

**Nulls.** 2,000 shuffles of T1 and of T2 ("19-shuffle"). 200 K1 plants: forward CC, w1 and w2 uniform 16–25,
615 letters of held-out Spanish telegraph text ("19-plant"), each with 200 shuffles of its own letters.

**Reading, fixed now.**
1. (a) family-wise p < 0.01 for T1 or T2: name the lag(s) as a lead on key geometry in `NEXT.md`, with the share
   of K1 plants that reach the same M.
2. (b) T1's S(20) or S(30) above the 99th percentile of the K1 plants' values: `18`'s excess is confirmed as a lead
   against K1 as a whole-text system (still post hoc in origin). Between the 95th and 99th: suggestive, as `18`
   found. Below the 95th: `18`'s check 2 was chance, recorded.
3. Nothing here is a decryption or an exclusion.

Run: `python3 -I lagprof.py > result.txt`

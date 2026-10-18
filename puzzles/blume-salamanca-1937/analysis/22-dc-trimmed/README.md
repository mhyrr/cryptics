# 22-dc-trimmed — forward double columnar w2 16–17 on trimmed T1 bodies

**Status: pre-registered 2026-10-17 23:17 EDT, before any control or target run in this folder.** The plan below is
not edited after the runs start; results go under "Result".

## Question
`21` excluded forward double columnar (CC) on T1 **at full length** for w1 2–15 × w2 16–17, with Lasry's
full-neighbourhood K2 climb at 50 M IDP evaluations per length pair (controls 20/20; T1 best −6.00 against −5.10).
`15` showed that any full-length columnar exclusion is void if 5–20 letters at an end are not transposed (double
columnar 10/10 → 0/10 at every tail and head trim). `17` covered trimmed bodies only for w2 ≤ 15. Does T1 read under
forward CC at w1 2–15 × w2 16–17 once a suspected untransposed end is cut off?

## Bodies
- **T1[0:595]**, 595 letters: the last 20 letters cut. They are rare-letter rich (`09`, H6), and T1's final group
  begins REF.
- **T1[5:615]**, 610 letters, and **T1[10:615]**, 605 letters: the first 5 or 10 letters cut, for an indicator at the
  head (Givierge, `canon.md`; H6).

T1 is `sources/telegram-1.txt`, letters only, upper case, 615 letters, SHA-256 beginning `e266615d` (as in
`target21.py`).

## Method
Exactly `21`'s target method: `21-dc-method/out/dcm solve CT w1=.. w2=.. lang=es seed=S budget=50000000 climb=1
idp=1 k1climb=0`, `01`'s K1 stage and refinement, Spanish model (`21-dc-method/out/lm_es_{2,4}.bin`, copies of `01`'s
tables). The binary is the one `21`'s controls A and A2 and its target used: `run22.py` refuses to run unless
`21-dc-method/out/dcm` matches the SHA-256 in `21-dc-method/dcm_ctlA.sha256` (`97863d12…`; source
`21-dc-method/dcm_ctlA.c`). `dcm` reads its tables relative to its working directory, so it runs with
`21-dc-method/` as working directory; it reads there and writes nothing. Nothing in `21-dc-method/` or any other
existing folder is modified. `run22.py` imports `21-dc-method/run21.py` for the plant generator (`plant`), the
seed stream (`stream`), the plaintext loader (`load_words`) and `01`'s accuracy rule (`shift_acc`).

## Pre-registration

### Controls, at each body length (595, 610, 605)
- **Plants:** 10 per length, Spanish telegraph-style held-out text (`01-solver/plaintext.py`, through `run21.plant`,
  as `run21.py` builds them), forward CC with random keys, Spanish model.
- **Lengths drawn from w1 2–15 × w2 16–17, stratified:** trials 0–5 draw (w1, w2) uniformly from w1 2–15 × w2 16–17;
  trials 6–9 draw uniformly from the hard corner w1 12–15 × w2 17. So at least 4 of 10 fall in the corner (`21`'s A2:
  13 × 17 needed up to 23.7 M evaluations).
- **Run and seed rules:** the same binary and the same arguments (`budget=50000000 climb=1 idp=1 k1climb=0`), one run
  per plant, the whole budget spent (no stop at a hit). Plant keys, lengths and plaintext offsets from the stream
  `plant|ctl22_N|i`; solver seeds from `solver|ctl22_N|i` (N the body length, i the trial; SHA-256, string-keyed,
  new tags). The planted K2 is passed to the solver (`truek2=`) only for the abort check (the solver exits if a random
  K2 start equals the planted K2) and for reporting `hit_at`; it does not steer the search. An abort (chance about
  1/16! per random start, about 10^-8 over a whole run) counts as a trial not recovered; it is not rerun.
- **Pass rule (`01`'s):** a plant counts as recovered if the final decryption matches the plaintext in ≥ 95% of
  positions, allowing a cyclic shift of up to 40 (`run21.shift_acc`). A length passes at ≥ 8 of 10. **A length that
  fails is "not testable" at this budget, and its target body is not run.**
- Recorded per plant: lengths, planted keys, final score, accuracy, the first improvement reading ≥ 95% (in IDP
  evaluations), whether the K2 stage reached the true K2's IDP, CPU and wall seconds.

### Threshold, per length
−5.10 (`01`'s candidate threshold, used by `03`, `17`, `21`), **unless a recovered control at that length scores at or
below −5.10**. In that case the threshold is halfway between the lowest recovered control score at that length and
−5.19 (`01`'s highest noise failure). Computed by `run22.py` from the control records before any target run, and
written into "Result" with the controls.

### Target
- For each body whose length passed: all 28 pairs, w1 2–15 × w2 16–17, one run per pair, the same binary and
  arguments, the whole budget spent.
- Seeds from `solver|target22|BODY|w1xw2`, BODY one of `T1[0:595]`, `T1[5:615]`, `T1[10:615]`.
- Before running, `run22.py` checks the binary's hash and T1's hash (615 letters, SHA-256 beginning `e266615d`), and
  that the controls for the body's length are complete and passed.

### Candidate rule
A target run whose final per-letter score is **above its length's threshold** is a candidate. A candidate goes to the
dive's criteria (whole text reads; T2 under the same system; independent re-decrypt) on the main thread. This
experiment does not chase it beyond printing its first 200 letters.

### What a result means
- **No candidate at a passing length:** forward CC at w1 2–15 × w2 16–17 is excluded on that body, for Spanish, at
  this budget.
- **A length that fails its controls:** that body is not testable at w2 16–17 at 50 M evaluations; the full-length
  exclusion (`21`) is not extended to it.
- Not covered whatever happens: other trims (other a, b; `17` tier 2 ran a, b ∈ {0, 5, 10, 15, 20} only for
  w2 ≤ 15), w2 ≥ 18, w1 ≥ 16, CR and other conventions, and languages other than Spanish at w2 16–17.

### Cost and scheduling
From `21` (controls and target, 615 letters): 70–1,900 CPU s per run, about 4.9 CPU h for 28 target pairs. About
30 control runs (≈ 8–10 CPU h with the corner stratification) and up to 84 target runs (≈ 15–17 CPU h). Up to 8
workers; jobs are ordered longest-expected first (by `21`'s measured CPU per pair) to shorten the tail. Order and load
do not change any result: each run is a fixed seed and a fixed evaluation budget.

## How to run
```
python3 -I run22.py controls 8      # -> results/controls22.jsonl (resumes); heavy logs in out/
python3 -I run22.py target 8        # bodies whose length passed -> results/target22.jsonl (resumes)
python3 -I run22.py summary         # -> results/summary.md
```

## Result
Before the controls, a plumbing smoke test ran `run22.py`'s two job functions at 300,000 evaluations on two plants
under the separate tag `smoke22` (output in `/tmp`, discarded). It is not part of the experiment and touched no T1
body.

### Controls (`results/controls22.jsonl`, `results/summary.md`; run 2026-10-17 23:18 – 2026-10-18 01:07 EDT, 8 workers)
All three lengths **pass**. Every recovery read 100% of positions with no shift, and every K2 search that recovered
reached the true K2's IDP.

| length (body) | recovered | recovered scores | slowest first recovery (M evaluations) | CPU h |
|---|---|---|---|---|
| 595 (T1[0:595]) | **10/10** | −4.16 to −4.00 | 15.4 (15 × 16) | 5.2 |
| 610 (T1[5:615]) | **10/10** | −4.33 to −4.02 | 47.9 (15 × 17) | 3.8 |
| 605 (T1[10:615]) | **9/10** | −4.16 to −4.04 | 27.9 (15 × 17) | 3.4 |

- The one failure, 605 trial 6 at 15 × 17, ended at −5.81 with 3 of 17 K2 elements right and no K2 hit: a search
  failure (below its true text), not a selectivity failure.
- **Thresholds:** no recovered control scored at or below −5.10, so the threshold is −5.10 at all three lengths
  (fixed here before any target run).
- **Coverage caveat, observed and not a change to the rule:** the budget margin at w1 15 × w2 17 is thin on these
  bodies. Of three 15 × 17 plants at 605–610 letters, two recovered, at 27.9 M and 47.9 M of the 50 M budget, and one
  did not. In `21`'s A2 at 615 letters, 15 × 17 recovered at 0.6–6.2 M; 615 = 15 × 41 makes the K1 rectangle complete
  there, which `21` (section 2) found adds about one swap of basin. 14 × 17 also needed up to 25.5 M (610). So an
  empty target at 15 × 17 (and to a lesser degree 14 × 17) on the trimmed bodies is a weaker exclusion than at the
  other pairs.
- CPU per run is about 1.5–2 times `21`'s for the same pair (8 workers on 4 performance and 4 efficiency cores); the
  budget is in evaluations, so the search is unchanged.

### Target (`results/target22.jsonl`, `results/summary.md`; run 2026-10-18 01:07 – 03:57 EDT, 8 workers, 21.4 CPU h)
**No candidate.** All 84 runs spent the full 50 M evaluations. Every pair on every body scored below the −5.10
threshold by at least 0.84, against control recoveries of −4.33 to −4.00 at the same lengths.

| body | pairs | scores | best (pair) | margin | first 60 letters of the best reading |
|---|---|---|---|---|---|
| T1[0:595] | 28/28 | −6.29 to −5.94 | −5.9425 (14 × 17) | −0.843 | `CIOMDGEAMAXORMENAPEOCTEDINESMEDIGASMPARDINSTAPTRELEPRACUCINT` |
| T1[5:615] | 28/28 | −6.23 to −6.00 | −6.0002 (13 × 17) | −0.900 | `PGEMNDEJOTFNDCTCGTTODOPBONQEDIOAULEITPDCOBSTTENCRENOODIENGON` |
| T1[10:615] | 28/28 | −6.23 to −6.01 | −6.0072 (14 × 17) | −0.907 | `POKEONKGUNNICNOENDOTEMTAITDEMPOSAOTDACISMASPIDORNEPITALTEAOF` |

No reading shows Spanish. The bests sit where `21` (−6.00 at full length) and `17` (−5.92, w2 ≤ 15, trimmed bodies)
put T1's noise level.

**Excluded now:** forward double columnar CC, Spanish, w1 2–15 × w2 16–17, at 50 M IDP evaluations per pair, on
T1[0:595], T1[5:615] and T1[10:615], so an untransposed last 20 or first 5 or 10 letters no longer escapes `21`'s
full-length exclusion at w2 16–17 (with `17`, these bodies are now excluded for w1 2–15 × w2 2–17). The exclusion is
weakest at 15 × 17, where 2 of 3 controls at 605–610 letters recovered and those late (27.9 M, 47.9 M of 50 M).
**Not covered:** the other trims (`17` tier 2's other a, b ∈ {0, 5, 10, 15, 20}, and any trim other than 0, 5, 10,
15, 20), w2 ≥ 18 and w1 ≥ 16 (`21`'s wall), CR and other conventions, and languages other than Spanish at w2 16–17.

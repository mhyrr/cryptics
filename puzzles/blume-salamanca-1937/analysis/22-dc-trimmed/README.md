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
(not yet run)

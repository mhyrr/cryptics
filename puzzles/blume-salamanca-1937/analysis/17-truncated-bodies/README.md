# 17-truncated-bodies — stage 4: the families `15` reopened, on bodies with the ends cut off

**Question.** If T1 (and T2) carry a few untransposed letters at an end (H6), do the families that were excluded at
full length read the body? `15` shows that 5–20 untransposed letters at either end drop single columnar recovery
from 39/40 to 0/40 and double columnar from 10/10 to 0/10, and that a preamble breaks the 4 × 4 grille. So those
exclusions are void for bodies shorter than 615 or 160. This experiment runs them on truncated bodies.

**Plan written 2026-10-17, before any control or target run in this folder, and committed before the run.** The
steps below are the pre-registration. Results go under "Result"; the plan is not edited afterwards.

## Bodies
`T1[a : 615 − b]` and `T2[a : 160 − b]`. Ordered by evidence:
- **Tier 1 (run now).** T1 tail trims b ∈ {1, 2, 3, 4, 5, 10, 15, 20}, a = 0. b = 1–4 covers fillers added after
  transposition to complete the last group. b = 5–20 covers whole groups at the end: `09` found T1's last 20 letters
  rare-letter rich, and both final groups begin REF. T2: b = 5 (`REFUD`), a = 0.
- **Tier 2 (only after tier 1, as budget allows; otherwise named in NEXT.md).** Every other (a, b) with a, b ∈
  {0, 5, 10, 15, 20}, and the joint double columnar attack T1[0 : 615 − b] + T2[0 : 155] under shared keys.

## Steps

### Step A — single columnar, forward, incomplete last row (`15-tail-robustness/colsolve.py`, unchanged)
1. Widths 5–45. Exhaustive for w ≤ 8; annealing for w ≥ 9 at colsolve's frozen schedule (2 restarts × 10,000·w
   steps).
2. **Control at the target lengths.** Plants of Spanish telegraph plaintext (`01-solver/plaintext.py`, glossary
   book excluded) at 611, 600 and 595 letters (T1 bodies) and 155 letters (T2 body), single columnar with a random
   key, solver seeded independently of the plant. Bands w 5–8, 9–30, 31–45; 10 plants per band per length, at the
   target's schedule. **Pass rule:** ≥ 80% of a band's plants with ≥ 90% of letters in place. A band that fails is
   "not testable" at that length and its target runs are not read.
3. **Noise ceiling.** The same solver on shuffles of the T1 body (600 letters) and the T2 body (155) at widths 5, 8,
   12, 20, 30, 45, three shuffles each. This gives the scores annealing reaches on letters with no plaintext order.
4. **Threshold, fixed after steps 2–3 and before step 5:** per letter Spanish quadgram score (log10, as colsolve
   reports it) halfway between the highest noise-ceiling score and the lowest true-text score among passing
   controls, per length. Written into this README before step 5.
5. **Target.** Every tier-1 body × every width whose band passed. Record the best score and key per (body, w).
6. **Pass rule for a candidate:** a target score above the step-4 threshold. A candidate goes to the dive README's
   criteria (whole text reads; T2 under the same system; independent re-decrypt). Nothing else counts.

### Step B — double columnar CC (`01-solver/out/dtsolve`, unchanged)
1. Widths w1 2–15 × w2 2–15 (196 pairs). This covers `03`'s region and Bourdeau's w2 ≤ 11 region, both of which
   were searched only at full length.
2. **Budget:** 30 s per (body, w1, w2), one seed per run, seeds drawn independently of any plant.
3. **Control at the target lengths and budget.** Plants at 611 and 595 letters, bands w2 2–11 and w2 12–15 (w1
   drawn from 8–15), 10 plants per band per length, 30 s each. **Pass rule:** ≥ 80% per band. If a band fails at
   30 s, rerun that band's controls at 90 s; if it then passes, that band's target runs use 90 s. A band that fails
   at 90 s is "not testable" and its target runs are not read.
4. **Threshold:** −5.10, the threshold `01` fixed from controls before any target run, unless the step-3 controls
   put a true-text score at or below −5.10. In that case the threshold is set halfway between the lowest true-text
   score and −5.19 (`01`'s highest noise failure), written here before step 5.
5. **Target:** T1 tier-1 bodies with b ∈ {5, 10, 15, 20} first, then b ∈ {1, 2, 3, 4}, across all 196 pairs.
6. **Pass rule for a candidate:** as in step A6.

### Step C — 4 × 4 turning grille on T2 with a preamble (`06-grille/grille.py` code path)
1. Offsets a = 1–15: the body is T2[a : a + 144] (nine blocks of 16). All 1,024 keys, both uses (`06`).
2. **Control:** 10 plants per offset class (a = 5, 10, 15) with a random untransposed preamble, at the same code
   path. Pass rule: ≥ 80% exact.
3. **Threshold:** `06`'s controls scored the true key far above the rest. Fix the threshold halfway between the
   lowest control true-key score and the highest wrong-key score across the controls, before step 4.
4. **Target:** every offset. Pass rule for a candidate: above the threshold, then the dive README's criteria.

### Not run here, and why
- **Letters within sets of n with a preamble, n 5–12.** `14`'s positive controls show that these sets leave
  vowel/consonant contact structure at any alignment (power 0.78–0.98 at 615), and T1 has none (p 0.56, 0.87). So
  an offset does not reopen them for T1.
- **Sets of n ≥ 20 and Nihilist read by rows, any n ≥ 8.** `15` found that `05`'s controls started the solver at the
  planted key. With independent seeds the solver recovers sets of 20 in 1/20 plants and Nihilist rows at n = 8 in
  14/20. These families have no working solver here; that is a wall, not an exclusion.
- **Double columnar with w1 or w2 ≥ 16.** The named wall (`01`): no gradient at this length. A trim does not change
  that.

## Run
Run 2026-10-17 by two agents (steps A + C; step B) and the main thread (B for b = 3, 4; the noise check). Each step
has its own record: `stepAC.md`, `thresholds-AC.md`, `result-A.txt`, `result-C.txt` (`step_a.py`, `step_c.py`);
`stepB.md`, `thresholds-B.md`, `controls-B.jsonl`, `result-B.jsonl`, `summary-B.txt` (`step_b.py`). Thresholds
were written to their files before any target run; the target scripts refuse to run without them. Plant and solver
seeds come from separate streams, and the code asserts that no solver starts at its planted key.
```
python3 -I step_a.py controls|noise|thresholds|target        # step A
python3 -I step_c.py controls|target                         # step C
python3 -I step_b.py controls 30 && python3 -I step_b.py target 30 30 -5.10 5,10,15,20,1,2,3,4
python3 -I noise_600.py > noise_600.txt                      # added after step B (see below)
```

## Result
**No candidate in any step.** Every target score is below its threshold, most by 0.6–0.9 log units per letter.

| step | controls (pass ≥ 8/10) | threshold | target bodies | best target | margin |
|---|---|---|---|---|---|
| A, single columnar, T1 | 611: w 5–30 pass, w 31–45 7/10 fail; 600 and 595: all pass | −4.94 (611), −4.88 (600), −4.89 (595) | b = 1–5 at w 5–30; b = 10, 15, 20 at w 5–45 | −5.50 (b 20, w 45) | −0.62 |
| A, single columnar, T2 | 155: w 5–30 pass, w 31–45 2/10 fail | −4.41 | T2[0:155], w 5–30 | −4.79 (w 26) | −0.38 |
| B, double columnar CC | 611 and 595, w2 2–11 and 12–15: 10/10, 10/10, 10/10, 9/10 at 30 s | −5.10 (lowest control true text −4.22) | T1 b = 1, 2, 3, 4, 5, 10, 15, 20 × w1 2–15 × w2 2–15 | −5.94 (b 15, 15 × 15) | −0.84 |
| C, 4 × 4 grille, T2 with preamble | 30/30 exact | −4.36 by formula (see below) | a = 1–15, all 1,024 keys, both uses | −5.86 (a 10) | −1.50 |

Per-body bests are in `stepAC.md` and `summary-B.txt`. In step A every body tracks the noise ceiling of its width
(for example T1 at w 45: target −5.50 to −5.52, shuffles −5.55), as a body with no columnar order should.

**Judgements by the main thread.**
- **Step C threshold.** The formula overlapped: the best wrong key in every control is the true grille started at
  another quarter-turn (−4.21 to −4.89), so one true key falls below −4.36. The target's best, −5.86, lies about
  one unit below every control score, true or wrong-key. The grille with a preamble is excluded however the
  threshold is drawn.
- **Step B pattern.** The six best runs all fall on T1[0:600] with w1 = 15, a complete first rectangle
  (600 = 15 × 40). `noise_600.py` (reading fixed before it ran): three shuffles of T1[0:600] at 15 × 15 score
  −5.96, −6.01 and −5.99 against the target's −5.94. That is within 0.05, so the pattern is the solver on a
  complete rectangle, not order in the text.

**What is excluded now (bodies with the ends cut off, as listed; controls pass):**
- Single columnar, w 5–30, for T1 with 1–5, 10, 15 or 20 letters cut from the end, and for T2 with 5; w 31–45 for
  T1 with 10, 15 or 20 cut.
- Double columnar CC, w1 2–15 × w2 2–15, for T1 with 1–5, 10, 15 or 20 letters cut from the end.
- 4 × 4 turning grille on T2 after a preamble of 1–15 letters.

**Not covered (open, not excluded):** single columnar w 31–45 at T1 b = 1–5 and on T2 (controls failed); tier 2 (head
trims and two-sided trims); the joint T1 + T2 double columnar attack on truncated bodies; letter-level trims other
than b = 1–5; grille plants in the inverse use (the controls planted the standard use only, as `06` did).

## Tier 2 (run 2026-10-17; setup, controls and thresholds in `stepT2.md`, committed c60d81a before any target run)
`step_t2.py`; results `result-T2A.jsonl`, `result-T2B.jsonl`, `result-T2J.jsonl`; tables `summary-T2.txt`.
**No candidate in any step.**

| step | bodies | runs | best | margin |
|---|---|---|---|---|
| A, single columnar, T1 | T1[a : 615 − b], a 5–20, b 0–20 (20 bodies), passing bands only | 629 | — | every body ≤ −0.46 |
| B, double columnar CC, T1 | the same 20 bodies, w1 2–15 × w2 2–15 (575 w2 12–15 at 90 s) | 3,920 | −5.92 (T1[10:600], 15 × 15) | −0.82 |
| A, single columnar, T2 | T2[a : 160 − b], 23 bodies, passing bands only | 353 | −4.39 (T2[20:145], w 30) | −0.14 |
| joint CC, T1 + T2[0:155] | b = 0 only (other lengths failed joint controls), w1 8–15 × w2 16–17, 180 s | 16 | −6.08 | −0.98 |

**Judgement by the main thread on T2.** The T2 thresholds were set by noise at w 45, a failed band, and sit above
some weak true texts (`stepT2.md`). That does not decide anything here: in every passing (length, band) the target's
best lies below the lowest true-text score of any recovered control at that length (margins −0.16 at 125 letters,
w 9–30, to −1.4 at w 5–8). So the T2 runs exclude however the threshold is drawn, as step C did in tier 1.

**Excluded now (controls pass):**
- Single columnar on T1 with 5–20 letters cut from the head, alone or with 5–20 from the tail (w 5–30; w 31–45 at
  605, 595, 585, 575 letters).
- Double columnar CC w1 2–15 × w2 2–15 on those 20 T1 bodies.
- Single columnar on T2 with 5–20 letters cut at the head, the tail or both: w 5–8 at every length, w 9–30 at 150,
  135, 125 and 120 letters.
- Joint CC w1 8–15 × w2 16–17 on T1 + T2[0:155].

**Not covered:** single columnar w 31–45 at T1 610, 600, 590, 580 and on every T2 body; T2 w 9–30 at 155, 145, 140,
130 letters; joint attack at 610–595 (controls failed). With tier 1, every (a, b) in {0, 5, 10, 15, 20}² is now run
for T1 single and double columnar (w ≤ 15).

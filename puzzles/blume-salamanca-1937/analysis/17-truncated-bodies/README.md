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
Filled in when the steps are run. Scripts live in this folder; each prints its own result file.

## Result
Not yet run.

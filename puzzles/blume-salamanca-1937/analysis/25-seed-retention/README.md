# 25-seed-retention — diagnose phrase seeds and enumerate their neighbours

2026-10-19. Greg said to proceed with the measured shortlist weakness from experiment 24.

## Initial design before implementation

1. Reconstruct the five failed holdout plants from 24. Score all 5,284 seeds at all first widths 12–22 and
   measure the base seed's rank at the true width. Refine that base seed directly as an **assisted diagnostic**,
   never as a blind recovery result. This separates filtering loss from inability to refine a retained seed.
2. Use only those development diagnostics to choose one wider, bounded filter. Preserve the contextual phrase
   list, Spanish model, plaintext length, and refinement budget. Do not use new target results to tune it.
3. Freeze a fresh holdout with at least ten plants each at exact/one-swap/two-swap distance and ten independently
   random off-list keys. Score all strata, including failures, with identical search/stop rules. A near-list
   stratum passes at >=8/10 recoveries under >=95% agreement allowing cyclic shift <=40; also report exact and
   in-place agreement. Off-list tests measure limits; near-list success does not imply arbitrary-key coverage.
4. Only if the changed method improves blind recovery in the previously failing region, freeze the target
   protocol and run full 615-letter T1 plus its own-letter shuffle. Any further preparation/system variant
   needs its own controls. One shuffle is not a p-value. No phrase-list expansion in this experiment.

The hypothesis is still H13. The finite contextual key list is a search assumption, not historical evidence.
The controls still use modified literary text; audit 23's preparation/corpus limits remain.

## Stop rule

One diagnostic batch and one fresh holdout with a predeclared filter. If it cannot recover the lost cases or
fails fresh controls, record the result and the next wall. Do not keep increasing the budget against T1.

## Provenance

- Repository evidence and generators: `../24-phrase-seeded/`, pinned inputs in its build manifest.
- C IDP/transposition/refinement implementation: `../21-dc-method/dcm.c`, unchanged.
- **SCHOLARLY** algorithm source: Lasry thesis chapter 9,
  https://kobra.uni-kassel.de/handle/123456789/15274 .
- **PRIMARY implementation** upstream:
  https://github.com/CrypToolProject/CrypTool-2/blob/main/CrypPlugins/IDPAttack/IDPAnalyser.cs .

Commands, chosen filter, frozen protocol and results will be added before their dependent runs.

## Development result and revised design

The five old failures have base-key ranks 1,717; 2,916; 4,876; 3,336; and 394 at their true first widths.
Supplying both the base phrase key and true first width to the old refinement recovers **0/5**, not blind
successes. Accuracies are 0.10–0.17. `diagnose.py` → `results/development.json`; original diagnostic source and
hashes are archived in `diagnostic_seedsolve.c` and `diagnostic-manifest.json`. Wider retention alone is not a fix.

Revised method: enumerate every exact list key and every one-rank-swap neighbour directly. `expand.py`
deduplicates the union into **1,286,188** keys, pinned in `expanded-manifest.json`. The scanner streams binary
records, scores all keys and retains four per **stated first-width hypothesis**. The refinement and threshold
are unchanged. This changes the search set; it is not evidence about the historical key.

Benchmark on old development ciphertext: the previously missed one-swap case reads at its supplied correct
first width 22 (score -4.0437; 44.868 process CPU seconds). Width 19, a cost check on the same ciphertext, gives
no candidate (83.309 CPU seconds). `benchmark.py` → `results/benchmark.json`. These are development results,
not fresh controls. Expected work is roughly 40 per-width controls plus 22 target/shuffle cells. Use at most
three workers. Fixed per-process CPU caps: 180 seconds for the streaming scan, 60 seconds for each seeded
refinement. A cap hit is a reported failure/incomplete batch, not grounds to replace that plant or raise the cap.

### Fresh calibration plan

Freeze before running: ten plants each at minimum swap distances 0, 1 and 2 from the original key list, plus
ten uniform-random numeric keys conditioned on minimum distance >3 from that list. Distance to the expanded
search set is max(0, original minimum distance minus one); random plants are therefore >2 from the expansion.
The near-list strata are not merely perturbations that might accidentally coincide with another list key.

Draw first widths uniformly 12–22 and second lengths uniformly 18–28. **Supply the stated first width in each
control run.** This calibrates conditional per-width recovery, not full unknown-width blind recovery. Do not
supply the key or plaintext. Target evaluation must enumerate all eleven widths, with the same per-width work
and no global early stop. An accidental candidate at one width must not prevent testing another width.

Keep four seeds after the expanded scan; 64 random reference keys per length; 20,000 IDP climb evaluations
per seed; 12 K1 restarts; candidate threshold -5.10. Stops within each width use score only. Record scanning and
refinement CPU cost, exact/in-place/shift-tolerant accuracy, true-key retention, and the minimum distance from
the true key to the retained seeds after search. Never feed that diagnostic into the search.

Exact/one strata must each recover >=8/10, and no control may give a false candidate (score passes but recovery
fails), before target work. Report two-swap/random outcomes even if they fail. A target failure is conditional
on the finite search set, width range, full body, preparation and budgets; no cipher exclusion follows.

Freeze the full control/build hashes in `protocol.json` before full T1 and one own-letter shuffle, all eleven
widths each. This is another exploratory T1 test; the complete solution criteria and independent T2 validation
still apply to any candidate. No list, budget, keep count or threshold changes after the holdout or target.

## Diagnostic correction and restart

Review caught a post-search reporting bug: nearest-retained swap distance compared keys of different lengths.
It now uses only same-length retained keys and reports null if none exist. The original run was stopped by
its source-hash guard after the preemptive edit. Seven valid partial records are preserved separately, with
their original driver/build/plan. They do not enter the new gate. The same tag, seeds and forty plants are
rerun after the correction; no plant was replaced and no search setting, candidate list or search function
changed. `results/restart-notice.json` records the archives. The independent verifier checks the exact AST
change and old/new plan and search equivalence.

## Commands

From this folder, with experiment 24's pinned model/corpus/key caches available:

```
python3 -I expand.py
python3 -I run.py build
python3 -I run.py verify
python3 -I run.py controls holdout25 10 3
python3 -I diagnose_gate.py
python3 -I summarize.py > results/summary.md
# Only after all 40 controls and the frozen protocol gate pass (this batch FAILED):
python3 -I run.py target target25 3
python3 -I verify_results.py --output results/verification.txt
```

Existing result tags are not overwritten. The frozen generator and caches let a new tag use a fresh sample;
do not replace failed plants under a supposedly unchanged tag.

## Result: recovery improves, acceptance gate fails

All forty controls completed under the fixed caps. Exact-list keys recover **10/10**, one-swap keys **10/10**,
two-swap keys **9/10**, and conditioned random keys **0/10**. Every recovery is exact. The first width was
supplied; these rates are not directly comparable to experiment 24's full unknown-width pipeline.

The missed two-swap plant, trial 8 at 21x22, scores **-4.5505**, above the frozen -5.10 candidate threshold,
despite only **0.4683** shift-tolerant agreement (0.0390 in-place). It is a false candidate under the frozen
rule. The gate therefore **FAILS**, even though both required recovery groups pass. **No T1 or shuffle run
was made, and no target protocol was frozen.** No threshold, budget or plant was changed to rescue the gate.

`diagnose_gate.py` reconstructs this synthetic plant without a search. The returned **second key is exactly
correct**; the first key is wrong. The true plaintext scores -4.068789. The pipeline stops after its first
retained seed because that imperfect result passes the score-only stop. This identifies a first-key
refinement/acceptance failure. It does not show that the phrase list contains the historical key.

Fresh-control work cost **3,242.504 process CPU seconds** (54.04 CPU minutes): 3,157.804 scanning, 84.700
refinement. This excludes development and the archived aborted run. Three workers were used. Enumerating a
finite phrase neighbourhood is CPU-feasible; arbitrary long-key recovery remains unvalidated (0/10 here).

`verify_results.py` independently reconstructs all forty plants and checks transformations, scores,
recovery metrics, retained-seed diagnostics, build/input pins and restart equivalence. Read
`results/verification.txt`, `results/summary.md` and `results/gate-diagnostic.json`. The next engineering
test must isolate first-key recovery with a known correct K2 and validate acceptance on fresh controls,
before another target run. The existing T1 negatives from experiment 24 remain the latest target result.

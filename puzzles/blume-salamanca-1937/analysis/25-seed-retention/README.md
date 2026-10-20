# 25-seed-retention — diagnose and improve phrase-key retention

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

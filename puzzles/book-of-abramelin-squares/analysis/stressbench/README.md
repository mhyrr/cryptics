# Shared stress-test harness

Three offline experiments answer the plan in [ATTACKS.md](../../ATTACKS.md).
Python 3.11+; standard library only. Run from the repository root:

```sh
python3 puzzles/book-of-abramelin-squares/analysis/stressbench/run_all.py
```

This prepares the manifest, runs experiments 02–04, writes the combined report,
and runs the shared tests. To verify that outputs survive another Python hash
seed without changes:

```sh
python3 puzzles/book-of-abramelin-squares/analysis/stressbench/run_all.py --check
```

`--check` snapshots the generated artifacts, reruns with a different hash seed,
and fails if any bytes change. It rewrites outputs during the check. No network
access, installation, source corrections or manuscript downloads occur.

## Data and split

`manifest.json` pins the input SHA-256, 81 complete grids, five folds and every
hidden coordinate. There are 81 connected groups in this sample. Grids with
identical first rows up to reversal, or identical whole grids up to rotation or
reflection, would share a group and fold. Tests cover transitive grouping.
This blocks obvious duplicate leakage; it does not establish independent
historical ancestry or detect all near-duplicates. All donor vocabularies,
transition tables and frequency baselines exclude the outer test fold.

Masks hide about 25% of individual cells, about 25% of complete eight-way
symmetry orbits, or everything outside the top row and left column. Whole-orbit
masking removes all possible geometric copies of a target. Each grid has one
fixed mask per type, shared across methods and controls. Per-cell results are
dependent; the reports make no significance or independent-sample claims.

## Controls and scoring

- `shuffled`: permute all cells within each grid; preserve its histogram.
- `symmetric_original`: the 55 grids with exact paired-diagonal symmetry.
- `orbit_shuffled`: the same 55 grids; shuffle values between same-size
  paired-diagonal orbits, preserving geometry and the exact letter histogram.
  Only compare this control with `symmetric_original`. Some orbit classes are
  too small to permute; this is a constrained control, not a full randomization.
- Planted data: each experiment has a known synthetic construction. Success
  demonstrates sensitivity to that construction, not to every possible rule.

Scores include correct and wrong predictions, coverage, abstentions and exact
recovery of every hidden cell in a task. Baselines use the training corpus's
most frequent letter, scored on **the same predicted cells**, as well as all
hidden cells. Experiment 02 also supplies exact global symmetry on common masks.
The combined report keeps the selected traversal-boundary test separate from
the fixed top-left boundary test. Neither teacher forcing nor symmetry copying
counts as a discovered generator.

`results.json` in each experiment contains every case and predicted coordinate.
The corpus and manifest hashes accompany each run. The source export and first
experiment remain unchanged. These are new masks on previously inspected
digital grids, not an untouched external test set. Thresholds were stated before
running these experiments; they have not been tuned against the outputs.

## Verification

The tests target orientation errors, related-grid leakage, corrupted scoring,
false donor multiplication, absent-context guessing and teacher-forcing leakage.
The planted tests require exact held-out recovery where the planted family is
identified. Reproduction additionally checks byte-for-byte outputs across fresh
Python processes. See [the combined report](../../STRESS-TESTS.md) for results.

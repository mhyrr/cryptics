# 27 — shorter phrase-derived second keys

## Question and frozen design

Does experiment26's repaired K1 recovery work on the uncovered band of first
widths16–22 and second widths12–17? This tests CC double columnar transposition
of the complete615-letter T1, using the existing Spanish model and phrase
guesses. It does not establish the historical system or language.

Before implementation: retain the exact26 optimizer,64 random reference keys
per second width, four retained seeds,20,000 IDP evaluations and12 K1 restarts.
Complete all four refinements. Filter24's FULL phrase metadata to12–17 and
expand each numeric key by all single arbitrary swaps of rank positions.
Deduplicate and hash the deterministic expansion. Add no phrases.

Run100 C/Python transposition checks, then freeze source/build/control plan
before fresh controls. Use40 fresh615-letter Spanish literary proxy plants:
10 each at minimum original-list distances0,1,2 and random>3. Supply the true
first width; withhold both keys and plaintext from the solver. Distances use
only equal-length keys. Random off-list plants may recover and are not
guaranteed negatives. Record per-width permutation-ball bounds to establish
that the random stratum exists. No assisted development or new optimizer
tuning is planned.

Gate: at least8/10 recoveries in each exact/one stratum, no false candidate
across all40, all40 complete. Recovery is at least95% agreement allowing
cyclic shifts through40 positions; exact/in-place agreement is separate.
Candidate threshold stays above-5.10. Two-swap and random recovery are
reported whether or not they meet8/10.

Only a passing, independently verified gate permits a frozen target protocol.
Then complete14 cells: seven first widths16–22 for T1 and one shuffle of its
own letters. Each cell scans the same expansion and completes all four seeds.
One shuffle is descriptive, not a false-positive rate estimate.

Stop after this one method if a gate fails, remains incomplete or hits its
CPU cap. No replacement plants, raised budgets or post-hoc thresholds.
Caps remain180 CPU seconds per scan and60 per refinement; at most3 workers.
Criteria for an actual solution remain those in the puzzle README: full,
reproducible coherent plaintext, exact re-encryption and independent evidence.
This finite, fallible phrase search cannot exclude arbitrary keys in this band.

## Run

Python standard library and a C compiler; uses pinned caches from24–26.

```
python3 -I puzzles/blume-salamanca-1937/analysis/27-short-k2/expand.py
python3 -I puzzles/blume-salamanca-1937/analysis/27-short-k2/run.py build
python3 -I puzzles/blume-salamanca-1937/analysis/27-short-k2/run.py verify
python3 -I puzzles/blume-salamanca-1937/analysis/27-short-k2/run.py controls holdout27 3
python3 -I puzzles/blume-salamanca-1937/analysis/27-short-k2/verify_results.py
python3 -I puzzles/blume-salamanca-1937/analysis/27-short-k2/freeze_protocol.py
python3 -I puzzles/blume-salamanca-1937/analysis/27-short-k2/run.py target target27 3
```

## Result

Not run yet. Source and control plan will be frozen before fresh controls.

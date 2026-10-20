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

The fresh control gate passes. All 40 cases finish: exact-list 9/10, minimum
one swap 10/10, two swaps 9/10, conditioned random 0/10. All 28 recoveries are
exact; zero false candidates. True first width is supplied per control.
The exact-list miss (22×14) loses its true key at shortlisting. This method
can miss even a listed key. The two-swap miss also remains below threshold.

Source/build/control plan freeze: `fa32d99`. Final build passes all 100 C/Python
transposition checks (`results/transform-checks.txt`). Control/protocol freeze
`5d99fe0` precedes target. The active list has 1,480 numeric keys, expanded to
160,327 unique keys. All distance bounds and sorted candidate bytes are
independently reconstructed.

All 14 target cells complete, with all four seeds each:

| Body | First widths | Second lengths | Best score | Candidates | CPU seconds |
|---|---|---|---:|---:|---:|
| T1 | 16–22 | 12–17 | -5.9662 | 0 | 86.510 |
| One own-letter shuffle | 16–22 | 12–17 | -5.9317 | 0 | 90.994 |

Threshold: above -5.10. Controls cost 511.967 CPU seconds; target 177.504.
Total recorded solver time is 689.471 CPU seconds (11.491 CPU minutes), summed
over workers. Preparation, build and verification are excluded.

`results/summary.md` and the recorded JSONL preserve the result. The independent
verifier checks all plants, decryptions, scores, shortlist diagnostics, seed
identities, all 56 target refinements and protocol pins. Run it after target
with `--output results/verification.txt` to save its report.

No reading. This is a finite, fallible phrase-neighbourhood negative under a
Spanish literary-proxy model. Arbitrary keys, other first widths, other
preparation and the actual historical cipher remain open. The one shuffle is
descriptive. No wider blind campaign is started. The next useful evidence is
independent period-telegram plaintext calibration or historical key/system
material.

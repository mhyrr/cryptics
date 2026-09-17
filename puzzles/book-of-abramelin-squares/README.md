# The word squares of the Book of Abramelin

**Catalog entry:** `catalog/entries/book-of-abramelin-squares.md`
**Status:** updated 2026-09-17 · four experiments complete; experiment 05 historical scoring blocked on dictionary inputs; no generator recovered

## Brief
Test whether a small, explicit rule predicts letters in Abramelin's incomplete
squares. Start with the Mathers transmission, preserve blanks and contradictions,
and reserve uninspected manuscript readings for later validation. Soyga motivates
the experiment; it does not establish that Abramelin has a comparable generator.

## What a solution would have to do
1. Publish a per-cell transcription with witness, square identifier, source
   locator, explicit blanks, and separate editorial conjectures. Ultimately
   collate all accessible witnesses; this first experiment is one transmission.
2. Specify a finite rule and its inputs before inspecting validation readings.
   Report contradictions, abstentions, and uncovered cells as well as matches.
3. Predict complete squares held out of fitting, and letters absent from Mathers
   but present in German witnesses. Compare against elementary symmetry and
   frequency baselines. Shared ancestry and modern editorial correction can
   produce agreement without validating an original generation process.
4. Distinguish constraint completion from generation: copying a reflected known
   letter does not explain how the unconstrained letters were chosen.
5. Test linguistic interpretations against declared controls before claiming
   meaningful language. This session makes no lexical identifications.

## Scope of this dive
First pass: locate German facsimiles and existing scholarship; extract a
machine-readable Mathers-derived corpus; characterize dimensions, blanks, letter
frequencies and symmetries; test elementary generation families; save conditional
fills without replacing source cells. Use Python's standard library.

Predeclared families: transpose symmetry, half-turn symmetry, their conjunction,
row/column reflections, cyclic shifts of the first row, and addition/subtraction
of first-row/first-column alphabet values modulo 26. These tests address exact
rules in the digital transcription. A failure does not prove the historical
text was random or that every more elaborate rule is impossible.

German images and corrected modern grids are not analysis input. Conditional
predictions are saved in `analysis/01-mathers-structure/predictions.json`.
Peterson variants and Kollatsch examples were exposed during discovery; a future
blind witness comparison needs an exposure audit and an alignment protocol.

## Three further attacks

Greg requested ten approaches and code for the best three. [ATTACKS.md](ATTACKS.md)
records the ranking and test design written before implementation. Experiments
02–04 test independent frame rules with copying-error costs, cross-family
fragment transfer and learned nonlinear local recurrences. The frozen benchmark
adds family-held-out folds, whole-orbit masks, geometry-preserving negative
controls and known synthetic constructions. No new witness letters were used.

The frame model recovers more scattered letters but fewer complete masked tasks
than strict symmetry. The other two methods do not reconstruct independent
letters reliably. Read the [combined results](STRESS-TESTS.md) and
[reproduction instructions](analysis/stressbench/README.md).

## Period-dictionary investigation

[Experiment 05](analysis/05-period-dictionary/README.md) identifies the cited
1595/1596 Frankfurt dictionary and records the source-access wall. It has a
written protocol and tested completion machinery, but no independent lexicon
or historical reconstruction score. Next: verify entry facsimiles, then test
fixed interior lexical placements. Identifying a seed alone cannot establish
how independent inner letters were selected. H7 and H12 remain open.

## Read the result
[Measured results](analysis/01-mathers-structure/RESULTS.md) ·
[method and rerun commands](analysis/01-mathers-structure/README.md) ·
[next session](NEXT.md). Follow-up: HIVE TK-005.

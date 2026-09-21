# The word squares of the Book of Abramelin

**Catalog entry:** `catalog/entries/book-of-abramelin-squares.md`
**Status:** reviewed 2026-09-20 · caption-guided dictionary seeds and partial structural prediction supported; no full generator; Warburg reading pending

## Current result

Experiments 12–19 establish more than the earlier E1/E2 pilots. Caption-only
German nominations retrieve seed words above permutation controls. All 21
selected experiment-14 hits have been checked on dictionary images. Symmetry
predicts many border letters; vowel/consonant alternation predicts interior
class. Exact interior-letter prediction remains weak.

The aggregate Dehn comparison gives 83/90 correct symmetry border predictions,
153/193 correct interior classes, and 61/193 letters against a 48/193 baseline.
Two records were exposed before freezing; excluding them gives 74/81 borders,
137/177 classes and 55/177 letters against 44/177. Dehn is edited evidence, not
an untouched manuscript. Experiment 16's separate discovery test peaks at
32.0% letter accuracy against 28.6% class-only.

These results support a partial construction account. They do not prove that
the remaining letters were freely chosen. The next step is the frozen
[Warburg witness test](analysis/20-warburg-witness/README.md). Its preflight
caught and fixed an uncertainty-counting defect in a separate wrapper; the
original models and predictions are unchanged. No Warburg historical score
exists yet. See [canon](canon.md), [hypotheses](hypotheses.md) and [handoff](NEXT.md).

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
   meaningful language. A reported lexical correspondence alone is not a construction rule.

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
1595/1596 Frankfurt dictionary; its selected facsimiles were subsequently
verified. [E1](analysis/10-caption-selector/README.md) freezes a literal caption
selector and an independent dictionary block. It remains unchanged.

[E2](analysis/11-caption-first-e2/README.md) instead freezes caption-first semantic
nominations. Eight German captions yield seven purpose-label alignments and three
complete Mathers targets, but no usable caption word domains or interior
predictions. The controlled pilot is uninformative. This describes the 2026-09-18 pilot. Experiments 12–19 subsequently
tested a revised lookup policy: H7 is supported, H12/H15 weakened. Neither a central word nor a source spelling assigns the remaining
independent interior letters.

## Read the result
[Measured results](analysis/01-mathers-structure/RESULTS.md) ·
[method and rerun commands](analysis/01-mathers-structure/README.md) ·
[next session](NEXT.md). Follow-up: HIVE TK-005.

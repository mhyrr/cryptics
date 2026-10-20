# 24-phrase-seeded — a bounded second-key attack

2026-10-19. Greg explicitly requested a new scripted solver attempt after the method audit.

## Initial development design, before implementation

Hypothesis H13: the second key of forward double columnar encryption is the stable alphabetic ranking of a
dossier-related phrase, or is within one or two rank swaps of such a key. This is a search assumption, not a
historical fact about the senders. The words are candidate key material, not imposed plaintext cribs.

Build a fixed, reviewable list from the existing names, places, firms and business context. Normalize accents,
rank repeated letters both left-to-right and right-to-left, and deduplicate numeric keys. Initially search first
widths 2–30 (narrowed in the frozen plan below). For each first width, shortlist phrase keys using IDP standardized against random second keys of the same
length, then climb from the shortlist and solve the remaining first key. Keep the two messages separate.

Reuse experiment 21's C transformation, IDP and refinement code without editing it. Add a small C scanning
front end and a Python driver. Record source/model/candidate hashes. The driver must independently re-decrypt
returned keys in Python. No plaintext or true key goes to the search, even for controls.

## Verification and limits

First run development plants at 615 letters with first widths 12–22 and second keys 18–28 letters, drawn
independently from solver seeds. Try exact list keys and keys one or two non-correcting swaps away. Register a
separate holdout control before using target text. A passing stratum needs at least 80% recovery under the
>=95%, cyclic-shift <=40 criterion over at least 10 trials. Report exact/one-swap/two-swap strata separately;
record exact/in-place accuracy too, and do not call failure a cipher exclusion.
Controls still use the earlier literary telegraph proxy; audit 23's historical-text limit remains.

Only run the target using strata that pass. Freeze parameters before the target. Candidate rule: whole-body
Spanish quadgram score above -5.10 and an independently matching decryption. A reading remains provisional
until the second telegram and all solution criteria are met. Score own-letter shuffles with the same pipeline
as a false-positive check. A candidate list that misses the actual key says nothing about the cipher family.

## Stop rule

One development batch, one holdout control per viable stratum, then a bounded target run if a stratum passes.
No expanding the word list or changing parameters in response to target fragments. If controls fail, retain
the scripts/results and name the failure. No outreach, new paid compute, or broad overnight campaign.

## Sources

- **Repository evidence:** `../../sources/context-cribs.md`, `../../sources/headers.md`, and audit 23.
- **PRIMARY implementation:** experiment 21's `dcm.c`; upstream IDP code by Lasry/Krauß,
  https://github.com/CrypToolProject/CrypTool-2/blob/main/CrypPlugins/IDPAttack/IDPAnalyser.cs .
- **SCHOLARLY method:** Lasry thesis, chapter 9,
  https://kobra.uni-kassel.de/handle/123456789/15274 (locally cached by experiment 21).

## Development and frozen holdout plan (before holdout/target)

The development batch `results/dev24.jsonl` recovered all three plants under the existing >=95%, cyclic-shift
<=40 criterion (each achieved 100% shift-tolerant agreement). Widths: exact 13x18; one-swap 16x25; two-swap 22x18.
This is development only, not the holdout result. It searched first widths 2–30 and all 8,534 keys of length
8–32; `build-manifest-dev.json` pins that earlier build.

After independent code review, record exact/in-place accuracy separately, pin plant inputs and JSON key
metadata, and enforce a nonempty control gate with unique trial IDs. Narrow the actual experiment to the
calibration region: **first widths 12–22; second lengths 18–28; 5,284 active numeric keys**. The same source
generator still records all 8,534 guesses in its metadata. This narrowing is before any holdout or target run.

Frozen parameters: 64 random reference keys per first-width/second-length cell; keep four seeds per first
width; try the original seed before IDP climbing; at most 20,000 IDP climb evaluations per seed; 12 K1 restarts
and the existing quadgram refinement. The budget caps the IDP climb, not total evaluations; process CPU time
includes scanning, K1 work and refinement. Across first widths, try seeds in descending standardized-IDP order.
Stop at the first independently checked plaintext score above -5.10, identically on controls and target.

**Holdout:** tag `holdout24`, ten independently seeded plants per distance 0/1/2, 30 trials total, 615 letters,
first width uniform 12–22, second length uniform 18–28, base numeric key uniform within the chosen length,
random first key. One/two swaps use distinct positions and cannot undo each other. No true key/plaintext is
passed to C. At least 8/10 recoveries (>=95% agreement allowing cyclic shift <=40) passes each stratum. Record
exact, in-place and shift-tolerant accuracy. Controls use the same literary proxy as previous experiments.

**Target gate:** require the exact-key stratum to pass; claim one/two-swap support only for the contiguous
passing strata. Freeze `protocol.json` with control/build hashes before running T1 at its full 615 letters and
one deterministic shuffle of T1's letters. No trimming, parameter change or word-list expansion in this shot.
A shuffle is a false-positive check, not a p-value estimate. A failed target is a negative result for this
finite list and pipeline; it does not exclude double columnar or other phrases.

## Commands

From the repository root, with experiment 21's cached Spanish model and held-out inputs available:

```
python3 -I puzzles/blume-salamanca-1937/analysis/24-phrase-seeded/run.py build
python3 -I puzzles/blume-salamanca-1937/analysis/24-phrase-seeded/run.py verify
python3 -I puzzles/blume-salamanca-1937/analysis/24-phrase-seeded/run.py controls holdout24 10 2
python3 -I puzzles/blume-salamanca-1937/analysis/24-phrase-seeded/run.py summary holdout24
# After recording protocol.json and only if the gate passes:
python3 -I puzzles/blume-salamanca-1937/analysis/24-phrase-seeded/run.py target target24
python3 -I puzzles/blume-salamanca-1937/analysis/24-phrase-seeded/run.py summary target24
```

No new Python dependency. Requires a C compiler. Missing corpus/model caches can be rebuilt with experiment
01/21's fetch/build instructions. The manifests pin the exact inputs used; downloaded revisions may differ.

## Holdout result and target registration

`results/holdout24.jsonl`: exact list key **10/10 exact recoveries**; one rank swap **9/10 exact recoveries**;
two rank swaps **6/10 exact recoveries**. No extra successes from shift tolerance. The two-swap stratum fails the
8/10 gate and is not claimed as supported. All five failures discarded the base phrase seed at the true first
width before refinement (from their saved shortlists). This identifies a limitation of the top-four filter.

`protocol.json`, written after all 30 controls and before any T1 run, pins the exact control/build hashes and
requires the passing distance-0/1 strata. The target uses the identical pipeline, full 615-letter T1 and one
own-letter shuffle. No list expansion, wider shortlist or new parameter tuning follows target inspection.
Only a negative result conditional on this finite list, preparation, model and budget can follow a failed run.

Recompute the compact report: `python3 -I summarize.py > results/summary.md` from this folder.

# Research log — append-only, newest first

## 2026-09-16 — Stress-test verification and close

`analysis/stressbench/run_all.py` completes all three new experiments and the
shared tests. `run_all.py --check` regenerates the manifest, six per-experiment
artifacts and the combined report under a different Python hash seed; all eight
artifacts match byte-for-byte. Fifteen new tests and eight first-pass tests pass.
The new tests exercise orientation, transitive grouping, histogram preservation,
whole-orbit masking, scoring, donor independence and causal rollout. No source
cells or experiment-01 outputs changed. Every new experiment has a README,
script and checked-in result. Canon, hypotheses and both handoffs are updated.

The benchmark generates 1,752 frame evaluation cases plus 666 corruption cases,
2,688 fragment cases and 4,992 recurrence cases. These are overlapping method,
mask and control evaluations, not independent observations. No catalog files
changed. TK-005 remains open for the source and witness audit.

## 2026-09-16 — Ten attacks, three implementations, controlled stress tests

Greg asked for ten different approaches and code for the best three. Wrote
[ATTACKS.md](ATTACKS.md) before running the new models. Selected independent
frame rules with copying-error costs, shared fragments across seed families,
and learned nonlinear local recurrences. These separate geometric completion,
independent letter content and recursive generation. No witness data were added.

Built a frozen shared manifest: 81 complete grids, 81 seed/orientation groups,
five deterministic folds. Masks remove scattered cells, whole eight-way
symmetry orbits, or all cells except a top-left boundary. Every model and donor
baseline excludes its test fold; the frame model itself only fits visible target
cells. Added full histogram-preserving shuffles, a geometry-preserving shuffle
on the same 55 symmetric grids, and known planted constructions. These are
fixed internal controls, not statistical significance tests or an untouched
historical test set. The original digital grids had already been inspected.

[The generated report](STRESS-TESTS.md) contains the measured outcomes and
per-fold evidence. Experiment 02 gets 555/591 scattered-cell predictions right
versus strict symmetry's 456/463. Coverage rises but exact recovery falls
30→18 of 81 tasks. It predicts nothing for entirely hidden symmetry orbits.
The original export receives 12 suggested letter changes across eight grids;
these are flags to inspect, not evidence of copying errors. H8 supported in
its narrow scattered-cell form; H11 refuted for the injected-error task.

Experiment 03 gets 2/10 whole-orbit predictions right and abstains in three
folds. Adding fragments after frames supplies two right and two wrong guesses
on scattered masks, and four wrong guesses on boundary masks. The standalone
method recovers all 320 planted motif centers; the composition misses one due
to a wrong frame prediction. H9 weakened for this corpus-derived vocabulary.

Experiment 04 selects from 12 family/corner configurations by nested training
validation. All five outer folds select pair lookup. Selected-corner rollout
gets 301/1,429 letters right, versus a frequency baseline's 262 on those cells;
one fold loses to the baseline. No complete task is recovered and no confident
prediction is made. The matched symmetric subset loses to the baseline.
Teacher-forced results are labelled separately; they never count as generation.
The planted nonlinear recurrence is recovered with 3,920/3,920 interior letters
correct in held-out confident rollout. H10 weakened as an Abramelin generator.

No thresholds or families were tuned after these outputs. The selected boundary
mask is separate because the training-selected corner can differ from top-left.
No control comparison silently uses different source subsets. Retain all results,
including the higher exact-task count for the simpler symmetry rule.

The Reeds comparison remains methodological. Search located the original paper
and its publisher bibliography, but direct PDF retrieval failed. We do not
claim to implement Reeds's historical Soyga algorithm; the planted recurrence
is explicitly our own A–Z construction. Kollatsch's frame and dictionary prior
art remains attributed in the plan and canon. Catalog scores are unchanged.

Next recommendation: verify the period-dictionary source and prepare an
independent lexicon/caption mapping for a new whole-orbit test. This is a distinct
attack, not parameter tuning on the current benchmark. Historical verification
still requires the facsimile audit and uncorrected witness targets in TK-005.

## 2026-09-16 — Verification and close

Eight unit tests pass. Re-running extraction, analysis and report generation
reproduces all four derived artifacts byte-for-byte; prediction input hashes
and the total fill count agree with the results. All 104 catalog entries pass
validation after adding the required tiered Sources list; rankings regenerated.
Git's default whitespace check flags the rank generator's existing intentional
Markdown two-space line breaks; the check passes with blank-at-eol disabled.
TK-004 is closed (first dive opened); TK-005 retains the witness-audit work.

## 2026-09-16 — First structural result and handoff

The web tool exposed rows and explicit dot placeholders, allowing an offline
corpus without the requested Python network download. Preserved a 207-line
row export spanning all numbered Mathers tables, then parsed its merged records
into 242 square records. The extraction excludes separately labelled German
supplements; raw rows and literal labels remain. Ten layouts fail the strict
square/single-letter criteria and stay excluded pending images.

[Experiment 01](analysis/01-mathers-structure/README.md) records the method;
[RESULTS.md](analysis/01-mathers-structure/RESULTS.md) gives generated counts.
Measured 81 complete and 151 incomplete analyzable grids. H1–H3 fail in their
declared exact forms. H4 is supported as a constraint statement: combined
symmetry forces 1,064 cells in compatible incomplete grids, yet MAIAM retains
four free letter choices. This is not a discovery of an original generator.

After that first result, added a fixed-rule diagnostic masking each complete
grid to top row and left column. It compares against a visible-letter mode on
the same prediction cells and counts errors and abstentions. No hidden answer
selects the evaluated sample. It tests artificial missingness in this export;
it neither trains nor validates against a second witness.

Saved conditional fills and source hashes in `predictions.json`. During source
discovery, Peterson's variants and examples from Kollatsch's November 2024 draft
were displayed. **Correction to the opening note:** no German manuscript images
were inspected, but some German *readings in editions* were exposed. Future
work must not call them blind targets.

Kollatsch's September 2025 inventory supersedes his 2021 count; see canon for
the updated source. The N 161 shelfmark was found in the SLUB holdings catalog,
but its open imaging remains unresolved. A [2020 source](https://solascendans.com/2020/05/15/abramelin-musings-the-dresden-manuscript/)
(POPULAR) places the N 111 squares at viewer image 243 / written page 240;
this is a locator to verify, not a checked folio reference.

Revised the catalog's absence-of-work claims, set status to partial, and reduced
compute 5→4 and crowding 4→3. Confidence becomes medium. The basis is prior
structural work and incomplete verification readiness, not the failure of an
exhaustive generator search. Follow-up ticket: TK-005.

## 2026-09-16 — Opening the dive and checking the premise

Greg selected Abramelin and authorized a first evening of witness discovery,
Mathers extraction, characterization and simple rule tests. The criteria and
finite first-pass families were written into README before computing results.

The literature search changes the proposed novelty claim. Peterson points to
Kollatsch's edition, and the author's publication list supplies a square-symmetry
draft and a conjecturally corrected compilation. See canon for tiered links.
Do not use those corrected letters as blind manuscript targets. The dictionary
derivation is a lead to replicate, not our finding.

The HAB records expose digitization requests but no direct manuscript images.
The Dresden N 111 viewer is linked but blocked by a JavaScript challenge.
N 161 access remains unresolved. No German square readings have been inspected.

The shell policy rejected curl, including an escalated call. Requested explicit
permission for Python HTTP downloads; web-source work continued independently.

## Dead ends

- 2026-09-16: H1–H3 fail as exact statements about the digital sample; see
  experiment 01. Preserve the distinction from possible corrupted precursors.
- 2026-09-16: H6, the claim of no prior structural work, refuted by the author's
  listing of an explicit symmetry study. No claim of first discovery is justified.

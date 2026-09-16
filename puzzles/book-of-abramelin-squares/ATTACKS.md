# Ten attacks and the next three experiments

Written 2026-09-16 before the new experiments. Greg requested ten approaches,
selection of three, implementation and stress tests. The existing source corpus
and experiment 01 stay unchanged. This is a feasibility study on the digital
Mathers transmission, not a manuscript decipherment.

## Ranked attacks

Ranking is a research judgment: prefer usable inputs, different failure modes,
and an explicit prediction test. It is not a numerical probability of success.

| Rank | Attack | What it could explain | Decisive test / present limitation |
|---|---|---|---|
| **1** | **Different rules for concentric frames, with a cost for copying errors** | Whole-grid symmetry failures caused by mixed frame types or a few bad letters | Predict masked letters and repair injected errors without rewriting sound letters; compare to global symmetry and shuffled grids. **Implement 02.** |
| **2** | **Reuse of letter sequences across squares** | Independent inner letters supplied by a shared stock of words or fragments | Learn only from other seed families; hide whole symmetry orbits, then test predictions. No assertion that fragments are natural-language words. **Implement 03.** |
| **3** | **Learned local recurrence** | A small nonlinear transition table, rather than the previously tested arithmetic of boundaries | Learn shared local rules on training squares; evaluate other seed families, both with observed neighbours and recursive generation. Demonstrate recovery on a planted nonlinear generator. **Implement 04.** |
| 4 | Period-dictionary reconstruction | Purpose words and embedded names providing independent constraints | Verify Kollatsch's cited dictionary entries, then retrieve words using captions without reading target cells. Needs a curated period lexicon and captions. |
| 5 | Witness collation and scribal-error model | Whether a discrepancy is a copying error, deliberate change or modern correction | Fit on witness pairs and predict a third witness; preserve conjectures separately. Direct images remain unresolved. |
| 6 | Caption / spirit-name alignment | Misnumbered squares and keys omitted from square-only analysis | Map captions and spirit lists before testing held-out letters; shuffled captions are a negative control. Needs reliable metadata extraction. |
| 7 | Joint row-and-column word-square search | Several known words forcing the intervening letters | Constraint search with a dated, independent multilingual vocabulary; report all solutions and matched random controls. Modern language guesses would bias it. |
| 8 | Minimum-description-length program search | A mixture of short recipes for frames, crosses and substitutions | Compare held-out compression and exact recovery to literal storage, charging for every exception and parameter. Broader grammar increases search and overfit risk. |
| 9 | Missingness and typography as evidence | Whether blanks, small letters and multi-letter cells are deliberate notation | Model masks by witness and caption; compare images, not just dot strings. Ten excluded layouts and the web layer currently limit this. |
| 10 | Controlled name insertion into an underlying square | Symmetry breaks caused by inserted spirit names rather than random damage | Infer the undamaged structure, then test whether residual paths match a withheld name list more often than shuffled lists. Needs case-preserving facsimiles and independent names. |

## Why these three
02 tests local composition and error tolerance. 03 tries to predict the free
letter choices that pure symmetry leaves untouched. 04 directly tests whether
there is a reusable generating process. All can run on the pinned local corpus
and can fail clearly. The manuscript-access wall still applies to historical
validation; it does not prevent these internal feasibility tests.

The frame idea follows existing prior art: CLAIMANT — Kollatsch's
[November 2024 symmetry draft](https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_).
The local-transition analogy comes from SCHOLARLY — Jim Reeds,
[John Dee and the Magic Tables in the Book of Soyga](https://citeseerx.ist.psu.edu/document?doi=1ab59debe52a20e98960c7f1de5c28d461892388&repid=rep1&type=pdf).
Synthetic tests below are our constructions, not transcriptions of Soyga.

## Frozen evaluation design
Use the 81 complete, unambiguous grids from experiment 01. Put identical grids
under the eight square orientations, and identical first-row seeds up to
reversal, in the same connected group. Assign groups deterministically to five
folds using SHA-256. All donors, letter frequencies and transition tables must
exclude the test fold. Record the split and masks before evaluating methods.

Evaluate three fixed missingness patterns on every test grid:
1. Randomly hide about a quarter of cells (fixed seed).
2. Hide about a quarter of the orbits of the full eight-way square symmetry
   group. This removes every geometric copy together.
3. Keep only the top row and left column (a gnomon). This tests boundary-driven
   completion and exposes the first pass's remaining free choices.

Report accuracy on predicted cells, coverage of hidden cells, errors,
abstentions, exact whole-task recovery and per-grid results. Compare every
method with a training-letter-frequency baseline on the same predicted cells,
and with exact global transpose-plus-half-turn completion. Report pooled counts
and per-grid/fold evidence; related cells are not independent statistical trials.

Controls: rerun on within-grid shuffled letters; rerun on shuffled assignments
of values to symmetry orbits for the symmetric subset (preserve geometry, remove
lexical ordering); and recover planted structures with known truth. Corruption
tests use artificial substitutions with the original digital reading as truth,
not a claim that the original reading is historically correct.

02: choose among identity, single reflections, half/quarter-turn, paired
diagonal symmetry and full square symmetry independently per frame. Charge
about log2(26) per independent observed symbol and the fixed 5%-error-channel
cost per changed observed letter. If best models disagree, abstain. No repair is
written back to the source. Keep the scoring and tie rules fixed.

03: use rows/columns/reversals from training grids as a fragment vocabulary.
Match observed context only; require at least two observed positions, at least
three distinct donor groups and at least 90% agreement among donor-group votes.
Never let a donor vote repeatedly through its reflected copies. Try lengths
3–5 and full rows, prefer more observed context, and abstain on tied conflicting
predictions. Also evaluate the declared composition: frame fills first, then
fragment inference. Count propagation errors against the original truth.

04: fit directional nonlinear families C=N+f(W), C=W+f(N), and C=f(N,W)
modulo 26. Select direction and family by inner training-fold validation, not
outer test scores. Require three supporting training grids and 90% agreement
for a confident transition; also report unrestricted modal prediction. Separate
one-step prediction with true neighbours from recursive generation from a
boundary. Missing predecessor predictions propagate abstention. No teacher
forcing may be labelled generation. Test all four corner traversal directions.

## Decision rule
A method earns further work only within the capability its tests demonstrate.
02 may be useful for repair without recovering free letters. 03 must improve
prediction after whole-orbit masking to support shared letter content. 04 must
generalize to held-out seed families and survive recursive rollout before it
supports a generator claim. Synthetic recovery verifies power for that planted
family only. No success threshold will be tuned after seeing the test results.

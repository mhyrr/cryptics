# Abramelin: three attacks under stress

Generated from experiments 02–04. The frame model supplies useful candidate
fills for scattered blanks. Fragment transfer and learned local recurrence
do not provide reliable reconstruction of the independent letters.

The [ten-attack plan](ATTACKS.md) was written before these runs. All tests
use the same 81 complete digital grids in 81 seed/orientation groups,
with five fixed folds. These are internal tests on a previously inspected
transcription, not German-witness validation or a decipherment.

## Principal results

| Method and target | Correct / predicted | Accuracy | Coverage | Frequency baseline correct on same cells | Exact tasks |
|---|---:|---:|---:|---:|---:|
| Frame rules; scattered blanks | 555/591 | 93.9% | 79.6% | 101 | 18/81 |
| Exact global symmetry; scattered blanks | 456/463 | 98.5% | 62.4% | 85 | 30/81 |
| Frame rules; whole orbits hidden | 0/0 | — | 0.0% | 0 | 0/81 |
| Fragments; whole orbits hidden | 2/10 | 20.0% | 1.2% | 0 | 0/81 |
| Fragments added after frames; scattered blanks | 2/4 | 50.0% | 0.5% | 2 | 0/81 |
| Local rule; selected-corner boundary; modal rollout | 301/1429 | 21.1% | 66.9% | 262 | 0/81 |
| Local rule; selected-corner boundary; confident rollout | 0/0 | — | 0.0% | 0 | 0/81 |
| Local rule; whole orbits hidden; modal rollout | 78/422 | 18.5% | 50.2% | 43 | 0/81 |

The frame method trades precision and exact task recovery for more cell
predictions. Its success concerns letters with surviving geometric copies;
it predicts none when every copy is hidden. The global comparator uses
transpose plus half-turn symmetry and rejects visible contradictions.

On the unmodified export it flags 12 letters in 8 grids.
These are disagreements with the digital reading, not established scribal errors.
With one artificial substitution per grid, 48/62 suggested repairs restore
the original letter; 13 proposals change cells that were not corrupted.
The method is unsuitable for automatic transcription correction.

The recurrence result contains a small pooled gain over the frequency baseline,
but no exact reconstruction and no confident predictions. The selected boundary
comes from the traversal chosen on training data. It is not necessarily the
top-left boundary, so it must not be compared directly with a different mask.

## Negative controls

Orbit-shuffled values preserve letter counts and paired-diagonal geometry.
Compare that control only with the same symmetric subset. The fully shuffled
control uses all complete grids. These are fixed permutations, not a p-value
or a sampling distribution.

| Method / mask | Dataset | Correct / predicted | Baseline correct |
|---|---|---:|---:|
| frame_mdl / cells | original | 555/591 | 101 |
| frame_mdl / cells | shuffled | 19/139 | 26 |
| frame_mdl / cells | symmetric_original | 388/390 | 70 |
| frame_mdl / cells | orbit_shuffled | 382/388 | 76 |
| fragments / orbits | original | 2/10 | 0 |
| fragments / orbits | shuffled | 1/4 | 2 |
| fragments / orbits | symmetric_original | 0/8 | 0 |
| fragments / orbits | orbit_shuffled | 4/4 | 4 |
| modal_rollout / selected_corner_boundary | original | 301/1429 | 262 |
| modal_rollout / selected_corner_boundary | shuffled | 272/2073 | 368 |
| modal_rollout / selected_corner_boundary | symmetric_original | 146/689 | 156 |
| modal_rollout / selected_corner_boundary | orbit_shuffled | 107/930 | 181 |

Frame completion also succeeds when lexical ordering has been shuffled but
symmetry survives. Thus high fill accuracy alone is not evidence of meaningful
language or a generator. Fragment transfer is too sparse and error-prone
to support its proposed use. The recurrence loses to the frequency baseline
on the matched original symmetric subset.

## Planted positive controls

| Known construction | Correct / predicted | Hidden cells | Exact tasks |
|---|---:|---:|---:|
| Mixed frame symmetries | 413/415 | 540 | 9/60 |
| Recurring fragments | 320/320 | 320 | 80/80 |
| Nonlinear local recurrence | 3920/3920 | 3920 | 80/80 |

These controls establish sensitivity to the specific planted constructions.
They do not replicate the historical Soyga algorithm. The composed frame-plus-
fragment method introduces one wrong answer on the planted fragment data;
its standalone fragment stage recovers every target.

## Results by outer fold

Counts concern the three principal masks; cells within a grid are dependent.
The frame model fits visible target cells only. Its fold assignment affects
the frequency baseline; the other methods exclude the fold from fitting.

| Experiment / mask | Fold | Correct / predicted | Hidden | Baseline correct |
|---|---:|---:|---:|---:|
| 02 / cells | 0 | 95/104 | 135 | 13 |
| 02 / cells | 1 | 146/153 | 192 | 34 |
| 02 / cells | 2 | 101/108 | 124 | 16 |
| 02 / cells | 3 | 111/120 | 163 | 21 |
| 02 / cells | 4 | 102/106 | 128 | 17 |
| 03 / orbits | 0 | 0/4 | 176 | 0 |
| 03 / orbits | 1 | 2/6 | 199 | 0 |
| 03 / orbits | 2 | 0/0 | 148 | 0 |
| 03 / orbits | 3 | 0/0 | 182 | 0 |
| 03 / orbits | 4 | 0/0 | 136 | 0 |
| 04 / selected_corner_boundary | 0 | 67/291 | 382 | 43 |
| 04 / selected_corner_boundary | 1 | 73/425 | 567 | 95 |
| 04 / selected_corner_boundary | 2 | 41/208 | 356 | 35 |
| 04 / selected_corner_boundary | 3 | 71/301 | 465 | 55 |
| 04 / selected_corner_boundary | 4 | 49/204 | 366 | 34 |

## Decision and limits

Retain frame fills as candidates for a facsimile audit. Do not tune these
three methods against the same outer folds and call the result validation.
The next distinct attack is the period-dictionary hypothesis already in the
literature: verify its sources, then test whether an independent lexicon
predicts letters hidden as whole symmetry orbits. A curated vocabulary and
reliable captions are missing inputs for that experiment.

Historical verification still needs an image audit of this transcription and
uncorrected German witness targets. No failure here establishes randomness,
corruption as the sole explanation, or absence of every possible generator.

## Reproduce and inspect

[Shared harness and checks](analysis/stressbench/README.md) ·
[02 frame method](analysis/02-frame-model/README.md) ·
[03 fragment method](analysis/03-fragment-transfer/README.md) ·
[04 recurrence method](analysis/04-local-recurrence/README.md).

Corpus SHA-256: `22b70346ddda2564a2881c342ba9f9bd04fbaad1c00a656f2ff7b8302cb3933d`.
Each JSON result includes the manifest hash and every predicted cell.
The digitized source is PRIMARY text mediated by
[Peterson](https://www.esotericarchives.com/abramelin/abramelin.htm);
its letters have not been collated to a facsimile.

# E2 results — uninformative caption-selector pilot

**No evidence for a caption selector.** E2 made no predictions on the
three complete aligned targets. Their caption lookups never supplied a
usable word domain. Accuracy is undefined, not 0% or 100%. This tests the
operational coverage of the narrow procedure; it does not reject semantic
selection, dictionary derivation, or a different placement.

Inputs: 8 consecutive German captions; 7 purpose-label alignments; 3 complete odd Mathers targets.
Lookups: 3 spelling_excluded, 6 unresolved, 2 verified.

## Every sampled caption remains in the ledger

| German caption ID | Mathers label | Size | Complete | Selection | Evaluation exclusion |
|---|---|---:|---|---|---|
| W1853-IV-5-1 | unmatched | — | None | not joined | unmatched_caption |
| W1853-IV-5-2 | 5/8 | 5 | True | unresolved_lookup | none; model may abstain |
| W1853-IV-5-3 | 5/3 | 7 | False | no_length_matched_word | incomplete_target |
| W1853-IV-5-4 | 5/9 | 5 | True | unresolved_lookup | none; model may abstain |
| W1853-IV-5-5 | 5/4 | 5 | False | unresolved_lookup | incomplete_target |
| W1853-IV-5-6 | 5/10 | 6 | False | ineligible_size | incomplete_target, ineligible_size |
| W1853-IV-5-7 | 5/5 | 5 | False | unresolved_lookup | incomplete_target |
| W1853-IV-5-8 | 5/11 | 5 | True | unresolved_lookup | none; model may abstain |

## All-interior mask

Each of three 5×5 targets contributes nine hidden cells in three whole D4
groups. All comparisons use these same targets; all have prior internal
Mathers exposure. There is no untouched-witness stratum.

| Method | Correct | Errors | Predicted / hidden | Exact tasks | Contradictions |
|---|---:|---:|---:|---:|---:|
| caption | 0 | 0 | 0 / 27 | 0 | 0 |
| dictionary_position_frequency | 6 | 6 | 12 / 27 | 0 | 0 |
| symmetry_T | 0 | 0 | 0 / 27 | 0 | 0 |
| symmetry_TA | 0 | 0 | 0 / 27 | 0 | 0 |
| training_frequency | 4 | 23 | 27 / 27 | 0 | 0 |
| without_captions | 0 | 0 | 0 / 27 | 0 | 3 |

## One whole interior D4 group at a time

| Method | Correct | Errors | Predicted / hidden | Correct groups | Wrong groups | Abstained groups |
|---|---:|---:|---:|---:|---:|---:|
| caption | 0 | 0 | 0 / 27 | 0 | 0 | 9 |
| dictionary_position_frequency | 6 | 6 | 12 / 27 | 0 | 3 | 6 |
| symmetry_T | 0 | 0 | 0 / 27 | 0 | 0 | 9 |
| symmetry_TA | 0 | 0 | 0 / 27 | 0 | 0 | 9 |
| training_frequency | 4 | 23 | 27 / 27 | 1 | 8 | 0 |
| without_captions | 0 | 0 | 0 / 27 | 0 | 0 | 9 |

## Controls and interpretation

All 120 control/mask summary rows have zero caption predictions.
Twenty within-size caption permutations ran. The unchanged-caption counts
are `[1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 3, 1, 3, 0, 0, 0, 0, 0, 1]`.
All three complete originals are T-compatible and enter the twenty
orbit-value permutations; their matched original rows are saved separately.
Word-letter controls have empty selected domains and are explicitly vacuous.
Changing captions cannot fix an unresolved lookup under this procedure.

Baseline comparisons on the caption-predicted subset have denominator zero.
The caption-free pool includes all five retrieved relevant-sense entries,
including spelling-excluded caption joins. Its no-prediction outcome here
is contradiction, whereas the caption model abstains before placement.
These different failure modes must not be presented as equivalent models.
Dictionary positional-frequency guesses do not use captions; their limited
matches are not evidence for a selector. No complete square was recovered.

## What this run can and cannot tell us

The sampled source solves the caption-access problem for this pilot. The
strict lookup policy does not solve usable lexical input. Six searches are
unresolved, not verified absences. Three found headwords need unpermitted
German spelling changes. The three -gestalt compounds were not split.
The unmatched giant and four incomplete aligned targets remain recorded.

Do not broaden spelling, split compounds, drop an unresolved alternative,
or redraw captions inside E2. Use these as development observations for a
separately frozen E3 on a new cohort. No incomplete-square witness stage
is justified. H7/H12/H15 remain open; E1 and H14 are unchanged.

See [README](README.md), [protocol](PROTOCOL.md), [exposure audit](EXPOSURE.md),
[lexicon](lexicon.json), [per-task results](results.json), and the complete
[frozen per-cell predictions](predictions.json).

# Experiment 05 protocol — 2026-09-17, before implementation

**Status: historical evaluation blocked on primary-source inputs.** Synthetic
checks below test machinery only. They do not test the dictionary hypothesis.

## Construction and prediction

The accessible literature supports investigating selected purpose words and
names placed within symmetric arrangements. It does not supply a deterministic
rule for the remaining letters. See the [source audit](SOURCE-AUDIT.md).

Our narrow, falsifiable candidate recipe is: choose a dictionary spelling from
a predeclared caption-to-entry mapping; place it on a predeclared straight row
or column; impose a specified symmetry; leave all unassigned orbits free.
This is our operational hypothesis, not a recovered historical recipe.
An outer seed alone cannot constrain a disjoint inner orbit.

Inputs must specify the alphabet, grid size, observed cells, hidden coordinates,
symmetry, dictionary candidates, permitted placements, and caption mapping.
No approximate matches, arbitrary insertion/deletion, phonetic replacement,
reversal, synonym expansion, or movement of a word after seeing an answer.
Multiple permitted placements must be counted as alternative models, not
selected for agreement with concealed truth. An all-rows word-square model
would be a separate hypothesis and requires separate justification.

Enumerate every compatible lexical assignment. Represent remaining freedom as
explicit independent orbits over the alphabet. Predict only letters common to
every completion; zero completions means contradiction, not unanimous support.
Report all branches, their counts and residual domains. Distinguish unique
letters from unique whole squares. Never resolve ambiguity by linguistic taste.

## Source gate and freeze

Before historical scoring, acquire legible title and entry images for the
Palthenius/Basse Frankfurt 1595 or 1596 dictionary. Check exact spelling,
adjacent alternatives, entry boundaries, and any purported error. Testing the
claim of an edition-specific error also requires an earlier comparison edition.
Record image identifiers and hashes. Keep Greek/Hebrew originals and printed
Latin transliterations separate. Do not silently supply modern transliteration.

Transcribe a contiguous, preselected entry/page block including misses, rather
than collect words already recognized in squares. Keep discovery examples in a
separate file. Lexicon rows need image, page/signature, headword, language, raw
spelling, context, uncertainty, and an ordered normalization log. Initially
permit only Latin case folding and long-s to s; exclude uncertain readings.
Freeze the lexicon, captions, placements, normalization, masks, controls and
code revision with hashes before scoring. Any revision starts a new experiment.
The current `claims.json` is deliberately **not** such a lexicon.

## Historical evaluation once the gate passes

Use the existing 81-grid manifest and five folds; call this **internal Mathers
evaluation**, never blind validation. Hide whole D4 orbits with the existing
orbit mask. Add a separately frozen interior-only D4-orbit mask so seed recovery
cannot masquerade as inner-letter prediction. If a mask is empty, mark the task
ineligible; do not count it as a successful reconstruction. Check that no
member of each target orbit remains visible. Models receive only masked input.

Compare lexical constraints plus symmetry to exact symmetry alone, training-fold
letter mode, and a length-matched frozen dictionary positional-frequency mode.
Report baseline accuracy both on all targets and on the method's predicted
cells. Report counts by grid/fold, inner versus border, discovery-exposed versus
other grids: errors, abstentions, coverage, contradictions, number of competing
completions, and completely correct squares. Cells are dependent; no binomial
significance claim over cells.

Use 20 deterministic permutations per control: caption assignments within size
strata; letters within dictionary words, preserving length and word histograms;
and orbit-value shuffles preserving symmetry and orbit-size histograms, compared
with the same symmetric subset of originals. Freeze seeds before scoring.
Caption controls require a caption-free lexical comparator. Enumerate rather
than silently discard incompatible cases. Report coverage as well as accuracy.

## Synthetic checks specified before coding

Generate symmetric squares from an explicit artificial vocabulary. Hide all
interior cells (a union of D4 orbits). Constrain declared interior rows by their
dictionary domains. Require recovery of the planted letters, zero errors and
one completion. Add an alternative word differing only at the central letter;
require two completions and abstention at that letter. Remove interior lexical
constraints; require remaining inner freedom. Supply a contradictory word;
require no predictions. These are software checks, not historical successes.

## Escalation to witness predictions

Only after inner-letter performance survives the comparisons, freeze incomplete
square predictions. First audit raw print/manuscript readings, editorial changes,
source exposure and caption/seed alignment. Numbering alone is insufficient.
Account for shared witness ancestry. Keep predictions, raw readings and editorial
conjectures in different files. Log unmatched squares and failures. Do not open
new witness answers during model selection. The current source-access failure
leaves this gate closed; it says nothing about randomness.

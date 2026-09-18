# E1: literal caption selector and central cross — exploratory freeze

2026-09-18, starting from 9202fed. This is our deliberately narrow hypothesis,
not an attribution to a historical author. No new square answers were read to
choose it. Experiments 06 and 09, and all their examples, are discovery data.
The specification is frozen before selecting a new dictionary block. A later
change requires E2, with its exposure recorded; do not overwrite E1.

## What this could establish

Test whether literal German caption wording selects printed Hebrew
transliterations that predict hidden inner letters under a fixed central-cross
construction. A successful partial prediction would not assign all letters,
establish dictionary dependence, or recover the original generator. A failure
would reject only E1. Purpose words can be associated semantically with captions
without occurring literally in them; E1 deliberately tests literal selection.

## Complete recipe

1. **Inputs and applicability.** Use an independently transcribed local German
   square caption, its source locator, a verified alignment to a target ID,
   the target size, and a masked grid. No seed, spirit name, apparatus gloss,
   chapter heading, or inferred purpose is a caption input. Only odd sizes n>=3
   are geometrically applicable. Even sizes and missing/uncertain captions remain
   in the ledger as misses/ineligible, not removed to improve coverage.
2. **Caption → entry.** Tokenize maximal Unicode alphabetic sequences after
   long-s→s and case folding. Match an entire printed German headword alias as
   a contiguous token sequence in the caption. Split aliases only at printed
   slash separators, not at commas or inferred synonyms. Use every matching
   entry; do not pick a noun, stem, translate, modernize u/v, expand a compound,
   follow cross-references, or add semantic neighbours. No matching headword in
   the sampled block is a *sample miss*, not a dictionary-wide absence.
3. **Alternative words.** Collect every printed Latin transliteration belonging
   to the Hebrew gloss of each selected entry, in printed order. Do not add the
   Latin, Greek, French, or poetic glosses. Each word is an alternative complete
   model, not an instruction to insert all synonyms at once. An entry without
   such a gloss is a recorded miss. Uncertain relevant headwords, entry boundaries
   or transliterations make the task abstain; excluding a possibly competing
   reading could create false consensus. Preserve them in the lexicon ledger.
4. **Spelling.** Retain raw readings and an ordered operation log. Allow long-s→s,
   ASCII uppercasing and joining a *visually verified typographic line break*.
   No other punctuation stripping inside a word, vowel substitution, h deletion,
   doubling, transliteration from Hebrew, or inflection. Only single A–Z tokens
   of exactly n letters enter the word domain. Other forms remain recorded with
   length/alphabet exclusion reasons. Duplicate normalized words count once.
5. **Orientation and placement.** Put each eligible word left-to-right across
   the full central row, row (n+1)/2 in one-based coordinates. No reversal,
   rotation, boundary-first option, even-grid expansion, offset or path search.
   This choice is motivated by the exposed central-line examples, but is ours.
6. **Overlaps and symmetry.** Impose transpose T, reflecting the row into the
   central column with the same word read top-to-bottom. All overlaps must agree
   exactly. Do not also impose A, TA, D4 or per-frame symmetry. Do not insert
   opposed copies. Those are separate future recipes, not fallback branches.
7. **Corruption and names.** Predict the surviving, case-normalized target text,
   not a latent precursor. All visible letters are binding. Contradiction gives
   zero completions and no predictions. No repairs, erasures beyond the mask,
   capital-based exceptions or post-hoc corruption allowance. No spirit names
   are independent inputs: the draft explicitly allows derivation from letters.
8. **Residual letters and uncertainty.** Enumerate all compatible word branches.
   Each untouched T orbit independently ranges over A–Z. Save branch orbit
   assignments and free domains, with exact completion counts. Predict a hidden
   letter only if every completion agrees. Zero completions is contradiction;
   multiple completions is not failure if some letters have consensus. Missing
   caption/lexicon input gives no lexical predictions, not a symmetry success.

## Sampling and exposure, in this order

First hash this specification and the executable selector/solver with its tests.
Then select a contiguous two-scan block from the 1596 A–S dictionary body
(scans 55–1153), excluding the previously acquired scans and adjacent scans.
Use SHA-256 of the literal string `9202fed:E1:dictionary` modulo the eligible
start list, sorted ascending. No redraw for dull entries, misses or illegibility.
Transcribe all entries beginning on either scan, including entries with no Hebrew
transliteration and entries with no caption match. Read following pages only to
finish the last included entry; leading continuation is context, not an entry.
Record all image hashes, locators, raw words, alternatives and uncertainty.
The sample is independent of answer selection, not a representative large corpus.

Freeze that transcription before joining it to captions. Caption-only target
alignment must be frozen separately, without grid-letter matching. The existing
Mathers export has no caption fields: obtaining and auditing that mapping is a
required input, not permission to manufacture captions from seeds. Do not expand
the dictionary sample to rescue a zero-overlap result. Discovery captions may
exercise the selector but must never enter evaluation denominators.

## Evaluation contract (experiment 05 retained)

Use the existing 81-grid/five-fold stressbench manifest: this is internal Mathers
evaluation, never independent witness validation. Before scoring, freeze captions,
lexicon, exposure exclusions, masks, controls, code and source hashes. Preserve
all target IDs and miss/contradiction reasons. Exclude any grid whose discovery
identity cannot be ruled out from the non-discovery stratum; report separately.

Use the existing whole-D4-orbit masks. Also mask *every* strict interior cell
(0<r,c<n-1); this is a union of whole D4 orbits. Assert no target-orbit member
remains visible. Empty masks are ineligible. D4 governs masking only; E1 uses T.
The solver receives masked grids only. Freeze per-cell predictions before a
separate scorer receives concealed letters. Whole-orbit and interior-only results
stay separate; seed recovery cannot satisfy the interior gate.

Compare to exact T alone (and retain experiment 05's TA baseline separately),
training-fold letter mode, and sampled length-matched dictionary positional mode.
Tied modes abstain. Caption-free comparator uses all sampled eligible words of
length n at the same path. Report all targets and the method's predicted subset
for every baseline. No targets means null accuracy, not 0% or 100%.

Use 20 permutations each, with integer seeds 2026091800+i, i=0..19, independently
for: caption assignments within size strata; letters within each dictionary word;
and orbit values within T-orbit-size strata on T-compatible originals. Compare
the last control only to those same original grids. Singleton strata and unchanged
permutations remain reported. Preserve words' lengths and letter histograms.
Use the caption-free comparator to identify gains due specifically to captions.

Save errors, abstentions, coverage, contradictions, competing completions and exact
square recovery by grid/fold and border/interior, with exposure strata separate.
Report no cell-level binomial significance: cells in an orbit are dependent.
No incomplete-square/raw-witness stage unless E1 has positive inner-letter evidence
beyond these comparisons. In particular no eligible tasks, no inner predictions,
or identical performance to the caption-free comparator cannot support a caption
selector. Any favorable small-sample result still requires a new independent block.
Raw witness answers remain closed until incomplete-square predictions are frozen.

## Evidence boundaries

CLAIMANT: [Kollatsch structural draft, pp. 35–41, 46](https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_).
Experiments [06](../06-construction-evidence/EVIDENCE.md) and
[09](../09-structural-draft/README.md) already inspect this supplied source.
They motivate exploration but do not transmit E1. No new acquisition search is
needed for the three supplied PDFs. PRIMARY dictionary images use the existing
BSB object bsb11762465 and its documented IIIF route.

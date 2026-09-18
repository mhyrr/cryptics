# E2 — caption-first lexical pilot

2026-09-18. Separate from experiment 10's frozen E1. This implements the
user's caption-first experiment. Neither E1's sample nor its recipe changes.

## Question and success condition

Does a German caption select dictionary words that improve prediction of
whole hidden interior symmetry groups? A central cross is a partial prediction;
unassigned interior groups remain unassigned. This cannot establish a generator.

## Caption sampling and exposure

Use the Warburg digitization of the German printed book, catalogued as Stuttgart
1853: PRIMARY [record](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf).
The catalog describes a reprint with a 1725 imprint; we do not resolve its dating.
Take the first eight consecutive local captions beginning with Book IV chapter 5.
Do not select by square size, completeness, dictionary availability or letters.
If fewer captions are accessible, keep the missing slots. Retain original German,
chapter context, printed and digital locators, uncertain readings, and unmatched
Mathers targets. Match purpose and local context, not numbering alone. No new
German square letters may be displayed to the selector. Crops must exclude them.
The Mathers corpus has prior internal exposure; no result is blind witness evidence.
Discovery examples and uncertain exposure identities cannot enter a clean stratum.

## Semantic selection, frozen before nominations

For each local caption nominate at most TWO German lookup concepts in order:
(1) the explicit concrete entity or material that the operation concerns;
(2) one direct German synonym for that same entity, if there is one with the
same scope. If there is no entity, use the named action as an infinitive, then
one direct synonym. An elliptical caption may inherit only the grammatical
action from its recorded chapter heading. No associated agent, instrument,
mythological identification, cause, effect, metaphor, or broader/narrower category.
An unclear referent abstains. Each nomination needs a caption phrase and a reason.
Unused second slots stay empty. This is a bounded human/LLM annotation procedure,
not a recovered historical instruction or deterministic semantic algorithm.

Freeze all nominations together before looking up any entry or target size.
German lookup permits case folding, long-s to s, singular nominative for an
explicit inflected noun, and infinitive for an explicit inflected verb. For
locating the SAME headword permit historical u/v, i/j, and th/t variants. No
compound splitting or new synonym after a lookup miss. Log each operation.
There are no spelling or inflection operations on Hebrew transliterations beyond
long-s to s, ASCII uppercase, and visually verified typographic line joins.

## Dictionary retrieval

Use the pinned Frankfurt Palthenius/Basse 1596 A–S and 1595 T–Z volumes.
Retrieve every nominated headword, including unresolved searches and entries
without a Hebrew gloss. Preserve all printed Latin transliterations of the
Hebrew gloss, in printed order, plus images and uncertainty. Retain other-language
glosses in the images; they are not lexical candidates in this recipe.
A bounded search failure is not proof of dictionary absence. No choosing by
square resemblance. An uncertain relevant entry or unresolved nominated lookup
causes that caption to abstain; do not discard potential competitors.

## Placement and evaluation design

The placement is fixed here, before entry retrieval: a single word of exactly
odd size n>=3, left-to-right on the full central row, reflected by transpose T
into the central column. No reversal, offsets, repairs, name overlays or other
placements. All eligible alternatives are branches. Visible contradictions
reject branches; only consensus across all surviving completions is predicted.
Unassigned T groups range independently over A–Z. Zero branches abstains.

After source and alignment gates, freeze lexicon, masks and executable evaluation
before predictions. Use the existing Mathers five-fold assignments for internal
evaluation. Preserve incomplete, even-size, unmatched and uncertain records in
the ledger. Score complete eligible records only, with two separate masks:
(a) every strict interior cell; (b) one whole strict-interior D4 group at a time.
Never leave another member of a hidden group visible. D4 is a masking rule; the
construction uses T. Record border filtering and residual free groups.

Controls on identical targets: T alone; TA alone; training-fold letter mode;
length-matched dictionary positional mode; the identical union of retrieved
vocabulary without captions; and 20 caption permutations within size strata,
seed 2026091800+i for i=0..19. Singleton/unchanged permutations remain reported.
Caption permutations move frozen nominations, never rerun semantic annotation.
Also run the 20 word-letter and T-orbit-value controls specified by E1, with
matched original subsets. Tied frequency modes abstain. Keep every lookup miss.

Freeze per-cell predictions before a separate scorer reads hidden letters.
Report errors, abstentions, coverage, contradictions, compatible branches,
residual completion counts and exact task recovery by target and exposure.
Compare baselines both on all target cells and on the caption method's predicted
cells. Report whole groups and squares; no cell-level binomial significance.
No gain over shuffled/absent captions is no evidence for this selector.
No eligible predictions means an uninformative pilot, not rejection of dictionary
derivation. A positive pilot requires independent replication before raw witness
answers are opened. Later policy changes require a new experiment.

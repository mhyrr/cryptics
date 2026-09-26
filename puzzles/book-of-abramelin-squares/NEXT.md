# NEXT — handoff

**Last updated:** 2026-09-26 (evening). Experiments 21–24 are complete. The dive is active; the Dresden N 111
image-access wall is resolved. No complete generator has been recovered.

## What moved

- **Warburg audit (21):** two independent Sol readings of a frozen 48-item
  sample and a Sol scorer review. Original scores reproduce. In comparable
  positions, the Opus and Sol pairs each agree internally but conflict with
  one another at 31 letters. Neither is adjudicated correct. The stricter
  gate mixes layout coverage with legibility; retain both historical gates.
- **Dresden accession (22):** SLUB's public OAI-PMH response indexes 302
  images. The cover and physical pages 243–245 (labels 240–242) were acquired.
  Two isolated Sol readers returned 22 grids. Their first index-based join
  was invalid because page traversal differed and reader A confused the
  opening chapter with book IV. Preserve this zero-target primary result.
- **Source-keyed collation:** a fresh Sol source-only locator audit establishes
  columns and headings. Its map was committed before post hoc scoring.
  All 22 row-length vectors match; 926/935 letters agree, eight conflict and
  one is unknown. Two row lists remain non-square. Ten Mathers joins pass;
  4/2 and 4/3 supply 72 agreed readings absent from Mathers.
- **Prediction diagnostic:** symmetry 22/22 borders, all 50 interiors abstained;
  class 27/50 interiors; class/chapter letters 11/50 versus global 10/50.
  No whole target recovered. This is post hoc, two adjacent grids, no A/B
  verdict. It does not establish historical free choice.

- **Construction types (23):** no seed-closed type (H26 weakened, calibrated;
  post hoc estimator correction recorded). APPARET is z 1.94, not extreme.
- **Square palette (24):** squares do not reuse their own interior letters
  (H27 weakened). Frozen palette predictions never differ from class mode on
  249 witness target orbits; the witness extraction reproduces 349/193/50.
- **Prior work:** Kollatsch's 2024 draft states the vowel/consonant alternation
  qualitatively (pp. 22–23). A bounded literature check found no controlled
  statistics on these squares; Reeds on Soyga is the method precedent.

Start with [the readable source packet](analysis/22-dresden-witness-pilot/COLLATION.md)
and [experiment 22's method/results](analysis/22-dresden-witness-pilot/README.md).
The failed initial output and all raw readings are retained alongside the
post hoc files. Canon and H16/H24 now distinguish observations from proposed
causes. The catalog restores solvable 3; failed predictors did not justify 2.

## Next bounded step

Proposed to Greg, awaiting his scale decision: a blind test of the frozen
predictions (experiments 13, 20, 24) on **all unopened Book IV pages, physical
246–297** (52 pages), as the confirmatory core of a paper. Before any page is
opened, freeze a pre-registration of expected accuracies with intervals
(symmetry, class, letter models) so the recipe can fail. If the scale is not
approved, the fallback is the three-page step below. Do not enlarge experiment
22 or reuse its pages as unseen.

1. Freeze that cohort, source URLs/hashes and unchanged prediction files.
   Record the alignment policy and implementation before reader dispatch.
2. Use a source-only locator pass to identify every grid by physical page,
   column and within-column position. Keep book, chapter and item separate.
   Freeze the complete inventory; do not select grids by apparent model fit.
3. Give two fresh Sol readers the same per-grid images and stable locator
   worklist. No other witness, prediction or other reader output. Save literal
   uneven rows, uncertainty and blanks. Do not repair with symmetry.
4. Keep source alignment separate from letter prediction. If same numbering
   fails, list unmatched objects; a caption-based remapping needs its own
   predeclared rule. Do not optimize joins on hidden letters.
5. Report all inventory omissions and shape disagreements, then cell and
   whole-target/orbit coverage. Preserve literal I/J readings beside any
   normalized comparison. Compare with the same global baseline.

This is feasible without a paid image request. The new limit is reliable
transcription and cross-witness alignment, not access to N 111. A paleographic
review could settle the nine uncertain positions in the current packet;
leave them unknown until then. Do not infer a universal generator, noise or
free choice from another small cohort.

## Tools and verification

- `22-dresden-witness-pilot/access.py --fetch` restores only the original four
  cached images. Do not change its cohort for experiment 23. The pinned
  `sources/dresden-n111/page-index.json` holds all source image URLs.
- `score.py --check` reproduces the flawed initial index comparison.
  `posthoc.py --check` reproduces the corrected collation and readable packet.
  `audit_scorer.py --check` independently checks counts and orbit coverage.
- `test_score.py` and `test_posthoc.py`: 11 focused checks. Experiment 21's
  four comparison checks and its two `--check` commands also pass.
- The raw METS has original trailing whitespace. Preserve source bytes.
- The accession's protocol/images/predictions were frozen before reading;
  its original scorer implementation was written later. Do not overstate
  the freeze. The corrected source map was frozen before post hoc scoring.

## Exposure and other open questions

Main thread has seen Mathers, Dehn chapters 1–14, Warburg and the selected
Dresden packet. The locator agent saw only those three source images and
their manifest. Other Dresden manuscript pages remain unopened in this dive.
Shared manuscript ancestry and model-training exposure remain unknown.

H22's Greek test is still open. The earlier dictionary edition comparison,
Mathers print audit, ten excluded Mathers layouts and label 25/4 remain open.
HAB witness image access and Dresden N 161 are separate unresolved questions.
No push or external message was sent.

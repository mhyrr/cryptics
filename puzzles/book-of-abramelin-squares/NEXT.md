# NEXT — handoff for the next session

**Last session:** 2026-09-17, image acquisition (after `b0a59b9`)
**Where it stopped:** the dictionary image packet is acquired and tracked in
`sources/period-dictionary/` (28 native-resolution full pages, SOURCES.tsv,
MANIFEST.sha256, README with the locator table). Nothing transcribed or
compared yet. Experiment 05 still has only its source audit, protocol and
synthetic machinery. H7/H12 open.

## Do first

1. Read `sources/period-dictionary/README.md`. Transcribe the six entries from
   the images, separately from Kollatsch's quotations, keeping uncertain
   letters uncertain (the "melabbed" bet/mem in Vnterweiſer, scan 105; Hebrew
   points generally). Record raw readings and every normalization. Then, and
   only then, compare against `claims.json` and record the result here and in
   research.md. Note the 1596 "Vnderweiſer" (d) vs 1595 "Vnterweiſer" (t).
2. The alleged edition-specific Vnterweiſer error still needs an earlier
   comparison edition's title/imprint and full entry. Identify it from the
   bibliography (VD16) first; the BSB IIIF + hOCR route in research.md
   2026-09-17 is the reproducible way to fetch pages once an id is known.
3. Read SOURCE-AUDIT.md and PROTOCOL.md. Preselect a contiguous dictionary
   sample including misses (the same route yields any block of scans).
   Preserve originals and every normalization. Independently justify an
   interior placement, then freeze lexicon, captions, placements, masks,
   controls and code before scoring. Seed attribution alone cannot predict
   disjoint interior orbits. Do not invent fitted transformations.
4. Run the protocol's whole-orbit and interior-only tests, enumerating competing
   completions and reporting errors, abstentions, coverage and exact recovery
   against symmetry, frequency and shuffled controls. The 81 reused Mathers
   grids are internal evaluation, never blind validation.
5. Only after demonstrated inner-letter performance, audit exposure, raw
   readings, corrections, alignment and ancestry. Freeze incomplete-square
   predictions before inspecting new uncorrected German witness answers.

## What exists and what was verified

Experiments 01–04 are unchanged. Experiment 05 now has facsimiles of the six
entries on hand but no transcription, independent lexicon, historical
placement rule or historical score. PROTOCOL.md, claims.json, synthetic.json, freeze.json, solver
and generated results were not changed. Six tests pass; `run.py --check` under
`PYTHONHASHSEED=7919` verifies the preflight outputs. These are software checks.

No new source letters were exposed. Prior exposure remains: Book IV edition
pp. 138–142 and variants, structural-draft examples, Peterson variants, and
all 81 complete Mathers grids reused in earlier experiments. No new raw German
witness was read and no new historical predictions were issued.

## Named wall

**Independent justification of an interior lexical placement**, and, for the
error claim, an **earlier comparison edition**. The page-image wall is down;
the BSB service's native resolution leaves Hebrew vowel points marginal, and
nothing higher exists there.

Historical validation separately needs the Mathers print audit and raw German
witnesses. Keep the audit queue: ten excluded layouts, label 25/4 among chapter
24, frame disagreements, Dresden N 111 access and HAB facsimiles. A corrected
modern edition is not uncorrected witness truth. TK-005 remains open.

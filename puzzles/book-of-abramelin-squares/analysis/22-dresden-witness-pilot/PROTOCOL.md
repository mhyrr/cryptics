# 22 — Dresden N 111 accession and bounded collation pilot

Frozen 2026-09-21 before any square-bearing Dresden image is opened.
Greg requested the next steps using Sol subagents. The public SLUB OAI-PMH
endpoint returned METS for `id364474017`; its title and shelfmark identify
Mscr.Dresd.N.111. Only physical image 1 (the cover) has been inspected so far.

## Cohort

Take physical images **243, 244 and 245**, without inspecting them first.
The 2020 [source-location note](https://solascendans.com/2020/05/15/abramelin-musings-the-dresden-manuscript/)+(POPULAR, locator lead only) links Book IV's start to physical page 243.
PRIMARY METS labels these images 240, 241 and 242. Selection is a consecutive
opening pilot, not a random sample or the whole manuscript. Do not expand it
based on the result. Record partial grids, unreadable text and missing labels.

## Reading

Two independent Sol readers see the same three full-resolution source pages,
no other witness transcriptions, no predictions, no other reader output.
Transcribe all letter grids on the pages literally, with image-local top-to-
bottom identifiers. Preserve source numbers and chapter labels separately;
uncertain identifiers are null. Capture captions only as printed, without
semantic interpretation or dictionary lookup. Full pages expose captions to
the readers; this is collation, not a new caption-nomination test.

No symmetry repair, lexical repair or completions. Uppercase Latin letters,
`?` for uncertain letter, `.` for explicitly empty grid cell. Preserve J/I in
raw readings; compare both literal and predeclared J-to-I-normalized copies.
Uneven rows are retained. Grids cut off by the cohort stay partial.

## Comparison

1. Verify source hashes. Compare readers by physical page and image-local
   grid index. Require identical row lengths before comparing positions.
   Report disagreements and unknowns, never replace them by a model guess.
2. Give every agreed reading a witness, physical page, printed page label,
   source URL and grid locator. This is a first collation packet, not a
   corrected text or an all-witness edition.
3. If both readers independently agree on a printed chapter and number,
   compare that identifier with Mathers, using the already frozen experiment
   20 same-size/visible-agreement gate. Do not choose targets by hidden cells,
   modify models or tune an alignment. No confident source number means no
   primary Mathers score. Secondary possible joins are listed, not scored.
4. Count letters absent in Mathers only when a valid primary join exists.
   Use existing experiment 13/20 predictions unchanged; report abstentions,
   disagreements and whole-square/orbit coverage. Under 50 evaluated interior
   positions gives no A/B criterion verdict. Counts are not independent trials.
5. This manuscript is newly accessed in this project, but shared ancestry and
   model training exposure remain unknown. Do not equate fresh access with
   historical independence. The pilot cannot prove free interior choice.

## Sources and boundaries

PRIMARY: [SLUB manuscript record](https://digital.slub-dresden.de/id364474017),
[published open-data interface](https://www.slub-dresden.de/mitmachen/open-source-open-data),
and the pinned METS response in `sources/dresden-n111/`. The web viewer still
returns a JavaScript challenge; the published machine interface and image URLs
work without that viewer. No challenge was solved or security setting changed.
No message, purchase or new software installation is needed.

Original experiment 20's prediction hashes, source hashes and this protocol
are committed before the readers run. Later corrections receive a new note.

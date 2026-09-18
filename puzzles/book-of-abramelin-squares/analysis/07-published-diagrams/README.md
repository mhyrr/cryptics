# 07 — Published diagram verification

2026-09-17, resumed from `3815688`. Question: does the experiment 06
rows-as-polygrams convention agree with an actual published figure?
Scope fixed before comparison: its same ten discovery examples; retain every
letter and case, compare exact rows and the previously nominated paths. Do not
transpose or correct either source. Experiments 05 and 06 remain unchanged.

## Sources and browser observations

- **Edited PRIMARY:** [2021 square compilation](https://works.hcommons.org/records/xep4n-asx54),
  DOI [10.17613/3hfq-9a74](https://doi.org/10.17613/3hfq-9a74),
  `buchstabenquadrate.pdf`, 36 PDF pages. Visually inspected pp. 1–4 in the
  public PDF viewer. Page 1 states that editorial conjectures are included.
  The record displays MD5 `9b000871d94ef6ecc61e044bfe730ee7`; this is repository
  metadata, not a checksum we computed. Exact figure locators and separately
  recorded rows are in `readings.json`.
- **Edited PRIMARY / CLAIMANT apparatus:** [second edition preview](https://works.hcommons.org/records/pd060-xcq09),
  DOI [10.17613/8dq6-6m31](https://doi.org/10.17613/8dq6-6m31),
  `lp_wp.pdf`, 128 PDF pages. Printed pp. 138–142 are PDF pages 120–124.
  Inspected their rendered sequences and text layer. These pages print
  polygram lists, not square diagrams. The note at 140,8 specifies the middle
  column for BEHEMOT; the list at 141,8 gives the wax sequence beginning NECOT.
- **CLAIMANT, access still blocked:** [structural draft](https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_).
  “See full PDF” opened an account prompt. The author's visible profile
  download link also led to signup. No account was created or terms accepted.
  Draft pp. 4, 7–10 and 35–41 remain visually unverified.
- **PRIMARY bibliographic observation:** the [author's Academia profile](https://independent.academia.edu/RickArneKollatsch)
  and [Knowledge Commons author results](https://works.hcommons.org/search?q=metadata.creators.person_or_org.name:%22Kollatsch,%20Rick-Arne%22)
  did not list separate lexical/name installments in the displayed results.
  This is a bounded access finding, not proof that they do not exist.

Browser access was first verified on example.com. All research navigation and
visual inspection used the in-app browser. Screenshots were inspected in the
session, but no PDF or screenshot files were saved into this repository.
The public record URLs, viewer URL, file names and page locators are retained
for a repeat inspection. No raw manuscript was opened. The browser text layer
also exposed adjacent compilation figures on pp. 1–5; treat those pages as
discovery-exposed, never as future blind test data. Edition navigation exposed
printed pp. 174–175 (prayer text), in addition to the already exposed 138–142.

## Result and limit

The script reports **10/10 exact case-sensitive row agreements** between the
new compilation readings and experiment 06. BEHEMOT occupies column 4 in
Qu. 3.2 (with uppercase E); TSIPPOR occupies row 4 in Qu. 3.4. NECOT is row 1
in Qu. 4.5. RAKKIA and MAIAM occupy row 3 in Qu. 1.9 and Qu. 4.8.
The script reports each previously nominated path separately.

This verifies the orientation against the **compilation**, not the structural
draft. We cannot yet tell whether that draft transposes its BEHEMOT figure,
mislabels a column as a row, or was misrepresented by extraction. Its wax
figure remains unchecked too. No source reading is replaced.

Agreement does not constitute independent historical validation: both edited
publications are Kollatsch's work and include conjectures. No predictive rule,
lexicon sample, hidden-orbit score or incomplete-square prediction is added.
The construction choices in experiment 06 EVIDENCE.md remain open. Access to
the draft would settle its specific orientation question; it would not by
itself supply the missing rule for choosing words, spelling changes and paths.

## Reproduce

From the repository root, Python standard library:

```sh
python3 puzzles/book-of-abramelin-squares/analysis/07-published-diagrams/compare.py
python3 puzzles/book-of-abramelin-squares/analysis/07-published-diagrams/compare.py --check
```

The check verifies saved transcription comparisons and input hashes. It does
not automate or certify the visual reading; repeat that using the cited pages.

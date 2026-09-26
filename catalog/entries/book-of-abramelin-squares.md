+++
title = "The word squares of the Book of Abramelin"
slug = "book-of-abramelin-squares"
kind = "constructed-text"
era = "early 17th-century witnesses; Mathers edition 1898"
origin = "German manuscript tradition, with translations and later redactions"
language = "German context; Latin-letter squares"
status = "partial"
confidence = "medium"
digitized = "https://www.esotericarchives.com/abramelin/abramelin.htm"
tags = ["magic", "word-square", "combinatorial", "Hebrew", "Mathers", "collation"]

[scores]
mystery = 3
material = 3
solvable = 3
compute = 3
verifiable = 4
crowding = 3
+++

# The word squares of the Book of Abramelin

## What it is
Abramelin's final book contains letter arrays associated with named magical
purposes. The question here is their textual construction and transmission.
Mathers's 1898 translation presents complete squares, borders, gnomons and
irregular arrangements; his own notes already distinguish those classes.
PRIMARY — [Mathers, Book III and notes, in Peterson's digital edition](https://www.esotericarchives.com/abramelin/abramelin.htm).

## What is unsolved
Whether explicit construction rules can predict uncorrected witness readings beyond the symmetries and lexical sources already described in the literature.
Distinguish three tasks: describe transmitted patterns, reconstruct damaged
readings, and explain the choice of independent letters. Agreement with a
second witness does not alone establish the original compositional process.

The [deep dive](../../puzzles/book-of-abramelin-squares/canon.md) has
characterized several constraints, with substantial limits:

- **Lexical sources.** Caption-guided dictionary nominations retrieve a subset
  of seed words above controls. The stored Warburg print comparison gives 17
  same-number hits against 3.5; 21 earlier selected hits were checked on
  dictionary images. This does not identify a universal selector or prove
  dependence on one edition. PRIMARY — [dictionary](https://www.digitale-sammlungen.de/de/view/bsb11762465),
  [Warburg print](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf);
  [experiments 14–20](../../puzzles/book-of-abramelin-squares/README.md).
- **Borders and interiors.** Symmetry predicts many missing border letters.
  Interior class predictions outperform exact-letter models in the aggregate
  Dehn/Warburg tests, but exact reconstruction remains weak. Exposure,
  editorial intervention, alignment and transcription limit those tests.
  A [Sol audit](../../puzzles/book-of-abramelin-squares/analysis/21-sol-reading-audit/README.md)
  reproduces the Warburg scores and retains unresolved cross-model reading
  conflicts. Its two gates measure different mixtures of layout and legibility.
- **Manuscript evidence.** Dresden N 111 is now accessible through SLUB's
  public metadata and image interface. A three-page pilot yields 22 source-keyed
  grids. Two supply 72 agreed readings at Mathers blanks: symmetry 22/22 border
  letters, interior class 27/50, exact letters 11/50 versus 10/50 baseline.
  These are post hoc collation diagnostics on two neighbouring grids, not a
  confirmatory construction verdict. PRIMARY — [SLUB record](https://digital.slub-dresden.de/id364474017);
  [experiment 22](../../puzzles/book-of-abramelin-squares/analysis/22-dresden-witness-pilot/README.md).

No complete generator has been recovered. Failure of the tested families does
not establish freely chosen letters or show that no determinate construction
exists. Further progress requires reliable source collation and fixed
cross-witness alignment before another prediction test.

## What survives
The old six-witness inventory was inadequate. Kollatsch's September 2025 list
reports 32 historical manuscripts in 23 libraries, including fragments and
translations; this is not a count of complete square-bearing witnesses.
PRIMARY bibliographic inventory — [updated list](https://www.academia.edu/144258692/Aktualisierte_Liste_historischer_Handschriften_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_).

HAB catalogs Wolfenbüttel **47.13 Aug. 4°** and **10.1 b Aug. 2°**. Both retrieved
records offer digitization requests; neither exposed a direct manuscript
facsimile. The latter is described as an apparent copy of the former.
PRIMARY — [47.13](https://diglib.hab.de/?db=mss&list=ms&id=47-13-aug-4f),
[10.1 b](https://diglib.hab.de/?db=mss&list=ms&id=10-1-b-aug-2f).

Dresden N 111's viewer returned a JavaScript challenge, but its public OAI-PMH
metadata and original image URLs worked on 2026-09-21. The pinned METS contains
302 physical image records; four images were acquired, including the three-page
square pilot. N 161's open imaging status remains unresolved. PRIMARY —
[N 111 record](https://digital.slub-dresden.de/id364474017),
[SLUB open-data interface](https://www.slub-dresden.de/mitmachen/open-source-open-data),
[SLUB catalog, N 161](https://kalliope-verbund.info/findingaid?fa.id=DE-611-BF-41898&fq=ead.corp.index%3A%28%22Dresdner+Liedertafel+%281839-%29%22%29&htmlFull=false&lang=de&lastparam=true).

## Prior attempts and current consensus
**The first catalog pass overstated the absence of prior work.** Kollatsch's
2021 historical edition supplies a text based on Wolfenbüttel 47.13. His separate
257-square compilation incorporates conjectures and cannot be an untouched
test witness. PRIMARY critical edition and editorial description —
[edition](https://www.academia.edu/45180953/Edition_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_Hamburg_2021_),
[publication list](https://independent.academia.edu/RickArneKollatsch).

His November 2024 draft studies whole-square and frame symmetries, then discusses
proposed corrections and their uncertainty. The elementary structural approach
has been tried. CLAIMANT — research draft, not independently replicated here:
[symmetry study](https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_).

Kollatsch traces lexical material to a multilingual dictionary of 1595/1596.
The cited dictionary entries and errors should be replicated before using this
as an independently established derivation. CLAIMANT —
[2021 account](https://www.academia.edu/55141247/Abraham_of_Worms_the_disciple_of_Abramelin_the_Mage_).
Heidrick offers a Hebrew interpretation while expressly disavowing scholarly
status for his method. CLAIMANT — [Heidrick](https://hermetic.com/heidrick/mq/5).

Do not infer a field-wide consensus or exhaustive review.
`partial` reflects existing structural and lexical research; it does not
certify a universal generator or accept a particular reconstructed text.

## What a solution would have to do
1. Publish per-cell witness transcriptions with image locators, keeping source
   readings, uncertainty and editorial conjecture separate.
2. Specify rules before inspecting validation targets. Align by purpose and
   text, accounting for changed numbering and orientation.
3. Predict held-out readings beyond elementary symmetry baselines. Report
   coverage, wrong predictions and abstentions. Common ancestry, duplicates,
   and already-exposed variants limit independence.
4. Explain the choice of independent letters if claiming a generator; constraint completion
   alone does not do this.
5. Test language claims against declared controls. A model's recognition of a
   plausible word is not a statistical result.

## Why the scores
Reviewed 2026-09-26 from the deep dive and source accession.
- **mystery 3:** lexical sourcing and symmetry partly characterize the text;
  independent interior-letter choices remain unexplained.
- **material 3:** substantial digital text, edited readings and a German print
  exist. Dresden N 111 images are accessible, but its collation is a small
  pilot and access across the German witnesses remains partial.
- **solvable 3, restored from 2:** whether every independent letter had a
  determinate construction remains open. The earlier reduction treated failed
  predictors as evidence that no rule exists; the tests do not warrant that.
- **compute 3:** code supports source comparison, alignment checks and bounded
  hypothesis tests. A total verifier for historical construction is absent;
  the tested families have not delivered an interior reconstruction.
- **verifiable 4:** frozen predictions can be checked against source readings,
  with exposure, ancestry and editorial intervention accounted for.
- **crowding 3:** Kollatsch's edition, symmetry study and dictionary
  identification establish prior work; the local dive adds controlled tests.

## Sources
- PRIMARY — Mathers, 1898, Book III, mediated by Peterson's digital transcription. https://www.esotericarchives.com/abramelin/abramelin.htm
- PRIMARY — HAB catalog, Cod. Guelf. 47.13 Aug. 4°. https://diglib.hab.de/?db=mss&list=ms&id=47-13-aug-4f
- PRIMARY — Kollatsch, historical edition, 2021. https://www.academia.edu/45180953/Edition_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_Hamburg_2021_
- CLAIMANT — Kollatsch, symmetry research draft, November 2024. https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_

Tiered sources are linked at claims above. The local research record is
[puzzles/book-of-abramelin-squares/](../../puzzles/book-of-abramelin-squares/README.md).
Dresden accession: 2026-09-21. Source and score review: 2026-09-26.

## Unverified claims
- Accuracy of every exported cell against the 1898 print and Arsenal manuscript.
- Edition-specific dependence on the 1595/1596 dictionary (no earlier edition compared); Kollatsch's proposed corrections.
- Full coverage of any published all-witness collation.
- Open image access for Wolfenbüttel 47.13, 10.1 b, and Dresden N 161.
- Number of complete squares and blanks in each historical witness.
- Novelty of the local structural results.
- The first pass's claims about Skinner's apparatus, Scholem's assessment,
  and authorial attribution were not independently verified here; they no
  longer support the scores.

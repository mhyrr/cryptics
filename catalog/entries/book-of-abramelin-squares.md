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
compute = 4
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

The [first local experiment](../../puzzles/book-of-abramelin-squares/analysis/01-mathers-structure/RESULTS.md)
extracts 242 records from a digital Mathers transmission, retaining 232
unambiguous layouts: 81 complete and 151 incomplete. Ten require layout checks.
Transpose symmetry holds in 69 complete grids; transpose plus half-turn in 55.
None fits the tested cyclic or boundary-arithmetic generators. These are
measurements of the export, not a critical edition or proof that no generator
exists. PRIMARY input — [Peterson's Mathers transcription](https://www.esotericarchives.com/abramelin/abramelin.htm);
method and full output in the linked experiment.

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

Dresden N 111 has a linked digital viewer, but it returned a JavaScript challenge
on 2026-09-16. N 161 appears in the SLUB holdings catalog; its open imaging status
remains unresolved. PRIMARY — [N 111 viewer](https://digital.slub-dresden.de/werkansicht/dlf/65720/1/),
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
4. Explain free letter choices if claiming a generator; constraint completion
   alone does not do this.
5. Test language claims against declared controls. A model's recognition of a
   plausible word is not a statistical result.

## Why the scores
- **mystery 3:** structures are described; reconstruction and composition remain
  separate questions. See the 2024 draft and local experiment above.
- **material 3:** digital English text and a modern German edition are accessible;
  direct witness access and per-cell provenance remain partial.
- **solvable 3:** structure is measurable, but a unique original or universal
  generator has not been established by this audit.
- **compute 4, reduced from 5:** code eliminates specified families and produces
  conditional fills; independent verification data is not ready.
- **verifiable 4:** uncorrected held-out letters offer strong checks after
  alignment and editorial history are controlled; not yet a total verifier.
- **crowding 3, reduced from 4:** a dedicated edition and explicit symmetry study
  cover the obvious structural approach. No novelty claim is made.

## Sources
- PRIMARY — Mathers, 1898, Book III, mediated by Peterson's digital transcription. https://www.esotericarchives.com/abramelin/abramelin.htm
- PRIMARY — HAB catalog, Cod. Guelf. 47.13 Aug. 4°. https://diglib.hab.de/?db=mss&list=ms&id=47-13-aug-4f
- PRIMARY — Kollatsch, historical edition, 2021. https://www.academia.edu/45180953/Edition_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_Hamburg_2021_
- CLAIMANT — Kollatsch, symmetry research draft, November 2024. https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_

Tiered sources are linked at claims above. The local research record is
[puzzles/book-of-abramelin-squares/](../../puzzles/book-of-abramelin-squares/README.md).
Access audit: 2026-09-16.

## Unverified claims
- Accuracy of every exported cell against the 1898 print and Arsenal manuscript.
- Independent replication of the dictionary derivation and proposed corrections.
- Full coverage of any published all-witness collation.
- Open image access for Wolfenbüttel 47.13, 10.1 b, and Dresden N 161.
- Number of complete squares and blanks in each historical witness.
- Novelty of the local structural results.
- The first pass's claims about Skinner's apparatus, Scholem's assessment,
  and authorial attribution were not independently verified here; they no
  longer support the scores.

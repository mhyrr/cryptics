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
solvable = 2
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

The [deep dive](../../puzzles/book-of-abramelin-squares/canon.md) ended on
2026-09-20 with the construction characterized and a wall named. In the pinned
Mathers export (232 analyzable layouts, 81 complete) and two further witnesses:

- **Seeds.** Caption subjects, looked up as German headwords in the Frankfurt
  *Sylvae quinquelinguis* of 1595/1596, give the top-row word from the printed
  Hebrew transliterations. On the 1853 German print, where captions and
  squares share one numbering, caption k retrieves the seed of square k 17
  times against a within-chapter control of 3.5. Twenty-one such entries were
  read on the dictionary's page images. An exploratory count attributes about
  45 % of top rows to the dictionary. PRIMARY — [dictionary, 1596 volume](https://www.digitale-sammlungen.de/de/view/bsb11762465),
  [Warburg print](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf); experiments
  [14](../../puzzles/book-of-abramelin-squares/analysis/14-caption-seed-test/README.md),
  [19](../../puzzles/book-of-abramelin-squares/analysis/19-image-reads/README.md),
  [20](../../puzzles/book-of-abramelin-squares/analysis/20-warburg-witness/README.md).
- **Borders.** Transpose plus half-turn symmetry, frozen beforehand, fills 83
  of 90 missing border cells on Dehn's readings and 101 of 120 on the print.
- **Interiors.** Letters alternate vowel and consonant down from the seed
  (about 80 % on unseen cells). The letter itself carries 2.9 bits per
  symmetry orbit and no tested context predicts it: best frozen model 32 % on
  Dehn, 23 % on the print. [Experiment 16](../../puzzles/book-of-abramelin-squares/analysis/16-interior-freedom/README.md).

What remains unsolved is the original reading of every interior the witnesses
leave blank or disagree on. On present evidence that cannot be computed; it
needs collation of the German manuscripts. Whether the interior letters were
freely chosen cannot be proven, only left unrefuted. The Warburg scores pass
the gate frozen with them and fail a stricter gate written by a parallel
review before the read, for a reason of print format; both are in experiment 20.

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
Re-scored 2026-09-20 from the deep dive.
- **mystery 3:** resolved in outline (source of seeds, symmetry, filler); the
  residue is the lost interior readings and an unprovable claim of free choice.
- **material 3:** English text, Dehn readings and one German print are usable;
  the German manuscripts are not openly imaged and no per-cell collation exists.
- **solvable 2, reduced from 3:** the seed half had a determinate source and
  it is found. For the interior letters the best evidence favours no rule to
  recover: five frozen tests and two further witnesses found none.
- **compute 3, reduced from 4:** computation settled the sub-questions it
  could. What is left is collation, where code assists and cannot decide.
- **verifiable 4:** a collated reading can be checked against further
  witnesses, and the frozen models give border and class checks.
- **crowding 3:** Kollatsch's edition, symmetry study and dictionary
  identification cover the ground; this dive adds controls and scale.

## Sources
- PRIMARY — Mathers, 1898, Book III, mediated by Peterson's digital transcription. https://www.esotericarchives.com/abramelin/abramelin.htm
- PRIMARY — HAB catalog, Cod. Guelf. 47.13 Aug. 4°. https://diglib.hab.de/?db=mss&list=ms&id=47-13-aug-4f
- PRIMARY — Kollatsch, historical edition, 2021. https://www.academia.edu/45180953/Edition_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_Hamburg_2021_
- CLAIMANT — Kollatsch, symmetry research draft, November 2024. https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_

Tiered sources are linked at claims above. The local research record is
[puzzles/book-of-abramelin-squares/](../../puzzles/book-of-abramelin-squares/README.md).
Access audit: 2026-09-16. Re-scored from the dive: 2026-09-20.

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

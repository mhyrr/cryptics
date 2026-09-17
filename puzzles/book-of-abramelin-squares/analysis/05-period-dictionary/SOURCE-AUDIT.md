# Dictionary source audit — 2026-09-17

## What was actually retrieved

**CLAIMANT:** Kollatsch's [2021 English account](https://www.academia.edu/55141247/Abraham_of_Worms_the_disciple_of_Abramelin_the_Mage_), p. 3, notes 7–8, identifies Heinrich
Decimator's *Sylvae quinquelinguis*, with Hebrew by Valentin Schindler and
revision by Zacharias Palthenius, Frankfurt, Basse, 1595/1596. He argues that
shared errors establish dependence. This has not been independently replicated.
He describes purpose words, sometimes also spirit names, among mostly
nonlexical sequences; this is not an all-rows word-square claim.

**CLAIMANT / edited PRIMARY text:** the [2021 second-edition preview](https://www.academia.edu/45180953/Edition_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_Hamburg_2021_)
was retrieved as extracted text. Introduction XV–XVI, note 20, distinguishes
part I's A–S and T–Z divisions from the proper-name part II. The accessible
Book IV sample is pp. 138–142, not the complete apparatus through p. 173.
`claims.json` records six short cited spelling pairs and their headword context.
The instructor entry is a candidate semantic-error check. Sky, water and wax
require changes beyond case folding in the cited correspondences. The preview
also discusses inserted names; it gives no general placement algorithm.

**CLAIMANT:** the [November 2024 draft](https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_)
publishes the structural part and defers lexical/name analysis. It works from
the modern edition, not an untouched witness test set.

## Independent access findings

**PRIMARY catalogue metadata:** [BSB/Bamberg record via DDB](https://www.deutsche-digitale-bibliothek.de/item/4JDRCQ4NAG6QNTCR3GANJZSQER4AE4HM)
identifies the 1596 Frankfurt volume: VD16 D 356, Bamberg Phil.o.339,
URN `urn:nbn:de:bvb:12-bsb11762465-5`, [viewer](https://www.digitale-sammlungen.de/de/view/bsb11762465).
The [1595 continuation record](https://www.deutsche-digitale-bibliothek.de/item/VDGSYVMVFXW3N5BXE6VBLFTQAJTS5ENL)
identifies VD16 D 354, Munich Polygl.37-2#Beibd.1,
URN `urn:nbn:de:bvb:12-bsb10314207-6`, [viewer](https://www.digitale-sammlungen.de/en/view/bsb10314207).
These are catalogue checks, not checks of printed letters.

**PRIMARY digitization metadata:** Google Books lists [1596 scan jkY8AAAAcAAJ](https://books.google.com/books/about/Sylvae_Quinquelinguis_Vocabularum_Et_Phr.html?id=jkY8AAAAcAAJ)
and [1596 scan LPyVAQ1q89cC](https://books.google.com/books?id=LPyVAQ1q89cC), the latter
from BSB Polygl.202 p-1. Neither returned readable page images in this session.

| Route attempted | Observed outcome | What it establishes |
|---|---|---|
| Academia English account, edition preview, structural draft | Extracted text retrieved | Claims and locators can be audited; no original dictionary letters |
| DOI `10.17613/8dq6-6m31` and Academia download link | Web retrieval error | Full edition not acquired |
| DDB records | Search-index text available; direct opens failed | Bibliographic locators, not facsimiles |
| BSB viewers and Bamberg URN resolver | Web internal/safe-open errors | Access failure in this tool, not absence of scans |
| BSB IIIF manifests for bsb11762465 and exploratory bsb10314206 | Web internal errors | No manifest or image inspected; the second identifier is unverified |
| Google Books metadata, preview and search-within route | Metadata only; preview/search retrieval errors | No spelling verified |
| Shell public DOI request with curl, then required escalated retry | Both rejected by global command policy before execution | No download; no alternate shell client used to bypass the restriction |

No manuscript/library request was sent. No paid source was acquired. No
dictionary facsimile has been inspected. The missing input is **legible,
edition-identified entry images with enough surrounding text to establish
entry boundaries**, not a missing modern translation.

## Independent findings versus claims

The computed audit in `results.json` checks literal equality of the *quoted*
spellings after the stated normalization. It cannot authenticate those
spellings against the dictionary. The distinction matters: using a claim's
own examples to build a lexicon and then recovering those examples would
test recognition of exposed answers.

A shared ordinary word would not by itself identify this edition as the
source. The proposed characteristic error needs checking in both the claimed
edition and an earlier comparison edition. Neither is done here. Context must
also distinguish a printed error from an obsolete gloss, an inflected form,
and a transcription error. We have not adjudicated those possibilities.

The construction class to investigate is therefore **selected lexical material
plus positional/symmetry constraints**. Which paths, which transformations and
which remaining letters are prescribed is unresolved. There is no evidence
here that justifies treating every row as a word or allowing approximate matches.

## Exposure and ancestry audit

The retrieved preview displayed the Book IV grids on pp. 138–142, including
editorial apparatus and variants. Treat all of them as exposed discovery data;
this includes water imagery and cannot be mapped to Mathers numbers by number
alone. The earlier sessions already exposed Peterson's variants and examples
in the structural draft. Conservatively treat every example in that draft as
exposed too. All 81 complete Mathers grids were reused in prior experiments.

No new raw German witness was read. The preview is an edition of W1 with
interventions, not W1 facsimile truth. Prior canon records a dependent HAB copy.
No cell-by-cell ancestry, correction or alignment audit has been completed.
Do not claim a future match to this preview is blind or independent.

## Next input and decision

Obtain the title pages and the six headword images in `claims.json`, including
adjacent entries; obtain a comparison-edition image for the suspected error.
Then preselect a contiguous dictionary block without consulting new square
answers. If this only validates seed selection, retain that finding and test
fixed interior placements separately. An independently transcribed word at a
predeclared interior path is the next experiment worth running. A negative
result would concern that recipe and lexicon, not randomness of the text.

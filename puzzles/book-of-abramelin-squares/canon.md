# Canon — what we believe now

## Evidence and prior work

- **Established (bibliographic):** Rick-Arne Kollatsch published a 2021 edition
  and lists a draft devoted to square symmetry. His separate 257-square
  compilation includes conjectural corrections. It cannot serve as an untouched
  manuscript test set. PRIMARY — [author's publication list](https://independent.academia.edu/RickArneKollatsch).
- **Established (reported research, not independently replicated here):**
  Kollatsch identifies the Frankfurt Palthenius/Basse *Sylvae quinquelinguis*
  of 1595/1596, part I, as the lexical source. CLAIMANT — [2021 account, p. 3](https://www.academia.edu/55141247/Abraham_of_Worms_the_disciple_of_Abramelin_the_Mage_).
  The [experiment 05 source audit](analysis/05-period-dictionary/SOURCE-AUDIT.md)
  distinguishes his correspondences from independent findings. The six cited
  Latin dictionary readings have now been checked on facsimiles; dependence
  on this specific edition remains unestablished.
- **Established (reported inventory):** His September 2025 list reports 32
  historical manuscripts in 23 libraries, including fragments and translations.
  This replaces the catalog's six-witness framing, but is not a count of
  complete square corpora. PRIMARY — [updated inventory](https://www.academia.edu/144258692/Aktualisierte_Liste_historischer_Handschriften_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_).
- **Established (prior interpretation exists):** Heidrick gives a Hebrew
  interpretation but expressly describes it as a meditation method rather than
  scholarship. CLAIMANT — [Heidrick](https://hermetic.com/heidrick/mq/5).

## Witness access, checked 2026-09-16

- **Established:** HAB's record identifies Cod. Guelf. 47.13 Aug. 4° and
  provides a digitization-request option; no manuscript facsimile link was
  found in the retrieved record. This does not prove no images exist.
  PRIMARY — [HAB record](https://diglib.hab.de/?db=mss&list=ms&id=47-13-aug-4f).
- **Established:** The other HAB shelfmark is **10.1 b Aug. 2°**. Its catalog
  description calls it an apparent copy of 47.13. It likewise exposes a
  digitization-request option, not a facsimile in the retrieved page.
  PRIMARY — [HAB record](https://diglib.hab.de/?db=mss&list=ms&id=10-1-b-aug-2f).
- **Established (access state only):** The linked Dresden N 111 viewer returns
  an Anubis JavaScript challenge to the web tool. No manuscript letters have
  been inspected. PRIMARY — [SLUB viewer](https://digital.slub-dresden.de/werkansicht/dlf/65720/1/).

## Structure and statistics

**Established for the pinned export only:** [Experiment 01](analysis/01-mathers-structure/RESULTS.md)
extracts 242 records and analyzes 232 unambiguous layouts: 81 complete and 151
incomplete, containing 5,244 letters and 3,310 blanks. Ten layouts are excluded.
The source is PRIMARY text mediated by [Peterson's transcription](https://www.esotericarchives.com/abramelin/abramelin.htm)
and the web tool; the export is not collated to the 1898 print.

**Established for that sample:** 69 complete grids satisfy transpose symmetry,
55 satisfy transpose plus half-turn. No complete grid fits the tested cyclic
row or four boundary-arithmetic families. These are exact-test failures, not
evidence that the historical text is noise. Source and method: experiment above.

**Established, conditional:** combined symmetry forces 1,064 blank cells across
111 compatible incomplete grids. In MAIAM (25/3), four free letter orbits remain:
456,976 completions over A–Z. No lexical constraints were imposed. The other
symmetry families overlap; their fill counts must not be summed. Source: same
experiment, `results.json` and `predictions.json`.

**Established method limitation:** when complete grids are masked to top row
plus left column, transpose alone predicts no hidden cells. The combined rule
predicts 696 of 2,136 hidden cells, of which 615 match and 81 fail. This internal
diagnostic is not a German-witness test. It filters only on visible conflicts.
Source: same experiment, `masked_complete_grid_diagnostic`.


## Stress tests of three further attacks

**Established for the same digital sample:** experiments 02–04 use 81 complete
squares in five fixed folds, with identical masks and declared controls. The
[ten-attack plan](ATTACKS.md) precedes the implementations; the generated
[combined report](STRESS-TESTS.md) links every method and per-cell audit.
These computations are evidence about the pinned digital data, not manuscript
readings. Source: PRIMARY text mediated by
[Peterson](https://www.esotericarchives.com/abramelin/abramelin.htm), as above.

**Established, limited capability:** independent frame fitting gets 555/591
scattered-cell predictions correct, versus 456/463 for strict whole-grid
symmetry. Coverage improves but exact task recovery falls from 30 to 18 of 81.
It cannot predict a wholly hidden symmetry orbit. It flags 12 letters in eight
unmodified digital grids; those are inspection candidates, not corrections.
Source: [experiment 02](analysis/02-frame-model/RESULTS.md) and its JSON audit.

**Established, weak reconstruction performance:** corpus-derived fragments get
2/10 predictions right when whole symmetry orbits are hidden. A learned local
rule gives 301/1,429 correct in boundary rollout, versus 262 correct for the
training-frequency baseline on the same cells; no complete target is recovered
and no confident prediction is made. The matched 55-grid symmetric subset
loses to that baseline. Sources: [03](analysis/03-fragment-transfer/RESULTS.md),
[04](analysis/04-local-recurrence/RESULTS.md), per-fold results in the combined report.

**Established test sensitivity, not Soyga replication:** standalone fragment
transfer recovers 320/320 planted motif centers. Nested recurrence selection and
confident rollout recover 3,920/3,920 planted interior letters. These synthetic
constructions are ours; their success does not show that an unknown Abramelin
rule would necessarily be found. Source: experiments 03–04.

## Period-dictionary investigation, 2026-09-17

**Established (PRIMARY facsimiles), 2026-09-17:** full-page images of the
title/imprint and the six target entries, with continuations and neighbours,
are tracked in [`sources/period-dictionary/`](sources/period-dictionary/README.md)
with a sources table and sha256 manifest. Both volumes are unpaginated;
locators are BSB viewer scan plus gathering signature. Himmel: 1596 scans
690–692 (Ss 2–4). Lehrer: 1596 scan 834 (between Ddd 3 and Ddd 4).
Vnterweiſer: 1595 scan 105 (Gggg 5). Wachs: 1595 scans 150–151. Warſager:
1595 scan 159. Waſſer: 1595 scans 160–161. The images are discovery-exposed
checks, not an independent lexicon. Scoped Latin transliteration excerpts and
comparisons now exist; no full multilingual transcription is claimed. Native
resolution leaves Hebrew vowel points marginal.

**Established for the inspected packet:** the six quoted dictionary Latin
transliterations occur in the cited entries. The reproducible
[facsimile audit](analysis/05-period-dictionary/FACSIMILE-FINDINGS.md) gives six
agreements with dictionary quotations, three with quoted square spellings under
the recorded operations. This is verification of selected examples, not a
reconstruction score. PRIMARY — [Lehrer](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=834),
[Vnterweiſer](https://www.digitale-sammlungen.de/en/view/bsb10314207?page=105),
[other primary locators](analysis/05-period-dictionary/facsimile-audit.json).
Lehrer prints `moreh, melammed, alluph`; Vnterweiſer prints `melabbed, moreh`.
The difference does not resolve the ambiguous Hebrew type or establish an
edition-specific error. All inspected pages are discovery-exposed.

**Established access finding:** catalogue records and the objects themselves
identify the 1596 A–S volume (VD16 D 356, `bsb11762465`) and 1595 T–Z
continuation (VD16 D 354, `bsb10314207`). PRIMARY metadata — [first volume](https://www.deutsche-digitale-bibliothek.de/item/4JDRCQ4NAG6QNTCR3GANJZSQER4AE4HM),
[continuation](https://www.deutsche-digitale-bibliothek.de/item/VDGSYVMVFXW3N5BXE6VBLFTQAJTS5ENL).
Earlier sessions could not retrieve page images; the 2026-09-17 acquisition
route (IIIF manifest, per-canvas hOCR, image verification) is in the research log.

**Established scope of the original preflight:** [experiment 05's original results](analysis/05-period-dictionary/RESULTS.md)
contain a quoted-spelling audit and artificial planted tests only. The later
facsimile audit above verifies source readings separately. Neither supplies
a historical reconstruction score or independent lexicon. Exact constraint
enumeration recovers nine planted inner letters; an alternative center word
leaves two completions and one abstention. Seed plus symmetry leaves 456,976
completions in that toy. These are computed facts about the fixture, not Abramelin.

**Methodological limit:** attributing a seed to a dictionary does not identify
the letters in disjoint interior symmetry orbits. A fixed interior lexical
placement must be tested separately (H12). Source-discovery examples and modern
edited German readings are exposed; see the source audit before any comparison.

## Construction evidence audit, 2026-09-17, after `bb87024`

**Established as reported placements, not predictions:** the accessible
apparatus includes inner lexical material, not only boundary seeds: rakkia
(139,6), behemot (140,8), tsippor (140,12), MAIAM (141,14), and opposed-word
interpretations at 141,2 and 141,4. CLAIMANT / edited PRIMARY —
[Kollatsch edition](https://www.academia.edu/45180953/Edition_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_Hamburg_2021_).
These pages were already discovery-exposed. The original experiment 06 pass
could not inspect diagrams. The follow-up below verifies the same sequences
against the public compilation, while the structural draft was still unchecked (resolved by experiment 09 below).

**Established for provisional extracted sequences only:**
[experiment 06](analysis/06-construction-evidence/README.md) records ten examples,
their captions, lexical alternatives, explicit paths, symmetry conflicts and
residual orbit coordinates. In its rows-as-polygrams convention, RAKKIA and
MAIAM reach inner orbits but fail exact comparison to independently read RAKIA
and MAIIM. Under TA, each quoted path still leaves two inner orbits free.
BEHEMOT occupies column 4, also confirmed in the compilation figure by the
follow-up below. The structural draft's extracted discussion says central row;
experiment 09 below now verifies the separate figure and prose discrepancies.
The beast/bird sequences conflict with all tested nonidentity global families.
These are discovery diagnostics, not historical performance or raw W1 truth.

**Construction limit:** the [structural draft](https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_)
(CLAIMANT), pp. 35–36, suggests a frame-filling order; pp. 37–41 discuss
name overlays. Neither supplies the missing independent letter assignments.
The prefatory leaf defers lexical/name installments. Exact central lines,
near-central expansion, opposed-word overlap and name overlays remain distinct
candidate constructions. No source-verified applicability selector, independent
evaluation lexicon, frozen historical recipe or historical score exists.
See [original evidence](analysis/06-construction-evidence/EVIDENCE.md) and the
[updated visual audit](analysis/07-published-diagrams/README.md).
Failure to find an adequate rule in the inspected material does not establish
that no rule exists. No randomness inference follows.

## Published diagram verification, 2026-09-17, after `3815688`

**Established for the edited compilation:** its figures on pp. 1–4 use the
rows recorded in experiment 06 for the ten selected examples. Experiment 07
computes 10/10 exact case-sensitive row agreements. BEHEMOT is in column 4,
TSIPPOR in row 4, and NECOT on the top row. RAKKIA and MAIAM are on row 3.
Edited PRIMARY — [Kollatsch compilation](https://works.hcommons.org/records/xep4n-asx54),
exact figures and comparison in [experiment 07](analysis/07-published-diagrams/README.md).
This is an edited-source transcription check, not independent witness evidence.

**Established access state:** the [edition DOI](https://doi.org/10.17613/8dq6-6m31)
now resolves to a public Knowledge Commons preview. Printed pp. 138–142 are
PDF pages 120–124 and were visually inspected. Its note 140,8 says middle
column. Academia's structural-draft viewer and profile download required an
account in that session; experiment 09 below resolves the figure access. Separate lexical/name
installments were not found in the displayed author publication lists. This
bounded search does not establish their nonexistence. Source locators and
exposure details are in experiment 07. No historical prediction gate passed.

## Supplied structural draft and overlay limits, 2026-09-18

CLAIMANT / edited examples — [draft](https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_), printed pp. 37–41, 46.
Direct image inspection confirms that the beast figure is untransposed but
has two cells different from its accompanying sequence and the compilation:
row 6 column 3 is blank rather than `r`; row 6 column 4 is `s` rather than `o`.
Its prose says row where the sequence gives column. The wax figure agrees
with the compilation. These source discrepancies are preserved in
[experiment 09](analysis/09-structural-draft/README.md).

Computed discovery results: capital-only erasure fails for dragon TA, beast T
and bird T, requiring at least 22, 14 and 6 further lowercase erasures.
NEBBELAH and GEBHINAH fit conditional T after erasure, but each retains three
free orbits, or 17,576 conditional A–Z completions. Neither recovers a changed
original letter. See [saved results](analysis/09-structural-draft/RESULTS.md).
These results describe edited examples under stated assumptions, not historical
accuracy. Experiment 08's different primary TA test remains separately recorded.

The author explicitly allows wider lowercase disruption and says names were
often derived from square letters (p. 46). This is a CLAIMANT explanation;
independent name inputs are not established. The requested PDF access wall is
resolved. Independent lexical selection and letter assignment remain open.

## Unverified claims

- Edition-specific errors and dependence on this particular dictionary edition;
  no earlier comparison edition has been acquired. The six cited Latin readings
  are verified, but ambiguous Hebrew and some adjacent alternatives remain
  unresolved; see the facsimile findings. No full multilingual transcription.
- A lexical rule assigning independent inner letters; inner word occurrences
  are verified in the selected compilation figures, but an answer-independent construction selector remains unverified. No complete word-square construction established.

- A single original generator; that failure to find one establishes noise.
- Completeness and per-cell accuracy of any online Mathers transcription.
- Open image access for Dresden N 161; its old catalog link failed, but a
  [SLUB holdings record](https://kalliope-verbund.info/findingaid?fa.id=DE-611-BF-41898&fq=ead.corp.index%3A%28%22Dresdner+Liedertafel+%281839-%29%22%29&htmlFull=false&lang=de&lastparam=true)
  (PRIMARY) confirms the shelfmark and German text.
- A modern all-witness collation's coverage and editorial independence.
- Novelty of the proposed computational characterization.

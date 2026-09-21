# Canon — what we believe now

## Current status, 2026-09-20, after the Warburg read

Experiments 12 to 20 are complete. The dive stops at end state B:
construction characterized, wall named. Caption-guided dictionary sourcing is
supported per square. Symmetry predicts border letters on two witnesses.
Vowel/consonant alternation predicts the class of interior letters; nothing
tested predicts the letter. No generator has been recovered. That the
interior letters were freely chosen is the reading the evidence supports; it
is not proven, and no test on surviving material could prove it. A parallel
review session on the same day tightened several claims below and wrote a
stricter legibility gate for experiment 20; that gate fails on the Warburg
print for a reason of format, recorded in the experiment's README.
The chronological sections below keep their dates.

## Construction account (end state B, 2026-09-20)

This is what the dive concludes. Each step cites the experiment that carries
it. It is a characterization with a named wall, not a generator.

1. **Caption to headword.** The compiler took the subject of each German
   caption as a headword of the Frankfurt *Sylvae quinquelinguis* of
   1595/1596. *Established on the print's own numbering:* caption k selects
   the seed of square k, 17 hits against 3.5, none at neighbouring numbers
   ([experiment 20](analysis/20-warburg-witness/README.md)); 27 by chapter
   against Mathers ([18](analysis/18-german-captions/README.md)); 21 entries
   read on the page ([19](analysis/19-image-reads/README.md)).
2. **Headword to seed.** The top row is one of the Hebrew transliterations
   printed in that entry, with aspirates reduced (sch S, ch C, bh B, th T).
   A minority of seeds come from the Greek gloss, read with η as I; none
   measurably from the Latin gloss. An exploratory count attributes roughly
   45 % of Mathers top rows to the dictionary; it is an aggregate over chance-
   contaminated tiers, not a verified list, and OCR coverage of the sampled
   entries was about one half ([12](analysis/12-dictionary-index/README.md),
   [17](analysis/17-greek-latin-seeds/README.md), 19). Names (URIEL, ASTAROT,
   BELIAL) and unexplained rows make up the rest.
3. **Seed to border.** The seed is written across the top, down the left,
   and reversed along the bottom and right: transpose plus half-turn. Frozen
   fills score 83 of 90 border cells on Dehn and 101 of 120 on the Warburg
   print ([13](analysis/13-dehn-witness-test/README.md), 20).
4. **Interior.** Letters alternate vowel and consonant downward from the
   seed: 79 % of unseen cells on Dehn, 83 % on Warburg. Inside the class the
   letter is a free choice of 2.9 bits per symmetry orbit. Chapter, prince,
   position, seed letters, the letter above and the spirit names do not
   predict it; the best frozen letter model scores 23 % on 349 unseen Warburg
   cells and 32 % on Dehn ([16](analysis/16-interior-freedom/README.md), 13,
   [15](analysis/15-spirit-names/README.md), 20).
5. **Transmission.** Witnesses disagree more in interiors than on borders
   (Mathers against Warburg, p 0.002), as expected where a copyist has
   nothing to check a letter against (20).

**The wall.** On present evidence a blank interior cell cannot be computed. A 5 × 5 interior holds
about 12 bits of free choice, a 7 × 7 about 26. Blank interiors can be
recovered only by collating German witnesses that still have them: Dresden
N 111 and N 161, Wolfenbüttel 47.13 and 10.1 b, Dehn's and Kollatsch's
editions. "Free" means free of every rule tested here; a rule keyed to a lost
external table is not excluded, and no test on surviving material could
exclude it.

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

## Exploratory caption selector frozen, 2026-09-18

[Experiment 10](analysis/10-caption-selector/README.md) specifies E1: literal
German caption/headword matching, all eligible printed Hebrew transliterations,
exact spelling, one central row in odd squares and transpose symmetry. No names,
repairs or semantic synonym choices enter the recipe. This is an exploratory
partial model, not an established historical construction.

PRIMARY — [dictionary scan 326](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=326)
and [327](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=327), with
[328](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=328) for continuation.
The recipe/code freeze precedes deterministic selection of this contiguous block.
The scoped transcription retains all ten entries, including five without Hebrew
transliterations and one uncertain entry. E1 admits PERESCH and NEKUDAH at size
seven from this sample; these are dictionary domains, not square predictions.
See the reproducible [input audit](analysis/10-caption-selector/RESULTS.md).

Computed discovery diagnostic: literal caption matching recovers two of nine
reported caption/headword associations in experiment 06. Semantic association,
orthographic equivalence and inflection remain different possible extensions;
none is justified by choosing a word from the answer. This is not a historical
performance score or a rejection of dictionary derivation.

The current Mathers export has no captions. The supplied edition is a reading
sample: its Book IV portion ends at printed p. 142 before an excerpt break and
appendix p. 175. Edited PRIMARY — [edition](https://works.hcommons.org/records/pd060-xcq09),
local hashes and bounded inspection in the experiment's caption-source audit.
Historical evaluation still lacks source-backed German captions aligned to the
fixed targets without using letters. E1's whole-orbit/interior controls are
specified but unrun. No raw witness answers opened, no historical predictions.

## Caption-first E2 pilot, 2026-09-18

**Established source access:** PRIMARY [Warburg print digitization](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf)
supplies German captions beyond the supplied edition excerpt. Eight consecutive
Book IV chapter-5 captions are visually transcribed from caption-only crops on
PDF pages 339–340. The catalog calls this the 1853 print; this experiment does
not adjudicate imprint dating. See [source provenance](sources/caption-first-e2/README.md).

**Established for the bounded E2 inputs:** eleven nominations were frozen from
captions before dictionary entries and target sizes. Seven purpose-label
alignments to the mediated PRIMARY [Mathers text](https://www.esotericarchives.com/abramelin/abramelin.htm)
include three complete targets. Five dictionary entries were retrieved with
their printed alternatives; two headword joins pass, three fail the frozen
German spelling policy, and six searches remain unresolved, not absent.
PRIMARY image locators, boundaries, uncertainty and hashes are in the
[lexicon](analysis/11-caption-first-e2/lexicon.json). No input was redrawn.

**Computed limitation:** E2 makes no predictions over the 27 strict-interior
cells of the three complete targets. Caption permutations and caption-free
vocabulary supply no positive caption evidence. Caption inputs abstain before
placement; the caption-free model instead contradicts visible letters. This is
an uninformative selector pilot, not a rejection of dictionary derivation.
The [results](analysis/11-caption-first-e2/RESULTS.md) preserve every exclusion,
control, baseline and failure. A nomination spelling ambiguity and extraction
exposures are recorded in the README/exposure audit. No independent witness
test occurred. E1 is unchanged; no historical construction has been recovered.

## Seeds, interiors and a second witness, 2026-09-20

**Established for the pinned corpus (computed):** top rows show dictionary
matches above the control; the tested interior rows do not. 56 of 232 Mathers top rows equal an OCR
transliteration of the 1595/1596 dictionary (control 8.6); interior rows 4 of
373 (control 2.7); interior substrings at control. PRIMARY, machine-read —
[1596 volume](https://www.digitale-sammlungen.de/de/view/bsb11762465),
[1595 volume](https://www.digitale-sammlungen.de/en/view/bsb10314207);
[experiment 12](analysis/12-dictionary-index/README.md). OCR vocabulary, so
the 56 is a floor.

**Supported (computed, frozen protocol):** caption subjects retrieve a subset
of seeds through that dictionary. German headwords nominated from Mathers's
English labels alone retrieve 21 of 232 top rows by chapter, against a
permutation mean of 1.9 and maximum of 14 in 2,000. The same candidates
retrieve 0 interior rows. [Experiment 14](analysis/14-caption-seed-test/README.md).
Two hits are read on the page: PRIMARY [Löwe, scan 852](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=852)
prints arieh and cephir, both Mathers seeds; PRIMARY [Schnee, scan 1056](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=1056)
prints ſcheleg. Experiment 19 subsequently checked all 21 hits on the images.
Which label belongs to which square inside a chapter is not established by
this chapter-level test.

**Established (second witness, edited):** Peterson's page prints 79 square
readings from Dehn's German-based edition. Edited PRIMARY at two removes —
[Peterson](https://www.esotericarchives.com/abramelin/abramelin.htm);
[experiment 13](analysis/13-dehn-witness-test/README.md). Against them,
predictions committed beforehand score: transpose plus half-turn 83 of 90 on
border cells; vowel/consonant checkerboard 153 of 193 interior cells; best
letter guess 61 of 193 against 48 for the most common letter. Dehn may have
corrected his text; this is not an untouched manuscript.

The aggregate includes two square records flagged as exposed before the
freeze. The scorer's narrower `_unseen` subset gives symmetry 74/81 border
predictions (10 abstentions), class 137/177 interior cells, and letter 55/177
against 44/177. The aggregate 153/193 must not be called wholly unseen.
Both sets are in experiment 13's unchanged `results.json`.

**Established description:** square interiors alternate vowels and consonants
downward from the seed word (74 % of interior cells in Mathers complete
squares, 74 % in Dehn readings, 153/193 on the aggregate scored cells). In 35 complete 5 × 5
Mathers squares the second letter of row two is R in 14, as in AREPO.

**Established (computed):** the spirit names of Book II chapter 19 overlap the
square rows: 29 exact matches of 390 Dehn names against Dehn readings, control
4.9, spread over top, bottom and inner rows. Direction of derivation is not
decided; CLAIMANT Kollatsch says names were often taken from squares.
[Experiment 15](analysis/15-spirit-names/README.md).

## The fork and the seed half, 2026-09-20 (second session)

**Established (computed, frozen tests):** inside its vowel or consonant class
the interior letter has measured conditional entropy of 2.92 bits per symmetry
orbit, against 2.99 for a top-row letter. Tested contexts give small effects:
chapter lowers cross-validated loss against permuted chapter labels by 0.15
bit, prince group and the letter above by 0.06, position, square
size and the seed's letters by nothing measurable. Seed-letter reuse is at its
chance rate (35.9 % against 35.4 %). R in row two is the commonest consonant,
not an established positional rule (16 of 42 against 12.1, p 0.07). Best
leave-one-out accuracy 32.0 %, against this experiment's 28.6 % class-only
baseline. No context improves absolute log loss over class-only. These
measurements do not establish historical free choice. Mediated PRIMARY corpus — [Peterson](https://www.esotericarchives.com/abramelin/abramelin.htm);
[experiment 16](analysis/16-interior-freedom/README.md). Discovery data with
controls, not a blind test.

**Established (computed):** Mathers and Dehn disagree on 9.5 % of top-row
cells, 9.2 % of other border cells and 12.5 % of interior cells. With each
square pair's error rate held fixed the interior excess is not significant
(p 0.13). Same source and experiment.

**Established (computed):** of the 176 top rows that experiment 12 left
unmatched, 74 lie one letter from a Hebrew transliteration of the dictionary
(control 32.3). The dictionary's Latin column shows no clear excess (9 against
6.5). Its Greek column is a candidate source: 5 exact under the frozen romanization
(control 2.2) and, post hoc, 6 under a Reuchlinian reading of η and ει as I
(control 0.5): THIRAMA θήραμα, PARADILON, ALAMPIS, KIXALIS. Experiment 17
offers an exploratory aggregate estimate of 105 to 110 of 232 dictionary
seeds. It is not a verified attribution count or a confidence interval;
overlapping vocabularies, chance matches and OCR limit the estimate. Exact
matches give entry candidates, not proof of borrowing. PRIMARY, machine-read — [1596](https://www.digitale-sammlungen.de/de/view/bsb11762465),
[1595](https://www.digitale-sammlungen.de/en/view/bsb10314207);
[experiment 17](analysis/17-greek-latin-seeds/README.md).

**Established (PRIMARY page images, one reader):** all 21 caption-selected
seeds of experiment 14 are printed in the nominated dictionary entry: Adler
nescher, Reuter parasch, Schlang pethen, Hagel chanamal, Fleisch basar, Gold
segor, Geschwer buah, Jungfrauw bethulah and ialdah, Braut callah, Liebe
dodim, Fraw sarah, Feindschafft sinah, Pallast atsarah, Brücke dobherah, Bawm
esahel, Blume perach, Einhorn reem, with Löwe and Schnee read earlier. Scan
locators and crops: [experiment 19](analysis/19-image-reads/README.md). The
square spelling reduces the aspirates of the printed word (sch S, ch C, bh B,
th T); this is an observation on 21 words. In a random sample of 30 entries
the OCR harvest holds 15 of 36 printed transliterations. This shows an OCR
coverage problem in the sampled entries; it does not justify doubling the
whole-corpus seed count.

**Established (PRIMARY print, read by subagents):** the Warburg print sets
Book IV chapters 1 to 3 as ruled grids and chapters 4 to 30 as lists of row
words under each caption; chapter 14 has rows without captions. 239 German
captions are transcribed with PDF page locators. Looked up by experiment 14's
unchanged code they retrieve 27 Mathers seeds by chapter (permutation maximum
14). Against Mathers's numbering caption k meets square k only weakly (7
against 3.5), with hits spread over neighbouring numbers: the witnesses order
squares differently inside chapters. PRIMARY — [Warburg print](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf);
[experiment 18](analysis/18-german-captions/README.md).

## Warburg preflight, 2026-09-20 continuation

**Established software defect, synthetic inputs only:** experiment 20's
original legibility gate ignores cells both readers mark `?`. A synthetic
grid with one agreed letter and 24 unreadable cells therefore has a
denominator of one. The separate checked scorer counts all 25 and stops
before historical scoring. Eight regression checks pass; both prediction
freezes are unchanged. [Preflight and reproducible result](analysis/20-warburg-witness/README.md).
This changes no historical finding. The reading followed the same evening; see the next paragraph.

**Established under the original frozen gate, disputed by the audited gate
(third witness, PRIMARY print read by two subagents):** the Warburg print was
read once after every model was committed. The audited gate of the preflight
above fails (38.6 %) because it counts the print's uneven row lists as
unread; a post hoc check finds 95.8 % reader agreement on those rows. Two independent
readers agree on 97.8 % of lettered cells in the 119 regularly shaped squares;
132 squares are ragged and count only through their top row. On cells blank
in Mathers: symmetry 101 of 120 border cells; vowel/consonant class 288 of 349
interior cells; best letter model 81 of 349; the chapter model 62 of 349.
Mathers and the print differ on 27 of 193 top-row cells, 45 of 259 other
border cells and 40 of 183 interior cells; the interior excess is significant
with each square's error rate held fixed (p 0.002). 39 of 205 top rows equal
an OCR transliteration (control 6.8); the prediction that the German print
would match better than Mathers failed (19 % against 24 %). Caption k selects
the seed of square k: 17 against 3.5, offsets 0, 1, 17, 0, 0. PRIMARY —
[Warburg print](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf);
[experiment 20](analysis/20-warburg-witness/README.md). The print belongs to
the tradition Dehn used; it is unseen, not independent of Dehn, and the scan
is about 100 ppi.

## Unverified claims

- Edition-specific errors and dependence on this particular dictionary edition;
  no earlier comparison edition has been acquired. The six cited Latin readings
  are verified, but ambiguous Hebrew and some adjacent alternatives remain
  unresolved; see the facsimile findings. No full multilingual transcription.
- A lexical rule assigning independent inner letters; inner word occurrences
  are verified in the selected compilation figures, but an answer-independent construction selector remains unverified. No complete word-square construction established.

- Any rule that fixes the interior letter beyond vowel/consonant class. None found in
  five frozen tests and two further witnesses (32 % on Dehn, 23 % on Warburg).
  This does not establish historical free choice.
- The itacist Greek reading (η as I) was found post hoc; it needs a blind repeat.
- The aspirate reduction (sch S, ch C, bh B, th T) is an observation on 21 image-read seeds.
- Warburg readings rest on a 100 ppi scan; C/E, long s/f and b/d are systematic doubts.
- A single original generator; that failure to find one establishes noise.
- Completeness and per-cell accuracy of any online Mathers transcription.
- Open image access for Dresden N 161; its old catalog link failed, but a
  [SLUB holdings record](https://kalliope-verbund.info/findingaid?fa.id=DE-611-BF-41898&fq=ead.corp.index%3A%28%22Dresdner+Liedertafel+%281839-%29%22%29&htmlFull=false&lang=de&lastparam=true)
  (PRIMARY) confirms the shelfmark and German text.
- A modern all-witness collation's coverage and editorial independence.
- Novelty of the proposed computational characterization.

# Canon — what we believe now

## Evidence and prior work

- **Established (bibliographic):** Rick-Arne Kollatsch published a 2021 edition
  and lists a draft devoted to square symmetry. His separate 257-square
  compilation includes conjectural corrections. It cannot serve as an untouched
  manuscript test set. PRIMARY — [author's publication list](https://independent.academia.edu/RickArneKollatsch).
- **Established (reported research, not independently replicated here):**
  Kollatsch attributes lexical square material to a dictionary of 1595/1596
  in his 2021 account. CLAIMANT — [Kollatsch, 2021 article](https://www.academia.edu/55141247/Abraham_of_Worms_the_disciple_of_Abramelin_the_Mage_).
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

## Unverified claims

- A single original generator; that failure to find one establishes noise.
- Completeness and per-cell accuracy of any online Mathers transcription.
- Open image access for Dresden N 161; its old catalog link failed, but a
  [SLUB holdings record](https://kalliope-verbund.info/findingaid?fa.id=DE-611-BF-41898&fq=ead.corp.index%3A%28%22Dresdner+Liedertafel+%281839-%29%22%29&htmlFull=false&lang=de&lastparam=true)
  (PRIMARY) confirms the shelfmark and German text.
- A modern all-witness collation's coverage and editorial independence.
- Novelty of the proposed computational characterization.

# 18 — German captions, per square. Frozen before any nomination

Date: 2026-09-20. Committed before the nominating agents run.

## Question

Experiment 14 showed that the caption's subject selects the seed word, scored
by chapter and from English labels. Does caption k of a chapter select the
seed of square k? H17 needs this to be a statement about squares.

## Captions

PRIMARY: [Warburg print](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf),
`sources/warburg-1853.pdf`, Book IV, PDF pages 323 to 378. Crop discipline:

1. `bands.py` renders each page and cuts it into ink bands by code.
2. Two layout subagents saw whole pages and returned band numbers, block
   types and x ranges only (`layout-*.json`). They were forbidden to write any
   square letter.
3. `mask_pages.py` blanks everything except captions and chapter headings
   (`out/captions/`), and separately everything except squares and row lists
   (`out/squares/`, for experiment 20).
4. Two transcribing subagents saw the caption pages only and wrote
   `captions-de-*.json`. They were told to report, not read, any leaked row.
5. The main thread has not opened a Warburg page or a `squares` image.

The print sets chapters 1 to 3 as ruled grids. From chapter 4 on it prints
each square as a list of row words under its caption. Chapter 14 has numbers
and rows but no captions.

## Nomination

Three Opus subagents, no nested agents. Each receives only the German captions
and chapter purposes of its chapters, and these rules, which are experiment
14's with the input language changed:

> For each caption nominate at most THREE German dictionary headwords, in this
> order of priority: (1) the concrete entity, material or state the operation
> concerns, as a noun (or adjective for a quality) in nominative singular,
> taken from the caption's own words where the caption names it; (2) one
> direct German synonym of the same scope, if a common one exists; (3) the
> action as an infinitive, only when the caption names an action and no
> entity, or when the action is the point of the caption. Use plain modern
> German spelling; the lookup code handles historical spelling. No
> mythological identifications, no Hebrew, no Latin, no guesses about what a
> magic square might contain. "In Gestalt eines X" means nominate X. If a
> caption only repeats its chapter purpose, nominate from the purpose. A
> caption with no nameable referent gets an empty list. Each nomination
> carries the caption words it renders.

The main thread does not nominate and does not edit nominations.
`nominations-de.json` is committed before `run.py` is run.

## Lookup and matching

Experiment 14's `lookup.py`, `forms`, `skeleton` and `exact`, imported and
unchanged. Candidates are experiment 12's OCR `hebrew_adjacent` tokens.

## Tests (seed 2026092018, 2,000 draws each)

Targets: complete top rows of Mathers squares, by chapter and number.

- **Per square.** Caption k of chapter c against Mathers square c/k, skeleton
  tier (and exact). Control: the chapter's candidate sets permuted among its
  own captions. This control keeps the chapter effect and tests only the
  alignment inside the chapter.
- **By chapter**, as experiment 14, with its across-chapter permutation, for
  comparison with the English labels.
- **Offsets.** Per-square hits when caption k is compared with square k + d,
  d from −2 to 2. A peak away from zero means the witnesses number differently.
- Chapter 5 was development data for E2. All counts are given with and
  without it.

Mathers and the Warburg print may number squares differently inside a
chapter. A weak per-square result on Mathers is therefore not final: the same
nominations are scored against the Warburg print's own squares in experiment
20, where caption and square share one numbering.

## Gate

Fewer than 100 captions with a candidate word: input failure, no reading.

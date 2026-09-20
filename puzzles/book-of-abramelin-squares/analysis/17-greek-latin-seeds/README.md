# 17 — Greek and Latin glosses, and what the unmatched seeds are

**Result.** The Hebrew column is the main seed source and the count of 56 was
too low by about forty. The Greek column is a small second source, read the
Reuchlinian way (η as I). The Latin column is not a source.

Frozen in commit `43eacb8`; protocol in
[PROTOCOL.md](PROTOCOL.md). 176 complete top rows were unmatched in experiment 12.

| Vocabulary | Forms | Exact | Control | Near | Control |
|---|---:|---:|---:|---:|---:|
| Hebrew-adjacent words (experiment 12), near tier | 4,130 | (56 already counted) | | 74 | 32.3 |
| Words on or after a line with Hebrew type | 8,639 | 5 | 3.2 | 83 | 42.1 |
| Romanized Greek, frozen scheme | 48,422 | 5 | 2.2 | 55 | 42.8 |
| Latin-script body words | 79,660 | 9 | 6.5 | 106 | 70.4 |
| Post hoc: Greek with η and ει read as I | 17,770 added | 6 (4 new rows) | 0.5 | | |

Control: the same rows with vowels shuffled among vowel slots and consonants
among consonant slots, 200 draws.

## Reading

- **One letter off from a Hebrew transliteration:** 74 rows against 32 for
  the control. About forty of the unmatched rows are therefore dictionary
  transliterations that differ by one letter, through OCR or through copying
  between the German original and Mathers's French source. The test cannot say
  which forty.
- **Seed estimate.** 56 exact, 5 more on Hebrew lines (chance 3), about 42
  near matches above chance, about 7 Greek. Roughly 105 to 110 of 232 top rows
  (45 %) are attributable to this dictionary by count. This is a statistical
  estimate, not a list: only the exact matches name their entry.
- **Greek.** The frozen scheme finds MILON, CUSIS, COLI, ORION, KERMA; chance
  is 2.2, so the frozen evidence alone is weak. The post hoc itacist reading
  adds THIRAMA (θήραμα), PARADILON (παραδηλῶν), ALAMPIS (ἀλαμπής) and KIXALIS
  (κιξάλης) against a control of 0.5. It was written after the frozen result
  was seen, because OIKETIS pointed to it; treat it as a lead with a good
  control, not as a blind result. `posthoc_itacism.py`, `posthoc-itacism.json`.
- **Latin.** At control. LUCIFER and APPARET are Latin words, and the corpus
  may hold a few more, but the dictionary's Latin column is not a measurable
  source.

## Residue, one label per row (`residue.json`)

| Label | Rows |
|---|---:|
| Hebrew line, exact | 5 |
| Greek, exact | 5 |
| Latin, exact | 3 |
| Hebrew-adjacent, one letter off | 71 |
| Greek, one letter off | 20 |
| Unexplained | 72 |

The near labels are contaminated by chance at the control rates above, so
they sort rows for inspection and do not identify sources. The unexplained 72
are listed in `residue.json`. They include names found elsewhere in the book
(URIEL, ASTAROT, EZECHIEL, IOSUA, BELIAL), and rows that look like Hebrew
transliterations more than one letter from any OCR form (LEUIATAN, BEHEMOT,
TSARAAT, IEDIDAH). That last remark is an impression, not a count. The OCR-gap
share is measured in [experiment 19](../19-image-reads/README.md).

## What was built

`build_vocab.py` imports experiment 12's `build_index.py` for page parsing and
entry detection and adds three vocabularies with first locators. Experiment 12
is unchanged and there is no second parser. `romanize.py` is the frozen scheme
with unit tests.

## Limits

OCR of sixteenth-century Greek type with ligatures is poor; Greek recall is
low. Mathers's rows come through a French manuscript, so spelling drift is
expected and the one-letter tier is the only allowance made for it.
Discovery data, exposed corpus.

## Reproduce

```sh
cd puzzles/book-of-abramelin-squares/analysis/17-greek-latin-seeds
python3 -m unittest test_romanize
python3 build_vocab.py        # needs experiment 12's out/hocr; rewrites the three tsv files
python3 residue.py
python3 posthoc_itacism.py
```

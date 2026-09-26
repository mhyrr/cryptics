# 21 — Sol audit of the Warburg readings

**Result, 2026-09-21:** the original model scores reproduce, but the new
readings do not supply a clean independent transcription confirmation. The
gate dispute concerns two separate properties: whether a row list is legible
and whether it can be assigned square coordinates.

Greg authorized Sol agents. Before dispatch, `3a21def` froze eleven pages
selected by page number alone, 48 labelled items. Two fresh `gpt-5.6-sol`
readers saw only square-only images and the worklist. Neither saw Opus answers,
captions, predictions or the other reader's output. All 48 items are present;
no item spans multiple pages in the frozen layout metadata.

PRIMARY — [Warburg print](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf),
experiment-18 square-only crops with hashes in `worklist.json`.

## Transcription comparison

| Quantity | Sol A/B | Opus A/B on the same cohort |
|---|---:|---:|
| Items with identical row-length vectors | 20/48 | 46/48 |
| Agreed letters / comparable nonblank positions | 734/792 | 1,758/1,826 |
| Letter or letter/blank conflicts | 49 | 68 |
| Unresolved comparable positions | 9 | 0 |

Literal and J-to-I-normalized totals are identical in this sample. The
denominators differ because shape disagreement excludes positions; the
agreement fractions alone must not be used to rank reader accuracy.

All four readers give the same shape on 14 items. On 454 positions where each
model pair agrees internally, the two model pairs agree on 423 and conflict
on 31. The conflicts remain in `comparison.json`; no majority vote or model
prediction adjudicates them. Shared-model agreement does not guarantee a
correct transcription. The sample does not establish which reader is right.

## Scorer audit

A third Sol agent independently reviewed the code and reproduced the original
outputs. [SCORER-AUDIT.md](SCORER-AUDIT.md) gives line references and
`audit_scorer.py` reproduces its measurements.

- The original gate's omission of `?/?` is a real defect, with no aggregate
  effect in the saved Opus regular grids.
- The checked gate counts ragged row-list positions as having zero agreement
  without comparing their letters. It measures a mixture of layout coverage
  and legibility. Its historical failure stays recorded, but “the print is
  unreadable” is not established by that failure.
- J/I normalization differs between the checked gate and historical scorer;
  no current aggregate change, but future comparisons must make it explicit.
- Frozen alignment scores cover 33 of 119 coordinate-bearing grids.
  Interior prediction coverage is 349 letters of 375 positions, with 11
  unreadable and 15 blank. The original 81/349 exact-letter result and 288/349
  class result reproduce; they remain conditional on those choices and source
  transcriptions.

Keep experiment 20 as conditional corroboration with its failed gate and
transcription limits attached. Its threshold B is not a proof of freely
chosen letters. This audit does not retroactively change that protocol or
create an independent historical witness.

## Reproduce

```sh
python3 test_compare.py
python3 compare.py --check
python3 audit_scorer.py --check
```

Four focused comparison tests pass. Raw reader files, worklist, comparison
output and scorer-audit output are retained. Crop files must be restored via
experiment 18 if absent; their checksums are verified before comparison.

The next source step was executed separately: experiment 22 obtains Dresden
N 111 through SLUB's public metadata interface and opens a bounded manuscript
collation pilot. That manuscript does not inherit Warburg's transcription.

# 12 — Local OCR index of the dictionary, and a row test

**Result.** Top rows of the squares are words of the dictionary's Hebrew
transliteration vocabulary far above chance. Interior rows are not.

| Row position | Full rows | Exact matches | Shuffled control (vowel and consonant slots kept) |
|---|---:|---:|---:|
| top | 232 | 56 | 8.6 |
| bottom, read right to left | 88 | 16 | 1.9 |
| upper inner | 155 | 2 | 0.7 |
| centre | 65 | 2 | 1.0 |
| lower inner | 153 | 0 | 1.0 |

Interior rows and columns that contain a dictionary word of four or more
letters as a substring: 83 of 395, against 86.7 for the control. Full counts,
the near-match tier and every hit are in `rows-in-dictionary.json` and
`substrings-in-dictionary.json`.

This bears on H7 (supported at corpus scale for seed words) and on H12, H14
and H15 (a dictionary word on a full interior row, central or otherwise, is
at the control rate in the exposed corpus).

## What was built

E2 lost six of eleven lookups to remote search failures. The Bayerische
Staatsbibliothek serves hOCR for every scan of both volumes
(`https://api.digitale-sammlungen.de/ocr/<id>/<scan>`; 1,158 + 276 scans;
rights statement NoC-NC). `fetch_hocr.py` downloads them to `out/hocr/`
(gitignored; `hocr-manifest.tsv` records size and sha256 per scan).
`build_index.py` rebuilds the two-column reading order from word boxes, finds
centred headword lines, and collects the Latin-script words printed next to
Hebrew type anywhere in each entry.

- `entries.tsv`: 14,360 detected headword lines with scan locators.
- `tokens.tsv`: 5,370 Hebrew-adjacent tokens, 3,680 distinct.

PRIMARY source, machine-read: [1596 A–S](https://www.digitale-sammlungen.de/de/view/bsb11762465),
[1595 T–Z](https://www.digitale-sammlungen.de/en/view/bsb10314207).

## Limits

Everything here is OCR. Long s is often read as f; the row test indexes both.
Hebrew type is sometimes not recognised, so the vocabulary is incomplete: the
56 top-row matches are a floor. Headword detection is a layout heuristic and
also catches some Latin lemma lines. The index is a locator and a statistical
vocabulary. A transliteration that a claim depends on must be read from the
page image. The row test is a discovery analysis on the exposed Mathers
export, not a blind test.

## Reproduce

```sh
cd puzzles/book-of-abramelin-squares/analysis/12-dictionary-index
python3 fetch_hocr.py fetch      # about 12 minutes, resumable
python3 fetch_hocr.py manifest   # compare with the checked-in manifest
python3 build_index.py
python3 rows_in_dictionary.py
python3 substrings_in_dictionary.py
```

The two analysis scripts need only the checked-in `tokens.tsv`.

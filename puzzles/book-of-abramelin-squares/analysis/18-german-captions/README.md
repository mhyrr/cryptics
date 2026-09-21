# 18 — German captions, per square

**Result.** The German captions select seeds better than Mathers's English
labels did (27 by chapter against 21). Against Mathers's numbering, caption k
and square k line up only weakly, because Mathers numbers squares differently
from the German print. The per-square question is reserved for
[experiment 20](../20-warburg-witness/README.md) on the print's own squares;
that reading and score have not yet been completed.

Protocol committed before nomination ([PROTOCOL.md](PROTOCOL.md)); captions
and nominations committed before lookup (`nomination-freeze.json`).

| Test, Mathers top rows (232) | Observed | Control mean | Control maximum | Share of draws at or above |
|---|---:|---:|---:|---:|
| By chapter, skeleton tier (across-chapter permutation) | 27 | 1.8 | 14 | 0.000 |
| By chapter, exact | 17 | 1.1 | 8 | 0.000 |
| Per square, skeleton (captions permuted inside the chapter) | 7 | 3.5 | 9 | 0.033 |
| Per square, skeleton, without chapter 5 | 6 | 3.0 | 9 | 0.049 |
| Per square, exact | 4 | 2.0 | 7 | 0.127 |

Per-square hits when caption k is compared with square k + d:
d = −2: 5, −1: 6, 0: 7, +1: 2, +2: 4. There is no sharp peak at zero.
The hits sit near the diagonal and spread along it, which is what a changed
order inside chapters looks like.

239 captions, 407 nominations; 167 captions received at least one candidate
word (gate 100). Lookup tiers: 221 exact key, 43 OCR-tolerant, 143 none.

## What was built

- `bands.py`: renders each PDF page and cuts it into ink bands.
- `layout-*.json`: two Opus subagents labelled every band (caption, square,
  row list, heading, other) with no letters in their output.
- `mask_pages.py`: caption-only pages and square-only pages, cut by code.
- `captions-de.json`: 239 German captions and 30 chapter purposes, read by two
  Opus subagents from caption-only pages. Neither reported a leaked row.
  PRIMARY — [Warburg print](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf),
  PDF page in every record.
- `nominations-de.json`: three Opus nominators, captions only.
- `run.py`: experiment 14's lookup and matching, imported unchanged.

## Findings about the print

Chapters 1 to 3 are ruled grids. From chapter 4 the squares are printed as
lists of row words under each caption. Chapter 14 prints numbers and rows
without captions. Chapter 2 has no caption 1, and captions 24/1 and 25/1 are
empty. Printed page = PDF page − 4.

## Limits

Transcription by one reader per page from a 100 ppi scan; 26 captions carry a
doubtful word. Nominators chose how to treat "Dasselbe" and empty captions
(from the antecedent or the chapter purpose) and said so in `renders`. The
Mathers corpus is exposed; candidates are OCR.

## Reproduce

```sh
cd puzzles/book-of-abramelin-squares/analysis/18-german-captions
python3 run.py --check                    # needs only checked-in files
python3 bands.py 320 388 && python3 mask_pages.py   # needs sources/warburg-1853.pdf, Poppler, ImageMagick
```

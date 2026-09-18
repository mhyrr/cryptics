# E2 caption and dictionary evidence

PRIMARY: [Warburg Institute print record](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf),
catalogued Stuttgart 1853 and described there as a reprint of the 1725 imprint.
This experiment does not adjudicate the imprint date. Downloaded 2026-09-18:
`https://wdl.warburg.sas.ac.uk/static/pdf/wdl-awm-aadf-0001-2.pdf?_m=1673341113`.
SHA-256 `195a49411cbd40d9299d6af326ad35723f8ccf92750c5b253881dd9cce8826bd`;
10,646,383 bytes, 388 PDF pages. Unchanged local PDF: `../warburg-1853.pdf`
(gitignored). Do not rediscover or reacquire if it is present.

The eight PNGs are caption-only crops from PDF pages 339–340, Book IV chapter 5,
local items 1–8. `chapter5-and-1.png` also preserves the chapter purpose and
cross-reference. Rendered with Poppler at 240 dpi; nothing retouched. Printed
page numbers have not been visually verified. PDF page, chapter and item are
the precise locators. Crop boxes and SHA-256 are in
[captions.json](../../analysis/11-caption-first-e2/captions.json).

PRIMARY: the twelve `bsb11762465_*.jpg` files are unchanged full-resolution
BSB images for the 1596 dictionary, A–S part. Each URL, viewer scan and SHA-256
is in [dictionary-images.json](../../analysis/11-caption-first-e2/dictionary-images.json).
The scoped [lexicon](../../analysis/11-caption-first-e2/lexicon.json) preserves all
Latin transliterations belonging to the Hebrew gloss of five retrieved entries.
All other printed alternatives/languages remain available in these full images.

| Scans | Role |
|---|---|
| 85–86 | `Alter` context and `Alter man`; the latter is the relevant sense |
| 239–240 | `Blume`, including complete poetic continuation and next boundary |
| 632–633 | bounded `Greis` search context; no verified headword found |
| 804–805 | `Kriegsman`, including continuation and next boundary |
| 996–997 | `Reuter` and context; `Reitter / Sieb` is a different sense |
| 1001–1002 | `Rieſe`, including continuation and next boundary |

The exact and prefix OCR query results are preserved in experiment 11; an OCR
miss is not a dictionary absence. No synonym was added after those searches.
See [EXPOSURE.md](../../analysis/11-caption-first-e2/EXPOSURE.md) before reusing
any of this packet for prediction.

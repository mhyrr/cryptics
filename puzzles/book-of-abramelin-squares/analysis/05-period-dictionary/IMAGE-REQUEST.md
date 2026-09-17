# Dictionary images — request and fulfilment

**Status 2026-09-17 (later session): minimum source packet acquired.** All
title/imprint pages and the six entries with continuations and neighbours are
tracked in [`sources/period-dictionary/`](../../sources/period-dictionary/README.md)
with SOURCES.tsv and a sha256 manifest. Resolution is the BSB service's native
ceiling (about 1290 × 2120 px, roughly 300 ppi on an octavo leaf), below the
2500 px aspiration stated below; Hebrew vowel points are marginal. The
"Additional input for the error claim" (an earlier comparison edition) is
still open. The original specification follows unchanged for the record.

---

**Original request (earlier 2026-09-17 continuation of `34b1f43`):** no images
acquired at that time. It is an acquisition specification, not a lexicon
or a new experimental freeze.

## Minimum source packet

| Volume (PRIMARY digitization target) | Required pages |
|---|---|
| Frankfurt Palthenius/Basse, part I, 1596 A–S: [bsb11762465](https://www.digitale-sammlungen.de/de/view/bsb11762465) | Title/imprint pages; complete pages containing **Himmel** and **Lehrer**, plus any continuation pages |
| Frankfurt Palthenius/Basse, part I, 1595 T–Z: [bsb10314207](https://www.digitale-sammlungen.de/en/view/bsb10314207) | Title/imprint pages; complete pages containing **Vnterweiſer**, **Wachs**, **Warſager**, **Waſſer**, plus any continuation pages |

The headwords are search targets quoted by Kollatsch, not independently
confirmed headings. Inspect the historical alphabetization, including U/V.
Printed dictionary page numbers and viewer page numbers are **unknown**.
Do not use `claims.json`'s 138–141 locators: those refer to the modern edition,
not to dictionary pages. Do not invent scan numbers from alphabetical position.

Alternative digitizations supplied for access: [Google Books jkY8AAAAcAAJ](https://books.google.com/books?id=jkY8AAAAcAAJ)
and [LPyVAQ1q89cC](https://books.google.com/books?id=LPyVAQ1q89cC).
Confirm the title, imprint and division before substituting either scan.
Full scans of both target volumes also satisfy this acquisition request.

Preserve full page edges, printed pagination/signatures, every language column,
adjacent headwords and all alternatives. Include the previous page if the entry
begins there and every subsequent page until the next entry boundary is visible.
Do not crop to the expected translation or retain only an OCR extract.

Use the original scan resolution if available. For captures, aim for at least
300 dpi equivalent (roughly 2500 pixels on the short page edge); this is a
practical target, not a guarantee. The acceptance test is legibility of Hebrew
points, Greek accents, Latin transliteration and long-s at native resolution.
Supplement a full-page capture with overlapping detail images if necessary.
Keep uncertain letters uncertain; do not infer them from the square.

Save files to `puzzles/book-of-abramelin-squares/sources/cache/period-dictionary/`.
For each image, add a line to `SOURCES.tsv` with filename, source URL, viewer
page number, printed page/signature, volume/year, capture date and uncertainties.
Use `unknown` for genuinely unresolved metadata. Hash acquired files and retain
a tracked manifest outside the ignored cache before any claim relies on them.
At present there are no image rows or hashes to record.

## Additional input for the error claim

The alleged edition-specific error associated with **Vnterweiſer** needs the
same complete entry and title/imprint from an **earlier comparison edition**.
No particular earlier edition or page has been verified here. Identify it from
the bibliography before asserting an edition-specific innovation. The first
packet can check the reported reading; it cannot establish that stronger claim.

## Access attempt in this continuation

- The browser skill was read. Tool discovery exposed neither `node_repl` nor
  its `js` execution tool, so the mandated in-app bootstrap could not run.
- The available Tidewave `browser_eval` help action returned: “No browser is
  connected to the Tidewave control page.” No browser was opened or controlled.
- Web opens of both BSB viewers and Google Books `jkY8AAAAcAAJ` returned
  non-retryable safe-open errors. `LPyVAQ1q89cC` returned a cache miss.
- No shell download or shell-launched browser was attempted. No account,
  purchase or library request was made. The requested fallback acquisition
  remains unfulfilled; this file is not a substitute for the images.

These are session access observations, not evidence that scans are absent.
The shell-download workaround suggested by an older HIVE memory conflicts with
the current user instruction and handoff; do not follow it.

## What remains after acquisition

The six entries are discovery-exposed checks, never an independent test lexicon.
Inspect and transcribe them separately from Kollatsch's quotations. Only then
preselect an unfiltered contiguous dictionary block, including misses, and
record every normalization and exposure before freezing historical inputs.

No newly inspected evidence fixes an interior placement. The protocol's straight
row/column recipe remains our candidate, not an established historical method.
Seed attribution plus symmetry leaves disjoint interior orbits unconstrained.
Do not implement a historical model by fitting transformations or paths to
observed answers. Source acquisition and independent placement justification
remain separate gates. Historical metrics stay null, and synthetic success
does not satisfy the gate for German-witness comparison. No randomness inference follows.

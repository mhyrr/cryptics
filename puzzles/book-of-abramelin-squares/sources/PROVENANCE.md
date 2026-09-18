# Provenance

One line per file in this folder: filename, origin URL or citation, date
fetched, and what (if anything) was changed from the original.

| File | Origin | Fetched | Changes |
|---|---|---|---|
| `mathers-web-rows.txt` | PRIMARY (mediated): [Mathers, Book III, in Peterson's digital edition](https://www.esotericarchives.com/abramelin/abramelin.htm) | 2026-09-16 | Web-tool text export, numbered square rows only. Retained web line numbers and merged rows. Removed separately marked German additions and inline variant commentary. No letters changed. |
| `period-dictionary/` (28 JPEGs, SOURCES.tsv, MANIFEST.sha256) | PRIMARY: BSB IIIF image API for `bsb11762465` (1596 A–S) and `bsb10314207` (1595 T–Z); per-file URLs in `period-dictionary/SOURCES.tsv` | 2026-09-17 | None. Original `full/full` bitstreams, uncropped. See its README. |
| `mathers-squares.json` | Derived from the pinned row export by `../analysis/01-mathers-structure/extract.py` | 2026-09-16 | Split numbered records and comma-delimited rows; whitespace trimmed; dot → null. Ten ambiguous layouts retained with exclusion reasons. Literal numbering and raw rows retained; no conjectural correction. SHA-256 of input embedded. |

## Capture and audit limits
The web tool fetched the single source page around line positions 1895, 1950,
2100, 2255, 2350, 2550 and 2730. Overlapping row lines were deduplicated with an
equality check. Retained numbered records span web lines 1895–2625. Web line
numbers identify this capture, not manuscript folios or stable print pagination.
Regeneration from the pinned extract is offline and deterministic. Recapturing
the source page may yield different web line numbers or text.

The source labels German supplements 10/6 and 10/7 with a colon; those are not
part of this Mathers corpus. The source's 25/4 among chapter 24 squares remains
25/4 in the corpus. Do not infer a German alignment from that label.

No 1898 print or manuscript image has been collated against every exported cell.
Lowercase additions, multi-letter cells, missing delimiters and ragged rows remain
unresolved. Neither modern correction nor the model's impression repairs them.

## Research exposure
The source page's German variants and Kollatsch's [2024 symmetry draft](https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_)
(CLAIMANT) were retrieved during discovery. They are excluded from the corpus,
but their displayed readings cannot be claimed as blind targets. For a future
blind study, audit the retrieval record or use a fresh independent adjudicator
and an untouched witness subset. This pass claims no blind German test.

## 2026-09-17 dictionary discovery

The [Kollatsch edition preview](https://www.academia.edu/45180953/Edition_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_Hamburg_2021_)
(CLAIMANT / edited PRIMARY) exposed Book IV pp. 138–142 and their variants.
Treat every square on those pages and every example in the retrieved 2024
symmetry draft as discovery-exposed. No raw German witness was newly inspected.
Numbering alone does not align these examples with Mathers.

Six short reported dictionary/square spelling pairs are preserved separately in
`../analysis/05-period-dictionary/claims.json`, with note locators and all
`facsimile_verified` fields false. Its raw strings are uncorrected quoted
readings, not dictionary transcriptions. `results.json` stores the explicitly
normalized comparison separately. No source cells or prior predictions changed.
See that experiment's `SOURCE-AUDIT.md` for catalogue locators and access failures.

## 2026-09-17 facsimile reading after acquisition

`../analysis/05-period-dictionary/facsimile-readings.json` records direct,
discovery-exposed Latin excerpts from the tracked PRIMARY images, plus
alternatives, boundaries and uncertainty. It does not replace the Hebrew or
Greek originals. `facsimile-audit.json` records image and input hashes, source
URLs, the explicit water line join and long-s/ASCII-case normalization. No
image bytes or SOURCES.tsv rows were changed. The frozen claims.json retains
its original flags; the new audit supplies the current verification status.

## 2026-09-17 user-supplied local PDFs

- `buchstabenquadrate.pdf`: edited PRIMARY, [public compilation](https://works.hcommons.org/records/xep4n-asx54), 36 pages. User supplied, unchanged. Computed MD5 agrees with the public record inspected in experiment 07.
- `lp_wp.pdf`: edited PRIMARY / CLAIMANT apparatus, [second-edition preview](https://works.hcommons.org/records/pd060-xcq09), 128 pages. User supplied, unchanged. Title and page count agree with the earlier browser inspection; no repository checksum comparison claimed.

Byte counts and computed hashes are pinned in `LOCAL-PDFS.json`. The PDFs remain
local and gitignored under the existing binary-source policy. Experiment 08
visually checks compilation pp. 3–4 and tests the already exposed capitalized
examples. No new raw witness or evaluation corpus is acquired.

## 2026-09-18 structural draft acquired

`Zur_Symmetriestruktur_der_magischen_Buch.pdf`: user supplied, unchanged,
50 pages, 509,974 bytes. CLAIMANT / edited examples — [source record](https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_).
SHA-256 `0975aee6da3a0093e3d5e7bb5a0065ff4d51b761f474a55b2fd18f2d6ceaf314`;
metadata in `../analysis/09-structural-draft/source.json`. Local and gitignored.
Printed p. n = PDF n+2. Requested pp. 4, 7–10, 35–41 and conclusion p. 46
visually inspected; text extraction also used to read the discussion. Treat
the supplied draft as discovery material. Separate figure and sequence readings
are preserved in experiment 09; no raw witness or historical evaluation target
opened. Earlier access-failure notes describe the prior session, now superseded.

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

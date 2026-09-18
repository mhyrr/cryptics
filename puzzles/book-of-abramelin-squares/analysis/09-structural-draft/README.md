# 09 — Structural draft: figure audit and qualified overlay test

2026-09-18. Greg supplied the previously inaccessible 50-page draft. Its title
dates the study November 2024; `source.json` pins the unchanged local PDF.
Printed p. n is PDF page n+2. The prefatory leaf is PDF 1, PDF 2 is blank.

## Scope fixed before the new computations

Visually inspect the requested printed pp. 4, 7–10, 35–41. Preserve the beast
figure separately from its accompanying sequence, edition and compilation;
record blanks as null. Compare the beast and wax figures cell by cell with
experiment 07, with no transposition or correction. This settles source layout,
not historical truth. A source figure may itself contain an error.

The draft says explicitly (pp. 37–38) that some name overlays disturbed nearby
lowercase cells, and proposes repeated trial insertions/erasures as a possible
history. Therefore experiment 08's failure of capital-only erasure does NOT
refute this broader claim. In particular, the source nominates transpose T,
not TA, for the beast and bird precursors. Report their existing T diagnostics
alongside dragon TA and water TA; do not relabel the original primary test.

For a positive comparison, add two source-selected, already exposed examples:
NEBBELAH (p. 37) and GEBHINAH (p. 40). Test T after capital erasure, retaining
all lowercase cells. NEBBELAH's outer frames are reported T; GEBHINAH's outer
frames are reported TA and its third T, so T is their common symmetry. Using T
also for the erased fourth frame is our conditional precursor model, not a
transmitted fact. Reuse the exact experiment 08 diagnostic and controls without
tuning it. Never turn a wholly erased orbit into a guessed letter.
For compatible cases, count the wholly erased independent orbits and report
26 to that power as conditional completions over A–Z. This is not a historical
alphabet claim or an inference that every completion would be linguistically valid.

## Source inspection findings

**CLAIMANT / edited examples:** [structural draft](https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_).
The following claims are about the rendered modern PDF, not a manuscript.

| Printed page | Observed content and consequence |
|---|---|
| 4 | NABHI is written in successive horizontal rows. No alternate column-first convention is declared here. |
| 7–8 | SATOR/NABHI are shown as spatially separated frames and center. Their text extraction interleaves these components; it is not a faithful row transcription of those decomposed figures. |
| 9–10 | NECOT figure preserves the compilation's orientation and all cells. The text identifies anti-diagonal symmetry. Footnote 12 reads frame strips in different directions: top rightwards, bottom leftwards, left downwards, right upwards; ordinary full rows rightwards and columns downwards. This resolves the earlier wax layout uncertainty. |
| 35 | Mixed frame types and possible errors are distinguished; the author warns against treating every departure from the common type as scribal error. |
| 36 | MAHAMORAH motivates a conjectured filling order: top/left frame strips outside-in, then right/bottom inside-out. It does not provide a rule for assigning all letters. The outer word's function is deferred to installment two. |
| 37 | NEBBELAH suggests some capitals replace identical lowercase letters; its innermost original letters are expressly called indeterminate. MAPPALAH has lowercase disruption beyond capital positions. |
| 38 | METHIRRAH motivates a possible history of repeated insertion/erasure and lost interior letters. The author explicitly qualifies this as a possible account. Dragon is conjectured originally TA. |
| 39 | BEHEMOT prose says middle row, while the figure is untransposed and the accompanying sequence puts the word in column 4. Additionally the drawn row 6 is `r e [blank] s t i n`, whereas the sequence on the same page is `rerotin`. The figure and prose cannot be harmonized by text extraction or a silent transpose. Bird has an intact TSIPPOR cross and is conjectured originally T. |
| 40–41 | GEBHINAH is a gentler mixed-frame case. EBENIEKARAH has four BAAL arrangements and broader disruptions; OIKETIS is considered without a successfully identified name. No general selection or placement rule is supplied in these pages. |
| 46 (additional conclusion check) | The author says installment two will treat lexical polygrams and the dictionary source, and installment three will treat names. He says names were inserted, or, more often, derived from the squares' letter material. This is a CLAIMANT assertion, not independently established here. It makes an independent-name-input assumption something to test, not take for granted. |

The beast figure's blank and `s` are source discrepancies, not proposed repairs.
Our prior edition/compilation readings remain unchanged. The apparent row/column
wording error and the figure/sequence discrepancy are distinct issues.

Local rendering used `pdftoppm -r 115 -png`; all requested pages were inspected
as images, plus the conclusion on p. 46, with pypdf text extraction for reading the German discussion. Source
PDFs remain local and gitignored. The previously exposed draft examples remain
discovery material; no raw witness or independent evaluation target is opened.

## Reproduce

Python standard library from repository root:

```sh
python3 puzzles/book-of-abramelin-squares/analysis/09-structural-draft/audit.py
python3 puzzles/book-of-abramelin-squares/analysis/09-structural-draft/audit.py --check
python3 puzzles/book-of-abramelin-squares/analysis/09-structural-draft/audit.py --check-source
```

`--check-source` checks the locally supplied PDF against its saved SHA-256;
normal computation needs only checked-in readings and the earlier scripts.
Experiment 08's exhaustive-mask tests verify the reused calculation. See
generated `RESULTS.md` and `results.json`; conditional precursor letters are
not historical predictions.

## Decision

The access wall and requested layout checks are resolved. Retain a mixture of
symmetries and a distinction between gentle replacements and wider rewriting.
Do not infer that the rejected capital-only model describes every overlay.
The remaining wall is construction: independent word/name selection and a
specified transformation/placement rule. This installment does not supply it.
The author's claim that names were often derived FROM the grids specifically
warns against treating those same names as independent reconstruction keys.
The next useful source is the author's promised second installment on lexical
polygrams (third on names), or explicit equivalent construction instructions.
An exploratory recipe can be designed from these discoveries, but must be
labeled as ours and frozen before independent lexicon sampling and evaluation.

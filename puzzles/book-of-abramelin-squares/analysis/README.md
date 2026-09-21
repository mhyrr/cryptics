# analysis/

One subfolder per experiment: `NN-short-name/` with its own `README.md`
stating the question, the method, how to run it, and the result. Heavy
outputs go in `out/` (gitignored); check in a summary. If the experiment
needs more than the standard library, it gets a `pyproject.toml` here and is
run with `uv run`.

| # | Experiment | Question | Result | Bears on |
|---|---|---|---|---|
| 01 | [Mathers structure](01-mathers-structure/README.md) | Can elementary rules recover missing letters? | 242 exported records; 232 analyzable; symmetry leaves free choices; no tested elementary generator fits a complete grid | H1–H4 |
| 02–04 | [Shared stress tests](../STRESS-TESTS.md) | Do frames, corpus fragments or local recurrences generalize? | Frame fills help scattered blanks; independent-letter reconstruction remains unreliable | H8–H11 |
| 05 | [Period dictionary preflight](05-period-dictionary/README.md) | Can independent lexical constraints predict inner orbits? | Selected facsimiles subsequently verified; no recovered construction selector; completion machinery passes planted checks | H7, H12 |
| 10 | [Frozen E1](10-caption-selector/README.md) | Does literal caption matching plus a central cross predict interiors? | Recipe and independent dictionary block frozen; historical caption join pending | H14 |
| 11 | [Caption-first E2](11-caption-first-e2/README.md) | Do bounded semantic caption nominations improve hidden-interior prediction? | Eight captions, eleven lookups; three complete aligned targets but no usable caption domains; controls ran, pilot uninformative | H7, H12, H15 |
| 12 | [Dictionary OCR index](12-dictionary-index/README.md) | Are square rows words of the dictionary's Hebrew transliterations? | Top rows 56 of 232 (control 8.6); interior rows and substrings at control | H7, H12, H14 |
| 13 | [Dehn witness test](13-dehn-witness-test/README.md) | Do frozen predictions match Dehn's readings on cells blank in Mathers? | Symmetry 83 of 90 on borders; vowel/consonant class 153 of 193 interior; letter 61 of 193 | H4, H16 |
| 14 | [Caption to seed (E3)](14-caption-seed-test/README.md) | Does the caption select the seed word, or interior rows? | Seeds 21 hits against a permutation maximum of 14; interior rows 0 | H7, H15, H17 |
| 15 | [Spirit names](15-spirit-names/README.md) | Do the chapter-19 spirit names occur as square rows, and can they fill blanks? | 29 exact of 390 (control 4.9); fills 0 of 3 | H18 |
| 16 | [Interior freedom](16-interior-freedom/README.md) | Can tested contexts determine interior letters? | Best accuracy 32.0% vs 28.6% class-only; free choice remains unproved | H16, H19–H21 |
| 17 | [Seed residue](17-greek-latin-seeds/README.md) | Do Greek, Latin and near Hebrew forms explain unmatched seeds? | Excess Hebrew near matches; post hoc Greek lead; Latin near control | H7, H22–H23 |
| 18 | [German captions](18-german-captions/README.md) | Do German nominations retrieve seeds by square? | 27 chapter-level hits; within-chapter numbering remains unresolved | H17 |
| 19 | [Dictionary image reads](19-image-reads/README.md) | Do OCR hits exist on the page? | 21 selected hits confirmed; sampled OCR recall 15/36 | H7, H17 |
| 20 | [Warburg witness](20-warburg-witness/README.md) | Do the frozen models hold on a witness read once? | Class 83 %, letter 23 % on 349 unseen cells; caption k to seed k 17 against 3.5; end state B | H4, H16, H17, H24, H25 |

# E2 exposure audit

2026-09-18. Source-backed and answer-independent selection does not make this
an untouched-witness test. This audit includes extraction failures.

## Before the new caption sample

The project's Mathers corpus and earlier structural/discovery examples were
already exposed. The session read handoffs, canon, hypotheses, E1 and the
existing source provenance. No existing exposure was reset by the new folder.

A first local text-layer filter meant to identify prose was too broad: it
emitted square sequences and apparatus from edition PDF page 120, printed
p. 138. Those are already discovery-exposed and outside this chapter-5 pilot.
The filter was not used for the pilot caption dataset.

## Warburg extraction

The Warburg PDF contains page images, not a text layer. OCR found chapter 5
on PDF page 339. A missing Tesseract TSV config caused plain OCR output to be
written under a `.tsv` filename. Inspecting its first four lines accidentally
displayed the neighboring chapter-4 moon and water captions and square rows.
Treat those Warburg chapter-4 readings as newly exposed. Do not reuse them as
blind validation. No chapter-5 square row was in that output.

The corrected locator used `tessedit_create_tsv=1` and filtered numbered caption
lines. Pilot visual inspection was restricted to the saved eight caption crops.
The first crop includes the chapter heading and purpose context; none includes
its square letters. The exact original wording is retained separately from
lookup labels. All nominations were hashed before dictionary lookup or sizes.

## Mathers alignment extraction

An HTML-context diagnostic after nomination freeze emitted some adjacent seed
commentary, including `ANAKIM` at 5/1 and `PARAS` with rider/eagle discussion.
Treat Mathers 5/1, 5/4 and 5/5 conservatively as newly re-exposed in this session.
The giant was not aligned by its seed. The rider/eagle targets are incomplete
and did not enter scoring. This diagnostic was replaced by extraction of the
numbered natural-language purpose list only. The alignment ledger makes no
claim about correct historical ordering of the underlying square texts.

## Dictionary and computational stages

Every viewed dictionary page and its context is now exposed. Five relevant-sense
entries were transcribed without choosing a transliteration by its resemblance
to a square. All alternatives, misses and prohibited German spellings remain.
The semantic procedure was not extended to use the exposed seed commentary.

The evaluator uses the previously exposed Mathers corpus, with three complete
targets: 5/8, 5/9 and 5/11. Code and inputs were frozen before per-cell predictions;
predictions were frozen before scoring. The scoring program sees the hidden
answers; the semantic selector does not. No newly acquired manuscript answers
or German chapter-5 square letters were opened. The control results expose
aggregate performance and are themselves development evidence for future work.

No untouched-witness accuracy, recovered historical selector, or dictionary
edition attribution follows from this pilot. A later E3 needs a new cohort,
a fresh exposure audit, and explicit handling of German spelling and compounds.

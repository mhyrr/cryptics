# 21 — Independent Sol transcription audit

2026-09-21. Greg authorized Sol subagents for the next steps. The repository
changed after the preceding conversation: Opus readers already completed
experiment 20. This experiment is a new transcription audit of that exposed
print, not a new blind historical witness and not a retroactive protocol change.
Original experiment 20 files and results remain unchanged.

## Cohort and reading freeze

Select every fifth page in the sorted experiment-18 square-mask page list,
starting with the first page. Selection uses page metadata only, not scores,
letter disagreements or shape quality. Eleven pages result: 324, 329, 334,
339, 344, 349, 354, 359, 364, 369 and 374. Pin crop hashes and item labels in
`worklist.json` before readers run. Items spanning other pages remain fragments
and are excluded from whole-item comparisons; preserve their visible text.

Two independent `gpt-5.6-sol` agents see the same square-only images and worklist.
They receive no existing readings, captions, predictions, scorer results or
each other's output. No nested agents. Each saves after every page. Transcribe
visible row groups literally in uppercase. Preserve I/J as read; uncertainty
is `?`, printed placeholders are `.`, and ambiguous segmentation is a note.
Do not infer missing letters, equalize row lengths or use symmetry, word
recognition or another source to resolve a glyph.

## Analysis fixed before new readings

1. Verify input hashes and reader coverage. Report unlocated items, partial
   items, uncertainty and shape differences. Never repair a raw reading.
2. Compare Sol A/B on full single-page items, first literally and then with
   the pre-existing J-to-I normalization. A word-list position is comparable
   only when both lists have identical row lengths; report coverage separately.
   `?/?` counts as unresolved, not agreed. Agreed printed blanks do not count
   as agreed letters. Ragged row lists are readable strings but not square
   coordinates; do not conflate those two properties.
3. Compare unanimous Sol letters with unanimous Opus letters on the same
   complete item and equal shape. Report matches, conflicts, missing coverage
   and a per-position disagreement table. Agreement is not adjudicated truth.
4. Reproduce both original experiment-20 gates unchanged. Their outcomes stay
   in the record. This sample cannot retroactively make a failed gate pass,
   and no new model-performance claim is made from selected audit pages.
5. Use the independent code audit to distinguish implementation defects,
   layout assumptions, exposure and overstrong interpretations. New analyses
   must be labelled post hoc relative to the historical readings.

The separate source-access task seeks metadata and public manuscript access.
It must not expose a new manuscript's square letters before a collation or
validation plan is frozen. No paid acquisition or external message is authorized.

PRIMARY source: [Warburg print](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf),
local unchanged PDF and experiment-18 square-only crops. Repository process:
`AGENTS.md`; rubric: `rubric/RUBRIC.md`; deep-dive template:
`puzzles/_template/README.md`. The main thread synthesizes; agents transcribe
or audit only.

# NEXT — handoff for the next session

**Last session:** 2026-09-20, continuation after `3d38e79`.
**Where it stopped:** experiments 12–19 reviewed and key outputs reproduced.
Experiment 20's legibility bug is guarded by a separate tested scorer,
committed as `b8ed565`. No Warburg square image was opened in this session.

## Do first

Resolve the pending reader-model question, then run experiment 20. The frozen
protocol and AGENTS.md specify two independent Opus readers. Native subagents
here offer GPT models. Greg was asked to permit a documented pre-reading
substitution of two isolated GPT readers; **no answer has arrived yet**.
The previous session records an Opus account-limit failure. Do not assume
approval or spend money to work around that boundary.

Everything needed is local:

- Source: `sources/warburg-1853.pdf`; provenance and SHA-256 in
  `sources/caption-first-e2/README.md`.
- Square-only pages: `analysis/18-german-captions/out/squares/`, 55 PNGs.
  Layout ownership: `mask-index.json`, `layout-*.json`; do not show captions
  or model outputs to readers. `bands.py` and `mask_pages.py` reproduce crops.
- Protocol and frozen predictions: `analysis/20-warburg-witness/`.
  Read its `README.md` and `PREFLIGHT.md` before dispatch. Original freeze
  `a4e2ad6` is unchanged. Record any permitted model amendment before reading.
- Each reader writes a separate JSON file with model/exposure metadata and
  `items` containing chapter, number, PDF page, literal uppercase rows,
  `?` for uncertain letters, `.` for blanks, and notes for unreadable items.
  Do not share answers between readers or repair letters to fit symmetry.
- Run `python3 score_checked.py READER_DIRECTORY`, then the same with
  `--check`. Preserve raw readings, checked results and consensus squares.
  The old `score.py` is retained for audit; do not use its legibility gate.

If the gate fails, name the resolution/shape wall and stop. If it passes,
report coverage, rejected shapes, conflicts, same-number and secondary
realigned scores separately. Then update canon, hypotheses, the catalog and
TK-005. Do not call a numerical A/B threshold proof of a full generator or
proof that historical letters were freely chosen.

## The supported construction account

1. Caption-guided German dictionary lookups retrieve a subset of seeds.
   Experiment 14 finds 21 chapter-level hits; experiment 19 confirms all 21
   on images. Experiment 18 gives 27 chapter-level German-caption hits.
   Selection of one alternative and exact per-square alignment remain open.
2. Symmetry predicts many missing borders. On experiment 13's flagged-unseen
   Dehn subset: 74/81 correct predictions, 10 abstentions.
3. Interior class is partly predictable: 137/177 on that subset. Exact letters
   score 55/177 versus 44/177 baseline. The full cohort, including pre-exposed
   records, gives 153/193 class and 61/193 letter versus 48/193 baseline.
4. Experiment 16 finds small contextual effects and no strong letter model:
   best 32.0% versus 28.6% class-only. This fails to recover a rule; it does
   not prove that the compiler chose letters freely. H16 remains open as a
   compound claim; its class clause has support.
5. Hebrew near matches and a post hoc Greek lead explain part of the seed
   residue. The 105–110 estimate is exploratory. OCR recall 15/36 in sampled
   entries cannot simply be used to double the seed count. H22 remains open.

## What is finished

Experiments 12–19 have outputs. Do not repeat the old handoff's Greek-index,
caption-nomination, image-hit-reading or interior-context tasks. E1 and E2
remain as originally recorded. No new historical witness score was produced.

Verification this session: experiment 20 predictions and experiment 18 results
pass `--check`; experiments 13, 16, 19 produce byte-identical results. Eight
synthetic preflight tests pass. The new gate counts `?/?` positions, checks
both prediction hashes and dependencies, rejects malformed reader records,
and suppresses historical scoring on unreadable input.

## Exposure and remaining limits

Mathers fully exposed. Dehn edited readings exposed; 5/1 and 5/2 were already
partly known before experiment 13. Warburg chapter-4 moon/water material was
seen in earlier source extraction; chapter 5 is caption-development data.
The remainder has no saved reader output. The historical log records failed
reader dispatches, so do not make claims about those agents' internal access.
No untouched-manuscript score or established witness independence exists.

The original reconstruction requirement still stands: a frozen procedure
must choose inputs and predict independent interior letters on new evidence.
Current results support only part of that requirement. Blank interiors may
require witness collation even if the construction account becomes clearer.

Other open work: ten Mathers layout exclusions, print audit, label 25/4 among
chapter 24, Dresden N 111 and HAB access, an earlier dictionary edition,
Greek-lead replication, and all-witness collation. TK-005 remains open.

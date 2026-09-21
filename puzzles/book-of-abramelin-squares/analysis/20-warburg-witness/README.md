# 20 — Warburg witness test

**Status, 2026-09-20:** predictions frozen; historical reading and scoring
pending. Eight synthetic preflight tests pass. No historical result exists.

The next test asks whether the models frozen on Mathers predict letters in
the Warburg print and whether German captions retrieve its own seed words.
PRIMARY — [Warburg source record](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf).
Source PDF and square-only crops already exist locally; no acquisition is
needed. The library catalogues the print as Stuttgart 1853, a facsimile reprint
of the 1725 imprint. Historical ancestry remains unresolved.

## Frozen material

- `PROTOCOL.md`, `predict.py`, `predictions.json`, `freeze.json`, `score.py`:
  original freeze in `a4e2ad6`; unchanged by this continuation.
- Predictions cover cells missing from Mathers. The numerical criteria remain
  at least 50 interior cells, A at letter accuracy >= 0.50, and B below 0.40
  with class accuracy >= 0.70. These are model-performance thresholds, not
  proof of a recovered generator or proof of historical free choice.
- Reading follows the protocol: two independent readers, square-only crops,
  literal row groups, explicit `?` and `.`, no correction to make symmetry fit.

## Preflight correction

The original scorer excludes `?/?` cells from its legibility denominator.
On a synthetic 5 by 5 grid containing one agreed letter and 24 unreadable
cells, it counts only one lettered cell. The corrected gate counts 25 and
reports 4% agreement, so historical scoring stops.

`score_checked.py` imports the original scorer without changing its models.
It checks both prediction freezes and all pinned dependencies, validates
reader records, applies the corrected gate, and writes separately named
outputs. Ragged items retain their top rows but cannot improve square
legibility. Their printed positions count conservatively against the gate.
See [PREFLIGHT.md](PREFLIGHT.md) and [synthetic result](preflight-results.json).

## Run

```sh
python3 predict.py --check
python3 test_preflight.py
python3 score_checked.py PATH_TO_READER_FILES
python3 score_checked.py PATH_TO_READER_FILES --check
```

Each reader file is named `readings-A.json` or `readings-B.json` and contains
an `items` list. Every item has integer `chapter`, `number`, `page` (1-based
PDF page), and literal uppercase `rows`. A wholly unreadable item needs an
empty `rows` list and an explanatory `note`; do not silently omit it. Each
reader file must record the reader model and what it was allowed to see.

Reader identifiers must agree before scoring. Reconcile only coverage and
locators; never reconcile letters by looking at the other reader's answers.
Both source files remain the evidence even when the readers disagree.

`results-checked.json` contains model scores only if the gate passes.
`warburg-squares-checked.json` records agreed cells separately from raw
readings. The checked-in manifest pins dependencies relative to the repo root.

## Named limit and next action

No reader was dispatched in this continuation. Native agents offer GPT
models; Opus is specified by both AGENTS.md and the frozen protocol. The
previous session also records an Opus account-limit failure before any reader
output. A pre-reading model substitution is pending Greg's answer. Until
resolved, the existing square-only images remain unopened in this session.

After the reading, preserve rejected shapes, exposure, coverage and
disagreements. Chapter 4 moon/water material was previously exposed; chapter 5
was used for caption development. The frozen same-number alignment and its
post hoc realignment must remain separate. A print corroborates transmission;
it does not by itself establish manuscript independence or the original rule.

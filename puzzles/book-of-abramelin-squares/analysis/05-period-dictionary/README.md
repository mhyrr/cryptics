# 05 — Period dictionary: source gate and synthetic preflight

**Historical experiment blocked. No independent lexicon or historical score.**
The image packet acquired in `d812620` has now been inspected. The six cited
Latin dictionary readings are verified against facsimiles, with alternatives,
entry boundaries and uncertainties recorded separately from the claimant text.
Read [FACSIMILE-FINDINGS.md](FACSIMILE-FINDINGS.md) for the result and construction
limit. The earlier comparison edition and justified interior placements remain
missing. No independent evaluation lexicon has been extracted.

[SOURCE-AUDIT.md](SOURCE-AUDIT.md) preserves the earlier access/discovery record.
[PROTOCOL.md](PROTOCOL.md) remains the unchanged preflight protocol; its access
status is historical. [IMAGE-REQUEST.md](IMAGE-REQUEST.md) is satisfied for the
two primary volumes, not for the earlier comparison edition.

## Files and boundaries

- `claims.json`: six short quotations from the edition's reported dictionary
  correspondences, with headwords and note locators. Its original unverified
  flags are preserved as part of the frozen preflight; the new facsimile audit
  supersedes that verification status. This file is not a lexicon.
- `synthetic.json`: artificial vocabulary and square, unrelated to historical
  language. Created before solver implementation. No corpus-derived words.
- `freeze.json`: hashes of protocol, claims and synthetic inputs fixed before
  running the solver. This freezes a preflight, not a historical evaluation.
- `run.py`: exact finite lexical assignments on fixed paths under transpose
  plus half-turn symmetry. Counts every remaining alphabet assignment through
  explicit free orbits. No truncation, approximate matching, likelihood ranking
  or choice of the most attractive completion. Takes masked cells, not truth.
- `results.json` and `RESULTS.md`: source spelling comparisons and synthetic
  checks only. Historical fields are null, not zero. No result is written into
  any source transcription. Every compatible branch is saved with its free
  orbit domains; this factorization exhaustively represents the completions.

- `facsimile-readings.json`: image-read discovery excerpts, alternatives,
  boundaries and uncertainties; not a full transcription or independent lexicon.
- `audit_facsimiles.py` and `facsimile-audit.json`: source checksum checks,
  explicit layout/spelling operations and comparison with the six quotations.
  Six dictionary quotations agree; three quoted square spellings agree. This
  is a selected-example audit, not predictive accuracy. See FACSIMILE-FINDINGS.

## Run

Python standard library only, from the repository root:

```sh
python3 puzzles/book-of-abramelin-squares/analysis/05-period-dictionary/audit_facsimiles.py --check
python3 -m unittest discover -s puzzles/book-of-abramelin-squares/analysis/05-period-dictionary -p 'test_*.py' -v
python3 puzzles/book-of-abramelin-squares/analysis/05-period-dictionary/run.py
PYTHONHASHSEED=7919 python3 puzzles/book-of-abramelin-squares/analysis/05-period-dictionary/run.py --check
```

The solver imports orbit and scoring helpers from `analysis/stressbench/common.py`.
It never loads the Mathers corpus or tests a German reading. Tests independently
enumerate small squares to check counts and consensus; they also check planted
recovery, competing completions, contradictions, duplicate domains and refusal
to equate altered spellings. The report includes errors, abstentions, coverage,
complete-square recovery and a vocabulary-mode baseline for the synthetic cases.
These software checks cannot estimate historical performance or statistical power.

## Wall and next experiment

Missing: independent justification of an interior word's placement, a
preselected vocabulary sample and caption mapping, and an earlier comparison
edition for the error claim. The six acquired entries do not fix coordinates.
Test **fixed interior lexical placement** with whole-orbit concealment only
after those historical inputs are declared and frozen. Full row-and-column
word squares are not supported by the inspected evidence.

Do not reuse the synthetic toy vocabulary or the six claimant examples as an
independent period lexicon. Do not treat these checks as experiment 05 historical
success or failure. No incomplete-square prediction should proceed to witness
comparison until the source and evaluation gates in the protocol pass.

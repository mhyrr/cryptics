# 05 — Period dictionary: source gate and synthetic preflight

**Historical experiment blocked. No independent lexicon or historical score.**
This session identifies the precise dictionary, audits the accessible claimant
argument, and leaves reproducible constraint machinery. It does not complete
the requested independent correspondence checks or test Abramelin reconstruction.

Read [SOURCE-AUDIT.md](SOURCE-AUDIT.md) for sources, failed access routes,
exposed examples and the exact missing input. Read [PROTOCOL.md](PROTOCOL.md)
for the recipe, falsifiable predictions and controls written before code.

The continuation from `34b1f43` could not acquire images: the required browser
execution tool is absent, Tidewave has no connected browser, and web retrieval
failed. [IMAGE-REQUEST.md](IMAGE-REQUEST.md) specifies the two volumes, six
headwords, page context, image quality and locator record needed to resume.
The scan-download/capture fallback is also unfulfilled. No historical inputs
or scores were added; the existing freeze remains unchanged.

## Files and boundaries

- `claims.json`: six short quotations from the edition's reported dictionary
  correspondences, with headwords and note locators. All are unverified against
  dictionary facsimiles and exposed. This file is not a lexicon.
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

## Run

Python standard library only, from the repository root:

```sh
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

Missing: legible dictionary entry images, a source-independent vocabulary sample,
and evidence fixing an interior word's placement. Catalogues and modern quoted
examples cannot substitute for these inputs. Obtain the images listed in
`SOURCE-AUDIT.md`, then freeze a contiguous entry sample and caption mapping.
Test **fixed interior lexical placement** with whole-orbit concealment; retain
seed selection as a separate, weaker question. Full row-and-column word squares
are not supported by the currently retrieved argument.

Do not reuse the synthetic toy vocabulary or the six claimant examples as an
independent period lexicon. Do not treat these checks as experiment 05 historical
success or failure. No incomplete-square prediction should proceed to witness
comparison until the source and evaluation gates in the protocol pass.

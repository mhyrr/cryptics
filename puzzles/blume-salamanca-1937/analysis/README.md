# analysis/

One subfolder per experiment: `NN-short-name/` with its own `README.md` stating the question, the method, how to
run it, and the result. Heavy outputs go in `out/` (gitignored); summaries are checked in.

| # | Experiment | Question | Result | Bears on |
|---|---|---|---|---|
| 01 | `01-solver` | Can a Lasry-style IDP search recover double columnar keys at 615 letters, and in which bands? | in progress | H1, H2, H3 |
| 02 | `02-shared-repeats` | Do T1 and T2 share more strings than chance? | yes: 9 shared 4-grams vs 2.2 (p = 0.001); APMOEP (p = 0.011); within-T1 repeats at chance | H1, H2, H5 |

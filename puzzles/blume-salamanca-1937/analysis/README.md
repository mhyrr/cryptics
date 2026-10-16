# analysis/

One subfolder per experiment: `NN-short-name/` with its own `README.md` stating the question, the method, how to
run it, and the result. Heavy outputs go in `out/` (gitignored); summaries are checked in.

| # | Experiment | Question | Result | Bears on |
|---|---|---|---|---|
| 01 | `01-solver` | Can a Lasry-style IDP search recover double columnar keys at 615 letters, and in which bands? | yes for w1 2–15 × w2 12–15 (30/30); no for w2 ≥ 16 (cliff) | H1, H2, H3 |
| 03 | `03-target-h1` | Target runs: CC w1 2–15 × w2 12–15; joint CC w1 8–15 × w2 16–17; CR w1 2–15 × w2 12–15 | no candidate in any (best −6.00, −6.09, −6.02; threshold −5.10): all excluded | H1, H2, H3 |
| 02 | `02-shared-repeats` | Do T1 and T2 share more strings than chance? | yes: 9 shared 4-grams vs 2.2 (p = 0.001); APMOEP (p = 0.011); within-T1 repeats at chance | H1, H2, H5 |

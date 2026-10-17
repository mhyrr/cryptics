# analysis/

One subfolder per experiment: `NN-short-name/` with its own `README.md` stating the question, the method, how to
run it, and the result. Heavy outputs go in `out/` (gitignored); summaries are checked in.

| # | Experiment | Question | Result | Bears on |
|---|---|---|---|---|
| 01 | `01-solver` | Can a Lasry-style IDP search recover double columnar keys at 615 letters, and in which bands? | yes for w1 2–15 × w2 12–15 (30/30); no for w2 ≥ 16 (cliff) | H1, H2, H3 |
| 03 | `03-target-h1` | Target runs: CC w1 2–15 × w2 12–15; joint CC w1 8–15 × w2 16–17; CR w1 2–15 × w2 12–15 | no candidate in any (best −6.00, −6.09, −6.02; threshold −5.10): all excluded | H1, H2, H3 |
| 02 | `02-shared-repeats` | Do T1 and T2 share more strings than chance? | yes: 9 shared 4-grams vs 2.2 (p = 0.001); APMOEP (p = 0.011); within-T1 repeats at chance | H1, H2, H5 |
| 04 | `04-run-keeping` | Does either telegram keep plaintext runs (word, route, block families)? | no: T1 p = 0.53, T2 p = 0.61; plants 20/20; those families excluded | H4, H5 |
| 05 | `05-periodic` | Letters permuted within sets of n = 2–40, alone or one key on both? | no candidate (best −5.86); plants 78/78; excluded | H4, H5 |
| 06 | `06-grille` | Is T2 a 4 × 4 turning grille (all 1,024 keys, both uses)? | no: best −6.30; controls 10/10; excluded | H4 |
| 07 | `07-shared-model` | Which families, with a shared phrase and one key, produce the shared strings? | only single columnar and Nihilist by rows; both excluded (Bourdeau; `05` Nihilist control 72/72) | H1, H5 |
| 08 | `08-letter-fit` | Do the letter counts fit Spanish, Italian or Portuguese? | Spanish best but marginal (T1 p 0.08); Italian rejected for T1 (0.004); misfits X in T1, F in T2 | H3, all |

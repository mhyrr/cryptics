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
| 08 | `08-letter-fit` | Do the letter counts fit Spanish, Italian or Portuguese? | corrected 2026-10-17 (glossary book removed): none fits T1 well (es 0.014, pt 0.022, it 0.004); T2 es 0.024; misfits X and P in T1, F in T2 | H3, all |
| 09 | `09-odd-positions` | Where are the odd letters, and does their placement fit a whole-text transposition? | T1's last 20 letters rare-letter rich: location-corrected p 0.019 (1.8–3.1% of plants reach it); ends-only p 0.0001 but post hoc. X and F positions indistinguishable from body letters (p 0.73, 0.28). T2 nothing | H6, H8 |
| 10 | `10-convention-fit` | Does a writing convention explain the X, F misfits? | X for every stop overshoots (12.5 vs 6); only X nulls at T1's own rate fit (p ≈ 0.2). P is T1's largest misfit without PUNTO (z +4.8). Only F-as-stop fits T2; no source | H8, H9 |
| 11 | `11-one-or-two` | Same language, convention and system for T1 and T2? | yes: homogeneity p 0.21; F borderline (adjusted p 0.056); both rank Spanish first; no group-position structure (controls: power high at 615, low for random codewords at 160) | H2, H9, H12 |
| 12 | `12-type-diagnostics` | Which cipher type fits, against plants of 12 types? | transposition family only (plain, with nulls, mixed text, jargon then transposed); substitution, Vigenère, bifid, ADFGX, Playfair, homophonic, nomenclator, codebook excluded. T1 slightly flat (IC 5th, MIC 2nd percentile of plain) | H10, H11, H12 |
| 13 | `13-shared-strings` | Is the shared-string excess robust after look-elsewhere? | suggestive, not established: family-wise p 0.008 (shuffle), 0.020 (Spanish plants), 0.052 (bigram-preserving). Reversed: none. REF in both final groups: post hoc | H5, H7 |

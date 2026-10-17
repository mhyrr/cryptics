# Hypotheses

Numbered, never renumbered. Status: `open` / `supported` / `weakened` / `refuted` / `superseded by Hn`. Every
hypothesis names the test that would move it. Results are recorded in `research.md` and in `analysis/`.

| # | Hypothesis | Status | Test that would move it | Evidence so far |
|---|---|---|---|---|
| H0 | Prior field position (Bourdeau): a transposition of telegraphic Spanish; single transpositions, reversed systems, and forward double columnar with w2 ≤ 11 are excluded | taken as given (CLAIMANT) | Rerun as solver controls only | Bourdeau NOTES.md, 11 Oct 2026 |
| H1 | Forward double columnar, both keys ≥ 12, Spanish, telegram 1 alone | **refuted for w1 2–15 × w2 12–15**; open (untestable here) for w2 ≥ 16 and for w1 ≥ 16 | Region w2 ≥ 16 needs a method that passes a control there (joint attack H2, a crib, or a better score) | `03`: no candidate in 56 runs (best −6.00 vs threshold −5.10; controls 30/30). `02`: the shared strings are chance under this system (p ≈ 0.001–0.01). Agent B: no documented use in Spain 1936–37 |
| H2 | The same keys on both telegrams (joint attack) | **refuted for CC, w1 8–15 × w2 16–17** (and, via H1, any w1 ≤ 15, w2 ≤ 15); open for w2 ≥ 18 (joint control 1/5) | A method that passes a joint control at w2 ≥ 18 | `03`: 16 runs, best −6.09 vs −5.10; joint controls 8/10 |
| H3 | The language is not Spanish (Italian or Portuguese) | **refuted as an escape from H1/H2**: the exclusions hold for Italian and Portuguese too | — | `01` xlang control: the Spanish model recovers Italian and Portuguese plants 10/10, scoring above −5.10 |
| H4 | Another transposition family Bourdeau did not cover (disrupted columnar, Nihilist, route, nulls before transposition) | **refuted for** word transposition, row and serpentine routes (width 5–30), block moves (sets 3–12), letters permuted within sets of 2–40, Nihilist read by rows (w 5–40), and the 4 × 4 turning grille on T2 (alone or one key on both); open for disrupted columnar, Nihilist read by columns, nulls, sets offset by a preamble, larger grilles with nulls | A family from the open list with a planted control that passes | `04`: no bigram structure (p 0.53, 0.61), plants 20/20. `05`: periodic plants 78/78, Nihilist-by-rows plants 72/72, target best −5.86. `06`: grille, all 1,024 keys, best −6.30, controls 10/10. Survey: no period source ties any transposition to the Oswalds |
| H5 | The system keeps short runs of plaintext together, and both telegrams contain a common phrase (address, signature or stock opening), which survives as the shared strings APMOEP, NOCU and OEPM (Bean, issue 37) | **refuted** as stated (neither telegram keeps runs) and **refuted** in its weaker form for every family tested: the only families where a shared phrase produces the shared strings (single columnar, Nihilist by rows) are excluded | A system not yet modelled that keeps row or column runs across messages without keeping letter pairs within one | `07`: a shared phrase gives 9+ shared 4-grams only under single columnar and Nihilist by rows; double columnar of any tested length and Nihilist by columns stay at chance. Both run-keeping families excluded (Bourdeau; `05`) |

## Notes
- CR convention (stage 1 rows→columns, stage 2 columns→rows): excluded for w1 2–15 × w2 12–15 (`03`, best −6.02;
  controls 8/10). It is part of H1's family and gets no number of its own.
- The pass rule for H1–H3 is pre-registered in `analysis/01-solver/README.md`: at least 80% full recovery over at
  least 10 trials per band, at the target's time budget. A band that fails is "not testable with this method".
- H5 is listed because of a measured anomaly (`02`), not because of a preferred system.

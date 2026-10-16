# Hypotheses

Numbered, never renumbered. Status: `open` / `supported` / `weakened` / `refuted` / `superseded by Hn`. Every
hypothesis names the test that would move it. Results are recorded in `research.md` and in `analysis/`.

| # | Hypothesis | Status | Test that would move it | Evidence so far |
|---|---|---|---|---|
| H0 | Prior field position (Bourdeau): a transposition of telegraphic Spanish; single transpositions, reversed systems, and forward double columnar with w2 ≤ 11 are excluded | taken as given (CLAIMANT) | Rerun as solver controls only | Bourdeau NOTES.md, 11 Oct 2026 |
| H1 | Forward double columnar, both keys ≥ 12, Spanish, telegram 1 alone | **refuted for w1 2–15 × w2 12–15**; open (untestable here) for w2 ≥ 16 and for w1 ≥ 16 | Region w2 ≥ 16 needs a method that passes a control there (joint attack H2, a crib, or a better score) | `03`: no candidate in 56 runs (best −6.00 vs threshold −5.10; controls 30/30). `02`: the shared strings are chance under this system (p ≈ 0.001–0.01). Agent B: no documented use in Spain 1936–37 |
| H2 | The same keys on both telegrams (joint attack) | **refuted for CC, w1 8–15 × w2 16–17** (and, via H1, any w1 ≤ 15, w2 ≤ 15); open for w2 ≥ 18 (joint control 1/5) | A method that passes a joint control at w2 ≥ 18 | `03`: 16 runs, best −6.09 vs −5.10; joint controls 8/10 |
| H3 | The language is not Spanish (Italian or Portuguese) | **refuted as an escape from H1/H2**: the exclusions hold for Italian and Portuguese too | — | `01` xlang control: the Spanish model recovers Italian and Portuguese plants 10/10, scoring above −5.10 |
| H4 | Another transposition family Bourdeau did not cover (disrupted columnar, Nihilist, route, nulls before transposition) | open, not started | Needs a family with documented 1937 use (AGENTS rule; prompt) | Agent B found none documented for Spain 1936–37 |
| H5 | The system keeps short runs of plaintext together, and both telegrams contain a common phrase (address, signature or stock opening), which survives as the shared strings APMOEP, NOCU and OEPM (Bean, issue 37) | open | Find a transposition (block, word, route or incomplete) under which the shared 4-grams align to one plaintext phrase. Or plant a common phrase under double columnar and measure how often shared 6-grams appear | `02`: 9 shared 4-grams vs 2.2 expected; T2 opens NOCUOAPMOEPM |

## Notes
- CR convention (stage 1 rows→columns, stage 2 columns→rows): excluded for w1 2–15 × w2 12–15 (`03`, best −6.02;
  controls 8/10). It is part of H1's family and gets no number of its own.
- The pass rule for H1–H3 is pre-registered in `analysis/01-solver/README.md`: at least 80% full recovery over at
  least 10 trials per band, at the target's time budget. A band that fails is "not testable with this method".
- H5 is listed because of a measured anomaly (`02`), not because of a preferred system.

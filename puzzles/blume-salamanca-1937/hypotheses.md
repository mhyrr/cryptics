# Hypotheses

Numbered, never renumbered. Status: `open` / `supported` / `weakened` / `refuted` / `superseded by Hn`. Every
hypothesis names the test that would move it. Results are recorded in `research.md` and in `analysis/`.

| # | Hypothesis | Status | Test that would move it | Evidence so far |
|---|---|---|---|---|
| H0 | Prior field position (Bourdeau): a transposition of telegraphic Spanish; single transpositions, reversed systems, and forward double columnar with w2 ≤ 11 are excluded | taken as given (CLAIMANT) | Rerun as solver controls only | Bourdeau NOTES.md, 11 Oct 2026 |
| H1 | Forward double columnar, both keys ≥ 12, Spanish, telegram 1 alone | open, weakened | Matched control by key band (`01-solver`), then target runs in the bands that pass | `02`: the shared strings are chance under this system (p ≈ 0.001–0.01). Agent B: no documented use in Spain 1936–37 |
| H2 | The same keys on both telegrams (joint attack) | open | Joint control at 615 + 160, then joint target | Same day, same sender, same office. `02` weakens it as for H1 |
| H3 | The language is not Spanish (Italian or Portuguese) | open | Only if H1's control passes and its target fails | Bourdeau's chi-squared favours Spanish/Latin/French. Agent B: context points to Spanish, and no W argues against German |
| H4 | Another transposition family Bourdeau did not cover (disrupted columnar, Nihilist, route, nulls before transposition) | open, not started | Needs a family with documented 1937 use (AGENTS rule; prompt) | Agent B found none documented for Spain 1936–37 |
| H5 | The system keeps short runs of plaintext together, and both telegrams contain a common phrase (address, signature or stock opening), which survives as the shared strings APMOEP, NOCU and OEPM (Bean, issue 37) | open | Find a transposition (block, word, route or incomplete) under which the shared 4-grams align to one plaintext phrase. Or plant a common phrase under double columnar and measure how often shared 6-grams appear | `02`: 9 shared 4-grams vs 2.2 expected; T2 opens NOCUOAPMOEPM |

## Notes
- The pass rule for H1–H3 is pre-registered in `analysis/01-solver/README.md`: at least 80% full recovery over at
  least 10 trials per band, at the target's time budget. A band that fails is "not testable with this method".
- H5 is listed because of a measured anomaly (`02`), not because of a preferred system.

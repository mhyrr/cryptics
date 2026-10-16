# NEXT — handoff for the next session

**Last session:** 2026-10-16 (opened)
**Where it stopped:** Double columnar is excluded wherever our Lasry-style solver passes a planted control:

| region (telegram 1, Spanish/Italian/Portuguese) | controls | target |
|---|---|---|
| CC, w1 2–15 × w2 12–15 | 30/30 | best −6.00 vs threshold −5.10 |
| CC joint (both telegrams, shared keys), w1 8–15 × w2 16–17 | 8/10 | best −6.09 |
| CR, w1 2–15 × w2 12–15 | 8/10 | best −6.02 |

Together with Bourdeau's exhaustive w2 ≤ 11, CC is excluded for w2 ≤ 15 whenever w1 ≤ 15. The transcription is
settled against the archive scans. The shared strings between the telegrams (`analysis/02`, p ≈ 0.001) argue
against double columnar of any length.

## Do first
1. **Sourced survey of key type (H4/H5).** Greg asked about this; it waits on his go. One Opus agent, about 25
   fetches, writing `sources/key-type-survey.md`. Targets: (a) the 2020 Heinzmann / Matteotti / Liniger / Viveksanth
   attempt (Bochsler, *Nylon und Napalm*, note 44): what did they try? (b) Swiss army and commercial cipher manuals
   of the 1930s, and German and Spanish ones: which hand transpositions would a Swiss engineer use in 1937? (c) Weierud's
   history of Wehrmacht hand ciphers 1936–45, and any other Oswald cipher traffic. Output: named candidate systems,
   each with a source, ranked by whether they keep short plaintext runs (what `02` asks for).
2. **H5 test.** For each surveyed family that keeps runs, check whether T2's opening `NOCUOAPMOEPM` and T1's
   NOCU (17), OEPM (42) and APMOEP (263) can be one plaintext phrase in both messages. Write it as a script in
   `analysis/04-*`.
3. Only then build a solver for the surveyed family, with a planted control first (the `01-solver` pattern).

## Open questions
- Who or what is "Blume"? Probably a registered telegraphic address. Fuentes has a BNE *Anuario* 1936 lead (unread).
- What does the "Cde" stamp on telegram 2 mean, and why 14.00 rather than 15.98?
- Do the two w1 = 2 CR control "failures" read correctly with a long displacement? (They score as their true texts.)

## Named wall
**Double columnar, w2 ≥ 16 (alone) or ≥ 18 (jointly), or w1 ≥ 16.** At 615 + 160 letters the IDP has no gradient
beyond 3–4 swaps of the true key, so hill climbing cannot find it (`analysis/01-solver`, probe; Bourdeau saw the
same). Breach: a crib of 60–100 letters (Lasry's hybrid attack), the key phrases, a third message in the same keys,
or a new method that passes a control there. Do not widen this search without one of these.

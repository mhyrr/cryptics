# NEXT — handoff for the next session

**Last session:** 2026-10-20, session 10 (`analysis/26-k1-recovery`).
**Where it stopped:** K1 repair passes fresh controls; full T1 still gives no candidate in the declared band.
All controls and target cells are complete and independently verified. No search is running.

## Read first

- `26/README.md`, `26/results/summary.md`, `26/results/verification.txt` and `26/protocol.json`.
  Here `26/` means `analysis/26-k1-recovery/`.
- `26/scope-audit.md` for the short-K2/long-K1 coverage gap.
- `canon.md`, `hypotheses.md` and audit `23`. Search `research.md`, session 10, for the experiment record.

## What moved

K1 now uses the existing full transformation neighbourhood, with twelve restarts. K2 quadgram refinement
stays stochastic. The pipeline completes all four retained seeds instead of stopping on a score screen.
The Spanish model, -5.10 threshold, 20,000 IDP evaluations and CPU caps stay fixed. This is local search,
not an exact global solver.

The old experiment 25 failure recovers exactly with true K2 locked, as assisted development. Fresh isolated
controls then recover all thirty positives (twenty-nine exact; one permitted cyclic shift). Ten wrong-width
and ten shuffled negatives produce no candidates. The fifty-case isolated gate passes.

Fresh end-to-end controls supply first width, withholding both keys and plaintext:

| K2 stratum | exact recoveries | false candidates |
|---|---|---|
| exact active-list key | 10/10 | 0 |
| minimum one swap from original list | 10/10 | 0 |
| minimum two swaps | 9/10 | 0 |
| random conditioned on minimum distance >3 | 0/10 | 0 |

The missed two-swap case stays below threshold (-5.8084). Both complete gates pass. Commit `6d6b4f0`
freezes controls/protocol before target. Source/plan remain frozen at `698e38f`.

All twenty-two target cells finish, with four retained seeds each:

| body | first widths | best score | candidates | recorded CPU seconds |
|---|---|---|---|---|
| full 615-letter T1 | 12–22 | -5.9141 | 0 | 792.058 |
| one own-letter shuffle | 12–22 | -5.9484 | 0 | 764.828 |

Second-key lengths are 18–28; the scanner streams 1,286,188 original/one-swap keys per first width. The
independent verifier checks all ninety fresh controls, all target cells, all 88 target refinements and pins.
Total recorded solver work is 4,486.920 CPU seconds (74.782 CPU minutes), excluding development, prep,
compilation and verification. Wall-time snapshots are in `26/results/timing.json`; host load matters.

## Do first

**Test the uncovered short-K2/long-K1 band under a new plan.** Earlier validated target searches at second
lengths 12–17 had first width <=15. The phrase metadata includes shorter keys that 24–26 did not activate.
A bounded follow-up can start with first widths 16–22 and second lengths 12–17, using declared contextual
keys and fresh end-to-end controls before target. Do not expand finished experiment 26 or call all phrases spent.
First widths beyond 22 and other phrase lengths also need their own calibration.

The actual system/preparation remains unidentified. Transposition is a working hypothesis. Current controls
use modified novels, not period commercial telegrams. Independent period-text calibration and external key
material remain useful. The bounded follow-up on the reported 2020 study found no matching report;
`sources/heinzmann-search-2026-10-20.md` records it. The Bochsler request remains unsent.

## Named walls

- **Active band negative (`26`).** CC, full 615-letter T1, Spanish model, first widths 12–22, second lengths 18–28,
  finite phrase-neighbour expansion and fixed budgets produce no reading. This is not an exhaustive key
  or cipher exclusion. Another band requires a separate plan and passing controls.
- **Short-K2/long-K1 band untested.** The repaired K1 stage is promising, but supplied-K2 controls alone
  do not fill the blind-target gap. Breach: the bounded controlled follow-up above.
- **Historical system and preparation unknown.** Similar distributions do not prove shared systems/keys;
  Werner's wool story is testimony, not known plaintext. More traffic, key instructions, the 2020 report or
  historically grounded plaintext calibration would help. One shuffle supplies no p-value.
- **Arbitrary long-key recovery unvalidated.** Random off-list recovery is 0/10 here. More hardware alone
  does not demonstrate a usable search over all keys. T2 remains uncalibrated for this new solver.

## Open questions

- Who or what is BLUME? The telegraphic-address/directory lead remains open.
- What accounts for T1's excess P/X and T2's seven F's? No sourced convention fits them all.
- Are the REF.. endings meaningful or chance? Current evidence is post hoc.
- Does T1's poorly fitting end extend beyond its final 20 letters? Check 18/19 before another trim.
- Why does T2's Cde stamp give 14.00 rather than the reverse-side 15.98?

Finished result tags are immutable. No post-target tuning or wider blind campaign was started.

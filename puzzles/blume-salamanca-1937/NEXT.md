# NEXT — handoff for the next session

**Last session:** 2026-10-20, session 11 (`analysis/27-short-k2`).
**Where it stopped:** the short-second-key phrase search passes controls and produces no T1 candidate.
The full finite grid is complete. No search is running.

## Read first

- `analysis/27-short-k2/README.md`, `results/summary.md`, `results/verification.txt` and `protocol.json`.
- `analysis/26-k1-recovery/scope-audit.md` for the original coverage gap.
- `canon.md`, `hypotheses.md`; search `research.md`, session 11, for this attempt.

## What moved

The experiment reuses 26's full-neighbourhood K1 optimizer, stochastic K2 quadgram refinement and all-four-seed
protocol. It tests first widths 16–22 and second lengths 12–17. Filtering the existing full phrase metadata
gives 1,480 numeric keys; all one-rank-swap neighbours expand this to 160,327 unique keys. No new phrases,
model changes, preparation changes or post-target tuning. The final build passes 100 C/Python checks.

All forty fresh controls finish with true first width supplied and keys/plaintext withheld:

| K2 stratum | exact recoveries | false candidates |
|---|---:|---:|
| exact active-list key | 9/10 | 0 |
| minimum one rank swap | 10/10 | 0 |
| minimum two rank swaps | 9/10 | 0 |
| random, minimum original-list distance >3 | 0/10 | 0 |

The gate passes. The missed exact plant (22×14) loses its true key at shortlisting. This is a fallible
finite phrase search. The missed two-swap plant and every random case also stay below -5.10. Recorded
control cost: 511.967 process CPU seconds. Independent verification reconstructs all candidate bytes,
checks distance bounds and all forty plants/all 160 refinements. Source/plan freeze `fa32d99` precedes
controls; control/protocol freeze `5d99fe0` precedes target.

All fourteen target cells finish, four seeds each:

| body | first widths | second lengths | best score | candidates | CPU seconds |
|---|---|---|---:|---:|---:|
| full 615-letter T1 | 16–22 | 12–17 | -5.9662 | 0 | 86.510 |
| one own-letter shuffle | 16–22 | 12–17 | -5.9317 | 0 | 90.994 |

Threshold stays above -5.10. Total recorded solver work including controls: 689.471 CPU seconds
(11.491 CPU minutes), excluding prep/build/verification. Final independent checks cover all fourteen
cells, all 56 target refinements and protocol pins. One shuffle is descriptive, not a p-value.

Experiment 26 already tested the separate finite band first 12–22/second 18–28, also negative. The two
experiments do not exclude arbitrary keys or establish that all contextual phrases have been tried.

## Do first

**Return to historical key/system evidence and independent period-telegram calibration.** The measured
CPU cost makes bounded phrase tests feasible. The remaining problem is how to select historically supported
keys, preparation and plaintext. No further blind campaign is running or automatically queued.

The next evidence-led lead is BLUME's identity in telegraphic-address registers and Salamanca directories,
or more same-key traffic/key instructions in the archives. The bounded follow-up on the reported 2020
study found no matching report; `sources/heinzmann-search-2026-10-20.md` records the search. The Bochsler
request remains unsent. Do not send outreach without Greg's approval.

## Named walls

- **Finite phrase tests negative.** Full T1, CC, Spanish model and fixed budgets produce no reading in 26
  or 27. Shortlist loss means even an active-list key can be missed. Another test needs a separate frozen
  design and fresh controls; do not expand finished experiments after seeing their targets.
- **Arbitrary key recovery unvalidated.** Conditioned-random recovery is 0/10 in both bands. First widths
  above 22 and other phrase lengths also need calibration. More hardware alone establishes no usable
  arbitrary-key solver. T2 remains uncalibrated for this solver.
- **Historical system and preparation unknown.** Similar distributions do not prove shared systems/keys.
  Werner's wool story is testimony, not known plaintext. Current controls use modified novels, not period
  commercial telegrams. Independent period-text calibration, more traffic or key instructions would help.

## Open questions

- Who or what is BLUME? The telegraphic-address/directory lead remains open.
- What accounts for T1's excess P/X and T2's seven F's? No sourced convention fits them all.
- Are the REF.. endings meaningful or chance? Current evidence is post hoc.
- Does T1's poorly fitting end extend beyond its final 20 letters? Check 18/19 before another trim.
- Why does T2's Cde stamp give 14.00 rather than the reverse-side 15.98?

Finished result tags are immutable. No post-target tuning or independent T2 attack was started.

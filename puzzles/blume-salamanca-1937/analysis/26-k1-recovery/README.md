# 26 — isolate and repair first-key recovery

2026-10-20. Greg said to proceed after experiment 25 recovered an exact K2 but accepted a wrong K1.

## Design before implementation

Make one solver change: use experiment 21's existing full transformation neighbourhood for **K1 quadgram
climbing**, instead of the stochastic patience stop. Keep the same rank space, Spanish model, twelve
restarts, stochastic K2 quadgram refinement, 20,000 IDP evaluations, four retained seeds and -5.10 candidate
threshold. Do not change the threshold after inspecting a failed output. Full neighbourhood search is
still local optimization; it is not a proof of the correct key or historical system.
Also remove the score -triggered early stop between retained seeds: process all four, then select the best.
This protocol change applies identically to end-to-end controls and target cells. Scores label provisional
candidates; they do not certify a decipherment.

1. Reconstruct experiment 25's two-swap trial8. Give the new stage its true K2 and first width, but no K1 or
   plaintext. This is an assisted development diagnostic. If it cannot fix the known failure under the
   existing sixty-second process CPU cap, stop this attempt.
2. Freeze source/build/input hashes and a fresh isolated-stage plan before any new controls. Thirty positive
   plants supply true K2 and true first width, ten per band 12–15,16–18,19–22. Ten further controls supply true
   K2 but a uniformly selected wrong first width12–22. Ten shuffle controls supply true K2/width for an
   own-letter shuffle of the plant ciphertext. The C process receives no true K1 or plaintext. All use
  615-letter literary-proxy plaintext and uniformly random numeric keys (w2=18–28), with new deterministic
   seeds. This is assisted K1 calibration, not a blind double-columnar attack.
3. Isolated-stage gate: >=8/10 recoveries in each positive width band, >=95% plaintext agreement allowing
   cyclic shifts <=40, with exact/in-place metrics separately reported; zero false positive candidates among
   positives and zero candidates among wrong-width/shuffle negatives. Run every control. Any incomplete
   batch or CPU-cap hit blocks the gate; do not replace plants or increase caps.
4. Only after that gate passes, run forty fresh end-to-end controls with the same minimum-distance strata
   as experiment 25: ten exact-list, one-swap, two-swap and conditioned random (>3 swaps) keys. Supply the
   true first width, withhold keys/plaintext. Reuse the unchanged 1,286,188-key expansion and scanner; the
   K1 change applies to both seeded attempts. Require >=8/10 recoveries in each exact/one stratum and zero
   false candidates across all forty. Report two/random failures. Do not reuse experiment 25's results as
   fresh end-to-end controls.
5. Only if both complete gates pass, freeze a target protocol with all hashes. Run all eleven first widths
  12–22 on full 615-letter T1 and one own-letter shuffle, with identical per-width work and no global early
   stop. One shuffle is descriptive, not a p-value. No new phrase list, body edits or target tuning.

Use at most three workers. Scans retain their 180-second process CPU cap; each refinement process retains
sixty seconds. A failed gate ends this attempt. Preserve all results. No second fix within this experiment.
The current family, preparation and literary-corpus limitations from audit 23 remain. A candidate still needs
full independent decryption and validation against T2; a quadgram threshold alone is not a decipherment.

## Sources and scope

- PRIMARY implementation: pinned local `../21-dc-method/dcm.c`, `../25-seed-retention/seedsolve.c`,
  generators and input manifests. Historical claims are not added by this engineering experiment.
- SCHOLARLY algorithm context: Lasry thesis, chapter 9,
  https://kobra.uni-kassel.de/handle/123456789/15274 .
- PRIMARY upstream implementation referenced by 21:
  https://github.com/CrypToolProject/CrypTool-2/blob/main/CrypPlugins/ADFGVXAnalyzer/common/TranspositionTransformations.cs
  (path recorded in experiment 21's source audit; this session's web fetch did not verify the live page).

Commands, frozen protocol and results follow as each stage completes. No target run is authorized by an
incomplete or failed control batch.

## Development checkpoint

The old failed `holdout25_two_8` plant is recovered exactly with true K2 locked and first width 21 supplied:
score -4.0688, recorded 0.6 process CPU seconds. `results/development.json` records the full reading and build
pin. This excludes the development case from fresh gates. One hundred independent C/Python transformation
checks pass. Static review confirms K1 alone uses full-neighbourhood climbing, K2 remains stochastic, and
locked mode cannot mutate K2.

## Frozen fresh controls

Commit `698e38f` freezes the control plan, current build and plan/build/tag guards. The development build
is preserved separately; only a source comment and CLI guards changed before the fresh freeze.

The isolated stage completes **50/50** controls. Low/middle/high positive bands each recover **10/10**;
twenty-nine are exact and `iso26_high_1` is a complete cyclic shift of -1, as allowed by the declared rule.
Wrong-width and own-letter-shuffle groups each give **0/10 candidates**. K2 is locked throughout. The
isolated gate passes independent reconstruction, decryption and rescoring. Recorded CPU cost **14.0 seconds**.
This supplies K2 and width and does not establish end-to-end double-columnar recovery.

Fresh `holdout26` end-to-end controls complete **40/40**. Exact-list keys recover **10/10**, one-swap keys
**10/10**, two-swap keys **9/10**, and conditioned random keys **0/10**. Every recovery is exact. The missed
two-swap trial2 scores -5.8084 and stays below threshold; all random-key cases also stay below threshold.
There are **zero false candidates**, so the end-to-end gate passes. Each run finishes all four seeds.
Recorded end-to-end CPU cost is **2,916.034 seconds** (48.60 CPU minutes), separately from isolated/development
work. These are per-supplied-width controls on the same literary proxy, not uniform arbitrary-key recovery.

Both gates pass independent reconstruction, decryption and rescoring. `protocol.json` now pins the verified
control bytes and build; `results/pre-target-verification.txt` records the freeze check. Target run is next.

## Commands

With the pinned parent caches from experiments 24/25 available, run from this folder:

```
python3 -I run.py build
python3 -I run.py verify
python3 -I run.py isolated iso26 3
python3 -I run.py controls holdout26 3
python3 -I summarize.py > results/summary.md
python3 -I verify_results.py --output results/verification.txt
# Only after both full gates pass:
python3 -I freeze_protocol.py
# Commit the protocol/results before this dependent run:
python3 -I run.py target target26 3
```

Existing results cannot be overwritten. Do not rebuild or edit a frozen build during an active batch.
The isolated/fresh pipeline commands enforce the frozen tags. A rerun with different controls requires
a separate declared plan; the checked-in records remain the result of this plan.

## Coverage audit

`scope-audit.md` checks earlier ranges. First widths>=16 with second lengths 12–17 remain outside our
validated target region; the broader phrase metadata also contains inactive lengths. Experiment26 does
not fill these gaps. A negative result here cannot establish that the whole contextual phrase list is spent.

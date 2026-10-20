# NEXT — handoff for the next session

**Last session:** 2026-10-19, session 9 (`analysis/25-seed-retention`).
**Where it stopped:** expanded phrase-neighbour solver built and tested; acceptance gate failed.
No experiment 25 T1/shuffle run or target protocol. The latest target evidence remains experiment 24's negative.

## Read first

- `25/README.md`, `25/results/summary.md`, `25/results/verification.txt`, and `25/results/gate-diagnostic.json`
  for the new solver, complete controls and precise failure. Here `25/` means `analysis/25-seed-retention/`.
- Audit `23` for the limits of all earlier negative results and historical claims.
- `canon.md` and `hypotheses.md` for current facts and H13. Search `research.md`, sessions 8–9; do not reread it all.

## What moved

The five failed experiment 24 plants still fail when supplied both the true first width and base phrase
(0/5 assisted diagnostics). Merely keeping more base phrases was not an established fix. Experiment25
instead enumerates all original keys and their one-swap neighbours: **1,286,188 unique numeric keys**.

Fresh controls supply the true first width (12–22), with second lengths 18–28 and 615-letter literary-proxy
plaintext. Minimum distance is from the original list, not just the phrase used to generate a key.

| key stratum | exact recoveries | false candidates |
|---|---|---|
| exact list | 10/10 | 0 |
| one swap | 10/10 | 0 |
| two swaps | 9/10 | 1 |
| uniform random conditioned on minimum distance >3 | 0/10 | 0 |

The failed two-swap trial 8 (21x22) recovers **the exact K2**, but a wrong K1. Its quadgram score is -4.5505,
above the frozen -5.10 threshold; shifted agreement is only 0.4683. The score-only stop fires after one seed.
The zero-false-candidate gate therefore **FAILS**. No threshold or budget was changed to rescue it.
Fresh controls cost 3,242.504 process CPU seconds (54.04 CPU minutes), with three workers; this excludes
assisted development and the archived aborted run. Per-width calibration is not full unknown-width recovery.

A reporting fix required repeating the same forty seeds/plants. The original seven-row partial batch,
driver/build/plan and restart notice are archived and excluded. Corrected search was frozen in `3eeac16`.
The independent verifier checks all 40 transformations, scores, recovery/retention metrics and provenance,
plus the failure diagnosis. All controls completed under the fixed CPU caps.

## Do first

**If resuming solver engineering, isolate the first-key stage.** Use the developed failure for diagnosis,
then freeze fresh controls with a known-correct K2. Test K1 recovery and acceptance together before any new
T1 work. A higher threshold chosen from this failure is not independent validation. The current run is
finished; do not rerun or relabel it as a passing gate. Random long-key coverage is absent here.

**Evidence remains the better way to narrow the search.** Seek the reported 2020 Heinzmann study, BLUME's
registered telegraphic address, related drafts/replies or key instructions. The existing Bochsler outreach
is unsent. Do not send it without Greg's approval. A new key list needs pinned inputs and fresh controls.

**Historical-text calibration remains open.** Current plaintext plants are modified novels, not period
commercial telegrams. Separate correct-key recognition from blind recovery on independent historical
traffic. Vary STOP/X, abbreviations, nulls and transmission errors one at a time, outside the target.

## Named walls

- **First-key refinement and acceptance (`25`).** Exact K2 is not enough for the current pipeline. Breach:
  a fixed method that reliably recovers K1 and distinguishes failed outputs on fresh controls.
- **Finite phrase list spent on full T1 (`24`).** Best -5.8023 against -5.10; own-letter shuffle -5.9946,
  no candidate. Breach: externally grounded key material or an independently validated method change.
- **System and preparation unidentified (`23`).** Transposition is plausible, not established. Similar
  distributions do not establish shared systems/keys. Werner's wool story is testimony, not known plaintext.
  Breach: more traffic, key instructions, the 2020 study, or a historically grounded model with passing controls.
- **Arbitrary long-key double columnar.** `21` measured a narrow IDP basin; `25` recovers 0/10 conditioned
  random keys. These do not prove CPU impossibility. Better hardware alone does not identify the system.
- **Short T2 (`18`).** At 160 letters, some wider systems fit wrong keys better than the true key. T2 is not
  calibrated for the new phrase solver. More same-key traffic or an externally supported key would help.

## Open questions

- Who or what is BLUME? The registered-address/directory lead remains unread.
- What produces T1's excess P/X and T2's seven F's? No sourced preparation convention fits them all.
- Are the REF.. final groups meaningful or chance? Current evidence is post hoc.
- Does T1's poorly fitting end extend beyond its final 20 letters? Check `18`/`19` before proposing another trim.
- Why does T2's Cde stamp give 14.00 rather than the reverse-side 15.98?

No wider blind campaign is running. Preserve all failed hypotheses and checked-in outputs.

# Pilot 01: OEIS conjectures checked only to a stated bound

**Question.** The OEIS holds hundreds of conjectures of the form "verified for n < N".
A173419's "true for n < 1800" (2019) sat at the edge of its own b-file for seven
years and failed at p = 3359 (Patanè, Aug 2026). How many more are one cheap
extension away from a counterexample, and how far can an LLM + laptop push the
verified range for the rest?

**Why this pilot.** Ranked #5 of 77 in `sources/untouched-data/RANKING.md` and the
only top-10 candidate whose data *and* verifier are reachable from this container
(see `sources/untouched-data/06-wildcards.md` §1). The verifier is mechanical.

**Data.** `github.com/oeis/oeisdata`, commit `955686d544c877fea31b8aecae8b125f7dea6130`,
export `2026-10-15T03:00:24-04:00`. CC BY-SA 4.0. Not checked in (2 GB).

**Method.**
1. `extract.py` (code) → `candidates.tsv`: every non-dead `%C`/`%F` line that says
   "conjecture" and states a checked bound, minus entries where a later line
   mentions a counterexample/proof. 400,313 entries scanned; 27,310 conjecture
   lines; 730 candidates. Calibration: the 2019 A173419 line is extracted with
   bound 1800 (the settled entry itself is correctly dropped).
2. `prioritize.py` → `batch.tsv`: 152 entries (all "edge" cases where the bound
   ≈ the b-file end, plus bound < 10^5 with a PARI/Python program).
3. Checker agents (one per quarter of the batch): triage each line
   (finite-checkable / not), write **two independent checkers** that must agree with
   the entry's `%S` terms, extend to ~10× the stated bound under a CPU cap, record
   results in `results/batch-K.tsv`. Code in `checkers/Annnnnn/`.
4. Main thread: re-verify every claimed counterexample with a third checker.

**Result.** See `RESULT.md` (written after step 4).

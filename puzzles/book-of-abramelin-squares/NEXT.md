# NEXT — handoff

**Last updated:** 2026-09-26 (night). Experiments 23–25 are complete. The
construction recipe passed a pre-registered blind test on Dresden N 111.
The dive's next product is a paper, not another hunt for a generator.

## What moved

- **Construction types (23):** no seed-closed type (H26 weakened; calibrated,
  with a recorded post hoc estimator correction).
- **Square palette (24):** squares do not reuse their own interior letters
  (H27 weakened).
- **Blind Dresden test (25):** Book IV of N 111 ends on physical 272; 223
  grids on pages 246–272, read by two isolated Opus readers (8,756 agreed
  letters, 3 conflicts). Frozen Mathers predictions on 119 joined squares:
  symmetry 571/647 (0.88), class 1,475/1,728 (0.85), class-mode letter
  435/1,728 (0.25). Verdict **recipe holds** (H29 supported). Class follows
  the checkerboard in 97 % of cells where the seed alternates. Interior
  disagreement with Mathers 21.7 % against 7.3 % on the top row (H24
  supported). The copyist restored lost rows into symmetric squares (H28)
  and turned the dictionary seed MILCHAMAH into MILEHAMAH on 12.4.
  An independent verifier recomputed every count; corrections are in the
  experiment README. Start with [experiment 25](analysis/25-dresden-blind-test/README.md).

## Next steps toward a paper (Greg decides scope and venue)

1. **Novelty check with access.** Kollatsch's academia.edu item 127154626
   may now contain his second and third parts; full text needs a login.
   Our claim is the controlled, witness-validated test, not the qualitative
   observations he makes (alternation, dictionary source, symmetry typology).
2. **A second reader family.** Readers were all Opus 5.5. Have a different
   model or a human read a frozen random sample of about 20 Dresden grids;
   report agreement with the consensus.
3. **Information budget.** Compute, by code, the bits per square the recipe
   leaves open (seed given caption; class uncertainty; letter residue), with
   the Dresden figures as the out-of-sample check.
4. **The 63 unjoined grids.** 46 differ in size from the same-numbered
   Mathers square. An alignment study (captions, not letters) could add
   targets; it is post hoc and must say so.
5. **Catalog.** Status is `partial`; consider re-scoring `solvable` and
   `verifiable` in light of experiment 25 (Greg's call).

## Tools and verification

- Experiment 25: `access.py --fetch` restores the 52 pinned images;
  `crop.py --check`, `score.py --check`, `copyist.py --check`,
  `collation.py --check`, `sensitivity.py --check`; `test_score.py` has 12
  synthetic checks. The scorer refuses to run if a frozen prediction changes.
- Experiments 23 and 24: `run.py --check` in each; `corrected.py --check`
  in 23; 8 synthetic checks each.
- Experiment 22 tools are unchanged; its `access.py` restores only its own
  four images.

## Exposure and other open questions

The main thread has now seen the scored Dresden results and the copyist
pairs; it did not view page images. All Dresden Book IV pages are read, so
no untouched Dresden cohort remains. A further blind test needs another
witness (HAB 47.13 or 10.1 b, Dresden N 161) or a different model family.

H22's Greek test is still open. The earlier dictionary edition comparison,
Mathers print audit, ten excluded Mathers layouts and label 25/4 remain open.
No push or external message was sent.

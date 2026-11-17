# Next session — missing keys, 1500–1620

**Last session:** 2026-11-17, no. 2911 known-answer bench on the V/140 pair.

## Where it stopped

No blind variant passed on p1. The homophone rule failed its check. The
repeat-seeded trial tried both all-right starts in its shortlist and added no
sign to either. The selected provisional table marked no values. The
strongest blind result remains `v2_boot` (0.566 precision, 0.065 recall).
The frozen full pair and both bare letters were left held out. H6 is
weakened and H7 is open.

Read `items/2911/bench/README.md`, including the stop and diagnosis, and
the latest entry in `research.md`. The aggregate audit is in
`items/2911/bench/runs/v3_seed-p1-seed-audit.tsv`.

## Wall and what would breach it

A correct seed is too sparse for a rule that locks only one sign at a time
between exact, already-valued flanks. Reranking those seeds alone would
still leave both correct shortlisted starts at their starting values.

If the bench reopens, first isolate extension on a synthetic syllable
cipher with registered abridgement and sparse, spatially distributed
anchors. Test a lock that can infer values agreed on by every plausible
segmentation between two independent anchors. Keep p1 as development
and reserve full and the bare letters for the registered pass.

## Open questions

- Can this method extend a sparse correct start across omissions and
  spelling differences?
- Can a control score choose a right start and set a stage 4 bar without
  the period table (H7)?
- Do the transcription's base and mark combinations support a consistent
  split into consonant and vowel? The guide describes shapes only.

The scope stays on the 2911 bench until Greg opens another item.

# Next session — missing keys, 1500–1620

**Last session:** 2026-11-17, reopened no. 2911 known-answer bench.

## Where it stopped

The best blind p1 run (`v6_merge`) scored 0.575 precision and 0.155
recall. Eight marked rows matched the period key and two differed.
It got 206 places right, including 105 syllables, and 152 places wrong.
H6 is weakened. H7 is open. The variant limit was reached. The full pair
and both bare letters remain held out.

Read the reopened trials in `items/2911/bench/README.md` and the latest
entry in `research.md`. The scored table stays sealed. The error counts
are in `items/2911/bench/runs/v6_merge-p1-errors.tsv`.

## Wall and what would breach it

The bench can find small correct starts and combine evidence across
passages. Neither the single-sign nor the multi-sign rule can extend
them with enough independent observations. A successful merge can
carry wrong parent values beyond the exact span that verified the merge.

Before another 2911 builder, test per-value support and approximate
alignment on a synthetic syllable cipher with registered abridgement,
known sparse anchors and spelling differences. The controls run this
session covered local locks and merges only. A target with independent
anchors distributed through the letter would supply stronger evidence.

## Open questions

- Can approximate alignment extend a sparse correct table across
  spelling differences and gaps?
- Can a shuffled control score set the H7 threshold without an answer?
- Does the mark system predict any part of a sign's value? The guide
  describes shapes only.

Another item requires Greg to open the scope.

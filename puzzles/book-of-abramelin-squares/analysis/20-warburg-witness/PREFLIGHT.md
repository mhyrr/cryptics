# Pre-reading audit, 2026-09-20

The original protocol, scorer and predictions from `a4e2ad6` remain unchanged.
No Warburg square image has been opened in this session. Experiment 18's
caption-only results and experiment 20's chapter predictions reproduce.

## Corrections to implement before reading

1. Count `?` as an unresolved potentially lettered cell in the legibility
   denominator. The original `merge()` ignores positions where both readers
   write `?`. One agreed letter among 24 unreadable cells would therefore
   pass as 100% readable. Printed blanks and padded absent rows stay excluded.
2. Refuse duplicate item identifiers, invalid symbols and missing reader
   items. Preserve page locators and uncertainty in the reader files.
3. Check both prediction hashes, not only experiment 20's hash. Pin every
   computation input and script used by the scorer in a separate manifest.
4. Stop before historical scoring when the legibility gate fails. The
   original scorer emits accuracy and seed tests even after that failure.
5. Keep the original numerical thresholds and models. Report their outcome
   as a threshold result: crossing A cannot establish a caption-to-square
   generator, and crossing B cannot prove that untested rules do not exist.

Implement these in `score_checked.py`, which imports the frozen scorer. Test
them on synthetic reader files before exposing the witness. Save original
and corrected agreement counts so the change is inspectable.

## Limits that code cannot remove

- Two independent readings of one print are transcription checks, not two
  independent historical witnesses. Shared manuscript ancestry is unresolved.
- Chapter 4 moon/water material was exposed in earlier work. Chapter 5 was
  caption-development data. Report this rather than calling every cell blind.
- The print's row-list-to-square convention is a frozen assumption. Preserve
  ragged lists and missing rows; do not repair them into squares.
- Cell counts include symmetry-related positions. They are not independent
  trials and do not support binomial confidence claims.
- The post hoc Greek romanization is absent from experiment 20's seed scorer.
  This run cannot be described as its blind replication.

## Reader availability

The native subagent tool offers GPT models, whereas the protocol and repository
instructions require Opus. A model substitution was asked before any reader
ran. Until answered, prepare and test the scorer without exposing the images.

PRIMARY source metadata rechecked 2026-09-20: the [Warburg record](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf)
catalogues the item as Stuttgart 1853, a facsimile reprint of the 1725 imprint.
The existing local PDF is retained. This is a bibliographic description, not
an adjudication of the imprint date or the witness's ancestry.

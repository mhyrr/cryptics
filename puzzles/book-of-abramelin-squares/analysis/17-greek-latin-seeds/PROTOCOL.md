# 17 — Greek and Latin glosses, and the seed residue. Frozen before the run

Date: 2026-09-20. `romanize.py`, `build_vocab.py`, `residue.py` and this file
are committed before `build_vocab.py` or `residue.py` is run.

## Question

Experiment 12 matched 56 complete top rows to the dictionary's Hebrew
transliterations. What are the others? The dictionary also prints a Greek and
a Latin gloss in every entry. If the compiler took seeds from those columns
too, romanized Greek and plain Latin words will match unmatched top rows above
the shuffle control.

## Romanization (frozen in `romanize.py`)

Diacritics are stripped. Letter values: η and ε give E; ο and ω give O; θ TH;
ξ X; χ CH; ψ PS; ρ R; σ S. Closed variant list, all indexed: υ as Y or U; κ as
K or C; φ as PH or F; ου as OU or U; γ before γ κ ξ χ as N or G; a rough
breathing as H or nothing. At most 32 variants per word. Nothing else: no
itacism, no Latin endings (-os to -us), no case changes.

Exposure: the main thread has seen three Mathers top rows that look Greek
(OIKETIS, PROXONOS, YPARCHOS). They informed Y for υ, K for κ, CH for χ and
the dropped breathing. The scheme is otherwise the conventional one.

## Test

- Rows: complete top rows of analyzable Mathers squares, normalised as in
  experiment 12 (`rows_in_dictionary.norm`), that are not in experiment 12's
  vocabulary. Experiment 12 reported 56 of 232 top rows; its count includes
  only complete rows, and this script recomputes it.
- Vocabularies: romanized Greek; Latin-script body words; Latin-script words
  on or just after a line with Hebrew type (a wider harvest than experiment
  12's adjacent word). OCR f/s tolerance as in experiment 12.
- Tiers: exact; near (edit distance one, length five and up), as experiment 12.
- Control: experiment 12's `cv_shuffle` of each row, 200 draws, same
  vocabulary. A vocabulary counts as a seed source only if its exact matches
  clearly exceed its control. The Latin vocabulary is large, so its control
  will be high; the control is the point.
- Every residue row gets one label by fixed priority: hebrew_line exact,
  greek exact, latin exact, hebrew-adjacent near, greek near, unexplained.

## OCR gap

"OCR gap" cannot be decided by code. It is estimated in experiment 19 by
reading dictionary entries on the page image and comparing the transliterations
printed there with the OCR harvest.

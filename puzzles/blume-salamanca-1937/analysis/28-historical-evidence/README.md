# 28-historical-evidence: checks behind the historical-evidence pass

2026-10-20. Supports `sources/historical-evidence/README.md`. No target decryption, no solver run, no score.

## Question

Which numerical claims in the historical-evidence report need a script? Four:

1. Givierge's (1925) keyword numbering, ties left to right, reproduces his printed cryptogram.
2. His one-table "double transposition" (keyed column order plus one keyed row order), on a complete rectangle,
   becomes experiment 18's family (letters permuted within sets of n by one key, sets in any order) after a fixed
   rearrangement. Two writing directions:
   - write rows, read columns: cut the ciphertext into w chunks of h and read across, giving sets of w;
   - write columns, read rows: take every w-th letter, giving sets of h.
3. The complete-rectangle shapes of 615 and 160, and which set sizes fall in 18's tested bands (T1 n 8–50,
   T2 n 8–15).
4. Whether HE-K01's names are already single components of 24's phrase lists, and whether
   `solver-options.jsonl` is well formed.

## Run

From the repository root:

```
python3 -I puzzles/blume-salamanca-1937/analysis/28-historical-evidence/check.py > puzzles/blume-salamanca-1937/analysis/28-historical-evidence/result.txt
```

Standard library only. The reduction check uses plaintext indices, not text, with seed "28-reduction".

## Result (`result.txt`)

- MARSEILLE gives key 7 1 8 9 2 4 5 6 3, and the cryptogram matches Givierge's printed
  `AIRIX SREPS IIAEO CMNEL DAOSV TRIII` exactly.
- Both rearrangements give exactly 18's family on 200/200 random complete-rectangle keys.
- T1's complete shapes are 3 × 205, 5 × 123, 15 × 41, 41 × 15, 123 × 5 and 205 × 3. Only w 15 and 41 give set
  sizes inside 18's tested band (15, 41). For T2, w 8, 10, 16 and 20 give set sizes 8 or 10. 18 ran on the raw
  text, not on these rearrangements, so this family is untested. Experiment 20 rearranged only n × n squares.
- MORITZ VICTOR OSWALD, BANCO GUIPUZCOANO and MIRACONCHA are not in 24's lists. SAN SEBASTIAN and VICTOR OSWALD
  are.
- `solver-options.jsonl`: 7 records, unique IDs, no missing fields, none solver-ready, ranked HE-P01 then HE-C01.

## Limits

Incomplete rectangles (615 not divisible by w) give columns of unequal length that depend on the column key. The
rearrangement then needs a long-column assignment search, which is not covered here. That the family is in
Givierge and Hitt shows availability, not use by the Oswalds.

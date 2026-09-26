# Independent verification of experiment 25

A fresh Opus agent checked this on 2026-09-26 with its own stdlib script, working from the raw inputs. I did not import or run `score.py` or `copyist.py`; I read them only afterwards.

| Quantity | Mine = stored |
|---|---|
| Square grids, joins, joins with targets | 210, 147, 119 |
| Interior, border targets | 1728, 849 |
| M1 correct/wrong/abstain | 571/76/202 |
| M2 correct/wrong | 1475/253 |
| M3 filler, chapter, global | 435, 341, 302 |
| S1: squares, alternating, class | 118, 76, 1021/1055 vs 454/673 |
| S3 (all joins): top, border, interior | 64/876, 135/1182, 173/798 |
| C2: 11/3, 12/4, 18/3 | 18/18, 36/36, 28/28 |

**No numeric discrepancy.** Two small points:

- **Reporting.** `unjoined` leaves out `p265-c3-g2`. It fails the gate at 0/13, and 26/2 then joins `p266-c1-g1`, a later grid with a repeated "2", at 8/13.
- **C2 alignment.** C2 matches only under one-to-one alignment. The literal "no identical exemplar row" gives 11/3 only row 6, at 6/6.

## Bug checks: all clean

- Indexing is zero-based on both sides.
- The interior flag and the S3 zones are geometrically correct.
- Every exp-13 class label equals "V iff top-row vowel XOR odd row". The comparison runs in the right direction.
- No prediction falls on a cell Mathers prints. No cell is duplicated, and each id joins one grid.
- There is no lowercase or J in the inputs. `load_readings` upper-cases the readers against literal transcription, which is harmless here.
- The verdict rule is applied correctly.

## Concerns

1. **The gate is loose.** 38 joins agree below 0.8, holding 668 of the 2577 targets. Three sit at exactly 0.5. The verdict survives a split at 0.8:

   | Agreement | M1 | M2 | Filler |
   |---|---|---|---|
   | ≥ 0.8 | .894 | .838 | .244 |
   | < 0.8 | .833 | .899 | .275 |

2. **S6 is empty.** No reader wrote J, so it reproduces the primary run by construction.
3. **C3 for 26/2 is meaningless.** The pair is not Mathers 26/2 (the gate gives 0/13).
4. **C2 counts too many rows as added.** Exact identity counts one-letter corrections (12/4 rows 0 and 8; 18/3 rows 3 and 4) and rows that differ only by a reader's `?` (12/4 rows 5 and 6; 18/3 row 6). The rows actually missing still give 1.0: 8/8, 7/7 and 12/12 to 18/18. So the README's "82 of 82" is really about 27 to 33 cells.
5. **C2 adds nothing to C1.** C1 is 1.0 on all three corrections, which already implies C2.
6. **The mechanism is not shown.** A half-turn gives the same rows as "reading down the columns".
7. **C1 compares raw row indices.** A lost row shifts every later row, so the three correction "wins" come nearly for free.
8. **The corrections barely touch the scores.** They reach the primary targets only through 19/6: 8 interior and 2 border abstentions.

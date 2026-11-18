# No. 1336 — Speciano and Borromeo: run record

Opened 2026-11-17 on Greg's instruction ("find a message that has not been decrypted and does not yet have a
key"). Gate: `gate.md`. This is the first run of the key line after the 2911 bench, and the first clean test
of its builder (H6) and of a key nobody holds (H8).

## The material
| Piece | Folio | Role |
|---|---|---|
| cipher slip, 13 lines | F 47 inf. no. 131 c. 269r | **build pair**, cipher side |
| clear text, about 14 lines | F 47 inf. c. 270r ("vedasi il foglio seguente" on 269r points to it) | build pair, plain side |
| cipher slip, 3 lines | F 49 inf. no. 18 c. 44r | **transfer test**: decoded with the frozen key |
| clear note of two lines under that slip | same leaf | the answer to the transfer test, if it is the slip's decipherment. Kept out of the build |
| cipher line in brackets | F 131 inf. no. 7 c. 14r (4 July 1574) | **bare**: no decipherment on the page. The reading, if the key holds |

## What the main thread has seen (stated before any reader runs)
The main thread looked at all the page images to cut strips and write the sign guide. It saw that the cipher
has about one sign per letter of the clear text (about 550 signs to about 600 letters on the pair), and, on
c. 44r, that the repeat pattern of the slip's first signs fits the first words of the note under it. No value
from that look enters the key: values come from `align.py` on the readers' files of the F 47 pair only.

## Stages and bars (written before the readers ran)
1. **Readers** (Opus, isolated): cipher A and B read all three cipher passages; plain A and B read c. 270r and
   the note on c. 44r. `line/compare.py` gives agreement. Stop if cipher agreement on c. 269r is under 0.85
   after one guide revision (PIPELINE.md stage 2).
2. **Build** on the F 47 pair, both-readers-agree signs against the plain consensus, with
   `align.py build` (the pair looks complete). If that build stops on its null check, or leaves over 20% of
   the plain letters unaccounted, rebuild with `--abridged` and say so.
3. **Held-out on the pair** (`align.py heldout`, five folds): accuracy ≥ 0.85 on covered signs, coverage
   ≥ 0.70, shuffled control ≤ 0.30. Fail → no reading; record and stop.
4. **Transfer** (the stronger test): decode the c. 44r slip with the frozen key, compare with the note under
   it by `align.score`. Bar: accuracy ≥ 0.85 with at least 70% of the slip's signs valued, and the shuffled
   control ≤ 0.30. If the note is not the slip's decipherment the comparison fails for that reason and the
   decode is judged as a bare letter.
5. **Bare line** on c. 14r: decode by script. Reported with every unvalued sign shown, English beside the
   Italian, and the sentence of clear text it stands in. It is a reading only if stages 3 and 4 pass.

## Result of stage 1 (2026-11-17): the main slip fails the agreement bar
`results/agreement.tsv`, `results/agreement-c269-pairs.tsv`.

| Piece | Agreement |
|---|---|
| c. 269r, readers A and B (guide as frozen) | 0.779 |
| c. 269r, readers C and D (guide revision 1) | 0.807 |
| c. 269r, all six pairs of the four readers | 0.742 to 0.807 |
| c. 44r slip, A and B | 0.941 |
| c. 14r line, A and B | 0.750 |
| c. 270r clear text, PA and PB (words) | 0.928 |
| note on c. 44r, PA and PB (words) | 0.933 |

The slip on c. 269r has 15 lines and about 795 signs (the brief said 13 and about 550). **Wall for plan A: sign
legibility of c. 269r at the 750 px the archive serves** (no larger size is served: nine URL variants return
the same file). The disagreements are spread over many pairs of shapes; the largest is q against qx (13 of
about 130 in C against D). Reader D made one full pass, reader C a full second pass on lines 7–15 only.
Breach: a better image of F 47 inf. c. 269r from the Ambrosiana.

## Plan B (registered 2026-11-17 after the agreement figures, before any build)
This departs from the stages above and is stated as such. What the main thread knew when writing it: the
agreement figures; the plain consensus texts; that the c. 44r slip has 102 signs against a note of about 101
letters; and the by-eye pattern match stated above. No table had been built.

1. **Build on the c. 44r pair**: `align.py build` on the A-and-B consensus of the slip against the PA-and-PB
   consensus of the note. The pair is small, so few rows can reach `probable` (4 places). Two tables are
   written: `key-v0.tsv` as built, and the **provisional** table: every row whose value holds at 60% of its
   places, whatever the count.
2. **Test on c. 269r** (this replaces the transfer test; the roles of the two slips are swapped). Decode the
   C-and-D consensus of c. 269r with the provisional table and score it against the c. 270r text with
   `align.score`, against 20 tables with values shuffled within type. The cipher there has about 795 signs to
   about 600 letters of clear text, so part of it has no counterpart and accuracy cannot reach the usual 0.85.
   **Bar: accuracy ≥ 0.55 on decoded letters, shuffled control ≤ 0.30, and at least 60% of the signs valued.**
   Fail → no reading of c. 14r.
3. **Bare line on c. 14r**: decode with the provisional table; each sign shown; unvalued signs as `?`.
   Two readers agree on only 0.750 of that line, so both readers' versions are decoded and shown.
4. If 2 passes: widen the table with `align.py build --abridged` on c. 269r against c. 270r, check that it
   does not contradict the c. 44r table (count of signs valued differently), and report it as a second,
   weaker table.

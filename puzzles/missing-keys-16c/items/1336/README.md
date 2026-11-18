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

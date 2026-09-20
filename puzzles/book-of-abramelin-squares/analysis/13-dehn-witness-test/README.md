# 13 — Frozen interior predictions scored against the Dehn readings

**Result.** Symmetry recovers border letters of a German-based witness at 92 %.
Interior letters follow a vowel/consonant checkerboard at 79 %. The letter
itself is predictable at only 32 %, against 25 % for the most common letter.

Peterson's web edition, the project's pinned source, prints `D:` readings from
Georg Dehn's German-based edition in its note column. The project had not used
them. `parse_dehn.py` extracts 79 square readings. The models were committed
in `469663f` before the readings were parsed; see [PROTOCOL.md](PROTOCOL.md).

## Scores on cells blank in Mathers and present in Dehn

Frozen alignment (same square number, same size, visible cells agree at least
half): 14 squares.

| Model | Zone | Correct | Wrong | Abstain |
|---|---|---:|---:|---:|
| transpose plus half-turn (experiment 01, committed 16 Sept) | border | 83 | 7 | 10 |
| same | interior | 6 | 2 | 185 |
| vowel/consonant checkerboard (class only) | interior | 153 | 40 | 0 |
| checkerboard, then most common vowel A or consonant R | interior | 61 | 132 | 0 |
| most common letter A | interior | 48 | 145 | 0 |

Excluding 5/1 and 5/2, which were seen before the freeze, changes no
percentage by more than two points. `results.json` has every cell count.

Post hoc realignment (`score.py --realign`, not in the frozen protocol): Dehn
numbers squares differently inside a chapter, so a reading is moved to the
same-chapter, same-size Mathers square it best matches on visible cells. This
scores 19 squares: symmetry border 108 of 117, checkerboard interior 220 of
277, letter filler 78 of 277, most common letter 61 of 277.

## Description of the Dehn readings

60 readings are clean squares. 31 satisfy transpose exactly, 27 also half-turn.
809 of 1,086 interior cells (74 %) follow the checkerboard. On cells visible
in both witnesses, Mathers and Dehn differ on 28 of 298 top-row cells, 53 of
567 other border cells and 71 of 563 interior cells.

## What this means

H4 now has witness support: the symmetry fills are mostly right where they
speak, and they speak almost only on borders. The interior is pronounceable
filler: alternate vowels and consonants down from the seed word. Inside that
constraint the letter choice carries little signal that these models can
recover. No generator is established.

## Limits

Dehn's text is a modern edition compared across German manuscripts, reached
through Peterson's notes. It may contain corrections. It is not an untouched
manuscript witness, and H5's caution applies. 29 readings stay unaligned,
mostly because their rows are ragged in Peterson's note. The Dehn readings for
chapters 1 to 14 are now exposed to the project.

## Reproduce

```sh
cd puzzles/book-of-abramelin-squares/analysis/13-dehn-witness-test
python3 predict.py --check
python3 parse_dehn.py
python3 score.py
python3 score.py --realign
```

`parse_dehn.py` needs the cached page `sources/cache/e2/mathers.html`
(gitignored; sha256 in `dehn-readings.json`). `dehn-readings.json` is checked in.

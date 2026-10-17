# 04-run-keeping — does either telegram keep runs of plaintext?

**Question.** H5 asks for a system that keeps short plaintext runs together. The survey
(`sources/key-type-survey.md`) names the period families that do: word transposition, route tables read by rows
(including serpentine), block moves of whole sets, and, in part, letters permuted within sets and the turning
grille. Does either telegram show the letter-pair structure that any of these would leave?

**Method.** `runs.py`. Statistic: the mean Spanish bigram log10 probability of adjacent ciphertext letters, read
forward and reversed, taking the larger. Each text is compared with shuffles of its own letters, so letter
frequency drops out. Plants: 20 per family per length (615 and 160), telegraph-style held-out Spanish from
`01-solver/plaintext.py`, parameter drawn uniformly from the range shown in the script. Single and double columnar
plants are negative controls. Run: `python3 -I runs.py > result.txt` (about 1 minute).

**Decision rule (fixed before the run).** A family is testable at a length if at least 95% of its plants reach
p < 0.01 against their own shuffles. A testable family is excluded for a telegram if that telegram does not reach
p < 0.01.

**Result** (`result.txt`).
| family | detected at 615 | at 160 | verdict |
|---|---|---|---|
| word transposition | 20/20 | 20/20 | **excluded** for T1 and T2 |
| row permutation, width 5–30 | 20/20 | 20/20 | **excluded** |
| serpentine rows, permuted, width 5–30 | 20/20 | 20/20 | **excluded** |
| block move, sets of 3–12 | 20/20 | 20/20 | **excluded** |
| letters permuted within sets of 3–12 | 13/20 | 11/20 | not testable this way (see `05`) |
| turning grille, side 4, 6, 8 | 17/20 | 2/20 | not testable this way |
| negative control: single columnar | 1/20 | 0/20 | — |
| negative control: double columnar | 0/20 | 1/20 | — |

T1: p = 0.53. T2: p = 0.61. Neither telegram has any bigram structure of its own, forward or reversed.

**Reading.** Neither message keeps plaintext runs internally. The shared strings of `02` therefore cannot be
plaintext runs that survived the transposition in each message. They need one of two things. Either the same key
maps a shared stretch of plaintext to matching ciphertext positions in both telegrams without keeping its letters
adjacent, or the shared strings are chance (p ≈ 0.001 says this is unlikely, but `02` chose n after looking).

The match offsets T1 − T2 are 17, 258, 34, 531, 187, 36 and 326. Three are multiples of 17. The best modulus in
2–40 has a binomial tail of 0.006, but the look-elsewhere p (T1 positions drawn at random, 20,000 draws) is
**0.054** (`offsets.py`, `offsets.txt`). That is not evidence on its own. It is the reason `05` searches periodic keys first.

This confirms for us the canon line "the ciphertext has no bigram structure of its own", which until now rested on
Bourdeau.

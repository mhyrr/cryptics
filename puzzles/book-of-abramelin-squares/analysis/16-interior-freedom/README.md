# 16 — Is the interior letter free?

**Result.** Yes, to the limit of these tests. By the rule fixed in
[PROTOCOL.md](PROTOCOL.md) before the run (commit `0fa7a37`), the evidence
supports end state B. No context lifts leave-one-square-out accuracy above
32 %, and the largest real entropy reduction is 0.15 bit out of 2.9.

## The number for "free"

781 interior orbits in 232 squares (320 vowels, 461 consonants). An orbit is
the set of cells that transpose plus half-turn copy onto each other.

| Quantity | Bits per letter |
|---|---:|
| Interior orbit letter, given its class (Miller–Madow) | 2.92 |
| vowels (uniform would be 2.32) | 2.10 |
| consonants (uniform over 21 would be 4.39) | 3.49 |
| Top-row letter, given its class, for comparison | 2.99 |

Given its class, an interior letter is as unpredictable as a seed letter is
to someone without the dictionary. A blank 5 × 5 interior has four orbits,
about 11.7 bits, or some 3,300 equally likely fills. A 7 × 7 has nine orbits,
about 26 bits.

## Tests

| Test | Observed | Control | p |
|---|---:|---:|---:|
| T1 chapter preference, loss in bits | 3.030 | 3.179 mean, 3.061 minimum of 1,000 | 0.001 |
| T2 prince preference | 3.049 | 3.110 mean | 0.022 |
| T3 interior letters that occur in the own top row | 35.9 % | 35.4 % mean, 40.2 % maximum | 0.40 |
| T4 R at row two, column two of 5 × 5 squares | 16 of 42 | 12.1 mean, 20 maximum | 0.07 |
| T4 without the SATOR family | 15 of 41 | 11.9 | 0.13 |
| T5 interior disagreements, Mathers against Dehn, 44 pairs | 69 | 63.0 mean, 81 maximum | 0.13 |
| T5 interior against top row only | 69 | 67.9 | 0.43 |
| M4 position in the square | 3.012 | 3.025 | 0.22 |
| M5 letter above | 3.019 | 3.081 | 0.002 |
| M6 letter up-left | 3.141 | 3.153 | 0.36 |
| M7 square size | 2.999 | 3.036 | 0.05 |
| M3 seed weight | 2.945, λ = 1.0 in every fold | M0 2.945 | none |

Top-one accuracy: class only 28.6 %; the best context (letter up-left) 32.0 %.

Reading:

- **Chapter and prince.** Chapters differ a little in their letters: 0.15 bit
  against the permuted control, prince groups 0.06. That is a compiler's
  habit, or shared material inside a chapter. It predicts nothing useful.
- **Seed reuse.** The 39 % in the handoff is the chance rate. Exchanging top
  rows among squares of the same size gives 35.4 %; the real squares give
  35.9 %. The fitted seed weight is exactly 1. Interior letters are not drawn
  from the seed.
- **AREPO.** R is the commonest interior consonant everywhere (115 of 461
  orbits; 17 of 66 at the other consonant positions of the same squares). Its
  share at row two, column two is not reliably higher.
- **Witnesses.** Raw rates are 9.5 % top row, 9.2 % other border, 12.5 %
  interior. With each square pair's own error rate held fixed the interior
  excess is not significant. Copyists did not visibly do worse in interiors.
  By the protocol this says nothing about freedom.
- **Letter above.** A small dependence (0.06 bit). It is the vowel/consonant
  alternation seen one level finer: some letter pairs are easier to say.

## Estimator note, 2026-09-20, after the run

Every context model has a higher absolute loss than the class-only model,
permuted controls included. Leave-one-square-out removes the held letters
from their own small context, which makes them look rarer there. The honest
gain is therefore the observed loss against the permuted mean, and the table
gives both. Against class-only the frozen rule reads "supports B"; against
the permuted controls the largest gain is 0.15 bit and the rule reads the
same. The protocol is unedited.

## Limits

Discovery data: all of Mathers was already seen. The tests cover the contexts
named in the protocol. A rule keyed to something outside the square and the
chapter (a lost table, a name list in another order) is not excluded.
Experiments 03, 04 and 15 tested fragments, local recurrences and the spirit
names, and also found nothing that predicts the letter.

## Reproduce

```sh
cd puzzles/book-of-abramelin-squares/analysis/16-interior-freedom
python3 run.py          # about 15 seconds; rewrites results.json identically
```

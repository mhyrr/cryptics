# 02 — key extensions found on f. 198, frozen for a held-out test

## Question
Five signs in f. 198–199 are missing from Tomokiyo's Cipher 4 table or read differently from
it. Do the values proposed from f. 198 hold at every occurrence there (criterion 4), and do
they hold in a *different* Cipher 4 letter transcribed afterwards?

## Method
`kwic.py` lists every occurrence in both readers with decoded context (`kwic.txt`). Values
were judged by reading every occurrence, not only the ones that first suggested them.
Extensions are frozen in `extensions.tsv` and applied by `decode_v1.py` (upper case in the
output marks an extension value).

## Result on f. 198 (in-sample)
| Sign | Value | Fit |
|---|---|---|
| 21. (q + dot) | que | 19/19 |
| 21_ (q + dot below) | qui | ~6/7 |
| 2H (reader B) | que | 6/7; A merges 2H and 2+ ("me") as "24+" |
| H | ne | 4/4 |
| Σ / ε | o | 9/9 |

## Held-out test (pending)
A Cipher 4 letter not yet transcribed (Pérez to Vargas Mexía, 13 Sept 1578, "casi toda en
cifra" per Ochoa 1844) is transcribed blind and decoded with `decode_v1.py`. Pass: each extension
reads consistently at ≥ 80% of its occurrences there.

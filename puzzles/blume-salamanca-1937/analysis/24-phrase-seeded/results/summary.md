# Phrase-seeded results

## Holdout controls

615 letters; first width 12–22, second length 18–28; 5,284 contextual second-key seeds.
Recovery criterion: >=95% agreement allowing a cyclic shift <=40. Exact is separately counted.

| rank swaps from list key | trials | recovered | exact in-place | process CPU seconds |
|---|---|---|---|---|
| 0 | 10 | 10 | 10 | 30.318 |
| 1 | 10 | 9 | 9 | 70.213 |
| 2 | 10 | 6 | 6 | 224.220 |

These are synthetic literary-proxy controls. They do not identify the historical system or key.

## Full T1 and own-letter shuffle

| body | best quadgram score | candidate above -5.10 | process CPU seconds | seeds refined |
|---|---|---|---|---|

All returned texts/keys and control accuracies are retained in the JSONL files.
A single shuffle is a false-positive check, not a p-value estimate.

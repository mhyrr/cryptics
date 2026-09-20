# 15 — The spirit names of Book II chapter 19 and the rows of the squares

**Result.** The spirit lists overlap the square rows far above chance, for top
rows and interior rows alike. They do not predict blank interior rows.

Peterson's foreword remarks on "a close connection between the lists of
spirits and the magical squares". Kollatsch's draft says names were often
derived from square letters (canon, 2026-09-18). This experiment counts it.

| Names | Squares | Names | Exact | Control | Near | Control |
|---|---|---:|---:|---:|---:|---:|
| Dehn lists | Dehn readings | 390 | 29 | 4.9 | 26 | 12.1 |
| Dehn lists | Mathers | 390 | 23 | 4.2 | 47 | 19.5 |
| Mathers lists | Mathers | 409 | 8 | 1.3 | 34 | 16.5 |
| Mathers lists | Dehn readings | 409 | 7 | 1.5 | 26 | 10.7 |

For Dehn names against Dehn readings the matched rows are 26 top, 26 bottom
and 31 inner. The first Dehn list (Moreh, Saraph, Proxonos, Nabhi, Kosem ...)
runs through the seed words of chapters 1 and 2 in order. Other lists carry
interior rows (Orinel, Kirik, Ranar, Rotor, Sapipas, Corilon). All matches are
in `names-in-squares.json`.

`predict_rows.py` then asks whether Mathers's own name list can fill inner
rows that Mathers leaves blank, scored against Dehn. Design fixed before the
single run: a name of the right length that fits every visible letter, unique
among candidates, predicts the row. Result: 70 rows, 3 predictions, 0 correct;
the shuffled-name control makes 2.9 predictions. The lists name too few rows
to work as a fill source.

## Limits

Direction is not decided: names may come from squares or squares from names.
The Mathers name lists are corrupt relative to Dehn's (Habhi for Nabhi, Nilen
for Milon). One Mathers list heading absorbs the lists that follow it, so list
attribution by prince is unreliable in `spirit-names.json`; membership is not.

## Reproduce

```sh
cd puzzles/book-of-abramelin-squares/analysis/15-spirit-names
python3 extract_names.py       # needs the cached page
python3 names_in_squares.py    # about two minutes
python3 predict_rows.py
```

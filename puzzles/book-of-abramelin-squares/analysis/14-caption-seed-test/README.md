# 14 — Does the caption select the seed word, or interior rows? (E3)

**Result.** The caption selects the seed word. It does not select interior rows.

| Target | Tier | Observed | Permutation mean | Permutation max (2,000) |
|---|---|---:|---:|---:|
| Mathers top rows (232) | exact | 14 | 1.1 | 10 |
| Mathers top rows | skeleton | 21 | 1.9 | 14 |
| Mathers top rows | near | 28 | 3.5 | 15 |
| Mathers interior rows (373, each also reversed) | exact | 0 | 0.0 | 0 |
| Mathers interior rows | skeleton | 0 | 0.3 | 3 |
| Mathers interior rows | near | 2 | 0.9 | 6 |
| Dehn top rows (60) | skeleton | 7 | 0.6 | 5 |
| Dehn interior rows (246, each also reversed) | skeleton | 2 | 0.4 | 5 |

No permutation of the 2,000 reaches the observed seed count at any tier on the
Mathers rows. Excluding the OCR-tolerant lookups leaves the skeleton seed count
at 21. Every count is in `results.json`.

## What was done

This is the E3 the experiment 11 handoff asked for, redirected by experiments
12 and 13; [PROTOCOL.md](PROTOCOL.md) states the three changes and was
committed in `9438ec0` before any nomination.

1. `extract_labels.py` takes Mathers's 231 numbered purpose labels for the 30
   chapters from the cached page. It reads no square rows.
2. Three Opus subagents, given only the labels and the nomination rules,
   nominated at most three German headwords per label. Frozen in
   `nominations.json` before lookup.
3. `lookup.py` joins nominations to OCR headwords with a closed list of
   spelling operations, each justified in the protocol from E2's failures:
   Kriegsmann / Kriegsman, Reiter / Reuter, alter Mann / Alter man, and
   -gestalt frames now join. 256 lookups hit an exact key, 66 needed the
   one-edit OCR tolerance, 168 found nothing. All are kept in `lookups.json`.
   No Hebrew transliteration is altered.
4. 173 of 231 labels received at least one candidate word (gate: 100).
5. A row is a hit when it matches a candidate word of any label in its own
   chapter. The control permutes candidate sets across chapters.

Seed hits at the skeleton tier, by chapter: 5 CEPHIR NESER PARAS PETHEN;
8 CANAMAL; 15 BASAR; 16 SEGOR; 18 BUAH; 19 BETULAH CALLAH DODIM IALDAH SARAH;
20 SINAH; 27 ARIEH ATSARAH DOBERAH ESAHEL PERAC REEM SELEG.

## Limits

The candidates are OCR. No hit has been read on the page image yet. The labels
are English, twice translated from German, and chapter 5 shows that label
order and square order disagree between witnesses; the test is therefore by
chapter, and says nothing about which label goes with which square. 21 hits of
232 is a floor set by OCR recall, translation drift and the three-word limit,
not an estimate of how many seeds come from the dictionary. Experiment 12's
caption-free count is 56. The Mathers corpus is exposed; this is not a blind
witness test.

## Reproduce

```sh
cd puzzles/book-of-abramelin-squares/analysis/14-caption-seed-test
python3 -m unittest test_lookup -v
python3 run.py --check
```

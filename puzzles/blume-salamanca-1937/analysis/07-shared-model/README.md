# 07-shared-model — which families could produce the shared strings?

**Question.** T1 and T2 share 9 distinct 4-grams where shuffles give 2.2 (`02`). Under which transposition, with
one key on both and a shared opening or closing of L letters, would that happen?

**Method.** `model.py`. For each family and L in {0, 30, 60, 100}, 60 trials: telegraph-style held-out Spanish of
615 and 160 letters, sharing the first (or last) L letters, enciphered under one random key. Count the distinct
4-grams the two ciphertexts share. Families: double columnar 8–15 and 16–25 (the named wall), single columnar 5–45
(a yardstick), Nihilist rectangle w 5–25 (one column key, rows reordered per message) read by rows or by columns.
Run: `python3 -I model.py > result.txt` (1 s).

**Result** (`result.txt`; mean, and the share of trials reaching 9).
| family | no common text | common opening, L 30 / 60 / 100 |
|---|---|---|
| double columnar 16–25 | 3.0, 0/60 | 2.6–2.8; at most 2/60 |
| double columnar 8–15 | 2.2, 0/60 | 2.2–3.0; at most 1/60 |
| single columnar 5–45 | 2.5, 0/60 | 4.3 / 11.1 / 31.9; 9, 21, 44 of 60 |
| Nihilist, read by rows | 3.5, 2/60 | 22.4 / 44.6 / 74.2; 60/60 |
| Nihilist, read by columns | 2.7, 0/60 | 2.4–2.8; 0/60 |
Common closings give the same pattern, weaker for Nihilist by rows.

**Reading.** A shared phrase does nothing under double columnar of any key length, or under Nihilist read by
columns: the shared strings stay at the chance level. That confirms Bean's point. Only families that leave
single-row or single-column runs intact produce them: single columnar and Nihilist read by rows. Both are
excluded for the real telegrams: single columnar by Bourdeau (w ≤ 45), and Nihilist read by rows by `05`
(`nihilist_control.py`, w 5–40). So no family that survives our tests explains the shared strings. Either they are
chance (p ≈ 0.001 on a statistic chosen after looking), or the system is one we have not modelled. A system we have
not modelled would have to keep column or row runs across messages without keeping letter pairs within one,
since `04` found no letter-pair structure.

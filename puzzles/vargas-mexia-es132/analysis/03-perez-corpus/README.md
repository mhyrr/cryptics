# 03 — Pérez's Cipher 4 letters (ff. 105, 148, 157, 179)

**Frozen 2026-10-04, before any of these folios was transcribed.**

## Question
1. Does the frozen decoder (`../02-key-extensions/decode_v1.py`, unchanged) read Pérez's other
   Cipher 4 letters as Spanish that fills the [CIFRA] gaps in Rubino's (2012) independent
   transcription of their clear text?
2. Held-out test 3 for the two extensions still untested: 21. = que and 21_ = qui. Also
   re-test 2H = que, H = ne and Σ = o.

## Letters
| Folio | Date (Rubino) | Canvas (c = f − 3) | Readers |
|---|---|---|---|
| f. 105 | 13 Oct 1578, "complete cipher" | ~102 | A and B (blind, separate) |
| f. 148 | 21 Nov 1578 | ~145 | one |
| f. 157 | 8 Dec 1578 | ~154 | one |
| f. 179 | 26 Jan 1579 | ~176 | one |

## Rules (fixed now)
- Readers are blind to the key, to each other, and to Rubino. Same notation as f. 198/f. 123.
- Decoding uses `decode_v1.py` unchanged. A new sign is reported, never valued in this run.
- Extension test: each extension consistent at ≥ 80% of its occurrences across the four letters,
  judged occurrence by occurrence with `kwic`-style listings. Fewer than 3 occurrences: untested.
- Rubino check: for each [CIFRA] gap in her transcription, record whether our decoded run fills it
  grammatically (yes / partly / no), in `rubino-joins.md`.

## Result
(pending)

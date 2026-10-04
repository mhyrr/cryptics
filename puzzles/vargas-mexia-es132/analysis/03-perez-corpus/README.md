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

## Result (2026-10-04)
**Scope corrections.** (2026-10-04, later: the first one below is half wrong. f. 105 is in Cipher 3, not 4, but under the v2 Cipher 3 guide f. 105 reads as
Pérez writing to Vargas about the King's letter, signed Antº Pérez; Rubino was right. See `../04-cipher3/`.)
- f. 105 is not a Pérez letter in Cipher 4. Tomokiyo lists ff. 103/105 as Philip II to Vargas Mexía,
  13 Oct 1578, in Cipher 3; the "Antonio Pérez" is the countersignature. Rubino's list put it among
  Pérez's letters, and this pre-registration followed her. Moved to `../04-cipher3/`.
- f. 148 has no cipher (reader; Rubino agrees: no [CIFRA]).
- The test therefore rests on ff. 157 (8 Dec 1578, ~350 tokens) and 179 (26 Jan 1579, ~139 tokens),
  one blind reader each.

**Decoder bug fix during the run** (dated note in `../01-decode-f198/README.md`): Cipher 4 has no 13; the
digit rules now accept only key numbers. Earlier outputs are byte-identical.

**Held-out test 3** (`kwic3.txt`, judged occurrence by occurrence):
| Extension | Test 3 | All held-out (ff. 87, 123, 157, 179) |
|---|---|---|
| 2H = que | 11/14 = 79% (just under 80%; the 3 misfits are in uncertain runs) | 24/27 = 89% |
| H = ne | 2/2 (untested, < 3) | 5/5 |
| Σ = o | 1/1 (untested), plus "imaginaci[0]n", read "0" by the reader | 7–8/10 |
| 21. = que | 1 fits, 1 unclear (untested) | 3/4 |
| 21_ = qui | 1/1 (untested) | 2/3 |
None is contradicted. 2H is established. The other four are consistent but thin.

**Content (provisional, one reader each).**
- f. 179: Pérez tells Vargas to send certain matter only in the private letter, "because [he] has
  much business and cannot look through all the letters; with this form there will be no danger". In
  cipher: "although he was given to understand in general that there was some knowledge of what had
  passed… it was with such discretion that not even in imagination could he understand…". This is the
  passage behind Rubino's "damaging admission".
- f. 157: "…se le escrive agora al Príncipe de Parma, y con cessar el manejo del dinero en los de ay,
  cessarán todos los…"; "cessará agora la [nueva] correspondencia que se avía comunicado…"; "Su Mag.d…
  dize que todavía procure V.m. de entender en todo lo que se pudiere, y si fuesse [posible] aver a las
  manos algunos papeles, pero que esto sea con el mayor recato…". This is the King's instruction of
  20 Oct (f. 123) repeated.
- Rubino check (`rubino-joins.md`): pending; her f. 157 and f. 179 have 13 and 8 [CIFRA] gaps.

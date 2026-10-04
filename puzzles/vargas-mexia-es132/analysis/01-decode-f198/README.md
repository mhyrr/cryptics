# 01 — decode f. 198–199 with Tomokiyo's Cipher 4

**Frozen 2026-10-03, before either blind transcription was opened.**

## Question
Does Tomokiyo's Cipher 4 table (`../../sources/keys/cipher4.tsv`, transcribed from Cryptiana),
applied mechanically, read Antonio Pérez's letter of 15 April 1579 as continuous Spanish that
joins the clear text? (H1, H2.)

## Method (fixed)
`decode.py`, standard library. Inputs: readers A and B (`../../sources/transcription/reader-*/f198.txt`),
decoded separately.
- Base numbers 1–23 → letters, as in the key. Marks: `.` → -a, `+` → -e, `_` → -i, `^` → -u;
  `<hat>`, `<v>` → null (Tomokiyo's reading; Devos's "doubling" reading is flagged, not applied).
- Digit runs: R1 1–23 → one base; R2 ends in 6 with prefix 1–23 → base + o (so "16" = "no",
  not x); R3 bare "6" → g; R4 otherwise split left to right into bases, each optionally followed
  by a 6-vowel. Every R2/R4 decision is flagged.
- Letter signs y→a, d→d, o→o (flagged: could be code "hu"), v→o, a→u. Clusters B=bl, C=cl, f=fr,
  g=gr, p=pr, t=tr; F, G, P, b, c (fl, gl, pl, br, cr) are Tomokiyo's conjectures and flagged.
  Codes vo = V.Magd., co = carta.
- Anything else is output as ⟨token⟩ and flagged. No value is assigned by context.

## Checks (computed afterwards, from the two decodes)
1. The share of cipher tokens decoded without an unknown sign, per reader.
2. Agreement of the two decodes, token-aligned per line.
3. Joins: each cipher run is read with the clear words on either side (judged by reading, and
   recorded run by run in `joins.md` with positions; LLM reading is allowed here because it is
   interpretation, not statistics).

## Run
```
python3 decode.py ../../sources/transcription/reader-A/f198.txt > out_A.txt
python3 decode.py ../../sources/transcription/reader-B/f198.txt > out_B.txt
```

## Result
(pending)

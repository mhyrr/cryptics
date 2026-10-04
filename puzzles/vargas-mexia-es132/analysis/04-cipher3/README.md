# 04 — Cipher 3 (Devos Cp.30), first attempt on f. 105

**Decoder frozen 2026-10-04** (`decode_c3.py`, commit before reader A of f. 105 was decoded).
Rules from `../../sources/keys/cipher3.tsv`: letters 1–29, clusters 30–37, vowel marks after (+ a,
. e, p o, s i), consonant marks above (v r, hat n, bar s), numbers > 37 treated as codes.

## Result (f. 105r–v = Philip II to Vargas Mexía, 13 Oct 1578; readers A and B)
- **Cipher 3 confirmed**: both readings yield Spanish fragments under Tomokiyo's table ("…fuera por la
  carta de [code] lo que le…", "contentase con", "con esto y con la", "hacerle", "por agora", "tenerle
  contento").
- **Not readable yet**:
  1. The readers segment digit groups differently: B writes "256" as a group where A writes "6256",
     "25626", "2561764". Cipher 3 transcription needs a group-segmentation convention fixed before
     reading (e.g. one token per symbol, with marks attached, confirmed against Tomokiyo's examples).
  2. Code numbers (108, 149, 224, 256, 300, …) have no values. 256 is the most frequent group in B (9×).
- Next: write a Cipher 3 transcription guide from Tomokiyo's f. 11v / Borgia examples, re-transcribe
  f. 105 with it, then collect code contexts across Cipher 3 letters to value the codes (criterion 4).

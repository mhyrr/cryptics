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

---

## Experiment 04b — Cipher 3 v2: tokenization guide, calibration, duplicates, concordance
**Pre-registered 2026-10-04, before any v2 transcription exists.**

**Finding that motivates it.** Tomokiyo's aligned reading of ff. 81/83 (`spanish3Dduplicates.png`), checked on
native crops of f. 81 (canvas 78), shows that the Cp.30 vowel marks look like digits and letters. The -i curl
looks like a 6 ("256" = 25 + curl = "vi"; "316" = "cri"). The -o hook looks like "p". The -u T-bar looks like "u".
"u·" standing alone is "que" (3× on f. 81). So many of reader B's "codes" (256, 316, 2464…) are probably
sign + mark, and only numbers with a cross above (108⁺, 149⁺, 1⁺) are marked code words.

**Frozen now:** `../../sources/transcription/CIPHER3-GUIDE.md` (notation; shapes only), `decode_c3_v2.py`
(rules in its docstring), `c3_extensions.tsv` (one value, "u." = que, from Tomokiyo's alignment, external).

**Runs (Sonnet 5.5 readers, blind to the key and to each other, given only the guide):**
1. *Calibration:* f. 83 cipher lines 1–6 (canvas 80), one reader. Score: share of syllables of the v2
   decode that agree with Tomokiyo's aligned labels on that image. Reported as is; no threshold.
2. *f. 105* (Philip II, 13 Oct 1578): readers A2 and B2. Decode both; report agreement and unknowns.
3. *Duplicates for codes:* f. 103 and f. 113 (Tomokiyo: no. 47 "seems to be a duplicate of" no. 52), one
   reader each. Tomokiyo shows duplicates were enciphered independently, so a code in one may be spelt out
   in the other.
4. *Concordance:* `concordance.py` lists every code word (cross above, or no parse) across all v2 letters
   with ±6 decoded tokens of context, into `concordance.txt`.
5. *Freeze, then held-out:* any code value proposed from (2)–(4) goes into `c3_extensions.tsv` with its
   evidence and is committed **before** a held-out Cipher 3 letter is transcribed (candidates: the duplicate
   pair ff. 165/167, 10 Jan 1579). Criterion 4: a value must fit at ≥ 80% of its held-out occurrences; with
   fewer than 3 it is "untested".
Also tested at held-out: 35 = pr (Borgia) vs pl (Cp.30), judged occurrence by occurrence.

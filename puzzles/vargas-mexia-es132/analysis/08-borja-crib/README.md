# 08 — Cipher 3 calibration on a contemporary crib (Borja to Philip II, 12 Jul 1579)

**Pre-registered 2026-10-16, before any reader output exists.**

## Question
How accurately does our Cipher 3 pipeline (Sonnet blind reader + `CIPHER3-GUIDE.md` v2.2 + frozen Cp.30 key and
extensions, decoder v2.2) read a Cipher 3 letter, measured against a 1579 decipherment rather than a modern one?
The only calibration so far is f. 83 against Tomokiyo (38/56 = 68% syllables exact, one reader, exp 04b).

## Object
BnF Français 15561, ff. 42r–43v (Gallica `ark:/12148/btv1b9064570k`; ark from Tomokiyo, cryptiana `henryiii.htm`).
Don Juan de Borja, Prague, to Philip II, 12 Jul 1579, on Parma's taking of Maastricht. Identified on the images: archival
French summary "12 juillet 1579 de Prague. Lettre de Don Juan de Borgia au Roy d'Espagne sur la prise de Maestrick";
folio "42" (old "48"); close "De Praga a [..] de julio 1579 … Don Juan de Borja". Images: screenshots taken by Greg in
his browser on 2026-10-16 (Gallica refused scripted requests that day), in `../../sources/cache/gallica-manual/`.
Shelfmark on the Gallica record not yet read; content matches Tomokiyo's description of fr. 15561 f. 42.

Four cipher passages, each deciphered in the same period hand:
| P | Where | Cipher | Decipherment |
|---|---|---|---|
| P1 | f. 42r | 2 struck lines after "lo qual importará mucho" | left margin, keyed by a sign |
| P2 | f. 42v | 1 struck line after "para" | interlinear, above |
| P3 | f. 42v | X'd block, ~17 rows | left margin, runs on into the main column |
| P4 | f. 43r | X'd block, ~10 rows | left margin |

Tomokiyo reconstructed his "Cipher with Don Juan de Borgia (1579)" table (`../../sources/keys/cipher3_borgia_variant.tsv`)
from this letter. That table is therefore **not used** here; the key is Cp.30 (`cipher3.tsv`, Devos via Tomokiyo).
Two items in the frozen decoder came partly from the Borgia table or a third party: 35 = pr (H11) and the vowel-mark
set. Results on 35 are reported but cannot count as independent support for H11.

## Method (frozen)
1. **Blind images** (`../../sources/cache/f42-borja-blind/`): margins cut away; the P2 interlinear gloss painted out;
   the facing page's margin cut from the P3 high-resolution crop. Checked by eye on 2026-10-16.
   p1 = P1; p2 = P2; p4 (high resolution) + p3 (overview, for the frame rows) = P3; p5 = P4.
2. **Two cipher readers**, A (forward) and B (reverse page order), Sonnet, prompt `reader-prompt.md` (exp 07 v1.1 with
   the passage headers added). Blind to the key, to the margins and to each other.
3. **One margin reader**, C, Sonnet, prompt `margin-prompt.md`: diplomatic transcription of the decipherments only
   (`../../sources/cache/f42-borja-margins/`), abbreviations expanded in [ ] only where certain. C sees no cipher.
4. **Scoring**: `score.py` (rules in its docstring), run on A and on B against C. Reported per passage and overall:
   letter recall and precision; per-base accuracy; every 108 / `<cross>` / 35 token with its aligned plaintext.
   A against B with `../07-after-arrest/compare_decoded.py` for reader agreement.
5. **No threshold.** This experiment measures. It reports the numbers as they come and lists the systematic misses.
   **H12 test (pre-stated):** H12 (108⁺ = Su Magestad) is supported by an external witness if, in both readers,
   every 108 token aligns to "Su Mag…" in C. A 108 that aligns to anything else weakens it.

## Caveats stated in advance
- A marginal decipherment may smooth, abridge or skip; recall below 100% is not all reader error.
- Struck frame rows (first and last of P3 and P4) are expected to read worst.
- Screenshots, not IIIF downloads: resolution varies by crop (p4 is the sharpest).

**Amendment 2026-10-16, after reader C, before any cipher reader output:** the scoring plaintext is built by
`prep_plain.py` from C's file. It drops the five full-width lines at the foot of f. 42v (clear main text; see the
script's docstring for the text-flow argument) and C's `[sign]` marker.

**Amendment 2, 2026-10-16, after reader B, before reader A reported: amendment 1 was wrong.** B's decode of the end of
P3 reads "valiendome de todas las ocasiones … el Emperador me responde muy bien con dezir…" and the start of P4 reads
"…todas palabras, yo hago las diligencias que puedo, si no se hazen…". The full-width lines at the foot of f. 42v are
therefore decipherment (the clerk ran out of margin), spanning the end of P3 and the start of P4. Primary scoring is
now `merge_p34.py`: P3 and P4 are one passage (P34) on both sides, full-width lines kept, so no boundary is drawn by
eye. The amendment-1 scores are kept in `score_*.txt` for the record; P1 and P2 are unaffected.

## Run
```
python3 merge_p34.py plain $T/fr15561-f42-margins/plaintext.txt > plain_p34.txt
python3 merge_p34.py cipher $T/fr15561-f42-A/transcription.txt > /tmp/A_p34.txt
python3 score.py /tmp/A_p34.txt plain_p34.txt --show > score_A_p34.txt   # primary (same for B)
T=../../sources/transcription
python3 prep_plain.py $T/fr15561-f42-margins/plaintext.txt > plain_scoring.txt
python3 score.py $T/fr15561-f42-A/transcription.txt plain_scoring.txt --show > score_A.txt
python3 score.py $T/fr15561-f42-B/transcription.txt plain_scoring.txt --show > score_B.txt
```
(Reader transcriptions are first decoded inside `score.py`; to see the decoded text alone:
`python3 ../04-cipher3/decode_c3_v2.py A/transcription.txt --v22`.)

## Result
(pending)

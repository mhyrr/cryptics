# Comparison with the third-party readings (step 8)

Run after all our window decodes were frozen (commits up to `1e9fca9`; f. 22 reader B was still blind and running).
Sources (CLAIMANT, model-produced, no paleographer): `el-descifrador/cabinet-noir`, folder `es132-vargas-mexia/`
(fetched 2026-10-04: f011-012, f017-025, f032, f034, `cle/`), and `pangoleen/cipher-readings`, folder `espagnol-132/`
(`reading_f26r.md`, `reading_perez_f87_f157_f179.md`). Cached in `sources/cache/thirdparty/` (git-ignored).

Script: `thirdparty_compare.py`, output `thirdparty_compare.txt`. Each third-party Spanish quotation is scored with
`mignet_check.best`: the share of its normalised letters found in order inside a window of our decode. Each letter's
control is the same quotation scored against a different letter.

## Agreement
| Letter | Third party | Quotations | Median vs ours | Control median |
|---|---|---|---|---|
| ff. 11–12v (24 Jan 1578) | cabinet-noir | 4 | 94% | 36% |
| ff. 17–25 (8 Mar 1578) | cabinet-noir | 12 | 82% | 42% |
| f. 26r (Mar 1578) | pangoleen | 5 sentences | 91% | 41% |
| f. 34 (16/17 Mar 1578) | cabinet-noir | 1 (too short to test) | – | – |
| f. 87 (13 Sep 1578) | pangoleen | 5 cipher runs | 95% | 58% |
| f. 157 (8 Dec 1578) | pangoleen | 19 cipher runs | 94% | 54% |
| f. 179 (26 Jan 1579) | pangoleen | 9 cipher runs | 94% | 58% |
f. 32 (Cipher 3) was compared by reading, since cabinet-noir quotes it in § form, not «»: both read the Duke of Lorraine at court, a
"liga" through him "con algunos príncipes del Imperio" so that the Protestants send no help to the Huguenots, and a visit
"al Cardenal y Duque de Guisa" to confirm them in their goodwill.

## Disagreements and corrections that matter
- **f. 12v (24 Jan 1578), the Sotomayor passage.** Both our blind readers and cabinet-noir read the same words: "y de
  todo lo [que] los Guysas trataron con él cerca del proceder de mi hermano y con Alanson". This is three independent
  readings of one cipher run. Cabinet-noir reports the passage but does not set it against Mignet's chronology.
- **f. 17 "liga".** Our first gloss gave it to Lorraine. Cabinet-noir reads "el Duque de Branzuich" (Brunswick), and our
  decode has "el [duque] de Branzui[c]". The league is Brunswick's, with "algunos Príncipes" against those who help the
  rebels. It is not a Don John–Guise league.
- **f. 34 date.** Cabinet-noir gives 16 Mar 1578; our reader A reads "A xvij de Março", reader B "A xbj?". Unresolved
  (the date line is cut at the gutter).
- **f. 26 swash sign.** Our in-sample candidate "ll" for the recurring long swash agrees with pangoleen's "mi-ll",
  "ui-ll-e-ro-y".

## Cipher 3 code values (our exp 04) against cabinet-noir's `cle/cp30_complements.tsv`
That file lists the team's additions to Alcocer's printed Cp.30 key (1921), and the team values that the print
contradicts.
- **u. = que:** agrees (their "Q" sign; Q. = que, proved by duplicate).
- **108⁺ = Su Magestad:** they have the same value but call it "non vérifiable dans l'imprimé", because Alcocer's table has
  a gap for codes ≈ 100⁺–128⁺. It is neither confirmed nor contradicted by print.
- **T⁺ (1⁺) = particular(es):** agrees ("1_c particular", proved by duplicates, including ff. 165/167).
- **149⁺ = V.m.:** not listed by them.
- **35:** they prove 35 = pr and *underlined* 35 = pl. That resolves our H11: both values exist, distinguished by an
  underline that our guide did not ask readers to record.
- They report team hypotheses that the print contradicts: xal = hereje (not hermano), yil = Imperio, vel = hasta agora,
  79⁺ = secretario. None of these is among our frozen values. Our f. 32 decode prints yil, xal and vel as unknown codes.

## Novelty
Our readings of the window letters replicate cabinet-noir's (ff. 11–12, 17–25, 32, 34) and pangoleen's (f. 26r). The
Cipher 1 letter f. 3 (16 Dec 1577) is not among cabinet-noir's 30 readings or pangoleen's. Tomokiyo posted a
"preliminary decipherment" of it on Academia.edu, which we have not seen (HTTP 403).

# 07 — After the arrest: what the King wrote to Pérez's friend (H17)

## Question
Antonio Pérez was arrested on the night of 28 July 1579. Juan de Vargas Mexía, ambassador in Paris, was his friend and
private correspondent, and in 1580 he cut Pérez from his will (Rubino 2012). Do Philip II's letters to Vargas of
24 Aug 1579 – May 1580 say anything about Pérez, the Princess of Éboli, the Escobedo affair, or the private
correspondence Pérez ran with Vargas?

## Hypotheses (pre-registered 2026-10-05, before any image of these letters is fetched or read)
- **H17a**: a royal letter to Vargas dated after 28 Jul 1579 refers to Pérez (by name, office or code), to his arrest, to
  the Princess of Éboli, to the Escobedo matter, or to Pérez's letters or papers held by Vargas.
- **H17b**: none does. The King writes as if nothing had happened, and Pérez vanishes from the correspondence.
- **H17c** (observable in clear): the countersigning secretary changes after the arrest.
- **Test.** Every royal letter of 24 Aug 1579 – May 1580 is read in full by two blind readers; a duplicate counts as the
  second witness. H17a is supported by one clear passage, quoted with token positions and read by both witnesses. H17b is
  supported when every letter is read and none has such a passage. Letters not read are listed as the wall. The
  pre-arrest letters of Jun–Jul 1579 (ff. 206, 208, 211, 213, 215) are read too, as the baseline.
- **What counts for H17a**: a reference to the persons or matters above, or an order about letters, papers or ciphers that
  Vargas exchanged with Pérez. A change of cipher key or of secretary alone does not count; it goes to H17c.
- **H17c** is judged from a table of the countersignature on every letter from f. 154 to f. 275, read on the images.

## The letters (Tomokiyo's table of contents, `../../sources/cache/cryptiana/spanish3D.htm`; Cipher 3 unless stated)
| Folio | Date | Note |
|---|---|---|
| 200, 202 | 21 Apr, 17 May 1579 | before the arrest |
| 206, 208, 211, 213, 215 | 8 Jun, 4 Jun, 3 Jul, 7 Jul, 13 Jul 1579 | baseline |
| 217 | 22 Aug 1579 | to M. de Lansac (clear?) |
| 218 | 24 Aug 1579 | first letter after the arrest |
| 220 + dup 224; 222 + dup 226 | 13 Sep 1579 | duplicate pairs |
| 228 + dup 231 | 13 Oct 1579 | duplicate pair |
| 235 + dup 237; 239 + dup 241 | 3 Nov, 13 Nov 1579 | duplicate pairs |
| 245 + dup 247 | 29 Nov 1579 | duplicate pair |
| 251, 253, 255, 257, 261, 263, 267, 269, 271 | 16 Jan, 28 Mar, 16 May 1580 | 261 = dup of 255; 257 = dup of 263 |
| 273 (Cipher 2), 275 | undated | |
| 279 | Aug 1579 | relation of French movements at Fuenterrabía (clear) |
Non-royal letters (Parma f. 233, Mansfeld f. 243, Acuña f. 249) are context, read last.

## Method (frozen order)
1. This README and H17 in `hypotheses.md`, committed first.
2. **Images.** `../../sources/cache/pages/fetch_pages.py spreads` fetches whole spreads c197–c288 serially (one request
   per canvas, 20 s apart, after a probe). Folio numbers and the map c = f − 3 are checked on the images; pages are then
   cut locally. **No reader contacts Gallica.**
3. **Guide v2.2.** CIPHER3-GUIDE gains one rule: an underline below a sign is written `<under>`. Decoder v2.2 (`--v22`) values
   it on 30–35 only: 35 = pr, `35<under>` = pl (H11; cabinet-noir's complement, CLAIMANT). On 30–34 an underline outputs
   the l-cluster as an open alternative, "c(r|l)", flagged, until a duplicate settles it. Without `--v22` the decoder is
   unchanged (checked on f. 32 A). Both frozen by commit before any reader starts.
4. **Readers.** Sonnet 5.5, no sub-agents, at most six at once, each with only the guide and local page images. For a
   duplicate pair, one reader per copy. For a single letter, two readers, one working in reverse page order. Each
   transcription is committed before it is decoded.
5. **Decode** with `../04-cipher3/decode_c3_v2.py` (v2.2). Align duplicates and reader pairs with
   `../05-cipher4-v2/align.py`. New code values come only from duplicate alignment (a code in one copy spelt out in the
   other); they are written to `c3_extensions.tsv`, frozen, then tested on later letters (held-out, ≥ 80% fit).
   Candidate code values from cabinet-noir's `cle/cp30_complements.tsv` are not used until one of our duplicates confirms them.
6. **External plaintext (criterion 6).** Cabinet-noir reports that the Simancas minute of f. 255 (28 Mar 1580) is printed in
   Teulet vol. 5 pp. 213–214 (and CSP Simancas III no. 16). After our f. 255/261 decodes are frozen, the printed text is read
   on the page images and scored with a word-recall script as in exp 06 (pass ≥ 75%, with a control on another letter).
7. **Countersignatures** (H17c): a table for ff. 154–275 from the images.
8. **Third parties**, only after our decodes are frozen: cabinet-noir's readings for overlapping folios (200, 211, 215,
   220–221, 222, 228–229, 233, 245, 255), scored with `../06-premurder/thirdparty_compare.py`.
9. Synthesis on the main thread.

## Honest scope
These are the King's letters only. Vargas's replies are in Simancas (Estado K 1554–55 for 1579; PARES). Silence (H17b)
would be a finding about what the King chose to write to Pérez's friend, not proof that Vargas knew nothing. The private
Pérez–Vargas correspondence after the arrest, if any, is not in this volume.

## Result
(pending)

## Log
- 2026-10-05. Guide v2.2 (§8: `<under>`, local cropping) and decoder v2.2 frozen before any reader.
- 2026-10-05. v1 readers of f. 222 and f. 215 B finished in ~3.5 min with no full second pass (their own words). Reader prompt
  v1.1 adds an effort block; exclusion rule fixed before any duplicate comparison: a reader who declares the second pass
  not done is not a witness, and the letter gets a v1.1 reader (f222-2, f215-B2 dispatched).
- f. 215 (13 Jul 1579, baseline), readers A and B agree on the extent: 10 cipher lines on 215r, the rest clear. Clear text
  (reader A, lines 18–25 of `f215_A_dec.txt`; checked by the main thread on the image): "Antonio Perez me ha mostrado la carta
  del comiss° Olaue para vos, que a el le embiastes" and "Tambien me ha mostrado Antonio Perez … el aviso q̃ ay se tenia de
  los de Mastricht". Countersigned Ant.º Pérez. Two weeks before the arrest, the King names Pérez as the man who shows him
  Vargas's letters.
- f. 218 (24 Aug 1579), clear, read on the image by the main thread: Vargas's letters of 8 and 31 Jul and 2 Aug "han venido a
  mis manos"; Vargas to stay at court "hasta que llegue el dicho don Ju[an de Idiáquez]"; no countersignature.
- 2026-10-05. **13 Sep 1579, letter ff. 222/226** (witnesses f222-2 and f226-2, both v1.1 with full second pass; decoded-text
  agreement 74%/75%; f226 v1 vs f226-2 91%/97%). Content: an envoy of the Archbishop of Embrun ("Ambrún") and the castle of
  his city; the archbishop is at odds with the provost and the governor of the citadel; act "atentadamente"; warn those "a
  mi devoción en Artois" and "el príncipe de Parma mi sobrino"; money offered to the archbishop; a loan asked of Vargas and
  repaid; a letter intercepted at Mons "que causó tanta alteración". Then (f226_2_dec lines 27–31; f222_2_dec 27–32):
  "en lo que toca a lo [ … ] que me escrivís que tienen de San(go)art de las [cosas] de acá, holgaré que si lo huviéredes
  entendido de dónde salen me lo digáis; y lo que Lan[gro]e dezía de lo del [?]ydo ce no es verisímil; todavía si él le
  huviere nombrado o dado más señal, será bien que lo digáis". The King asks the source of Saint-Goard's news of the
  Madrid court and whether an informant named someone. The noun after "lo del" is an unvalued letter form (the "h-like"
  sign) in both f226 readers and unread in f222-2. No name: **not H17a** under the pre-registered definition; recorded as
  context (`leak_passage_f226_f222.txt`).

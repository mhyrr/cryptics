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
- **H17a (a post-arrest royal letter refers to Pérez, his arrest, Éboli, Escobedo or Pérez's papers): not supported.** Every
  dated royal letter of 24 Aug 1579 – May 1580 was read: f. 218 in clear on the image; ff. 220/224, 222/226, 228/231,
  235/237, 239/241, 245/247, 255/261, 257/263 (duplicate pairs) and ff. 251, 253, 267, 269, 271 (two blind readers each),
  decoded-text agreement 62–91% between witnesses. `h17_scan.py` and a full read of each witness find no such reference.
  cabinet-noir's independent readings of six of these letters have none either.
- **H17b (Pérez vanishes; the King writes as if nothing had happened): supported, with a qualification.** Pérez is never
  named after 13 Jul 1579 (f. 215: "Antonio Perez me ha mostrado la carta … que a el le embiastes"). But the letters do
  change: on 24 Aug Vargas's letters "han venido a mis manos" (f. 218); on 13 Oct they come "a mis manos, como a las de
  Çayas" (ff. 228/231); Idiáquez is named in cipher as a correspondent (13 Sep, May 1580). And twice the King hunts a leak
  without naming anyone: 13 Sep (ff. 222/226), where Saint-Goard's news "de las cosas de acá" comes from, and whether an
  informant "le huviere nombrado o dado más señal" (the key noun is an unvalued sign in both witnesses and in
  cabinet-noir); 29 Nov (ff. 245/247), how a private advice paper on Portugal written for the King reached Paris.
- **H17c (the countersigning secretary changes): supported** (`countersignatures.md`). Pérez countersigns ff. 200, 206,
  208, 211, 213, 215 (Apr–13 Jul 1579; Çayas on 17 May); 24 Aug: none; 13 Sep 1579 – May 1580: Don Juan de Idiáquez on
  every letter checked. The 24 Aug letter still has Vargas waiting in Paris for Idiáquez as his successor.
- External check: the 28 Mar 1580 letter matches the Simancas minute in Teulet vol. 5 pp. 213–214 (f255 77–82%; dup f261
  70–72%; controls 28–41%).
- **Wall.** (1) f. 273 is not a royal letter: a copy (Cipher 2, Italian) of a Savoy memorial given to the King by
  "Mos de la Cruz", endorsed "Para embiar à Juan de Vargas Mexia" (reader A, single pass; B pending). (2) Baseline: ff. 206,
  208, 211 read by one reader each; f. 213 not read. f. 206 names Pérez in cipher as receiver of Vargas's despatches. (3) Readability: 10–38% of
  each decoded text differs between witnesses, so a short reference inside an unread span cannot be excluded; the term scan
  covers both witnesses. (4) The noun in the 13 Sep leak passage (an unvalued letter-form sign). (5) Vargas's own
  dispatches of Aug 1579 – May 1580 (AGS Estado K 1553–1555) are unread; f. 275 is a court relation sent to Vargas (Fuenterrabía, no Pérez).

## Run
From this folder: `python3 ../04-cipher3/decode_c3_v2.py <transcription> --v22 > fNNN_dec.txt`;
`python3 compare_decoded.py A_dec.txt B_dec.txt [--show]`; `python3 h17_scan.py *_dec.txt`;
`python3 teulet_check.py f255_dec.txt f261_dec.txt f228_dec.txt f220_2_dec.txt`; `python3 thirdparty_compare07.py`.
Images: `../../sources/cache/pages/fetch_pages.py spreads` then `split_spreads.py` (throttled; 92 canvases).

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
- 2026-10-05. All 92 spreads c197–c288 fetched (one 'HTTPError' on c270, recovered on retry). Map c = f − 3 confirmed on folio numbers at c250 (253), c270 (273), c285 (288).
- 2026-10-05. **13 Sep 1579, letter ff. 220/224** (witnesses f220-2 and f224-2, both v1.1; decoded-text agreement 75%/78%;
  `align_f220_f224.txt`). Content: find out where Alençon is going and his dealings with the King, the Queen Mother's
  movements, the Prince of Béarn's moves; the Scots commended to Mos de la Mota; the Scottish ambassador; Orange; La Rochelle;
  La Mota's encomienda and the habit of Santiago; a copy of Alençon's letter to the [Cologne] commissioners; the "Reyna
  Christianísima". **Idiáquez is named twice in the cipher** (f220_2_dec lines 24 and 40; f224_2_dec the same lines): "…
  don [Ju(an)] de Y[di]aquez de lo que entendereis [por] carta suya" and "os lo dará don [Ju(an)] de Y[di]aquez". No Pérez,
  Éboli, Escobedo or Pérez papers in either witness (h17_scan and full read). Countersignature: f220-2 read "Don Antonio de
  Eraso"; the main thread, f220 v1 and f224/f224-2 read Idiáquez.
- 2026-10-05. **13 Oct 1579, f. 231** (witness, v1.1; f. 228 reader pending). Clear opening, checked by the main thread on the
  image: "se han recibido todas vras cartas desde principio de septiembre, hasta xjx y xx del mismo / assi las que haueis
  encaminado a mis manos como a las de Çayas, con todos los auisos y papeles que con ellas venian". After the arrest Vargas
  routes his letters to the King's own hands or to Zayas, not to a secretary of State in Pérez's place (cf. f. 218: "han
  venido a mis manos"; f. 215, before the arrest: "Antonio Perez me ha mostrado la carta … que a el le embiastes"). Cipher
  (f231_dec): Cambrai and a relation of events there; Mos de Selles; Alençon's designs on Artois and Hainaut; Mos de la Mota;
  the governor of Burgundy; the Prior of Cambrai; Frenchmen imprisoned and Saint-Goard; the Queen Mother and Alençon. No Pérez.
- **3 Nov 1579, ff. 235/237** (witnesses f235 v1.1, f237 v1.1 with pass 2 completed on request; agreement 66%/62%, verso
  show-through): Scottish ambassador; "milord" [Bretton?]; Burgundy and its governor; the Parlement; the Queen Mother's
  coming. No Pérez in either (h17_scan and full read); readability is lower than the Sep–Oct letters.
- 2026-10-05. 13 Oct 1579: second witness f228 (v1.1); f228/f231 decoded-text agreement 76%/81% (`align_f228_f231.txt`). Same clear opening ("a mis manos, como a las de Cayas"). The 'papeles' at f228_dec l. 76 / f231_dec l. 47 are papers shown to Vargas (Cambrai/Artois context: "tomado copia de los papeles que os mostró y embiado los a los de Artois"), not Pérez's. No Pérez in either witness.
- 2026-10-05. **13 Nov 1579, f. 239** (witness v1.1; dup f. 241 pending). Clear: letters of 22 and 23 Oct; "las cosas deste Reyno, como de las de Flandes"; date "Del Pardo a xiij de noviembre 1579". Cipher: Portugal ("lo qe a intentado [#760] de Portugal"; a writing to be got "a las manos", "tanto mas haviendose hecho por personas que no se puede dezir que tienen passion en esto por mi"); the Prince of Béarn's request for an enterprise ("de Navarra"?). Countersignature read by the reader as "Domingo d'Oriag?"; on the image (main thread, 35%) it is the same "Don Juº de Idiaq[ue]z" as on ff. 221–245. No Pérez.
- 2026-10-05. **29 Nov 1579, f. 245** (witness v1.1; dup f. 247 pending). Cipher: aid asked by the Prince of Béarn; Navarre; the Queen Mother; then (f245_dec lines 23–28) "el parecer que alla dezian que es del Conse[j]o … sobre lo de Portugal … del consejo no lo es … holgare que procureys entender con destreza por qué via ha ido a parar alla este papel". A second leak hunt (cf. 13 Sep, Saint-Goard): a paper presented in Paris as a Council opinion on Portugal. No name; not H17a. Clear (245v): French prize of a Portuguese ship with sugar and hides. Docket: received Paris 17 Dec, "con cifra".
- 2026-10-05. 13 Nov 1579: second witness f241 (v1.1); agreement 83%/86% (`align_f239_f241.txt`). The Portugal passage: a writing on the succession "se ha escrito en la universidad de [?]" in the King's favour; get the original "por todas las vias posibles", the more since it was made "por personas que no se puede dezir que tienen passion en esto por mi". No Pérez. (The f241 reader saw a git log mentioning Idiáquez in its context; this touches only its countersignature reading.)
- 2026-10-05. **28 Mar 1580, ff. 255/261** (witnesses f255, f261, v1.1; agreement 77%/79%). **External check passed**
  (`teulet_check.py`, `teulet_check.txt`): Teulet vol. 5 pp. 213–214 (Simancas minute B. 51 n. 69, read on the page images)
  against our decodes: f255 78% / 82% / 77% (pass on all three passages); f261 71% / 72% / 70% (duplicate; below the frozen
  75%, as f. 22 in exp 06); controls (f228, f220-2) 28–41%. Content: the Scottish ambassador on behalf of his Queen and the
  removal of her son the King from Scotland, to be received in Spain "como si le fuesse hijo proprio"; secrecy, "que S.t
  Goart ni hombre del mundo no lo podrá entender". Teulet dates the minute "Février" (annexed to Vargas's 21 Feb dispatch);
  the sent letter is dated Guadalupe 28 Mar 1580. Both readers of f. 255 and f. 261 read the countersignature as "Don Antº de
  Eraso" / "Don Juan de Idiaquez" respectively; on the image it is Idiáquez (`sig_f255v_over_f221r.jpg`: the two signatures
  are the same form). No Pérez.
- 2026-10-05. 29 Nov 1579: second witness f247 (v1.1); agreement 76%/76% (`align_f245_f247.txt`). The leak passage, both witnesses (f245_dec 23–28, f247_dec 23–29): a "parecer" said in Paris to be "del Consejo … sobre lo de Portugal"; "del consejo no lo es"; comparing it with "otros pareceres que me han dado [personas particulares] sobre este negocio", the King finds it is one of those; Vargas to find out "con destreza por qué via y medio ha ido a parar alla este papel". A private advice paper on the Portuguese succession, written for the King in Madrid, reached Paris. No name: not H17a; context for the leak theme (13 Sep Saint-Goard; 29 Nov Portugal paper).
- 2026-10-05. Prompt wording for reverse-order readers (f251-B, f253-B onward): 'the letter that ends on the last folio' and 'put the pages back in normal order' in the output. Wording only; no change to the guide or to what is transcribed.
- 2026-10-05. **16 Jan 1580, f. 251** (witnesses A and B, v1.1; agreement 91%/91%). Clear: Vargas's letters of 9–29 Nov
  and 2–14 Dec "con todas las copias, relaciones y papeles". Cipher: a governor and an example to others; the French King's and
  then "el secretario [Vil]leroy"'s request "cerca de la libertad de [los] vassallos suyos que estan presos en estos
  reynos" (the scan's "secretario" hit; it is Villeroy); the Bishop of Comminges; a "milord" to be paid once instead of a
  pension; an abbey; the Scottish ambassador on marriages (Condé, Orange); a councillor of Savoy; Casimir; the Queen Mother's
  pretension (Portugal). Docket: received Paris 4 Feb. Countersigned Idiáquez. No Pérez.
- **16 Jan 1580, f. 253** (witnesses A and B, v1.1; agreement 87%/90%). A second letter of the same day ("en otra carta que
  va con esta se responde a todas las vuestras hasta la de 14 del passado"): Mos de [ ]; a pension in escudos a month; ships
  and the Indies; a death and its consequences; clear postscript: licence for Geronymo Gondi to take two horses out of Spain.
  Countersigned Idiáquez. No Pérez.
- 2026-10-05. **16 May 1580 (Mérida), f. 267** (witnesses A and B, v1.1). Clear: Vargas's letters of 26 Feb – 8 Mar 'con todos los papeles y avisos'; arrests of French ships denied; the Fuenterrabía alarm; Villeroy's complaint about Saint-Goard's man taken at Irún. Cipher: a relation of [ ]'s pretensions; Lansac; an offer against Orange; the Archbishop of Cambrai; the Indies fleet. Date read 'xvj' (A) and '26' (B). Countersigned Idiáquez. No Pérez.
- 2026-10-05. **May 1580 (Mérida), f. 271** (witness A, v1.1; B pending). Clear: 'demas de las cartas vras a que se responde en las otras dos que van con esta'. Cipher: the governor of Burgundy and the Count of [ ]'s intelligence; Méndez de Vitoria; 'milord' Bretton: 'ya havréis entendido [por carta] de don Juan de Idiaquez lo que [a]pareció … señalarle pensión' (f271_A_dec l. 36–38) — Idiáquez writes to Vargas directly; 'el secreto que se tratava entre el secretario Villeroy y [ ] de Francia en Inglaterra' (l. 52–53; the scan's 'secretario' hits are Villeroy). No Pérez.
- 2026-10-05. **16 May 1580 (Mérida), f. 269** (witnesses A and B, v1.1). Clear: 'En otra que va con esta se responde a vuestras cartas desde … de Hebrero hasta … de Março'. Cipher: Alençon and Cambrai; Portugal (the Prior's ships, money); the Queen Mother's renunciation and the County of Burgundy; Parma; reprisals against French ships, Saint-Goard; Casimir; the Queen of Scots; a merchant ship taken. Countersigned Idiáquez. No Pérez.
- 2026-10-05. **28 Mar 1580 (Guadalupe), long letter ff. 257/263** (witnesses f257 v1.1, pass 2 short one strip; f263 v1.1, pass 2 a full fresh re-read rather than reverse; agreement 80%/76%, `align_f257_f263.txt`). Answers Vargas's letters of 29 Dec – 20 Feb. Cipher: Casimir's colonels and money; Lorraine; Cambrai; Norman ships for the Indies; La Rochelle and the Portuguese; Taxis and the Queen Mother; the Scottish ambassador on Guise; 'la vida y costumbre del nuncio … que reside en essa corte'; secret commissions to the governors of Narbonne, Bayonne and Montpellier; a person the Queen Mother 'embía secretamente' to Portugal; the Portuguese succession; the 'concierto' with Condé; movements in Languedoc and Dauphiné. Countersigned Idiáquez. Docket: received Paris 16 Apr 'con Gabriel Martin'. No Pérez (the scan's 'secretario' hit is 'secretamente').
- 2026-10-05. **f. 275 is not a royal letter.** f. 276v: '[[Para embiar à Su M.d]]' and the signature 'Vargas Mexia' (reader f275-A). It is Vargas's own cipher memorandum for the King on 'el origen que se entiende que tuvo el movimiento de franceses a la [parte] de Fuenterrabía': the Montauban assembly; the French King's claim to Navarre; Canfranc and Jaca in Aragon; the French King writing 'secretamente' three letters to Gramont; the Prince of Béarn. It pairs with the clear relation at f. 279 (Aug 1579). Out of H17's royal-letter scope; read anyway (Vargas's own text); no Pérez. f275-B pending.
- 2026-10-05. f. 271: second witness f271-B (v1.1).
- 2026-10-05. Third-party comparison done for the frozen letters (`thirdparty-compare07.md`): medians 76–89% vs controls 26–41%; cabinet-noir agrees on the Idiáquez countersignature, on both leak passages (same unread noun in f. 222), and has no Pérez reference after the arrest.
- 2026-10-05. **3 Jul 1579, f. 211** (baseline, one reader A, v1.1): a copy enclosed 'de lo que don Juan de Idiaquez me ha escrito' (Idiáquez, then in Venice) on Count Pedro Avogadro's qualities; the Marquis of Ayamonte (Milan) and Gerónimo Gondi; prisoners incl. a Captain Alberto de Ponte. Countersigned 'Ant.' with Pérez's looped flourish. No Pérez reference in the cipher. Idiáquez is already the King's correspondent before the arrest.
- 2026-10-05. **Correction: f. 275 is sent TO Vargas.** The endorsement on f. 276v reads "Para embiar à Ju.º de Vargas
  Mexia" (main thread on the image, `f276v_endorsement.jpg`; reader B agrees; reader A's "à Su M.d" was a misreading). It is
  a cipher relation from court on the origin of the French movement toward Fuenterrabía, the counterpart of the clear
  relation f. 279 ("Para embiar a Juan de Vargas", Aug 1579). Read by two witnesses; no Pérez.
- 2026-10-05. **8 Jun 1579 (Toledo), f. 206** (baseline, one reader A, v1.1). Cipher: Artois and Hainaut reconciled; Orange; Holland and Zeeland; a preaching friar at Antwerp; the succession of the kingdom of [#22]; and (f206_A_dec l. 29–31) '… [Juan Martín de Robledo?] y [su] criado entregó a Antonio Perez los despachos que él os havrá dado'. Pérez is named in cipher too before the arrest, as the receiver of Vargas's despatches. Countersigned 'Ant. Pz.' One witness only (baseline). Readers share /tmp/claude-501 as scratch; f206-A reported a folder collision and moved its crops (no transcription files there).
- 2026-10-05. **4 Jun 1579 (Aceca), f. 208** (baseline, one reader A, v1.1; noisy decode). Letters of 9 Apr – 1 May received; the Archbishop of Cambrai; French affairs. No hit for the H17 terms. Countersigned 'Ant.º Pz'.
- 2026-10-05. **f. 273** (reader A, Cipher 2, no second pass; `../06-premurder/decode_c2.py` → `f273_A_dec.txt`): Spanish heading "copia de lo que ha dado Mos de la Cruz a Su Magestad", then Italian: "Il signor Duca di Savoia, mio signore … servicio di Vostra Maestà … nelle imprese di Fiandra … li Spagnuoli". A Savoy memorial copied for Vargas; endorsed "Para embiar à Juan de Vargas Mexia". Agrees with pangoleen's identification (not opened; filename only). No Pérez.
- 2026-10-05 (after close). **The 13 Sep leak word: candidate "Consejo".** At the place where f. 226r has the single
  "h-like"/"he" letter-form sign ("6' [he] 28 6ρ.7. 17ρ 4̄"), the original f. 222r spells "d' 7ρ^ 23. 13. 23 28 7ρ.7. 17ρ 4̄"
  (main thread on the images, `leak_word_f222r_over_f226r.jpg`; reader f222-2 wrote "d.<acute> 7p<hat> 13. 13. 23"): "del
  con-se-je-s…". Reading: "lo que Lan[glée?] dezía de lo del Consejo … no es verisímil; todavía si él le huviere nombrado o dado
  más señal, será bien que lo digáis" — the suspected source of Saint-Goard's news of Madrid would be in the Council, and the
  King asks for a name. Status: CANDIDATE (one spelled duplicate; "-jes/-jos" ending and the "y doce/y coce" that follows
  unresolved; "he" as a code for Consejo occurs once). Not canon. Test: another occurrence of the "he" sign, or a Simancas
  minute of this letter.
- 2026-10-05 (after close). **Paz's Simancas catalogue for Vargas's side (`sources/paz-1579-1580.md`)**: K 1554–55, 1557,
  1558 summaries name no Pérez after the arrest. They corroborate many of our decodes (Cambrai castle, 13 Sep; Toulouse opinion,
  13 Nov; Hamilton's pension; the nuncio; the spy "Abadía"; Balfour; Méndez de Vitoria). **Correction:** the archbishop of the
  13 Sep letter is Cambrai, not Embrun (our "dam bra y" is "[C]ambray"). The leaked Portugal paper of 29 Nov is listed by Paz
  in K 1554–55: "Relación del Consejo de guerra de Felipe II sobre los medios de apoderarse de Portugal en caso de guerra".
- 2026-10-05 (after close). **f. 273, second witness B** (Cipher 2, v1.1, pass 2 complete; decoded agreement with A 81%/91%,
  `f273_B_dec.txt`). Both read the heading "copia de lo que ha dado Mos de la Cruz a Su Magestad de parte del [Duque de Saboya]"
  and Italian text. Reader B's margin date "16 de março de 1580" is the docket of f. 272v (f. 271's address leaf, visible at
  the gutter edge of the f. 273r image; f271-B read the same docket); the f. 273r margin itself has only "Dupp.do" (main thread
  on the image). pangoleen (opened only now, after both decodes were frozen; CLAIMANT) reads the same heading and dates the
  content to spring 1573 (Requesens's march; Vargas then ambassador in Turin), by inference. Not a royal letter; no Pérez.

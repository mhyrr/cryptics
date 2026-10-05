# 06 — The pre-murder letters: Don John and the Guises before 31 March 1578 (H16)

## Question
Before Juan de Escobedo was murdered (31 March 1578), did Philip II's letters to Vargas Mexía report, or ask about, a
Don John–Guise league, pact or "unión"? Pérez later named such a "confederation", denounced by Vargas, among the reasons
for the murder (Mignet 1846 pp. 68–69). Mignet answered that Vargas's reports on it are "presque toutes postérieures au
meurtre" (pp. 71–73, 435–436).

## Hypotheses (pre-registered 2026-10-04, before any reading in this experiment)
- **H16a**: a letter in the window (10 Dec 1577 – 31 Mar 1578) reports or asks about a Don John–Guise league, pact or
  "unión", beyond the marriage/England hearsay of Vargas's letter of 16 Feb 1578 (Teulet vol. 5 p. 137).
- **H16b**: none does. The window holds only that hearsay and the King's dismissive reply of 8 Mar 1578.
- **Test.** Every es. 132 letter of the window is read in full by our blind readers, and every Teulet excerpt of the
  window is checked against the printed page. H16a is supported by one clear passage quoted with token positions.
  H16b is supported when every window letter has been read and none has such a passage. Any letter not read is listed
  as the wall.
- What counts as "a league, pact or unión": words of agreement between Don John and Guise (or the Guises): liga,
  confederación, unión, concierto, inteligencia, tratar/correspondencia between them about a joint aim. Marriage or
  England hearsay already printed for 16 Feb does not count. A passage about the Guises alone (without Don John), or
  about Spain and France, does not count.

## The window in es. 132 (canvas map checked 2026-10-04 on Gallica thumbnails)
Canvas c shows f. (c − 2) on its right page for ff. 1–26, and f. (c + 3) for ff. 32 onward.
**ff. 26v–31r are not in the scan**: canvas 28 right is f. 26r, canvas 29 right is f. 32r (folio numbers read on the
images). So the letter of f. 26 has only its first page, and its duplicate (f. 28) is absent.

| Folio | Date | Cipher | Pages (canvas, side) |
|---|---|---|---|
| 3–4 | 16 Dec 1577 (Cayas) | 1 | 3r = c5 R; 3v = c6 L; 4r = c6 R |
| 11–12 | 24 Jan 1578 (Pérez) | 2 | 11r = c13 R; 11v = c14 L; 12r = c14 R; 12v = c15 L |
| 17–20 | 8 Mar 1578 (Pérez) | 2 | 17r = c19 R … 20v = c23 L |
| 22–25 | duplicate of 17–20 | 2 | 22r = c24 R … 25r = c27 R |
| 26 | 8/16 Mar 1578 | 2 | 26r = c28 R only (26v–31r not scanned) |
| 32–33 | 17 Mar 1578 (Cayas) | 3 | 32r = c29 R; 32v = c30 L; 33r = c30 R |
| 34–35 | 16 Mar 1578 (Pérez) | 2 | 34r = c31 R; 34v = c32 L; 35r = c32 R |
Clear letters of the window (ff. 5, 7, 9, 14, 15) are read on the image for Guise/Don John mentions, not decoded.

## Method (frozen order)
1. This README and H16 in `hypotheses.md`, committed first.
2. `decode_c2.py`: Tomokiyo's Cipher 2 table (`sources/keys/cipher2.tsv`) and his mark conventions. Run on Tomokiyo's own
   partial transcription of ff. 11r–12r (`tomokiyo_f11.txt`, his page, converted to our notation by `convert_tomokiyo.py`).
   Letter-forms the table does not value (free ρ, g, R, C, ♀, v, h, m, P, …) are reported as unknown.
   **Extensions**: any value added for such a sign is derived only from Tomokiyo's f. 11 text, written to
   `c2_extensions.tsv`, and frozen by commit before any blind transcription of ff. 17–25, 26 or 34 exists. Those letters
   are then held-out tests: an extension passes at ≥ 80% fitting occurrences (as in exp 05). f. 11 is in-sample.
3. `CIPHER2-GUIDE.md` (shapes only) from native crops of f. 11v. One blind calibration reader on f. 11v, scored against
   Tomokiyo's transcription (`calibrate_c2.py`, token-exact share).
4. Two blind readers each (Sonnet 5.5, no sub-agents) for ff. 17–20v, 22–25r, 11–12v, 34–35r, 26r; f. 32 (Cipher 3, guide
   v2.1). Readers see only the guide and the Gallica images. Each transcription committed before decoding. Reconciliation
   with `../05-cipher4-v2/align.py` and a blind reconciler (crops only).
5. **Mignet check (external, plaintext).** The decoded f. 17–25 must contain Mignet's two printed passages (app. E p. 437
   n. 2; p. 439 n. 5; read on the archive.org page images). `mignet_check.py` scores word recall in order.
6. f. 3 (Cipher 1): `decode_c1.py` from `keys/cipher1.tsv`. Devos's conflicting values (12 a, 21 e, 31 u) are reported, never
   chosen silently. If the table is too thin, the wall is named.
7. Teulet vol. 5 pp. 132–146 on the page images: the 16 Feb and 13 Apr 1578 passages quoted exactly. Also look for
   Mignet's undated "grande confidence" letter (Série B, liasse 44, n. 89; Mignet p. 439 n. 1) and the "investidura"
   letter (liasse 44, n. 84).
8. Third-party comparison only after our decodes are frozen (`thirdparty-compare.md`).

## Calibration texts (printed plaintext of the 8 Mar 1578 letter, from the Simancas minute B.47 n. 47)
- Mignet p. 437 n. 2: "Muy bien haveis hecho en avisarme de lo que el duque de Guisa havia comunicado..... y seria muy
  conveniente tener grangeados al dicho duque y a los de Guisa, y mantener los en mi devocion por los mejores medios que
  se pudiere. Y assy os ancargo que vos lo procureys por vuestra parte, tratandolo con la dissimulacion y cordura que vos
  sabreis."
- Mignet p. 439 n. 5: "Ha sido bien advertirme... sobre lo de los casamientos del rey de Escocia con la hija de Lorrena, y
  de mi hermano con la de Escocia. Y aunque estas cosas deven de ser por via de discurso y de poco fundamento, todavia es
  conveniente tener noticia de lo que se dize y discurre en semejantes materias."
Both read on archive.org `antonioperezetph00mign`, leaves 232–233 (page images, 2026-10-04).

## Result
- **H16a (league, confederation or unión between Don John and the Guises before the murder): refuted** on the letters in
  reach. No window letter uses such wording. The two "liga" passages (8 Mar, Brunswick; 17 Mar, Lorraine with princes of
  the Empire) do not involve Don John.
- **H16b (only the 16 Feb hearsay and the 8 Mar dismissal): weakened.** f. 12v (24 Jan 1578; readers A and B; cabinet-noir
  agrees), decoded lines 94–101 of `f11_B_decoded.txt`: "y de todo lo [que] los Guysas trataron con él [Sotomayor] cerca del
  proceder de mi hermano y con Alanson … cosas que tienen mucha consideración". Paz p. 382 (K 1543) summarises a
  Sotomayor–Guise conference "sobre el resentimiento que en la Corte de Francia tenían con D. Juan de Austria por su manera
  de escribirles".
- Mignet check on the 8 Mar letter: f. 17 A 84%/87%, f. 17 B 78%/86% (pass); f. 22 A 70%/72% (below the frozen 75%; both
  passages legible in `f22_A_joined.txt` lines 51–64 and 168–175).
- f. 3 (Cipher 1) reads: Vaux's mission, Namur, no aid to the rebels, 4,000 arquebusiers. f. 7r summarises it in clear.
- Third parties: `thirdparty-compare.md`.
- **Wall:** ff. 26v–31r not scanned (the rest of a March letter and its duplicate f. 28); Vargas's own dispatches of the
  window (AGS Estado K 1543–1547; Teulet prints Scotland excerpts only); Mignet's undated B.44 n° 89 ("grande confidence").
  Breach: PARES/AGS images or a Simancas reading-room request; Gallica for a rescan of ff. 26v–31r.

## Log
- 2026-10-04. `decode_c2.py` on Tomokiyo's f. 11 text (`tomokiyo_f11.txt`): continuous Spanish ("lo que me escrivis …
  mostrado que le embio mi hermano para que imprimiese", "con madama mi hermana", "la poca satisfacion que la Reyna madre
  tiene del dicho duque"). In-sample values for six letter-forms frozen in `c2_extensions.tsv` before any held-out
  transcription. Not valued: a free "g" (Tomokiyo also writes the g-shaped 9 as "g"), "m", "v", Tomokiyo's 〓 sign, and "1".
  Orthography, not extensions: 20 with a mark is consonantal v (escrivis, haver); 16+ is "qe" = que.
- `mignet_check.py` control on the f. 11 decode (a different letter): long passages 36% and 40%, short ones 57% and
  79% by chance. Only the two long passages (p437n2b, p439n5b) discriminate; pass mark for "the passage is in the
  letter" set now at ≥ 75% on both.
- Teulet pp. 132–146 checked on the page images (`teulet-check.md`). In the window, Don John appears only on 28 Jan
  (Vargas warned him of an English spy) and 16 Feb ("grandes quimeras"). The "dos coronas" letter is 13 Apr (B. 44 n. 57),
  Guise speaking of Spain and France.
- Canvas 29 left page (checked on the native image): an address leaf, "Por el Rey" / "A Juan de Vargas Mexia, Paris",
  docketed "16 de março de 1578". It is the outer leaf of a 16 Mar letter (probably f. 31v), so the scan really jumps from
  f. 26r to this leaf. The text of ff. 26v–31r is not imaged.
- 2026-10-04, readers: the first dispatch (13 agents, each fetching strips from Gallica) set off Gallica's rate limit
  within minutes; every request from this machine was refused for about an hour. All readers stopped; nothing was
  transcribed. Fix: `sources/cache/pages/fetch_pages.py` fetches each needed page once (one native request per page,
  20 s apart) after a probe succeeds; readers crop locally and make no network requests (guide v1.1 §0).
- Calibration (f. 11v, one blind reader, guide v1.1): 394/454 = 87% of Tomokiyo's tokens exact, 441/454 = 97% on the
  base (`calibration_f11v.txt`). Systematic: Tomokiyo's hook "11e" written "11+e" (11×); about a dozen dots above
  dropped (-o lost). Decoder v1.1 (frozen before any held-out decode): "+e" = the hook; "C" = c.
- **Clear letters of the window, read on the native page images (2026-10-04):**
  f. 5r (18 Dec 1577, Juan Delgado): Captain Cabreta goes to serve in Flanders by the King's order; send letters by him.
  f. 6r (6 Jan 1578, Pérez): four letters of 15 Dec received; Mos de Selles; "con esta se os embia un despacho para el
  Ill.mo don Juan de Austria mi hermano", to be sent on "con correo propio en diligencia". f. 6v: address leaf.
  f. 7r–v (18 Jan 1578, Cayas): opens "A xvj del passado os escriuí y embié a mandar el officio que auiades de hazer con el
  Rey Chr.mo y su madre, sobre las cosas de mis Payses baxos", i.e. the cipher letter of f. 3, summarised in clear
  (criterion 6 check of our f. 3 decode); audience to Saint-Goard and Gassot; no aid "publica ni secreta á mis
  rebeldes"; Mos de Selles; inform "al Ill.mo Don Juan de Austria mi hermano para que lo sepa".
  f. 9r (18 Jan 1578, Cayas): Low Countries news, the English, Antonio de Guaras.
  f. 14r (31 Jan 1578, Cayas): Bernardino de Mendoza to England via the French court; a letter of 4 Jan "con correo
  propio" had not arrived (no such letter in es. 132).
  f. 15r–v (19 Feb 1578, Cayas): Diego Fernández de Soto's ship, taken by a French ship; restitution via Saint-Goard.
  None mentions the Guises. Don John appears only as the recipient of forwarded dispatches and news.
- **f. 3 (16 Dec 1577, Cipher 1), two readers, decoded:** Longueval de Vaux, sent by Don John to the French court;
  Don John's withdrawal to the castle of Namur; Vargas to ask that the French King allow "ningún género de [ayuda] ni
  assistencia directa ni indirecta" to the rebels; Vaux's offer, on a count's behalf, of 4,000 arquebusiers for Don John,
  for which the French King refused leave to levy. No Guise. f. 7r summarises it in clear (above).

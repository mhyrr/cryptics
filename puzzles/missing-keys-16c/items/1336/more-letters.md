# No. 1336 — more letters in the Speciano–Borromeo cipher: scout report (2026-11-18)

Scope: find and describe candidates in the Ambrosiana OPAC. No signs were transcribed and nothing was read.
Images are the OPAC's 750 × 1,125 px JPEGs, cached (git-ignored) in `cache/more/<id>.jpg`. The URL form is
`https://ambrosiana.comperio.it/clavisng/index.php?file=<id>`, so each row gives only the id.

**Route.** Plain `urllib` requests to `opac/detail/view/...` and `opac/search/lst` return the OPAC's "Verifica in
corso / Checking" page, which runs a script check. A Playwright browser ran the check without changes and got
through, and every catalogue fetch below went that way. Image URLs are served directly to `urllib`. Bourdeau's
harvest of the same OPAC (October 2026, `research/milan_archives/ambrosiana_details.json` and `ambrosiana_hits.json`,
CLAIMANT tier as a route, PRIMARY as to content) gave the image ids for the records that carry a cipher note.

**Budget used.** 16 catalogue fetches out of 20, and 146 image downloads out of about 150. **I stopped because I
reached the image limit.** Leads 1 and 3 are exhausted as far as the catalogue notes go. Lead 2 got about 15–25
ids on each side of each held group, not 30 (see Not found).

## Candidates (images that show cipher signs)

| Image id | Shelfmark, folio | Date, correspondents | Cipher, roughly | Decipherment beside it? | Legibility at 750 px |
|---|---|---|---|---|---|
| **11447** | F 46 inf., n. 275, c. 652r ([record](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:594139)) | 1573. Catalogue: "Lettera di N.D. a N.D.", author indexed as Carlo Borromeo. Note: "Ep. scritta per lo più in cifra." | About 8 of 12 lines contain sign runs, mixed with clear Italian ("Le cause di sospicione…", "a S. S.", "per il quale"…). Sign runs of roughly 10–40 signs each, perhaps 150–200 signs in all. The shape inventory looks like ours: figures 4 6 7 8, l, q, x, A, K, M, H, a triangle, a hash, a small box, a ring/phi. | **No.** C. 652v (image 11446) is blank with show-through. The neighbouring units are clear: n. 274 (c. 651r–v, images 11444–11445, a clear text that names Mons. Carniglia and Mons. Speciano) and n. 276 (c. 653r, image 11448, headed "Poscritta"). | **Good.** The hand is clear and the signs are well separated, better than c. 269r. |
| **11170** | F 46 inf., n. 227, c. 515r ([record](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:594090)) | Rome, 14/10/1573. Giovanni Battista Castelli to Borromeo. Note: "L'ep. contiene due nomi in cifra." | One sign group of about 10 signs in mid-page (phi, 6, a cross, 7, a box among them), and a shorter group nearby. | **Possibly.** Interlinear clear words are written above both groups in a smaller hand. They look like a decipherment but I have not read them; this needs checking. | Fair. The page is cramped and the interlinear gloss is small. |
| **11173** | F 46 inf., n. 227, c. 516v (same record) | As above | One sign group of about 9 signs ("…intraina" followed by figures, a triangle, v, a cross, phi, 7, a box, q, 8). | None seen above it | Fair to good |
| 16419 | F 53 inf., n. 90, c. 182r ([record](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:595338)) | Rome, 21/11/1578. Speciano to Borromeo. Note: "Alcune parole dell'ep. in cifra." | In the second-to-last line, two short groups of figure-like signs (perhaps 3–4 signs each). I found nothing else at this size. | No | Poor to fair. The hand is dense and the groups are tiny. |
| 15827, 15828 | F 52 inf., n. 170, cc. 341r–342v ([record](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:595200)) | 30/07/1578. Borromeo to Speciano (a minute). Note: "Nomi cifrati." | Numbers stand for names, for example "Nel fatto di 739…". These are numeric name codes, not the sign alphabet. | The same text survives as the sent copy, n. 178 (next row), so it is not a decipherment. | Good |
| 15873 | F 52 inf., n. 178, c. 363r ([record](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:595211)) | Milan, 31/07/1578. Borromeo to Speciano. Note: "Nomi cifrati. Cfr. F 52 inf., n. 170." | The same numeric name codes ("739"…) | No | Good |

Two other Speciano letters from 1578 carry the note "Nomi cifrati": F 52 inf. n. 123 (15632–15635,
[record](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:595151)) and n. 124 (15636–15643,
[record](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:595152)). On the leaves I looked at closely
(15632, 15633, 15636, 15638, 15639, 15642), I saw only abbreviations such as "H.S." and "N.S.". Those are probably
ordinary forms of address, not cipher, and I found no sign groups. If these letters do have name codes, they are
likely numeric, like those in n. 170 and n. 178.

### Ranking for the dive

1. **F 46 inf. 275, c. 652r (11447).** It is the most cipher of any leaf found, it is legible, the shapes appear
   to be the same, it dates from 1573, and its neighbouring units name Carniglia and Speciano. It has no
   decipherment, so it would be a new text to read with key-v2, not a source for widening the key. A cipher letter
   inside the same Borromeo group is the strongest independent test of the key we could get.
2. **Castelli, F 46 inf. 227, cc. 515r and 516v (11170, 11173).** These are short, but c. 515r seems to carry an
   interlinear gloss above the signs. If that gloss is a decipherment and the table is the same, the group would
   widen the key; the visible shapes include phi and box, which have no value yet. Castelli is a different
   correspondent, so the table may differ. Check before relying on it.
3. **F 53 inf. 90, c. 182r (16419).** Speciano, 1578: a few signs, poorly legible. It is mainly useful for asking
   whether the sign alphabet was still in use in 1578, when the F 52 inf. letters use numeric name codes.

## Context found for the slip we already hold (F 47 inf. 131)

- F 47 inf. is the 1574 volume, 387 cc., 142 units
  ([volume record](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:49301)). Units 130, 131 and 132
  are all indexed under Speciano.
- **N. 130** ([record](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:594279)) is a letter from Cesare
  Spetiano to Cardinal Borromeo, Rome, 30/10/1574, on cc. 268r–v and 271r–272v, images 12034–12039. Its note
  reads: "Inserite anche le cc. relative alla ep. F 47 inf, n. 132, perchè poscritto della presente: cfr.
  FUSTELLA" ("The leaves of ep. F 47 inf. n. 132 are also included, because they are the postscript of this
  letter: see FUSTELLA"). Its subjects include Carniglia, Tolomeo Gallio (Cardinal of Como) and the Marchese de
  las Navas.
- **N. 132** ([record](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:594281)) is on c. 271r–v
  (images 12044–12045, byte-identical to 12036–12037). The record is dated 1574 and noted "Poscritto con
  segnatura propria" ("postscript with its own shelf number"). Its subjects are Carniglia, Gallio, Gregory XIII
  and Navas. On the image it is headed "Poscritta" and written in clear text.
- So the cipher slip, cc. 269–270, is physically **inside** the letter of 30 October 1574: c. 268 is the letter,
  cc. 269–270 the slip and its translation, c. 271 the postscript and c. 272 the address leaf. Carniglia, a
  subject of n. 130 and n. 132, is also named in our reading of the slip. **It is an inference, not established,
  that the slip is the cipher enclosure of the 30 October letter.** The catalogue sends the attribution to
  RIVOLTA; check it there. All the leaves of n. 130 and n. 132 are clear text.

## Lead 1: the correspondence, volumes 1573–76

The OPAC full-text search "Spetiano" returns 1,695 records, 1,652 of them indexed under Speciano
([search](https://ambrosiana.comperio.it/opac/search/lst?q=Spetiano)). The searches turned up these volumes for
1573–76. This is not a full census: the year facet does not cover these records, and full-text search on a year
matches only a few of them.

| Volume | Dates seen | Source |
|---|---|---|
| F 46 inf. | 23/09–11/11/1573, letters both ways; also Castelli, Ormaneto and the unit 274–276 cluster | [search](https://ambrosiana.comperio.it/opac/search/lst?q=Spetiano), [volume](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:49300) |
| F 128 inf. | Speciano to Borromeo, 19/09–12/12/1573 | [search "Spetiano 1574"](https://ambrosiana.comperio.it/opac/search/lst?q=Spetiano+1574) |
| F 129 inf. | 20/02–13/03/1574 | same |
| F 130 inf. | 03/04/1574 | same |
| F 87 inf. | 12/06/1574 | same |
| F 131 inf. | 04/07/1574 (the leaf we hold) | same |
| F 47 inf. | 1574: 24/07, 14/08 and 30/10/1574, plus the slip | same; volume above |
| O 178 sup. | Copies of Borromeo's letters to Speciano, 27/01 and 17/02/1574 | same |
| F 49 inf. | 02/03/1575 (the leaf we hold) | gate.md |
| F 50 inf. | Borromeo to Speciano, 16/10, 24/10, 04/11/1576 | [search](https://ambrosiana.comperio.it/opac/search/lst?q=Spetiano) |

## Lead 3: catalogue notes on cipher

These searches found nothing beyond the rows above and the records we already hold: "Spetiano cifra",
"Spetiano cifr\*", "Speciano cifr\*" (12 hits), "Ormaneto cifr\*" (1 hit, a payment "cifra" in scudi, P 7 inf.;
not cipher), "Carniglia cifr\*" (2), "Castelli cifr\*" (2) and "Galesini cifr\*" (0). Bourdeau's harvest of
34 cipher terms over the whole OPAC (359 hits) contains no further item in the 1572–77 Borromeo volumes. The
catalogue notes are an incomplete guide: n. 130 and n. 132 in F 47 inf. have no cipher note because the cipher is
filed as n. 131, and F 46 inf. 275 is noted only as "N.D. a N.D.".

## Looked at, no cipher

Viewed one by one at full or 700 px: 12034, 12035, 12036 (= 12044), 12037 (= 12045), 12038, 12039, 11446 (blank
verso of 652), 16418, 16420, 16421, 15632, 15633, 15636, 15638, 15639, 15642, 15851, 12517–12528, 11171, 11172,
11174, 11175.

Viewed on contact sheets at about 500 px. Isolated groups of one to three signs could be missed at that size.
- 12010–12033 (F 47 inf. cc. 256–267, Carniglia and Speciano letters, October 1574)
- 12046–12060 (F 47 inf. cc. 272–279, November–December 1574; 12058–12060 may already be F 48 inf.)
- 89411–89420 and 89425–89440 (F 131 inf. cc. 6–25, other correspondents, early July 1574)
- 12531–12540 (F 49 inf. cc. 45–49, March 1575)
- 11440–11445 and 11448–11452 (F 46 inf. cc. 649–655, the units around n. 275)

## Downloaded but not inspected

These are F 52 inf. leaves (1578, numeric "nomi cifrati"), left because their codes are not the sign alphabet:
15634, 15635, 15637, 15640, 15641, 15643, 15829, 15830, 15849, 15850, 15852–15856, 15872, 15874, 15875.

## Not found

- No further 1574–75 leaf carries the sign alphabet in the ±15–25 ids around 12040–12043, 12529–12530 and
  89421–89424. The full ±30 was not covered: 12000–12009, 12061–12073, 89391–89410, 89441–89454, 12499–12516
  and 12541–12560 are still unseen.
- No decipherment for F 46 inf. 275 in the neighbouring units 274 and 276. Nor is there one in the F 49 inf. 18
  letter (cc. 38–43), which is clear throughout.
- No catalogue note for any Ormaneto or Galesini letter in cipher in these years.
- Not attempted: paging through the full lists of the F 128–F 131 inf. volumes (Speciano's own letters, 1573–74).
  Their units are not noted as cipher, but F 47 inf. shows that the notes miss things. This is the next lead.

## Unverified claims

- That F 46 inf. 275 uses the same table as the F 47 and F 49 slips. This rests on shape resemblance only and
  needs the key test.
- That F 46 inf. 275 is by Borromeo, or from his secretariat, and to whom it went. The OPAC indexes Borromeo as
  author but titles it N.D. to N.D. Units 266–284 around it are mostly Borromeo's letters to Castelli, the nuncio
  in Spain, Ormaneto and Carniglia.
- That the interlinear words on Castelli c. 515r decipher the sign group beneath them. Not read.
- That the cipher slip F 47 inf. 131 is the enclosure of Speciano's letter of 30/10/1574 (n. 130). This is
  inferred from the folio order and the catalogue note on n. 130; RIVOLTA not consulted.
- The 1578 F 52 inf. "nomi cifrati" being numeric throughout: I checked this on nn. 170 and 178 only.

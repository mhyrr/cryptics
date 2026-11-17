# Gate: item 2911 (with 2910 and 1549)

Stage 0 scout, 2026-11-16. Scope as in `PIPELINE.md` stage 0. No sign values were read or assigned, no key
work was done, no key file of any project was opened. Rough counts below come from looking at pages, not
from a script.

**Item 2911**: Dieci di Balìa to Machiavelli at the French court, Florence, 17 Aug 1510, BNCF Autografi
Palatini, Carte Machiavelli V/134 (lapis "134", old foliation 230), 2 ff.
**Sibling 2910**: "Summario di l(ette)ra d(e) 18 dì" (summary of a letter of the 18th), V/125 (lapis "125",
old foliation 252), 1 leaf, enclosure of V/124. **Related 1549**: Luppi to Machiavelli, [14 Jul] 1510, I/3.

## Proposed verdict

- **2911: `go`, on one condition the main thread should settle first: check that the period key sheets
  Carte Machiavelli VI/82 (online, see check 5) are not this cipher.** If one of them is, 2911 becomes a key
  lookup and the pipeline says skip.
- **2910: `go`, together with 2911**: the same sign system by look, same chancery, five days later. It
  should be read as a second bare letter with the key 2911 builds, not as a separate item.
- **1549: no gate of its own here.** By an earlier vetting it is the same sign family. Read it as a
  third bare letter once the key passes. The catalogue's "Teca serves only about 900 px" is wrong: 300 dpi
  masters are served (recipe below). Not fetched in this run.

## 1. Race and prior art

| check | result | evidence |
|---|---|---|
| Bourdeau issues and PRs | No issue or PR mentions 2911 or 2910. "Machiavelli" finds #590 (closed 14 Nov, on 1549: sender is Luppi), #206 (closed, printed-prior-art check) and PR #248 (closed, marked lead 1548 = V/140 + V/139 "existing at edition level"). Nothing open on these shelfmarks. | GitHub search API `repo:dbourdeau/cyphersolver` for Machiavelli, Dieci, 2911, 2910, 1549, 2026-11-16 |
| Site pages | /solve/2911.html and /2910.html show the catalogue status text and "Open a solution issue". There is no reservation or progress note. | https://cyphersolver.com/solve/2911.html, /2910.html, /1549.html |
| Bourdeau targets | No `targets/*/profile.json` concerns Machiavelli or the Dieci of 1510. `florence1414`, `florence1429` and `medici1425` are other Dieci ciphers of the 1400s. `line/taken.tsv` does not list 2911, 2910 or 1549. | `sources/cache/bourdeau-profiles-2026-11-16.json` (titles grepped) |
| Tomokiyo | `unsolved.htm` has no Machiavelli, Firenze, Dieci or Soderini. `crypto.htm` has only "Florentine Ciphers of Guicciardini (ca.1590-1593)". | https://cryptiana.web.fc2.com/code/unsolved.htm, /code/crypto.htm, fetched 2026-11-16 |
| DECODE | The search page is JavaScript and did not return results to a script. **Not verified this run.** The catalogue vetting (known.py over the DECODE dumps, 16 Nov) found no record. | https://de-crypt.org/decrypt-web |
| Opere VI (Passerini-Milanesi 1877) | **Does not print a Dieci letter of 17 Aug 1510.** The 1510 legation runs from Machiavelli's letter "Ex Bles, die 13 augusti 1510" (From Blois, 13 August 1510) straight to "I Dieci al Machiavelli. Die 18 augusti 1510" (the Ten to Machiavelli, 18 August 1510; this is V/135, pp. 72-74). V/125 is not printed either. The volume does print many sibling cipher letters with source notes such as "È tutta in cifra" (it is all in cipher), e.g. V/126, V/129, V/131, V/137, V/139. | archive.org `leoperediniccol03milagoog` djvu text |
| Chiappelli, *Legazioni, commissarie, scritti di governo* (Laterza 1971-85) | Stops at 1505, so it does not cover this letter. | archive.org `271MachiavelliLegazioni3Si168`, `272MachiavellLegazioni4Si169` (texts: years 1503-1505 only) |
| Bertelli, *Legazioni e commissarie* (Feltrinelli 1964) | On archive.org as lending-only (`legazioniecommis0002nicc`, `bwb_S0-DQS-837`); the text is restricted. **Not checked.** | archive.org metadata |
| Edizione Nazionale, *Legazioni. Commissarie. Scritti di governo* (Salerno 2002-2011) | Issue #206 says the 1507-1510 volume prints V/139 and V/140 "in clear from the ASF register". The volume itself could not be opened. **Whether it prints V/134 or V/125 is unverified.** | issue #206; one web search found nothing more |
| ASF Dieci di Balìa, missive register for 17 Aug 1510 | Probably holds a clear minute of V/134, since the edited Dieci letters of 1510 come from those registers. **Not checked**, and not online as far as this run found. | (inference from #206, not a fact) |

What could not be verified: whether Bertelli 1964 or the Edizione Nazionale prints the 17 Aug letter or the
"Summario" in clear. If either does, 2911 is still a valid blind test (the edition becomes the stage 6
check), but it is not a new reading. Two web searches (the Italian date with Dieci and cifra; the
Edizione Nazionale volume with cifra/decifrato) found nothing on either letter.

## 2. The pair

The catalogue entry does not name a single pair. It claims class A from printed siblings (V/124,
V/126-131, V/135, V/138, V/150) and from Machiavelli's interlinear decipherments (V/130, V/141-149, IV/111).
On the images, the candidates are:

| pair | form | of this very text? | size | note |
|---|---|---|---|---|
| **V/140** (Matteo Niccolini's letter from Rome, 5 Aug 1510, copied in cipher by the Dieci) **+ V/139 cc. 1v-2r** (Machiavelli's autograph decipherment, headed "Copia d'una l(ette)ra da Roma de' 5 d'agosto", copy of a letter from Rome of 5 August) | **A1**, period, separate leaves (V/140 is filed as V/139's enclosure) | Yes. The BNCF record says the decipherment is of the enclosure V/140, and the heading and date match. The record also calls it "inexatta ed incompleta" (inexact and incomplete). | cipher about 85 lines, about 3,800 signs; clear about 57 lines, about 600 words | **Recommended pair.** Its clear text is also printed (Opere VI pp. 54-55 n. 1; Bertelli app. A pp. 1352-53, per BNCF and #206). That gives a second plaintext where Machiavelli's is incomplete, but the pipeline does not define a "print" witness: flag it. V/140 itself is Bourdeau lead 1548 (existing at edition level), so it is used as a pair, not claimed as a reading. |
| V/136 cc. 5-6 (copy of the Dieci's letter to Francesco Pandolfini at Milan, 18 Aug 1510, all cipher after one clear line) + V/136 c. 7 (a **modern** sheet on ruled paper, "Copia di lettera a Francesco Pandolfini a Milano", copy of a letter to Francesco Pandolfini at Milan) | A1, but **modern** (19th-century hand), not period | Yes. c. 7 begins with V/136's clear opening line ("Magnifice vir etc. Havendo ricevuto la tua de' VII tenuta alli X fino martedì che fummo a dì XIII", Magnificent sir, having received yours of the 7th, kept until the 10th, until Tuesday, which was the 13th) and runs on into the part the original has in cipher. | cipher about 78 lines, about 3,400 signs; clear about 36 lines, about 400 words: **partial**, roughly the first half | Second pair, or a held-out check. Source of the modern text (a decipherment, or a copy from the ASF register) unknown. |
| V/135 (18 Aug 1510, all cipher after "Sp(ectabi)lis vir etc.") + Opere VI pp. 72-74 | **print only** | Yes, by date and position; Opere VI prints it without a source note in the OCR | cipher about 70 lines | Not defined by the pipeline. Visual note only: V/135 and V/134 open, right after "Sp. vir etc.", with the same run of signs. |
| V/123 (cipher postscript slip + Machiavelli's decipherment slip) | A1, period | Yes (BNCF record) | about 9 lines each | Too small to stand alone; a useful held-out check. |
| V/139 c. 1r line 3 | A2 | Yes | one line | Negligible. |
| Machiavelli's interlinear decipherments in V/141-149 (and an interlined page at V_124_133 c. 14r, shelfmark not identified) | A2 | not examined | not counted | Pages fetched at survey size only. |

**Same sign set?** By look only, yes. V/134, V/125, V/135, V/136, V/140 and V/139 c. 1r share one
repertoire: lower-case letter forms (r, g, s, t, b, o, a, e, c, p...), figures (2, 3, 4, 8), invented
marks (a boxed sign, a crossed x, a φ-like sign, a ∂-like sign, a ♀-like sign), small superscript o's and
dots over signs, and frequent doubled signs (bb, ss, tt, aa, rr). The hand is the same chancery hand
throughout. This is a judgment of shape, not a test.

## 3. Images

**Recipe.** Page list: OAI-PMH `https://teca.bncf.firenze.sbn.it/OAI/servlet/OAIHandler?verb=GetRecord&metadataPrefix=mag&identifier=oai:bncf.firenze.sbn.it:21:FI0098:AutografiPalatini:Machiavelli_<V_134_136|V_124_133|V_139|...>`
(each `<mag:img>` gives the carta and its image id). Image: `https://teca.bncf.firenze.sbn.it/ImageViewer/servlet/ImageViewer?idr=<image id>&azione=showImg&usage=2`
serves the **300 dpi master (about 2700 x 3700 px)**. Without `usage=2` it serves the viewer's 100 dpi
copy (about 920 x 1220 px), and `height`/`reduce` change nothing. The MAG's own file URLs on
`digitale.bncf.firenze.sbn.it` return 404. The viewer's `azione=readBook` gives the same page list. The
Internet Culturale record pages sit behind a captcha. The MAG groups several documents in one folder
(`V_134_136` = V/134, V/135, V/136). The document boundaries were read from the lapis numbers top right
and are recorded below.

Script: `fetch.py` (masters of the pages below; `--survey` for viewer-size copies of every page of the six
folders). 29 masters and 119 survey copies are in `cache/`, one line each in `PROVENANCE.md`. Licence per
the Teca: CC BY-NC 4.0 for freely accessible content.

**Legibility.** At the master size a cipher line of V/134 is clearly legible, sign by sign, including the
superscript marks. At the viewer's 900 px the superscripts and dots are marginal. Machiavelli's cursive
decipherment in V/139 is legible at master size, but it will need careful readers.

### Page inventory

| file (cache/) | shelfmark | what it is | kind | lines | rough signs |
|---|---|---|---|---|---|
| V_134_136_02_1r.jpg | **V/134** c. 1r | Dieci to Machiavelli, "Ex Palatio florentino Die xvij Augusti 1510" | mixed: line 1 clear, line 2 half clear | 16 (14 cipher) | about 580 |
| V_134_136_03_1v.jpg | V/134 c. 1v | blank | - | 0 | 0 |
| V_134_136_04_2r.jpg | V/134 c. 2r | faint address or docket (not read) | clear | few | 0 |
| V_134_136_05_2v.jpg | V/134 c. 2v | address to Machiavelli, "In Corte" (at court), seal | clear | 5 | 0 |
| V_134_136_06_3r.jpg, _07_3v | V/135 cc. 3r-3v | Dieci, 18 Aug 1510 (printed Opere VI 72-74) | cipher | about 35 + 33 | about 3,000 |
| V_134_136_08_4r.jpg, _09_4v | V/135 c. 4 | blank; address | clear | - | 0 |
| V_134_136_10_5r.jpg, _11_5v, _12_6r, _13_6v | V/136 cc. 5-6 | "Copia di l(ette)ra a Franc(esc)o Pandolphini in Milano" (copy of a letter to Francesco Pandolfini at Milan), dated "Die xviij Augusti" | cipher, line 1 clear | about 32 + 38 + 8 | about 3,400 |
| V_134_136_14_7r.jpg, _15_7v | V/136 c. 7 | modern clear text of V/136 (partial) | clear (modern) | about 28 + 8 | about 400 words |
| V_124_133_10_5r.jpg | **V/125** c. 5r | "Summario di l(ette)ra d(e) 18 dì", ending "Bene vale. Ex Palatio Flor(enti)no Die 22 Augusti 1510" | cipher (heading and date clear) | about 24 (19 + 5 in a second block) | about 1,050 |
| V_124_133_11_5v.jpg | V/125 c. 5v | blank | - | 0 | 0 |
| V_140_02_1r.jpg, _03_1v, _04_2r | **V/140** | Niccolini, Rome, 5 Aug 1510, Dieci copy; first words "Dopo l'ultima mia etc." (after my last etc.) clear | cipher | about 40 + 40 + 5 | about 3,800 |
| V_140_05_2v.jpg | V/140 c. 2v | blank | - | 0 | 0 |
| V_139_02_1r.jpg | V/139 c. 1r | Dieci, 7 Aug 1510; two clear lines, line 3 glossed interlinear | mixed | about 18 | about 650 |
| V_139_03_1v.jpg, _04_2r | **V/139** cc. 1v-2r | Machiavelli's decipherment of V/140 | clear | about 30 + 27 | about 600 words |
| V_139_05_2v.jpg | V/139 c. 2v | address | clear | - | 0 |
| V_123_02_1r.jpg … _06_3r | V/123 | modern wrapper; cipher slip (about 9 lines); blank; decipherment slip (about 9 lines); blank | cipher / clear | 9 / 9 | about 400 / about 90 words |

Folder V_124_133 also holds V/124 (cc. 1-4, two ciphered leaves and an address; old 237, 236, 239),
V/126 (c. 6, old 238), V/127 (c. 7, old 242, with marginal notes), V/128 (cc. 8-9), V/129 (c. 11) and
later items. These are printed siblings, available as further "print only" material. They were not
fetched as masters.

## 4. Size

- **Pair (V/140 + V/139 cc. 1v-2r):** cipher about 3,800 signs over about 85 lines. Plain side about
  600 words over about 57 lines, incomplete by BNCF's note. Well over the 150 bar. V/136 + c. 7 adds about
  1,500-2,000 cipher signs covered by about 400 modern words.
- **Bare letters:** V/134 about 580 signs (14 cipher lines); V/125 about 1,050 signs (about 24 lines).
  1549 (I/3), per its vetting: about 32 lines.

## 5. A period key

**A candidate survives online and has not been tested.** BNCF Carte Machiavelli **VI/82**, 9 ff., five
"Cifrario" units, on Teca (folder idr BNCF0003858588; OAI `Machiavelli_VI_82`). The BNCF record quotes
the old index: "chiave delle cifre usate dal governo di Firenze nella corrispondenza col Machiavelli, con
Francesco Pepi, con Francesco Gualterotti e Luigi della Stufa, con Mess. Goro ed altre" (the key of the
ciphers used by the government of Florence in its correspondence with Machiavelli, with Francesco Pepi,
with Francesco Gualterotti and Luigi della Stufa, with Messer Goro and others). VI/82 1° is endorsed
"Cyfra co(n) li O(rato)ri di Francia, it(em) per Roma co(n) m(esse)r F(rancesco) Pepi, con m(esse)r
F(rancesc)o Gualterotti et Luigi d(e)lla Stufa o(rato)ri al Re (Cristianissi)mo" (cipher with the orators
of France; also for Rome with Messer Francesco Pepi; with Francesco Gualterotti and Luigi della Stufa,
orators to the Most Christian King). The names in the units point to 1502-1503 (Valentino, Vitellozzo,
Rouen) and 1510 (Chaumont, La Trémoille). This run did not open the VI/82 images: that would be key work.
The 1549 vetting viewed them and did not apply them.

**If one VI/82 unit is the 1510 Dieci–Machiavelli system, the item is a key lookup, not a key build
(pipeline: skip and note).** If none is, VI/82 stays as the outside check for stage 7. Other places not
checked: ASF *Cifrari*/*Chiavi delle cifre* (the source of the `florence1414` key), DECODE key records
(not searchable by script), Machiavelli's own decipherment notebooks I/80-I/81 (they are decipherments,
not a key).

## Notes from looking only

- Sign system: letters, figures and invented marks, with superscript o's and dots over signs. Doubled
  signs are frequent. Words do not look separated: gaps are irregular.
- Clear text inside the cipher: V/134 has "Sp(ectabi)lis vir etc. Dopo l'ultima de' x mandatati per mano
  del Pandolphino comparse …" (Worshipful sir etc. After the last, of the 10th, sent through Pandolfini,
  there arrived …) and, on line 2, a clear stretch "… et di nuovo non haviamo di poi che … salvo …" (and of
  news we have nothing since … except …). These readings are tentative. It closes "Bene vale. Ex Palatio
  florentino Die xvij Augusti 1510" (Farewell. From the Florentine Palace, 17 August 1510), subscribed
  "Decemviri Libertatis et Baliae R(ei) P(ublicae) Florentinae" (the Ten of Liberty and Balìa of the
  Florentine Republic).
- Surprise: the Teca serves 300 dpi masters with `usage=2`. Earlier notes in the catalogue (1549, 2910,
  2911) say only about 900 px is available.
- Surprise: V/136 carries a modern clear text that the catalogue calls "partly deciphered on a modern
  slip". It is a full page and more, and it is of V/136 itself.

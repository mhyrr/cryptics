# Headers, annotations and the transcription check

Source for everything below unless stated: BAR E4320B#1974/47#277*, subdossier 0000066, Unterlagen_0000072,
read from the full-size IIIF images on 2026-10-16 (PRIMARY; files and hashes in `PROVENANCE.md`).
Handwriting readings are ours; uncertain ones are marked (?).

## Telegram 1 (canvas 9; fold views c10, c11; reverse c12)

The object is a printed PTT form "Telegramm – Télégramme – Telegramma" (foot of form: "No. 1 – Format A 5
(148 × 210)"), with a typed tissue sheet attached over its address and text area.

| Field | Reading |
|---|---|
| Stamp, top left (violet) | `II A* 49.90z` (series/class II; fee 49.90, "z" probably Swiss francs) |
| No. (serial) | `- 1381` (violet stamp) |
| Datum | `-8 JAN -37` (violet stamp) |
| Pencil, top centre, circled | `8/I` (8 January) |
| Stunde – Heure – Ora (handed in) | `-11 31` (violet stamp): 11:31 |
| Bureau – Ufficio | `ZURICH` stamp and `797` (office number) |
| Wörter – Mots – Parole (words) | `125`, pencil |
| Taxe – Tassa / Total | empty |
| Befördert – Expédié – Spedito (sent on) | nach `London Mcl.` (violet stamp); Stunde `1142` (11:42); Name `kl` (operator's initials) |
| Routing, pencil above the address | `Angleterre Eastern` ("[via] England, Eastern [Telegraph Company]") |
| Address, typed | `BLUME  SALAMANCA` (SALAMANCA underlined), then typed `(VIA VIGOEMDENKABEL)` struck through in blue crayon ("via Vigo–Emden cable", replaced by the Eastern routing) |
| Pencilled counts in the text | `(50)` after group 48 ACCEL, `100` (superscript) after group 98 TNCEN |
| Pencil, left margin | `als Chiffriert aufgegeben` ("handed in as cipher") |
| Pencil, right margin | a single sign, `Gi` or `G` (?) |
| Red crayon, lower left | `Aufgabe: Oswald Viktor, geb. 15.11.1909, in Burgos Z` ("Handed in [by]: Viktor Oswald, born 15 Nov 1909, in Burgos"); a black pencil `Z` follows |
| Sender block (pencil, boxed in blue) | `Oswald, Bahnhofstr. 12` |
| Sender block (pencil, lower right) | `Telephon: 72150 ab 9.V.36` ("Telephone 72150 from 9 May 1936"), `Dr. ing. W. E. Oswald, Bureau Bahnhofstr 12` |
| Reverse of the attached tissue (c11, c12) | pencilled fee arithmetic, partly legible: `80`, `40`, `47.–`, `9.40`, `3.95` (?), `28.–`, `13.55`, `48.–`, `190`, `11.55`, `49.90`, and below a rule `59.05` (?). We have not reconstructed the sum; the stamped fee is 49.90 |

**Word count check.** 123 groups + BLUME + SALAMANCA = 125 = the Wörter box. The pencilled (50) falls after
group 48 (48 + 2 = 50) and the 100 after group 98 (98 + 2 = 100): the clerk counted the address as two words
and every five-letter group as one. Group 113 (RBEEP) is word 115, so it was counted and charged.

## Telegram 2 (canvas 13; reverse canvas 14)

The object is a plain greenish tissue sheet, not the printed form; no Wörter box is visible on it.

| Field | Reading |
|---|---|
| Stamp, top (violet) | `I A* 14.00z` (class I; fee 14.00), serial `- 1486`, date `-8 JAN -37` |
| Time handed in, top right (violet stamp) | `17 – 34`: 17:34 |
| Office | `910` and `ZURICH` stamp |
| Routing, violet pencil | `„Via angleterre Eastern“` ("via England, Eastern"), and below it `3 H W` (?, meaning unknown) |
| Fee, violet pencil, right | `14 fr`, underlined in blue |
| Stamp, left (violet) | `Cde` (see Unverified) |
| Address, typed | `BLUME  SALAMANCA` (SALAMANCA underlined); no struck routing line |
| Pencil, right of text | a large initial or paraph, `Ok` or `Oh` (?) |
| Pencil | `Oswald, Bahnhofst. 12.` |
| Sent on | `London Mcl.` (violet stamp), pencil `1740 kl` (17:40, operator kl) |
| Sender block, pencil, boxed | `Absender: Dr ing. W. E. Oswald, Bureau Bahnhofstr 12, Zürich` ("Sender: …"; the middle initial could be read as L, but telegram 1 and the archive's own records give W. E.) |
| Reverse (c14), violet pencil | `47 × 34 = 188 + 141 = 15.98`, then `16.60`, and a `2` to the right: 0.47 × 34 words = 15.98 |

**Word count check.** 32 groups + 2 = 34, the multiplier on the reverse. The form itself carries no word count.
The 0.47 rate times 34 gives 15.98 (with 16.60 written below), not the 14.00 stamped on the front; we have not
explained the difference.

Both telegrams went from Zurich to London (Mcl. = probably the London cable office or company relay) for
onward carriage by Eastern Telegraph; the first at 11:31 / 11:42, the second at 17:34 / 17:40, the same day.

## The transcription check

**Blind reading first.** We read all 123 + 32 groups from the BAR images (row strips at native resolution,
then 4 × 4 blocks at ~1.8×) before opening Bourdeau's `ct1.txt` / `ct2.txt`.

* Telegram 2: our blind reading matched Bourdeau's and Bean's hash (`8fd5cfb8…`) at the first try.
* Telegram 1: our blind reading differed in **one letter**: group 61 read ANIPS. At group zoom (crop
  ~230 × 70 px of the original, enlarged 4×) the third letter has no serif at the top right and a long foot
  running right to touch the P: it is **L**, so **ANLPS**, as Bourdeau and Bean have it. Our blind misreading
  was ours, not the form's. With it corrected, our 615 letters hash to `e266615d…`, the published value.

**The glyph test.** On this typewriter the **I** carries a slab serif at both top and bottom, symmetric about
the stem (compare the I in IPLAN, RSIUO, IINPE, LIAIN). The **L** has a top serif on the left only and a long
foot to the right (compare LGMAL, LIAIN, AXLNK, REFLX, DRODL).

| Group | Reading | Evidence |
|---|---|---|
| 38 | **SOLRS** | third letter: left-only top serif, long right foot reaching under the R; not the symmetric I |
| 48 | **ACCEL** | final letter: same L shape; the right foot runs into the pencilled "(50)" |
| 122 | **FTULX** | fourth letter: L foot extends right nearly to the X; compare the I of IPLAN on the same line, which is symmetric |
| 61 | **ANLPS** | as above (our only blind-reading slip) |
| 113 | **RBEEP** | letters fully legible under the red crayon stroke, which is the underline of the red "Aufgabe:" note running across the bottom left of the text, not a deletion. Counted in the 125 words |

Issue 14's correction (SOIRS→SOLRS, ACCEI→ACCEL, FTUIX→FTULX) is confirmed on the archive scan. We find
no other disagreement with Bourdeau's current text or Bean's hash.

**Other marks on the text.** Pencil (50) and 100 (word counts); red crayon over RBEEP and the start of IPLAN
(underline of the red note); nothing else is written over the groups. On c11 the attached tissue is folded back
and its groups show through in reverse (the same text, e.g. IPLAN FTULX REFLX, RBEEP DRODL …); they are not a
second text.

## The rest of the dossier

Checked: all 14 canvases of Unterlagen_0000072 viewed (c01 PTT letter, c02 blank, c03–c08 Hunziker bomb
drawing and photographs with their backs, c09–c14 the two telegrams with fold views and reverses); and a
text search of the BAR OCR for the whole dossier (219 OCR files, all subdossiers) for *Blume*, *Salamanca*,
*chiffr*, *Schlüssel*, *Oswald*, *Telegr*. The other units of subdossier 0000066 (Umschlag 67, Unterlagen 68,
Dokument 69, Unterlagen 70, Dokument 71) were downloaded at 1000 px and covered by the OCR search, not read
image by image.

Findings:

* **c01**, PTT Generaldirektion, Rechtsdienst, to the Bundesanwaltschaft, Bern, 15 Jan 1937, ref. 6011.8.3,
  received 15 Jan 1937 (stamp, file C.8.1.), subject "Neutralität gegenüber Spanien" ("Neutrality towards
  Spain"): "Wir beehren uns, Ihnen vertraulicher Weise die beiliegenden 2 Abschriften von chiffrierten
  Telegrammen von Zürich nach Salamanca zur gef. Kenntnis zu übermitteln" ("We have the honour to send you
  confidentially, for your information, the enclosed 2 copies of cipher telegrams from Zurich to Salamanca").
  Note: the letter calls them *Abschriften* (copies), but what survives bears the office stamps, times and
  operator initials of handed-in forms.
* **Dokument_0000069** (OCR), Werner Oswald's interrogation: asked about "den beiden am 8. Januar 1937 von
  Zürich nach Salamanca aufgegebenen, chiffrierten Telegrammen … wo haben Sie den Schlüssel dazu?" ("the two
  cipher telegrams handed in at Zurich for Salamanca on 8 January 1937 … where do you have the key?"), he says
  his brother Viktor sent them while passing through Zurich, about wool buyers and keeping Hisma (Seville)
  uninformed until Burgos had been approached; "Den Inhalt kenne ich nicht … Den Schlüssel besitze ich
  ebenfalls nicht, da ich selbst mit meinem Bruder nicht chiffriert verkehre" ("I do not know the content …
  Nor do I have the key, since I myself do not correspond with my brother in cipher").
* **Dokument_0000071** (OCR) identifies Viktor Oswald, b. 15.11.1909, bank clerk, living in Burgos, matching
  the red note on telegram 1.
* **No key, no plaintext, no worksheet and no third ciphertext** turned up. This agrees with Bourdeau
  (NOTES.md, fourth session, CLAIMANT). The OCR is machine OCR and unreliable on handwriting, so a key written
  by hand elsewhere in the dossier could have been missed by the search; we did not view the other 200-odd
  units' images.

## Unverified claims

* `Cde` stamp on telegram 2: we suspect the service indicator for a telegram in code language (CDE) under
  the 1932 Madrid Telegraph Regulations, charged at a reduced rate, which would bear on the 14.00 vs 15.98
  figures. One search did not confirm it (ITU history collection, `https://search.itu.int/history/`, not
  read). Telegram 1 carries no such stamp.
* "Mcl." in the London stamp: meaning not checked.
* "Eastern" = the Eastern Telegraph Company (Cable & Wireless group by 1937): inferred, not checked.
* The pencilled fee sums on the back of telegram 1: partly illegible; readings marked (?) above.

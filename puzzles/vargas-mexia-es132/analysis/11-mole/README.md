# 11-mole: whose desk did Saint-Goard's Spanish state papers come from? (H22)

Run 2026-11-10. Brief: `../../PROMPT-mole.md`.

## Question and bar

BnF fr. 16106 ff. 210–380 holds copies of Spanish state papers on the Portuguese succession, which Saint-Goard says he
"recovered" (12 Nov 1579, f. 359r). **H22:** they came from one desk in the secretariat of State with standing access
to the King's returned papers, and that desk was not Pérez's.

The bar was fixed before looking. Name a desk only if the papers show it, through addressees, countersignatures,
secretariat dorses ("Recibida…", "Respondida…") and which secretary handled Portugal. Name a person only if a
document names them. "Cannot tell" is an acceptable result.

## Method

- `build.py` (standard library) reads the three spread indexes in `../10-saint-goard/` and splits the views into 59
  documents. The segmentation is transcribed from the index rows and kept in the script's `DOCS` table. The script
  checks that every cited view exists, copies the dorse wording from the index (or from an image reading, see below),
  parses received and answered dates, and does all the counting. Output: `papers.tsv`, and `counts.txt` (stdout).
- `crop_dorses.py` enlarges the half-spreads 2x into `sources/cache/fr16106/crops/mole-vNNN-S.jpg`.
- Eleven images were read: v241 (whole spread), and the crops of 235L, 246R, 271L, 285L, 369L, 381L, 384L, 219R and 239R.
- `state_paper = N` marks six items that are not government papers: the Marquês de Vila Real's letter to Henri III,
  pamphlets, a speech, the Lisbon newsletter and a partisan memorial. Excluded entirely: Saint-Goard's own letters,
  Pierre Dor's letters, the French decipherments (vv. 216–217), the printed Latin index (vv. 334–337) and a later
  genealogy (v. 340).

## Image readings (2026-11-10)

| view | reading |
|---|---|
| 235L | Dorse: "Lisboa. A Su Mag.d. R° Vasquez y Molina a viij de agosto. Recebida en xvj [or xv] del mismo. **Sacada en relacion**" ("Lisbon. To His Majesty. Rodrigo Vázquez and Molina, 8 August. Received the 16th [or 15th] of the same month. Abstracted into a report") |
| 241 | Dorse: "Descifrada. Paris. Juan de Vargas Mexia a xxiiij de Agosto 1579. Reci.da en iiij de sept.e" ("Deciphered. Paris. Juan de Vargas Mexía, 24 August 1579. Received 4 September"). In the King's letter to Moura of 26 Aug on the facing page: "como os lo ha avisado **Cayas**" ("as Zayas has informed you") |
| 246R | King to Vázquez and Molina: "de Sant Loren[ço] a 26 de Agosto 1579. Yo el Rey", countersigned "**Cayas**" ("San Lorenzo, 26 August 1579. I the King", countersigned "Zayas") |
| 285L | Dorse: "Lisboa. A Su Mag.d **en su mano**. Del doctor Luys de Molina a 18 de 7bre" ("Lisbon. To His Majesty, into his own hand. From Doctor Luis de Molina, 18 September"), with a secretariat abstract. No received date seen |
| 369L | Dorse: "Lisboa. A Su Mag.d. R° Vazquez y Molina de 25 de octubre 1579. Rda a 28 del mismo" ("Lisbon. To His Majesty. Rodrigo Vázquez and Molina, 25 October 1579. Received the 28th of the same month"), plus an abstract |
| 381L | The copy of Moura's letter of 29 Dec 1578 carries marginal notes headed "De mano del Rey" and "De mano de Su Md." ("In the King's hand", "In His Majesty's hand"). One reads "puede se advertir a Don Xpoval" ("Don Cristóbal may be told"); another ends "avise se me lo que paresciera" ("let me be told what is thought"). These are the King's notes, rendered by a clerk for whoever drafts the reply |
| 384L | No legible dorse for that letter |
| 271L | Upside down: "Al muy mag.co señor … [name not read] … **Paris**" ("To the very magnificent lord … Paris"), with a seal trace. This is the address leaf of the Lisbon newsletter of 28 Aug |

## Results (from `counts.txt`)

1. **Addressees.** Of the 53 state papers: 24 are addressed to the King, 6 to Zayas, 16 to others (royal letters going
   out, petitions, enclosures) and 7 have no addressee (abstracts, memorials, acts). None is addressed to, endorsed by
   or countersigned by Pérez, and none names him.
2. **Zayas.** 8 of 53 (15%) are addressed to Zayas, countersigned by him or certified by him: six letters or capítulos
   (extracts) to him from Guardiola, Osuna, Moura and Vázquez; the royal letter of 26 Aug countersigned "Cayas"; and
   the Autos, which carry his certification of 8 Mar 1579. Counting the papers whose text names Zayas as the channel,
   the figure is 15 of 53 (28%). On the papers themselves, the Portugal business runs through Zayas. No other
   secretary is named in any of them.
3. **Papers that would not have passed through the same hands:**
   - Vargas's Paris dispatch of 24 Aug, deciphered in Madrid and received 4 Sep. This is French business; from 13 Sep
     Idiáquez countersigns the replies to Vargas (canon).
   - The Lisbon newsletter of 28 Aug, addressed to someone in Paris, so it never went through Madrid.
   - The Marquês de Vila Real's letter to Henri III.
   - Álava's parecer: the King himself asked how a Portugal advice paper reached Paris.
   - The public sentence against Dom Antonio (Dec 1579).
4. **Lag.** 17 papers have a parsed Madrid receipt or answer date. The latest receipt is Vázquez and Molina's letter
   of 25 Oct, received 28 Oct, and Saint-Goard sent the papers on 12 Nov, so the shortest gap from receipt to dispatch
   is **15 days**. Lisbon to Madrid took 3–8 days. The receipts of Sep–Oct cluster on the secretariat's batch days
   (27 Sep; 15, 18, 22, 25 and 28 Oct).
5. **Split at 28 July 1579.** Six dated papers fall before the arrest, 36 after, and 11 are undated.
   - Before: outgoing royal papers and lists, Álava's parecer, and Moura's letter of Dec 1578. None has a receipt dorse
     and none has a Zayas link, though the undated Autos carry Zayas's certification of March. The only royal
     holograph notes in the run are on the 1578 Moura letter.
   - After: incoming ministers' letters with receipt dorses and abstracts (16 of them), all six letters to Zayas, and
     every Zayas countersignature or named-handler mention.

   The kind of paper changes at the arrest. That fits a desk opening after July. It also fits a single late haul,
   since the volume's March–September dispatches are missing.
6. **Hands (weakest evidence).** The copy hands of v219 (Álava, May), v239 (Vargas, Aug) and v381 (Moura, Dec 1578)
   share the same chancery-italic letterforms (y, long s, q, "V. Md."). Verdict: **probably the same scribe; cannot
   confirm** at 1,800 px.

## Verdict on H22

The papers show the **Portugal desk of Gabriel de Zayas**. Three facts carry it:
- the King's letter of 26 Aug is countersigned "Cayas";
- the King writes to Moura that Zayas has kept him informed;
- six of the copies are letters or capítulos addressed to Zayas.

The received/abstract dorses show the copies were made from the secretariat's own filed papers, after receipt and
abstracting. The papers do not show **whose desk the copies left from**, and they name no copyist or informant. Three
papers came by other routes: Vargas, the Paris newsletter and probably Álava. So "one desk" is too strong. "Not
Pérez's" is consistent with the evidence but untested before July.

Proposed status for H22: **open → weakened (as stated) / partly supported**. Restate it as: "the Portugal papers came
from the Zayas-handled Portugal correspondence after receipt in Madrid; other items came by other routes."

## Limits

- The document segmentation is a transcription of the index, not a re-reading.
- Fourteen dorses were not quoted in the index or not read on the images.
- "xvj" versus "xv" at 235L is uncertain.
- The dates of eleven papers are only "1579".
- The hand comparison rests on three pages at low resolution.

## Rerun

```
python3 build.py > counts.txt
uv run --with pillow python3 crop_dorses.py   # crops only
```

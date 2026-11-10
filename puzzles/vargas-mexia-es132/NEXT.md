# NEXT — handoff for the next session

**Last session:** 2026-11-10, exp 10 (Saint-Goard's file, BnF fr. 16106). Before that 2026-10-16, essay update under
`PROMPT-essay-update.md`; the essay state below is unchanged.
**Where it stopped:** `essay/DRAFT.md` is revised and checked. Greg approved the plan, then asked to preserve the
actual research and diplomatic detail while making Pérez's French channel central. The new f. 41 scene does that;
Lalaing, fleets/Bordeaux/Ayala and Walloon terms remain in the narrative. A short Lansac thread supplies the concrete
subject of September's leak inquiry. No publication or push. The approved outline was removed from the draft and
every decision recorded in `essay/EDITOR-NOTES.md`.

## New on 2026-11-10 (exp 10) — read `analysis/10-saint-goard/README.md` first

- BnF fr. 16106 is reachable: Gallica serves the Playwright browser, not scripts. Views 196–391 are cached.
- Found and partly read: **Saint-Goard to Henri III, 23 Dec 1579** (ff. 363r–366r), cipher with no decipherment. It
  forwards letters of **Dom António de Castro, lord of Cascais**, calls Cascais the key to Lisbon, and asks for
  orders on him and on the infante Dom António (H20, supported by one letter). Working text:
  `analysis/10-saint-goard/reading-1579-12-23.md`.
- Found, not read through: a copy of **Vargas's own dispatch of 24 Aug 1579** (ff. 231–232v) inside a dossier of
  Spanish state papers of 1579 (H18 note).
- `unbleed.py` removes show-through. It is ready to try on es. 132 f. 213.

Done the same day: es. 336 read (H20 restated: Castro offered himself, the Cascais gloss is Saint-Goard's); the
12 Nov 1579 clear letter says Saint-Goard "recovered" and sent the Spanish papers; H21 opened (Álava's advice of
28 May 1579 as the paper Philip disowns on 29 Nov); no French reply in the printed letters; Castro went over to
Philip and was at Alba's landing at Cascais in July 1580 (weak source for the last point).

Also done: Dor's letter of 10 Feb 1580 (Castro "est espaignol"); the King's minute of 4 Apr 1580 (30% read);
H22 (`analysis/11-mole/`: the Portugal papers trace to Zayas's correspondence, no person named).

**Late correction:** the 23 Dec letter's court decipherment is at fr. 16106 ff. 208r–209v under the wrong date
"23 avril 1579". Read `sources/fr16106-ff208-209-decipherment.md` before anything else in exp 10.

Next, in order:
0. Tell Tomokiyo (follow-up drafted in `sources/outreach-tomokiyo-draft.md`); score reader C against the
   decipherment in code (`analysis/10-saint-goard/`), which turns exp 10 into a calibrated test of the readers and of
   `unbleed.py`; resolve the "Prieur" / Francisco de Ibarra passage on f. 209v with a closer reading.
1. **Outside confirmation (Greg sends).** `sources/outreach-tomokiyo-draft.md` is drafted. Check the signature, drop
   or fill [LINK], attach the working text and two strips.
2. **H21:** transcribe fr. 16106 ff. 210–215 (Álava) and compare with Paz's K 1554–55 description and our 29 Nov decode.
3. **Reply:** fr. 16107 ff. 201v–202r (rest of the 4 Apr minute, view 207, not fetched at full size) and the 16 Mar,
   27 Mar and 15 Apr minutes; the last margin lines of f. 63v (which King Dom António means).
4. Finish the letter (ff. 364v–365v, 363v ll. 8–16); read es. 336 f. 78 (copy for the King).
5. Castro: a sourced account of July 1580 (Velloso's Interregno; Valladares 2008); Castries II pp. 69–78.
6. Sweep pilot (Greg's call): classify cipher pages with and without decipherment across fr. 16104–16110.
7. Essay: decide whether this is a coda or a separate piece.

## Named wall added 2026-11-10
Saint-Goard's dispatches of Jan–Oct 1579 are missing from fr. 16106 and were already missing in 1877. They would
hold his report of Pérez's arrest and, if anywhere, the name of his source. Breach: the Dubrovsky collection
(National Library of Russia), the Institut's Godefroy papers, fr. 17019 ff. 176–197 (old item list), or a copy
series (Brienne). Cheaper first: his letters to Villeroy and the decipherments of Jan–Mar 1580 in fr. 16107.

## Do first

1. **Greg reviews the full draft.** Apply his notes; keep `essay/CLAIMS.md` and `essay/QUOTES.md` current. Do not ask
   for outline approval again. The narrative is 4,462 whitespace words; specialist section 1,478; notes 1,289.
   Verification: 378 exact claim mappings and matching hash, 32 ordered notes, 47 quote entries, all 81 earlier
   narrative quoted spans retained. Editor and Deslopify checks recorded in `EDITOR-NOTES.md`.
2. **After full-draft review**, follow `PROMPT-essay.md` for the page/document choice and publication. No essay page
   has been built. The existing OVERVIEW v7 remains at https://claude.ai/artifact/BSsgyjHHehAd9nA3zLWBi2.

## Evidence boundaries to retain

- Exp 09 contains **twelve distinct letters**, thirteen encipherments including f. 171, and fourteen sectional A/B
  comparisons (f. 185 has three sections). The earlier fourteen-letter summary was wrong. Rerun
  `python3 analysis/09-unread-letters/audit_inventory.py`; checked output is `inventory-audit.md`.
- No earlier decipherment was found in the searched publications/repositories. Do not turn that into universal
  priority or a claim that the historical episodes themselves were unknown.
- Two readers per main encipherment; agreement 80–97% **except f. 181, 85% / 66%**. The extra f. 171 copy is shorter
  and assessed separately. Model agreement is not historical accuracy. The Borja calibration gives 86% precision,
  63–64% recall on one letter (exp 08), with a model-produced margin transcription.
- F. 41 shows Philip using Pérez for the French ambassador's proposal. The ambassador says he acted without orders
  or commission; Henri III's authorization is not established. Saint-Goard is identified by date, not decoded name.
- F. 34 provenance resolved: both local exp 06 decodes contain the damaged discourse passage. The essay's exact
  quotation and “l[e]” remain cabinet-noir's. The supplied Chinchón and [dudas] also retain their credits.
- September names Lansac's talks and considers his own disclosure, but establishes no culprit. Longlée remains a
  candidate for a preceding name. No letter connects Pérez to the leak. Ribera/Le Roux are known through a secondary
  account, not inspected books. Context checks: `sources/essay-context-2026-10-16.md`.
- The Theatine remains unidentified. Do not extend seventeenth-century Jesuit usage to the 1570s without evidence.
- Earlier comparison figures are character matches, not word recall or an accuracy rate. Retain the poorer Teulet
  duplicate (70–72%) and distinguish each project's selected-passage scores.

## Research state and optional queue

H17 remains judged: every dated royal letter to Vargas of 24 Aug 1579 – May 1580 is read (f. 218 in clear, others by
two witnesses). No Pérez/Éboli/Escobedo or Pérez papers found, subject to disputed/unread spans. Pérez countersigns
through 13 July, no secretary on 24 August, Idiáquez from 13 September. F. 273 now has two witnesses (81% / 91%):
it is a separate Savoy memorial, not another royal letter. The 28 March 1580 letter has a Teulet minute check.

If research resumes after the essay review:

- H18: compare Saint-Goard's March–September 1579 dispatches (BnF fr. 16106) with the Lansac inquiry and candidate
  Longlée. For H19, his April dispatch is the direct outside check on the Pérez exchange.
- Vargas's side: AGS Estado K 1543–1558. Paz summaries of K 1554–55, 1557, 1558 corroborate business but contain no
  Pérez reference (`sources/paz-1579-1580.md`). Request the Portugal Council of War paper and September dispatch
  about Saint-Goard's information; do not identify the leaked paper from a catalogue title alone.
- H6: test Trigosso and padre Hernández against the ff. 123/154/157 contexts. Neither identification is established.
- Remaining unread: ff. 39, 50, 79, 129 (duplicate of 132), 150; f. 169 (clear decipherment of 22 Jan 1579), f. 177.
  F. 213 is parked at the show-through wall; possible next test is mirrored facing-page subtraction.
- Paz checks for ff. 54, 62, 85, 89, 119, 132 (K 1546–1551) remain. Cloulas p. 451 provides context for f. 85, not
  an independent reading of the secret instruction; later pages were not inspected.
- Older queue: date Mignet's B.44 n° 89; human paleographer for f. 12v and v2 texts; second local reader for f. 154.
  June–July baseline ff. 206, 208, 211 have one reader each. F. 206 names Pérez as receiver of Vargas's dispatches.

## Open questions and walls

Who is the partly read name in September, and what is the candidate “Consejo” noun? Whose Portugal opinion reached
Paris in November? F. 253's date remains xvj versus xxvj January 1580. The earlier questions about f. 34's date,
missing ff. 26v–31r, Cipher 2's long swash, Arcauti, `21. = que` and `ra = oficio` remain in the research record.

The King's side is read within the stated windows; Vargas's originals are not. A short reference can remain inside
a disputed passage. No human paleographer has checked these model transcriptions. Breach: dispatch images and a
paleographer, not more confidence from model agreement. Gallica blocks scripted requests (HTTP 403); Greg supplied
browser screenshots in `sources/cache/gallica-manual/`. Survey leads remain in the BnF and Italy survey notes.

## Operational lessons

Readers need the explicit second-pass instruction. Download whole spreads once, serially, and crop locally.
The earlier large reader batches hit the session limit; do not repeat that fan-out without a bounded question.

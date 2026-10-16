# NEXT — handoff for the next session

## 2026-10-16 session (untouched-data follow-up → exp 08, exp 09)
**What happened:** BnF and Italian surveys (`sources/bnf-survey-2026-10-15.md`, `sources/italy-survey-2026-10-15.md`).
Gallica refuses scripted requests (HTTP 403); Greg supplies browser screenshots (`sources/cache/gallica-manual/`).
- **Exp 08** (Borja crib, BnF fr. 15561 f. 42): Cipher 3 pipeline precision 86%, recall ~63% against a 1579
  decipherment; 108⁺ = Su Magestad confirmed (H12); letter-form h added to guide v2.3.
- **Exp 09: first readings of 14 royal cipher letters nobody had read** (two blind readers each, 80–97% agreement;
  `analysis/09-unread-letters/reading_f*.md`): ff. 37 (15 Apr 1578), **41 (Apr 1578: French league proposal routed through
  Antonio Pérez, four weeks after the murder; matches Paz K 1546)**, 54 (7 Jun), 62 (14 Jun: Saint-Goard's audience), 85
  (10 Sep: Lalaing via Nazareth), 89 (19 Sep: Maintenon's audience), 119 (15 Oct), 132 (1 Nov: padre Hernández, Guise,
  Sotomayor), 171/174 (23 Jan 1579), 181 (7 Feb: Walloon terms), 185 (18 Mar: **Lansac plática run by the King**,
  Portuguese pilgrim, Don António, Duburg), 202 (17 May: Franciscan chapter).
- `marknorm.py`: per-reader vowel-mark normaliser, controls pass.
- f. 213 parked: show-through wall (four partial readers).

## Do first (new)
1. **Fold exp 09 into canon/hypotheses.** f. 41 bears on the Pérez–Philip relationship after the murder (essay?);
   f. 185 ¶2 + f. 222 + cabinet-noir "Lan-gl-e" → the 13 Sep 1579 leak concerns the Lansac plática, informant Longlée
   (Saint-Goard's secretary) — test against Saint-Goard's dispatches in BnF fr. 16106.
2. **H6 "teatino":** candidates Trigosso (Mignet app., Don John's letter 1577) and the Jesuit padre Hernández (ff. 132,
   174, 185: Guise go-between in Paris). Search ff. 123/154/157 contexts for "Hernández".
3. Remaining unread: ff. 39, 50, 79, 129 (dup of 132), 150; f. 169 (clear decipherment of 22 Jan 1579 letter) and f. 177.
4. Show-through subtraction for f. 213 (mirror the facing page and subtract).
5. Paz cross-checks for ff. 54, 62, 85, 89, 119, 132 (K 1546–1551) not yet done.

---

**Last session:** 2026-10-09 (line edit of the uncommitted essay additions)
**Where it stopped:** Greg requested direct edits using Deslopify and the writing repository's editor prompt.
`essay/DRAFT.md` retains the new Verdinegro note, f. 34 quotation, f. 123 concession, office committee, Los Vélez and
Pazos passages. Removed narrative cues, clarified the return to Pérez's complaint and recast the proposed April
reconciliation. Quotations, numbers, URLs and note text match the input. `CLAIMS.md`: 311 checked mappings;
`QUOTES.md`: 41 entries; 26 ordered notes. Editorial record in `essay/EDITOR-NOTES.md`. Changes remain uncommitted.
Publication pending review. **New flag:** the draft calls f. 34 unread here, but experiment 06 contains two local
decodes. Reconcile that provenance before publication; no attribution was silently changed in the style pass.

**Research state:** H17 judged. Every dated royal letter to Vargas of 24 Aug 1579 – May 1580 is read: f. 218 in clear on
the image; ff. 220/224, 222/226, 228/231, 235/237, 239/241, 245/247, 255/261, 257/263 (duplicate pairs) and ff. 251,
253, 267, 269, 271 (two blind readers each). **H17a not supported**: no letter names Pérez, Éboli or Escobedo or mentions
Pérez's papers. **H17b supported, qualified**: Pérez vanishes, but the channel changes and the King twice hunts a leak
without naming anyone (13 Sep: Saint-Goard's source for "las cosas de acá"; 29 Nov: a Portugal advice paper that reached
Paris). **H17c supported**: Pérez countersigns to 13 Jul 1579, none on 24 Aug, Idiáquez from 13 Sep. The 28 Mar 1580 decode
matches the Simancas minute in Teulet (77–82%). OVERVIEW has a new scene "After the arrest" and §7.4.

## Do first
- **Resolve the f. 34 provenance conflict** recorded in `essay/EDITOR-NOTES.md`: compare the quotation against
  `analysis/06-premurder/f34_A_decoded.txt` and `f34_B_decoded.txt`, then align note 4, claim key AD and Q37.
- **Greg reviews the reordered `essay/DRAFT.md`.** Apply further notes; keep `essay/CLAIMS.md` and `essay/QUOTES.md` current.
  His requests for fuller storytelling, context first, quotation provenance and more consequential cipher text have been applied.
  Then follow `PROMPT-essay.md`: ask once whether he wants a page (default, alongside OVERVIEW) or a document for comments;
  publish only after full-draft review. The outline is approved; do not ask for that approval again.
- The requested Artifact `quickstart` tool was not exposed in this Codex session; publication tooling is for the next
  checkpoint. No page was built or external publication attempted. The source text is ready for review as Markdown.
- **Drafting source cautions:** use the scripts' character-matching definition for comparison scores, not the README
  shorthand “word recall”; include the weaker Teulet duplicate (70–72%). Report each third-party comparison separately
  rather than reuse the brief's combined 76–95% as an accuracy rate. The outline records the exact source tables.
0. OVERVIEW republished 2026-10-05 (v7, https://claude.ai/artifact/BSsgyjHHehAd9nA3zLWBi2).
1. **f. 273** done: two witnesses (81%/91%); a Savoy memorial copy, content c. 1573 per pangoleen; not a royal letter.
2. **The 13 Sep leak noun**: candidate "Consejo" (f. 222r spells "con-se-je-s…" where f. 226r has the "he" sign; see exp 07
   log). Test it on another occurrence of the "he" sign or a Simancas minute.
3. **Vargas's side**: Paz's summaries (K 1554–55, 1557, 1558) read: no Pérez; many decodes corroborated
   (`sources/paz-1579-1580.md`). Item-level: request the leaked "Relación del Consejo de guerra … Portugal" (K 1554–55) and
   Vargas's Sept 1579 dispatch on Saint-Goard's source, via PARES (browser) or Simancas.
4. Baseline Jun–Jul 1579: ff. 206, 208, 211 read by one reader each (f. 206 names Pérez in cipher as receiver of Vargas's
   despatches); f. 213 unread. Low priority.
5. Older queue: date Mignet's B.44 n° 89; human paleographer for f. 12v and the v2 texts; f. 154 second reader.

## Open questions
- Who or what is "lo del [?]" in the 13 Sep leak passage, and did Vargas name the informant in his reply?
- Whose private opinion on Portugal reached Paris (29 Nov 1579)?
- f. 253's date: xvj (reader A, Tomokiyo) or xxvj (reader B) de enero 1580.
- Earlier open points (B.44 n° 89; ff. 26v–31r unscanned; f. 34's date; Cipher 2 long swash = ll; Arcauti; 21. = que;
  "ra" = oficio) stand.

## Named wall
For H17: the King's side is read; Vargas's dispatches (AGS Estado K 1553–1555) are not, and a short reference inside the
10–38% of each decoded text where witnesses differ cannot be excluded. For all readings: Sonnet transcriptions, no human
paleographer. Breach: PARES images and a paleographer.

## Operational lessons
- Readers need the effort block (reader-prompt v1.1): without it they stop after ~3 minutes with no second pass.
- Fetch whole spreads once, serially (~90 s per canvas); readers crop locally. 92 canvases took about 2 hours.
- Sonnet readers cost ~150–400k tokens each; 40+ readers in one session hit the session limit.

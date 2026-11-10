# PROMPT — who was copying Philip's papers for the French ambassador? (H22)

Written 2026-11-10 for one bounded agent. Read `CLAUDE.md` rules 1–6 first. Do not spawn agents. No browser, no web.
**Hard budget: 35 tool calls, final report under 350 words.** Stop when the budget is spent and say what is left.

## The question

BnF Français 16106 is the file of Saint-Goard, French ambassador in Madrid. From f. 210 it holds copies of Spanish
state papers on the Portuguese succession: ministers' letters to Philip II and to his secretary Zayas, Philip's
replies, council papers. Saint-Goard's own letter of 12 Nov 1579 (f. 359r) says he "recovered" the papers and sent
them home by express. On 13 Sep 1579 Philip asked his ambassador in Paris where Saint-Goard got his knowledge of
Madrid business (es. 132). Nobody we have found has asked who the source was.

The run of copies spans the arrest of the secretary Antonio Pérez (28 July 1579): the earliest is Moura to Philip,
29 Dec 1578, copied with the King's holograph replies ("De mano del Rey"); the latest is 25 Oct 1579.

**H22.** The copies came from one desk in the secretariat of State with standing access to the King's returned
papers, and that desk was not Pérez's.

## What a result would have to do (the bar, fixed before you look)

Name a desk only if the papers themselves show it: addressees, countersignatures, dorses in a secretary's hand
("Recibida…", "Respondida…"), and which secretary handled Portugal. Name a person only if a document does. "Cannot
tell from this evidence" is a full result. Do not reason from who seems likely.

## Material you already have (use it before reading any image)

- `analysis/10-saint-goard/index-196-260.tsv`, `index-261-325.tsv`, `index-326-391.tsv`: one row per spread, with
  writer, addressee, date as written, and notes on dorses.
- `sources/alava-advice-1579-05-28.md`, `sources/saint-goard-prior-publication-2026-11-10.md`,
  `sources/castro-cascais-context.md`, `canon.md` (search for Zayas, Idiáquez, Pérez, Moura; do not read end to end).
- Images, 1,800 px spreads: `sources/cache/fr16106/vNNN.jpg` (NNN = view). Crop and enlarge with
  `uv run --with pillow python3 …` when a dorse or heading must be read. Read at most 12 images.

## Steps

1. **Table.** From the index files build `analysis/11-mole/papers.tsv`, one row per copied Spanish or Portuguese
   state paper (not Saint-Goard's or Pierre Dor's own letters, not printed pieces): view, folio, date written, place,
   writer, addressee, whether a received/answered dorse is noted, whether the King's holograph notes are copied,
   language. A script (`analysis/11-mole/build.py`) builds it; no hand counts.
2. **Which desk.** Count by addressee (the King, Zayas, others) and by writer. Report the share addressed to or
   endorsed by Zayas. Note any paper that would not have passed through the same hands (for example a letter
   addressed to another secretary, a council consulta, a paper from Paris such as Vargas's dispatch of 24 Aug 1579
   at ff. 231–232v, or Álava's advice at f. 210).
3. **Lag.** Where a "Recibida" date is recorded or legible, list written date, received date and the next French
   dispatch date (known: 12 Nov 1579 and 23 Dec 1579; the dispatches of Mar–Sep 1579 are missing from the volume).
   Read the dorses on the images for the six or eight papers where it matters most: views 241 (Vargas), 384–385
   (Moura, Dec 1578), 368–369 (Vázquez and Molina, 25 Oct), and others the index flags.
4. **Before and after 28 July 1579.** Split the table at Pérez's arrest. Does the kind of paper, the addressee or the
   presence of royal marginalia change?
5. **Hands.** Only if budget remains: compare the copy hand of three papers far apart in date (for example views
   219, 239, 381). Say "same", "different" or "cannot tell", with what you compared. This is the weakest evidence;
   mark it so.

## Output

- `analysis/11-mole/README.md` (question, bar, method, results, limits, how to rerun), `build.py`, `papers.tsv`.
- Do not edit `hypotheses.md`, `canon.md`, `research.md` or `NEXT.md`; propose changes in your report.
- Report: the desk, if the evidence names one, with the three facts that carry it; what the split at 28 July shows;
  the shortest lag found; and the one document that would name a person.

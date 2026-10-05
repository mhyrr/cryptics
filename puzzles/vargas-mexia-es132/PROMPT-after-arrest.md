# Session prompt: what the King told Pérez's friend after the arrest (H17)

Paste everything below the line into a fresh session.

---

/focus vargas-mexia-es132

Goal: read the King's cipher letters to Vargas Mexía from April 1579 to May 1580, and find out whether, around and after
Antonio Pérez's arrest (night of 28 July 1579), the King tells Vargas anything about Pérez, Éboli, the Escobedo
affair, or the private correspondence Pérez ran with Vargas. Vargas was Pérez's friend and correspondent. In 1580 he cut
Pérez from his will (Rubino 2012). These letters are the King's side of that friendship's end.

## Read first, in order
1. `NEXT.md`, `README.md`, `canon.md`, `hypotheses.md`; search `research.md` for "session 4" (experiment 06).
2. `OVERVIEW.md` "The story" and §7; `analysis/06-premurder/README.md` (method and the Gallica lesson).
3. `sources/transcription/CIPHER3-GUIDE.md` (v2.1) and `analysis/04-cipher3/` (decoder v2, `c3_extensions.tsv`,
   concordance); `analysis/06-premurder/thirdparty-compare.md` (Cp.30 code checks, 35 = pr / underlined 35 = pl).
4. Third-party readings: cabinet-noir has read ff. 200, 211, 215, 220–221, 222, 228–229, 233, 245 and 255 (cached list in
   `sources/cache/thirdparty/cn_es132_README.md`; letters not yet fetched). **Do not open their readings until our
   decodes of the same letters are frozen.**

## Where things stand (do not re-derive)
- Cipher 3 (Cp.30) reads under guide v2.1 and decoder v2: ff. 103/113, 105, 165/167 read; codes u. = que, 108⁺ = Su
  Magestad, 149⁺ = V.m., T⁺/1⁺ = particular(es). Cabinet-noir's `cle/cp30_complements.tsv` (CLAIMANT, citing Alcocer 1921)
  lists further code values. Treat them as candidates, never as frozen values, until one of our duplicates confirms them.
- Pérez countersigned the King's letters to Vargas up to the spring of 1579 (ff. 6, 11–12, 17–25, 34, 123, 154). Who signs after
  July 1579 is not yet recorded.
- The canvas map is c = f − 3 from f. 32 to at least f. 250 (`canon.md`). Check it on the thumbnails for ff. 250–290.

## The letters (Tomokiyo's table of contents, `sources/cache/cryptiana/spanish3D.htm`; Cipher 3 unless stated)
| Folio | Date | Note |
|---|---|---|
| 200, 202 | 21 Apr, 17 May 1579 | before the arrest; 200 read by cabinet-noir |
| 206, 208, 211, 213, 215 | 8 Jun, 4 Jun, 3 Jul, 7 Jul, 13 Jul 1579 | the last letters before the arrest; 211, 215 read by cabinet-noir |
| 217 | 22 Aug 1579 | to M. de Lansac (clear?) |
| 218 | 24 Aug 1579 | **first letter after the arrest** |
| 220 + dup 224; 222 + dup 226 | 13 Sep 1579 | duplicate pairs |
| 228 + dup 231 | 13 Oct 1579 | duplicate pair |
| 235 + dup 237; 239 + dup 241 | 3 Nov, 13 Nov 1579 | duplicate pairs |
| 245 + dup 247 | 29 Nov 1579 | duplicate pair |
| 251, 253, 255, 257, 261, 263, 267, 269, 271 | 16 Jan, 28 Mar, 16 May 1580 | 261 = dup of 255; 257 = dup of 263 |
| 273 (Cipher 2), 275 | undated | 273 read by pangoleen (Savoy memorial) |
| 279 | Aug 1579 | "Relacion del movimiento de Franceses … Fuenterravia" (clear) |
Non-royal letters in the run (Parma f. 233, Mansfeld f. 243, Acuña f. 249) are context, read last.

## H17, pre-registered (write into `hypotheses.md` before any reading)
- **H17a**: a royal letter to Vargas dated after 28 Jul 1579 refers to Pérez (by name, office or code), to his arrest,
  to the Princess of Éboli, to the Escobedo matter, or to Pérez's letters or papers held by Vargas.
- **H17b**: none does. The King writes as if nothing had happened, and Pérez simply vanishes from the correspondence.
- **H17c (observable in clear)**: the countersigning secretary changes after the arrest. Record each letter's
  countersignature from the image.
- **Test.** Every royal letter of 24 Aug 1579 – May 1580 is read in full by two blind readers. A duplicate counts as the
  second witness. H17a is supported by one clear passage, quoted with token positions and read by both witnesses. H17b is
  supported when all letters are read and none has such a passage. Letters not read are listed as the wall. The pre-arrest
  letters of Jun–Jul 1579 are read too, as the baseline for "as if nothing had happened".
- What counts: a reference to the persons or matters above, or an order about letters, papers or ciphers that Vargas
  exchanged with Pérez. A change of cipher key or of secretary alone does not count for H17a; record it under H17c.

## Work, in order
1. **Experiment folder** `analysis/07-after-arrest/` with a README pre-registering H17 and the steps. Commit first.
2. **Images, throttled.** Extend `sources/cache/pages/fetch_pages.py` with every page of the letters above (both sides of
   each leaf; confirm folio numbers and the canvas map on the images). One request per page, 20 s apart, after a probe.
   **No reader ever contacts Gallica.** Readers crop locally (guide §0 of CIPHER2-GUIDE.md shows how; give Cipher 3 readers
   the same instruction in their prompt).
3. **Guide check.** Add one line to CIPHER3-GUIDE (v2.2) asking readers to record an underline below a sign as `<under>`
   (cabinet-noir's 35 = pr vs 35̲ = pl; also 30̲–34̲ clusters). Teach the decoder `<under>` on 30–35 only. Freeze both
   before any reader starts.
4. **Readers.** Use Sonnet 5.5, no sub-agents, and at most 6 running at once. For each duplicate pair, one reader per copy;
   the two copies check each other. For each single letter, two readers, one working in reverse page order. Freeze each
   transcription by commit before decoding. Start with f. 218 (first after the arrest) and the 13 Sep pairs.
5. **Decode** with `analysis/04-cipher3/decode_c3_v2.py` (plus the v2.2 underline rule). Align duplicates with
   `../05-cipher4-v2/align.py`. New code values: derive them only from duplicate alignment (a code in one copy, spelled out in
   the other), freeze them, then test them on later letters (held-out, ≥ 80% fit).
6. **Countersignatures** (H17c): a table of the signature on every letter from f. 154 to f. 275, read on the images.
7. **Third-party comparison** after our decodes are frozen: fetch cabinet-noir's readings for the overlapping folios and
   score them with `analysis/06-premurder/thirdparty_compare.py` (add the pairs). Record disagreements.
8. **Synthesis on the main thread**: judge H17; if anything bears on Pérez's fall, add a scene to OVERVIEW "The story"
   and to §7, then rebuild and republish to https://claude.ai/artifact/BSsgyjHHehAd9nA3zLWBi2 (read it first if the session
   has not).

## Honest scope
These are the King's letters only. Vargas's replies are in Simancas (Estado K 1554–55 for 1579; PARES). Silence in the
King's letters (H17b) would be a finding about what the King chose to write to Pérez's friend, not proof that Vargas knew
nothing. The private Pérez–Vargas correspondence after the arrest, if any, is not in this volume.

## Rules
AGENTS.md throughout. Freeze before testing. Commit transcriptions before decoding. Statistics come from scripts. File
findings as they happen. Stop at a clean wall and name it. Before calling anything new, search GitHub and the web for the
folio and the shelfmark. Run `/session-close` at the end.

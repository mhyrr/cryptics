# NEXT — handoff for the next session

**Last session:** 2026-10-05 (session 5, experiment 07)
**Where it stopped:** H17 judged. Every dated royal letter to Vargas of 24 Aug 1579 – May 1580 is read: f. 218 in clear on
the image; ff. 220/224, 222/226, 228/231, 235/237, 239/241, 245/247, 255/261, 257/263 (duplicate pairs) and ff. 251,
253, 267, 269, 271 (two blind readers each). **H17a not supported**: no letter names Pérez, Éboli or Escobedo or mentions
Pérez's papers. **H17b supported, qualified**: Pérez vanishes, but the channel changes and the King twice hunts a leak
without naming anyone (13 Sep: Saint-Goard's source for "las cosas de acá"; 29 Nov: a Portugal advice paper that reached
Paris). **H17c supported**: Pérez countersigns to 13 Jul 1579, none on 24 Aug, Idiáquez from 13 Sep. The 28 Mar 1580 decode
matches the Simancas minute in Teulet (77–82%). OVERVIEW has a new scene "After the arrest" and §7.4.

## Do first
0. OVERVIEW republished 2026-10-05 (v7, https://claude.ai/artifact/BSsgyjHHehAd9nA3zLWBi2).
1. **f. 273** is a copy of a Savoy memorial (Italian, Cipher 2) sent to Vargas, not a royal letter. Reader A done (single
   pass); reader B stalled and wrote nothing, so a second reader is still needed; then open `sources/cache/thirdparty/pg_reading_f273_274_savoy_memorial.md`.
2. **The 13 Sep leak noun** (ff. 222r/226r, the "h-like" letter-form sign after "lo del"): look for the same sign elsewhere
   in Cp.30 letters; check cabinet-noir's `cle/cp30_complements.tsv` for a letter-form value; a human look at the image.
3. **Vargas's side**: AGS Estado K 1553–1555 (Aug 1579 – 1580) on PARES, for what he wrote about Pérez, Saint-Goard's
   source and the Portugal paper. Teulet vol. 5 prints Scotland excerpts only.
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

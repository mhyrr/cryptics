# f271-B blind transcription notes (BnF Esp. 132, ff. 271-272)

Reader: blind, guide CIPHER3-GUIDE.md v2.2 only. No network, no other files. Page images: exp07/f271r, f271v, f272r, f272v.

## Extent
- One letter. It **starts on f. 271r** (header "+ El Rey", salutation "Juan de Vargas Mexia", then 4 lines of clear Spanish, then cipher) and **ends on f. 271v** (last cipher line, a date line "de Merida a [blotted numeral] de mayo 1580", the King's signature "Yo el Rey", the secretary's countersignature).
- f. 271r: header, 4 clear lines (the clear paragraph ends "en esta 1."), 21 cipher lines (C1-C21). f. 271v: 26 lines (V1-V26; V26 is the last cipher fragment plus the date), then signature and countersignature.
- f. 272r: blank leaf. At its right edge a strip of the next leaf's line-ends (numerals such as 19, 14, 20, 17, 11) shows; not part of this letter, not transcribed.
- f. 272v: address leaf: "+ Por el Rey / A Juan de Vargas Mexia / en Paris" (large flourish between "el" and "Rey"; "en Paris" underlined), and a docket in a second hand along the right edge, read "16. de março de 1580." (year underlined). Note the docket month (março) differs from the letter's date line (mayo); the day on the date line is blotted, so I cannot compare days. The sliver of cipher at the right edge of 272v belongs to another leaf.
- Paragraph ends (a short last line ending `1.` or a dash+`1.`): 271r clear para (after "en esta"), C10 (short line ending `6.`), C17 (`24. 1.`), C21 (`... 12+ 1.`); 271v V4 (`22 <sign:dash> 1.`), V12 (`22. 1.`), V16 (`y<bar> 1.`), V20 (`/ 1.`). After the 271r last line (C21) the new paragraph on 271v starts at V1, indented (all of V1-V26 start about 800 px from the left edge, the left of the page is empty).

## Passes
- Pass 1 (guide §6.1): 271v first (reverse page order), then 271r, then 272r, 272v (the output file is in normal order). Each page cut into strips about 380 px high (3 lines) by about 1650 px wide (L and R, overlapping about 150 px; slightly wider than the 1500 requested, so the viewer shrank them by about 5%), native pixels, no upscaling.
  Strips viewed in pass 1: f. 271v 30 (14 L/R pairs, plus 2 signature crops); f. 271r 40 (24 text strips in the final cut, 8 earlier strips from a first cut with a narrower right margin, 8 header/clear-text crops); f. 272v 5; f. 272r 1. Total 76.
- Pass 2 (opposite direction: 271r from bottom to top first, then 271v from bottom to top; right half before left half, tokens right to left): 271r 26 strips (r13L, r12R, and 12 L/R pairs) plus 8 clear-text crops; 271v 26 strips (13 L/R pairs) plus 9 detail crops (date line, King's signature, countersignature, two checks of 2-vs-7 shapes). Total 69.
  Not re-viewed in pass 2: the "+ El Rey" header crop, f. 272r, f. 272v (read once only; one-line items). Pass 2 was completed for all cipher lines.
- What pass 2 changed (main points): C3/C4/C5 several numbers re-split (`21 4`, `24+`, `86` joined); V11 (`21 24 12+<bar>` instead of a run of digits); V19, V20, V21, V24 re-segmented; hats/bars re-assigned to the sign they stand over; `Jum` on C13 re-read as the letters `S u m` (line-initial flourish); the "bul" clear word seen twice (C18, V22); "a los quales" corrected from "a las quales"; "Se recibieron" capital S.

## Confidence, plainly
This is a hard hand. The count of `?` below understates my doubt. Systematic ambiguities that affect many tokens, and how I resolved them:
1. z-shaped 2 vs flat-barred 7. A glyph followed by a closed loop "o" I wrote `20` when it was clearly the curly z-shaped 2 and `76` when it had a flat bar. This is a judgement call in many places (C2 `76 76`, C19 `76 76`, V6, V13, V23).
2. A closed loop "o" after 1, 2 or 3: written as zero (`10`, `20`, `30`); after 4-9 written as the joined curl (`86`, `76`, `256`...). I could not always tell a 0 from a joined curl.
3. Hook `p` vs curl: a loop with a tail after a number is written `p` (`24p`, `15p`); where it looks closed and small it is a curl.
4. Letter S (long flat-topped) vs digit 5 or 8 at the start of a group (`S`, `5 9` in V14, `S 1`, `S 6`). Several `S` could be 8 or 5.
5. Bars, hats and acutes above signs are faint and sit between lines; I assigned each to the sign directly beneath it. A few may belong to the neighbour.
6. Sign boundaries inside pen-joined groups (for example `2 14+`, `21 4`, `11 14`) are my best split.
7. "q"-shaped sign (a 9-like form with a long tail): written `9.` where it stands alone (C5, V18).
8. Single-letter forms such as `p+`, `T`, `i`, `L`, `m`: read as letters; `y i m` (C21) could be `y 1 m`.

## Every 3+ digit run left joined (curl rule; each is a number plus a curl-shaped 6, or two numbers I could not split)
271r (C = cipher line, counting cipher lines only): C1 `296<bar>`; C2 `156<2dot>`, `256`; C5 `256`, `296<bar>`; C6 `256`; C8 `176`, `176<2dot>`; C14 `246`; C15 `256`, `226`; C16 `236`; C17 `246`; C18 `296`; C20 `236<hat>`.
271v: V1 `246` (twice), `226`; V3 `256`, `296<bar>`; V4 `126`, `296`; V7 `176`; V8 `356<under>`; V11 `156`; V15 `236`; V17 `256`, `176`; V19 `316`; V22 `226`, `256`; V24 `236`.
Unsure whether a curl is joined: C1 `86<bar>?`; C2 `156<2dot>`; C11/V12/V10 `76`; V13 `86 6`; V14 `5 9`; V15 `20<tilde>`; the `66` pairs (C3, C5, C9, V3, V8, V9, V13, V18, V19, C19, C20, C21) where two curls stand side by side and I wrote them as separate `6 6` or `66`.

## Every `?`
- C1 `86<bar>?` (curl joined? bar position).
- C6 `7p<under>?` (an underline under 7p; could be a flourish, or the number 37).
- V6 end `1?`, V7 end `2?`, V8 end `7?`, V9 end `0?`, V10 end `2?`, V18 end `1?`: signs cut by the dark gutter shadow at the right edge of 271v (about x = 3140); the last sign on those lines is partly lost.
- Clear text: salutation line `de las?` (the vowel looks like "o": "de los cartas"?), line 3 end `dos de?` ("ee"), line 4 `se respondera?` (the d of "respondera" is not visible: I read "se re-pon-era").

## Every `<sign:...>`
- C1 `12p<sign:2-shaped stroke above>` (a small 2-like stroke above the 12p).
- C5 end and V4 `<sign:dash>`: a short dash before the paragraph-ending `1.`.
- C10 `28<sign:small 2-shaped stroke above>` (the short line "29.<v> 7p<hat> 4<acute> 28<sign...> 6.").
- C15 `15<sign:arch above>` (a rounded arch, like an inverted v, above the 15).
- V6 `9<acute><sign:Z-shaped stroke above>`: a large bold Z stands between lines 5 and 6 above the first `9<acute>`; the two `9<acute>` signs (a 9 with a tick) begin the line.
- V8 `<sign:2-shaped stroke above an ink blot>` followed by `7?` at the edge.
- V13 `246<sign:tilde above>` and V15 `20<sign:tilde above>`: a ~ above (the guide has `<v>` for a small v; this is wavy).
- V26 `<sign:blotted overwritten numeral group...>`: the day of the month, a blotted group of strokes (x, v, j shapes), with a loop descending below the line; the letter writes "de Merida a [this] de mayo 1580". I read it as possibly a Roman numeral (xvj?) but this is only a shape guess.

## Every `<under>`
271r: C7 `34+<under>` (in "u. 18<bar> 6. 34+<under> 22. y<bar> m+ / ..."), C17 `34+<under>`; C6 `7p<under>?`. 271v: V1 `35+<under>`; V5 `30<under>.`; V8 `356<under>`; V25 `7p<hat><under>` (last cipher sign of the line before the date: the underline is bold).
All of these are short strokes under the number, clearly under, not the next line's ascender. I looked at every number in the 30s (30, 31, 33, 35, 36) and found underlines only on those listed (not on `31.`, `33`, `35.` elsewhere, nor on `36`/`36+`).

## Clear Spanish and signatures (diplomatic)
- 271r: `+ El Rey` (cross over the "l"), `Juan de Vargas Mexia / Demas de las? cartas Vras`, `a que se responde en las otras dos que van con esta`, `Se recibieron a 28 del passado vna de catorze y dos de?`, `20<bar> del mismo a los quales se respondera? en esta` followed by `1.`. The "28" in the third line has the shape of the cipher number 28 (not 18).
- Clear words inside the cipher (all in `[[ ]]`): V1 `mil`, V6 `de`, V10 `de`, V17 `quam`, V26 `quam`, V21 `hum` (could be "bum"/"hun"), V22 and C18 `bul` (could be cipher letters b-u-l). They are written in the same cursive as clear Spanish.
- Date line (end of V26): `de Merida a [blotted day] de mayo 1580`; final 0 touches the gutter shadow.
- King's signature, below the date line: `Yo el Rey`: a large "Yo" with a long tail, "el" and "Rey" with a flourish and a rubric of crossing loops.
- **Countersignature as I read it: "Don Juan de Idiaquez".** Shapes: "Don"; a tall looped initial stroke followed by a short compressed run (read "uan", but the letters are fused); "de"; a second tall looped initial stroke (the "I"), then "diaq" and a final flourish with a loop and a short baseline stroke (the "uez" abbreviation). The first name is the least certain part.

## Image problems
- 271v: right edge of the leaf is cut by the dark gutter shadow (about x = 3140); the last sign of many lines is partly lost (listed under `?`). The left ~700 px is empty (show-through, no text). Heavy mirror show-through from the verso (faint, no confusion with text except below V22). Ink blot at the end of V8 (a blot with a Z-shaped stroke above) and a blot in the date line.
- 271r: a black vertical bar at the far left (page edge) and an ink-ringed blot beside the 4th clear line. Faint show-through of the verso throughout. Right edge about x = 3300; text ends before it. Line-end numerals of the next leaf show in the right gutter (not transcribed).
- 272r: blank. 272v: the address block is large and rotated 90 degrees relative to the text on 271; the docket runs along the right edge.
- Strips were 1650 px wide (guide §8 asked for ~1500): the viewer reduced them by about 5%; no other resizing.

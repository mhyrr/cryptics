# f. 231-232 (13 Oct 1579), blind transcription notes (guide v2.2)

## Extent
- The letter begins at the top of **f. 231r** (heading "el Rey", salutation "v. Juan de Vargas. Mexia.", a 10-line clear
  paragraph, then 21 cipher lines) and runs on **f. 231v** (24 cipher lines, place and date line, "Yo el Rey", countersignature).
  It ends on f. 231v.
- f. 231r: clear opening (10 manuscript lines incl. the salutation line) + 21 cipher lines. The first cipher paragraph ends with a
  virgula at the end of line 13; the second begins line 14. Last line (21) is short and ends with a virgula, which closes the page.
- f. 231v: 24 cipher lines in six blocks of 3, 3, 3, 5, 5, 5 lines (blocks end in a virgula, or cut at the edge). The last cipher
  line (24) ends "... d. 24p 7p /" and the date line follows on the same manuscript line: "De S.t Lorenço a xiij de Otubre 1579 /".
  Below it, "Yo el Rey" (large, with rubric) and, lower right, the countersignature.
- f. 232r: blank leaf (page number "232" top right). Only show-through of the verso address and of the cipher of 231v. Nothing transcribed.
- f. 232v: address leaf, written turned 90 degrees (read after rotating the image 90 degrees counter-clockwise):
  "Por (+) el Rey" with a long rubric underneath; "A Juº de Vargas Mexia"; at the top right a three-line archival docket
  ("Sant Lorenzo / De su Mt. de 13 de octubre R.do / Paris a los 26 del Respondida"), plus a partial "1579" underlined
  at the very top edge. Transcribed in [[ ]] under its own header; not cipher.

## Signatures (as read)
- King: "Yo el Rey", large cursive with a heavy rubric: a looped Y, "o", then "el" and "Rey" run together, long descending stroke and figure-eight loop to the right.
- Countersignature, as read: **"Don Iuº de Idiaquez"** (written "Don Iu^o de Idiaq..."; the last letters "...q", then a long thick descender curving back
  and a loop, and a long oval rubric underneath). I read the "q" and the closing loop as "-quez", but the end is a flourish. Shape only for that end.
- Heading on f. 231r: "el Rey" with a small cross above the R and a very large flourish under the whole line, sweeping to the right.

## Method and passes (guide section 6, with deviations)
- Cropped with `magick` at native resolution into `/tmp/claude-501/t231/`. For the cipher I used strips of 3 manuscript lines in
  **three columns of 1000-1100 px** (not two halves of 1500 px) with ~100-300 px overlap at the column joins, because the signs are
  about 50 px high and a 1100 px strip read better. On 231v the lines rise to the right (about 70 px over the width), so strips are 400 px high.
- Clear text of f. 231r: 4 strips of 3 lines, each in a left and a right half (1600 px wide, 100 px overlap).
- **Pass 1 (forward, top to bottom, left to right):** f. 231r 8 clear strip-halves + 21 cipher column-strips = 29 views;
  f. 231v 9 strips x 3 columns = 27 views. Total 56 strip views. Extra single crops: header (1), a few one-line zooms at native scale (6),
  1600 px half-strips for cipher strips 1 and 4 of 231r (3), signature crops (2), f. 232v rotated crops (4) and overview crops of 232r/232v.
- **Pass 2 (reverse: bottom to top, right to left):** all 56 strip views repeated (f. 231v from the date line up, then f. 231r cipher
  from line 21 up, then the clear text from "continueis" up to the salutation). Corrections were made line by line. The signature crops,
  the 232r overview and the 232v address/docket crops were viewed **once only** (no second pass for those).
- Pass 2 changed, in particular: `ω`-like glyph recognised as "10" (the 1 and 0 ligatured) and rewritten everywhere; the many `H`-shaped glyphs
  read as `7+` (checked against the repeated opening "4^ 15p u. 24p 7+ 9" on l. 1 and l. 16 of 231r); several "u." versus "21." starting signs; `d+`
  versus `2+`; bars and hats added on 231r lines 6, 7, 14, 16; "11p" for "14p" on l. 2; extra small-"2" marks on 231v l. 9; `236<2dot>` on l. 3; `10`
  for `ω` in 231v. I have not been able to tell all of these apart with certainty, see the lists below.

## Conventions I had to add (outside the guide)
- `P` (capital) = a p-shaped sign standing alone (hooked loop with long descender, not a hook on a number); `P+`, `P<v>`, `P.<v>` carry the usual marks.
- `np` = letter n with a hook. `d` = the "∂"-shaped sign (a d form with a curl over). `dp` = `d` followed by the hook.
- Letter forms I wrote as letters: `S` (long flat-topped, also `S o m`, `S i m`, `S e m`), `B a m` (231v l. 21), `m u y` (231r l. 12 and l. 19), `L` (231r l. 19), `y`, `u`, `u.`.
  `S o m`, `S i m`, `S e m`, `B a m`, `m u y` look like Roman-letter syllables written in the cipher; "muy" may be clear Spanish, I could not tell. The middle letter of `Som`/`Sim`/`Sem` could also be a digit (0, 1) or the hook.
- A bare `4<bar>`: the 4 here is open-topped like a `q` with a descender; the bar sits over it.
- `<sign:small-2-above>`: a small digit-2-like mark written above a sign (231r l. 8 x4, l. 11 x6 plus one small 3-like; 231v l. 3, l. 9). Not in the guide. Positions are approximate; they sit over the sign named.
- `<sign:paren-stroke>` 231r l. 11: a "(" shaped stroke before the `d.`.
- `<sign:flourish>` 231v l. 17: closing flourish at the right end of the line. `<sign:cut>`: sign cut by the page edge.
- A thin long hairline "/" between `422.<hat>` and `36+` on 231v l. 9 was written as a virgula; it is lighter than the other virgulas.
- `6` curls: where a 6-shaped curl touched the number before it I wrote it joined (`286`, `246`, `176`, `236`...). Where it carried its own hook, plus or dot, or stood clear, it is its own token (`6p`, `6+`, `6.`, `6 7`).

## Every 3+ digit run left joined (token form; includes curl-joined numbers like 286, and unsplit pairs like 8618)
Numbers that are two numbers written together are marked by being listed here. Digit runs ending in a letter mark are included with them:
`1117p` (231v l. 2).
- f. 231r cipher line 1: 869 183 8618 2817+ 7618<hat>
- f. 231r cipher line 2: 156<2dot> 2869 2317. 224+ 869 183 226 246
- f. 231r cipher line 3: 241 316 2469 176 236<2dot> 286<v> 246
- f. 231r cipher line 4: 236<v> 224 281 7618<hat> 224+
- f. 231r cipher line 5: 236 176<bar>
- f. 231r cipher line 6: 264 7618<hat> 236 166 161.
- f. 231r cipher line 7: 422.
- f. 231r cipher line 8: 296<sign:small-2-above> 246 166
- f. 231r cipher line 9: 869 156<2dot>
- f. 231r cipher line 10: 161. 769
- f. 231r cipher line 11: 286<hat> 769 246 129 2861764
- f. 231r cipher line 12: 226
- f. 231r cipher line 13: 769
- f. 231r cipher line 14: 286<bar> 316 246<acute>?
- f. 231r cipher line 15: 183 769 316 28618
- f. 231r cipher line 16: 356<hat> 176
- f. 231r cipher line 17: 117+<v> 236
- f. 231r cipher line 18: 7618<bar> 316 2469 176 236
- f. 231r cipher line 19: 236 286 183
- f. 231r cipher line 20: 236 231
- f. 231v cipher line 1: 161 2869<bar>
- f. 231v cipher line 2: 236 218
- f. 231v cipher line 3: 356<hat> 166 306
- f. 231v cipher line 4: 316 286<bar> 156<hat>
- f. 231v cipher line 5: 2269 286 316
- f. 231v cipher line 7: 156 769 126 286 116 2969
- f. 231v cipher line 9: 422.<hat>
- f. 231v cipher line 10: 7618<bar> 2969 246 7618<hat> 161
- f. 231v cipher line 11: 176 286 236 117+ 124? 2864
- f. 231v cipher line 12: 236 356
- f. 231v cipher line 13: 124? 2864 869
- f. 231v cipher line 15: 161 246<v> 156 296
- f. 231v cipher line 16: 236
- f. 231v cipher line 17: 246 7618<hat> 286
- f. 231v cipher line 18: 286 211 214
- f. 231v cipher line 19: 236 2269 176
- f. 231v cipher line 20: 286<bar> 316 769
- f. 231v cipher line 21: 156<2dot> 2869
- f. 231v cipher line 22: 236 161 246
- f. 231v cipher line 23: 181 296
Runs I am least sure how to split (no gap visible): `8618`, `2817+`, `2869`, `2317.`, `224+`, `28618`, `2861764` (231r l. 11, same shape as the guide's `2561764`), `1117p` and `117+` (231v), `2469`, `2969`, `2864`, `124?`, `211`, `214`, `241`, `129`.

## Every `?` (token, page, cipher line)
- 231r l. 4 `d6<2dot>?` (two dots near the 6, unsure they are marks above); l. 8 `13<grave>?`; l. 11 `86.?<sign:small-3-above>` (a heavy blot at the baseline after 86 that may be a dot, and a small 3-like mark above);
  l. 13 `22.<2dot><bar>?` (two dots and a bar above 22. both uncertain); l. 14 `7p<under>?` (a short stroke below 7p, possibly an underline; guide asks for `<under>?`) and `246<acute>?`;
  l. 17 `17+?`; l. 21 `13p.<dot>?` and the sign before it (`P 14 2+`) is a poor read.
- 231v l. 1 `4?` (end, cut by the page edge); l. 2 `4?` (cut); l. 4 `2?` (cut); l. 5 `u?` (cut); l. 7 `d?` (cut); l. 8 `7?` (cut); l. 10 `7p<hat>?` (cut);
  l. 11 `124?` and l. 13 `124?` (third digit could be 1 or 4); l. 14 `28p<hat>?` (could be `7p<hat>`); l. 15 `11.<hat>?`; l. 21 `1?` (cut); l. 22 `4?` (cut).

## Every `<sign:...>`
See "Conventions". In order: 231r l. 8 (4 small-2-above); l. 11 (paren-stroke; 6 small-2-above, the last as `<sign:small-3-above>` on `86.?`);
231v l. 3 (1), l. 9 (2), l. 13 (cut), l. 17 (flourish).

## Every `<under>`
- 231r l. 9 `35+<under>` (clear underline below 35+).
- 231r l. 14 `7p<under>?` (doubtful).
- 231v l. 16 `30<under>` (the last sign of the line, under "30", clear).
- 231v l. 19 `30.<under>` (second sign of the line; underline under 30 clear, dot follows).
I looked for underlines on the numbers in the 30s in both passes and saw none besides these four; this is not an exhaustive per-token check.

## Where I am unsure whether a curl is joined or a separate 6
`156<2dot>` (231r l. 2, l. 9; 231v l. 21), `356<hat>`, `286`, `246`, `236`, `176`, `166`, `161.`: in each the 6 touches the number. `6 7` (231r l. 6, 17; 231v l. 15 has `76`): a 6 with a flourish toward the 7, written as two tokens. `d6` / `d6.`: written as one sign: d with a curl joined.
Also unsure: `H`-shaped signs (`17+`, `7+`): the "+" and the 7 share strokes, so I wrote `7+` / `17+` without a second plus. If the + is a separate cross at mid-height, those should read differently.

## Image problems
- f. 231v: the right edge of the leaf is a dark shadow or damage band from about x=3200; the ends of lines 1, 2, 4, 5, 7, 8, 10, 13, 16 to 18, 20 to 24 are cut or heavily shadowed. Cut signs are marked `?` or `<sign:cut>`. After "Sem" on l. 9 a virgula may be hidden in the shadow.
- f. 231v: lines slope up to the right; the left edge is bound and slightly dark; a hairline crack/scratch crosses 231v l. 11 near `286 6 2`.
- f. 231r: the left margin has a dark gutter band. Show-through is faint. A heavy ink blot on l. 13 (after `24p /`). A small blot after `86` on l. 11.
- f. 231r l. 8 and 11: the small marks above the signs overlap the descenders of the line above, so some small-2 marks may be descender tails. I judged them marks from their shape (curl at the foot, and a separate stroke).
- Facing-page strips (about 400 px at the gutter of 231v and 232r) show the other leaf and were ignored.

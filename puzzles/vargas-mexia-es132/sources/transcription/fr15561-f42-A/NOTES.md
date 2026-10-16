# Reader A notes (blind, guide v2.2)

Images: `sources/cache/f42-borja-blind/` only. Crops in a scratch folder under /tmp/claude-501/. Native resolution, no scaling.

## Passes
- Pass 1 (left to right, passages P1 to P4): 28 strips viewed. P1 2 (L+R), P2 2, P3 16 (12 hi-res strips of 3 rows,
  each L+R, plus 4 overview crops for the struck first and last rows), P4 8 (4 strips of 3 rows, L+R).
- Pass 2 (opposite direction: P4 to P1, bottom strip first, right half before left): 28 strips re-viewed, same split.
  Both passes complete. Changes in pass 2: added missing marks above (`256<v>` P3 r9, `156<dot>` P3 r6, `24.<hat>` P4 r7,
  `21<bar>` P4 r6 made certain), corrected `24+<bar>` to `24+<hat>` (P3 r10), changed `<hat>` to `<v>` on `7p` (P3 r4),
  made P3 r12 `24` carry a 2-shaped mark above instead of `<v>`, added `y<v>?` (P3 r15). Pass 2 added no new signs.
- Resolution of P1 and P2 is low (the screenshots are small and the strike lines run through the signs); those lines are the least reliable.

## Systematic judgment calls
- Z-shaped "ʒ" after an upright stroke written as `12` (addendum v2.1), everywhere: `12.`, `12+`, `121`, `126`. A true 13 or 23 would be misread this way.
- A tailed g-like sign written `9`. 
- A hook after a number (e/ε-like) written `p`: `6p`, `15p`, `20p`, `7p`. An s-like glyph inside numbers written `5` (`15`, `25`, `35`).
- Letter-like three-letter signs written as `<sign:...>` (zom/xom/ham/sem/lul/cil/col/yum/mis/de/Zam/Zum). Unsure whether they are cipher signs or clear syllables.
- `<sign:h+>`: a tall h-like stroke with a cross (12 occurrences). Might be a letter form or a 6 with tall stem; left undescribed.
- "Tall curl joined" 6 written joined whenever it touched the number: see list below.

## 3+ digit runs left joined (all are joined curl or two numbers; shape decision in each case)
316 (x4), 156 (x4), 201? (x4, last stroke may be a dot or 1), 296<v> (x2), 256 (x2, plus 256<v>), 176 (x2, plus 176<hat>, 176<bar>),
166 (x2, plus 166<bar>), 108<cross> (x2), 356<v>, 356<under>, 322<hat>?, 246 (x2), 246<2dot>?, 226, 221, 215?, 161,
156<dot>, 126 (x2), 121<hat>. Curls I was unsure were joined: `66` pairs everywhere (could be 6 + curl or hook), `201?`, `215?`, `221`.

## Every `?`
Token-level `?` appears 71 times (count of `?` characters in non-comment lines). Locations by line:
- P1 l1: `16.?` `11?`. P1 l2: `67?` `21<hat>?` `66?` `76?` `23+?` `215?` `35p?`. P1 l3: `60?` `2?`.
- P2: `15?` `2?` `12<v>?` `6p<v>` not marked; `322<hat>?` `22<v>?` `16p?`.
- P3 r1 (struck): `33?` `16.?` `9?` `35p?`. r2: `11+?` `201?` `20?`. r3: `15p?` `21<cross>?`. r4: `7p<v>?` `25+?`. r5: `7p?`. r6: `24p?`.
  r7: `92<hat>?`. r8: `26?<hat>?` `35p?` `246?` `62<dot>?`. r9: `9?` `201?`. r10: `5.?`. r11: `?1<bar>?` `15+?`. r12: `20p<v>?` `4<hat>?`.
  r13: `11p?` `201?`. r15: `25+?` `y<v>?`. r16: `20p<hat>?` `12<hat>?`. r17: `?0` `71<grave>?` `246<2dot>?` `35p?`. r18 (struck): `11+<cross>?` `17.?` and several bare `<sign:struck, illegible>`.
- P4 r1 (struck): `21<hat>?` `20?` `41<cross>?` `6?` `9<hat>?`. r2: `61<cross>?`. r3: `12p<hat>?` `201?`. r6: `22+<v>?`. r7: `4<bar>?`. r9: `4+?`. r10 (struck): bare `?` x5.

## `<sign:...>`
`<sign:h+>` x12; `<sign:Zom>` x3 (P3 r7, r15; P4 r1); `<sign:sem>` x3 (P3 r8; P4 r9, r10); `<sign:lul>` x2; `<sign:de>` x2; `<sign:cil>` x2;
`<sign:xom>`, `<sign:ham>`, `<sign:col>`, `<sign:yum>`, `<sign:Zum>`, `<sign:Zam>`, `<sign:mis>`, `<sign:h.>`, `<sign:f-like>`;
`<sign:2-shaped mark above>` x4 (P1 l2, l3; P3 r12; P4 r1: a small "2"-like stroke above a number, perhaps a mark of the same family);
P1 l1 opening `<sign:small 7-like sign above-left of line start>`; struck or illegible forms in P3 r1, r2, r18, P4 r1, r10.

## `<under>`
One only: `356<under>` (P3 r4). No other underline seen on any number in the 30s (`30.`, `316`, `33.`, `35p`, `36+` have none).

## Image problems
- P1: low resolution; heavy strike through both lines; line 1 almost only `16.` and `11`; the 7-like mark above the line start is not on the line.
- P2: white box hides the first signs of the line (annotation); the rest is struck and faint. "para" is clear and omitted.
- P3: left edge cut: row 2 first sign (`11+?`), row 4 first sign (`h.`), row 6 first sign, row 8 first signs, row 11 first sign (`?1<bar>`), row 17 first sign (`?0`) are partial.
  Rows 1 and 18 are struck by a heavy line and mostly illegible. The two X lines cross rows 3 to 17 and hide parts of signs (e.g. row 9 `9?`, row 13 `7p<hat>`).
  A large ink blot sits between rows 5 and 6 (near x 660, hires 1330/700 area). Row 11 ends in a flourish line (not a sign). Faint ghost signs in rows 2 (`20?`) and 4.
  Two dots after `24.<bar>` in row 5 (written `24.<bar>`, second dot dropped). A dot below `22.` in row 12 and below `11+<v>` in row 6 not recorded.
- P4: struck first and last rows; row 1 is mostly illegible. Faint dots above `12.` and `<sign:h+>` in row 2 not recorded. A dot below `yum+` in row 4 not recorded.
  The left margin edge is cut: first signs of rows 2, 3, 5, 6, 7, 8 may be partial.

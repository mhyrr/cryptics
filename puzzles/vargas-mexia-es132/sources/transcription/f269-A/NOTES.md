# f269-A: blind transcription notes (CIPHER3-GUIDE v2.2)

## Extent
- Letter starts on f. 269r (heading "El Rey", cross above "El"; page number 269 top right) and ends on f. 270r
  (place and date "De Merida a 16. de Mayo 1580.", then "Yo el Rey" and the countersignature).
- f. 269r: 5 clear lines (salutation "Juan de Vargas mexia." and a clear opening paragraph) + 25 cipher lines
  (first cipher line begins with clear "Venian me auisays").
- f. 269v: 29 cipher lines (no clear text except "ta" and "de" fragments inside lines). Faint mirror-image show-through of
  f. 270r at the top margin and right margin; ignored.
- f. 270r: 14 cipher lines (the last is a short line "231. /" followed on the same manuscript line by the date).
- f. 270v: address leaf, text rotated 90 degrees: "Por el Rey" (cross above "el", long rubric) / "A Juo de Vargas mexia en Paris. /".
  Transcribed in `[[ ]]` under its own header; not cipher. A seal ghost sits to the right.
- Total cipher lines: 68 (25 + 29 + 14). Several lines are short paragraph-enders ending in `/`.
- Countersignature as read: "Don Iuº de Idiaquez" (low confidence on the forename abbreviation and on the surname letters
  after "Id"; "Don" is clear, surname is tall-looped I, d, i, a, g/q, then a rubric). The King's signature reads "Yo el Rey".

## Passes and strips
Strip = one 3-line crop in a left and right half (1500 px wide, 300 px overlap, native resolution; line pitch is about
120 px so each crop is about 410 px high, which is 3 lines).
- Pass 1 (forward, left half then right half, first line to last): f. 269r 13 strips, f. 269v 12 strips (plus a reduced view of
  the foot of the page), f. 270r 6 strips, plus 3 crops of the two signatures and 1 of the rotated address = 35 strips.
- Pass 2 (opposite direction: last page first, last strip first, right half before left half, bottom line to top): f. 270r 6 strips,
  f. 269v 12 strips, f. 269r 11 strips (all cipher strips and the clear lines) = 29 strips re-viewed, plus the signature region of f. 270r
  as it appears in the last strip. The address leaf and the three signature crops were not re-viewed in pass 2.
- Pass-2 changes (about 25): 24+ marked with tilde above (269r l.2); 24 to 25+ (269r l.9); 14+ to 12+ (l.5); 17+ to 74 (l.13);
  74 with hat (l.23); 24 1 to 241 (two lines); 25+ gained bar and 2dot marks (269r l.17, l.15); 8+ gained 2dot (269v l.20);
  x-shaped sign "8+ x+" read as 2+ (269v l.3); 33+ hat added (269v l.8); a hat dropped on 3 (269v l.25).
  Remaining uncertainty is mostly in glyph identity (see below), not in tokenization.

## Glyph conventions I adopted (shapes only, no values)
- The sign that looks like a capital `H` (two uprights with a bar) is written `4`; where it stands as a base after a number it is
  written as a separate `4` (e.g. `34p 4 24+`). It might instead be a plus joined to the preceding digit. Uncertain throughout.
- An `x`-shaped sign is written `2` (`2+`, `2p`).
- The omega-shaped sign is written `w` (guide gives no form for it).
- A z-shaped 2 with tail is `2`; a tailed u-shape standing alone is written `u.` or `u` (guide: true `u` has no tail; many of
  these may be a 2).
- Hook after a base = `p`. A 6-shaped curl that carries its own `+` or `.` is written as its own token (`3 6+`, `1 6.`, `1 6p`),
  following guide section 2.
- A colon-like pair of dots after a sign is written `<sign:colon>`.
- The sign after "3<hat>" that looks like `d` (a looped `d` or delta shape) is written `d` (269r l.14, 269v l.4, l.20, 270r l.1).
- The letter forms `L u m` (269r l.11), `a<sign:tilde-above> L b u l d.` (269r l.16) and a `b` (269v l.20) are cipher letter forms
  as I read them; they could be clear Spanish, I could not tell.

## 3+ digit runs left joined
117 (1), 124 (4), 126 (3), 146 (1), 150 (1), 156 (1), 161 (3), 166 (9), 176 (7), 201 (9), 206 (1), 224 (1), 226 (1), 231 (6),
236 (12), 241 (5), 246 (9), 256 (20), 306 (4), 326 (3), 346 (2). Counts are token occurrences. Most of these are a
number plus a joined curl (236, 246, 256, 306, 326, 346, 166, 176, 206, 226, 126, 146, 156, 161) and are the curl rule applied.
Plain digit pairs with no gap that I left joined: 124, 201, 224, 231, 241, 117, 150. `763` was written `76 3` and `1 6+`, `3 6+`
etc. were written split.

## Every `?`
Line numbers below are approximate (my own counting per page); search transcription.txt for the token text to locate them.
269r: l.7 `3<acute>?`, `3p?` (end of l.7); l.8 (c3) `201?`, `6.<acute>?`; l.16 `a<sign:tilde-above>?`, `14?`; l.19 `231<bar>?`;
l.22 `74?`; l.23 `150<acute>?`; l.24 `25+<2dot><hat>?`; l.24 `25+<2dot>?` (end of cipher line 15 of that group).
269v: l.1 `1?` (cut by right edge); l.2 `u?` (cut by edge); l.5 `256?` (cut by edge); l.7 `2+<v>?`; l.10 `w<acute>?`; l.12 `6?`;
l.17 `24<hat>?`; l.20 `6?`; l.21 `4?`; l.23 `?` (cut by edge); l.25 `u?`; l.26 `24?`; l.27 `u?`.
270r: l.4 `117?`; l.5 `24+<v>?`; l.8 `22.?`; l.14 `231.<2dot>?`.
Many other tokens are less sure than their unmarked appearance suggests; I marked only the worst.

## Every `<sign:...>`
`<sign:colon>` (colon-like dot pair after a sign; about 40 uses), `<sign:tilde-above>` (269r l.16), `<sign:small-z-above>` (269r l.28,
a small z-like mark above 11), `<sign:2-above>` (269r l.30, a small 2-like mark above y), `<sign:end-flourish>` (269v l.3, line
ends in a pen flourish), `<sign:small-z-above-17>` (270r l.5, two small z-like marks above the end of the line),
`<sign:u-dot-hat-above>` (269r l.18, a small "u." with caret sitting above the sign), `<sign:close-paren>` (269r l.12,
a ")" shape after 24+; may be a virgula).

## Every `<under>`
269r: `33+<under>` (c1), `23.<under>` (c3), `34<under>` (269v l.1), `33+<under>` (269v l.8), `y<under>` (269v l.18),
`33+<hat><under>` (269v l.22), `18<under><v>` (270r l.3), `326<under>` (270r l.13), `y<under>` (270r l.13). None needed `<under>?`.

## Image problems
- Right edge of f. 269v is a dark band (page edge) about x=3140; the last sign or two of several lines (l.1, 2, 5, 14, 20, 21, 23, 25)
  are partly cut. These are marked `?`.
- Show-through of f. 270r (mirror writing) in the top margin and right strip of f. 269v; not confused with text.
- Ink blot under 12p on 270r l.9 and a smudge at the start of 270r l.4; no sign lost.
- A foxed/dark spot at the right margin of 270r near l.5 (outside the text).
- Foot of 269v and 270r clean; address leaf has a seal ghost and faint show-through of other text.

## Repeated sequences seen (for the reader, no values)
The phrase `34p 4 24+ 22. y<bar> 6. 3<hat> 24<hat>:` recurs (269r l.9 and l.28; 269v l.24, 25; 270r l.11, 14 approximately) and the
phrase `201 3` / `20+ ...` recurs; their recurrence made the H-sign reading more stable but is not proof.

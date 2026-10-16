# f. 89-B blind transcription notes (reader B, guide v2.3)

Line numbers below refer to lines of `transcription.txt` (header lines included).

## Images and overlaps
Nine screenshots `f89_s01.png` .. `f89_s09.png`, worked last to first, then re-checked first to last.
- s01 (top of f. 89: `El Rey.`, folio no. 89, salutation) and s02: the last 6 manuscript lines of s01 repeat as the first 6 lines of s02. Transcribed once, under s02.
- s03 and s04: the last 4 lines of s03 (`y 15p xom y Ra ...`, `23+ 28 6+ w ml ...`, `25+ pam ...`, `15+ ril ...`) repeat as the first 4 lines of s04. Transcribed once, under s04.
- s05 and s06: the last 3 lines of s05 repeat as the first 3 lines of s06 (the first of them is cut at the top of s06, so its text was read from s05). Transcribed once, under s06.
- s07 and s08: the last 5 lines of s07 repeat as the first 5 lines of s08. Transcribed once, under s08.
- s02/s03, s04/s05, s06/s07, s08/s09: no overlap found. s04 ends `...12+ 296 4<cut>` and s05 starts `12+ 296 4<hat> 6p quam`; the lines differ at their start, so I took it as a coincidence of repeated groups, not an overlap.
- Paragraph breaks (blank space, previous line ending in `/`): after s03 line `7p<hat> 25. 176<v> /` (new paragraph starts with a large flourished initial), after s04 `... 17+ /` (new paragraph with large initial A), after s09 line 3 and line 8 (the date).
- Top of f. 89 (s01): the header `El Rey.` has a bar and a cross above `El` and a small curl above the last letter of `Rey`; written as clear text in `[[ ]]`, marks not tokenised. Folio number `89` at top right. Large decorative flourishes (header, left margin of salutation, s09 left margin `Ey`-shaped flourish) are not transcribed. s09 shows folio number `91`.
- s01 line 3 of the salutation block ends with a cipher group `Lum 21. 24p` after a `/`, then a hook or comma-like flourish that I did not write as a token.

## Method deviations (be aware)
- Crops: strips of at most 3 lines, native resolution, ImageMagick. For s02..s08 the screenshots are at most 1532 px wide, so I cropped **full width** (no left/right halves) to keep them at native size under the viewer limit. Only s01 (1656 px) and s09 (1622 px) were cut into left and right halves (s01: 1000 px wide, overlap 344 px; s09: 950 px wide, overlap about 280 px).
- Crop heights were chosen from row positions measured from the image (row centres every ~70 px), so a strip can show the edge of its neighbour's line; those partial lines were ignored.
- Strips used: s01 5 strips (header, a-d, each in two halves), s02 5, s03 5, s04 5, s05 5, s06 6, s07 6 (4 viewed twice, the last two lie in the overlap with s08), s08 6, s09 3 (each in two halves).
- Images viewed: pass 1 about 63 views (including 9 overview views and 3 wasted views of mis-cut s08 strips), pass 2 50 views. Total about 113.

## Passes (guide section 6)
1. Pass 1: last image to first, each image bottom strip to top strip, each line left to right.
2. Pass 2: first image to last, each image top strip to bottom strip, each line re-read right to left against the same crops. **Completed for every image except the s01 header (strips `s1_hL`, `s1_hR`), which I did not re-view** (it is clear text, `El Rey.`). The s07 strips e and f (the overlap with s08) were not re-viewed as s07; they were checked as s08 lines 1-5.
Changes made in pass 2:
- s01: `68` on the second cipher row now `68<bar><cross>` (bar and cross seen together); an extra edge glyph `1.<cut>` added at the end of the last s01 row; a duplicated `22.` removed where the left and right halves overlap.
- s02: first line `86` marked `86?`.
- s04: `68` in line 5 of s04 now `68<bar><cross>`; `11.` marked `11.?`.
- s06: `68` in line 5 now `68<bar><cross>`; last token of the `... 9+ 24<acute>? 23+` line changed from `24.<acute>?` to `21.<acute>?`; `24+` before `15p<v> Rom` changed to `2+`.
- s07: `37<bar>` changed to `37<bar><cross>` (cross seen above, partly in the strip above).
- s09: `9<cross>? 2` changed to `92<cross>?` to match the same shape in s02.
Not resolved in pass 2: most `?` items below stayed uncertain.

## Reading conventions I adopted (these are guesses on shape, not values)
- The digit 5 here is written like a long `S`/`f`; I wrote it as `5` when it is joined to a number (`25+`, `15p`, `35p`) and as `S` only in the isolated forms (line `S 28 a 21` in s08, `4S`, `6S`, `Su`).
- `p` for the hook mark, including the e-shaped tail that follows `1`, `2`, `6`, `7`.
- The plus is often written like a small `t` or like a short `1` after the digit (`12t`, `23ı`). I wrote `+` in all those cases; some of them (e.g. `23+?`, `20+?`, `15+`) could be a curl or a different mark.
- `10` versus `w`: forms like `ω` are written `w`; forms where an upright `1` and an `o` are visible are `10`. The two forms are close and I may have split the same sign both ways.
- `h+?`: a tall-stroke sign followed by a plus that looks like `1t+` or `1ı+` (guide §9). I could not decide between letter `h` and the digits `11`/`14`, so every one is `h+?` (or `h|14p?`, `h|11p?`).
- `Rom`, `Ra`, `Zum`, `Qul`, `Bul`, `bul`, `dom`, `sem`, `ham`, `xal`, `xom`, `pam`, `pam+`, `qua`, `quam`, `Quam`, `Qom`, `Jam`, `Jim`, `Ja`, `Jo`, `Na`, `Lum`, `lum`, `Lo`, `Vum`, `bum`, `bim`, `ril`, `til`, `nel`, `gul`, `gil`, `cul`, `mil`, `ml`, `ym`, `rum`, `qum`, `dol`, `Dul`, `Dum`, `Su`, `de`, `d`, `a`, `co`, `no`, `C`: short letter groups, written as seen (guide §9).
- Large flourished initials at the start of a paragraph (before `Po` in s03, before `15p 356` in s04) are written as `<sign:large flourished initial ...>`. s03: `<sign:large flourished initial P> o`, but the letter could equally be `L`.

## Image problems
- Right margin ghost marks: in many images a column of small glyphs appears at the right edge, between lines (e.g. `4<hat>`, `+`, `u.`, `1.`, `8+`). Some are bleed-through from the other side of the leaf, some are overflow of a line past the margin. Where a glyph sits level with a line end I wrote it with `<cut>` or as a final token; others I left out (s02 margin `u.` at the end of line 12 region, a `+` beside line 10 and `4` beside line 7; s06 margin `+` beside line 12; s07 ghost text at right edge).
- Show-through (faint reversed writing) is visible in many strips, mostly in the gaps between lines and at the top of s06 and s07. Ignored.
- Strips are cut at the right edge in s01 (cipher lines run past the viewed area at x = 1656?), s04, s05, s07, s08: lines ending in `<cut>` may continue off the image. In s04 and s05 the screenshot cuts every line, while s02 and s06 show the true line ends.
- s01 right half: the first cipher row of the page carries a hatched stroke at the left margin (`////`), not a sign.
- s08, strip b first lines: black blob (ink) under the `y` of `y ym y`: ignored.
- s06 strip `d`: a faint `+` and `Na 6...` ghost at the top are bleed-through, not a line.
- s07 has a gap between the 9th and 10th line (about 140 px) that looks like a skipped row or a flourish descender only.
- s08 right edge shows ghost digits `10`, `13`, `21` at the end of several lines (line 14 `15. 13`, line 11 `1` after `66`): ignored; the `<cut>` on those lines marks where the real text stops.

## 3+ digit runs left joined (line numbers refer to transcription.txt)
- `246` x14: lines 6, 8, 15, 16, 18, 19, 37, 49, 52, 53, 65, 83, 106, 114
- `316` x5: lines 6, 21, 31, 33, 64
- `256` x27: lines 6, 9, 11, 21, 23, 25, 33, 34, 35, 36, 39, 41, 45, 53, 54, 55, 60, 60, 74, 80, 81, 81, 82, 106, 117, 119, 122
- `236` x22: lines 8, 13, 15, 15, 15, 17, 18, 20, 41, 49, 51, 53, 63, 76, 78, 81, 95, 105, 106, 117, 121, 123
- `131` x1: lines 10
- `176` x10: lines 11, 22, 38, 41, 47, 63, 69, 92, 103, 123
- `226` x11: lines 12, 16, 24, 28, 42, 49, 51, 52, 72, 78, 93
- `366` x2: lines 13, 115
- `156` x2: lines 13, 118
- `126` x2: lines 15, 61
- `326` x4: lines 17, 50, 95, 98
- `144` x1: lines 32
- `166` x13: lines 33, 48, 64, 64, 65, 66, 75, 80, 82, 101, 114, 114, 121
- `296` x9: lines 35, 57, 59, 65, 67, 83, 101, 109, 117
- `356` x5: lines 43, 53, 111, 112, 114
- `107` x1: lines 47
- `143` x1: lines 57
- `306` x2: lines 62, 82
- `100` x1: lines 68
- `117` x1: lines 68
- `206` x1: lines 70
- `139` x1: lines 76
- `118` x1: lines 102
- `663` x1: lines 104

## Every token carrying `?` (92)
- line 8 (f89_s01.png): `15+<hat>?<cut>`
- line 9 (f89_s01.png): `22.+?`
- line 11 (f89_s01.png): `22.<bar>?`
- line 13 (f89_s01.png): `13<acute>?`
- line 13 (f89_s01.png): `236<2dot>?`
- line 13 (f89_s01.png): `27+<v>?`
- line 15 (f89_s02.png): `86?<cut>`
- line 16 (f89_s02.png): `h+<v>?`
- line 18 (f89_s02.png): `1<bar>?`
- line 18 (f89_s02.png): `92<cross>?`
- line 21 (f89_s02.png): `h+<hat>?`
- line 21 (f89_s02.png): `p?`
- line 23 (f89_s02.png): `h+<hat>?`
- line 23 (f89_s02.png): `9+?`
- line 24 (f89_s02.png): `9+?`
- line 27 (f89_s02.png): `92<bar>?`
- line 28 (f89_s02.png): `h|14p?`
- line 28 (f89_s02.png): `18?`
- line 33 (f89_s03.png): `25p<v>?`
- line 39 (f89_s03.png): `h+?`
- line 42 (f89_s03.png): `66<cross>?`
- line 48 (f89_s04.png): `h+?`
- line 49 (f89_s04.png): `h+?`
- line 50 (f89_s04.png): `h+?`
- line 51 (f89_s04.png): `23.<2dot>?`
- line 52 (f89_s04.png): `h+?`
- line 54 (f89_s04.png): `h+<hat>?`
- line 54 (f89_s04.png): `11.?`
- line 55 (f89_s04.png): `h|11p?`
- line 55 (f89_s04.png): `d?`
- line 56 (f89_s04.png): `66<v><bar>?`
- line 57 (f89_s04.png): `143<bar><cross>?`
- line 59 (f89_s05.png): `86p?`
- line 62 (f89_s05.png): `h+?`
- line 63 (f89_s05.png): `h+?`
- line 64 (f89_s05.png): `2p<v>?`
- line 66 (f89_s05.png): `0<cross>?`
- line 67 (f89_s05.png): `4<hat>?<cut>`
- line 68 (f89_s05.png): `h+<hat>?`
- line 68 (f89_s05.png): `100<cross>?`
- line 69 (f89_s05.png): `h+?`
- line 70 (f89_s05.png): `Dum?`
- line 70 (f89_s05.png): `11S<cross>?`
- line 73 (f89_s06.png): `13p<2dot>?`
- line 73 (f89_s06.png): `h+?`
- line 76 (f89_s06.png): `139<cross>?`
- line 77 (f89_s06.png): `0<cross>?`
- line 79 (f89_s06.png): `h+?`
- line 81 (f89_s06.png): `24<acute>?`
- line 81 (f89_s06.png): `21.<acute>?`
- line 82 (f89_s06.png): `306<under>?`
- line 85 (f89_s06.png): `20+?`
- line 88 (f89_s07.png): `2?<cut>`
- line 90 (f89_s07.png): `15p<bar>?`
- line 91 (f89_s07.png): `25p<v>?`
- line 92 (f89_s07.png): `176<v>?`
- line 93 (f89_s07.png): `20+?`
- line 96 (f89_s07.png): `h+?`
- line 97 (f89_s07.png): `10?`
- line 97 (f89_s07.png): `20+?`
- line 97 (f89_s07.png): `Dul?`
- line 98 (f89_s07.png): `20+<hat>?`
- line 100 (f89_s08.png): `7<cross>?`
- line 102 (f89_s08.png): `h+?`
- line 102 (f89_s08.png): `6S?`
- line 103 (f89_s08.png): `h+?`
- line 104 (f89_s08.png): `0<cross>?`
- line 104 (f89_s08.png): `20+?`
- line 104 (f89_s08.png): `23+?`
- line 104 (f89_s08.png): `67<cross>?`
- line 105 (f89_s08.png): `6S.?`
- line 105 (f89_s08.png): `h+?`
- line 106 (f89_s08.png): `w?`
- line 108 (f89_s08.png): `20+?`
- line 109 (f89_s08.png): `h+?`
- line 110 (f89_s08.png): `15.<2dot>?`
- line 113 (f89_s08.png): `8+<v>?`
- line 113 (f89_s08.png): `20+?`
- line 117 (f89_s09.png): `w<hat>?`
- line 118 (f89_s09.png): `6.<acute>?`
- line 118 (f89_s09.png): `66<cross>?`
- line 118 (f89_s09.png): `6S?`
- line 119 (f89_s09.png): `29.<v>?`
- line 120 (f89_s09.png): `25p<bar>?`
- line 120 (f89_s09.png): `92<cross>?`
- line 121 (f89_s09.png): `6.<acute>?`
- line 123 (f89_s09.png): `176<bar>?`
- line 123 (f89_s09.png): `w<acute>?`
- line 123 (f89_s09.png): `86?`
- line 123 (f89_s09.png): `85<cross>?`
- line 123 (f89_s09.png): `1+?`
- line 123 (f89_s09.png): `h+?`

## Every `<sign:...>` (13)
- line 26 (f89_s02.png): `4<bar><sign:small 3 above>`
- line 36 (f89_s03.png): `16p<sign:small 2 above>`
- line 37 (f89_s03.png): `246<sign:small 2 above>`
- line 39 (f89_s03.png): `<sign:large flourished initial P>`
- line 39 (f89_s03.png): `<sign:V-shaped flourish>`
- line 53 (f89_s04.png): `<sign:large flourished initial A>`
- line 54 (f89_s04.png): `lum<sign:small 15p above lum>`
- line 55 (f89_s04.png): `<sign:t-shaped stroke>`
- line 80 (f89_s06.png): `3<sign:small 22 above>`
- line 92 (f89_s07.png): `<sign:small 2 above 6>`
- line 92 (f89_s07.png): `<sign:small 3 above 2p>`
- line 102 (f89_s08.png): `6<sign:small 3 above>`
- line 117 (f89_s09.png): `<sign:large V-shaped flourish>`

## Every `<under>` (7)
- line 10 (f89_s01.png): `30+<under>`
- line 15 (f89_s02.png): `3+<under>`
- line 18 (f89_s02.png): `30+<under>`
- line 51 (f89_s04.png): `30.<under>`
- line 62 (f89_s05.png): `306<under>`
- line 82 (f89_s06.png): `306<under>?`
- line 114 (f89_s08.png): `356<under>`
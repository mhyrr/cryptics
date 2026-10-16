# f. 62 (blind transcriber B) notes

Source images: `sources/cache/f62-blind/f62_s01.png` .. `f62_s11.png` (browser screenshots, page order). Transcribed under CIPHER3-GUIDE v2.3, blind to the key. Line references below are `sNN line K` = Kth transcribed line under that image header in `transcription.txt` (cipher lines counted together with the clear lines of s01).

## Deviation from the briefing (read first)
- Strips were cut as **full-width strips of 330 px height, step 300 px** (about 3 lines each, native resolution), not as left and right halves. Halves would have needed about 100 views per pass; the stated budget was about 120 in total. 50 strips per image set were made.
- Pass 1 (last to first image) viewed all 50 strips, plus one full-image view of s11 to see the layout (51 views). Pass 2 (guide section 6, first to last image, re-reading each line right to left) re-viewed 47 strips, about 98 views in all. **Not re-viewed in pass 2**: s01_01 (signature and flourish only), s02_04 and s11_05 (no cipher). Pass 2 was complete for every cipher line.
- Crops are in `/tmp/claude-501/f62B/` (`sNN_KK.png`).
- Because the strips are full width, the right edge of the screenshots is the limit; where a line runs off the image it ends in `<cut>`.

## Overlaps between screenshots (each repeated line transcribed once, under the earlier image)
- s01 / s02: the first 2 lines of s02 (`xom 21. 7p<hat> 4 ...` and `10 / 28 67 ...`) are the last 2 lines of s01 (s01 lines 14-15). Placed under s01. s02 starts at its third line.
- s03 / s04: the first 4 lines of s04 (`10 23+ 68 Rom ...`, `14 17p ...`, `23+ 86 ...`, `4 24 ...`) are s03 lines 13-16. Placed under s03. The first of the four had its marks above cut at the top of s04; the s03 reading is used.
- s05 / s06: the first 3 lines of s06 (`62 16. 15p 25. ...`, `15+ 18 30+ ...`, `23+ 10 6. ...`) are s05 lines 12-14. Placed under s05.
- s07 / s08: the first 3 lines of s08 (`246 6p 10 ...`, `28 25p ...`, `6. 4 24 ...`) are s07 lines 11-13. Placed under s07.
- s09 / s10: the first 2 lines of s10 (`6. 15+ 17p 23. ...`, `15p 6. sel ...`) are s09 lines 11-12. Placed under s09.
- No overlap found between s02/s03, s04/s05, s06/s07, s08/s09, s10/s11: each of these pairs is a page boundary or a clean continuation. Folio numbers seen in the margin: 62 (s01), 63 (s05), 64 (s09). Blank bottoms follow s02 (end of the page) and s04 / s06.

## Passes
- Pass 1: left to right per line, strips viewed last image to first.
- Pass 2: first image to last, each line re-read right to left against the crop. Changes made in pass 2 (examples): added marks above that pass 1 dropped (bar over `166`, `246`, hats over `15+`, `14`, `25+`; grave over `7p` in s11); corrected `22+`/`25+` to `24+` where the shape is the z-form 2 plus 4; re-split `46`/`12`/`14`; replaced `4p` with `49` where the hook is a g-shaped tail; changed `1ɿ` forms to `12+` and kept `14` only for the H-shaped form.
- Pass 2 changed roughly 60 tokens. Where the two passes disagreed and the crop did not settle it, the token carries `?`.

## Systematic ambiguities (not all marked `?`)
- **`12+` versus `14`**: a z-form second stroke after `1` (read `12+`) versus the H-shaped open 4 (read `14`). The two shapes are close; the reading is by shape and may be inconsistent in places.
- **`24+` versus `22+`**: the bold z-form followed by a tail was read `24+` throughout; a few could be `22+`.
- **`4` plus tail versus `49`**: the g-shaped tail after a 4 or 2 was read as digit `9` (`49`, `29`, `296`); a hook `p` is the alternative.
- **`6 8`/`68`, `6 7`/`67`, `6 2`/`62`**: written joined (a 6 followed by a number); these are two-digit runs, not 3+, but could be a free-standing 6 plus a number.
- **Pen-join dashes** (short horizontal strokes between signs, esp. in s01 and s02) were ignored as joins, not read as bars.
- **Faint ghosts** (bleed-through of the verso, e.g. `// 256 17p` in the margin of s02 L5 and the faint text under the signature in s11_05) were ignored.
- `y?`: a gamma-like letter form (tall `v`/`r`-shaped top with a descender) read as `y`; may be `r` or `v`.
- The `(` and `)` around a clear group in s02 lines 7-8 are written as `<sign:paren-open>` and `<sign:paren-close>`.
- `Rom`, `Rum`, `Ram`, `Ra`, `Pam`, `Bam`, `Ham`, `Zim`, `Qua`/`Qual`: capital-initial letter groups with a large swash first letter; `Rom`/`Rum`/`Ram`/`Ra` are readings of a Z-like swash capital (could be `Zom` etc.).
- Date line of s01: `uuij. vj. xj. xuij. xbij. xxj. xxuij. y xxvuij.` read as written (roman numerals with `u`/`b` letter-forms); not interpreted.
- Letter groups transcribed as seen: `bum bul sem sim sel si ril til pil tum Zim xom xul xal cem nec bel dom dul de pol mo quam qual Quam gil yul yum ho Ta a`.

## Every 3+ digit run left joined (token: count: image-line)
- `256` x39: s01:10, s02:5, s02:5, s02:7, s02:9, s03:1, s03:3, s03:4, s03:6, s03:7, s03:8, s03:16, s04:1, s04:3, s04:5, s04:5, s04:7, s04:8, s05:4, s05:8, s06:1, s06:2, s06:4, s06:6, s06:7, s06:9, s07:2, s07:10, s08:1, s08:3, s09:9, s09:12, s10:3, s10:6, s10:8, s11:7, s11:7, s11:8, s11:9
- `246` x23: s01:6, s02:2, s02:6, s03:7, s03:15, s05:1, s06:2, s06:3, s06:8, s07:4, s07:4, s07:8, s07:11, s08:7, s08:8, s09:1, s09:1, s09:2, s10:3, s10:5, s10:8, s11:6, s11:7
- `236` x20: s01:6, s01:8, s01:11, s01:13, s02:1, s02:5, s02:7, s02:7, s03:8, s03:9, s03:11, s04:4, s05:12, s05:13, s06:6, s06:9, s07:8, s08:1, s09:4, s11:4
- `166` x16: s01:7, s01:8, s01:11, s02:7, s03:3, s03:6, s05:4, s05:7, s05:14, s06:6, s07:1, s07:3, s08:6, s09:12, s11:6, s11:10
- `226` x15: s01:9, s01:12, s01:15, s02:1, s02:8, s03:4, s03:9, s03:14, s05:1, s05:10, s05:12, s05:14, s06:4, s07:9, s09:1
- `296` x9: s01:14, s01:15, s04:8, s05:2, s05:3, s05:8, s06:7, s07:1, s07:3
- `176` x7: s01:6, s03:3, s04:3, s06:1, s06:8, s09:3, s10:6
- `106` x5: s01:5, s02:3, s07:10, s08:7, s09:1
- `326` x5: s03:12, s04:2, s05:11, s06:2, s07:13
- `126` x3: s01:7, s03:5, s05:3
- `113` x3: s06:5, s07:3, s09:5
- `115` x2: s03:2, s10:5
- `156` x2: s03:11, s09:5
- `216` x2: s03:11, s05:13
- `133` x2: s04:4, s10:6
- `306` x2: s05:3, s11:3
- `316` x2: s10:2, s11:7
- `276` x1: s01:8
- `366` x1: s01:11
- `116` x1: s02:1
- `115+` x1: s05:3
- `166.` x1: s06:5
- `646` x1: s07:2
- `144+` x1: s07:6
- `224` x1: s08:2
- `118` x1: s09:2
- `100` x1: s09:7
- `107` x1: s11:4
- `144` x1: s11:8

## Every `?` (76 question marks in 76 tokens)
- s01 line 7: `r?`
- s01 line 7: `29p?`
- s01 line 8: `276<bar>?`
- s01 line 9: `y?`
- s01 line 12: `y?`
- s01 line 12: `17p<bar>?`
- s02 line 7: `4<acute>?`
- s03 line 2: `4<cross>?`
- s03 line 3: `16+<hat>?`
- s03 line 5: `til?<cut>`
- s03 line 9: `x?<cut>`
- s03 line 12: `2?<cut>`
- s03 line 15: `6?`
- s03 line 15: `13?`
- s03 line 15: `1?<cut>`
- s04 line 1: `1?<cut>`
- s04 line 2: `?<cut>`
- s04 line 8: `35p?<cut>`
- s05 line 3: `24+?`
- s05 line 3: `51<cross>?`
- s05 line 3: `9<bar>?`
- s05 line 12: `0<cross>?`
- s06 line 3: `/?`
- s06 line 5: `24p<hat>?`
- s06 line 5: `6?`
- s06 line 5: `24+?`
- s06 line 6: `0<cross>?`
- s06 line 6: `24?`
- s06 line 7: `2<cross>?`
- s06 line 9: `,?`
- s07 line 1: `51<cross>?`
- s07 line 1: `ho?`
- s07 line 1: `6?`
- s07 line 3: `24?`
- s07 line 3: `Z?<cut>`
- s07 line 5: `?`
- s07 line 6: `12+<bar>?`
- s07 line 6: `144+<cross><bar>?`
- s07 line 6: `91<bar>?`
- s07 line 10: `pol<bar>?`
- s07 line 10: `2?<v><cut>`
- s07 line 11: `6?<cut>`
- s07 line 12: `24?`
- s07 line 12: `2?<cut>`
- s07 line 13: `6.<bar>?`
- s08 line 1: `23<2dot>?`
- s08 line 1: `12+<hat>?`
- s08 line 2: `224<2dot>?`
- s08 line 2: `2?<cut>`
- s08 line 7: `2<cross>?`
- s08 line 9: `24<hat>?`
- s09 line 1: `246<hat>?`
- s09 line 2: `118<cross><bar>?`
- s09 line 4: `4<bar>?`
- s09 line 5: `113<cross>?`
- s09 line 7: `67<cross>?`
- s09 line 7: `100<cross><bar>?`
- s09 line 9: `22.?`
- s09 line 11: `y?`
- s10 line 2: `7<cross>?`
- s10 line 2: `67?`
- s10 line 3: `y?`
- s10 line 4: `67<cross>?`
- s10 line 5: `115<cross>?`
- s10 line 5: `0?`
- s10 line 5: `34?`
- s10 line 7: `10<hat>?`
- s11 line 2: `semp<bar>?`
- s11 line 3: `20+?`
- s11 line 3: `2?<cut>`
- s11 line 4: `107<cross>?`
- s11 line 6: `6.<bar>?`
- s11 line 7: `5?`
- s11 line 7: `1?<cut>`
- s11 line 8: `144<cross>?`
- s11 line 8: `6?<cut>`

## Every `<sign:...>`
- s01 line 11: `<sign:tall vertical squiggle>`
- s02 line 7: `<sign:paren-open>`
- s02 line 8: `<sign:paren-close>`
- s06 line 1: `<sign:faint dots>`
- s11 line 6: `<sign:wavy above>`

## Every `<under>`
- s02 line 5: `30.<under>`
- s03 line 10: `30.<under>`
- s05 line 3: `306<under>`
- s06 line 2: `35+<under>`
- s11 line 3: `306<under>`

## Image problems
- The screenshots are of a high-contrast binarised image; fine marks above signs (hats, small v) sit close to the line above and are sometimes clipped at the top of a strip. Where a strip boundary cut a mark, the neighbouring strip was used.
- The right edge of s03, s04, s05, s07, s08, s11 cuts the last sign of many lines (`<cut>`); the gutter shadow clips about one sign.
- s11_05 and s02_04 carry no cipher (signature tail, blank).
- s01_01: the signature "El Rey" with a long flourish; a cross above the "El"; faint verso text is visible below it.
- The browser UI toolbar icons are visible at the top of s07 (ignored).
- A stray stroke left of s05 line 13 (`15+<bar> ...`) and at the left margin of s11 line 8 was ignored.

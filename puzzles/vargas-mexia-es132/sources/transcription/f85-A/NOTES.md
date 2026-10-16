# f85-A blind transcription notes (guide v2.3)

Images: f85_s01..s05.png (5). No other file was opened apart from the guide. No network.
Cipher-bearing lines: 57 (s1 3, s2 17 incl. the wrapped tail `23.`, s3 18, s4 11, s5 8). Clear-Spanish-only lines are in `[[ ]]`.

## Overlaps
- s01 / s02: the last cipher line of s01 (`81 4 24+ 6. 16p ...`) is the first line of s02. Transcribed once, under s01. Line-by-line check against the s02 crop done; s02 starts at its second line.
- s03 / s04: the last four lines of s03 (`32. ...`, `28 16. ...`, `81 4 ...`, `28 7+ m6 n. ...`) are the first four of s04. Transcribed once, under s03, and cross-read against s04 crops (differences were folded in, e.g. `21.<acute>`).
- s02 / s03 and s04 / s05: no overlap (s05 is the next page, f. 86 recto, folio number 86 at top right; its first line is new).
- s02, last cipher line: the line ends with `10` at the right and `23.` stands under it. Written as a separate line `23.` (wrapped tail). 

## Passes
- Pass 1: left to right over strips of at most 3 lines, left and right halves (900 px wide, ~300 px overlap), native resolution, crops in /tmp/claude-501/f85A/crops/. 
- Pass 2: all strips viewed again in the opposite order (last image to first, right half before left half), every line re-checked token by token. Complete. 
- Images viewed: 54 crop views in pass 1 (+ 5 whole-page views at the start, + 4 extra crops of s04 top and the `7. 6. n` line that the first strip set missed: x0L, x0R, x1L, x1R), about 59 in pass 2.
- Changes in pass 2 (examples): `21.<acute>` (s03 line 16, s04) was an acute over the 21 and not over the 10; acute vs hat on the 4 before `66 7p` (s02); bar over `15+` and over `12+`; `m 1 n6` and not `mp 1 n 6` (s03 line 11); `r. 24` end of s03 line 14; hat on `7p` after `10<acute>` (s04 line 2); `ya avisarmeeis` in the clear text.
- Not resolvable at this resolution (kept as written, see `?`): the many hooks `p` after 7, 15, 20, 24, 29 versus a plain 6-curl; the tiny marks above (acute / v / hat) are easy to confuse at 900 px halves. Expect disagreement with another reader on these.

## Decisions on shapes
- `1H` shapes (a tall 1 followed by an H-like open 4 with crossbar) were read as `14` everywhere (`14+`, `14p`, `14<hat>`). Two strokes were visible in each; none was read as the letter `h`. If the guide's h-form is the intended reading for some of these, every `14` followed by a mark is a candidate.
- `x` is a crossed letter form with a diagonal stroke; `r` is the small v/r-shaped letter form (in `6. r.`, `20+ r.`). The line between them is not sharp in this hand; some `x.` / `r.` may be swapped.
- `n`, `m`, `A r`, `em`, `mp`, `np`: letter groups written as one token where the letters were joined. `m 1` (m followed by a separate 1) was kept apart.
- `z`-shaped 2: read as 2 inside numbers (`24`, `23`, `22`).
- `7p`, `7+`: a 7 with a hook / a 7 with a plus. Many have a flourish across the stem; I did not split it off.
- The first `/` after `n6 4 x.` (s02) and the `/` after `24p` (s03 line 6) and after `se ofreziere` (s04) and the one after the `El qual alt` Spanish are followed by a small dot; written `/ .` (or `/.`). 
- A long faint straight line crosses `7+ 21. 18 ...` on s03 line 17 / s04 (`18<bar>?`): probably a page scratch or ruling, not a mark above 18.
- Page edge: on s03 and s04 the right edge of the page (dark band) cuts every line near x ~ 1400 (s03) / 1430 (s04); these lines end with `<cut>`. s05 lines are mostly complete; line 3 (`... 26`) and line 5-6 may be cut at the right edge.

## 3+ digit runs left joined (all are a number plus a curl 6 touching it, unless marked)
296 (s01 l1, s01 l3, s02 l13, s04 l2, s03 l1, s03 l14), 256 (many; each followed by `76 18` in the recurrent `256 76 18`), 316 (s01 l1, s03 l8), 166 (many; read as 16 + curl, or 1 + 66), 156 (s02 l2 `156<acute>?`, s04 l12 `156`), 246, 236, 306<under> (s02 l11), 106 (s04 `106 25.`), 216 (s04 `10 216`), 176 (s04 `176 6+`, s05 `176`), 206 (s04 `7+ 206 24+<hat>`), 166<bar> (s02 l6), 246<bar>, 256<bar>, 236<2dot-less>. 
Joined with doubt about the curl: `161` (s02 `14p 161 7p`), `306<under>` (underline spans the curl), `176 6+` (s04: could be `17 66+`), `166` generally (16+curl vs 1 + 66), `86` / `86<bar>` (8 + curl).
Not joined but close: `10 15+` at the end of s01 l2, `10 15` end of s01 l3 and s02: kept apart (small gap).

## Every `?`
- s02 l2: `156<acute>?` (tick over the 15 is faint)
- s02 l4: `15<dot>?` (dot above the second 15)
- s02 l13: `10<acute>?`
- s02 l17: `2p<v>?` (first sign could be `20p<v>` or `27p<v>`)
- s03 l1: `71?` and `29.<v>?<cut>` (edge)
- s03 l2: `4<acute>?`
- s03 l3: `16.<v>?`, `2+?` (could be `24+`)
- s03 l6: `4<cross>?` (an X-like blot above the 4)
- s03 l10: `71?`
- s03 l13: `15<dot>?`
- s03 l14: `24+?` (overwritten / scribbled)
- s03 l17: `18<bar>?` (see the ruling line above)
- s04 l2: `em.?`
- s04 l7 (the `7. 6. n` line): `23p<bar>?`
- s04 l8: `71 ?<cut>` (the last sign(s) are cut by the page edge)
- s05 l3: `24.<bar>?`
- s05 l7: `8?` (last sign overstruck with a heavy stroke)
- in the Spanish lines: `[[se ofreziere?]]`.
Total: 19 `?` on cipher lines, 1 more in clear text.

## Every `<sign:...>`
None used.

## Every `<under>`
- s02 l11 `306<under>` (underline under 30 and the curl)
- s02 l15 `30.<under>`
- s03 l13 `35.<under>`
- s05 l5 `30<under>`
- s05 l7 `3 6<under>` (underline under the 6 only; it may belong to `36`)
No `<under>?` was needed; no underline was seen on 31, 32, 33, 34, 35 elsewhere, but `35` in s02 l4 (`4<hat> 35.`, twice) and s03 l13 were checked: only the s03 one is underlined.

## Image problems
- s02: bottom edge shows part of another hand (`9. 96 12 20+ 100 6+ ...`), cut off: not part of the letter, ignored.
- s04: lower right has a rotated marginal note in another hand (`... de Agosto ... presso ...`), not transcribed.
- s03 and s04: right-edge band is the dark gutter; lines are cut (see above).
- s05: page top edge is rolled/curled; top-right folio number 86; a flourished signature under the date line (clear: `Yo el Rey`).
- Resolution: native 1400-1570 px wide pages. Small marks above signs (hat vs acute vs v) and the p-hooks are at the limit of legibility; the p hook on 15p / 24p / 29p versus a smudge was not always certain.
- Clear text: Spanish readings are diplomatic guesses at best (`xvj`, `Mantigond`, `xby. xxiy.`, `a ix.`); they were not the target.

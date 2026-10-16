# f185b-A blind transcription notes (CIPHER3-GUIDE v2.3)

Images: 7 screenshots, `f185_s08.png` to `f185_s14.png` (in `sources/cache/f185b-blind/`). Cipher lines transcribed: 103 (plus 7 header lines). Reader: blind, no decoding attempted.

## Overlaps (transcribed once)
- s09 starts a new leaf (page number "187" at top right). A short cross-like mark at the very top of s09 sits above the first line and was not assigned to any sign.
- s10 rows 1-2 repeat the last two rows of s09 (`4 22.<hat> Rum 4<bar> 11 14 29+ ...` and `6+ 6p 6. 8e ... S.<hat>`). Kept in s09 only.
- s11 does not overlap s10 (no repeated rows found).
- s12 rows 1-2 repeat the last two rows of s11 (`15+ 12.<bar> 256 20 6.<bar> ...` and `4 15+<bar> ... quam 7 1`). Kept in s11 only.
- s13 starts a new leaf (page number "188" at top right); no overlap with s12.
- s14 rows 1-2 repeat the last two rows of s13 (`15+ 22. 20 1 306<under> ...`, `12+ S6 6p 364 ...`). Kept in s13 only. Within s14 the strips overlap by design; s14 rows `15p q. 66 276 ...`, `17p 28<bar> 4<hat> ...`, `17p S. ...` at the bottom were not repeated elsewhere.
- s08: a fragment of a further line appears at far bottom right (`<cut> 66.?`); its left part is below the image edge. s09: a faint partial line at the very bottom edge was not readable.
- Page-edge: every right-hand line is cut at the dark page margin; such lines end `<cut>`.

## Passes
- Pass 1: left to right, top to bottom, in half-width strips (3 lines, left 0-850 px, right from 500 px), at native resolution. ~72 strip views plus 2 targeted crops (s10 rows near the faint fragment).
- Pass 2: independent re-read bottom to top, right to left, in full-width 3-line strips (native resolution, about 1300 px wide, so no downscaling). Not half strips, to stay within the ~120 image budget. Pass 2 views: 5 (s14) + 5 (s13, one wasted on a tiny last strip) + 4 (s12) + 4 (s11) + 4 (s10) + 5 (s09) + 4 (s08) = 31. Completed for all images.
- Changes from pass 2: `20 4+` read as `20 L4` (two lines); s11 row C end `2019` re-read `20 14<bar>?`; s11 row H `14 4` -> `14 4<bar>?`; s08 rows 7 `L` -> `L4?` (two places). Everything else confirmed.
- Total images viewed: about 112 (pass 1 about 80 including 4 wasted/tiny strips; pass 2 31).

## Quality caveat
The hand is small, joined, and the images are about 1300 px wide, so many 2-digit versus 3-digit splits are uncertain. Expect split errors in runs listed below. In particular `22`/`2`+`2`, `1`/`4`/`14`, `6` vs `5`/`S`, `0` vs `6` and the curl rule are all frequently ambiguous.

## 3+ digit runs left joined
Joined curls (`6` after a number, guide rule): 256 (14), 246 (8), 316 (7), 156 (5), 126 (5), 286. (4), 176 (3), 236 (2), 296 (2), 226, 276, 116, 306 (underlined), 346, 356 (underlined), 806-like `800`/`8 0 28` splits, 1660, 7620 / 7618 / 7610 / 7018 (these are `7`+`6`+`20`/`18`/`10` or `70`+`18`: ambiguous), 2064 / 2564 / 1764 / 1760 / 2964 / 764 / 664 / 224 / 214 / 113 / 128 / 1200 / 1028 / 1561 / 2014 / 250 / 249p / 235 / 230 / 804 / 028 / 1166 / 114 / 127p. Every one of these is a joined run I could not safely split; most are curl-after-number or digit-pair collisions (`2564` = 25 6 4? or 256 4, `1764` = 17 6 4 or 176 4).
Exact joined runs and counts are in `transcription.txt`; find them with `grep -o '[0-9]\{3,\}'`.

## Question marks
72 `?` characters in the transcription (see `grep -n '?'`). Systematic groups: marks above (`<hat>?`, `<acute>?`, `<bar>?`) where a stroke could be a bleed-through; letter forms (`m`, `q`, `u`, `y`, `S`) vs digits; `h|14?` at s12 row 3 and `114<hat>?` at s13 row 5; `L4?` (s08 row 7); the faint cluster in s10 and s14 `22+ 224+ 22+ u+ 6p 25p 16.` (the left half is show-through-like but the right half is bold; recorded once in s10 as a right-hand fragment and once as the tail of a long s14 line).

## `<sign:...>` used
- `<sign:ink blot>` (2): a black blot in s08 row 6 and s10 last row, taking the place of a sign.
- `<sign:ligature like 'Dig'>` / `'Digi'` / `<sign:loop ligature like 'Dig'>` (5): a looped ligature that looks like the letters "Dig" or "Digi"; shape not resolved to digits or letters. Appears at s08 rows 11-12, s09 rows 8 and 15, s12 row 11.
- `<sign:long thick horizontal flourish>` (1): s11 row 11, ends a short line.
- `<sign:small 2 above>` (4): a small 2-shaped mark above a number; in other places it may be a mark above that I could not classify (the guide has no 2-shaped mark above).

## `<under>`
Written at: s12 row 2 (`356<under>?`), s12 row 12 (`35+<under>`), s13 row 5 (`35+<under>`), s13 row 13 (`306<under>`), s14 row 8 (`296<under>`). All are clear short strokes under the number, except `356<under>?` in s12 row 2.

## Image problems
- Ink bleeds through from the other side in s10 (rows around the faint fragment), s09 right half, s14 bottom half; read as faint show-through and ignored.
- Lines slope and the page margin cuts every right end; many lines end `<cut>`.
- Resolution of about 1300 px for ~35-sign lines makes the small marks above (hat versus bar versus acute) unreliable. Treat marks above as lower-confidence than bases.
- Short lines ending in `1` (e.g. s08 row 5, s09 row 10, s10 row 3) look like paragraph or sentence ends with a long vertical stroke.
- Repeats noted for the decoder: the phrase `[[quam]]` appears in cipher lines at the start of line-segments about 12 times; `[[de]]` about 4 times; `Rom`/`Rum`/`Romise`, `xom<bar>`, `Jim`, `sem<bar>`, `mer` appear as letter groups. Clear Spanish was otherwise not present (no salutation, date or signature in these images).

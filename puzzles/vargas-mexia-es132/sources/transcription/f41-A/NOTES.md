# f41-A notes (blind transcriber, guide v2.3)

Images: f41_s01 ... f41_s07 (7). s01-s04 are the page numbered 41; s05-s07 are the page numbered 42 (new page starts at s05).
Cipher lines in transcription.txt: 97 (includes the last cipher line that shares its row with the clear date). Header "El Rey", salutation, date, signature are in [[ ]].

## Method actually used (deviations, stated plainly)
- Pass 1 (left to right): every image cut into strips of at most 3 lines, each strip cut into a left half (900 px) and a right half (about 600 px overlap), native resolution. Lines rise toward the right (up to ~45 px on s03/s04/s05), so right halves for s03, s04, s05 (some), s06, s07 were re-cut with extra headroom (the `R2` crops). Images viewed in pass 1: 75 strips + 7 whole-image overviews = 82.
- Pass 2 (right to left, last image to first, each line re-read from its right end): done in full, but on **full-width 3-line strips** (about 1500 px wide, native), not on half strips, because left and right halves again would have been about 150 views against a budget of about 120. 35 views. Total 117 views. The right-to-left reading was done on all lines of s01-s07 except the two overlap lines at the top of s06 (read in pass 1 only, compared with s05).
- Changes made in pass 2 (about 25 tokens): e.g. `8+<hat>` in s03 L4, `3<hat>` on several "86 3" groups, `<bar>` added on 25p and 18 in s05 L10, `3<grave>` in s01 L11 and L14, `121?` for what pass 1 gave as `12+?`, `176<hat>` s03 L13, `20p<hat>` s03 L16, `co<bar>?` s03 L2.
- Resolution is the limit: at this screenshot size the tiny marks above signs (hat vs v vs bar vs 2dot) and the curl vs plus distinction are often at the edge of legibility. Expect marks-above errors to be the most common kind in this transcription. Digits themselves are more stable than marks.

## Overlaps
- s02 lines 1-4 repeat the last four lines of s01 (s01 L13-L16). Transcribed once, under s01 (L16 completed from the s02 image, because it is cut at the bottom of s01).
- s04 lines 1-5 repeat s03 L15-L19, and s04 line 6 is the line cut at the bottom of s03. Transcribed once: s03 L15-L19 under s03, line 6 under s04.
- s06 lines 1-2 repeat the last two lines of s05 (s05 L17, L18). Transcribed once, under s05.
- No overlap between s02/s03, s05/s04 (page change), s06/s07: the last line of the earlier image and the first line of the later one differ.

## Conventions added (not in guide)
- `:` after a number = two dots at baseline after the sign (e.g. `24:`). Used about 40 times. If you treat it as `<2dot>` it is a different mark; I kept it distinct from marks above.
- `Z` and `d`-like big flourish signs are written `<sign:Z-flourish>` and `<sign:d-like>`; they occur in the same positions line after line (after `20. 22.` the Z-flourish; after `co` the d-like) so they are almost certainly single signs.
- `/` (virgula) used for the vertical stroke in s03 L2, the slash after `24:` in s01 L10, the slash at the right end of s01 L13 (`/?`), the stroke before the date (s07), and the paragraph slash in s06 L6 (`6. 15+ /`).
- Paragraph break in s06: blank space after `6. 15+ /`, then a line starting with a tall initial `y` with a long looping left tail and a faint arc above it.
- `<cut>`: the right margin rule on f. 42 (and the page edge on f. 41, s03/s04) hides or crosses the last sign or two of most lines of s03 and s04 and a few of s05; marked on each.
- Not transcribed: page numbers "41" (top right of s01) and "42" (top right of s05).

## Pass checks
Pass 2 left each line at the pass-1 reading unless listed above. Lines where pass 1 and pass 2 disagreed on a base digit (not a mark): s01 L7 (`121?`), s05 L15 (`336?` vs `326?`), s04 L14 end (`201?`).

## 3+ digit runs left joined
Most are number + curl: `256` (31+), `176`, `236`, `246`, `226`, `166`, `161`, `156`, `326`, `346?`, `336?`, `356`, `216`, `166p`, `114p`, `114`. All treated as number + closed curl (guide section 2). Runs that are not clearly number + curl:
- `161` / `161n` (numerous): "16" + "1" or 16 with a bar-like stroke; left as `161`.
- `231?` (s05 L2, L5 region), `231` (s07 L3 end), `201?` (s05 L1, s04 L14 end), `181<cut>` (s03 L4), `187+` (s07 L3: could be `18 7+`), `121?` (s01 L7), `113<bar>?` (s06 L11), `224:` (s02 L7), `226.<v>?` (s02 L7).
- `166` has a number-curl-curl reading too (`16 6` / `1 66`); left joined.
- `1578` and 11 in `6. 11 256` (s01 L3, s05 L9 `6. 11 256`) are written as 11.

## Every `?` (60 in total) / question areas
In transcription.txt the `?` is attached to the token. Grouped:
- Marks above unsure (most): `7+<v>?` `24+<2dot>?` `23<v>?` `8+<bar>?` `co<bar>?` `17p<bar>` pairs in s01-s03, s05 `25p<v>?`, s06 `8p<2dot>?`, s02 L11 `3<hat>?`.
- Base unsure: `06.?` `3 326?` `y 4p?` (could be y + 4p, or `y4p` `yep`) s01 L2/L4; `356<under>?` s01 L6; `121?` s01 L7; `33+<2dot>?` s01 L8; `10`/`co|10` in s06 L13; `201?` runs; `231?`; `346?`/`336?`/`326?`; `24p?` s04 L16; `2?<cut>` at line ends hidden by the margin; `75 18?` s02 L13; `26<v>?` s02 L18; `20p 23?` s06 L10; `2.?` s06 L7; `113<bar>?`.
- Joined-curl doubts: all `?`-marked runs above; I never wrote a free `6` where a curl touched the previous number.
- `<sign:ink blot>`: s02 L6 has a heavy ink blot (printed as 16p y 3p? y u. 15<bar> ... blot ... 17p<bar>); a few signs there may be wrong or missing.

## Every `<sign:...>`
- `<sign:Z-flourish>` x5 (s02 L9, s03 L4, L9, L14, s04 L17; also `<sign:z-flourish>` s03 L5): a z-shaped stroke with a long curved tail after `20. 22.`
- `<sign:d-like>` x6 and `<sign:d-like-flourish>` x2: a d/delta-like loop after `co` (s03 L11-12, s04 L10, s05 L11, s06 L7, L15) and at the end of s02 L18.
- `<sign:small-z-above>` s06 L16, a small z over the second 24+.
- `<sign:ink blot>` x1, see above.

## Every `<under>`
s01 L6 `356<under>?`; s01 L13 `33+<hat><under>`; s02 L10 `33+<under>`; s02 L14 `20+<under>?` (this is a small z-like squiggle under 20+, not a plain bar: treat as unsure); s03 L18 `35+<under>`; s06 L11 `34+<hat><under>`. The date "1578" in s07 is underlined (inside the [[ ]] date).

## Image problems
- Small size: the marks above (hat, v, bar, 2dot, acute) are 5-10 px; many calls are probable, not certain.
- s03, s04: right margin rule crosses the lines; the last sign or two of many lines are hidden or cut (marked `<cut>`). Lines rise ~45 px left to right; a crop at fixed y cut the right ends until re-cut.
- s02 L5-L7: ink blots and show-through.
- s07 date: "a x x x? de Abril de 1578": the day numeral is written as three or four x-like strokes (`xxx?`); not resolved.
- Letter-form groups (`xom`, `Rom`, `co`, etc.) per guide section 9: only `co` (omega-like, extremely common), `n`, `S`, `y`, `u`, `r`, `M6` (s04 L16) occur; I found no `h` and no other 3-letter groups.

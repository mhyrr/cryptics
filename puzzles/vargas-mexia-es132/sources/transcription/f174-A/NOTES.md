# f. 174 blind transcription, reader A (guide v2.3)

Line references are "image, n-th line of that image's block" counting every non-comment line (cipher or clear) in
`transcription.txt`. Images: f174_s1 (clear text only), s2-s4 (f. 174 cipher), s5 (f. 175 begins: page number "175"
visible), s6, s7 (end: "del Pardo", date, signature).

## Overlaps
None found between consecutive images. The first ~20-30 px of s4 and s6 show descenders of the previous image's last
line (not new lines); s6 also has faint bleed-through at top right ("28 256"), ignored. s3/s4 and s5/s6 begin with a new
line. The s4 bottom right carries a cut-off signature/word (not transcribed).

## Passes
- Pass 1 (left to right): half-strips (left x 0-900, right x 600-end, ~300 px overlap) at native resolution, 3 lines each
  (s3 right half of its 10th line, and s4 line 9, needed an extra crop because lines rise to the right and the strip
  boundary cut them; those extra crops were viewed).
- Pass 2 (right-to-left, bottom-to-top, every line re-read from its right end): done in full for every cipher line of s2-s7,
  but on **full-width** 3-line strips (reused crop coordinates), not on half-strips, to stay inside the image budget.
  About 20 lines changed in pass 2 (mostly marks above, `16`/`18` confusions, `14`/`h`, a few curl joins, last-token cut-offs).
- Not done: s1 (clear Spanish, 3 views, read once only) and the date/signature strip (read once). Hand-drawn signature
  not transcribed.
- Views: pass 1 about 78 (incl. 7 overviews), pass 2 about 32; total about 110.

## Conventions I adopted (shapes only)
- Glyph like a `q` (loop with descender, often a hat/bar/acute above) written `q`; open-tailed `g` written `g`; the
  looped script-d `d`; z-shaped 2 as `2` (guide 7); a closed curl after a number joined (`156`, `246`, `166`).
- Letter groups (guide 9): `Rom`, `gil`, `sim`, `Zum`, `Sem`, `Bam`, `bel`, `mil`. `p` with long stem plus hook written `p`,
  `p6`, `p+`. `6z`, `7g6`, `d618` kept as seen.
- "1H" shapes mostly written `14`; written `h|14?` only where it looked like a single tall h.
- Virgula `/` appears mid-line once (s6 line 14).

## 3+ digit runs left joined
Almost all are a number plus a joined curl by the curl rule: `156` (65), `246` (55), `166` (41), `236` (32), `286`, `356`,
`176`, `316`, `226`, `256`, `126`, `296`, `106`, `206`, `146`, `276`, `346`, `386`, `266`, `116`, `610`, `310`/`316`,
`2306`. Runs that are not a plain number+curl and are the real uncertainty:
`2269` (s2 l3, s3 l4/l5), `269` (s2 l5, s6 `246q`-adjacent), `769`/`1769`/`869`/`2869`/`7618`/`8618`/`28618`/`6618`/`d618`/`2861764`
(sequences where I could not tell number boundaries), `201`, `2014`, `114`, `231?`, `0236?`, `3567`/`3567.`/`3567+`/`30617e`,
`1833.`, `7620.`, `2864`, `766`, `300`, `224+`, `281`, `d296`. In each of these the split is a guess.

## Every `?`
s2: l1 `11.?`, `10<v>?`, `g?`; l2 `6z?`, `156<2dot>?`; l5 `14+?`; l6 `15+<2dot>?`; l12 `20+<2dot>?`, `23+<2dot>?`
(the two small "2"-like marks above those signs).
s3: l4 `6p?<cut>`; l9 `1<cross>?`. s4: l2 `q?`; l3 `231?`; l5 `y?<cut>`; l7 `14?`; l8 `156<2dot>?`; l10 `24+<bar>?`
(a bar struck through the sign); l13 `34?<cut>`. s5: l2 `22<cross>?`; l5 `0236?`; l7 `21.<2dot>?`.
s6: l4 `m?`; l5 `256?`; l10 `h|14?`; l12 `2p<hat>?`; l13 `124?`; l17 `34<under>?`, `18<hat>?`.
s7: l5 `6y?<cut>`; l10 `q<acute>?`; l15 `231?`. Total 31.
Curl-joining was uncertain (guide 2 "when in doubt write joined") in many more places than carry a `?`; I did not mark the
ordinary `156`/`246`/`166` cases. Where "bp"/"be" (a 6 plus hook or curl after 1) I wrote `16p`/`166` or `6p`/`66` by shape.

## `<sign:...>`
- s2 l16: black ink blot (thick comma-like) with `76<hat>` and small marks above it.
- s3 l9: an `f`-like sign with a bar above.
- s7 l15: a loop flourish after "del Pardo" (not cipher).

## `<under>`
s3 l13 `3q<under>.`; s4 l2 `35+<under>`; s6 l5 `33+<under>`; s6 l12 `30.<under>`; s6 l17 `34<under>?`; s7 l7 `356<under>`
(the underline sits under the 3-and-next sign; it may span two signs).

## Image problems
- Right margin of s3, s4, s7 is dark (page edge); lines end with `<cut>` where a sign touched it. Lines slope upward to the right,
  so the 3-line strips sometimes clip a line's right end (re-cropped s3 l10, s4 l9).
- Faint bleed-through (mirror cipher) throughout; ignored. Marks above (`<v>`, `<hat>`, `<acute>`, `<2dot>`) are the least
  reliable part of this transcription, especially at line ends and where the hat/acute/tilde could not be told apart.
- Final tokens of lines near the edge (`2<cut>`, `1<cut>`, `14<cut>`) are fragments.

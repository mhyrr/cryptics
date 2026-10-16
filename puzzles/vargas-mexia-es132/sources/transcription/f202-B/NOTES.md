# f202-B: blind transcription of the letter on BnF Esp. 132 ff. 202r-203v (guide v2.3)

Transcriber worked blind: read only CIPHER3-GUIDE.md and the four page images, no network, no other repository file,
no decoding. Output: `transcription.txt`, in letter order (202r, 202v, 203r, 203v). Pass 1 was done last page to first
(203v, 203r, 202v, 202r) as briefed; pass 2 in the opposite order (202r, 202v, 203r, 203v), bottom to top and right
half before left half within each page. "ms-line" below = manuscript line counted from the top of the page, clear lines
included (so 202v cipher line 1 is ms-line 8).

## Extent
- Starts: f. 202r, top: "+ El Rey", then "Juan de Vargas Mexia / A vuij. del presente se recibieron vras cartas de
  xxuij. y xxv. del passado". The cipher begins mid-line 2, right after "passado".
- Ends: f. 203v, ms-line 6: "De Aranxuez a xxvij. de Mayo. M. D. lxx|x." (read lxxix, the "|" being a slashed i),
  then "Yo el Rey", the countersignature, and the address line "A Juan de Vargas mexia". One letter on four pages.
  Nothing else starts or ends on these pages.
- Layout: 202r = header, 2 clear lines (line 2 continues into cipher), cipher block 1 (ms-lines 2-7), 8 clear lines
  ("Segun la diligencia ... de mi parte"), cipher block 2 (7 lines, ends `1. 18<v> 9. 1.`). 202v = 7 clear lines, then 16
  cipher lines. 203r = 17 cipher lines, then 3 clear lines ("Ha se entendido ... y assi les"). 203v = 6 clear lines,
  the two signatures, the address.
- Total: 46 cipher lines (13 on 202r counting the mixed clear + cipher line 2; 16 on 202v; 17 on 203r; none on 203v).
- Not transcribed (one line each): (a) bottom of 202r (and again on the facing 203r position): a two-line note in
  French in a later hand ("... gouvernement et parhalitez dont l'exemple est"), not part of the letter; (b) sideways
  fragments in the right margin or gutter near the foot of 202v and 203v ("29"-like, cut by the paper edge); (c) faint
  mirror-image cipher visible through the leaf on 203v, 202v, 202r (show-through); (d) the ~400 px of facing page at
  each gutter (e.g. "gil", "22", "21" at the left edge of 203r); (e) the foliation "202" at top right of 202r; (f) small
  dashes "-" at the right end of many 203r cipher lines (margin marks, not tokens).

## Countersignature
"Cayas": a large looped rubric with the initial (C or cedilla C) and "ayas" clear, then a second rubric. Probably the
secretary Zayas written Cayas/Çayas; I give it as written: Cayas. The King's signature is "Yo el Rey" with a
large flourish.

## Passes and strip counts
- Pass 1: left half then right half of each strip, top to bottom, native resolution. Halves were 1700 px wide
  (overlap ~200 px, not 300). Strips were 430-640 px tall. Pass-1 strips on 203r and part of 202r were up to ~3.7 lines
  tall (about 640 px), slightly over the 3-line limit. Two crops were viewed at 200-250% to learn the glyph vocabulary
  (203r lines 1-3, one 202v line); everything was read at native size afterwards.
- Pass 2: re-cut at different row offsets, 3 lines or fewer, and every line re-read against the draft. Pass 2 added many
  marks above that pass 1 had dropped and corrected several tokens (examples: 202v ms-lines 13-14 `22+`/`16+<bar>`,
  203r l9 `24p<bar> 166<bar>`, 203r l11 `23.<v>`, 202r B2-4 `3<hat>`, `4<hat>`, `7p<hat>`). It also removed a spurious
  `<under>?` (the "underline" under `18` on 202r ms-line 7 was the bar over `8+` on the next line).
- Strips (native-size views) pass 1: 64 (203v 10, 203r 15, 202v 21, 202r 18), plus 2 zoom views.
- Strips (native-size views) pass 2: 76 (202r 22, 202v 24, 203r 20, 203v 10).
- Second pass was completed on all four pages.

## Judgement calls (so a reader can undo them)
- `<bar><cross>` where a plus sits over a visibly separate horizontal stroke; a single plus is `<cross>`. At native size the
  two are often indistinguishable.
- A "1H" glyph (1 + H-shaped stroke) is written `14`, `14+` when a separate cross follows, `146` before a curl.
- The 4 is often drawn with a long crossbar and looks like `24+`; I wrote `+` only where a separate cross seems visible.
  This is the most uncertain systematic choice (`24+`, `22+`, `20+`, `12+`, `17+`, `13+`).
- A hook without a descender is still `p`. `y+` = tailed y with a cross.
- Letter groups, one token each: sol, Ral, ral, ham, quam, Rom, fom, fum, lum, yum, som, mc, cu, dc, co, fil, gil, pal,
  Bam, ta, xal, Jo. Single letters: y, e, a, d, g, j, R, S6.
- `iod?` (3 places: 202r B2-4 end, 203r l7, 203r l17): a 3-letter group; could instead be `10` + `d`, or `cod` (the first stroke is an
  upright with a small foot, not the round c of `co`).
- The glyph "1o" with a small closed loop (tall 1 + small circle, sometimes with a tick) is written `10`, with its marks
  (`10<hat>`, `10<acute>`). It may be `16` (number + curl). Occurs: 203r l1, l5, l15; 202v l4, l6, l16, l17; 202r B2-1.
- "86", "46", "26", "66", "36", "76": curl joined per the guide. On 202v ms-line 18 I wrote `8 6.` because the curl has
  its own dot.

## Every 3+ digit run left joined
All are a number plus a touching 6-curl or a pair of such (`156` = 15 + curl, `166` = 16 + curl or 1 + 66, etc.).
By line of transcription.txt (lines count the header comments; the file has 4 page headers):
- 202r: 8 `246`; 10 `166`; 11 `176`; 12 `166`; 21 `356`, `176`; 22 `246`, `176`; 23 `316`; 24 `246`; 25 `256`;
  26 `176`, `136<2dot>?`.
- 202v: 36 `166`; 37 `356<under>`, `166`; 38 `236`, `236<hat>`, `246`; 39 `166`, `166`; 42 `246`, `156`, `146`; 43 `246`;
  44 `246`, `166`, `176`, `226`; 45 `356<under>`, `246`; 46 `236`, `216`; 47 `236`; 48 `166`; 49 `176`, `246`;
  50 `176`, `166`, `246`.
- 203r: 53 `236`, `226`; 54 `236`, `246<v>`; 57 `156`, `146`; 58 `236`; 59 `166`; 60 `236`; 61 `166<bar>`, `226`; 63 `256`;
  64 `256`; 65 `166`; 67 `176`, `176`; 68 `246`; 69 `246`.
Doubtful splits: `166` (could be `16 6` or `1 66`), `226`, `236`, `246`, `256`, `146`, `156` (curl vs a free 6), and `176`.

## Every `?`
202r: ms-line 5 `/?` (a slash at the margin end of the line); ms-line 7 `76<2dot>?`; B2-4 `gi?`, `iod?`;
B2-6 `136<2dot>?` (a dotted 1-like first stroke before 3 and a curl).
202v: ms-line 8 `13+<2dot>?`, `15p<2dot>?` (dots over the first stroke), `o?` (the "/0/" group before the last `6.`);
ms-line 9 `13<bar>?`, `2?` (after the `6`); ms-line 10 `7+<v>?`; ms-line 11 `gi?`; ms-line 13 `2?` (the "42"); ms-line 14
`R<v>?` (a large curled letter with a small hook above); ms-line 17 `10<cut>?` (gutter); ms-line 18 `4<acute>?`, `6.?`
(see `8 6.`); ms-line 20 `21.?` (could be `2c.`).
203r: l1 `sol<bar>?`; l4 `15p<dot>?`, `o?` ("/0/"); l6 `4<bar><cross>?` (final group "1 4 4" under a plus); l7 `iod?`,
`u<acute>?` (the last sign, a small u with a tick); l8 `51<cross>?`; l17 `iod?`, `1.?` (a slanted stroke plus dot closing
the cipher; 202r ends with `1.` too).
Total 27 `?`.

## Places where I was unsure whether a curl is joined
202v ms-line 9 `6 2?` (a 6 followed by a z-like 2: curl + 2, or joined `62`); 202v ms-line 18 `8 6.`; 202r l2 `6 7` (two
bases, not `67`); 203r l6 final group; 202r B2-6 end `136<2dot>?`; the `10`/`16` glyph above; every `166`.

## `<sign:...>`
None used.

## `<under>`
Five: 202v ms-lines 9 `356<under>`, 15 `35+<v><under>`, 17 `356<under>`, 23 `35p<under>`; 203r l11 `35+<under>`. I looked for
an underline below every number in the 30s (30, 31, 33, 35, 36) and saw one only on these. 202v ms-line 15 and 203r l11 are
the two with a clear stroke of the same length as the number; none is doubtful enough for `<under>?`.

## Marks above I hesitated over (not `?`-marked)
`<hat>` vs `<acute>` on short strokes over `24.` (203r l1, l9); `<v>` vs `<2dot>` for tilde-like marks (202v ms-line 21
`20p`, 203r l2 `246<v>`, 202r B2-1); bar vs cross on an elongated plus. A few small marks may still be missing: marks
above sit at the very top of the line and were the most often dropped in pass 1.

## Image problems
- Gutter: each page carries ~400 px of the facing page. The dark gutter shadow on the right of 202v cuts the last token of
  many cipher lines (`<cut>`), the end of clear line 1 ("Itali[a?]") and `parte`.
- Show-through of mirror-image cipher under the clear text on 202r, 202v, 203v; ignored.
- Blots and smears: 203r l6 dark smudge by `28` and a smear over `66`; 203r l2 `246` looks struck through; 202r stray
  dot after `24p` (l5); a stray acute-like tick left of `16p` (202r B2-1); a "u"-like mark at the right edge of 202r l5 beyond
  the last token; dashes at the right margin of 203r.
- Lower right of 202v and 203v: sideways marginal writing, cut by the paper edge, not read.
- 203v begins mid-sentence ("direis ..."); the sentence started at the foot of 203r ("y assi les").
- Uncertain clear readings: first word of 203r ("Ha" or "Ya"); the numerals "vuij"/"xxuij" on 202r (read as written);
  "nras" on 202v (abbreviation of "nuestras", not expanded); "elisan" on 202r (long s; could be "elijan").

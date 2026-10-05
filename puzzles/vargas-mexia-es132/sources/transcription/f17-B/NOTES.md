# f17-B transcription notes (blind reader B; guide v1.1)

Source: sources/cache/pages/f017r..f020v.jpg, read in reverse page order (20v first, 17r last), one page per file.
Method: native crops resized to ~0.7-0.8x and **thresholded at 30-32%** (ImageMagick `-threshold`) to suppress the grey
mirrored bleed-through; crops in sources/cache/f17-B-crops/. Pages 18r, 19v, 20v have the worst bleed.

## Honest statement on the passes
Pass 1 (left to right per strip) was done for every line. **No complete independent right-to-left second pass was run**;
only spot re-reads of doubtful stretches (20r/20v, bottom of 19v, 18r) were done. Treat the transcription as a single-pass
reading with many `?`.

## Page/line map (non-comment lines in transcription.txt, includes clear-text lines)
| page | lines | notes |
|---|---|---|
| 17r | 26 | heading "El Rey" + 9 clear lines (letter opening), 16 cipher/mixed lines; clean image |
| 17v | 25 | 3 clear-in-cipher lines; nearly all cipher; clean |
| 18r | 26 | heavy bleed; lines 1-6 and 15-22 partly unreadable (`<illegible: bleed>`) |
| 18v | 27 | mixed; catchword "Por vra carta" bottom right; "2o" top right margin |
| 19r | 27 | most of page is clear Spanish with 6 as an embedded cipher sign |
| 19v | 27 | 7 clear lines at top then cipher; bleed bottom third |
| 20r | 28 | cipher; ends with a flourish below last line |
| 20v | 16 | not blank: last cipher lines, date, signatures |
Page numbers in manuscript: "17" (17r), "18" (18r), "19" (19r), "20" (20r), "2o" in top-left of 19r and top-right of 18v.
20v: 13 text lines (cipher and clear), date line "[[A vnj? de Marco 1578]]" (bar above 1578 and a dash after),
royal signature (flourish, illegible), "Ant. Perez" signature, small "Dup." and a smaller word above it ("Dal?").

## Letter-forms and special signs used
- `<rho>`: used often (large looped sign with long descender), esp. 17v, 18r, 18v, 19v, 20r. Many uncertain: the line
  between `<rho>` and a plain g-shaped 9 with a long tail was hard; where tail was short I wrote 9 or 9e.
- `<venus>`: 20r line 9 (once), 17v line 2 and 17v line 3 (with the 9+ before it), 18v none, 17r line 15 ("9. <venus>"), 19r none,
  19v none, 20r also `<venus>^` in line 23.
- Letters: `R` (very frequent), `C` (frequent, often with dot above `C^`), `P` (17r once), `f` (many), `p` (20r, 18r, 19v), `m`
  (17v, 17r, 18v), `n` (many, 17v/18r/18v/19v), `Ce` (19v, 17r). 
- Other: `<sign:u-like>` = a u/v-shaped stroke before or after 6/2 (17r, 17v, 18v, 20r); `<sign:z-with-tail>`;
  `<sign:y-like>` (17v last-but-one line); `<sign:L-like>` (18r); `<sign:large loop, e-like>` (17v); `<sign:flat stroke>` and
  `<sign:long flat stroke linking ...>` (a horizontal stroke joining two signs, 20r lines 8 and 20, 17r).
- The "6" is a separate frequent base (also written inside clear text as a cipher word). 0 appears on its own as `0+`/`0e`
  (e.g. "6 0+ 6"); I did not merge it with a preceding 2 where there was a gap.
- `<bar>` used above 12, 14, 15, 18, 19, 2, 6, 7, 10, 11, 13, 21, 22, 4, 5, m; many may be pen flourishes.

## Number of `?` (rough, including those inside clear text)
17r 2, 17v 5, 18r 19, 18v 14, 19r 18, 19v 23, 20r 19, 20v 20 (about 120 lines flagged in total, plus all `<illegible>`).

## Hardest places
- 18r (all of it between the heading and the middle): mirrored 18v text overlaps.
- 19v lines 1-7 (clear text, overlapped), the stretch "que ... mis ... arbuse" (19v), last 3 lines of 19v.
- 20v lines 1-6 (bleed from 20r on the right side); the "g/8/9/<rho>" family throughout.
- Dots: above/below dots are the least reliable layer on all pages (many lines have none recorded where the dot may exist).
- Overlaps of left/right strips: signs near the overlap (x ~ 1900 native) may be duplicated or dropped.
- 17v/18v/20r have recurring sequences ("6 0+ 6", "9+ 17 12e 13", "R 6 ...") that I did not use to cross-check, to stay independent.

## Clear-text readings are low confidence
They are diplomatic-ish but not carefully collated; expand/modernize nothing. Example doubtful: 19r line 1 "Por vra carta de" (read from the catchword at 18v foot), 17r line 6 "do , y por todas ...".

# f22-B: blind transcription of the Cipher 2 letter, BnF es. 132 ff. 22r-25r

Reader: one blind reader following CIPHER2-GUIDE.md v1.1. Shapes only; no keys, no other transcriptions or analysis
files were opened, nothing fetched. Output: `transcription.txt` (manuscript order, `# ===== f. NNr =====` markers).

## 1. Page map used
Local whole-page images in `sources/cache/pages/`: f022r, f022v, f023r, f023v, f024r, f024v, f025r (one folio side
per file; no Gallica canvas numbers used). Strips were cut with ImageMagick at native size (about 1,300-1,500 x
330-360 px, halves overlapping about 150-200 px) into `sources/cache/f22-B-crops/`; hard places re-cut at 150-250 %.
Reading order: 25r first, then 24v, 24r, 23v, 23r, 22v, 22r; lines in order within a page; output re-assembled in
manuscript order.

## 2. Line counts
| page | cipher lines | clear lines | notes |
|---|---|---|---|
| f. 22r | 18 | 8 + heading "El Rey" | heading, 8 clear lines, then 18 cipher lines |
| f. 22v | 28 | 0 | |
| f. 23r | 29 | 0 | |
| f. 23v | 19 | 10 + 1 short last line | cipher, then clear paragraph, then a last line "y parte?" and an ink blot |
| f. 24r | 22 | 7 | cipher 8 lines, clear 7 lines, cipher 14 lines |
| f. 24v | 29 | 0 | |
| f. 25r | 15 | 3 | last cipher line ends in clear "De Madrid. A vij."; then date line, "Yo" signature, "Antseros?" |

Total: 160 cipher lines and 29 heading/clear/signature lines. Question marks in the file: 129 (cipher and clear
together). Page-by-page counts of `?` (cipher + clear): 22r 10, 22v 13, 23r 14, 23v 29, 24r 23, 24v 29, 25r 11.

## 3. Show-through, page edges, blobs
- 22r, 22v, 23r, 23v, 24r, 24v all carry mirror show-through from the other side of the leaf. It is worst in the left
  half of the lines of 24v (almost every line), in 23v lines 1-5 and 17-19, in the lower lines of 23r (where the clear
  text of 23v shows through as mirrored cursive), and in 24r lines 1, 9-14, 18-22. Show-through is grey and
  mirror-reversed; I did not transcribe it, but where real signs are overwritten I wrote `<smudged ~N signs>` or
  `<smudge>`.
- Right-hand ends: on 22v, 23r, 23v, 24r, 24v many lines run off the visible page edge (cut facsimile or gutter
  shadow). The last sign there is often partial: marked with a bare `1`, `9?`, `<sign:dash at edge>`,
  `<sign:diagonal stroke at edge>`. I did not invent continuation.
- Paragraph ends: a heavy blob stroke (thick short slash, usually dot after it) at the end of a short line. Written
  `1?` (or `1.?`, `1.`). Occurrences: 22v l. 8 and 19; 23r l. 4 (`8? 1?`) and 9; 23v l. 19 and (cipher) l. 17 end; 24r l. 8 and 17;
  24v l. 5 and 22; 25r l. 8. Whether it is a digit 1 is a judgement call.
- 22r: faint mirrored lines above the clear paragraph are 22v showing through; "D. p12" at lower right is a later hand
  (not transcribed); a small cross sits above "El Rey". 22v: a faint mirrored "El Rey" above line 1 is the 22r heading
  showing through.
- 25r: right margin has small separate marks beside lines 7-12 (a "p"-like sign and dots), outside the text block, not
  transcribed. Below the date: "Yo" (royal signature, flourished) and lower right "Antseros?" (endorsement hand, read
  tentatively).

## 4. Conventions I added (the guide has no slot for these)
- `<sign:small o>+` (also bare `<sign:small o>`): a small round o with a cross, written `o+`; seen often, mostly alone
  between 6s or between 2 and 10. I could not decide whether it is 20 with a tiny 2, a 0, or a letter. Where it is
  clearly joined to a 2 I wrote `20+`.
- `8` vs `9`: a figure-8-shaped sign (closed loops, usually with a tail) is written `8` (`8e`, `8.`); the g-shape with an
  open tail down-left is `9`, as in the guide. Many cases are borderline; `9?`/`8?` mark the worst. The first sign of
  25r l. 1 (`9?`) is a g/8 hybrid. The guide's `g?` was not used.
- `<rho>`: only where the tail drops well below the line. A smaller hooked p with a tail is `pe` (letter-form p plus
  hook); `p`, `p?e`, `p_?` otherwise.
- `2<bar>`: a z-like 2 with a long horizontal stroke over or beside it, often drawn out to join the next sign. Many are
  swoosh strokes rather than true bars; `2<bar>?` where it runs on.
- `<sign:long dash>`, `<sign:thick dash>`, `<sign:long stroke>`: free horizontal strokes between signs.
- A sign carrying both a hook and a cross: the guide allows one mark after; I wrote only the hook (`13e`, `20e`,
  `4e`). Where a base looks as if it already contains the cross (an H-shaped 4) I wrote `14`, `14+`, `14e` by the mark seen.
- Clear text: diplomatic, long s written s, abbreviation tildes `~`, doubtful words `?`, `/` where a virgula is written.

## 5. Letter-forms and special signs used (where)
- `f` (long f with descender; usually `f.`): 22r l. 1, 13-ish (lines 1 and 12 of the cipher), 22v l. 10, 23v (1), 24r (6), 24v l. 6, 17,
  25r l. 1, 2, 8.
- `p` / `pe`: `pe` on 23r (8: e.g. cipher l. 2, 3, 6, 8, 11, 12), 23v (3), 22v (3), 22r l. 6; bare `p` on 23r l. 13 (`p+`... see 24v l. 13 `p`), 24r.
- `n`, `n+`, `n^`, `n_`: 22r, 22v l. 2, 9, 23r, 23v, 24r, 24v l. 4, 25r l. 4.
- `m`, `me`, `m+`: 22v l. 6 (`me`), 23r l. 12 (`m a?`) and l. 25 (`m+`).
- `R`: 22v (7), 23v (4), 24v (6), 22r, 24r, 25r l. 4, 12.
- `C`, `Ce`, `C^`, `C_`, `C+`: 22r (3), 22v (8), 23r, 23v, 24r, 25r l. 4, 9.
- `P`, `Pe`, `Pe<bar>`: 22v l. 23, 27; 24v l. 14; 25r l. 6.
- `v`: 22v l. 13, 16; 23r l. 12.
- `h+`, `he`: 23r l. 16 (`h+`), 25r l. 4 (`he`).
- a-like forms: 25r l. 1 (`<sign:a-shaped loop>_`), 23r l. 12 (`m a?`), 23v l. 11 (`<sign:small a/o>+?`).
- Other specials: `<rho>` (22v l. 1 `<rho>_`, 23v l. 5, 6, 7?; 24v l. 6; 25r l. 1, 3, 12); `<venus>` not seen;
  `<sign:D-shaped loop>` (23v l. 19 end); `<sign:d-form>+` (24v l. 13, a d-shaped ascender sign with cross);
  `<loop with dot>` (22r cipher l. 2).

## 6. Every `?` (cipher tokens; clear lines by number), by page
Line numbers count every non-comment line of the page, so on 22r the heading is line 1 and the 8 clear lines are
lines 2-9 (the cipher starts at line 10).
- 22r: clear lines 2, 4, 5; cipher (numbering from line 10 = first cipher line): `2<bar>?` (l. 10), `2<bar>?` (12), `2<bar>?` (17), `14e?` (18), `2<bar>?` (19), `9?` (21).
- 22v: 1: `11?` `9?`; 6: `2<bar>?`; 7: `2<bar>?`; 8: `1?`; 11: `,?`; 13: `C_?`; 14: `16?`; 19: `2<bar>?` `1?`; 20: `1?`; 22: `5?`; 26: `2<bar>?`.
- 23r: 4: `8?` `1?`; 5: `n<bar>?`; 9: `1.?`; 10: `6+?`; 11: `p?e`; 12: `a?`; 13: `18?` `11?`; 14: `18?` `2<bar>?`; 18: `8?`; 23: `2<bar>?`; 29: `3?`.
- 23v: 2: `9?`; 3: `8?`; 7: `2<bar>?`; 8: `2<bar>?`; 9: `12^?`; 10: `6?` `3^?`; 11: `<sign:small a/o>+?`; 13: `12^?` `8?`; 17: `4e?` `1?`; 18: `2<bar>?` `4?` `8?`; 19: `1?`; clear lines 20-30 all carry doubtful words.
- 24r: 1: `4?.` `8?` `9?`; 3: `9?`; 8: `p?e` `1?`; clear lines 12-15 doubtful words; 18: `13?`; 20: `p_?` `1?`; 21: `8?`; 23: `,?`; 24: `1?`; 25: `9e?`... (numbered as in the file); 26: `1?`; 27: `2<bar>?`; 28: `1?`; 29: `5?` `6?` `14e?`.
- 24v: 1: `12^?` `12+?` `17+?` `5?` `7?` `4+?` `10?` `12e?`; 2: `2?`; 5: `1?`; 6: `6<bar>?`; 7: `20_?`; 9: `8.?` `4?` `18_?`; 10: `14+?`; 12: `4^+?` `<sign:small o>e<bar>?`; 14: `4?`; 15: `11_?`; 17: `12e?`; 18: `4^?` `5?`; 20: `4?`; 22: `1?`; 25: `8?` `13?`; 27: `18_?`; 29: `2<bar>?`.
- 25r: 1: `9?`; 3: `17_?`; 6: `18^?` `11_?`; 8: `20_?` `1.?`; 9: `2?`; 12: `11^?`; 14: `18.?`; 15: `20_?`; clear line 18 (Antseros).
(A grep for `?` on `transcription.txt` reproduces the exact list; the per-line numbers above are approximate for the
pages with clear paragraphs.)

## 7. Hardest places (where another reader will most likely differ)
1. 24v, whole page: dense small signs with mirror show-through in the left half of every line; lines 1, 2, 12-14,
   18-22 worst. Every line carries at least one `?`. Treat 24v as the least reliable page.
2. 24r lines 1, 9-14, 18-22 and 23r lines 1-4, 12-16, 24-29: show-through plus smeared ink; `<smudged>` stretches are
   real signs I could not separate from the reverse text.
3. 22r cipher line 2: the left half is a dark smear with ink overwriting the signs; I give only the outer signs.
4. 8/9/5 and S-curve vs g-shape; the sign I write `8` can be confused with `9`, or (with a long entry stroke) with a
   z-like `2`.
5. Dots above vs below: decided by distance. Doubtful dots are `_?` or `^?`; other dots are unmarked but may be the
   neighbouring line's dot; not every dot was checked systematically.
6. 11 vs 14 vs 12 in fast hands on 23r and 24r (H-shaped 4 read as `14`).
7. Clear text: abbreviations (Resp.ta, Seruiº, chro~, occasio~, enq~) and the unusual spellings on 23v are
   tentative; 23v and 24r clear lines run into the cut right edge.
8. The heavy end blobs `1?`: digit one or paragraph mark?

## 8. Pass 2 (independent right-to-left re-check): honest coverage
- Pass 1: left to right per strip, at native resolution, for every line of all seven pages, working in reverse page
  order (25r, 24v, 24r, 23v, 23r, 22v, 22r).
- Pass 2: I re-cut strips with different cut points and read them right to left against the written lines for 25r lines
  1-14 (the whole cipher except the last line and the signature block) and for 22v lines 2-5 and 9-14. I did **not**
  repeat a full independent right-to-left pass over 22r, 23r, 23v, 24r, 24v, 22v l. 15-28, or 25r l. 15. For those pages the
  only second look was the overlap between left and right strips (cut at different x offsets, vertically staggered),
  plus zoom re-checks of individual doubtful signs.
- Changes found in pass 2: 25r l. 3 `9e` -> `8e` (before `17^`); 25r l. 10 `13` -> `13^`; 22v l. 13 `<rho>` -> `C_?`. No other
  discrepancies in the re-read lines. Both passes were done by the same reader, so the stability is optimistic.

## 9. Not done
Any decoding, any look at keys or other readers' work, any fetch of images.

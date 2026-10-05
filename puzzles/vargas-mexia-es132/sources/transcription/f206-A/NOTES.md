# f206-A: blind transcription notes (BnF Espagnol 132, ff. 206-207, 8 Jun 1579)

Reader: blind, working only from the four page images in `sources/cache/pages/exp07/` and
`CIPHER3-GUIDE.md` (v2.2). No key, no other transcription, no network. Crops were cut with `magick`
at native resolution (strips of 3 lines, left and right halves 1500 px wide, overlap about 300 px).

## Extent

One letter, Philip II to Juan de Vargas Mexia, begins at the top of f. 206r and ends on f. 207r.

- f. 206r: royal heading ("el Rey", with a small cross above it), salutation "Juan de Vargas Mexia", five
  lines of clear Spanish (acknowledging the receipt of Vargas's letters up to 1 May and listing which
  numbered letters of his are answered), then cipher: 23 lines in two paragraphs (16 + 7), each ending in a `/`.
  Folio number "206" at top right (with a "?" before it).
- f. 206v: 28 cipher lines, four paragraphs (16, 4, 3, 5 lines), each paragraph ending in a `/`. Faint show-through
  of the recto heading at the top. A small "c o" mark at the top left, outside the text block; not transcribed.
- f. 207r: 12 cipher lines (paragraphs of 5 and 7 lines). The last cipher line ends in a `/` and is followed on
  the same line by the clear place and date, "de Toledo / a viij. de Junio 1579 /". Below it, the King's
  autograph "Yo el Rey" and, lower and to the right, the secretary's countersignature. Folio number "207" top right.
- f. 207v: address leaf, text written sideways in the image (I read it after rotating the image 270 degrees). "Por el Rey" (cross above "el") and "A Juan de Vargas Mexia". A seal remnant carries a
  pasted paper slip with a few cipher-like figures, running into the gutter band: read as `28+ 12+ / 11+ 10<v> 176 76 1 /
  16 1 176`. It is recorded as a comment line only; I take it to be a fragment pasted over the seal, not part of
  the letter. Modern library label and ink stamp are not transcribed.
- Cipher lines transcribed: 63 (23 + 28 + 12). Clear text: 5 lines (206r) plus the date line, plus the two
  signatures and the address.

## Countersignature as read

"Ant. Pz." (Ant.o Perez?). The King's autograph reads "Yo el Rey" (flourished). The countersignature is "Ant."
followed by a tall looped capital (read P; B or S not excluded) and a z-shaped 3 (read z), then a dot and long
flourishes below. The identification of the person is a reading of shapes only, not something I checked.

## Passes

- Pass 1: left to right, first page to last. 46 cipher half-strips (206r 16, 206v 20, 207r 10), plus 4 crops of the
  clear Spanish on 206r, 2 right-margin crops of 206r, 3 crops of the top and bottom of 206v, 2 crops of the
  signatures on 207r, 4 views of the address leaf (207v): 61 views in all.
- Pass 2: right to left within each line, last page to first, last strip to first, right half before left half.
  All 46 cipher half-strips re-viewed in full, plus the 4 clear-text crops: 50 views. Not re-viewed in pass 2: the margin
  crops, the signature crops, the address leaf crops (each read once, in pass 1).
- Pass 2 changed many marks above (bars, hats, v's, dots) that pass 1 had dropped (about 40 additions), added the
  loop-ended bars over three signs on 206r L1, corrected the acute/grave on some digits, moved a stray "8." on 206v from
  the head of L28 to the end of L27, and changed a few splits (e.g. `16 1p`, `7 1 22+`).
- Guide note on marks above: bars are the most frequent, and many sit over a mark-after (`6+<bar>`).

## Conventions I had to choose (shapes only; the guide does not cover these)

- **q-shaped glyph written `4`.** The hand writes the digit 4 as a q with a straight descender. A free-standing
  q-shaped sign is also written `4` (very frequent, usually with a hat, bar or acute). If the cipher has a separate q-sign,
  this is a collision I cannot see.
- **Hook after a number written `p`.** The small e-shaped loop after a number or letter (`24p`, `15p`, `dp`, `Sp`, `yp`,
  `1p`) is written `p` (guide: "e with a tail"). I did not see a clear descender on most of them; if the hook
  and a letter e are different signs in the cipher, all of these are wrong in the same way.
- **9 vs 4:** g-shaped sign with a curved tail written `9`; q-shaped with a straight stem written `4`.
- **Letter forms written as letters:** `d` (a script d or delta-shaped sign, very frequent, usually `d.`), `Z` (large
  flourished Z/S-shape with a descending tail, always before "um" or "om": `Z u m`, `Z o m`), `S` (large S, in `Sp m`),
  `m`, `u`, `o`, `y`, `L`, `w` (omega-shaped, 206r L19, L22), `p` (tall-tailed letter p, often with `+` or `.`, or followed
  by `e<v>` as `p e<v>`).
- **Sign with `<cross>`:** circle with a small cross above, written `o<cross>` (206r L8, 206v L11).
- **Loop-ended bars over 19, 24, 26 on 206r L1:** a long stroke ending in a loop over each; written `<bar>`.
- **Reading `1 2 + 2 8 6 9`:** I split digit-plus-curl as `286 9`, not `2869`; same for `226 9`, `296 9`.
- The sign `6+` is written as its own token (curl with its own plus), after the previous number: `3 6+`, `18 3 6+`.

## Every 3+ digit run left joined (all are a number with a curl 6, or `176`)

`116` (207r L9), `126`, `156`, `166`, `176`, `216`, `226` (many), `236`, `246`, `256`, `286` (very many), `296`, `316` (many),
`356` (206v L21, with underline), `376` (206v L23). Joined by the curl rule, except `176` which I read as 17 plus curl, and
`166` (16 + curl, or 1 + 66; left joined). `296?` (206v L27, under blot) and `356<hat>?` (206v L2) carry a `?`.

## Places where I was unsure whether a curl is joined

- `66` (206r L13, L21, L22): number 6 plus a joined curl, or two digits.
- `3 6+` vs `36+`: written as `3` and `6+` throughout (curl carries its own plus).
- `3 66.` (206v L17), `36 1 27p` (207r L10), `246 24+` (206v L8), `5 6` (206v L15), `d 6` and `d 6 6p`
  (curl after d, written separate), `22 16` (206v L27), `1 5 6`.
- `16 1 y`, `1 1 6` runs: could be `116` or `11 6`; left as written in the file.

## Every `?` (page, cipher-line number counted from the first cipher line of the page)

- 206r: L8 `o<cross>?`; L10 `4<grave>?`; L11 `p.<v>?`; L12 `18+?`; L13 `17+?`; L15 `22.<bar>?`; L17 `5<hat>?`.
- 206v: L2 `356<hat>?`; L3 `4<acute>?`; L7 `7+?`; L8 `L?`; L9 `20.<v>?` `17?`; L10 `24+<grave>?` `4<acute>?`;
  L11 `24p<v>?`; L12 `10<v>?` `1?`; L13 `22?`; L17 `3<bar>?`; L19 `y?` `23?` (and `m 1 y?`); L21 `5<hat>?`;
  L22 `7+<bar>?` `28.<v>?`; L24 `6p?`; L25 `3?`; L27 `296?` `4<acute>?`.
- 207r: L3 `yp?`; L4 `4<v>?` `p?`; L6 `22.<bar>?`; L7 `p<under>?`.
- Clear text: `xvij?` (206r clear L4) and `contenido?` (206r clear L4): the last word before "de los" is not
  certain. Also uncertain in the clear text: whether "xy" at the end of clear line 3 is "xv" (read as written).
  The countersignature's first capital is uncertain (P, B or S).

## Every `<sign:...>`

- 206v L22: `<sign:obscured by ink blot>` between `18<v>` and `7+<bar>?` (ink spatter over the line, with other blots on
  206v L22-L27).
- 207r: the King's autograph and the secretary's countersignature (descriptions in the file).

## Every `<under>`

- 206r L21: `30.<under>` (clear underline under the 30, the only one on the recto).
- 206v L21: `356<under>` (underline under the 35 and its curl).
- 207r L7: `p<under>?` (a long stroke under the last sign of the line, possibly only the tail of a tall hook rather than an underline).
- Numbers in the 30s seen without an underline: `30.` (206v L14), `31.<bar>` (a bar above), `33+`, `34+` (206r L3; 206v L13, L17),
  `35.` (many), `36.`, `37+` (206r, 206v), `376`.

## Image problems

- 206v: black vertical band at the gutter (image x about 3310-3340) touches the right ends of many lines (not counted line by line);
  the last sign on those lines is partly hidden (flagged `?` where it matters, e.g. `286`, `p`, `16`).
- 206v L22-L27: ink spatter (dots and streaks) in the middle and right of the lines; one sign hidden (`<sign:obscured by ink blot>`).
  Some marks above in these lines may be spatter, not pen.
- 206v top: show-through of the recto heading. 206r left margin: a sliver of the facing page; 207r left: a sliver of 206v at the gutter.
- 206r and 207r edges are clean; 206r right margin has no further signs (checked in two edge crops).
- 207r: faint show-through of the verso under the signatures; the countersignature has long hair-line strokes crossing
  the first letters.
- 207v: rotated text; seal remnant with a pasted slip; library label.

## Collision note

The scratch folder `/tmp/claude-501/t1/` already existed and held files from earlier work. I did not open any file I did not
create. My crops were then moved to `/tmp/claude-501/blind-f206A/`; a few of my crops of the clear text on 206r remain in `t1`.

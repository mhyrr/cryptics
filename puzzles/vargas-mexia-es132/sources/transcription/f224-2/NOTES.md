# f224-2 transcription notes (blind reader, guide CIPHER3-GUIDE v2.2)

Scope: BnF es. 132, ff. 224r-225v. Read forward (224r -> 225v), second pass in reverse (225v -> 224r,
bottom strip to top, right half before left half).

## Extent
- f. 224r: top "Yo el Rey" (clear, large paraph), folio number "224" top right. Clear salutation and 5 clear lines,
  then 24 cipher lines. Letter starts here.
- f. 224v: 30 cipher lines, no clear text. Bottom-left docket-like note "Dup.da" (transcribed in [[ ]]).
- f. 225r: 4 cipher lines (the 4th ends with "/" and the clear place "de St Lorenço"), then the date line, the King's
  signature, the secretary's countersignature at right, and "Dup.da" bottom-left. The letter ENDS here.
- f. 225v: address leaf, not cipher. Written sideways (reads with page turned): "Por el Rey" with a cross above "el", and
  "Juan de Vargas Mexia"; docket "13 de setiembre de 1579"; "Dup.da" bottom-left. Transcribed in [[ ]]; a faint
  show-through of 225r text is visible in the upper half.
- Cipher lines: 24 + 30 + 4 = 58. Numbering below counts every non-comment output line of a page, clear lines included
  (so on 224r the first cipher line is "l.7").

## Countersignature
Read as "Don Iuº de Idiaquez" (Juan de Idiáquez), with a long paraph. The King's signature reads "Yo el Rey" with
big looped paraph; it is crowded with loops and I give only that reading.
Date line reads "(looped initial like an alpha) xiij. de Septie 1579." The first sign before the numeral is a looped
shape I took as a flourish; the numeral after it is x, a short stroke, and a y-shaped j. If that looped initial is an
x the date would read xxij; the docket on 225v reads 13, which agrees with "xiij". Treat the numeral as uncertain.
The date line is written in [[ ]] as `xiij.`; the looped initial is not transcribed.

## Conventions I used (the guide does not fix these; decide when reconciling)
- The "ð"-like letter with a flat upper stroke (very frequent, usually followed by a dot) is written `d`.
- The "e with tail" that follows a base is written as the hook `p` (e.g. `6p`, `7p`, `15p`, `dp`). Bare `p` is the
  letter p with a long descender (`p+`, `p 14`).
- The q-shaped sign with a straight descender is written `9`; the closed digit 4 is `4`. Several are doubtful.
- The large looped letter at the start of "S i m / S o m / S e m / S u m" is written `S`; the middle vowel is as seen
  and each of these words is separated by spaces (`S i m`, `S o m`, `S e m`, `S u m`). Whether they are one sign
  or three is open.
- `o<cross>` is a small round "o" with a cross above (not the digit 0). `n?` is a small letter n form.
- A "v" mark above is `<v>`; a grave or acute is as seen; long overbars spanning two signs are put on one sign.
- Line-final tails are written `<sign:flourish>` when I could not read a digit under them.
- `l` is a tall plain l (in "6p l", which looks like "bel").

## Passes
- Image prep: each page deskewed with ImageMagick (224r, 224v, 225r, 225v by +3, +1.3, +3, +3 degrees; resampled).
  Strips are about 380 px high (2-3 lines), halves 1650 px (left) and 1750 px (right) wide, overlap about 150 px, native
  scale, no downscaling (the reader may have shown them slightly reduced).
- Pass 1 (left to right, top to bottom): 224r strips 01-11 (the last two strips and 12 were blank; 13-14 viewed in
  pass 2), 224v strips 01-14 (15-18 not viewed in pass 1 beyond the overview, blank), 225r strips 01-04 (3-4 mostly
  signatures). About 29 strip pairs (58 half-strips) plus 10 extra crops for headings, signatures, address leaf.
- Pass 2 (reverse): 225v crops, 225r strips 04, 02, 01 (03 not re-viewed), 224v strips 14-01, 224r strips 14, 13, 11-01
  (12 not re-viewed). About 30 strip pairs (60 half-strips). Pass 2 is complete for every cipher line.
- Pass 2 changes: line "224v l.27" had lost "28 17+ 176 4<hat>" in pass 1 (a whole stretch missed at a strip overlap);
  duplicated "7p" on 224v l.14 removed; several hats, bars and v marks added; 224r l.13 "35p p p" corrected to "35p pp";
  "296" -> "246" on 224v l.8; "9" -> "4" on 224v l.17; first "S 1 m" readings regularized to "S i m".
- Because strips overlapped by only ~150 px and some lines continue across both halves, a duplicated or dropped sign at
  the L/R seam is the most likely error type. The seam is near x = 1900 of the deskewed page.

## Digit runs of 3+ left joined (all are number + closed curl, or number + digit with no visible gap)
Joined runs by count (file line numbers): 246, 286, 236, 166, 356, 106, 311?, 176, 256, 226, 366, 211, 216, 231, 296,
316, 156, 183, 219, 186, 376, 326, 129, 111, 116, 869, 936, 306, 1219?, 124+. Most are of the form 2+3 digits
with a 6-shaped curl (guide curl rule). The doubtful ones are: 224r l.8 "286" vs "28 6"; 224r l.29 "1219?" and
"183"; 224v l.7 "124+<bar>?"; 224v l.9 "936"; 224v l.14 "111"; 224v l.16 "111"; 224v l.18 "211<hat>?"; 224r l.12, l.9
"311<under>?". Where I was unsure the curl is joined I joined it.

## Every `?` (file line numbers; 45 in all)
224r: l.8 `1?`; l.9 `d1?`, `6?`; l.12 `311<under>?`; l.15 `d<bar>?`; l.16 `11<v>?`; l.17 `18?`; l.19 `18<bar>?`, `28<v>?`;
l.23 `17.<v>?`; l.28 `23<v>?`, `9<hat>?`; l.29 `1219?`, `11<hat>?`, `11<v>?`.
224v: l.2 `86?`; l.3 `2?` (line cut by page edge); l.7 `l<bar>?`, `124+<bar>?`; l.8 `11?`, `23?`; l.9 `311<under>?`,
`4<bar>?`, `y?`; l.10 `7?`; l.11 `n?`; l.12 `30?`; l.13 `7+<v>?`, `24+<bar>?` (this stretch is overwritten in heavier
ink); l.15 `9?`; l.16 `18<under>?`, `1<under>?`; l.17 `13+p?`, `9<bar>?`, `15p<2dot>?`; l.18 `211<hat>?`; l.19 `15+<hat>?`;
l.20 `9<hat>?`; l.21 `d1<v>?`; l.22 `6?`; l.27 `12p<under>?`; l.28 `4?<bar>`; l.29 `7?`; l.30 `22<hat>?`.
225r: l.2 `24+p?`.
Line ends cut by the right-hand edge shadow on 224v (l.2, l.3, l.7, l.9, l.10, l.13, l.16, l.19-l.21, l.28-l.30) may
have lost a sign.

## Every `<sign:...>`
`<sign:flourish>`: 224r l.7 (end "17"), 224r l.15 (end "29"), 224v l.19 and l.20 (end "7"). `<sign:two marks above>` on "7p"
224v l.14; `<sign:small marks above>` on "166" 224v l.19 (two small signs, like "25" in superscript); `<sign:small
curl above>` on "76" 225r l.1.

## Every `<under>`
Certain or fairly certain: 224r l.7 `35+`; 224r l.23 `35+` and `306`; 224v l.2 `35.`; 224v l.18 `311`; 224v l.21 `35p`.
Doubtful: 224r l.12 `311?`; 224v l.9 `311?`; 224v l.16 `18?` and `1?`; 224v l.27 `12p?` (could be a flourish or the next
line's overbar).

## Image problems
- 224r: left margin shows other writing (facing f. 223v) and a dark gutter; right edge has a fold/shadow; the cipher is
  readable. A stray hairline/ink trace crosses 224r l.12-14 near x=2600 (show-through).
- 224v: right edge has a dark band (page edge or binding) that cuts or abuts the last sign of many lines; a heavy blot
  ("X") under l.14; overwriting around "7+ 24+" in l.13; a row of dots above a sign in l.14.
- 225r: left strip is facing page; dark vertical streak in the middle is show-through of the address leaf; King's
  signature is faint and crossed by loops. 225v: dark band at the bottom of the docket crop; ink spots.
- The page bottoms of 224r, 224v and 225r are blank except "Dup.da".

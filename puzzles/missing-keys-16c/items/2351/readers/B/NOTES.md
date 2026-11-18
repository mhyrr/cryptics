# Reader B — notes on letter A (item 2351)

Rows in `A.txt` are counted from the first row after `# A`. Row numbers below use that count.
Opened: CLAUDE.md, SIGN-GUIDE.md, strips `cache/strips/A*.jpg`, and crops I made in `crops/`
(ImageMagick crop + resize only). Passes: first top-down; second bottom-up (row 27 back to row 3),
in which every row's signs were counted again on the strip before being compared with the file.
One row differed (row 11, see below), and that was settled by looking again.

## Layout: what I found against what the prompt expected
- **27 rows, not about 29.**
  - Row 1: the strips show only the bottoms of a line above "molto ..." (a large capital
    flourish and some ascenders). I took it to be the first of the three opening lines and wrote
    it as `[[?]]`, because none of it can be read in the strips.
  - Rows 2–3: the clear lines. The cipher starts near the end of row 3 (after "lasera"), as in the
    guide's worked example.
  - Front cipher: rows 4–21. That is **18 full cipher lines**, plus the cipher tail of row 3,
    which makes 19 lines that hold cipher. A10 ends at row 21 and there is nothing below it. If the
    prompt's "19 lines of cipher" means 19 lines after row 3, then one line is missing from the
    strips, or I have miscounted. I checked every band overlap: A01→A02→…→A10 each repeat the
    previous band's last line, and A07 repeats two lines (rows 13 and 14).
  - Back: rows 22–27. That is six cipher lines; row 27 is short and runs into clear words.
  - **The clear line with the date is not in A11–A13.** A13 ends with "... V.ra e ne" and a long
    curved stroke, and I can see no further line. I wrote no date row.
- In row 27 the cipher ends `7^3`. A dot follows, then the clear words. I wrote the dot as `dot`.

## Clear words (letters as I read them; abbreviations not expanded)
- Row 2: "molto ch aire se non accusero le vre de .x. portate da bastiano mandatto di". The second
  word is doubtful: it is "ch" with a tall flourish/superscript through it, and a crease runs
  through the word after it ("aire"/"aize"). "accusero" could also be "accusem". "vre" has a
  superscript stroke.
- Row 3: "costi dal R^mo di Sanseuerino alquale arriuo adi xxi Lasera ·". "R" has a superscript
  "mo". A dot comes before the first cipher sign; I did not write it.
- Row 27: "Hec plura per questa ch(e) Raccomandarmi alla Mag(ca) V(ost)ra e ne". "ch" has a
  flourish; "Mag" and "Vra" have superscripts. A long curved stroke runs under "e ne" to the edge.

## Names I made up (guide 3e)
- `bcross`: a `6`/`b` bowl whose stem rises tall and is crossed by a short bar near the top, like
  `ƀ` or a `6` with a `†` on its stem. Rows 5 (×2), 9 (doubtful), 10 (×2), 11, 14, 17, 19, 20, 21,
  23 (×2), 25. It always stands where a tall crossed stroke rises from a bowl on the line. **Do not
  confuse it with `delta`**, which bends left and has no bar.
- `h`: a tall stem from above the line that bends into a hump and then runs down below the line
  to the left, like `ɧ`. Rows 5, 13, 16, 17, 18 (first sign), 20. It may be the guide's `brace`
  drawn wide. I kept them apart because the hump is rounded, not a zigzag.
- `loop`: a tall, narrow, closed loop like an upside-down `U`, standing on the line, with its
  right side coming down to the line. Row 6 (after `r^3`) and row 7 (after `r^3`). It may be a
  large `delta`.
- `Dloop`: a tall sign with a small loop at the top left, a diagonal running down to the right,
  and a flat foot, like a rounded `Δ` or `∂`. Row 7, the 9th sign (after `L4 y?`).
- `ctop`: a `c` whose top has a flat flag to the right, like `Ϲ` or `ꞇ`. Row 5, after `r^4`. It
  could be a `t` written as `ƭ`.
- `8leg`: an `8`/`δ` loop whose right side runs down into a leg, like `ϑ` or `&`. Row 12, after
  `ttt`.
- `Li`: like the guide's `Lz`, but with a small upright stroke (`i`/`1`) in the corner of the `L`
  instead of a `z`. Row 12, after `beta`.
- `crossloop`: a large composite figure in row 17, after `8^~ dot`. It has a slanted stem with a
  foot and a top bar, and the top bar curves right and down into a hook. A long diagonal crosses
  that curve to make a large X, and there is a small dot or ring inside. **It may be two or three
  signs** (a `gamma`/`T` with a dot, then a large `x`). I wrote it as one token because the
  strokes are joined.
- `bowldot`: a large open bowl (`U`) entered from the upper left by a diagonal stroke, with a dot
  or small ring inside it. Row 16 (after `c`) and row 22 (after `beta c`).
- `dot`: a dot standing on the line between two signs, not above one. Rows 10, 11 (end), 12, 15
  (end), 17, 19, 20, 21, 23, 25, 27. It appears several times as `3 dot 4`. It may be punctuation.
- `dotdash`: a dot standing above a short flat stroke, at the end of row 22.

## Guide names used in a stretched sense
- `alpha` (often `alpha?`): I used it for a `y`-like sign whose tail loops back up to the right
  (`ȣ`, `ɣ` with a closed loop), standing alone. Where such a loop hangs from `tt`/`ttt` under one
  bar, I wrote `hash` (the guide's "#y, the tail is part of it"). In the first pass I had written
  those as `tt alpha` / `ttt alpha` and changed them. The affected tokens are: row 7 `r hash? p`
  and `s hash? 3`, row 8 `n hash?`, row 18 `q hash?`, row 23 `n hash?`. `z hash?` (rows 17, 19,
  22, 24) is a small filled `z` followed by two slanted stems under a bar that runs on from the `z`.
  The `z` may belong to the hash.
- `Q|alpha`: a round bowl whose tail crosses down to the left and then sweeps right and up. Rows
  10, 12, 19, 22, 25.
- `L4`: a tall `4` whose left stroke rises far above the line. The flat stroke usually does not
  run out to the left. Rows 5 (×2), 7, 16, 18 (×2), 20 (faint), 22, 23 (faint), 24.
- `R`: a `D`/`R` with a long tail along the line and a dot after it. I counted the dot as part of
  the `R`. Rows 5, 14, 17 (end), 19.
- `T`: a capital T with a long top bar. Row 21 (last sign, `T^5`) and row 22 (`T^.`, a dot above).
- `S?` in row 18: a large, slanting `s` with a crossbar that reaches below the line.

## Struck-out signs (left out)
- Row 4: between `7^3` and `r^4`, a long stroke cancels about five signs, roughly `z q 7 n tt`, with
  marks `3 4 5` above them (as the guide says).
- Row 18: between `x^1` and the final `3^3`, a thin continuous stroke runs through three heavily
  inked signs, roughly `alpha`, a blotted `q`/`4`, and `beta`, with a heavy dash above. **I left them
  out as struck. This is a judgement call:** the line could be paper texture and the signs
  overwritten rather than cancelled.

## Doubts by row (beyond the `?`/`|` in the file)
- Row 4: sign 1 `y?` (a 7-shape with a long tail down to the left; could be `q`). Sign 3 `t|x`. The
  mark on sign 4 is a small box shape, written `^4?` (could be `^n` or `^o`). Sign 6 `7` is a round
  `ɔ` shape. I took marks sitting between two bases to belong to the left base (`2^3 8^~`).
- Row 5: `L4?` (sign 9) has two down-strokes under one bar. `q i i bcross`: the two short uprights
  after `q` could be an `n` or an unbarred `tt`. `ttt?` is `ɛ`+`H`.
- Row 6: `flong|gamma` (sign 10) has a hook at the foot and no visible crossbar.
- Row 7: `z` (sign 2) may carry `^~`, or the stroke may be the end of a descender. `y?` (sign 8)
  has a loop. `3^3^~?`: two marks are stacked, a 3 below and a tilde above. `t^o?` is a dark blob.
  `3|z` has a flat top. `zm?` is a `ʒ` with a second leg.
- Row 8: `3^5?`: I cannot tell `^3` from `^5` here. The last sign `s?` is crossed by a long rising
  stroke, which may be a line-end flourish or a fold.
- Row 9: `alpha?` (sign 20). `i?` is a small upright inside the tail of `Q`. `bcross?` near the end
  is under a crease.
- Row 10: `q^5?` (×2), `6^1?`, and `3^3?` (the mark is 7-shaped).
- Row 11: `zm^~?`: the tilde sits between `zm` and the `6` after it, so it may belong to the `6`. A
  faint arc above the `8` that follows looks like show-through. **Second pass:** in the first pass I
  had dropped the `6` after `zm`. The recount (47 against 46) caught it, and I restored it by looking
  again.
- Row 12: `flong^e?`: the mark looks like a small `e`/`ε` with a tick to its left. `s^3?` (last
  sign): the mark is shaped like `)`.
- Row 13: `4^3?` (sign 3): the base is a 4-like stroke. `t^h?`: the mark is tall, like a small
  `h`/`k`. `D^c?`: the mark is shaped like a `C`/`ε`. `8^1?`: the tick may be the top of the brace.
- Row 14: sign 1 `?` is blotted and crossed by a crease. It is a tall upright with crossbars and a
  descender (`flong` or `hash`?). `pt^~`: the `p` and the `t` look joined.
- Row 15: `8^3? 8^3?`: the marks are `ʒ` shapes, 3 or 5. The `?` after `Q` is a tiny scribble and a
  dot inside Q's tail; it may be part of the tail. The two `alpha?` here are y-loops.
- Row 17: `hash?` (×2). Sign 5 `q` has a looped tail, like a `g`. `crossloop` (see above).
- Row 18: `beta^1?`: the tick is high and may be the end of a descender. `S?`. `i^.` has a dot above
  and to the right of the stroke.
- Row 20: `L4?` is faint, with its flat stroke running left under the `h`. `2^4`: the 2 is small but
  sits on the line.
- Row 21: `alpha?` (×2) and `A?`. The `A?` is like a capital `A` whose left leg runs far below the
  line. `z?` is small and angular, between `7` and `p`.
- **Row 22 (back, first line): a dark stain covers the first part of the line.** I estimate 14 signs
  and wrote them as bare `?`. The count is approximate, 13–15. Faint possible readings, not trusted:
  `7^4 4 ? r ? 2 ? delta r t r t ? ?`. `z|2^4`: the sign has a flat base and a curved top.
- Row 23: `z^3?`, `t^~?` (the mark is 7-shaped) and `7^4?` are at the stained edge. `s^5?`. `s^3?` is
  before `z^~`. `L4?` and `alpha?` at the line end are faint.
- Row 24: `flong^o?`: the mark is a small ring or `e`. A large `)` curve after the last `8`, running
  from the line above to the line below, is a flourish, not a sign.
- Row 25: a small comma-like stroke below the line after the second `Q` (before `4`) is left out. It
  may be the end of Q's tail.
- Row 26: `i?` is a short slanted stroke at mid-height between `x^3` and `s^5`, possibly a
  punctuation mark.

## Marks
- Marks mostly sit above and slightly to the right of their base. Where a mark was between two
  bases, I gave it to the left base, as the guide says.
- `^3` and `^5` are often hard to tell apart. Many marks have the shape `ʃ` (a slanted s-curve with
  a blob at the top). I wrote `^5` for these, and `^1` only for a straight tick.
- Marks the guide does not list: `^e?` (row 12), `^h?` (row 13), `^c?` (row 13).
- Long tails from the line above (flong, q, y) often reach the row of marks, especially in rows
  6–7, 15, 18 and 25. I did not count them.

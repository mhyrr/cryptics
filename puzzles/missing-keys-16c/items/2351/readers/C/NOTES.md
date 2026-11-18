# Reader C — letter A, notes

Pass 1 top-down. Pass 2 top-down, each line read right to left from the strips (c, then b, then a) before
comparing with pass 1. Pass 2 changed three tokens: L5 last sign (`8|sigma` → `yloop`), L8 (`8^5?` → `8^3?`),
L23 (`brace` → `brace^.?`). All other rows matched in sign count and order on the second look.

Rows below are numbered as in `A.txt` (row 1 = first row after `# A`).

## Line structure (differs from the prompt)

- A01 shows two full lines of clear words, not three. Above row 1 only the tops of tall letters and a large
  initial-like loop show at the top edge of the strip. The cipher starts near the end of the **second**
  visible line (row 2), after "adi xxi lasera".
- Front: bands A01–A10 give rows 1–20: 2 clear rows (row 2 ends in cipher), then 18 full cipher rows (3–20).
  So 19 rows contain cipher, which matches "19 lines of cipher" if row 2 is one of them. The overlaps are
  uneven: A07 repeats **two** lines of A06 (its first line is row 12), so A07 adds only row 14. Rows 13 and
  14 come from both A06/A07 and A07/A08.
- Row 20 is short (it ends about 4/5 of the way across). Nothing follows it on A10.
- Back: A11–A13 give rows 21–26. That is 6 cipher rows, and the last one (row 26) is short and runs into
  clear words.
- **The clear line with the date is not on A13.** A13 ends with row 26, and only a few tops of letters
  show at its bottom edge. So no date row is written. Total: 26 rows, not about 29.

## Conventions I settled on (apply everywhere)

- Marks usually sit a little right of their base. Where one stood between two bases I gave it to the left
  one (guide 2.2), unless it stood clearly over the right one's body.
- `^5` = slanted s-like tick ("ʃ"). `^1` = short upright tick. These two get confused easily; a slanted
  tick with a blob head I wrote `^5`.
- `^~` = small caret or arc. `^2` = a tiny "2" with a tail (rows 9, 20, 22, and `s^2?` in row 8).
  `^a` = a tiny box or "a" shape (rows 3, 12, 22). `^n` = tiny n/m.
- `7` covers both the plain 7 and a rounded reversed-c ")" shape (ↄ). I did not split them, but they may be
  different signs. The ↄ form occurs in rows 3, 4, 6, 7, 8, 11, 13, 16, 17, 18, 19, 20 and 25 (usually
  just before a `t`).
- `hash` = stems crossed by one bar, often run into a looped `y`. When the looped tail is there I counted
  it as part of `hash` (guide's "#y"), not as a separate `yloop`.
- Strokes that come down from the line above and pass through the mark row were left out (guide 2.3). Rows
  where I judged a mark-like squiggle to be such a tail: row 11 start ("ᶜ" over the flong = bottom of the
  row-10 "3"), row 12 ("ᶜ" over D = brace tail from row 11), row 13 (a "ʒ" over brace/q = flong tail from
  row 12), row 11 phi (tick over phi = tail), row 23 end (a long ")" curve = tail of the last row-22 sign).

## Names I made up (guide 3e)

| name | rows | what it looks like |
|---|---|---|
| `h` | 4, 12, 16, 19 | tall stem whose foot turns into a bowl or arch to the right and drops below the line, like ɦ or h |
| `l` | 4, 8, 24 | a tall thin upright stroke with no bar. Always a pair after a `q` and before a `bbar`: "q l l bbar" |
| `bbar` | 4, 8, 9, 10, 18, 19, 20, 22, 24 | a 6 or b whose tall stem is crossed near the top by a short bar, like ƀ or a b with "+" or "f" on top |
| `C` | 4 | a full-height open curve with a flag at the top right, bigger than `c` |
| `yloop` | 5, 6, 8, 14, 18, 20, 22, 23, 25 | a y whose tail closes into a loop at the bottom, like ɣ or an 8 with arms; sometimes it has a bar through it |
| `loopn` | 11 | a closed loop with an n-like arch joined on its right, like θn |
| `Li` | 11 | an L whose corner holds a small upright stroke (like `Lz`, but with "i" instead of z/x) |
| `cupdot` | 15 | a large cup or U open at the top with a dot inside it, the left arm entering from above |
| `tdot` | 16 | a long flat top stroke curving down at the right, crossed by a slanted stroke, with a small dot or ring under the bar |
| `jbar` | 20 | a short cross (+) whose upright goes on below the line and hooks left, like ɉ |
| `v` | 21 | a v or check-mark shape; it carries a ring above inside the right arm, written `v^o` |
| `dot` | 9, 10, 11, 14, 16, 18, 19, 22, 24, 26 | a dot standing **on the line** between signs, not raised as a mark. It occurs four times as "3^3 dot 4" (rows 9, 11, 19, 22); at line end in rows 14 and 26; inside a Q tail in rows 10 and 14 |

I also used `triangle?` (row 6) for a large Δ with one curved side, bigger than the guide's "small"
triangle, and `S?` (row 17) for a §-like S with a hook that drops below the line.

## Struck-out signs

- Row 3: one long horizontal stroke cancels about five or six signs between `7^3` and `r^4`. Under it I see
  roughly: a small "ʃ", a z-like sign with a 3/7-like mark, `q^4`, `7^1`, `n`, `tt`. All left out (this is
  the strike the guide example mentions).
- Row 17: one sign after `yloop` is blotted with heavy ink (it looks like a thick `t`), and a thick dash
  lies above `yloop` and the blot. I did **not** treat it as struck: written `t?`, with no mark. It might
  be a correction.
- Row 19: `L4?` and the `brace` after `h` are much lighter in ink than their neighbours. They might be
  faded, or erased, or struck lightly. I kept them.

## Doubts by row

- Row 1 (clear): "molto cl aire" — the word after "molto" is abbreviated, with superscripts above "c" and
  "aire", maybe "Cl.mo S.re". "accuson": the last letters are unsure. "vre": v.re with a superscript.
- Row 2 (clear): "R mo" = R with superscript "mo". Cipher: `ttt|tt` — I see three stems (the first one
  curved) under one bar; the guide example has `tt`.
- Row 3: `q|y` (first sign: a bowl with a long tail going down-left); `dash?` (a faint flat stroke between
  `t` and `7`); `3^a` (box-shaped mark); `2^3 8^~` (the 3 sits over the join of 2 and 8);
  `flong|gamma`; `t^3? y^3` (two 3-marks over t–y); `z^a`; `S^5?` (mark like ")"); `7^3` (could be `r`);
  `D` at the end is shaped like Ↄ.
- Row 4: `t^5?` (faint mark); `L4` here is an L fused with a crossed 4 (like Ⱡ#).
- Row 5: `D?` (rounded, open at the bottom right); `gamma` twice (short foot, no deep loop).
- Row 6: `triangle?`; `6^5?` (the mark is joined to the 6's rising stroke); the second `hash` has three
  stems.
- Row 7: `7^5?` (faint); `q^~?` (could be on the next sign); `5?` at the line end lies under a straight
  diagonal stroke — a crease or a pen stroke, I can't tell.
- Row 8: `s^2?`; `8^3?` (3 or 5); `Q i` (a small upright stroke sits inside Q's tail); `bbar?` (under a
  crease); `x^5` (mark could be `^1`).
- Row 9: `t^2?`; `alpha|Q` (a loop with a crossing tail like "&"). This shape recurs in rows 11, 14, 18, 21
  and 24 with the same notation.
- Row 10: `2^3` (large mark); `Q dot` at the end.
- Row 11: base `5` versus `s` (flat-top s-shape) in `5^3` and at the end (`5^3?`).
- Row 12: `4^3` (the base could be a t); `x^a?`; `t^n` (the mark is like a tiny h or n); `8^1` (a tick beside
  the top of the brace).
- Row 13: `hash?` (first sign, crossed strokes at a crease); `c?` (a small e-like loop); the `Q` tail is
  long.
- Row 14: `flong? yloop` (a tall stem with a cross-stroke low down, then a y with a bar; this might be one
  sign); `Q dot o?` (a dot and a small blob inside Q's tail); `delta^3`; the line ends in a `dot`.
- Row 15: `2^4|r^4` (a ʔ-shaped base).
- Row 16: `x?` (a large cross whose right arm ends in a hook, right after `tdot`); `z hash q` (a hash
  without a looped tail, then a q with a big loop below).
- Row 17: `brace?` (first sign); `S?`; `i^.` (a raised dot between i and s); `t?` (the blot, see above).
- Row 18: `s i` (a small s and a short upright).
- Row 19: `6^1?`; `L4?`.
- Row 20: `jbar^2?` (the mark sits between the dot and jbar); `z?` (a small z/x-like base).
- Row 21: **the start is under a dark stain.** About 14 signs before `L4?`, written
  `3? ? ? ? 2? ? ? delta? t? ? ? ? ? ?`. The count itself is uncertain (12–15). Marks are visible above
  them (4, 1, 3, ~, 3, 5, 4, ~) but I did not assign them. `T^.` (T with a dot above); `dash^.` at the end
  (a short flat stroke with a dot above).
- Row 22: `3^5?`; `2^a?`; `s^1`; the `7` before `s^3` is crossed by a tail from row 21.
- Row 23: `c?` after the first D (a small c at mid-height, maybe part of D like the R ring); `y^~?` (a
  j-like y); `brace^.?` (a dot above the brace top, separate from the `^o` of the preceding flong).
- Row 24: the `Q` tail ends in a small stroke (part of Q).
- Row 25: `y^5?` (the second of two y's, j-like); `q^1?` (the mark is crossed by a fold line).
- Row 26: clear words "nec plura per questa ch raccomandarmi alla mag vra a ne" — the first letter (N/H)
  is unsure; "ch" has an abbreviation stroke; "mag" and "vra" carry superscripts. A long flourish runs
  under "a ne" with a small x-like mark at its end. The signature and the stamped number are left out; the
  date line is not on the strips.

## Things the guide missed

- The reversed-c ")" sign (ↄ), which might be distinct from `7`.
- `h`, `l`, `v`, `C`, a dot on the line, a hash with three stems, a y with a closed loop, and a b/6 with a
  barred stem (see the table above).
- A mark shaped like a tiny "2" (rows 8, 9, 20, 22) and a box/"a" mark (rows 3, 12, 22). Both are covered
  by the guide's `^2`/`^a` rule but are not listed in its table.
- Recurring "3^3 dot 4" groups, and dots sitting inside Q tails.

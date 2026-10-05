# Cipher 3 transcription guide (v2.2, 2026-10-05)

For readers of Cipher 3 letters in BnF es. 132 (Philip II to Vargas Mexía, 1578–80). This guide fixes
**how signs are split into tokens and how marks are written**. It gives shapes only, never values. A
reader who follows it stays blind to the key.

**Why it exists.** The two first readers of f. 105 split digit groups differently: one wrote "256" where
the other wrote "6256" or "2561764". This guide is built from Tomokiyo's aligned reading of ff. 81 and 83
(`../cache/cryptiana/spanish3Dduplicates.png`) and native crops of f. 81 (canvas 78). It is the
tokenization those letters need.

## 1. What a sign looks like
Each cipher sign is one **base** followed by up to one **mark after** and any number of **marks above**.
Signs are often joined by the pen, and the joins cross word boundaries. Split at every new base,
not at pen lifts.

**Bases:**
- **Numbers.** Write the digits as seen. The numbers in this cipher run from 1 to 37. A run of three or
  more digits is two numbers written together, or a number plus a mark that looks like a digit (§2).
- **Letter forms.** A few signs are written as letters inside the cipher: `S` (a long flat-topped s), `m`,
  `y` (tailed), `L`, `T`, `u`, `n`, and others. Write the letter.

## 2. Marks after a base (write them right after the base, no space)
| Shape | Write | Look-alike to watch for |
|---|---|---|
| a plus sign or cross at mid-height | `+` | a "t" |
| a dot at the baseline or mid-height | `.` | a comma (`,` is a separator, not a mark) |
| a hook: a small loop with a descender, like a `p`, `ρ` or `e` with a tail | `p` | the digit 6 or 9 |
| a small closed curl, like a `σ`, a `6` or a `б`, joined to the number before it | `6` written joined: `256` | a free-standing digit 6 |
| a T-bar, `⊣` or `⊥`, a short horizontal stroke with a vertical | `<tbar>` | a `u` or a `t` |

**The curl rule (the one that matters most).** A 6-shaped curl that touches the number before it, or sits
closer to it than the gap between signs, and has no mark of its own, is written **joined**: `256`, `316`,
`156`. A 6 that stands apart, or carries its own dot, plus, hook or bar, is its own token: `6.`, `6+`, `6p`.
When in doubt, write it joined and add `?`. Never write a curl as a separate `6` only because it is a 6 in shape.

## 3. Marks above a base (in angle brackets, after any mark-after)
| Shape | Write |
|---|---|
| slash `/` above | `<acute>` |
| backslash `\` above | `<grave>` |
| caret `^` above | `<hat>` |
| small `v`, `˘` or hook above | `<v>` |
| horizontal bar above | `<bar>` |
| small cross `+` above (code-word marker) | `<cross>` |
| two dots above | `<2dot>` |
| one dot above | `<dot>` |

Order inside a token: base, mark after, marks above. Examples: `20p<v>`, `6+<bar>`, `25<bar>` joined with a
curl as `256<bar>`, `6.<acute>`, `15+<hat>`, `22.<2dot>`, `108<cross>`.

## 4. Everything else
- `/` is a virgula between signs (its own token). `,` is a comma (its own token).
- Clear Spanish goes inside `[[ ]]`, in diplomatic spelling.
- `?` after any token you are unsure of; `a|b` for two close readings (`24|29`).
- `<sign:description>` for any sign that is none of the above.
- One output line per manuscript line; comment lines start with `#`.

## 5. Worked example (tokens only; f. 81, first cipher line, native crop of canvas 78)
Manuscript, as written with pen joins: `28 20ρ˘ 24ρ6+‾ 12· 25σ‾24ρ`
Tokens: `28 20p<v> 24p 6+<bar> 12. 256<bar> 24p`
Three points: (1) `24ρ6+` is two signs, so it is split at the second base. (2) The curl after 25 is joined: `256`.
(3) The bar sits over the curl, but it belongs to the sign, so `256<bar>`.

## 6. Passes
1. Left to right per crop, at native resolution (no upscaling beyond 100%).
2. Independent right-to-left re-check of every line against the crops. Note what changed.
3. List in NOTES.md: every 3+ digit run you left joined, every `?`, and every place where you were unsure
   whether a curl is joined.

## 7. Addendum v2.1 (2026-10-04, after the f. 83 calibration; shapes only)
- **The digit 2 is often z-shaped** (like `ʒ`, or a `u`/`z` with a tail dropping below the line). Inside a
  number (`22`, `23`, `24`, `25`) it is still a 2. Do not write it `u`. A true `u` letter form has no tail and
  stands alone.
- **The digits 12 written together** can look like `ız` or a `u`. If the first stroke is a short upright and the
  second a z-shaped 2, write `12`.
- **Marks above are easy to drop.** Before finishing each line, re-check every sign for a bar, caret, small v,
  two dots or cross above it. Marks above often sit over the *mark after* (the curl or hook); they still belong
  to that sign.

## 8. Addendum v2.2 (2026-10-05; shapes only)
- **Underline below a sign.** A short horizontal stroke *under* a number (not a bar above, not a ruling line of the
  page) is written `<under>` after any other marks: `35<under>`, `31.<under>`, `33+<bar><under>`. Look for it on every
  number in the 30s. If you cannot tell an underline from the next line's ascender or a flourish, write `<under>?`.
- **Crop locally.** Your page images are local files. Do not fetch anything from the network. Crop strips with
  ImageMagick at native resolution, e.g. `magick PAGE.jpg -crop 1500x350+300+1200 +repage <your-crop-folder>/r05a.jpg`,
  then view the strip. A reduced overview (`magick PAGE.jpg -resize 12% overview.jpg`) helps to find the lines. Strips of
  3-5 manuscript lines read best.

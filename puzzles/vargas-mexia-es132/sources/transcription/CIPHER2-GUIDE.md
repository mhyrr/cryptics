# Cipher 2 transcription guide (v1, 2026-10-04)

For readers of Cipher 2 letters in BnF es. 132 (Philip II to Vargas Mexía, January–March 1578). This guide fixes **how
signs are split into tokens and how marks are written**. It gives shapes only, never values. A reader who follows it
stays blind to the key. Built from native crops of f. 11v (Gallica canvas 14, left page).

## 0. Images
Gallica IIIF, `https://gallica.bnf.fr/iiif/ark:/12148/btv1b10032556x/f{canvas}/{x},{y},{w},{h}/full/0/native.jpg`
(region in pixels of the full canvas; `full/1000,/0/native.jpg` gives a 1000-px overview). Fetch with Python `urllib` and a
`User-Agent: Mozilla/5.0` header (shell curl is blocked). Each canvas is an open spread of about 6,800 × 5,450 px: the left
page is roughly x 0–3,400, the right page x 3,400–6,800; the exact gutter varies, so take an overview first. Read from
native-resolution strips about 1,500 × 350 px, with the left and right halves of each line overlapping by about 150 px.

## 1. What a sign looks like
Each cipher sign is one **base**, followed by at most one **mark after**, and possibly a **mark above**. The pen often
joins signs; split at every new base, not at pen lifts. Word gaps in the cipher are visible but are not tokens.

**Bases**
- **Numbers.** The numbers run from 2 to 23 (a 1 may occur). Several digits are written in disguised shapes; write the
  digit, not the letter it looks like:
  - **5 looks like an `S`** (an S-curve, often followed by a cross: `S+` is written `5+`).
  - **9 looks like a `g`**: an open loop with a tail going down and to the left (`g` + hook is written `9e`).
  - **3 looks like a `ʒ`** or a `z` with a tail.
  - **4** is sometimes written like a `q` or `ɋ` with a stroke through the tail; write `4`.
  - **2** alone is a small `z`-like stroke; in numbers (20, 22, 23) it is still 2.
  - **11** is two upright strokes, often looking like `ll` or `ii`; **12** like `lz`; write the number.
- **Letter-forms.** A few signs are letters, not numbers. Write the letter: `f` (a long f with a descender), `p` (a p
  with a long descender), `n`, `m`, `R` (a capital R), `C` (a capital C, often with a dot above), `v` (or `U`, write `v`),
  `h`, `P` (a capital P). If a g-shaped sign is clearly not one of the page's 9s, write `g?` and describe it in NOTES.
- **Two special shapes:**
  - `<rho>`: a **large ρ**, a loop at mid-height with a long tail that drops well below the line and often curls back into
    a loop. It stands as a sign of its own (with space or after a word gap), and is bigger than the small hook below.
  - `<venus>`: a circle with a short cross or bar below it (like ♀).
- Any other sign: `<sign:short description>`.

## 2. Marks after a base (write them right after the base, no space)
| Shape | Write | Look-alike to watch for |
|---|---|---|
| a plus sign or cross at mid-height | `+` | a "t" |
| a small hook: a loop at x-height with a short tail, like a small `ρ` or `e`, joined to the sign | `e` | the large free `<rho>` (§1); a 9 |
| a dot **below** the sign | `_` | the dot above of the line below |
| a dot **above** the sign | `^` | the dot below of the line above |
| a dot to the **right**, at mid-height or baseline | `.` | a comma |

## 3. Marks above
| Shape | Write |
|---|---|
| a horizontal bar over the sign | `<bar>` |
| anything else above | `<sign:above-description>` |
Order: base, mark after, mark above. Examples: `13e`, `9e`, `5+`, `12_`, `11^`, `4.`, `2<bar>`, `13e<bar>`, `R+`, `Pe`.

**Dots are the hard part.** A dot sits between two lines and can belong to the sign above or below. Decide by distance;
if unsure, write the more likely one and add `?` (`12_?`). Do not drop dots: re-check every line for dots before moving on.

## 4. Clear text and everything else
- Clear Spanish (ordinary handwriting) goes inside `[[ ]]`, in diplomatic spelling, one `[[ ]]` per run. Clear text and
  cipher mix within lines; mark every switch.
- `/` virgula and `,` comma are their own tokens.
- `?` after any token you are unsure of; `a|b` for two close readings (`13|15`).
- One output line per manuscript line; comment lines start with `#`; mark each page with `# ===== f. NNr =====`.

## 5. Worked example (f. 11v, first cipher line; native crop of canvas 14, x 650–2150, y 1030–1360)
Manuscript: two uprights with a dot above, `16` with a cross, `12` with a cross, … an f with a dot under its stem, `20`
with a dot below, … a long p with a cross, …
Tokens: `11^ 16+ 12+ 6 18 f_ 20_ 18 18^ 6+ 6 11 6 13 p+ 19+ 13+ 17`
Points: (1) the `ll` is 11, with a dot above. (2) the `f` with a dot below it is the letter-form f with a dot below,
`f_`. (3) `p+` is the letter-form p with a cross.

## 6. Passes and notes
1. Left to right per strip, at native resolution.
2. Independent right-to-left re-check of every line against the strips. Note what changed.
3. NOTES.md: the page/canvas map you used, line counts per page, every `?`, every letter-form or special sign you used
   and where, and the hardest places.

# Cipher 1 transcription guide (v1, 2026-10-04)

For readers of the Cipher 1 letter in BnF es. 132, ff. 3r–4r (Philip II to Vargas Mexía, 16 Dec 1577). This guide fixes
**how signs are split into tokens and how they are written**. It gives shapes only, never values. Built from native crops
of f. 3r.

## 0. Images
Whole pages at native resolution are on disk: `sources/cache/pages/f003r.jpg`, `f003v.jpg`, `f004r.jpg`. **Do not fetch
anything from Gallica.** Cut strips locally with ImageMagick (`magick sources/cache/pages/f003r.jpg -crop 1500x350+600+2230
+repage <your-crop-folder>/r01a.jpg`) and view them. Overview first (`-resize 1000x`). Strips about 1,500 × 350 px,
halves of each line overlapping by about 150 px.

## 1. Signs
The cipher is written as separate groups with clear gaps. Each group is one token: a **base**, then optional **marks after**
(touching the base, at its right) and optional **marks above**.

**Bases**
- **Numbers**, mostly two digits (6 to 100). Write the digits. The 2 is often z-shaped; 4 can look like a cross; 9 can
  have a long tail; 1 is a short upright.
- **Glyphs** (not numbers). Write the label:
  | Shape | Label |
  |---|---|
  | a `v` or triangle with a small flag or tick (like ᐁ) | `<tri>` |
  | a `w` with a bar over it | `<wbar>` |
  | an open curve like `ɔ` or `c` | `<arc>` |
  | a capital `A` with a crossbar, or a cursive `a` with a long horizontal stroke through it (`-a-`) | `<abar>` |
  | a `θ` (an oval with a stroke through it; the stroke often runs out on both sides, `-θ-`) | `<theta>` |
  | an `8` or `g` with a squiggle | `<8sq>` |
  | a large `w` (no bar) | `<W>` |
  | an `ε` | `<eps>` |
  | a ♀ (circle on a cross) | `<venus>` |
  | a small rounded `ω` | `<omega>` |
  | two uprights with a bar across the top (`π`, `Π`, `II`) | `<II>` |
  | a capital `Ω` | `<Omega>` |
  | a `#` (two uprights crossed by two bars) | `<hash>` |
  Anything else: `<sign:short description>`.
- **Letter groups.** A few groups are written in ordinary letters (for example something like `hu`, `mu`, `qui`, `ges`).
  Write the letters inside braces: `{hu}`, `{mu}`. Their marks above follow as usual: `{hu}<3>`.

**Marks after (no space)**
| Shape | Write |
|---|---|
| a cross or plus sign touching the right of the base | `+` |
| a small closed curl rising from the end of the base, like `б` or a `6` | `<curl>` |
| a tail that drops below the line and hooks, like `ρ` or `ꝛ` | `<tail>` |

**Marks above (in this order after any mark after)**
| Shape | Write |
|---|---|
| one dot | `<dot>` |
| two dots | `<2dot>` |
| an arch or ∩ | `<arch>` |
| a short slanted stroke `/` | `<acute>` |
| a small x | `<x>` |
| a dot over a small hook | `<dothook>` |
| a small ω | `<om>` |
| a small digit 2 or 3 | `<2>`, `<3>` |
| a tilde ~ | `<tilde>` |
| a horizontal bar (over one group, or spanning several: put it on each group it covers) | `<bar>` |
| a small cross `+` | `<cross>` |
| a curl or loop | `<loop>` |

Examples (shapes only): `47<curl>`, `57<tail>`, `12<dot>`, `81<bar>`, `75<arch>`, `<theta><2dot>`, `{hu}<3>`, `8<2>`.

## 2. Everything else
- Clear Spanish goes inside `[[ ]]`, diplomatic spelling. The letter opens in clear and switches to cipher.
- `/` virgula and `,` comma are their own tokens. A group's "N. J." heading-like letters: write them in `[[ ]]`.
- `?` after a doubtful token; `a|b` for two close readings.
- One output line per manuscript line; `# ===== f. 3r =====` page markers; comments start with `#`.
- Marginal notes (the left margin of 3r has small faint writing) are not part of the letter: describe them in NOTES.md.

## 3. Passes and notes
1. Left to right per strip at native resolution. 2. Independent right-to-left re-check; note what changed.
3. NOTES.md: lines per page, every `?`, every `<sign:…>`, the hardest places.

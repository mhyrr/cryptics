# f123-B notes (reader B, blind)

Date of work: 2026-10-04. Blind: no repo files under the puzzle directory were opened except these two and my own crops.

## Method
- Gallica IIIF, canvas f120, right page. Overview 1000 px, then native-resolution strips 1250x450 px at y = 780, 1140, 1500, 1860, 2220, 2580 (step 360), left half x=3750 and right half x=4800 (about 200 px overlap).
- Crops in sources/cache/f123-B-crops/ (overview.jpg, s{0-5}{L,R}_y*.jpg). Strips 4-5 at y>=2580 hold only the signature.
- Pass 1 left to right on each strip; lines joined across the L/R overlap by matching shared tokens. Pass 2 right to left, re-reading each line against the crops (no PIL available, so no zoom beyond native). Changes in pass 2: line 6 reassembled (L and R strips show different halves of the same line); line 9 end confirmed to be the Sigma before line 10 starts; 10+ and 3+ crosses above assigned to lines 7 and 10 rather than the line above.

## Layout as read
15 body lines: line 1 = clear address then cipher; lines 2-14 cipher; line 15 = cipher then clear dateline. Above: "El Rey" with cross above (not transcribed). Below: "Yo el Rey" (flourished) and "Antonio Perez" (secretary).

## Date and signature
Dateline as read: "De Madrid A xx De octubre 1578." (month smudged, "octubre" with a long overline over the middle letters/year area; may be a flourish). Signature: "Yo el Rey"; "Ant(onio) Perez" below.

## Counts
Cipher tokens: 314 (my tokenization, including "/" tokens and letter-sign tokens, excluding the clear Spanish). Tokens carrying "?": 11.

## Hardest readings
- L2: leading-dash epsilon-like sign after 2H (could be a t or Sigma variant).
- L2/L4: "6+" (Cursive 6 vs c/G); the L2 instance is only "6+?".
- L3 "11_?" and L5 "14_?": dot below sits between/under strokes, attachment ambiguous.
- L4 and L7 "8?": open-topped gamma-like 8; also same in a few "y" forms.
- L6 "y/a?": the glyph before "a" looks like a y with a slash through/against it; may be y + "/" + a.
- L7 "10+" with a separate cross above the 1: recorded as 10+<cross above>?. L10 "3+" likewise.
- L8 "186 9.?": 6 and 9 touch; could be one token 1869.
- L11 "<sign:J-like with foot>?+" before 1: a J/long-s with a baseline foot, not a digit.
- 5-6 "36<cross above>" (L5): cross sits above the 3 of 36.

## Convention choices (doubt flags)
- Letter pairs written separately where a gap was visible: "c o", "q u a", "d u", "v 2", "a 3", "a 6", "p 6", "y a". They could be read as joined letter-groups (co, qua, du, ya); "qua" in particular looks like a word with a large loop Q. Possibly these are nulls or clear fragments; boundary clear/cipher uncertain there.
- The slash after "Mexia" in L1 has a dot at its foot ("/."): recorded as "/" only, dot lost.
- Comma-shaped virgulas (L8 after 19, L10 after 96, L10 end, L11 after "y 1", L12 after "9. 19", L5 after 36-cross) and tall slashes (L3, L5, L6) are all written "/". 
- Dots: "." is baseline-right dot; dot-below written "_", dot-above "^". L1 first sign is a with a grave-like accent mark, written "a^".
- Standalone g-shaped sign read as digit 9 ("9", "9+", "9."); "19" when a separate 1 stroke precedes it.
- L1 "t." and L14 "t." read as letter t; the L2 sign differs (leading dash, epsilon-like).
- "8H" (L10) and "2H" read as digit + H sign; standalone "H" in L9 and L11.

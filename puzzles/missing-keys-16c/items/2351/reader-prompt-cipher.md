You are cipher reader {READER} for item 2351. Your whole task is to transcribe one letter in cipher into a
text file, sign by sign, by shape. You are not asked what the signs mean, and you must not try to find out.
Do not spawn agents.

Work in `/Users/mhyrr/work/cryptics`. Read `CLAUDE.md` (rules 6 and 8), then all of
`puzzles/missing-keys-16c/items/2351/SIGN-GUIDE.md`.

**What you may open:** those two files; the strips `puzzles/missing-keys-16c/items/2351/cache/strips/A*.jpg`;
your own output files. Nothing else: no other strip (the `p233` and `q233` strips are forbidden), no page
image, no `readers/` folder but your own, no `work/` or `results/` folder, no key file, no notes, no web, no
git. Do not write scripts that process images, except to enlarge a part of an allowed strip with ImageMagick;
keep such crops in `crops/` under your output folder and open no crop you did not make.

**The letter.** Bands `A01` … `A13` run down the letter. Each band shows about three lines and repeats the
last line of the band before as its first line. Each band comes in thirds `a`, `b`, `c`, left to right,
overlapping by a few signs; `A<nn>-all.jpg` shows the band's whole width small, for keeping your place only.
- `A01` starts with three lines of clear words; the cipher begins near the end of the third. Write those
  three lines as rows, with the clear words in `[[ ]]`.
- `A01`–`A10` are the front of the sheet: after the three opening lines, 19 lines of cipher.
- `A11`–`A13` are the end of the letter on another image: 6 lines of cipher, the last one short and running
  into clear words, then a clear line with the date. Write the clear closing as `[[ ]]` rows. Leave out the
  signature and the stamped number.
- So expect about 29 rows. Report what you find if it differs.
The strips are grey and enlarged four times. The marks above the signs are small: enlarge where you doubt.

**Passes.** First pass top-down. Second pass, independent: reader A top-down again; reader B from the last
line to the first; reader C top-down, reading each line from right to left. You are reader {READER}. Look at
the strip again before you look at what you wrote, count the signs of each line again, and settle
differences by looking again. Count the signs in each overlap twice so none is dropped or doubled.

**Write** in `puzzles/missing-keys-16c/items/2351/readers/{READER}/`: `A.txt` (first row `# A`, then one
manuscript line per row) and `NOTES.md` (every doubt with its line, every name you made up with a
description, struck-out signs, anything the guide missed).

**Final message:** the file path; rows; tokens per row; how many tokens carry `?` or `|`; names you made up.
Do not include the transcription.

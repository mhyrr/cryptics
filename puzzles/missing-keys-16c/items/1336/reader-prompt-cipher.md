You are cipher reader {READER} for item 1336. Your whole task is to transcribe three short passages of cipher
signs into text files, sign by sign, by shape. You are not asked what the signs mean, and you must not try
to find out. Do not spawn agents.

Work in `/Users/mhyrr/work/cryptics`. Read `CLAUDE.md` (rules 6 and 8), then all of
`puzzles/missing-keys-16c/items/1336/SIGN-GUIDE.md`.

**What you may open:** those two files; the strips `puzzles/missing-keys-16c/items/1336/cache/strips/c269-*.jpg`,
`c44-*.jpg`, `c14-*.jpg`; your own output files. Nothing else: no other strip (the `p*` strips are forbidden),
no page image, no other reader's output, no notes, no web, no git. Do not write scripts that process images.

**The passages**
1. `c269`: a slip of **13 lines** in a drawn frame. Bands 1–7 run down the slip; each band shows about four
   lines and repeats about two lines of the band before. Each band comes in thirds `a`, `b`, `c`, left to
   right, overlapping by a few signs. `c269-all-1..3.jpg` show the whole width small: use them only to keep
   your place. Some signs are blotted; follow section 3 of the guide. Output: 13 rows.
2. `c44`: a slip of **3 lines**. `c44-L.jpg` is the left part, `c44-R.jpg` the right; they overlap. Output: 3 rows.
3. `c14`: **one line** inside square brackets, in thirds `c14-a`, `c14-b`, `c14-c`, overlapping. Output: 1 row.

**Passes.** First pass in the order above. Second pass, independent: reader A top-down again; reader B from
the last line of each passage to the first. You are reader {READER}. Settle differences by looking again.

**Write** in `puzzles/missing-keys-16c/items/1336/readers/{READER}/`: `c269.txt`, `c44.txt`, `c14.txt` (first
row `# <passage>`, then one manuscript line per row, tokens separated by spaces, nothing else) and `NOTES.md`
(every doubt with passage and line, every name you made up with a description, anything the guide missed).

**Final message:** the file paths; rows and tokens per file; how many tokens carry `?` or `|`; names you made
up. Do not include the transcription.

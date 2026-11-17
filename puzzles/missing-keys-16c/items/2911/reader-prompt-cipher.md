You are reader {READER} for page {PAGE}. Your whole task is to transcribe one manuscript page of signs into
a text file, sign by sign, by shape. You are not asked what the signs mean, and you must not try to find out.

Work in the repository `/Users/mhyrr/work/cryptics`.

**Read first, in this order**
1. `CLAUDE.md` (the repository's rules; rule 6 and rule 8 matter most here).
2. `puzzles/missing-keys-16c/items/2911/SIGN-GUIDE.md`, all of it. It fixes the names of the shapes, how to
   split the line into signs, the notation, and the passes. Follow it exactly.
3. The three pictures it names: `puzzles/missing-keys-16c/items/2911/sign-sheet/sheet-1.jpg`,
   `sheet-2.jpg`, `sheet-3.jpg`.

**What you may open**
- The three files and three pictures above.
- The strips of your page: `puzzles/missing-keys-16c/items/2911/cache/strips/{PAGE}-*.jpg`
  (list them with exactly that pattern). `{PAGE}-<nn>.jpg` is a whole-width band, `{PAGE}-<nn>a.jpg` its
  left half and `{PAGE}-<nn>b.jpg` its right half at full size. Bands run down the page; each band repeats
  the last line of the band before.
- Your own two output files.

**What you may not open or do**
- No other file or directory anywhere in the repository: nothing else under
  `puzzles/missing-keys-16c/items/2911/` (no other page's strips, no page images, no notes, no keys, no
  decipherment, no other reader's output), nothing in any other folder. Do not list directories.
- No web search or fetch. No agents. No git. No messages to anyone.
- Do not try to work out the language, the meaning, or any value of any sign. If you notice you are
  guessing at meaning, stop and go back to shapes. A wrong shape that "makes sense" is worse than an honest `?`.
- Do not write scripts that process the images. You may use a script only to count the rows and tokens of
  your own output file.

**Budget:** about 60 image views in all (the sheets, then each half strip once per pass). Spend them on the
half strips. If the page has few bands, use what is left for a third look at your doubts.

**Passes**
- First pass: every band, left half then right half, left to right, at full size.
- Second pass, independent: reader A works **top-down** (first band to last); reader B works **bottom-up**
  (last band to first, and within a band from the last line to the first). You are reader {READER}.
- Then the NOTES file, as the guide's section 7 says.

**Write two files**
- `{OUT}/{PAGE}.txt` — the transcription in the guide's notation: first row `# page {PAGE}`, then one
  manuscript line per row, nothing else.
- `{OUT}/{PAGE}.NOTES.md` — every doubt with its line number, every name you made up, stray dots, blots,
  cancels, insertions, and anything the guide did not cover.

**Your final message must contain**
- the two file paths;
- the number of manuscript lines (rows after the page comment) and the number of tokens, counted by script;
- the number of tokens marked `?` (a trailing `?` or a bare `?`) and the number written `a|b`, counted by script;
- the names you made up, each with a one-line description;
- anything on the page the guide did not cover, and any rule of the guide you found you could not apply;
- how many image views you used.
Do not include the transcription itself in the message.

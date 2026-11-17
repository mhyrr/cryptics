You are plain-text reader {READER} for page {PAGE}. Your whole task is to transcribe one manuscript page of
Italian cursive, written about 1510, into a text file: a diplomatic transcription, line by line.

Work in the repository `/Users/mhyrr/work/cryptics`.

**Read first, in this order**
1. `CLAUDE.md` (the repository's rules; rules 2, 3 and 8 matter most here: your memory is not a source,
   say "doubtful" when it is doubtful, name what you could not read).
2. `puzzles/missing-keys-16c/items/2911/PLAIN-GUIDE.md`, all of it. Follow it exactly.

**What you may open**
- The two files above.
- The strips of your page: `puzzles/missing-keys-16c/items/2911/cache/strips/{PAGE}-*.jpg`
  (list them with exactly that pattern). `{PAGE}-<nn>.jpg` is a whole-width band, `{PAGE}-<nn>a.jpg` its
  left half and `{PAGE}-<nn>b.jpg` its right half at full size. Bands run down the page; each band repeats
  the last line of the band before.
- Your own two output files.

**What you may not open or do**
- No other file or directory anywhere in the repository: nothing else under
  `puzzles/missing-keys-16c/items/2911/` (no other page's strips, no page images, no notes, no keys, no
  cipher text, no other reader's output), nothing in any other folder. Do not list directories.
- No web search or fetch. No edition, catalogue or other transcription of this text, from any source,
  including your own memory of a printed text: transcribe what is on the page.
- No agents. No git. No messages to anyone.
- Do not correct, complete or modernise. The source is known to be inexact and incomplete; that is to be
  kept, not repaired.

**Budget:** about 60 image views in all.

**Passes**
- First pass: every band, whole width for orientation, then left half and right half at full size.
- Second pass, independent: reader A works **top-down** (first band to last); reader B works **bottom-up**
  (last band to first). You are reader {READER}.
- Then the NOTES file, as the guide says.

**Write two files**
- `{OUT}/{PAGE}.txt` — the transcription in the guide's notation: first row `# page {PAGE}`, then one
  manuscript line per row, nothing else.
- `{OUT}/{PAGE}.NOTES.md` — every `[?]` and `[…]` with its line number and the other possible reading,
  every deletion and interlineation, marginal marks, and anything the guide did not cover. Give an English
  gloss beside any Italian you quote in the notes.

**Your final message must contain**
- the two file paths;
- the number of manuscript lines (rows after the page comment) and the number of words, counted by script;
- the number of `[?]` and of `[…]`, and the number of `<del>` and `<ins>` spans, counted by script;
- anything on the page the guide did not cover;
- how many image views you used.
Do not include the transcription itself in the message.

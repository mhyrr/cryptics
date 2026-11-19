You are cipher reader {READER} for item 1336, leaf c. 652r. Your whole task is to transcribe the cipher signs
on **two lines** of one page, lines 6 and 7, into a text file, sign by sign, by shape. You are not asked what
the signs mean, and you must not try to find out. Do not spawn agents. Nothing leaves the machine: no web.

(Brief made 2026-11-19 from `reader-prompt-c652.md` and `reader-note-c652.md`, for the guide's revision 2.
Readers: N and O.)

Work in `/Users/mhyrr/work/cryptics`. Read `CLAUDE.md` (rules 6 and 8), then all of
`puzzles/missing-keys-16c/items/1336/SIGN-GUIDE-r2.md`. Its section 6 (revision 2) overrides the earlier
sections where they differ, and section 5 overrides sections 1 to 4. Use the names in that guide only.

**What you may open:** those two files; the strips of your two lines,
`puzzles/missing-keys-16c/items/1336/cache/strips652/c652-06a.jpg`, `c652-06b.jpg`, `c652-06c.jpg`,
`c652-06-all.jpg`, `c652-07a.jpg`, `c652-07b.jpg`, `c652-07c.jpg`, `c652-07-all.jpg`; the strips the guide
names as examples (`cache/strips652/c652-04b.jpg`, `c652-04c.jpg`, `c652-05a.jpg`, `c652-05c.jpg`,
`c652-12a.jpg`, and `cache/strips/c44-L.jpg`, `cache/strips/c14-c.jpg`), only to see the example shapes;
your own output files. Nothing else: no other strip (the `p652` strips are forbidden), no page image, **no
`readers/` folder but your own** (other readers have transcribed these lines; do not look), no `work/` or
`results/` folder, no key file, no notes, no `rename-r2.tsv`, no README or READING, no git. You may enlarge
a part of an allowed strip with ImageMagick; keep such crops in `crops/` under your output folder and open
no crop you did not make.

**The page.** A memorandum in clear Italian with runs of cipher signs inside eight of its lines (4, 5, 6, 7,
8, 10, 11, 12). You transcribe **lines 6 and 7 only: two rows, no more.** For each line there are thirds
`c652-<line>a`, `b`, `c` (left to right, overlapping by a few signs) and `c652-<line>-all.jpg` (the whole
line, smaller, for keeping your place and for counting the overlaps). A strip shows the edges of the lines
above and below: transcribe only the line in the middle. Tails of line 5 hang into the top of the line 6
strips, and tails of line 6 into the top of the line 7 strips: they are not signs of your line. A pale
watermark in large letters crosses the left third of both lines: it is not ink. Some signs have a stroke
under them, a dash joining them, or a tick over them: apply section 6 of the guide, and describe each stroke
in NOTES.

**What to write.** Two rows, line 6 then line 7. Signs as tokens separated by spaces, always in
left-to-right order, whichever way you read. Dots and commas between signs are tokens (`.` `,`), as section
6.3 says; strike stretches are marked as section 6.4 says. Where clear Italian words stand in the line,
write `[[clear]]` once for each unbroken stretch of clear words, so the row shows where the cipher runs
start and stop; do not transcribe the clear words. If a line has no clear words, write no `[[clear]]`.

**Passes.** Two passes, independent, each in a different direction.
- Reader N: first pass, line 6 then line 7, each line read **left to right**. Second pass, line 7 then
  line 6, each line read **right to left**.
- Reader O: first pass, line 7 then line 6, each line read **right to left**. Second pass, line 6 then
  line 7, each line read **left to right**.

You are reader {READER}. **As soon as the first pass is done, write it to `pass1.txt` and do not change that
file again.** Then run the second pass from the strips, without looking at `pass1.txt`, and write it to
`pass2.txt`. Only then compare the two: for each difference, look at the strip again (enlarge it), and
settle by looking, not by choosing between your files. Count the signs of each line again, and count the
signs in each overlap of the thirds twice. Write the settled rows to `c652-67.txt`.

**Write** in `puzzles/missing-keys-16c/items/1336/readers/{READER}/`:
- `pass1.txt`, `pass2.txt` and `c652-67.txt`, each with first row `# c652 lines 6-7`, then exactly two rows
  (line 6, line 7);
- `NOTES.md`: every doubt with its line and its position (count signs from the left), every stroke under,
  through or over signs and which signs it touches, every place where the two passes differed and how you
  settled it, every name you made up with a description (check section 6.5 first), and anything the guide
  missed.

**Final message:** the folder path; signs per row in `c652-67.txt` (count `.` and `,` separately from
signs; do not count `[[…]]` markers); how many tokens carry `?` or `|`; how many positions differed between
pass 1 and pass 2; names you made up. Do not include the transcription.

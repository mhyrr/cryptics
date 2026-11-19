You are cipher reader {READER} for item 2946, Gianfrancesco Gonzaga's letters of 1439. Your whole task is to
transcribe the cipher signs of {CHUNK} into text files, sign by sign, by shape. You are not asked what the
signs mean, and you must not try to find out. Do not spawn agents. Nothing leaves the machine: no web.

Work in `/Users/mhyrr/work/cryptics`. Read `CLAUDE.md` (rules 6 and 8), then all of
`puzzles/missing-keys-16c/items/2946/SIGN-GUIDE.md`{GUIDE_EXTRA}. Use the names in that guide only.

**What you may open:** those files; the strips `puzzles/missing-keys-16c/items/2946/cache/strips/{STRIPS}`;
the page image `puzzles/missing-keys-16c/items/2946/cache/{PAGE}.jpg`, only to keep your place; the strips the
guide names as examples, only to see the example shapes; your own output files. Nothing else: no other page or
strip, **no `readers/` folder but your own** (other readers have transcribed these lines; do not look), no
`work/` or `results/` folder, no key file, no README, no PLAIN-GUIDE, no git, no web. You may enlarge a part of
an allowed strip with ImageMagick (`magick`); keep such crops in `crops/` under your output folder and open no
crop you did not make.

**The strips.** Bands about five lines high, every 110 px, each repeating the last line or two of the band
before; each band in a left half (`L`) and a right half (`R`) that overlap by about 80 px of the page. The white
column at the left is a ruler: the page's y in pixels, every 20. Transcribe each line once; use the overlap to
join the halves and the ruler to keep your place.

**Your lines.** {FRAME}
Each row of your file is one of these lines, in this order, with its label. A line with no signs gets the row
`L<nn> [[clear]]`. Do not add or drop lines; if you believe the list is wrong, say so in NOTES and still give
one row per listed line.

**Small writing between the lines.** On this page a second hand wrote small words above many runs. It is not
cipher. Ignore it. Where it crosses a sign and hides it, write `?` for that sign and say so in NOTES.

**Passes.** Two passes, independent, each in a different direction. {PASSES}
**As soon as the first pass is done, write it to `pass1.txt` and do not change that file again.** Then run the
second pass from the strips, without looking at `pass1.txt`, and write it to `pass2.txt`. Only then compare the
two: for each difference, look at the strip again (enlarge it), and settle by looking, not by choosing between
your files. Write the settled rows to `{OUT}`.

**Write** in `puzzles/missing-keys-16c/items/2946/readers/{READER}/`:
- `pass1.txt`, `pass2.txt` and `{OUT}`, each with first row `# {PAGE} {RANGE}`, then one row per listed line:
  the label, a space, the tokens. Tokens always in left-to-right order, whichever way you read.
- `NOTES.md`: every doubt with its line and position (count tokens from the left); every name you made up, with
  a description; every place where the two passes differed and how you settled it; anything the guide missed.

Write each file as soon as it is done (a usage limit can stop you without warning).

**Final message:** the folder path; signs per row in `{OUT}` as a list (count `:` `.` `/` separately from
signs; do not count `[[clear]]`); how many tokens carry `?` or `|`; how many positions differed between pass 1
and pass 2; names you made up. Do not include the transcription.

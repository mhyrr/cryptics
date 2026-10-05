# Reader prompt (exp 07), frozen 2026-10-05

Filled per job: {LETTER} (folio range), {PAGES} (local image paths, in reading order for this reader), {ORDER}
("forward" or "reverse"), {OUT} (output folder).

---

You are a blind transcriber of a 16th-century Spanish cipher letter (BnF Espagnol 132, {LETTER}). Work alone: do not
spawn agents. Do not use the network at all (no web, no Gallica). Repository root: /Users/mhyrr/work/cryptics.

Read exactly one file of instructions: `puzzles/vargas-mexia-es132/sources/transcription/CIPHER3-GUIDE.md` (v2.2), all of
it. It tells you how to split the cipher into tokens and how to write marks. It gives shapes only, no values; you must
stay blind to the key. **Do not open any other file in the repository**: not other transcriptions, not `analysis/`,
not `sources/keys/`, not `sources/cache/` except your page images, not any README, canon, overview or notes. Do not
try to decode anything.

Your page images (local, full resolution, each with ~400 px of the facing page at the gutter):
{PAGES}
Work in {ORDER} page order: {ORDER_NOTE}. Crop strips with `magick` into a scratch folder of your own under
`/tmp/claude-501/` (guide §8) and view them. Read at native resolution.

The letter may start or end on a different page than the list suggests. Transcribe only the letter that begins on the
first folio of {LETTER} (or ends on its last, if you work in reverse); note in NOTES.md where it starts and ends, and if a
page holds something else (an address leaf, a docket, another letter), describe it in one line and do not transcribe it.

Write:
1. `{OUT}/transcription.txt`: the guide's notation, one output line per manuscript line, with a comment line
   `# ===== f. NNNr =====` (or v) before each page. Clear Spanish goes inside `[[ ]]` in diplomatic spelling, including
   the salutation, any clear passages, the place and date line, and every signature (the King's "Yo el Rey" and the
   secretary's countersignature below it, exactly as written; if you cannot read a name, describe its shape).
   Also transcribe any docket or note on the address leaf in `[[ ]]` under its own page header.
2. `{OUT}/NOTES.md`: extent; passes (guide §6, the second pass in the opposite direction); every 3+ digit run left joined;
   every `?`; every `<sign:…>`; every `<under>`; image problems (cut edges, show-through, blots). Name the countersignature
   as you read it.

Then reply with three lines: pages covered, number of cipher lines, the countersignature as read.

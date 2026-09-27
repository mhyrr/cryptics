# Instructions for dictionary readers (experiment 26)

You read entries of a German dictionary printed in Frankfurt in 1595/1596.
Each entry opens with a German headword printed centred in black letter
(Fraktur). The entry gives Latin equivalents, then Hebrew words in Hebrew
type, each followed by a transliteration in Latin letters, then Greek
(after "Græc."), then French (after "Gallic."). Some entries add a
"POETICE" section with Latin epithets.

You receive a worklist and crop images. Open only the crops named in your
worklist. Do not search the web, do not open any other file, and do not
start other agents. Another reader reads the same crops; do not look for
their work.

## Task

Each worklist item names one crop (one or two image parts) and the OCR's
reading of its headword, which may be wrong. The entry to read begins at the
headword line near the top of part 1. If there is a part 2, it is the
continuation of the same column (the top of the next column). Read only that
entry, down to the next centred headword.

Transcribe literally, as printed:

1. `headword_printed`: the headword line.
2. `hebrew`: every word in Latin letters printed beside Hebrew type (the
   transliterations), in order. Do not transcribe the Hebrew type itself.
3. `greek`: every Greek word, in Greek letters, with accents and breathings
   as printed. Expand a ligature into the letters it stands for.
4. `latin`: every Latin word or phrase given as an equivalent of the
   headword. Skip labels (C., Inde, Item, Græc., Gallic.), the French forms,
   the POETICE section and example sentences.

Rules:

- Write long s (ſ) as s. Keep accents that are printed (é, á).
- Join a word broken across a line with a hyphen, and say so in `note`.
- Put `?` in place of any letter you are not sure of. Never guess a letter.
- No normalization, no spelling correction, no knowledge of Hebrew, Greek or
  Latin used to fill a letter the print does not show.
- If the named entry is not in the crop, set `entry_found` to false.
- If the entry continues past the bottom of the last part, set `truncated`
  to true.

You may zoom by cropping the image yourself; save zooms only in your own
folder.

## Output

Write one JSON file, `readings-<batch>-<A or B>.json`, in your own folder:

```json
{"reader": "<batch>-<A or B>",
 "items": [
  {"crop": "e0001", "headword_printed": "<as printed>", "entry_found": true,
   "hebrew": ["<transliteration 1>", "<transliteration 2>"], "greek": ["<Greek word>"],
   "latin": ["<Latin word or phrase>"], "truncated": false, "note": ""}
 ]}
```

One item per worklist crop, in worklist order.

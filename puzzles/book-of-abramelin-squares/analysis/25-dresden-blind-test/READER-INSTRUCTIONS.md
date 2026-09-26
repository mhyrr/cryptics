# Reader instructions — experiment 25

You transcribe letter grids from a 17th-century German manuscript
(Mscr.Dresd.N.111, Book IV). Another reader transcribes the same grids
independently. Your two transcriptions are compared cell by cell. Accuracy
matters more than completeness: an honest `?` is better than a guess.

## What you may open

Only the crop images and full-page images listed in your worklist, and this
file. Open nothing else in the repository: no other reader's output, no
experiment, no transcription, no edition, no prediction. Do not use anything
you remember about the Book of Abramelin, its squares, or any printed
edition. Many grids look symmetric or contain word-like rows; **write what the
manuscript shows, even when it breaks a pattern.** Never complete or correct
a grid by symmetry, by a word you recognise, or by what "should" be there.

## Finding the grid

Each worklist entry gives a crop, the full page it was cut from, the grid's
short heading and item number, and its position (column, top-to-bottom
index). A crop may also show parts of neighbouring grids; transcribe only the
grid under the named heading. If the crop cuts the grid off, read it from the
full page and set `crop_ok` to false.

## Transcription rules

- One string per grid row, top to bottom, letters left to right.
- Uppercase Latin letters A–Z only. Write each letter as its modern capital:
  long s (ſ) → `S`; keep I and J as written; keep U and V as written;
  ÿ or y → `Y`; w → `W`.
- `?` for a letter you cannot read with confidence. One `?` per cell.
- `.` only for a cell that is explicitly empty in the manuscript.
- Keep uneven rows uneven. Do not pad or trim to make a square.
- In `uncertain`, list each `?` or doubtful cell as
  `"r<row>c<col>: <what it might be>"` (1-based), for example `"r3c4: C or E"`.
  Put your best reading in the grid only if you are confident; otherwise `?`.

## Output

Write one JSON file to the path given in your task:

```json
{"reader": "A", "reader_model": "<your model name>", "batch": "<batch id>",
 "items": [{"locator_id": "p246-c1-g1", "rows": ["ABCDE", "B?..."],
            "complete": true, "crop_ok": true,
            "uncertain": ["r2c2: C or E"], "note": ""}]}
```

Every worklist entry must appear once in `items`. If a grid is unreadable,
give `rows: []` and explain in `note`.

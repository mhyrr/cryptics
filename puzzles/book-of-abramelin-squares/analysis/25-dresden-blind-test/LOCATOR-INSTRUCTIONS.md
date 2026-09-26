# Locator instructions — experiment 25

You locate letter grids on pages of a 17th-century German manuscript
(Mscr.Dresd.N.111, Book IV). You do **not** transcribe the letters inside any
grid. Your output fixes which grid is which, so that two later readers can be
compared cell by cell.

## What you may open

Only the page images named in your task, plus the one context page before
them. Open nothing else in the repository: no other experiment, no
transcription, no prediction, no edition. Do not use anything you remember
about the Book of Abramelin or its squares.

## Page layout (learned from the three pages before this cohort)

- Pages have up to three columns. Items run **down column 1, then down
  column 2, then down column 3**. Count columns left to right on the page.
- A chapter heading looks like "Lib: IV. Cap: 5." followed by a title. The
  book stays IV; the chapter number changes. A chapter can start mid-column.
- Each grid has a short heading with its item number ("3." or "3. In der
  lufft."). Item numbers restart at 1 in each chapter.
- A chapter can continue from the previous page without a new heading. Use
  the context page to know which chapter is running at the top of a page.

## What to record, per page

- `physical_page`, `page_label` (from your task), `content`: one of
  `grids`, `no grids`, `mixed`. Describe any non-grid content in `note`
  (for example a list of names, prose, a blank page, the end of Book IV).
- `headings`: every chapter heading on the page, as written (keep the
  spelling), with its column and rough position.
- `grids`: every letter grid, in traversal order, each with:
  - `locator_id`: `pPPP-cC-gG` — physical page (3 digits), column counted
    left to right, grid counted top to bottom in that column.
  - `book` (4), `chapter` (integer), `item` (the integer written in the
    grid's short heading, or null if you cannot read it).
  - `chapter_basis`: `heading on this page` or `continued from previous page`.
  - `short_heading`: as written, spelling kept. Uncertain words in [a/b].
  - `bbox`: `[x0, y0, x1, y1]`, fractions of image width and height, origin
    top-left. It must contain the whole grid **and** its short heading. Err
    larger rather than smaller; the crop will add a margin, but a cut grid
    is useless.
  - `rows`, `columns`: how many rows and how many letters per row you see.
    If rows have different lengths, give `columns` as a list of lengths.
  - `note`: anything unusual (grid split across columns, cut by the page
    edge, crossed out, a grid without an item number, a second numbering).

If a grid continues onto the next page, locate each part on its own page and
say so in both notes.

## Output

Write one JSON file to the path given in your task:

```json
{"locator_model": "<your model name>", "batch": "<batch id>",
 "context_page": {"physical_page": 245, "running_chapter_at_bottom": 4, "last_item": 4},
 "pages": [{"physical_page": 246, "page_label": "243", "content": "grids", "note": "",
            "headings": [{"text": "Lib: IV. Cap: 5. ...", "column": 1, "position": "middle"}],
            "grids": [{"locator_id": "p246-c1-g1", "book": 4, "chapter": 4, "item": 5,
                       "chapter_basis": "continued from previous page",
                       "short_heading": "5. ...", "bbox": [0.05, 0.08, 0.34, 0.31],
                       "rows": 6, "columns": 6, "note": ""}]}]}
```

Check before you finish: item numbers within a chapter should rise by one;
if they skip or repeat, say where in the page `note`. Do not fix numbering
to make it look regular; record what is written.

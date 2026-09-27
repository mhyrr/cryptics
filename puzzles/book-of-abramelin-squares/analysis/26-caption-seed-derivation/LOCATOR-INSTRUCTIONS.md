# Instructions for locators (experiment 26)

You find entries in a German dictionary printed in Frankfurt: volume
`bsb11762465` (1596, headwords A–S) and volume `bsb10314207` (1595, T–Z).
Headwords are German, printed centred in black letter (Fraktur) above each
entry, roughly in alphabetical order, two columns per page. Each column has a
two-letter running head at the top (for example "Lo").

Your folder holds a worklist, the two tables of contents `toc-*.tsv` (per
scan and column: running head, and the first and last headword as an OCR
read them, often with errors) and `fetch_scan.py`. Open nothing outside your
folder, do not search the web, and do not start other agents.

## Task

For each worklist item you get a German headword, its volume and a starting
bracket of five scans. Find the entry whose headword is that word, allowing
for 16th-century spelling: v/u, w/u (Bawm), i/j/y, th/t, ck/k, dt/t, a dropped
h (Lerer), doubled letters, a final e, umlauts written as e. A headword line
may print several words separated by "/"; the entry counts if one of them is
the word. The dictionary's order follows its own spelling and is loose in
places, so use the tables of contents to choose pages beyond the bracket.

Fetch a page with `python3 fetch_scan.py <volume> <scan> small` (overview) or
without `small` (full resolution), run inside your folder, and view the image.
Look at no more than about ten pages per headword.

Record, for each item:

- `found`: true or false;
- `volume` and `scan` of the page where the headword line is;
- `column`: 1 (left) or 2 (right);
- `y`: the vertical position of the headword line as a fraction of the page
  height, to two decimals (measure on the full-resolution image);
- `headword_printed`: the headword line as printed (long s as s);
- `note`: one line, for example "Ga–Ge checked, word absent" or "printed as a
  subheading inside the entry X".

If you do not find the word, record `found: false` and what you checked. Do
not transcribe anything else from any entry.

## Output

Write one JSON file, `locations-<your id>.json`, in your folder:

```json
{"locator": "<your id>",
 "items": [{"headword": "<as in worklist>", "found": true, "volume": "bsb11762465",
            "scan": 1234, "column": 2, "y": 0.41, "headword_printed": "<as printed>", "note": ""}]}
```

One item per worklist headword, in worklist order.

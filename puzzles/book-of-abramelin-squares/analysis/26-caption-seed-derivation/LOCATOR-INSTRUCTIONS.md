# Instructions for locators (experiment 26)

You receive a worklist and full-page images of a German dictionary printed
in Frankfurt in 1595/1596. Headwords are German, printed centred in black
letter (Fraktur) above each entry, in alphabetical order, two columns per
page. Open only the images named in your worklist. Do not search the web and
do not start other agents.

## Task

For each worklist item you get a German headword and three page images that
bracket its alphabetical position. Find the entry whose headword is that
word, allowing for 16th-century spelling (v/u, w/u, i/j/y, th/t, ck/k,
doubled letters, a final e, umlauts written as e or as a small e above).
A headword line may print several words separated by "/"; the entry counts
if one of them is the word.

Record, for each item:

- `found`: true or false;
- `scan`: the scan number of the image where the headword line is;
- `column`: 1 (left) or 2 (right);
- `y`: the vertical position of the headword line as a fraction of the page
  height, to two decimals;
- `headword_printed`: the headword line as printed (long s as s);
- `note`: one line, for example "range covers Ga–Ge, word absent" or
  "printed as a subheading inside the entry X".

If the word is absent from the three pages, record `found: false` and the
alphabetical range you saw. Do not transcribe anything else from the entry.

## Output

Write one JSON file, `locations-<your id>.json`, in the folder you are given:

```json
{"locator": "<your id>",
 "items": [{"headword": "Wittfrau", "found": true, "scan": 1234, "column": 2,
            "y": 0.41, "headword_printed": "Witfraw.", "note": ""}]}
```

Use a zoom of your own if needed, saved only in your own folder.

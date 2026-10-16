# analysis/

One subfolder per experiment: `NN-short-name/` with its own `README.md`
stating the question, the method, how to run it, and the result. Heavy
outputs go in `out/` (gitignored); check in a summary. If the experiment
needs more than the standard library, it gets a `pyproject.toml` here and is
run with `uv run`.

| # | Experiment | Question | Result | Bears on |
|---|---|---|---|---|
| 01 | download | Fetch Barb.lat.6960 from DigiVatLib | 194 canvases, ~700 px/page microfilm | H1–H3 |
| 02 | key-check | Does the 1628 Pallotto key read 1629? | One line aligns with Kiewning Nr. 153 (19/22 groups in key); one reader | H1 |
| 03 | bav-survey | Which DigiVatLib volumes hold undeciphered cipher? | None found online without a decipherment or solution | scope |

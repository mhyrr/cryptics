# analysis/

One subfolder per experiment: `NN-short-name/` with its own `README.md`
stating the question, the method, how to run it, and the result. Heavy
outputs go in `out/` (gitignored); check in a summary. If the experiment
needs more than the standard library, it gets a `pyproject.toml` here and is
run with `uv run`.

| # | Experiment | Question | Result | Bears on |
|---|---|---|---|---|
| 01 | `01-gaps/` | Which open items of 1550–1620 in Bourdeau's catalogue can be worked from online images? | 56 of 1,388 (17 A, 22 B, 17 C) | target choice |

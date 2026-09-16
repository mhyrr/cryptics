# analysis/

One subfolder per experiment: `NN-short-name/` with its own `README.md`
stating the question, the method, how to run it, and the result. Heavy
outputs go in `out/` (gitignored); check in a summary. If the experiment
needs more than the standard library, it gets a `pyproject.toml` here and is
run with `uv run`.

| # | Experiment | Question | Result | Bears on |
|---|---|---|---|---|
| 01 | [Mathers structure](01-mathers-structure/README.md) | Can elementary rules recover missing letters? | 242 exported records; 232 analyzable; symmetry leaves free choices; no tested elementary generator fits a complete grid | H1–H4 |

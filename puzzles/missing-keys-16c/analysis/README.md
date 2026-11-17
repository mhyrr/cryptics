# analysis/

One subfolder per experiment: `NN-short-name/` with its own `README.md`
stating the question, the method, how to run it, and the result. Heavy
outputs go in `out/` (gitignored); check in a summary. If the experiment
needs more than the standard library, it gets a `pyproject.toml` here and is
run with `uv run`.

| # | Experiment | Question | Result | Bears on |
|---|---|---|---|---|
| 01 | `01-gaps/` | Which open items of 1550–1620 in Bourdeau's catalogue can be worked from online images? | 56 of 1,388 (17 A, 22 B, 17 C) | target choice |
| 02 | `02-calibration-synthetic/` | Does `line/align.py` rebuild Cp.30 from a synthetic pair with reader noise? | Pass after three fixes: 0 wrong marked values on 5 seeds; held-out 0.93–0.95, control 0.25 | the key line (PIPELINE stage 3–4) |
| 03 | `03-calibration-real/` | Does it rebuild Cp.30 from es. 132 f. 255 and the Simancas minute? | Pass: 26 of 29 frequent signs right, 0 wrong `certain`; held-out 0.83 vs true-key ceiling 0.79 | the key line; replaces the Saint-Goard test |

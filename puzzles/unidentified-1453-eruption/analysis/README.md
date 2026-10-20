# analysis/

One subfolder per experiment: `NN-short-name/` with its own `README.md`
stating the question, the method, how to run it, and the result. Heavy
outputs go in `out/` (gitignored); check in a summary. If the experiment
needs more than the standard library, it gets a `pyproject.toml` here and is
run with `uv run`.

| # | Experiment | Question | Result | Bears on |
|---|---|---|---|---|
| 01 | gvp-window | Which GVP eruptions could have produced UE 1453 by date and size? | 58 in 1420–1490 with VEI ≥ 4 or unknown; 59 cover 1452; only VEI-5 rows covering 1452 are Pinatubo 1450 ± 50 and El Chichón 1360 ± 100 | H5–H8 |

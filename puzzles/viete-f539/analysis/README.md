# analysis/

One subfolder per experiment: `NN-short-name/` with its own `README.md`
stating the question, the method, how to run it, and the result. Heavy
outputs go in `out/` (gitignored); check in a summary. If the experiment
needs more than the standard library, it gets a `pyproject.toml` here and is
run with `uv run`.

| # | Experiment | Question | Result | Bears on |
|---|---|---|---|---|
| 00 | transcription-and-gate | How long is f. 539 by two blind readers? Does it pass the 300-token gate? | 344 sign tokens, 145–165 signs, ~2.4 uses per sign; gate passes on length | H1, H2 |
| 01 | annealing | Can a homophonic annealer recover an f. 539-shaped key? | No: 0.093 median vs 0.986 positive control; needs 700–1,400 same-key tokens | H2, H6 |

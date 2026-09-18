# analysis/

One subfolder per experiment: `NN-short-name/` with its own `README.md`
stating the question, the method, how to run it, and the result. Heavy
outputs go in `out/` (gitignored); check in a summary. If the experiment
needs more than the standard library, it gets a `pyproject.toml` here and is
run with `uv run`.

| # | Experiment | Question | Result | Bears on |
|---|---|---|---|---|
| 01 | [Mathers structure](01-mathers-structure/README.md) | Can elementary rules recover missing letters? | 242 exported records; 232 analyzable; symmetry leaves free choices; no tested elementary generator fits a complete grid | H1–H4 |
| 02–04 | [Shared stress tests](../STRESS-TESTS.md) | Do frames, corpus fragments or local recurrences generalize? | Frame fills help scattered blanks; independent-letter reconstruction remains unreliable | H8–H11 |
| 05 | [Period dictionary preflight](05-period-dictionary/README.md) | Can independent lexical constraints predict inner orbits? | Selected facsimiles subsequently verified; no recovered construction selector; completion machinery passes planted checks | H7, H12 |
| 10 | [Frozen E1](10-caption-selector/README.md) | Does literal caption matching plus a central cross predict interiors? | Recipe and independent dictionary block frozen; historical caption join pending | H14 |
| 11 | [Caption-first E2](11-caption-first-e2/README.md) | Do bounded semantic caption nominations improve hidden-interior prediction? | Eight captions, eleven lookups; three complete aligned targets but no usable caption domains; controls ran, pilot uninformative | H7, H12, H15 |

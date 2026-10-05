# analysis/

One subfolder per experiment: `NN-short-name/` with its own `README.md`
stating the question, the method, how to run it, and the result. Heavy
outputs go in `out/` (gitignored); check in a summary. If the experiment
needs more than the standard library, it gets a `pyproject.toml` here and is
run with `uv run`.

| # | Experiment | Question | Result | Bears on |
|---|---|---|---|---|
| 01 | decode-f198 | Does Tomokiyo's Cipher 4 key read f. 198? | Yes, with residues | H1 |
| 02 | key-extensions | Five f. 198 extensions; held-out ff. 87, 123 | 2H, H pass; reading v1 | H1, H3, H4 |
| 03 | perez-corpus | Held-out test 3 on ff. 157, 179; Rubino joins | 2H established; joins mostly clean | H4, H6, H7 |
| 04 | cipher3 | Cipher 3 tokenization, decoding, codes | Guide v2.1; ff. 103/105/113/165/167 read; codes u., 108, 149, T | H9–H13 |
| 05 | cipher4-v2 | Reconciled v2 texts; held-out f. 154; extension tally | 2H, Σ, cross-doubling, H established; 21. local | H4–H8 |
| 06 | premurder | Before the murder, did the letters speak of a Don John–Guise league (H16)? | No league wording; but a 24 Jan 1578 Sotomayor–Guise report the King took seriously; Cipher 1 and 2 decoders; f. 3 read | H16, H11 |

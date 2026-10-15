# Checker-agent brief (pilot 01)

Read `README.md` here and the repo's `AGENTS.md` (Rule 6 is the point of this pilot).
Do not spawn agents. Do not post anything to OEIS or anywhere else.

You get the rows of `batch.tsv` with `id` in your range. OEIS entries are at
`$OEIS/seq/Axxx/Annnnnn.seq` where
`OEIS=/tmp/claude-0/-home-user-cryptics/c65ae72a-6e03-5f50-a653-43bbdec9a35a/scratchpad/oeis_dl/oeisdata`
(read-only; it has no b-files). Python 3.13 is available; make a venv with
`uv venv /tmp/claude-0/-home-user-cryptics/c65ae72a-6e03-5f50-a653-43bbdec9a35a/scratchpad/venv-oeis-K`
(K = your batch number) and `uv pip install` what you need (sympy, gmpy2,
python-flint, cypari2, numba all come from PyPI, which is reachable). The machine
has 4 cores shared with 3 other agents: run one heavy job at a time, cap each
item at **5 minutes CPU** (`timeout 300`).

For each row:
1. Read the whole `.seq` entry. Triage the conjecture line into
   `checkable` (a finite statement you can test for each n up to a bound),
   `not-checkable` (asymptotic, existential with no bound, vague), or
   `already-settled` (another line or a cross-referenced entry settles it; say which).
2. If checkable: write `checkers/Annnnnn/check_a.py` (compute the sequence from
   its definition, independently of any OEIS program) and `check_b.py` (a
   different method: translate the entry's own PARI/Python program, or a
   different algorithm). Both must reproduce every term in `%S/%T/%U` first.
   Then both test the conjecture over the same range, from the stated bound
   upward toward 10× it (or as far as 5 min allows). They must agree.
3. Record one row in `results/batch-K.tsv` with columns:
   `id anum triage old_bound new_bound result agree minutes note`
   where `result` is `holds` (to new_bound), `COUNTEREXAMPLE n=…`, `timeout`
   (could not reach old_bound), or `-`. `agree` is Y/N for the two checkers.
   Keep `note` one line; say exactly what was tested if it differs from the
   literal conjecture (e.g. "tested part (i) only").
4. A counterexample needs both checkers agreeing *and* the defining property
   re-checked by hand at that n (print the witness). Do not over-claim: a
   misread definition is the main false-positive source. Re-read the
   definition and the `%e` example before reporting.

Be quick on not-checkable rows (one line). Spend time on the checkable ones.
Write scripts only under `checkers/` and results only to your `results/batch-K.tsv`.
Do not commit. Final report: counts by triage/result, every counterexample with
its witness, and anything suspicious.

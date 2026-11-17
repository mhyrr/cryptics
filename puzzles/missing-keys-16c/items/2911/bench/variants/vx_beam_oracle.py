"""vx_beam_oracle: NOT a key build. A diagnostic for v7_beam: read the cipher with the true table held, and
count how the places fall (match, other spelling, no counterpart, gap). If the true table itself rarely spells
the printed text at the pointer, exact repeats cannot carry a blind build on this pair. Reads
../outside/truth-as-key.tsv (sealed). Logs counts only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "..", "line"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "outside"))
import align, v7_beam, decode  # noqa: E402


def build(cipher, plain, log):
    units, P, wb, lac, pairs = align.load_pair(cipher, plain)
    known = {r["unit"]: decode.norm(r["value"]) for r in
             align.read_key(os.path.join(HERE, "..", "..", "outside", "truth-as-key.tsv"))}
    lens = {}
    for v in known.values():
        lens[len(v)] = lens.get(len(v), 0) + 1
    log(f"true table: {len(known)} rows; value lengths {sorted(lens.items())}")
    score, tab, ops = v7_beam.search(units, P, lac, None, known)
    log(f"score {score:.1f}; path: {v7_beam.summary(units, ops)}")
    run, runs = 0, []
    for kind, j0, j1 in ops:
        if kind == "G":
            run += 1
        elif run:
            runs.append(run)
            run = 0
    if run:
        runs.append(run)
    log(f"gap runs: {len(runs)}; lengths {sorted(runs, reverse=True)[:25]}")
    return v7_beam.rows_from(units, P, tab, ops, known)

"""v9: v8_handoff, then more rounds. After each round of passes the corridor is re-centred on the best path
of the table just built, and the passes go on from that table. A better table gives a better path; a better
path lets rarer signs find their letters. Parameters: V9_ROUNDS; v8's for the rest."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "..", "line"))
import align, v1_gap, v7_beam, v8_handoff as v8  # noqa: E402

ROUNDS = int(os.environ.get("V9_ROUNDS", 4))
SETTLE = 0.0      # > 0: stop when the path moves less than this many letters a unit (v11 sets it)


def build(cipher, plain, log):
    units, P, wb, lac, pairs = align.load_pair(cipher, plain)
    known = {}
    for k in range(v7_beam.PASSES):
        score, tab, ops = v7_beam.search(units, P, lac, None, known)
        rows = v7_beam.rows_from(units, P, tab, ops, known)
        known = {r["unit"]: r["value"] for r in rows if r["status"] == "certain"}
    log(f"beam: score {score:.1f}; table {len(tab)} signs; path: {v7_beam.summary(units, ops)}")
    centers = [float(j0) for kind, j0, j1 in ops] + [float(len(P))]
    old = (align.P_LEN[0], align.SKIP, v1_gap.OPEN, v1_gap.EXT, v1_gap.SKIP)
    align.P_LEN[0], align.SKIP, v1_gap.OPEN, v1_gap.EXT, v1_gap.SKIP = 0.0, v8.SKIP, v8.OPEN, v8.EXT, v8.SKIP
    try:
        table = align.Table()
        for r in rows:
            for k in range(3):
                table.add(r["unit"], r["value"], v8.SEED[r["status"]] / 3, k)
        for rnd in range(ROUNDS):
            seg = v1_gap.GapSegment(units, P, wb, lac, v8.BAND, centers)
            for it in range(v8.ITERS):
                new = align.Table()
                z, g = seg.estep(table, new)
                table = new
            path, skipped = align.best_path([(0, 0, seg)], table)
            rows = align.key_from_path(path, skipped)
            moved = sum(abs(c - j0) for c, (u, j0, j, s) in zip(centers, path)) / len(path)
            st = {}
            for r in rows:
                st[r["status"]] = st.get(r["status"], 0) + 1
            log(f"round {rnd + 1}: ll per unit {z / len(units):.3f}; units in gaps "
                f"{sum(1 for u, a, b, s in path if s is None)}; path moved {moved:.1f} letters a unit; rows {st}")
            centers = [float(j0) for u, j0, j, s in path] + [float(len(P))]
            if SETTLE and moved < SETTLE:
                break
        return rows
    finally:
        align.P_LEN[0], align.SKIP, v1_gap.OPEN, v1_gap.EXT, v1_gap.SKIP = old

"""v8: the beam reads first, the soft passes finish.

v7_beam gives a path (where each unit sits in the plain text) and a table that is partly right. Its hard
rule cannot mend a wrong value that hits by chance. v1_gap's passes can: started from the true table they hold
it (vx_oracle). Here they start from the beam's table and run in a corridor of +-BAND letters round the beam's
path, so a sign that occurs 15 times is compared with 30 letters a place, not 550.
No null value (the empty emission has prior 0). A gap costs about what an unvalued sign costs, so the passes
do not flee into gaps. Parameters: V8_BAND, V8_ITERS, V8_OPEN, V8_EXT, V8_SKIP.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "..", "line"))
import align, v1_gap, v7_beam  # noqa: E402

BAND = int(os.environ.get("V8_BAND", 15))
ITERS = int(os.environ.get("V8_ITERS", 8))
OPEN = float(os.environ.get("V8_OPEN", -4.0))
EXT = float(os.environ.get("V8_EXT", -4.0))
SKIP = float(os.environ.get("V8_SKIP", 0.02))
SEED = {"certain": 6.0, "probable": 3.0, "unknown": 1.0}


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
    align.P_LEN[0], align.SKIP, v1_gap.OPEN, v1_gap.EXT, v1_gap.SKIP = 0.0, SKIP, OPEN, EXT, SKIP
    try:
        seg = v1_gap.GapSegment(units, P, wb, lac, BAND, centers)
        table = align.Table()
        for r in rows:
            for k in range(3):
                table.add(r["unit"], r["value"], SEED[r["status"]] / 3, k)
        for it in range(ITERS):
            new = align.Table()
            z, g = seg.estep(table, new)
            table = new
            log(f"pass {it + 1}: ll per unit {z / len(units):.3f} units in gaps {g:.0f}")
        segs = [(0, 0, seg)]
        path, skipped = align.best_path(segs, table)
        log(f"best path: {sum(1 for u, a, b, s in path if s is None)} units in gaps, {len(skipped)} letters unaccounted")
        return align.key_from_path(path, skipped)
    finally:
        align.P_LEN[0], align.SKIP, v1_gap.OPEN, v1_gap.EXT, v1_gap.SKIP = old

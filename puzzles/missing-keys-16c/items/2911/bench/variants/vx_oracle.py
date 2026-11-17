"""vx_oracle: NOT a key build. A diagnostic: start the passes from the true table and see whether they stay there.
If they do, the model and the pair are sound and the open problem is the start. If they drift off, the model is
wrong for this pair. Reads ../outside/truth-as-key.tsv (sealed)."""
import math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "..", "line"))
import align, v1_gap  # noqa: E402
sys.path.insert(0, os.path.join(HERE, "..", "..", "outside"))
import decode  # noqa: E402

WEIGHT = float(os.environ.get("VX_WEIGHT", 20))
ITERS = int(os.environ.get("VX_ITERS", 6))


def build(cipher, plain, log):
    old = (align.P_LEN[0], align.SKIP)
    align.P_LEN[0], align.SKIP = v1_gap.NULL0, v1_gap.SKIP
    try:
        units, P, wb, lac, pairs = align.load_pair(cipher, plain)
        segs = [(a, c, v1_gap.GapSegment(s.units, s.P, s.wb, s.lac)) for a, c, s in align.make_segments(units, P, wb, lac, pairs)]
        table = align.Table()
        for r in align.read_key(os.path.join(HERE, "..", "..", "outside", "truth-as-key.tsv")):
            for k in range(3):
                table.add(r["unit"], decode.norm(r["value"]), WEIGHT / 3, k)
        for it in range(ITERS):
            new, ll, gp = align.Table(), 0.0, 0.0
            for a, c, seg in segs:
                z, g = seg.estep(table, new)
                ll += z
                gp += g
            table = new
            log(f"pass {it + 1}: ll {ll:.1f} per unit {ll / len(units):.3f} units in gaps {gp:.0f}")
        path, skipped = align.best_path(segs, table)
        log(f"best path: {sum(1 for u, a, b, s in path if s is None)} units in gaps, {len(skipped)} letters unaccounted")
        return align.key_from_path(path, skipped)
    finally:
        align.P_LEN[0], align.SKIP = old

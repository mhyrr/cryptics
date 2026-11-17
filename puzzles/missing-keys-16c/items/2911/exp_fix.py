"""exp_fix.py - builds after the stage 4 failure. Every figure from this script is "after a fix".
    python3 exp_fix.py <cipher> <plain> <tag> <null0> <skip> [iters]
null0: prior weight of the empty emission for the first half of the passes (then align.py's 0.04).
skip : cost of a plaintext letter no unit accounts for, all passes.
Writes results/fix-<tag>.key.tsv and prints the null share of the best path after training.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import align_log  # noqa: E402  (puts line/ on the path, patches Segment.estep to log space)
import align      # noqa: E402

cipher, plain, tag, null0, skip = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5])
iters = int(sys.argv[6]) if len(sys.argv) > 6 else 12
align.SKIP = skip
units, P, wb, lac, pairs = align.load_pair(cipher, plain)
segs = align.make_segments(units, P, wb, lac, pairs)
segs = [(a, c, align_log.LogSegment(s.units, s.P, s.wb, s.lac)) for a, c, s in segs]
table = align.Table()
base0 = align.P_LEN[0]
for it in range(iters):
    align.P_LEN[0] = null0 if it < iters // 2 else base0
    table._cache = {}
    new, ll = align.Table(), 0.0
    for k, (a, c, seg) in enumerate(segs):
        l, centers = seg.estep(table, new)
        ll += l
        if it >= 4 and seg.n > 60:
            w = max(40, int((seg.hi[seg.n // 2] - seg.lo[seg.n // 2]) / 2 * 0.7))
            segs[k] = (a, c, align_log.LogSegment(seg.units, seg.P, seg.wb, seg.lac, w, centers))
    table = new
    nul = sum(v.get("", 0.0) for v in table.cnt.values()) / max(1e-9, sum(table.tot.values()))
    print(f"{tag} pass {it + 1}: ll {ll:.1f} null share {nul:.3f}", flush=True)
align.P_LEN[0] = base0
path, skipped = align.best_path(segs, table)
rows = align.key_from_path(path, skipped)
align.write_key(rows, os.path.join(HERE, "results", f"fix-{tag}.key.tsv"))
vals = [s for u, a, b, s in path if u.kind == "sign" and u.sym != "?" and s is not None]
st = {}
for r in rows:
    st[(r["status"], r["type"])] = st.get((r["status"], r["type"]), 0) + 1
print(f"{tag} done: units {len(units)} letters {len(P)} skipped {len(skipped)} null share on path "
      f"{sum(1 for v in vals if v == '') / len(vals):.3f}; rows {sorted(st.items())}", flush=True)

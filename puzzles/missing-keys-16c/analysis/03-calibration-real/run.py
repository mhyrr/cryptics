"""Real calibration of line/align.py on es. 132 f. 255 against the Simancas minute. Bars: README.md.
    python3 prep.py && python3 run.py   -> key-v0.tsv, result.tsv
"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "line"))
import align  # noqa: E402

MINOCC = 5


def main():
    truth = dict(l.rstrip("\n").split("\t") for l in open(HERE / "truth.tsv"))
    units, P, wb, lac, pairs = align.load_pair(HERE / "cipher.txt", HERE / "plain.txt")
    segs = align.make_segments(units, P, wb, lac, pairs)
    path, skipped = align.best_path(segs, align.train(segs))
    rows = align.key_from_path(path)
    align.write_key(rows, HERE / "key-v0.tsv")
    occ = {}
    for u in units:
        if u.kind == "sign" and u.sym != "?":
            occ[u.sym] = occ.get(u.sym, 0) + 1
    freq = [s for s, n in occ.items() if n >= MINOCC]
    got = {r["unit"]: r for r in rows}
    top_right = [s for s in freq if s in truth and got[s]["value"] == truth[s]]
    no_truth = [s for s in freq if s not in truth]
    marked = [r for r in rows if r["status"] != "unknown" and r["unit"] in truth]
    wrong = [r for r in marked if truth[r["unit"]] != r["value"]]
    certain = [r for r in marked if r["status"] == "certain"]
    wrong_c = [r for r in wrong if r["status"] == "certain"]
    h = align.heldout(units, P, wb, lac, pairs)
    # ceiling: the true table on the same lines, same scorer
    spans = align.line_spans(path, len(P))
    mat = dec = 0
    by = {}
    for u in units:
        by.setdefault(u.line, []).append(u)
    for ln, us in by.items():
        c, d = spans[ln]
        a, b, _ = align.score(align.decode_units(us, truth), P[c:d])
        mat, dec = mat + a, dec + b
    ceil = mat / dec
    nt = len(freq) - len(no_truth)
    r1 = len(top_right) / nt >= 0.80
    r2 = len(wrong_c) / max(1, len(certain)) <= 0.05 and len(wrong) / max(1, len(marked)) <= 0.10
    r3 = h["accuracy"] >= ceil - 0.10 and h["control"] <= h["accuracy"] - 0.25
    lines = [f"units\t{len(units)}", f"letters\t{len(P)}", f"letters_unaccounted\t{len(skipped)}",
             f"frequent_types_with_truth\t{nt}", f"top_value_right\t{len(top_right)}",
             f"top_value_right_share\t{len(top_right) / nt:.3f}",
             f"frequent_types_without_truth\t{' '.join(sorted(no_truth)) or '-'}",
             f"marked\t{len(marked)}", f"marked_wrong\t{len(wrong)}\t{' '.join(r['unit'] + '=' + r['value'] for r in wrong)}",
             f"certain\t{len(certain)}", f"certain_wrong\t{len(wrong_c)}",
             f"heldout_acc\t{h['accuracy']:.3f}", f"heldout_coverage\t{h['coverage']:.3f}",
             f"heldout_control\t{h['control']:.3f}", f"true_key_ceiling\t{ceil:.3f}",
             f"R1\t{'pass' if r1 else 'FAIL'}", f"R2\t{'pass' if r2 else 'FAIL'}", f"R3\t{'pass' if r3 else 'FAIL'}"]
    (HERE / "result.tsv").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

"""Synthetic calibration of line/align.py. Bars are in README.md, written before this was run.
    python3 run.py            # seeds 11-15, 3000 letters -> result.tsv
"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "line"))
import align, make_pair  # noqa: E402

SEEDS, NLET, MINOCC = [11, 12, 13, 14, 15], 3000, 5


def table_score(rows, truth, units):
    occ = {}
    for u in units:
        if u.kind == "sign":
            occ[u.sym] = occ.get(u.sym, 0) + 1
    frequent = [s for s, n in occ.items() if n >= MINOCC and s in truth]
    got = {r["unit"]: r for r in rows}
    right = sum(1 for s in frequent if s in got and got[s]["status"] != "unknown" and got[s]["value"] == truth[s])
    marked = [r for r in rows if r["status"] != "unknown"]
    wrong = [r for r in marked if truth.get(r["unit"]) != r["value"]]
    wrong_c = [r for r in wrong if r["status"] == "certain"]
    return len(frequent), right, len(marked), len(wrong), len(wrong_c)


def true_share(rows, truth, d):
    """S1a: as S1, over unit types enciphered five times or more before noise (occ.tsv)."""
    occ = {l.split("\t")[0]: int(l.split("\t")[1]) for l in open(d / "occ.tsv")}
    freq = [s for s, n in occ.items() if n >= MINOCC]
    got = {r["unit"]: r for r in rows}
    right = sum(1 for s in freq if s in got and got[s]["status"] != "unknown" and got[s]["value"] == truth[s])
    return len(freq), right


def main():
    out = ["seed\tunits\tletters\tfrequent_types\trecovered\trecovered_share\tmarked\twrong\twrong_certain\t"
           "heldout_acc\tcoverage\tcontrol\tS1\tS2\tS3\ttrue_frequent\ttrue_recovered\tS1a"]
    for seed in SEEDS:
        d = HERE / "out" / f"s{seed}"
        make_pair.main(NLET, seed, d)
        truth = dict(l.rstrip("\n").split("\t") for l in open(d / "truth.tsv"))
        units, P, wb, lac, pairs = align.load_pair(d / "cipher.txt", d / "plain.txt")
        segs = align.make_segments(units, P, wb, lac, pairs)
        path, skipped = align.best_path(segs, align.train(segs))
        rows = align.key_from_path(path, skipped)
        align.write_key(rows, d / "key-v0.tsv")
        nf, right, marked, wrong, wrong_c = table_score(rows, truth, units)
        tf, tr = true_share(rows, truth, d)
        h = align.heldout(units, P, wb, lac, pairs)
        s1 = right / nf >= 0.90
        s2 = wrong / marked <= 0.02 and wrong_c == 0
        s3 = h["accuracy"] >= 0.85 and h["coverage"] >= 0.70 and h["control"] <= 0.30
        out.append(f"{seed}\t{len(units)}\t{len(P)}\t{nf}\t{right}\t{right / nf:.3f}\t{marked}\t{wrong}\t{wrong_c}\t"
                   f"{h['accuracy']:.3f}\t{h['coverage']:.3f}\t{h['control']:.3f}\t"
                   + "\t".join("pass" if x else "FAIL" for x in (s1, s2, s3))
                   + "\t%d\t%d\t%s" % (tf, tr, "pass" if tr / tf >= 0.90 else "FAIL"))
        print(out[-1], flush=True)
    (HERE / "result.tsv").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

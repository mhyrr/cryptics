"""stage4_collect.py - gather the held-out runs into results/heldout.tsv and apply the four bars of README section 4.

    python3 stage4_collect.py

Reads results/log/heldout-<run>.tsv (written by `align_log.py heldout --out`). One row per run, labelled
primary or side. The verdict column is filled for the primary run only; side runs get the same four tests
under "bars_met" and cannot change the verdict.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = [
    ("primary", "primary", "cipher consensus, base+mark one unit", "plain consensus of readers A and B"),
    ("side-separate-units", "side", "cipher consensus, base and marks separate units", "plain consensus of readers A and B"),
    ("side-plain-A", "side", "cipher consensus, base+mark one unit", "plain reader A alone"),
    ("side-print", "side", "cipher consensus, base+mark one unit", "printed text (Opere VI, 1877)"),
]
cols = ["run", "role", "cipher_side", "plain_side", "accuracy", "coverage", "control", "gap_points", "recall", "units", "letters",
        "acc>=0.85", "cov>=0.70", "ctrl<=0.30", "gap>=25", "bars_met", "verdict"]
out = ["\t".join(cols)]
for run, role, cs, ps in RUNS:
    p = os.path.join(HERE, "results", "log", "heldout-%s.tsv" % run)
    if not os.path.exists(p):
        out.append("\t".join([run, role, cs, ps] + ["not run"] * (len(cols) - 4)))
        continue
    d = dict(l.split("\t") for l in open(p).read().splitlines() if l.strip())
    acc, cov, ctrl = float(d["accuracy"]), float(d["coverage"]), float(d["control"])
    gap = round((acc - ctrl) * 100, 1)
    t = [acc >= 0.85, cov >= 0.70, ctrl <= 0.30, gap >= 25]
    verdict = ""
    if role == "primary":
        if all(t):
            verdict = "pass"
        elif 0.70 <= acc < 0.85 and t[1] and t[2] and t[3]:
            verdict = "failed (accuracy between 0.70 and 0.85; other bars met)"
        else:
            verdict = "failed"
    out.append("\t".join([run, role, cs, ps, d["accuracy"], d["coverage"], d["control"], str(gap), d["recall"], d["units"],
                          d["letters"]] + ["yes" if x else "no" for x in t] + ["yes" if all(t) else "no", verdict]))
open(os.path.join(HERE, "results", "heldout.tsv"), "w").write("\n".join(out) + "\n")
print("\n".join(out))

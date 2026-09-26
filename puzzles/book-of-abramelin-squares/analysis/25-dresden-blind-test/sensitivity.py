#!/usr/bin/env python3
"""Post hoc, after the scoring run and the independent verification: the primary
measures split by how well each joined grid agrees with Mathers on shared
letters. The frozen gate admits agreement from 0.5; this shows whether the
verdict depends on the loosely joined grids. Nothing in score.py or its outputs
changes.

python3 sensitivity.py            write sensitivity.json
python3 sensitivity.py --check    verify it reproduces
"""
import json, sys
from pathlib import Path

import score

HERE = Path(__file__).resolve().parent


def agreement(m, rows):
    n = len(rows)
    both = [(i, j) for i in range(n) for j in range(n) if m[i][j].isalpha() and rows[i][j].isalpha()]
    return sum(m[i][j] == rows[i][j] for i, j in both) / len(both)


def main():
    consensus = json.load(open(HERE / "consensus.json"))["grids"]
    mathers = {s["id"]: [r.upper() for r in s["rows"]]
               for s in json.load(open(score.DIVE / "sources" / "mathers-squares.json"))["squares"]}
    cells = json.load(open(HERE / "cells.json"))["cells"]
    joined = score.primary_join(consensus, mathers)
    agree = {sid: agreement(mathers[sid], g["rows"]) for sid, g in joined.items()}
    out = {"status": "post hoc; see README 'Verification and corrections'"}
    for name, keep in (("agreement >= 0.8", lambda a: a >= 0.8), ("agreement < 0.8", lambda a: a < 0.8)):
        sub = [c for c in cells if keep(agree[c["id"]])]
        m = score.measures(sub)
        out[name] = {"joins": sum(keep(a) for a in agree.values()), "targets": m["targets"],
                     **{k: m[k] for k in ("M1_sym_border", "M2_class_interior", "M3_letter_filler")},
                     "verdict_rule": score.decide(m)}
    unjoined = [g["locator_id"] for g in consensus if joined.get(f"{g['chapter']}/{g['item']}") is not g]
    out["unjoined_grids"] = len(unjoined)
    text = json.dumps(out, indent=1) + "\n"
    path = HERE / "sensitivity.json"
    if "--check" in sys.argv:
        assert path.read_text() == text, "sensitivity differs"
        print("sensitivity reproduces")
        return
    path.write_text(text)
    for k, v in out.items():
        if isinstance(v, dict):
            print(k, v["joins"], v["targets"], {x: round(v[x]["accuracy"], 3) for x in ("M1_sym_border", "M2_class_interior", "M3_letter_filler")}, v["verdict_rule"])
    print("unjoined grids", out["unjoined_grids"])


if __name__ == "__main__":
    main()

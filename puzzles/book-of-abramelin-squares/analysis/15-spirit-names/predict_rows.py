#!/usr/bin/env python3
"""Can Mathers's own spirit list fill interior rows that Mathers leaves blank?

Design fixed before the first run (2026-09-20) and run once.
Inputs the model sees: the Mathers squares and the `mathers` name lists only.
For each incomplete Mathers square that experiment 13 aligned to a Dehn reading
(id gate or post hoc realignment), and each inner row with at least one blank:
candidates are names of length n, read forward or reversed, that agree with
every visible letter of the row (the left-column letter is always visible).
Exactly one candidate -> predict the row; otherwise abstain.
Control: the same procedure with the name list cv-shuffled (200 draws).
Score: predicted rows equal to the Dehn row (exact) or within one letter.
"""
import json, pathlib, random, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "13-dehn-witness-test"))
from names_in_squares import norm, cv_shuffle, HERE, ROOT
import score as s13


def run(names, pairs):
    res = {"rows": 0, "predicted": 0, "exact": 0, "within_one": 0, "detail": []}
    for sid, m, d in pairs:
        n = len(m)
        for i in range(1, n - 1):
            if "." not in m[i]:
                continue
            res["rows"] += 1
            cands = {c for nm in names if len(nm) == n for c in (nm, nm[::-1])
                     if all(a == "." or a == b for a, b in zip(m[i], c))}
            if len(cands) == 1:
                c = cands.pop()
                truth = norm(d[i])
                res["predicted"] += 1
                res["exact"] += c == truth
                res["within_one"] += sum(x != y for x, y in zip(c, truth)) <= 1
                res["detail"].append({"square": sid, "row": i, "visible": m[i], "predicted": c, "dehn": truth})
    return res


def main():
    lists = json.load(open(HERE / "spirit-names.json"))["lists"]
    names = list(dict.fromkeys(norm(x) for l in lists if l["source"] == "mathers" for x in l["names"]))
    mathers = {q["id"]: q["rows"] for q in json.load(open(ROOT / "sources" / "mathers-squares.json"))["squares"]}
    dehn = s13.realign(json.load(open(HERE.parent / "13-dehn-witness-test" / "dehn-readings.json"))["squares"], mathers)
    pairs = []
    for d in dehn:
        m = mathers.get(d["id"]); rows = d["rows"]; n = len(rows)
        if not m or len(m) != n or any(len(r) != n for r in m) or any(len(r) != n for r in rows):
            continue
        a, b = s13.agreement(m, rows)
        if b and a / b >= 0.5 and any("." in r for r in m):
            pairs.append((d["id"], m, rows))
    real = run(names, pairs)
    rng = random.Random(2026092016)
    ctrl = [run([cv_shuffle(x, rng) for x in names], pairs) for _ in range(200)]
    out = {"squares": len(pairs), "real": real,
           "control_mean": {k: sum(c[k] for c in ctrl) / 200 for k in ("predicted", "exact", "within_one")}}
    (HERE / "row-predictions.json").write_text(json.dumps(out, indent=1) + "\n")
    print({k: v for k, v in real.items() if k != "detail"}, out["control_mean"])
    for d in real["detail"]:
        print(d)


if __name__ == "__main__":
    main()

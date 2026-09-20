#!/usr/bin/env python3
"""Score the frozen predictions against the Dehn readings. See PROTOCOL.md.

Alignment gate, decided before scoring and using visible cells only: a Dehn
reading is scored against a Mathers square when both are n x n with the same n
and they agree on at least half of the cells that are letters in both. A
reading that fails the gate is listed under `unaligned` and never scored.
"""
import collections, hashlib, json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V = set("AEIOU")
SEEN = {"5/1", "5/2"}
MODELS = ["sym_TA", "sym_T", "letter_filler", "letter_global"]


def main():
    pred_text = (HERE / "predictions.json").read_text()
    frozen = json.load(open(HERE / "prediction-freeze.json"))["predictions_sha256"]
    assert hashlib.sha256(pred_text.encode()).hexdigest() == frozen, "predictions changed after freeze"
    preds = {s["id"]: s for s in json.loads(pred_text)["squares"]}
    mathers = {s["id"]: s["rows"] for s in json.load(open(ROOT / "sources" / "mathers-squares.json"))["squares"]}
    dehn = json.load(open(HERE / "dehn-readings.json"))["squares"]

    tally = collections.defaultdict(collections.Counter)
    disagree = collections.defaultdict(collections.Counter)
    per_square, unaligned, complete_pairs = [], [], []
    desc = collections.Counter()
    for d in dehn:
        rows, sid = d["rows"], d["id"]
        n = len(rows)
        m = mathers.get(sid)
        square_like = all(len(r) == n for r in rows) and all(c.isalpha() for r in rows for c in r)
        if square_like and n >= 4:
            desc["dehn_squares"] += 1
            desc["T"] += all(rows[i][j] == rows[j][i] for i in range(n) for j in range(n))
            desc["TA"] += all(rows[i][j] == rows[j][i] == rows[n - 1 - i][n - 1 - j] for i in range(n) for j in range(n))
            for i in range(1, n - 1):
                for j in range(1, n - 1):
                    desc["interior_cells"] += 1
                    desc["interior_checkerboard"] += (rows[i][j] in V) == ((rows[0][j] in V) ^ (i % 2 == 1))
        if not m or not square_like or len(m) != n or any(len(r) != n for r in m):
            unaligned.append({"dehn_id_basis": d["id_basis"], "id": sid, "reason": "shape or id", "raw": d["raw"][:120]})
            continue
        both = [(i, j) for i in range(n) for j in range(n) if m[i][j] != "."]
        same = sum(m[i][j] == rows[i][j] for i, j in both)
        if not both or same / len(both) < 0.5:
            unaligned.append({"id": sid, "reason": f"visible agreement {same}/{len(both)}", "raw": d["raw"][:120]})
            continue
        for i, j in both:
            zone = "top_row" if i == 0 else ("other_border" if i in (0, n - 1) or j in (0, n - 1) else "interior")
            disagree[zone]["cells"] += 1
            disagree[zone]["differ"] += m[i][j] != rows[i][j]
        if sid not in preds:
            complete_pairs.append(sid)
            continue
        sq = {"id": sid, "size": n, "seen_before_freeze": sid in SEEN, "visible_agreement": f"{same}/{len(both)}"}
        local = collections.defaultdict(collections.Counter)
        for c in preds[sid]["cells"]:
            truth = rows[c["row"]][c["column"]]
            zone = "interior" if c["interior"] else "border"
            for mdl in MODELS:
                k = (mdl, zone)
                guess = c[mdl]
                outcome = "abstain" if guess is None else ("correct" if guess == truth else "wrong")
                tally[k][outcome] += 1
                local[mdl][outcome] += 1
                if sid not in SEEN:
                    tally[(mdl, zone + "_unseen")][outcome] += 1
            cls = c["class_checkerboard"]
            outcome = "abstain" if cls is None else ("correct" if (truth in V) == (cls == "V") else "wrong")
            tally[("class_checkerboard", zone)][outcome] += 1
            if sid not in SEEN:
                tally[("class_checkerboard", zone + "_unseen")][outcome] += 1
        sq["models"] = {k: dict(v) for k, v in local.items()}
        per_square.append(sq)
    out = {"scored_squares": len(per_square), "unaligned": unaligned,
           "aligned_but_complete_in_mathers": complete_pairs,
           "tally": {f"{a}|{b}": dict(c) for (a, b), c in sorted(tally.items())},
           "mathers_vs_dehn_on_visible_cells": {k: dict(v) for k, v in disagree.items()},
           "dehn_description": dict(desc), "per_square": per_square}
    (HERE / "results.json").write_text(json.dumps(out, indent=1) + "\n")
    print("scored", len(per_square), "unaligned", len(unaligned), "complete pairs", len(complete_pairs))
    for k, c in sorted(tally.items()):
        tot = c["correct"] + c["wrong"]
        print(f"{k[0]:20} {k[1]:16} correct {c['correct']:4} wrong {c['wrong']:4} abstain {c['abstain']:4}  precision {c['correct']/tot if tot else float('nan'):.3f}")
    print(dict(desc)); print({k: dict(v) for k, v in disagree.items()})
    for u in unaligned: print("UNALIGNED", u)


if __name__ == "__main__":
    main()

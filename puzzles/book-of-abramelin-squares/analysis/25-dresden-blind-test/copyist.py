#!/usr/bin/env python3
"""The copyist's corrections against his exemplar readings. See ADDENDUM-COPYIST.md."""
import json, math, sys
from pathlib import Path

import score

HERE = Path(__file__).resolve().parent
PAIRS = [("11/3", "p251-c2-g2", "p251-c2-g1"), ("12/4", "p252-c1-g2", "p252-c1-g3"),
         ("18/3", "p257-c3-g2", "p257-c3-g3"), ("19/6", "p259-c2-g1", "p259-c2-g2"),
         ("26/2", "p265-c3-g2", "p265-c3-g3")]


def consensus_rows(a, b):
    """Row-wise consensus that tolerates non-square grids; None if row lengths differ."""
    if not a or not b or list(map(len, a)) != list(map(len, b)):
        return None
    return ["".join(x if x == y and "A" <= x <= "Z" else "?" for x, y in zip(ra, rb)) for ra, rb in zip(a, b)]


def letter(rows, i, j):
    if i < len(rows) and j < len(rows[i]) and "A" <= rows[i][j] <= "Z":
        return rows[i][j]
    return None


def transpose_agreement(rows):
    same = total = 0
    for i in range(len(rows)):
        for j in range(i + 1, len(rows[i])):
            a, b = letter(rows, i, j), letter(rows, j, i)
            if a and b:
                total += 1
                same += a == b
    return {"same": same, "pairs": total, "share": same / total if total else None}


def added_rows(corr, exem):
    remaining = list(exem)
    added = []
    for k, r in enumerate(corr):
        if r in remaining:
            remaining.remove(r)
        else:
            added.append(k)
    same = total = 0
    for i in added:
        for j in range(len(corr[i])):
            if j == i:
                continue
            a, b = letter(corr, i, j), letter(corr, j, i)
            if a and b:
                total += 1
                same += a == b
    return {"added_rows": added, "cells": total, "equal_to_transpose": same,
            "share": same / total if total else None}


def mathers_agreement(rows, m):
    if not m:
        return None
    same = total = 0
    for i, mr in enumerate(m):
        for j, c in enumerate(mr.upper()):
            d = letter(rows, i, j)
            if c.isalpha() and d:
                total += 1
                same += c == d
    return {"same": same, "cells": total}


def sign_p(wins, losses):
    n = wins + losses
    return sum(math.comb(n, k) for k in range(wins, n + 1)) / 2 ** n if n else None


def main():
    readings = score.load_readings()
    mathers = {s["id"]: s["rows"] for s in json.load(open(score.DIVE / "sources" / "mathers-squares.json"))["squares"]}
    out, wins, losses = [], 0, 0
    for sid, c_id, e_id in PAIRS:
        corr = consensus_rows(readings["A"].get(c_id), readings["B"].get(c_id))
        exem = consensus_rows(readings["A"].get(e_id), readings["B"].get(e_id))
        row = {"square": sid, "correction": c_id, "exemplar": e_id,
               "correction_rows": corr, "exemplar_rows": exem}
        if corr is None or exem is None:
            row["status"] = "reader shapes differ; not scored"
            out.append(row)
            continue
        tc, te = transpose_agreement(corr), transpose_agreement(exem)
        row.update(C1_correction=tc, C1_exemplar=te,
                   C2=added_rows(corr, exem) if len(corr) > len(exem) else None,
                   C3_correction=mathers_agreement(corr, mathers.get(sid)),
                   C3_exemplar=mathers_agreement(exem, mathers.get(sid)))
        if tc["share"] is not None and te["share"] is not None:
            wins += tc["share"] > te["share"]
            losses += tc["share"] < te["share"]
        out.append(row)
    res = {"addendum": "ADDENDUM-COPYIST.md", "pairs": out,
           "C1_sign_test": {"correction_higher": wins, "exemplar_higher": losses, "p_one_sided": sign_p(wins, losses)}}
    text = json.dumps(res, indent=1) + "\n"
    path = HERE / "copyist-results.json"
    if "--check" in sys.argv:
        assert path.read_text() == text, "copyist results differ"
        print("copyist results reproduce")
        return
    path.write_text(text)
    print(json.dumps(res["C1_sign_test"]))
    for r in out:
        print(r["square"], r.get("status", ""), r.get("C1_correction"), r.get("C1_exemplar"), r.get("C2"))


if __name__ == "__main__":
    main()

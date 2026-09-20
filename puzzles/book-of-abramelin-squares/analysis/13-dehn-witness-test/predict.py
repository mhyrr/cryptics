#!/usr/bin/env python3
"""Freeze interior predictions for every incomplete Mathers square. See PROTOCOL.md."""
import collections, hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SQ = ROOT / "sources" / "mathers-squares.json"
P01 = ROOT / "analysis" / "01-mathers-structure" / "predictions.json"
V = set("AEIOU")


def shape_ok(rows):
    n = len(rows)
    return n >= 3 and all(len(r) == n for r in rows)


def train(squares):
    vow, con, allc = collections.Counter(), collections.Counter(), collections.Counter()
    for s in squares:
        g = s["rows"]
        if not shape_ok(g) or any("." in r for r in g) or len(g) < 4:
            continue
        n = len(g)
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                ch = g[i][j]
                allc[ch] += 1
                (vow if ch in V else con)[ch] += 1
    top = lambda c: sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
    return top(vow), top(con), top(allc)


def main():
    squares = json.load(open(SQ))["squares"]
    vmode, cmode, gmode = train(squares)
    ta = {s["id"]: {(f["row"], f["column"]): f["letter"] for f in s["fills"]}
          for s in json.load(open(P01))["squares"]}
    out = []
    for s in squares:
        g = s["rows"]
        if not shape_ok(g) or not any("." in r for r in g):
            continue
        n = len(g)
        cells = []
        for i in range(n):
            for j in range(n):
                if g[i][j] != ".":
                    continue
                t = g[0][j]
                cls = None if t == "." else ("V" if ((t in V) ^ (i % 2 == 1)) else "C")
                cells.append({
                    "row": i, "column": j,
                    "interior": 0 < i < n - 1 and 0 < j < n - 1,
                    "sym_TA": ta.get(s["id"], {}).get((i, j)),
                    "sym_T": g[j][i] if g[j][i] != "." else None,
                    "class_checkerboard": cls,
                    "letter_filler": None if cls is None else (vmode if cls == "V" else cmode),
                    "letter_global": gmode,
                })
        out.append({"id": s["id"], "size": n, "cells": cells})
    doc = {"trained_modes": {"vowel": vmode, "consonant": cmode, "global": gmode},
           "index_base": "rows and columns are zero-indexed, as in experiment 01",
           "squares": out}
    text = json.dumps(doc, indent=1) + "\n"
    p = HERE / "predictions.json"
    if "--check" in sys.argv:
        assert p.read_text() == text, "predictions differ from frozen file"
        print("predictions reproduce")
        return
    p.write_text(text)
    freeze = {"predictions_sha256": hashlib.sha256(text.encode()).hexdigest(),
              "corpus_sha256": hashlib.sha256(SQ.read_bytes()).hexdigest(),
              "exp01_predictions_sha256": hashlib.sha256(P01.read_bytes()).hexdigest(),
              "protocol_sha256": hashlib.sha256((HERE / "PROTOCOL.md").read_bytes()).hexdigest()}
    (HERE / "prediction-freeze.json").write_text(json.dumps(freeze, indent=1) + "\n")
    print(vmode, cmode, gmode, len(out), "squares", sum(len(s["cells"]) for s in out), "blank cells")


if __name__ == "__main__":
    main()

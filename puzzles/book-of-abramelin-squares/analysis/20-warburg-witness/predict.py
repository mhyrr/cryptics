#!/usr/bin/env python3
"""Freeze the chapter-model letter predictions for cells blank in Mathers."""
import collections, hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
A = HERE.parent
sys.path.insert(0, str(A / "16-interior-freedom"))
import run as e16     # load(), orbits(), V, C, K; not modified

P13 = A / "13-dehn-witness-test" / "predictions.json"


def main():
    squares, _ = e16.load()
    orbs = [o for s in squares for o in e16.orbits(s)]
    chap = {s["id"]: s["chapter"] for s in squares}
    tot = {"V": collections.Counter(), "C": collections.Counter()}
    ctx = collections.defaultdict(collections.Counter)
    for o in orbs:
        tot[o["cls"]][o["letter"]] += 1
        ctx[(o["cls"], chap[o["sq"]])][o["letter"]] += 1
    base = {}
    for cls, alpha in (("V", e16.V), ("C", e16.C)):
        z = sum(tot[cls][l] + 0.5 for l in alpha)
        base[cls] = {l: (tot[cls][l] + 0.5) / z for l in alpha}
    p13 = json.load(open(P13))
    out = []
    for s in p13["squares"]:
        ch = int(s["id"].split("/")[0])
        cells = []
        for c in s["cells"]:
            cls = c["class_checkerboard"]
            guess = None
            if cls:
                t = ctx[(cls, ch)]
                n = sum(t.values())
                guess = sorted(base[cls], key=lambda l: (-(t[l] + e16.K * base[cls][l]) / (n + e16.K), l))[0]
            cells.append({"row": c["row"], "column": c["column"], "letter_chapter": guess})
        out.append({"id": s["id"], "cells": cells})
    text = json.dumps({"model": "experiment 16 M1, all Mathers interior orbits", "squares": out}, indent=0) + "\n"
    p = HERE / "predictions.json"
    if "--check" in sys.argv:
        assert p.read_text() == text
        print("predictions reproduce")
        return
    p.write_text(text)
    (HERE / "freeze.json").write_text(json.dumps({
        "predictions_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "exp13_predictions_sha256": hashlib.sha256(P13.read_bytes()).hexdigest()}, indent=1) + "\n")
    print(len(out), "squares", sum(len(s["cells"]) for s in out), "cells")


if __name__ == "__main__":
    main()

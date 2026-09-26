#!/usr/bin/env python3
"""Collate the frozen three-page Dresden pilot; keep readers and models separate."""
import argparse
import collections
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PUZZLE = HERE.parents[1]
ROOT = HERE.parents[3]
LETTERS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
VOWELS = set("AEIOU")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def readers(path):
    data = json.loads(path.read_text())
    if sorted(data["pages_completed"]) != [243, 244, 245]:
        raise ValueError(f"Reader did not finish frozen cohort: {path.name}")
    out = {}
    for item in data["items"]:
        key = (item["physical_page"], item["grid_index"])
        if key in out or key[0] not in (243, 244, 245):
            raise ValueError(f"Duplicate or out-of-cohort item: {key}")
        if any(not r or any(c not in LETTERS | {".", "?"} for c in r) for r in item["rows"]):
            raise ValueError(f"Invalid literal row: {key}")
        out[key] = item
    return out


def consensus(a, b):
    counts = collections.Counter()
    grids, issues = [], []
    for key in sorted(set(a) | set(b)):
        if key not in a or key not in b:
            issues.append({"locator": key, "reason": "grid missing from one reader"})
            continue
        x, y = a[key], b[key]
        ra, rb = x["rows"], y["rows"]
        if not ra or [len(r) for r in ra] != [len(r) for r in rb]:
            issues.append({"locator": key, "reason": "empty or row lengths disagree",
                           "shape_a": list(map(len, ra)), "shape_b": list(map(len, rb))})
            continue
        counts["same_shape_grids"] += 1
        merged, conflicts = [], []
        for i, (left, right) in enumerate(zip(ra, rb), 1):
            row = ""
            for j, (raw_x, raw_y) in enumerate(zip(left, right), 1):
                u, v = raw_x.replace("J", "I"), raw_y.replace("J", "I")
                if raw_x == raw_y and raw_x in LETTERS:
                    counts["literal_agreed_letters"] += 1
                counts["j_to_i_positions"] += raw_x == "J" or raw_y == "J"
                if u == v == ".":
                    counts["agreed_blanks"] += 1
                else:
                    counts["potentially_lettered_positions"] += 1
                    if u == v and u in LETTERS:
                        counts["normalized_agreed_letters"] += 1
                    elif "?" in (u, v):
                        counts["unresolved_positions"] += 1
                    else:
                        counts["conflicting_positions"] += 1
                agreed = u == v and u != "?"
                row += u if agreed else "?"
                if not agreed:
                    conflicts.append({"row": i, "column": j, "reader_a": raw_x, "reader_b": raw_y})
            merged.append(row)
        chapter = x.get("chapter") if x.get("chapter") == y.get("chapter") else None
        number = x.get("number") if x.get("number") == y.get("number") else None
        valid_id = type(chapter) is int and chapter > 0 and type(number) is int and number > 0
        grids.append({"physical_page": key[0], "grid_index": key[1],
                      "source_id": f"{chapter}/{number}" if valid_id else None,
                      "source_id_readings": [[x.get("chapter"), x.get("number")], [y.get("chapter"), y.get("number")]],
                      "complete_both": x.get("complete") is True and y.get("complete") is True,
                      "rows": merged, "conflicts": conflicts})
    counts["reader_a_grids"] = len(a)
    counts["reader_b_grids"] = len(b)
    return grids, dict(counts), issues


def evaluate(grids, mathers, p13, p20):
    tally = collections.defaultdict(collections.Counter)
    aligned, exclusions, cells = [], [], []
    ids = collections.Counter(g["source_id"] for g in grids if g["source_id"])
    for g in grids:
        sid, rows = g["source_id"], g["rows"]
        n = len(rows)
        reason = None
        if not g["complete_both"] or n < 3 or any(len(r) != n for r in rows):
            reason = "not a complete coordinate-bearing grid"
        elif not sid:
            reason = "readers did not establish a source chapter/number"
        elif ids[sid] != 1:
            reason = "duplicate source identifier; no primary join"
        elif sid not in mathers or len(mathers[sid]) != n or any(len(r) != n for r in mathers[sid]):
            reason = "Mathers identifier absent or shape differs"
        if reason:
            exclusions.append({"physical_page": g["physical_page"], "grid_index": g["grid_index"], "source_id": sid, "reason": reason})
            continue
        m = mathers[sid]
        both = [(i, j) for i in range(n) for j in range(n) if m[i][j] in LETTERS and rows[i][j] in LETTERS]
        same = sum(m[i][j] == rows[i][j] for i, j in both)
        if not both or same / len(both) < 0.5:
            exclusions.append({"physical_page": g["physical_page"], "grid_index": g["grid_index"], "source_id": sid,
                               "reason": "visible agreement below half", "same": same, "compared": len(both)})
            continue
        aligned.append({"source_id": sid, "physical_page": g["physical_page"], "grid_index": g["grid_index"],
                        "visible_agreement": [same, len(both)], "prediction_positions": len(p13.get(sid, []))})
        for pred in p13.get(sid, []):
            i, j = pred["row"], pred["column"]
            if m[i][j] != ".":
                raise ValueError("Frozen prediction is not on a Mathers blank")
            truth = rows[i][j]
            zone = "interior" if pred["interior"] else "border"
            guesses = {"sym_TA": pred["sym_TA"], "letter_class_mode": pred["letter_filler"],
                       "letter_global": pred["letter_global"], "letter_chapter": p20.get(sid, {}).get((i, j)),
                       "class_checkerboard": pred["class_checkerboard"]}
            outcomes = {}
            for model, guess in guesses.items():
                if truth not in LETTERS:
                    outcome = "unreadable_truth" if truth == "?" else "blank_truth"
                elif guess is None:
                    outcome = "abstain"
                else:
                    actual = ("V" if truth in VOWELS else "C") if model == "class_checkerboard" else truth
                    outcome = "correct" if guess == actual else "wrong"
                outcomes[model] = outcome
                tally[f"{model}|{zone}"][outcome] += 1
            cells.append({"source_id": sid, "physical_page": g["physical_page"], "grid_index": g["grid_index"],
                          "row": i + 1, "column": j + 1, "zone": zone, "dresden_consensus": truth,
                          "predictions": guesses, "outcomes": outcomes})
    return {"aligned": aligned, "excluded": exclusions,
            "tally": {k: dict(v) for k, v in sorted(tally.items())}, "cells": cells}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    freeze = json.loads((HERE / "freeze.json").read_text())
    for rel, expected in freeze["sha256"].items():
        if sha(ROOT / rel) != expected:
            raise ValueError(f"Frozen input changed: {rel}")
    manifest = json.loads((HERE / "image-manifest.json").read_text())
    sources = {im["physical_page"]: im for im in manifest["images"]}
    for im in sources.values():
        if sha(PUZZLE / "sources/cache/dresden-n111" / im["filename"]) != im["sha256"]:
            raise ValueError("Source image changed")
    grids, agreement, issues = consensus(readers(HERE / "readings-A.json"), readers(HERE / "readings-B.json"))
    for g in grids:
        im = sources[g["physical_page"]]
        g.update(witness="Mscr.Dresd.N.111", source_url=im["original_image"], page_label=im["page_label"], image_sha256=im["sha256"])
    mathers = {s["id"]: [r.upper() for r in s["rows"]] for s in json.loads((PUZZLE / "sources/mathers-squares.json").read_text())["squares"]}
    p13 = {s["id"]: s["cells"] for s in json.loads((HERE.parent / "13-dehn-witness-test/predictions.json").read_text())["squares"]}
    p20 = {s["id"]: {(c["row"], c["column"]): c["letter_chapter"] for c in s["cells"]}
           for s in json.loads((HERE.parent / "20-warburg-witness/predictions.json").read_text())["squares"]}
    result = evaluate(grids, mathers, p13, p20)
    interior = result["tally"].get("class_checkerboard|interior", {})
    evaluated = interior.get("correct", 0) + interior.get("wrong", 0)
    result.update(agreement=agreement, reading_issues=issues, evaluated_interior_cells=evaluated,
                  interpretation="Bounded manuscript collation; no full-generator or historical-independence claim",
                  threshold_assessment="Insufficient interior cells for the frozen A/B criterion" if evaluated < 50 else
                  "Report model counts; this opening-page pilot is not a general construction verdict",
                  reader_sha256={name: sha(HERE / name) for name in ("readings-A.json", "readings-B.json")})
    outputs = {"results.json": result, "collation.json": {"scope": "Three-page literal consensus, not a corrected edition", "grids": grids}}
    for name, data in outputs.items():
        text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        path = HERE / name
        if args.check:
            if path.read_text() != text:
                raise ValueError(f"Does not reproduce: {name}")
        else:
            path.write_text(text)
    print("Pilot reproduces" if args.check else json.dumps({"agreement": agreement, "aligned": result["aligned"],
          "excluded": result["excluded"], "tally": result["tally"], "assessment": result["threshold_assessment"]}, indent=2))


if __name__ == "__main__":
    main()

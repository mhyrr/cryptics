#!/usr/bin/env python3
"""Audit the frozen index-key comparison without changing primary outputs."""
import argparse
import collections
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
LETTERS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_reader(name):
    data = json.loads((HERE / name).read_text())
    return {(item["physical_page"], item["grid_index"]): item for item in data["items"]}


def exact_cross_matches(item, other, own_key):
    return [list(key) for key, candidate in sorted(other.items())
            if key[0] == own_key[0] and key != own_key and candidate["rows"] == item["rows"]]


def audit(a, b):
    keys = sorted(set(a) | set(b))
    totals = collections.Counter()
    shape_disagreements = []
    contradicted = []
    exact_same_index, exact_cross_index = [], []

    for ka, item_a in sorted(a.items()):
        for kb, item_b in sorted(b.items()):
            if ka[0] != kb[0] or item_a["rows"] != item_b["rows"]:
                continue
            match = {"reader_a": list(ka), "reader_b": list(kb)}
            (exact_same_index if ka == kb else exact_cross_index).append(match)

    for key in keys:
        totals["union_local_keys"] += 1
        if key not in a or key not in b:
            totals["missing_from_one_reader"] += 1
            continue
        totals["paired_local_keys"] += 1
        ra, rb = a[key]["rows"], b[key]["rows"]
        shape_a, shape_b = list(map(len, ra)), list(map(len, rb))
        if not ra or shape_a != shape_b:
            totals["dropped_shape_disagreement"] += 1
            shape_disagreements.append({"local_key": list(key), "shape_a": shape_a, "shape_b": shape_b})
            continue

        totals["same_shape_pairs"] += 1
        pair = collections.Counter()
        for left, right in zip(ra, rb):
            for raw_a, raw_b in zip(left, right):
                x, y = raw_a.replace("J", "I"), raw_b.replace("J", "I")
                if raw_a == raw_b and raw_a in LETTERS:
                    pair["literal_agreed_letters"] += 1
                pair["j_to_i_positions"] += raw_a == "J" or raw_b == "J"
                if x == y == ".":
                    pair["agreed_blanks"] += 1
                    continue
                pair["potentially_lettered_positions"] += 1
                if x == y and x in LETTERS:
                    pair["normalized_agreed_letters"] += 1
                elif "?" in (x, y):
                    pair["unresolved_positions"] += 1
                else:
                    pair["conflicting_positions"] += 1
        totals.update(pair)

        a_elsewhere = exact_cross_matches(a[key], b, key)
        b_elsewhere = exact_cross_matches(b[key], a, key)
        if a_elsewhere or b_elsewhere:
            totals["same_shape_pairs_contradicted_by_exact_cross_index_match"] += 1
            totals["conflicts_in_contradicted_pairs"] += pair["conflicting_positions"]
            totals["unresolved_in_contradicted_pairs"] += pair["unresolved_positions"]
            contradicted.append({"local_key": list(key),
                                 "reader_a_exact_elsewhere_in_b": a_elsewhere,
                                 "reader_b_exact_elsewhere_in_a": b_elsewhere,
                                 "conflicting_positions": pair["conflicting_positions"],
                                 "unresolved_positions": pair["unresolved_positions"]})

    totals["exact_same_index_full_grid_matches"] = len(exact_same_index)
    totals["exact_cross_index_full_grid_matches"] = len(exact_cross_index)
    for name in ("agreed_blanks", "j_to_i_positions", "literal_agreed_letters"):
        totals[name] += 0

    return {
        "scope": "Audit of the preserved local-index comparison; no source-image adjudication",
        "method": "A same-shape local-index pair is contradicted when either full raw grid has an exact same-page match at a different index in the other reader.",
        "input_sha256": {name: sha(HERE / name) for name in
                          ("readings-A.json", "readings-B.json", "score.py", "results.json", "collation.json")},
        "counts": dict(sorted(totals.items())),
        "shape_disagreements": shape_disagreements,
        "same_shape_pairs_contradicted_by_exact_cross_index_match": contradicted,
        "exact_full_grid_matches": {"same_index": exact_same_index, "cross_index": exact_cross_index},
    }


def audit_posthoc(a, b):
    results = json.loads((HERE / "posthoc-results.json").read_text())
    collation = json.loads((HERE / "posthoc-collation.json").read_text())
    alignment = json.loads((HERE / "alignment.json").read_text())
    mathers_path = HERE.parents[1] / "sources/mathers-squares.json"
    sizes = {s["id"]: len(s["rows"]) for s in json.loads(mathers_path.read_text())["squares"]}
    alignment_by_locator = {item["locator_id"]: item for item in alignment["items"]}

    status = collections.Counter()
    coordinate_kind = collections.Counter()
    ragged_same_shape = []
    raw_preserved = True
    for grid in collation["grids"]:
        coordinate_kind[grid["coordinate_kind"]] += 1
        status.update(cell["status"] for cell in grid["cells"] or [])
        item = alignment_by_locator[grid["locator_id"]]
        raw_preserved &= (grid["reader_a"] == a[(item["physical_page"], item["reader_a_grid_index"])] and
                          grid["reader_b"] == b[(item["physical_page"], item["reader_b_grid_index"])])
        rows_a, rows_b = grid["reader_a"]["rows"], grid["reader_b"]["rows"]
        shape_a, shape_b = list(map(len, rows_a)), list(map(len, rows_b))
        if shape_a == shape_b and any(length != len(rows_a) for length in shape_a):
            ragged_same_shape.append({"locator_id": grid["locator_id"], "source_id": grid["source_id"],
                                      "shape": shape_a, "positions": sum(shape_a)})

    cells = results["cells"]
    models = list(cells[0]["outcomes"]) if cells else []
    by_zone = {}
    for zone in ("border", "interior"):
        selected = [cell for cell in cells if cell["zone"] == zone]
        orbits = collections.defaultdict(list)
        for cell in selected:
            n = sizes[cell["source_id"]]
            i, j = cell["row"] - 1, cell["column"] - 1
            key = min((i, j), (j, i), (n - 1 - i, n - 1 - j), (n - 1 - j, n - 1 - i))
            orbits[(cell["source_id"], key)].append(cell)
        by_zone[zone] = {
            "target_positions": len(selected),
            "target_TA_orbits": len(orbits),
            "models": {model: {
                "outcomes": dict(sorted(collections.Counter(cell["outcomes"][model] for cell in selected).items())),
                "target_orbits_all_correct": sum(
                    all(cell["outcomes"][model] == "correct" for cell in orbit)
                    for orbit in orbits.values())
            } for model in models},
        }

    return {
        "input_sha256": {name: sha(HERE / name) for name in
                          ("alignment.json", "locator-audit.json", "posthoc.py",
                           "posthoc-results.json", "posthoc-collation.json")},
        "raw_reader_records_preserved": raw_preserved,
        "counts": {
            "collated_grids": len(collation["grids"]),
            "aligned_mathers_grids": len(results["aligned"]),
            "excluded_mathers_grids": len(results["excluded"]),
            "target_cells": len(cells),
            "agreed_letters": status["agreed_letter"],
            "conflicts": status["conflict"],
            "unknowns": status["unknown"],
            "square_coordinate_grids": coordinate_kind["square_row_column"],
            "row_group_only_grids": coordinate_kind["row_group_position_only"],
        },
        "ragged_same_shape_grids": ragged_same_shape,
        "prediction_coverage_by_zone": by_zone,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    a, b = load_reader("readings-A.json"), load_reader("readings-B.json")
    output = audit(a, b)
    if (HERE / "posthoc-results.json").exists() and (HERE / "posthoc-collation.json").exists():
        output["posthoc_audit"] = audit_posthoc(a, b)
    text = json.dumps(output, indent=2, ensure_ascii=False) + "\n"
    path = HERE / "audit-scorer.json"
    if args.check:
        if path.read_text() != text:
            raise ValueError("Does not reproduce: audit-scorer.json")
        print("Scorer audit reproduces")
    else:
        path.write_text(text)
        print(json.dumps(output["counts"], indent=2))


if __name__ == "__main__":
    main()

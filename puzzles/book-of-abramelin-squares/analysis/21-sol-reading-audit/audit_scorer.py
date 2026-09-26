#!/usr/bin/env python3
"""Reproduce the numerical diagnostics in SCORER-AUDIT.md.

Usage: python3 audit_scorer.py [--check]
"""
import collections
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
E20 = HERE.parent / "20-warburg-witness"
PUZZLE = HERE.parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


frozen = load("audit_e20_frozen", E20 / "score.py")
checked = load("audit_e20_checked", E20 / "score_checked.py")


def normalize(readings):
    return {key: [row.replace("J", "I") for row in rows]
            for key, rows in readings.items()}


def gate_summary(gate):
    return {
        "agreed": gate["agreed"],
        "potentially_lettered": gate["potentially_lettered"],
        "agreed_share": gate["agreed_share"],
        "readable": gate["readable"],
        "unscored_printed_positions": gate["corrected_counts"].get(
            "unscored_printed_positions", 0),
    }


def main():
    raw_a = checked.read_items(E20 / "readings-A.json")
    raw_b = checked.read_items(E20 / "readings-B.json")
    norm_a, norm_b = normalize(raw_a), normalize(raw_b)
    raw_gate = checked.gate(raw_a, raw_b)
    norm_gate = checked.gate(norm_a, norm_b)

    items, merge_stats = frozen.merge(norm_a, norm_b)
    mathers = {square["id"]: [row.upper() for row in square["rows"]]
               for square in json.loads(
                   (PUZZLE / "sources/mathers-squares.json").read_text())["squares"]}
    p13 = {square["id"]: square for square in json.loads(
        (HERE.parent / "13-dehn-witness-test/predictions.json").read_text())["squares"]}

    regular = []
    aligned = []
    for (chapter, number), item in sorted(items.items()):
        rows = item["grid"]
        if rows is None:
            continue
        sid = f"{chapter}/{number}"
        regular.append(sid)
        m = mathers.get(sid)
        if not m or len(m) != len(rows) or any(len(row) != len(rows) for row in m):
            continue
        both = [(i, j) for i in range(len(m)) for j in range(len(m))
                if m[i][j].isalpha() and rows[i][j].isalpha()]
        same = sum(m[i][j] == rows[i][j] for i, j in both)
        if both and same / len(both) >= 0.5:
            aligned.append((sid, rows))

    coverage = collections.defaultdict(collections.Counter)
    for sid, rows in aligned:
        for cell in p13.get(sid, {}).get("cells", []):
            zone = "interior" if cell["interior"] else "border"
            truth = rows[cell["row"]][cell["column"]]
            kind = "letter" if truth.isalpha() else "unknown" if truth == "?" else "blank"
            coverage[zone][kind] += 1
            coverage[zone]["total"] += 1

    ragged = []
    denominator_dots = 0
    for key in sorted(raw_a):
        ga, _ = frozen.to_square(raw_a[key])
        gb, _ = frozen.to_square(raw_b[key])
        if ga is not None and gb is not None and len(ga) == len(gb):
            continue
        a_text, b_text = "".join(raw_a[key]), "".join(raw_b[key])
        chosen = a_text if len(a_text) >= len(b_text) else b_text
        denominator_dots += chosen.count(".")
        ragged.append(key)

    result = {
        "j_to_i": {
            "raw_j": {
                "reader_a": sum(row.count("J") for rows in raw_a.values() for row in rows),
                "reader_b": sum(row.count("J") for rows in raw_b.values() for row in rows),
            },
            "raw_gate": gate_summary(raw_gate),
            "normalized_gate": gate_summary(norm_gate),
        },
        "ragged_gate_denominator": {
            "items": len(ragged),
            "unscored_printed_positions": raw_gate["corrected_counts"]["unscored_printed_positions"],
            "printed_placeholders_in_selected_longer_strings": denominator_dots,
            "rule": "For each unscored item, max(total characters from reader A, total characters from reader B).",
        },
        "alignment": {
            "regular_consensus_grids": len(regular),
            "primary_pairs_passing_gate": len(aligned),
        },
        "blind_cell_coverage": {zone: dict(counts) for zone, counts in sorted(coverage.items())},
        "merge_item_counts": {key: value for key, value in merge_stats.items()
                              if key.startswith("items_")},
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    output = HERE / "audit-scorer.json"
    if "--check" in sys.argv:
        if output.read_text() != text:
            raise SystemExit("audit-scorer.json does not reproduce")
        print("audit-scorer.json reproduces")
    else:
        output.write_text(text)
        print(text, end="")


if __name__ == "__main__":
    main()

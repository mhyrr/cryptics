#!/usr/bin/env python3
"""Compare independent transcriptions without converting word lists to grids."""
import argparse
import collections
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
LETTERS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path, keyed_by_page):
    data = json.loads(path.read_text())
    items = {}
    for item in data["items"]:
        key = (item["chapter"], item["number"])
        if keyed_by_page:
            key += (item["page"],)
        if key in items:
            raise ValueError(f"Duplicate {key} in {path.name}")
        rows = item["rows"]
        if not isinstance(rows, list) or any(not isinstance(r, str) or
                any(c not in LETTERS | {".", "?"} for c in r) for r in rows):
            raise ValueError(f"Invalid rows for {key} in {path.name}")
        items[key] = rows
    return data, items


def normalize(rows, merge_ij):
    return [r.replace("J", "I") if merge_ij else r for r in rows]


def shape(rows):
    return tuple(map(len, rows))


def pair(a, b, cohort, merge_ij):
    counts = collections.Counter()
    differences, excluded = [], []
    for key in cohort:
        ra, rb = normalize(a.get(key, []), merge_ij), normalize(b.get(key, []), merge_ij)
        if not ra or not rb:
            counts["empty_or_missing_items"] += 1
            excluded.append({"item": key, "reason": "empty or missing"})
            continue
        if shape(ra) != shape(rb):
            counts["shape_disagreement_items"] += 1
            excluded.append({"item": key, "reason": "row lengths differ", "left_shape": shape(ra), "right_shape": shape(rb)})
            continue
        counts["same_shape_items"] += 1
        regular = len(ra[0]) >= 3 and len(ra) <= len(ra[0]) and all(len(r) == len(ra[0]) for r in ra)
        counts["same_shape_regular_items" if regular else "same_shape_ragged_items"] += 1
        for i, (left, right) in enumerate(zip(ra, rb), 1):
            for j, (x, y) in enumerate(zip(left, right), 1):
                if x == y == ".":
                    counts["agreed_blank_positions"] += 1
                    continue
                counts["potentially_lettered_positions"] += 1
                if x == y and x in LETTERS:
                    counts["agreed_letters"] += 1
                elif "?" in (x, y):
                    counts["unresolved_positions"] += 1
                else:
                    counts["letter_or_blank_conflicts"] += 1
                if x != y or x == "?":
                    differences.append({"item": key, "row_group": i, "position": j, "left": x, "right": y})
    total = counts["potentially_lettered_positions"]
    return {"counts": dict(counts), "agreement_on_comparable_positions": counts["agreed_letters"] / total if total else None,
            "excluded": excluded, "differences": differences}


def cross_consensus(sa, sb, oa, ob, cohort):
    counts = collections.Counter()
    conflicts = []
    for key in cohort:
        rows = [normalize(x.get(key, []), True) for x in (sa, sb, oa, ob)]
        if not all(rows) or len({shape(r) for r in rows}) != 1:
            counts["excluded_missing_or_shape_items"] += 1
            continue
        counts["four_way_same_shape_items"] += 1
        for i, groups in enumerate(zip(*rows), 1):
            for j, (a, b, c, d) in enumerate(zip(*groups), 1):
                if a == b and a in LETTERS and c == d and c in LETTERS:
                    counts["both_pairs_agree_positions"] += 1
                    counts["pairs_agree_with_each_other" if a == c else "pairs_conflict"] += 1
                    if a != c:
                        conflicts.append({"item": key, "row_group": i, "position": j, "sol": a, "opus": c})
                else:
                    counts["not_jointly_agreed_letters"] += 1
    return {"counts": dict(counts), "conflicts": conflicts,
            "interpretation": "Agreement between transcriptions, not adjudicated historical truth"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    work = json.loads((HERE / "worklist.json").read_text())
    expected, cohort, fragments = set(), [], []
    for page in work["pages"]:
        if sha(Path(page["image"])) != page["sha256"]:
            raise ValueError(f"Crop changed: {page['page']}")
        for item in page["items"]:
            key = (item["chapter"], item["number"], page["page"])
            expected.add(key)
            (cohort if item["full_single_page"] else fragments).append(key)
    paths = [HERE / "readings-sol-A.json", HERE / "readings-sol-B.json",
             HERE.parent / "20-warburg-witness/readings-A.json", HERE.parent / "20-warburg-witness/readings-B.json"]
    loaded = [load(p, i < 2) for i, p in enumerate(paths)]
    for meta, items in loaded[:2]:
        if set(meta["pages_completed"]) != {p["page"] for p in work["pages"]} or set(items) != expected:
            raise ValueError("Sol reader coverage differs from the frozen worklist")
    sa, sb = [x[1] for x in loaded[:2]]
    oa, ob = [{key: x[1].get(key[:2], []) for key in cohort} for x in loaded[2:]]
    out = {"scope": "Exposed print; independent transcription audit, not a new historical prediction test",
           "input_sha256": {str(p.relative_to(HERE.parent)): sha(p) for p in paths},
           "worklist_sha256": sha(HERE / "worklist.json"), "selected_pages": len(work["pages"]),
           "selected_blocks": len(expected), "full_single_page_items": len(cohort), "excluded_fragments": fragments,
           "sol_literal": pair(sa, sb, cohort, False), "sol_ij_merged": pair(sa, sb, cohort, True),
           "opus_literal_same_cohort": pair(oa, ob, cohort, False),
           "opus_ij_merged_same_cohort": pair(oa, ob, cohort, True),
           "cross_model_consensus": cross_consensus(sa, sb, oa, ob, cohort)}
    text = json.dumps(out, indent=2) + "\n"
    target = HERE / "comparison.json"
    if args.check:
        if target.read_text() != text:
            raise ValueError("Comparison does not reproduce")
        print("Comparison reproduces")
    else:
        target.write_text(text)
        print(json.dumps({k: v["counts"] for k, v in out.items() if isinstance(v, dict) and "counts" in v}, indent=2))


if __name__ == "__main__":
    main()

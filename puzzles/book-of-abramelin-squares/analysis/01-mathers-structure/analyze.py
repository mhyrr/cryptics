#!/usr/bin/env python3
"""Exact structural tests. Null means an observed blank, never a guessed letter."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path


TRANSFORMS = {
    "transpose": lambda r, c, n: (c, r),
    "anti_transpose": lambda r, c, n: (n - 1 - c, n - 1 - r),
    "half_turn": lambda r, c, n: (n - 1 - r, n - 1 - c),
    "row_reflection": lambda r, c, n: (n - 1 - r, c),
    "column_reflection": lambda r, c, n: (r, n - 1 - c),
}
FAMILIES = {key: (key,) for key in TRANSFORMS}
FAMILIES["transpose_and_half_turn"] = ("transpose", "half_turn")


def validate(grid):
    n = len(grid)
    if n < 2 or any(len(row) != n for row in grid):
        raise ValueError("Expected an explicitly square grid; do not pad ragged rows")
    if any(x is not None and (not isinstance(x, str) or len(x) != 1 or
                             not "A" <= x <= "Z") for row in grid for x in row):
        raise ValueError("Cells must be A–Z or null; preserve anomalies outside analysis")


def orbits(n, family):
    unseen = {(r, c) for r in range(n) for c in range(n)}
    groups = []
    while unseen:
        seed = min(unseen)
        group, pending = {seed}, [seed]
        while pending:
            r, c = pending.pop()
            for name in FAMILIES[family]:
                pos = TRANSFORMS[name](r, c, n)
                if pos not in group:
                    group.add(pos)
                    pending.append(pos)
        unseen -= group
        groups.append(sorted(group))
    return groups


def constrain(grid, family):
    """Never select a majority letter or resolve a conflict by guessing."""
    groups = orbits(len(grid), family)
    conflicts, fills, free = [], [], []
    constrained_known = comparable_pairs = agreeing_pairs = 0
    for group in groups:
        observed = [(r, c, grid[r][c]) for r, c in group if grid[r][c] is not None]
        values = {x for _, _, x in observed}
        if len(group) > 1:
            constrained_known += len(observed)
        for i, a in enumerate(observed):
            for b in observed[i + 1:]:
                comparable_pairs += 1
                agreeing_pairs += a[2] == b[2]
        if len(values) > 1:
            conflicts.append({"cells": observed})
        elif not values:
            free.append(group)
        else:
            letter = next(iter(values))
            fills.extend({"row": r, "column": c, "letter": letter}
                         for r, c in group if grid[r][c] is None)
    # Local fills survive in the audit, but a conflicted whole-grid rule is rejected.
    return {"compatible": not conflicts, "orbit_count": len(groups),
            "free_orbits": free, "conflicts": conflicts,
            "conditional_fills": fills, "constrained_known_cells": constrained_known,
            "comparable_pairs": comparable_pairs, "agreeing_pairs": agreeing_pairs}


def generators(grid):
    """Fit-free exact tests on complete grids; every interior cell must match."""
    n = len(grid)
    if any(x is None for row in grid for x in row):
        return None
    seed = grid[0]
    shifts = [k for k in range(n) if all(
        grid[r][c] == seed[(c + k * r) % n]
        for r in range(n) for c in range(n))]
    arbitrary = all(any(row == seed[k:] + seed[:k] for k in range(n)) for row in grid)
    val = lambda x: ord(x) - ord("A")
    a = val(grid[0][0])
    # Compare interiors only: boundary rows/columns are supplied inputs.
    affine = {}
    for sr in (1, -1):
        for sc in (1, -1):
            name = f"row_{sr:+d}_column_{sc:+d}"
            wrong = sum(val(grid[r][c]) != (
                a + sr * (val(grid[r][0]) - a) + sc * (val(grid[0][c]) - a)
            ) % 26 for r in range(1, n) for c in range(1, n))
            affine[name] = {"mismatches": wrong, "tested": (n - 1) ** 2}
    return {"fixed_cyclic_steps": shifts, "arbitrary_row_rotations": arbitrary,
            "boundary_affine_mod26": affine}


def masked_check(grids, family):
    """Hide interiors and bottom/right edges; never select on the hidden answer."""
    totals = Counter(grids=0, rejected=0, hidden=0, predicted=0, correct=0,
                     visible_mode_correct_all_hidden=0, visible_mode_correct_on_predictions=0)
    for grid in grids:
        n = len(grid)
        masked = [[cell if r == 0 or c == 0 else None
                   for c, cell in enumerate(row)] for r, row in enumerate(grid)]
        visible = Counter(x for row in masked for x in row if x is not None)
        mode = min(visible, key=lambda x: (-visible[x], x))
        totals["grids"] += 1
        totals["hidden"] += (n - 1) ** 2
        totals["visible_mode_correct_all_hidden"] += sum(
            grid[r][c] == mode for r in range(1, n) for c in range(1, n))
        fit = constrain(masked, family)
        if not fit["compatible"]:
            totals["rejected"] += 1
            continue
        for p in fit["conditional_fills"]:
            answer = grid[p["row"]][p["column"]]
            totals["predicted"] += 1
            totals["correct"] += p["letter"] == answer
            totals["visible_mode_correct_on_predictions"] += mode == answer
    totals["wrong"] = totals["predicted"] - totals["correct"]
    totals["abstained"] = totals["hidden"] - totals["predicted"]
    return dict(totals)


def run(corpus):
    details, excluded, seen = [], [], set()
    for square in corpus["squares"]:
        sid = square["id"]
        if sid in seen:
            raise ValueError(f"Duplicate square ID: {sid}")
        seen.add(sid)
        if square.get("exclude_reason"):
            excluded.append({"id": sid, "reason": square["exclude_reason"]})
            continue
        grid = square["grid"]
        validate(grid)
        letters = Counter(x for row in grid for x in row if x is not None)
        details.append({"id": sid, "dimension": len(grid),
                        "blank_cells": len(grid) ** 2 - sum(letters.values()),
                        "letter_counts": dict(sorted(letters.items())),
                        "symmetry": {f: constrain(grid, f) for f in FAMILIES},
                        "generators": generators(grid)})
    complete = [s for s in details if s["blank_cells"] == 0]
    incomplete = [s for s in details if s["blank_cells"] > 0]
    counts = Counter()
    for s in details:
        counts.update(s["letter_counts"])
    summary = {
        "source_records": len(corpus["squares"]), "analyzed": len(details),
        "excluded": excluded, "complete": len(complete), "incomplete": len(incomplete),
        "dimensions": dict(sorted(Counter(s["dimension"] for s in details).items())),
        "known_cells": sum(counts.values()),
        "blank_cells": sum(s["blank_cells"] for s in details),
        "letter_counts": dict(sorted(counts.items())),
        "complete_exact_symmetry": {
            f: sum(s["symmetry"][f]["compatible"] for s in complete) for f in FAMILIES},
        "incomplete_symmetry": {
            f: {"compatible_grids": sum(s["symmetry"][f]["compatible"] for s in incomplete),
                "conditional_fills_in_compatible_grids": sum(
                    len(s["symmetry"][f]["conditional_fills"]) for s in incomplete
                    if s["symmetry"][f]["compatible"])} for f in FAMILIES},
        "complete_fixed_cyclic": sum(bool(s["generators"]["fixed_cyclic_steps"]) for s in complete),
        "complete_arbitrary_row_rotations": sum(s["generators"]["arbitrary_row_rotations"] for s in complete),
        "complete_boundary_affine": {
            f"row_{sr:+d}_column_{sc:+d}": sum(
                s["generators"]["boundary_affine_mod26"][f"row_{sr:+d}_column_{sc:+d}"]["mismatches"] == 0
                for s in complete) for sr in (1, -1) for sc in (1, -1)},
    }
    grids = [s["grid"] for s in corpus["squares"] if not s.get("exclude_reason")
             and all(x is not None for row in s["grid"] for x in row)]
    summary["masked_complete_grid_diagnostic"] = {
        f: masked_check(grids, f) for f in ("transpose", "half_turn", "transpose_and_half_turn")}
    for s in details:
        if s["id"] == "25/3":
            fit = s["symmetry"]["transpose_and_half_turn"]
            summary["maiam_25_3_example"] = {
                "known": sum(s["letter_counts"].values()), "blank": s["blank_cells"],
                "conditional_fills": len(fit["conditional_fills"]),
                "free_orbits": len(fit["free_orbits"]),
                "compatible_completions_over_A_Z": 26 ** len(fit["free_orbits"]) if fit["compatible"] else 0}
    return {"summary": summary, "squares": details,
            "caution": "Exact descriptive tests on one digital transmission; conditional fills are not verified readings. Coordinates are zero-based."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raw = args.corpus.read_bytes()
    result = run(json.loads(raw))
    result["input_sha256"] = hashlib.sha256(raw).hexdigest()
    # One square per line keeps the complete audit small and diffable.
    detail = result.pop("squares")
    prefix = json.dumps(result, indent=2, ensure_ascii=False)
    args.output.write_text(prefix[:-2] + ',\n  "squares": [\n' +
                           ",\n".join("    " + json.dumps(s, ensure_ascii=False) for s in detail) +
                           "\n  ]\n}\n")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()

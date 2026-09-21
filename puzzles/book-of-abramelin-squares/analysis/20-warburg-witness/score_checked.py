#!/usr/bin/env python3
"""Pre-reading safeguards around the unchanged experiment 20 scorer.

Run: python3 score_checked.py READER_DIRECTORY [--check]
The directory must contain readings-A.json and readings-B.json.
"""
import argparse
import collections
import hashlib
import importlib.util
import json
import pathlib
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
spec = importlib.util.spec_from_file_location("warburg_frozen", HERE / "score.py")
frozen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frozen)
original_merge = frozen.merge


def read_items(path):
    data = json.loads(path.read_text())
    items = {}
    for item in data["items"]:
        key = (item["chapter"], item["number"])
        if not all(type(x) is int and x > 0 for x in key):
            raise ValueError(f"{path.name}: invalid identifier {key}")
        if key in items:
            raise ValueError(f"{path.name}: duplicate identifier {key}")
        if type(item.get("page")) is not int or not 1 <= item["page"] <= 388:
            raise ValueError(f"{path.name}: missing/invalid PDF page for {key}")
        rows = item["rows"]
        if not isinstance(rows, list) or not all(isinstance(r, str) for r in rows):
            raise ValueError(f"{path.name}: invalid rows for {key}")
        if any(not r or any(c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ.?" for c in r) for r in rows):
            raise ValueError(f"{path.name}: noncanonical symbols for {key}")
        if not rows and not item.get("note"):
            raise ValueError(f"{path.name}: empty item needs an explanation: {key}")
        items[key] = rows
    return items


def corrected_merge(a, b):
    """Keep frozen consensus; fix the gate's denominator without filling cells."""
    if set(a) != set(b):
        raise ValueError("Reader item identifiers differ; reconcile coverage before scoring")
    items, legacy = original_merge(a, b)
    stats = collections.Counter({k: v for k, v in legacy.items() if k.startswith("items_")})
    for key in sorted(a):
        ga, _ = frozen.to_square(a[key])
        gb, _ = frozen.to_square(b[key])
        if ga is None or gb is None or len(ga) != len(gb):
            # Ragged items have no reliable cell geometry. They cannot rescue
            # the cell-legibility gate; their agreed top rows remain preserved.
            stats["unscored_printed_positions"] += max(sum(map(len, a[key])), sum(map(len, b[key])))
            continue
        n = len(ga)
        for i in range(n):
            for j in range(n):
                x, y = ga[i][j], gb[i][j]
                zone = "top" if i == 0 else "border" if i == n - 1 or j in (0, n - 1) else "interior"
                if x == y == ".":
                    continue
                stats[f"lettered_{zone}"] += 1
                stats[f"agreed_{zone}"] += x == y and x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                stats[f"both_unreadable_{zone}"] += x == y == "?"
    return items, stats


def gate(a, b):
    _, old = original_merge(a, b)
    _, new = corrected_merge(a, b)
    lettered = sum(v for k, v in new.items() if k.startswith("lettered_"))
    # A ragged item cannot be counted as a legible square. Conservatively
    # retain its printed positions in the whole-packet gate denominator.
    denominator = lettered + new["unscored_printed_positions"]
    agreed = sum(v for k, v in new.items() if k.startswith("agreed_"))
    return {"original_counts": dict(old), "corrected_counts": dict(new),
            "agreed": agreed, "potentially_lettered": denominator,
            "agreed_share": agreed / denominator if denominator else None,
            "readable": bool(denominator) and agreed / denominator >= 0.5}


def verify_inputs():
    manifest = json.loads((HERE / "input-manifest.json").read_text())
    for rel, digest in manifest["sha256"].items():
        actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        if actual != digest:
            raise ValueError(f"Frozen input changed: {rel}")
    freeze = json.loads((HERE / "freeze.json").read_text())
    for path, key in ((HERE / "predictions.json", "predictions_sha256"),
                      (HERE.parent / "13-dehn-witness-test/predictions.json", "exp13_predictions_sha256")):
        if hashlib.sha256(path.read_bytes()).hexdigest() != freeze[key]:
            raise ValueError(f"Prediction freeze mismatch: {path.name}")
    return manifest


def score(directory):
    manifest = verify_inputs()
    a = read_items(directory / "readings-A.json")
    b = read_items(directory / "readings-B.json")
    agreement = gate(a, b)
    provenance = {"reader_files_sha256": {name: hashlib.sha256((directory / name).read_bytes()).hexdigest()
                  for name in ("readings-A.json", "readings-B.json")},
                  "input_manifest_sha256": hashlib.sha256((HERE / "input-manifest.json").read_bytes()).hexdigest(),
                  "original_freeze_commit": manifest["original_freeze_commit"]}
    if not agreement["readable"]:
        return {"provenance": provenance, "legibility": agreement,
                "historical_scores_reported": False,
                "end_state": {"verdict": "witness unreadable under the corrected gate; no historical score"}}, None
    # Run unchanged models in a temporary directory, leaving both source
    # transcriptions and the original scorer untouched.
    with tempfile.TemporaryDirectory(prefix="abramelin-score-") as tmp:
        temp = pathlib.Path(tmp)
        for name in ("readings-A.json", "readings-B.json"):
            (temp / name).write_bytes((directory / name).read_bytes())
        old_read, old_merge = frozen.READ, frozen.merge
        try:
            frozen.READ, frozen.merge = temp, corrected_merge
            frozen.main()
        finally:
            frozen.READ, frozen.merge = old_read, old_merge
        result = json.loads((temp / "results.json").read_text())
        squares = json.loads((temp / "warburg-squares.json").read_text())
    result.update(provenance=provenance, legibility=agreement, historical_scores_reported=True)
    result["end_state"]["interpretation"] = (
        "Frozen numerical criterion only. A does not establish a full generator; "
        "B does not prove free choice or exclude untested rules.")
    result["exposure"] = "Prior chapter-4 moon/water exposure; chapter 5 caption development. Scores are not uniformly blind."
    squares["tier"] = "PRIMARY print, two reader transcriptions; see reader files for models and exposure. '?' means no agreed letter."
    squares["provenance"] = provenance
    return result, squares


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=pathlib.Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result, squares = score(args.directory)
    outputs = {"results-checked.json": result}
    if squares is not None:
        outputs["warburg-squares-checked.json"] = squares
    elif (args.directory / "warburg-squares-checked.json").exists():
        raise ValueError("Stale scored-square output exists beside an unreadable result; use a fresh output directory")
    for name, data in outputs.items():
        text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        path = args.directory / name
        if args.check:
            if path.read_text() != text:
                raise ValueError(f"Does not reproduce: {name}")
        else:
            path.write_text(text)
    print("Results reproduce" if args.check else result["end_state"])


if __name__ == "__main__":
    main()

"""Aggregate diagnostics for the 2911 bench. Output contains counts only."""
import argparse
from collections import Counter, defaultdict
import csv
from pathlib import Path
import re


def sheet_unit(unit):
    if unit in {"aa", "bb", "ss", "ff", "oo"}:
        return " ".join(unit)
    return unit


def group_counts(pair_rows, truth_rows, normalize):
    values = defaultdict(set)
    for row in truth_rows:
        if row["type"] == "none":
            continue
        known = values[row["unit"]]
        known.add(normalize(row["value"]))
        for value in re.findall(r"(?:^|;\s*)([a-z]+)\s*\(", row["also_covers"] or ""):
            known.add("" if value == "null" else normalize(value))

    counts = Counter(pairs=0, share_value=0, disjoint=0, unknown=0)
    seen = set()
    for row in pair_rows:
        left, right = sorted(sheet_unit(row[field].strip()) for field in ("left", "right"))
        if not left or not right:
            raise ValueError("empty pair member")
        if left == right or (left, right) in seen:
            continue
        seen.add((left, right))
        counts["pairs"] += 1
        if not values[left] or not values[right]:
            counts["unknown"] += 1
        elif values[left] & values[right]:
            counts["share_value"] += 1
        else:
            counts["disjoint"] += 1
    return counts


def key_counts(rows, units, kmap, normalize):
    by_sign = defaultdict(Counter)
    by_type = defaultdict(Counter)
    for row in rows:
        for item in row:
            kind = item["type"]
            if kind in {"clear", "unread", "missing"}:
                continue
            vals = [kmap.get(units[s]) for s in sorted(set(item["src"]))]
            verdict = "silent"
            if None not in vals:
                built = "".join(vals)
                matches = normalize(built) == normalize(item["value"] or "")
                verdict = "right" if matches and (built == "") == (kind == "null") else "wrong"
            by_type[kind][verdict] += 1
            by_sign[tuple(item["names"])][verdict] += 1

    by_frequency = defaultdict(Counter)
    for counts in by_sign.values():
        freq = sum(counts.values())
        band = "1-4" if freq < 5 else "5-9" if freq < 10 else "10-19" if freq < 20 else "20+"
        by_frequency[band].update(counts)
    return by_type, by_frequency


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("groups").add_argument("pairs", type=Path)
    key = commands.add_parser("key")
    key.add_argument("key", type=Path)
    key.add_argument("cipher", type=Path)
    args = parser.parse_args()

    import score
    if args.command == "groups":
        truth = Path(score.HERE).parent / "outside" / "truth.tsv"
        with truth.open(encoding="utf-8") as sheet, args.pairs.open(encoding="utf-8") as pairs:
            counts = group_counts(csv.DictReader(pairs, delimiter="\t"),
                                  csv.DictReader(sheet, delimiter="\t"), score.decode.norm)
        print("metric\tcount")
        for metric, count in counts.items():
            print(metric, count, sep="\t")
    else:
        rows = score.decode.decode_file(args.cipher, score.decode.load_truth())
        units = score.built_units(args.cipher)
        kmap = score.align.key_map(score.align.read_key(args.key), "probable")
        by_type, by_frequency = key_counts(rows, units, kmap, score.decode.norm)
        print("dimension\tband\tright\twrong\tsilent")
        for dimension, groups in (("type", by_type), ("frequency", by_frequency)):
            for band, counts in groups.items():
                print(dimension, band, counts["right"], counts["wrong"], counts["silent"], sep="\t")


if __name__ == "__main__":
    main()

"""Aggregate diagnostics for the 2911 bench. Output contains counts only."""
import argparse
from collections import Counter, defaultdict
import csv
from functools import lru_cache
from pathlib import Path
import re
import sys


def sheet_unit(unit):
    if unit in {"aa", "bb", "ss", "ff", "oo"}:
        return " ".join(unit)
    return unit


def sheet_values(truth_rows, normalize):
    values = defaultdict(set)
    for row in truth_rows:
        if row["type"] == "none":
            continue
        known = values[row["unit"]]
        known.add(normalize(row["value"]))
        for value in re.findall(r"(?:^|;\s*)([a-z]+)\s*\(", row["also_covers"] or ""):
            known.add("" if value == "null" else normalize(value))

    return values


def group_counts(pair_rows, truth_rows, normalize):
    values = sheet_values(truth_rows, normalize)
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
    sign_types = defaultdict(Counter)
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
            sign = tuple(item["names"])
            by_sign[sign][verdict] += 1
            sign_types[sign][(kind, verdict)] += 1

    by_frequency = defaultdict(Counter)
    by_type_frequency = defaultdict(Counter)
    for sign, counts in by_sign.items():
        freq = sum(counts.values())
        band = "1-4" if freq < 5 else "5-9" if freq < 10 else "10-19" if freq < 20 else "20+"
        by_frequency[band].update(counts)
        for (kind, verdict), count in sign_types[sign].items():
            by_type_frequency[f"{kind}/{band}"][verdict] += count
    return by_type, by_frequency, by_type_frequency


def seed_counts(cipher_path, plain_path, truth_rows, normalize):
    """Compare the original blind seed lists after ranking, without feeding back any values."""
    sys.path.insert(0, str(Path(__file__).resolve().parent / "variants"))
    import v3_seed

    units, plain, _, lac, _ = v3_seed.align.load_pair(cipher_path, plain_path)
    cipher = v3_seed.symbols(units)
    lacunae = [i for i, cut in enumerate(lac) if cut]

    @lru_cache(maxsize=32768)
    def positions(block):
        return [match.start() for match in re.finditer(f"(?={block})", plain)
                if not any(match.start() < p < match.start() + len(block) for p in lacunae)]

    candidates = v3_seed.seed_candidates(cipher, plain, lacunae)
    ranked = v3_seed.rank_seeds(cipher, plain, positions, candidates)
    shortlist = ranked[:32]
    _, nulls = v3_seed.near_repeats(cipher)
    extended = [v3_seed.extend(cipher, plain, positions, sig, seeds, nulls)
                for _, _, sig, seeds in shortlist]
    values = sheet_values(truth_rows, normalize)

    def agreement(signature):
        return sum(normalize(v) in values[sheet_unit(s)] for s, v in signature)

    full = {sig for sig in candidates if agreement(sig) == len(sig)}
    first = next((i for i, (_, _, sig, _) in enumerate(ranked, 1) if sig in full), 0)
    right_starts = [(len(sig), len(key), agreement(key.items()))
                    for (_, _, sig, _), (_, key, _) in zip(shortlist, extended) if sig in full]
    _, chosen, _ = max(extended, default=(0, {}, set()), key=lambda x: (x[0], len(x[1])))
    return {
        "candidate_seeds": len(candidates),
        "candidate_seeds_all_right": len(full),
        "union_of_all_right_seed_signs": len({sign for sig in full for sign, _ in sig}),
        "ranked_seeds": len(ranked),
        "ranked_seeds_all_right": sum(sig in full for _, _, sig, _ in ranked),
        "first_all_right_rank_or_zero": first,
        "shortlisted_seeds": len(shortlist),
        "shortlisted_seeds_all_right": len(right_starts),
        "shortlisted_seeds_at_most_one_wrong": sum(agreement(sig) >= len(sig) - 1
                                                   for _, _, sig, _ in shortlist),
        "max_new_signs_from_all_right_seed": max((after - before for before, after, _ in right_starts), default=0),
        "max_new_right_signs_from_all_right_seed": max((right - before for before, _, right in right_starts), default=0),
        "chosen_provisional_signs": len(chosen),
        "chosen_provisional_signs_right": agreement(chosen.items()),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("groups").add_argument("pairs", type=Path)
    key = commands.add_parser("key")
    key.add_argument("key", type=Path)
    key.add_argument("cipher", type=Path)
    seeds = commands.add_parser("seeds")
    seeds.add_argument("cipher", type=Path)
    seeds.add_argument("plain", type=Path)
    args = parser.parse_args()

    import score
    if args.command in {"groups", "seeds"}:
        truth = Path(score.HERE).parent / "outside" / "truth.tsv"
        with truth.open(encoding="utf-8") as sheet:
            truth_rows = csv.DictReader(sheet, delimiter="\t")
            if args.command == "groups":
                with args.pairs.open(encoding="utf-8") as pairs:
                    counts = group_counts(csv.DictReader(pairs, delimiter="\t"), truth_rows, score.decode.norm)
            else:
                counts = seed_counts(args.cipher, args.plain, truth_rows, score.decode.norm)
        print("metric\tcount")
        for metric, count in counts.items():
            print(metric, count, sep="\t")
    else:
        rows = score.decode.decode_file(args.cipher, score.decode.load_truth())
        units = score.built_units(args.cipher)
        kmap = score.align.key_map(score.align.read_key(args.key), "probable")
        groups = key_counts(rows, units, kmap, score.decode.norm)
        print("dimension\tband\tright\twrong\tsilent")
        for dimension, counts_by_band in zip(("type", "frequency", "type/frequency"), groups):
            for band, counts in counts_by_band.items():
                print(dimension, band, counts["right"], counts["wrong"], counts["silent"], sep="\t")


if __name__ == "__main__":
    main()

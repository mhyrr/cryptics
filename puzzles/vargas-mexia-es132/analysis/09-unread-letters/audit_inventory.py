"""Audit completed readings and reproduce agreement with the experiment 07 comparator.

Run from any directory: python3 audit_inventory.py > inventory-audit.md
The inventory describes checked-in witnesses, not a claim of exhaustive historical priority.
"""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
COMPARE = ROOT.parent / "07-after-arrest/compare_decoded.py"
PAIRS = [
    ("37", "37", "dec"), ("41", "41", "norm"), ("54", "54", "norm"),
    ("62", "62", "norm"), ("85", "85", "norm"), ("89", "89", "norm"),
    ("119", "119", "norm"), ("132", "132", "norm"), ("174", "174", "norm"),
    ("181", "181", "norm"), ("185", "185a", "norm"),
    ("185", "185b", "norm"), ("185", "185c", "norm"), ("202", "202", "dec"),
]


def compare(a, b):
    result = subprocess.run(
        [sys.executable, str(COMPARE), str(ROOT / a), str(ROOT / b)],
        check=True, text=True, capture_output=True,
    ).stdout.strip()
    match = re.fullmatch(
        r"A (\d+) chars, B (\d+) chars, matched (\d+) = (\d+)% of A, (\d+)% of B",
        result,
    )
    if not match:
        raise ValueError(result)
    return tuple(map(int, match.groups()))


def main():
    letters = {letter for letter, _, _ in PAIRS}
    readings = {p.stem.removeprefix("reading_f") for p in ROOT.glob("reading_f*.md")}
    if readings != letters:
        raise ValueError(f"Inventory/readings mismatch: {readings ^ letters}")
    print("# Experiment 09 inventory audit · 2026-10-16\n")
    print(f"{len(letters)} distinct letters; {len(letters) + 1} encipherments including f. 171, "
          f"the additional copy of f. 174; {len(PAIRS)} A/B comparisons.\n")
    print("The three sections of f. 185 are one letter. F. 213 is excluded: no accepted reading. "
          "The earlier summary's ‘fourteen letters’ is not supported by this inventory.\n")
    print("Uses `../07-after-arrest/compare_decoded.py` unchanged: retained alphabetic characters, "
          "unknowns omitted, clear text included; ordered character matches, not accuracy.\n")
    print("| Witness pair | A characters | B characters | Matched | Share of A | Share of B |")
    print("|---|---:|---:|---:|---:|---:|")
    scores = []
    for letter, part, suffix in PAIRS:
        a, b, matched, pa, pb = compare(f"f{part}_A_{suffix}.txt", f"f{part}_B_{suffix}.txt")
        scores.append((letter, pa, pb))
        print(f"| f. {part} | {a} | {b} | {matched} | {pa}% | {pb}% |")
    regular = [x for letter, a, b in scores if letter != "181" for x in (a, b)]
    all_scores = [x for _, a, b in scores for x in (a, b)]
    print(f"\nAll A/B comparisons: {min(all_scores)}–{max(all_scores)}%. "
          f"Excluding the weak f. 181 pair: {min(regular)}–{max(regular)}%.\n")
    print("Additional encipherment, not an additional letter:\n")
    for witness in "AB":
        a, b, matched, pa, pb = compare("f171_A_norm.txt", f"f174_{witness}_norm.txt")
        print(f"- f. 171 A against f. 174 {witness}: {matched}/{a} ({pa}%) of f. 171; "
              f"{matched}/{b} ({pb}%) of f. 174.")
    print("\nTwo readers per main encipherment; six readers cover the three sections of f. 185. "
          "The extra f. 171 reader is a third witness to the January letter. "
          "This audit does not repair transcriptions or establish priority.")


if __name__ == "__main__":
    main()

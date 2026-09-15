#!/usr/bin/env python3
"""Validate every catalog entry. Exit 1 and print problems if any fail."""
import sys
from catalog_lib import ENTRIES, parse, validate

def main() -> int:
    paths = sorted(ENTRIES.glob("*.md"))
    problems = [msg for p in paths for msg in validate(parse(p))]
    if problems:
        print("\n".join(problems))
        print(f"\n{len(problems)} problem(s) across {len(paths)} entries", file=sys.stderr)
        return 1
    print(f"OK: {len(paths)} entries valid")
    return 0

if __name__ == "__main__":
    sys.exit(main())

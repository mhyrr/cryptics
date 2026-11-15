#!/usr/bin/env python3
"""Check the ranking against the cases whose outcome we know.

Three checks, from TK-003 and rubric/RUBRIC.md § Calibration:

1. `attackable` ranks every solved case above every hoax or noise case.
2. Solved cases score compute >= 4 and verifiable >= 4, except the cases
   listed in EXCEPTIONS, each with the reason its lower score is right.
3. Hoax and noise cases score solvable <= 2.

`--formula v1` scores check 1 with the pre-TK-003 formula (no solvable gate)
so the before/after in rubric/CALIBRATION.md can be reproduced. Exits 1 if
any check fails.
"""
from __future__ import annotations

import argparse
import sys

from catalog_lib import load_all, Entry
from rank import WEIGHTS, composite

SOLVED = {"solved"}
HOAX = {"likely-hoax", "likely-noise"}

# The cases TK-003 named. Reported separately because the ticket's wording
# covers only these; the checks run on every solved and hoax/noise entry.
NAMED_SOLVED = {"copiale-cipher", "zodiac-z340", "trithemius-steganographia-book-iii", "poe-tyler-ciphers"}
NAMED_HOAX = {"kensington-runestone", "oera-linda-book", "le-serpent-rouge"}

# Solved cases allowed to miss check 2. Each reason is the entry's own
# argument in its "Why the scores" section. A listed case that starts
# passing, or an unlisted one that fails, fails the check.
EXCEPTIONS = {
    "trithemius-steganographia-book-iii":
        "compute 3: fell to human reading of number tables, not to search (Ernst, Reeds). "
        "Open question for Greg: the axis is defined forward-looking, and a 2026 effort "
        "would likely attack the tables statistically.",
    "berg-lyric-suite":
        "compute 2: fell to an archival find (the annotated score), after fifty years of "
        "analysis on the notes produced nothing.",
    "chaocipher":
        "compute 3: verification was mechanical, but the hypothesis space was not "
        "enumerable; the system fell when its papers were donated.",
    "silk-dress-cryptogram":
        "compute 3: a one-part code on dictionary words has no statistics to attack; "
        "it fell to a codebook search (SWEEP), not key fitting.",
    "mene-mene-tekel-upharsin":
        "compute 1, verifiable 3: four words, a philological problem settled by consensus. "
        "The bottom anchor of both axes.",
    "number-of-the-beast":
        "compute 2: the gematria space is trivially enumerable; nothing for computation "
        "to decide. Verifiable 4 passes.",
}


def v1(e: Entry, name: str) -> float:
    """The formula before TK-003: plain weighted sum, no gate."""
    return sum(w * e.score(a) for a, w in WEIGHTS[name].items())


def check_order(solved: list[Entry], hoax: list[Entry], score) -> tuple[bool, str]:
    lo = min(solved, key=lambda e: score(e, "attackable"))
    hi = max(hoax, key=lambda e: score(e, "attackable"))
    bad = [(s.slug, h.slug) for s in solved for h in hoax
           if score(s, "attackable") <= score(h, "attackable")]
    ok = not bad
    line = (f"lowest solved {lo.slug} {score(lo, 'attackable'):g}, "
            f"highest hoax/noise {hi.slug} {score(hi, 'attackable'):g}, "
            f"margin {score(lo, 'attackable') - score(hi, 'attackable'):+g}; "
            f"{len(bad)} inverted pairs")
    if bad:
        line += "\n      " + "\n      ".join(f"{s} <= {h}" for s, h in bad)
    return ok, line


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--formula", choices=["current", "v1"], default="current")
    args = ap.parse_args()
    score = composite if args.formula == "current" else v1

    entries = load_all()
    solved = [e for e in entries if e.meta.get("status") in SOLVED]
    hoax = [e for e in entries if e.meta.get("status") in HOAX]
    named_s = [e for e in solved if e.slug in NAMED_SOLVED]
    named_h = [e for e in hoax if e.slug in NAMED_HOAX]
    missing = (NAMED_SOLVED | NAMED_HOAX) - {e.slug for e in named_s + named_h}
    if missing:
        print(f"FAIL: named calibration entries missing or re-statused: {sorted(missing)}")
        return 1

    print(f"formula: {args.formula}; {len(solved)} solved, {len(hoax)} hoax/noise\n")
    results = []

    ok, line = check_order(named_s, named_h, score)
    print(f"1a {'PASS' if ok else 'FAIL'}  attackable order, ticket's named cases: {line}")
    results.append(ok)
    ok, line = check_order(solved, hoax, score)
    print(f"1b {'PASS' if ok else 'FAIL'}  attackable order, all solved vs all hoax/noise: {line}")
    results.append(ok)

    fails = {e.slug for e in solved if e.score("compute") < 4 or e.score("verifiable") < 4}
    unlisted = sorted(fails - EXCEPTIONS.keys())
    stale = sorted(EXCEPTIONS.keys() - fails)
    ok = not unlisted and not stale
    print(f"2  {'PASS' if ok else 'FAIL'}  solved compute>=4 and verifiable>=4: "
          f"{len(solved) - len(fails)}/{len(solved)} meet it; {len(fails & EXCEPTIONS.keys())} documented exceptions"
          + (f"; UNLISTED {unlisted}" if unlisted else "") + (f"; STALE {stale}" if stale else ""))
    for slug in sorted(fails & EXCEPTIONS.keys()):
        e = next(x for x in solved if x.slug == slug)
        print(f"      {slug} C{e.score('compute')} V{e.score('verifiable')}: {EXCEPTIONS[slug]}")
    results.append(ok)

    bad = [f"{e.slug} R{e.score('solvable')}" for e in hoax if e.score("solvable") > 2]
    ok = not bad
    print(f"3  {'PASS' if ok else 'FAIL'}  hoax/noise solvable<=2: "
          + ", ".join(f"{e.slug} R{e.score('solvable')}" for e in sorted(hoax, key=lambda e: e.slug))
          + (f"; FAILING {bad}" if bad else ""))
    results.append(ok)

    print("\nALL PASS" if all(results) else "\nSOME CHECKS FAIL")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())

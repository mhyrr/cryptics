#!/usr/bin/env python3
"""Experiment 18. See PROTOCOL.md. Usage: run.py [--check]"""
import collections, glob, json, pathlib, random, sys

HERE = pathlib.Path(__file__).resolve().parent
A = HERE.parent
import importlib.util
sys.path.insert(0, str(A / "14-caption-seed-test"))
_spec = importlib.util.spec_from_file_location("e14run", A / "14-caption-seed-test" / "run.py")
e14 = importlib.util.module_from_spec(_spec)      # exact, skeleton, forms, permutation_test; not modified
_spec.loader.exec_module(e14)                     # loaded by path: this file is also called run.py
from lookup import Index          # frozen lookup, not modified

SEED, DRAWS = 2026092018, 2000


def candidates(noms):
    ix = Index()
    lookups, cand = [], collections.defaultdict(set)
    for lab in noms:
        for nom in lab["nominations"][:3]:
            tier, entries = ix.find(nom["german"])
            toks = sorted({t for e in entries for t in e["hebrew_adjacent"].split()})
            lookups.append({"chapter": lab["chapter"], "number": lab["number"], "german": nom["german"], "tier": tier,
                            "entries": [[e["volume"], int(e["scan"]), e["headword_ocr"]] for e in entries],
                            "candidates_ocr": toks})
            for t in toks:
                cand[(lab["chapter"], lab["number"])] |= e14.forms(t)
    return lookups, cand


def per_square(cand, tops, rng, tier, offset=0, skip=()):
    """tops: {(chapter, number): row}. Returns observed and the within-chapter control."""
    norm = e14.skeleton if tier == "skeleton" else e14.exact
    chapters = sorted({c for c, _ in tops if c not in skip})
    def count(assign):
        return sum(norm(row) in {norm(x) for x in assign.get((c, k - offset), ())} for (c, k), row in tops.items() if c not in skip)
    obs = count(cand)
    hits = sorted(f"{c}/{k} {row}" for (c, k), row in tops.items() if c not in skip
                  and norm(row) in {norm(x) for x in cand.get((c, k - offset), ())})
    draws = []
    for _ in range(DRAWS if offset == 0 else 0):
        assign = {}
        for c in chapters:
            keys = sorted(k for k in cand if k[0] == c)
            sh = keys[:]
            rng.shuffle(sh)
            assign.update({a: cand[b] for a, b in zip(keys, sh)})
        draws.append(count(assign))
    out = {"observed": obs, "targets": sum(1 for (c, _k) in tops if c not in skip), "hits": hits}
    if draws:
        out.update({"control_mean": round(sum(draws) / DRAWS, 2), "control_max": max(draws),
                    "share_at_least_observed": sum(d >= obs for d in draws) / DRAWS})
    return out


def mathers_tops():
    tops = {}
    for s in json.load(open(A.parent / "sources" / "mathers-squares.json"))["squares"]:
        rows = s["rows"]
        c, k = (int(x) for x in s["id"].split("/"))
        if len(rows) >= 3 and all(len(r) == len(rows) for r in rows) and "." not in rows[0] and rows[0].isalpha():
            tops[(c, k)] = e14.exact(rows[0])
    return tops


def main():
    noms = json.load(open(HERE / "nominations-de.json"))["captions"]
    lookups, cand = candidates(noms)
    tops = mathers_tops()
    rng = random.Random(SEED)
    out = {"captions": len(noms), "captions_with_candidates": len([k for k, v in cand.items() if v]),
           "lookup_tiers": dict(collections.Counter(l["tier"] for l in lookups)), "gate": 100}
    out["gate_passed"] = out["captions_with_candidates"] >= 100
    for tier in ("skeleton", "exact"):
        out[f"per_square|{tier}"] = per_square(cand, tops, rng, tier)
        out[f"per_square|{tier}|without_chapter_5"] = per_square(cand, tops, rng, tier, skip=(5,))
    out["offsets|skeleton"] = {str(d): per_square(cand, tops, rng, "skeleton", offset=d)["observed"] for d in (-2, -1, 0, 1, 2)}
    bych = collections.defaultdict(set)
    for (c, _), v in cand.items():
        bych[c] |= v
    for c in range(1, 31):
        bych.setdefault(c, set())
    seed = collections.defaultdict(list)
    for (c, _), row in tops.items():
        seed[c].append(row)
    for tier in ("skeleton", "exact"):
        out[f"by_chapter|{tier}"] = e14.permutation_test(seed, bych, tier, rng)
    text = json.dumps(out, indent=1, ensure_ascii=False) + "\n"
    ltext = json.dumps(lookups, indent=1, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        assert (HERE / "results.json").read_text() == text and (HERE / "lookups.json").read_text() == ltext
        print("results reproduce")
        return
    (HERE / "results.json").write_text(text)
    (HERE / "lookups.json").write_text(ltext)
    print(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Run experiment 14. See PROTOCOL.md. Usage: run.py [--check]"""
import collections, json, pathlib, random, re, sys
from lookup import Index

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DRAWS, SEED, GATE = 2000, 2026092014, 100


def exact(s):
    s = s.upper().replace("ſ", "S").replace("J", "I").replace("V", "U").replace("W", "U")
    return "".join(c for c in s if "A" <= c <= "Z")


def skeleton(s):
    s = exact(s).replace("SCH", "S").replace("H", "")
    return re.sub(r"(.)\1+", r"\1", s)


def near(a, b):
    if len(a) < 5 or abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) <= 1
    if len(a) > len(b):
        a, b = b, a
    return any(a == b[:i] + b[i + 1:] for i in range(len(b)))


def forms(token):
    e = exact(token)
    return {e, e.replace("F", "S")} if "F" in e else {e}


def hits(rows, cands, tier):
    """Number of rows matching any candidate form under the tier."""
    if tier == "exact":
        return sum(r in cands for r in rows)
    if tier == "skeleton":
        sk = {skeleton(c) for c in cands}
        return sum(skeleton(r) in sk for r in rows)
    return sum(any(near(r, c) for c in cands) for r in rows)


def targets(squares):
    seed, inner = collections.defaultdict(list), collections.defaultdict(list)
    for sid, rows in squares:
        ch = int(sid.split("/")[0])
        n = len(rows)
        if n < 3 or any(len(r) != n for r in rows):
            continue
        if "." not in rows[0] and rows[0].isalpha():
            seed[ch].append(exact(rows[0]))
        for r in rows[1:-1]:
            if r.isalpha():
                inner[ch] += [exact(r), exact(r)[::-1]]
    return seed, inner


def permutation_test(tgt, cand, tier, rng):
    chapters = sorted(cand)
    obs = sum(hits(tgt.get(c, []), cand[c], tier) for c in chapters)
    draws = []
    for _ in range(DRAWS):
        perm = chapters[:]
        rng.shuffle(perm)
        draws.append(sum(hits(tgt.get(c, []), cand[p], tier) for c, p in zip(chapters, perm)))
    return {"observed": obs, "control_mean": round(sum(draws) / DRAWS, 2), "control_max": max(draws),
            "share_at_least_observed": sum(d >= obs for d in draws) / DRAWS,
            "targets": sum(len(tgt.get(c, [])) for c in chapters)}


def main():
    noms = json.load(open(HERE / "nominations.json"))["labels"]
    ix = Index()
    lookups, labels_with = [], 0
    cand = {False: collections.defaultdict(set), True: collections.defaultdict(set)}  # key: strict (no ocr_tolerant)
    for lab in noms:
        got = False
        for nom in lab["nominations"][:3]:
            tier, entries = ix.find(nom["german"])
            toks = sorted({t for e in entries for t in e["hebrew_adjacent"].split()})
            lookups.append({"chapter": lab["chapter"], "number": lab["number"], "german": nom["german"], "tier": tier,
                            "entries": [[e["volume"], int(e["scan"]), e["headword_ocr"]] for e in entries],
                            "candidates_ocr": toks})
            for t in toks:
                got = True
                cand[False][lab["chapter"]] |= forms(t)
                if tier != "ocr_tolerant":
                    cand[True][lab["chapter"]] |= forms(t)
        labels_with += got
    for c in range(1, 31):
        cand[False].setdefault(c, set()); cand[True].setdefault(c, set())
    mathers = [(s["id"], s["rows"]) for s in json.load(open(ROOT / "sources" / "mathers-squares.json"))["squares"]]
    dehn = [(s["id"], s["rows"]) for s in json.load(open(HERE.parent / "13-dehn-witness-test" / "dehn-readings.json"))["squares"] if s["id"]]
    out = {"labels": len(noms), "labels_with_candidates": labels_with, "gate": GATE,
           "gate_passed": labels_with >= GATE,
           "lookup_tiers": dict(collections.Counter(l["tier"] for l in lookups)), "tests": {}}
    rng = random.Random(SEED)
    for wname, sq in (("mathers", mathers), ("dehn", dehn)):
        seed, inner = targets(sq)
        for tname, tgt in (("seed", seed), ("interior", inner)):
            for strict in (False, True):
                for tier in ("exact", "skeleton", "near"):
                    k = f"{wname}|{tname}|{'no_ocr_tolerant' if strict else 'all_lookups'}|{tier}"
                    out["tests"][k] = permutation_test(tgt, cand[strict], tier, rng)
    # which seeds were hit, for image verification afterwards
    seed, _ = targets(mathers)
    out["mathers_seed_hits_skeleton"] = {str(c): sorted(r for r in seed.get(c, []) if skeleton(r) in {skeleton(x) for x in cand[False][c]}) for c in sorted(seed)}
    text = json.dumps(out, indent=1) + "\n"
    ltext = json.dumps(lookups, indent=1, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        assert (HERE / "results.json").read_text() == text and (HERE / "lookups.json").read_text() == ltext
        print("results reproduce")
        return
    (HERE / "results.json").write_text(text)
    (HERE / "lookups.json").write_text(ltext)
    print({k: out[k] for k in ("labels", "labels_with_candidates", "gate_passed", "lookup_tiers")})
    for k, v in out["tests"].items():
        print(f"{k:45} {v}")


if __name__ == "__main__":
    main()

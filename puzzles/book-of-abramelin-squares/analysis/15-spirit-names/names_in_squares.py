#!/usr/bin/env python3
"""Do the spirit names of Book II chapter 19 occur as rows of the squares?

Names: spirit-names.json (mathers and dehn lists, kept apart).
Rows: every full row of every Mathers square, and of every Dehn reading from
experiment 13. A row and its reversal are both indexed; position is recorded
(top, bottom, inner).
Tiers: exact; near (edit distance <= 1, length >= 5); stem (one string is a
prefix of the other, shorter length >= 5).
Control: each name with vowels permuted among vowel slots and consonants among
consonant slots, 200 draws, random.Random(2026092015). Normalization: upper
case, J->I, V/W->U, Y->I.
"""
import collections, json, pathlib, random

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
VOW = set("AEIOU")
DRAWS = 200


def norm(s):
    s = s.upper().replace("J", "I").replace("V", "U").replace("W", "U").replace("Y", "I")
    return "".join(c for c in s if "A" <= c <= "Z")


def near(a, b):
    if min(len(a), len(b)) < 5 or abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) <= 1
    if len(a) > len(b):
        a, b = b, a
    return any(a == b[:i] + b[i + 1:] for i in range(len(b)))


def stem(a, b):
    s, l = sorted((a, b), key=len)
    return len(s) >= 5 and l.startswith(s)


def cv_shuffle(w, rng):
    vs = [c for c in w if c in VOW]; cs = [c for c in w if c not in VOW]
    rng.shuffle(vs); rng.shuffle(cs)
    vi, ci = iter(vs), iter(cs)
    return "".join(next(vi) if c in VOW else next(ci) for c in w)


def row_index(squares):
    idx = collections.defaultdict(set)   # row text -> {(square, position)}
    for sid, rows in squares:
        n = len(rows)
        for i, r in enumerate(rows):
            if not r.isalpha() or len(r) < 4:
                continue
            pos = "top" if i == 0 else ("bottom" if i == n - 1 else "inner")
            idx[norm(r)].add((sid, pos, "forward"))
            idx[norm(r)[::-1]].add((sid, pos, "reversed"))
    return idx


def match(name, idx, by_len):
    if name in idx:
        return "exact", name
    for L in (len(name) - 1, len(name), len(name) + 1):
        for r in by_len.get(L, ()):
            if near(name, r):
                return "near", r
    for r in idx:
        if stem(name, r):
            return "stem", r
    return None, None


def main():
    lists = json.load(open(HERE / "spirit-names.json"))["lists"]
    mathers = [(s["id"], s["rows"]) for s in json.load(open(ROOT / "sources" / "mathers-squares.json"))["squares"]]
    dehn = [("D" + s["id"], s["rows"]) for s in json.load(open(HERE.parent / "13-dehn-witness-test" / "dehn-readings.json"))["squares"]]
    rng = random.Random(2026092015)
    out = {"tests": {}, "matches": []}
    for src in ("mathers", "dehn"):
        names = [norm(n) for l in lists if l["source"] == src for n in l["names"] if len(norm(n)) >= 4]
        names = list(dict.fromkeys(names))
        for wname, sq in (("mathers_squares", mathers), ("dehn_squares", dehn)):
            idx = row_index(sq)
            by_len = collections.defaultdict(list)
            for r in idx:
                by_len[len(r)].append(r)
            obs = collections.Counter(); pos = collections.Counter()
            for nm in names:
                tier, r = match(nm, idx, by_len)
                if tier:
                    obs[tier] += 1
                    for p in sorted({p for _, p, _ in idx[r]}):
                        pos[p] += 1
                    out["matches"].append({"names": src, "squares": wname, "name": nm, "tier": tier, "row": r,
                                           "where": sorted(idx[r])})
            ctrl = collections.Counter()
            for nm in names:
                for _ in range(DRAWS):
                    tier, _r = match(cv_shuffle(nm, rng), idx, by_len)
                    if tier:
                        ctrl[tier] += 1 / DRAWS
            out["tests"][f"{src}_names|{wname}"] = {"names": len(names), "observed": dict(obs),
                                                     "control_mean": {k: round(v, 2) for k, v in ctrl.items()},
                                                     "matched_row_positions": dict(pos)}
    (HERE / "names-in-squares.json").write_text(json.dumps(out, indent=1) + "\n")
    for k, v in out["tests"].items():
        print(k, v)


if __name__ == "__main__":
    main()

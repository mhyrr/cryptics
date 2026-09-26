#!/usr/bin/env python3
"""Does a square reuse its own interior letters? Every definition is in PROTOCOL.md."""
import collections, hashlib, importlib.util, json, math, pathlib, random, sys

HERE = pathlib.Path(__file__).resolve().parent
ANALYSIS = HERE.parent
ROOT = ANALYSIS.parent
_spec = importlib.util.spec_from_file_location("exp16", ANALYSIS / "16-interior-freedom" / "run.py")
exp16 = importlib.util.module_from_spec(_spec)  # load(), orbits(), base_probs(); not modified
_spec.loader.exec_module(exp16)

V = "AEIOU"
CONS = exp16.C
ALPHA = {"V": V, "C": CONS}
SEED = 20260926
NPERM = 5000
NCTRL = 200
KS = [0.25, 0.5, 1, 2, 4, 8, 16, 32, 64]
MOTIVATING = {"17/3", "16/20", "22/1", "16/19", "18/10"}
DENOMINATORS = {"W": 349, "D": 193, "R": 50}


def orbit_cells(n, i, j):
    return tuple(sorted({(i, j), (j, i), (n - 1 - i, n - 1 - j), (n - 1 - j, n - 1 - i)}))


def adjacent(a, b):
    return any(abs(p - r) + abs(q - s) == 1 for p, q in a for r, s in b)


def make_item(s):
    orbs = exp16.orbits(s)
    cells = [orbit_cells(s["n"], *o["cell"]) for o in orbs]
    pairs = [(p, q, not adjacent(cells[p], cells[q])) for p in range(len(cells)) for q in range(p + 1, len(cells))]
    return {"id": s["id"], "chapter": s["chapter"], "n": s["n"], "letters": [o["letter"] for o in orbs],
            "cls": [o["cls"] for o in orbs], "cells": cells, "pairs": pairs}


def part_a_items(drop=MOTIVATING):
    squares, _ = exp16.load()
    items = [make_item(s) for s in squares if s["id"] not in drop]
    return [it for it in items if len(it["letters"]) >= 2]


# ---------------------------------------------------------------- part A

def rep_stats(items, letters):
    rep = far = 0
    for it, ls in zip(items, letters):
        for p, q, is_far in it["pairs"]:
            if ls[p] == ls[q]:
                rep += 1
                far += is_far
    return rep, far


def shuffle_within(items, rng, key):
    pools, slots = collections.defaultdict(list), collections.defaultdict(list)
    for a, it in enumerate(items):
        for b, (l, c) in enumerate(zip(it["letters"], it["cls"])):
            g = (key(it), c)
            pools[g].append(l)
            slots[g].append((a, b))
    new = [it["letters"][:] for it in items]
    for g in sorted(pools):
        pool = pools[g]
        rng.shuffle(pool)
        for (a, b), l in zip(slots[g], pool):
            new[a][b] = l
    return new


KEYS = {"chapter": lambda it: it["chapter"], "corpus": lambda it: 0,
        "chapter_size": lambda it: (it["chapter"], it["n"])}


def part_a(items, key, nperm, seed=SEED):
    rng = random.Random(seed)
    obs = rep_stats(items, [it["letters"] for it in items])
    nulls = [rep_stats(items, shuffle_within(items, rng, KEYS[key])) for _ in range(nperm)]
    out = {"null": key, "squares": len(items), "orbits": sum(len(it["letters"]) for it in items), "nperm": nperm}
    for k, name in enumerate(("Rep", "Rep_far")):
        vals = [x[k] for x in nulls]
        out[name] = {"observed": obs[k], "null_mean": round(sum(vals) / nperm, 2),
                     "p": (1 + sum(v >= obs[k] for v in vals)) / (1 + nperm)}
    return out


# ---------------------------------------------------------------- part C

def dists_for(items, letters):
    orbs = [{"sq": it["id"], "cls": c, "letter": l} for it, ls in zip(items, letters) for l, c in zip(ls, it["cls"])]
    return exp16.base_probs(orbs)


def pick(scores, base):
    return max(scores, key=lambda x: (scores[x], base[x], -ord(x)))


def loo(items, letters):
    """Leave-one-orbit-out loss and accuracy for M0 and every K."""
    dists = dists_for(items, letters)
    loss0, right0, n = 0.0, 0, 0
    loss = {K: 0.0 for K in KS}
    right = {K: 0 for K in KS}
    for it, ls in zip(items, letters):
        d = dists[it["id"]]
        for p, (l, c) in enumerate(zip(ls, it["cls"])):
            cnt = collections.Counter(ls[q] for q in range(len(ls)) if q != p and it["cls"][q] == c)
            N = sum(cnt.values())
            base = d[c]
            n += 1
            loss0 -= math.log2(base[l])
            right0 += pick(base, base) == l
            for K in KS:
                loss[K] -= math.log2((cnt[l] + K * base[l]) / (N + K))
                right[K] += pick({x: cnt[x] + K * base[x] for x in base}, base) == l
    kbest = min(KS, key=lambda K: loss[K])
    return {"orbits": n, "K": kbest, "bits_M0": loss0 / n, "bits_K": loss[kbest] / n,
            "gain": (loss0 - loss[kbest]) / n, "acc_M0": right0 / n, "acc_K": right[kbest] / n,
            "bits_by_K": {str(K): round(loss[K] / n, 4) for K in KS}}


def part_c(items, nctrl=NCTRL, seed=SEED):
    obs = loo(items, [it["letters"] for it in items])
    rng = random.Random(seed + 7)
    ctrl = [loo(items, shuffle_within(items, rng, KEYS["chapter"]))["gain"] for _ in range(nctrl)]
    obs["control_gain_mean"] = sum(ctrl) / nctrl
    obs["control_gain_max"] = max(ctrl)
    obs["p"] = (1 + sum(g >= obs["gain"] for g in ctrl)) / (1 + nctrl)
    return obs


# ---------------------------------------------------------------- part B

def raw_mathers():
    return {s["id"]: s["rows"] for s in json.load(open(ROOT / "sources" / "mathers-squares.json"))["squares"]}


def grid_upper(rows):
    return [[c if "A" <= c <= "Z" else "." for c in r.upper()] for r in rows]


def m0_counts():
    squares, _ = exp16.load()
    cnt = {"V": collections.Counter(), "C": collections.Counter()}
    for s in squares:
        for o in exp16.orbits(s):
            cnt[o["cls"]][o["letter"]] += 1
    return {c: {l: cnt[c][l] + 0.5 for l in ALPHA[c]} for c in "VC"}


def predictions(K):
    m0 = m0_counts()
    base = {c: {l: v / sum(m0[c].values()) for l, v in m0[c].items()} for c in "VC"}
    mode = {c: pick(base[c], base[c]) for c in "VC"}
    out = []
    for sid, rows in raw_mathers().items():
        n = len(rows)
        if n < 3 or any(len(r) != n for r in rows) or not any("." in r for r in rows):
            continue
        g = grid_upper(rows)
        sq = {"id": sid, "n": n, "g": g}
        orbs = [(orbit_cells(n, *o["cell"]), o["letter"], o["cls"]) for o in exp16.orbits(sq)]
        cells = []
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                if rows[i][j] != ".":
                    continue
                own = orbit_cells(n, i, j)
                pal = {c: collections.Counter(l for cells_, l, cc in orbs if cells_ != own and cc == c) for c in "VC"}
                top = g[0][j]
                cells.append({
                    "row": i, "column": j, "orbit": [list(x) for x in own],
                    "class_mode": mode,
                    "palette": {c: pick({x: pal[c][x] + K * base[c][x] for x in base[c]}, base[c]) for c in "VC"},
                    "palette_size": {c: sum(pal[c].values()) for c in "VC"},
                    "checkerboard": None if top == "." else ("V" if (top in V) ^ (i % 2 == 1) else "C"),
                })
        if cells:
            out.append({"id": sid, "size": n, "cells": cells})
    return {"K": K, "class_mode": mode, "squares": out}


def witness_warburg(mathers):
    res = {}
    for s in json.load(open(ANALYSIS / "20-warburg-witness" / "warburg-squares.json"))["squares"]:
        rows = s.get("grid")
        sid = f'{s["chapter"]}/{s["number"]}'
        m = [r.upper() for r in mathers.get(sid, [])]
        if not rows or not m or len(m) != len(rows) or any(len(r) != len(rows) for r in m):
            continue
        n = len(m)
        both = [(i, j) for i in range(n) for j in range(n) if m[i][j].isalpha() and rows[i][j].isalpha()]
        if both and sum(m[i][j] == rows[i][j] for i, j in both) / len(both) >= 0.5:
            res[sid] = rows
    return res


def witness_dehn(mathers):
    res = {}
    for d in json.load(open(ANALYSIS / "13-dehn-witness-test" / "dehn-readings.json"))["squares"]:
        rows, sid = d["rows"], d["id"]
        n = len(rows)
        m = mathers.get(sid)
        square_like = all(len(r) == n for r in rows) and all(c.isalpha() for r in rows for c in r)
        if sid in res or not m or not square_like or len(m) != n or any(len(r) != n for r in m):
            continue
        both = [(i, j) for i in range(n) for j in range(n) if m[i][j] != "."]
        if both and sum(m[i][j] == rows[i][j] for i, j in both) / len(both) >= 0.5:
            res[sid] = rows
    return res


def witness_dresden(mathers):
    res = {}
    for x in json.load(open(ANALYSIS / "22-dresden-witness-pilot" / "posthoc-collation.json"))["grids"]:
        a, b, sid = x["reader_a"]["rows"], x["reader_b"]["rows"], x["source_id"]
        if not a or list(map(len, a)) != list(map(len, b)):
            continue
        rows = ["".join(u if u == v and u.isalpha() else "." for u, v in zip(ra, rb)) for ra, rb in zip(a, b)]
        m = [r.upper() for r in mathers.get(sid, [])]
        n = len(rows)
        if not m or len(m) != n or any(len(r) != n for r in m) or any(len(r) != n for r in rows):
            continue
        both = [(i, j) for i in range(n) for j in range(n) if m[i][j].isalpha() and rows[i][j].isalpha()]
        if both and sum(m[i][j] == rows[i][j] for i, j in both) / len(both) >= 0.5:
            res[sid] = rows
    return res


def sign_test(wins, losses):
    """One-sided exact binomial p of at least `wins` successes in wins + losses fair trials."""
    n = wins + losses
    if n == 0:
        return None
    return sum(math.comb(n, k) for k in range(wins, n + 1)) / 2 ** n


def score(preds, witness):
    cell_tally = collections.Counter()
    orbit_rows, seen = [], set()
    for sq in preds["squares"]:
        rows = witness.get(sq["id"])
        if not rows:
            continue
        for c in sq["cells"]:
            truth = rows[c["row"]][c["column"]]
            if not ("A" <= truth <= "Z"):
                continue
            cls = "V" if truth in V else "C"
            cell_tally["cells"] += 1
            cell_tally["class_mode"] += c["class_mode"][cls] == truth
            cell_tally["palette"] += c["palette"][cls] == truth
            cb = c["checkerboard"]
            if cb is not None:
                cell_tally["cb_cells"] += 1
                cell_tally["cb_class_mode"] += c["class_mode"][cb] == truth
                cell_tally["cb_palette"] += c["palette"][cb] == truth
            key = (sq["id"], tuple(map(tuple, c["orbit"])))
            if key in seen:
                continue
            seen.add(key)
            orbit_rows.append({"id": sq["id"], "row": c["row"], "column": c["column"], "truth": truth,
                               "class_mode": c["class_mode"][cls], "palette": c["palette"][cls],
                               "palette_size": c["palette_size"][cls]})
    wins = sum(o["palette"] == o["truth"] != o["class_mode"] for o in orbit_rows)
    losses = sum(o["class_mode"] == o["truth"] != o["palette"] for o in orbit_rows)
    disc = sum(o["palette"] != o["class_mode"] for o in orbit_rows)
    return {"squares": len({o["id"] for o in orbit_rows}), "cells": dict(cell_tally),
            "orbits": len(orbit_rows),
            "orbit_correct": {"class_mode": sum(o["class_mode"] == o["truth"] for o in orbit_rows),
                              "palette": sum(o["palette"] == o["truth"] for o in orbit_rows)},
            "discordant_orbits": disc, "palette_wins": wins, "palette_losses": losses,
            "sign_test_p": sign_test(wins, losses), "orbit_rows": orbit_rows}


def interior_denominator(preds, witness):
    """Interior target cells, counted as experiments 13, 20 and 22 counted them."""
    return sum(1 for sq in preds["squares"] if sq["id"] in witness for c in sq["cells"]
               if witness[sq["id"]][c["row"]][c["column"]].isalpha())


# ---------------------------------------------------------------- calibration

def planted(items, rng, share=0.3):
    pools = collections.defaultdict(list)
    for it in items:
        for l, c in zip(it["letters"], it["cls"]):
            pools[(it["chapter"], c)].append(l)
    chosen = set(rng.sample(range(len(items)), round(share * len(items))))
    out = []
    for k, it in enumerate(items):
        if k not in chosen:
            out.append(it)
            continue
        pal = {c: [rng.choice(pools[(it["chapter"], c)]) for _ in range(2)] for c in "VC" if pools[(it["chapter"], c)]}
        out.append(dict(it, letters=[rng.choice(pal[c]) for c in it["cls"]]))
    return out


def homogeneous(items, rng):
    pools = collections.defaultdict(list)
    for it in items:
        for l, c in zip(it["letters"], it["cls"]):
            pools[(it["chapter"], c)].append(l)
    return [dict(it, letters=[rng.choice(pools[(it["chapter"], c)]) for c in it["cls"]]) for it in items]


# ---------------------------------------------------------------- main

def main():
    check = "--check" in sys.argv
    res = {"protocol": "PROTOCOL.md", "seed": SEED}
    items = part_a_items()
    res["A_primary"] = part_a(items, "chapter", NPERM)
    res["A_corpus"] = part_a(items, "corpus", NPERM)
    res["A_chapter_size"] = part_a(items, "chapter_size", NPERM)
    res["S1_with_motivating"] = part_a(part_a_items(drop=set()), "chapter", NPERM)
    print("A", {k: (res["A_primary"][k]["observed"], res["A_primary"][k]["null_mean"], res["A_primary"][k]["p"]) for k in ("Rep", "Rep_far")})

    res["C"] = part_c(items)
    print("C", {k: res["C"][k] for k in ("K", "bits_M0", "bits_K", "gain", "acc_M0", "acc_K", "control_gain_mean", "p")})

    preds = predictions(res["C"]["K"])
    ptext = json.dumps(preds, indent=1) + "\n"
    ppath = HERE / "predictions.json"
    if check:
        assert ppath.read_text() == ptext, "predictions differ from checked-in file"
    else:
        ppath.write_text(ptext)
    res["predictions_sha256"] = hashlib.sha256(ptext.encode()).hexdigest()

    mathers = raw_mathers()
    witnesses = {"W": witness_warburg(mathers), "D": witness_dehn(mathers), "R": witness_dresden(mathers)}
    res["denominators"] = {w: {"expected": DENOMINATORS[w], "found": interior_denominator(preds, wit)}
                           for w, wit in witnesses.items()}
    res["denominators_ok"] = all(v["expected"] == v["found"] for v in res["denominators"].values())
    for w, wit in witnesses.items():
        res[f"B_{w}"] = score(preds, wit)
        b = res[f"B_{w}"]
        print("B", w, b["orbits"], "orbits", b["orbit_correct"], "discordant", b["discordant_orbits"],
              "wins", b["palette_wins"], "losses", b["palette_losses"], "p", b["sign_test_p"], b["cells"])

    rng = random.Random(SEED + 1)
    p1 = part_a(planted(items, rng), "chapter", 1000)
    res["P1_planted"] = {"Rep_p": p1["Rep"]["p"], "detected": p1["Rep"]["p"] < 0.01}
    p0 = []
    for rep in range(20):
        t = part_a(homogeneous(items, random.Random(SEED + 100 + rep)), "chapter", 1000, seed=SEED + 200 + rep)
        p0.append(t["Rep"]["p"])
    res["P0_homogeneous"] = {"Rep_p": p0, "below_0.01": sum(p < 0.01 for p in p0), "below_0.05": sum(p < 0.05 for p in p0)}
    res["calibration_ok"] = res["P1_planted"]["detected"] and res["P0_homogeneous"]["below_0.05"] <= 3

    pa = res["A_primary"]["Rep"]["p"]
    bw = res["B_W"]
    if not res["calibration_ok"]:
        verdict = "withheld: calibration failed"
    elif pa >= 0.05:
        verdict = "weakened"
    elif not res["denominators_ok"]:
        verdict = "open: witness extraction does not reproduce earlier denominators"
    elif bw["discordant_orbits"] < 10:
        verdict = "open: witness half underpowered"
    elif pa < 0.01 and bw["sign_test_p"] is not None and bw["sign_test_p"] < 0.05:
        verdict = "supported"
    else:
        verdict = "open"
    res["verdict"] = verdict

    text = json.dumps(res, indent=1) + "\n"
    rpath = HERE / "results.json"
    if check:
        assert rpath.read_text() == text, "results differ from checked-in file"
        print("results reproduce")
        return
    rpath.write_text(text)
    print("verdict", verdict, "calibration_ok", res["calibration_ok"], "denominators", res["denominators"])


if __name__ == "__main__":
    main()

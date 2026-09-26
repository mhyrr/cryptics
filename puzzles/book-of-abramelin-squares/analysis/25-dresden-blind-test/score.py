#!/usr/bin/env python3
"""Score the frozen predictions against the Dresden consensus. Every rule is in PROTOCOL.md.

python3 score.py            write consensus.json and results.json
python3 score.py --check    verify both reproduce
"""
import collections, hashlib, importlib.util, json, math, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ANALYSIS = HERE.parent
DIVE = ANALYSIS.parent
V = set("AEIOU")
SEED = 20260926
NBOOT = 2000
NPERM = 5000
LETTER_MODELS = ["letter_filler", "letter_chapter", "letter_global", "palette_cb"]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check_freeze():
    frozen = json.load(open(HERE / "freeze.json"))
    for key, rel in frozen["paths"].items():
        if key == "protocol":
            continue
        assert sha(DIVE / rel) == frozen[key], f"{key} changed after the freeze"


# ---------------------------------------------------------------- consensus

def consensus_grid(a_rows, b_rows, normalize=False):
    """Agreed letters, '?' elsewhere; None when the row-length vectors differ."""
    if not a_rows or not b_rows or list(map(len, a_rows)) != list(map(len, b_rows)):
        return None
    f = (lambda c: "I" if c == "J" else c) if normalize else (lambda c: c)
    return ["".join(f(x) if f(x) == f(y) and "A" <= x <= "Z" else "?" for x, y in zip(ra, rb))
            for ra, rb in zip(a_rows, b_rows)]


def reader_stats(a_rows, b_rows):
    s = collections.Counter()
    if not a_rows or not b_rows or list(map(len, a_rows)) != list(map(len, b_rows)):
        s["shape_differs"] += 1
        return s
    s["same_shape"] += 1
    for ra, rb in zip(a_rows, b_rows):
        for x, y in zip(ra, rb):
            if "?" in (x, y):
                s["unknown"] += 1
            elif x == y:
                s["agreed_letter" if x != "." else "agreed_blank"] += 1
            else:
                s["conflict"] += 1
    return s


def load_readings():
    out = {}
    for reader in "AB":
        items = {}
        for f in sorted((HERE / "readings" / reader).glob("R*.json")):
            for it in json.load(open(f))["items"]:
                items[it["locator_id"]] = [r.upper() for r in it.get("rows") or []]
        out[reader] = items
    return out


def square(rows):
    n = len(rows) if rows else 0
    return rows if n >= 4 and all(len(r) == n for r in rows) else None


# ---------------------------------------------------------------- joins

def gate(m, rows):
    """Experiment 20's frozen gate: same n, agreement at least half on cells lettered in both."""
    n = len(rows)
    if not m or len(m) != n or any(len(r) != n for r in m):
        return False
    both = [(i, j) for i in range(n) for j in range(n) if m[i][j].isalpha() and rows[i][j].isalpha()]
    return bool(both) and sum(m[i][j] == rows[i][j] for i, j in both) / len(both) >= 0.5


def primary_join(grids, mathers_upper):
    joined = {}
    for g in grids:
        sid = f"{g['chapter']}/{g['item']}"
        if g["chapter"] is None or g["item"] is None or sid in joined:
            continue
        if gate(mathers_upper.get(sid), g["rows"]):
            joined[sid] = g
    return joined


def secondary_join(grids, mathers_raw, mathers_upper, exp13score):
    readings = [{"id": f"{g['chapter']}/{g['item']}", "rows": [r.replace("?", ".") for r in g["rows"]],
                 "raw": "", "id_basis": "Dresden locator", "_g": g}
                for g in grids if g["chapter"] is not None and g["item"] is not None]
    moved = exp13score.realign(readings, mathers_raw)
    joined = {}
    for d in moved:
        sid, g = d["id"], d["_g"]
        if sid not in joined and gate(mathers_upper.get(sid), g["rows"]):
            joined[sid] = g
    return joined


# ---------------------------------------------------------------- scoring

def outcome(guess, truth):
    return "abstain" if guess is None else ("correct" if guess == truth else "wrong")


def cell_outcomes(joined, p13, p20, p24):
    rows_out = []
    for sid, g in sorted(joined.items()):
        if sid not in p13:
            continue
        rows = g["rows"]
        pal = p24.get(sid, {})
        for c in p13[sid]["cells"]:
            i, j = c["row"], c["column"]
            truth = rows[i][j]
            if not ("A" <= truth <= "Z"):
                continue
            cb = c["class_checkerboard"]
            tcls = "V" if truth in V else "C"
            p = pal.get((i, j))
            rows_out.append({
                "id": sid, "locator_id": g["locator_id"], "row": i, "column": j, "truth": truth,
                "zone": "interior" if c["interior"] else "border",
                "sym_TA": outcome(c["sym_TA"], truth),
                "class_checkerboard": "abstain" if cb is None else ("correct" if (truth in V) == (cb == "V") else "wrong"),
                "letter_filler": outcome(c["letter_filler"], truth),
                "letter_global": outcome(c["letter_global"], truth),
                "letter_chapter": outcome(p20.get(sid, {}).get((i, j)), truth),
                "palette_cb": outcome(p["palette"][cb] if p and cb else None, truth),
                "palette_true_class": outcome(p["palette"][tcls] if p else None, truth),
                "class_mode_true_class": outcome(p["class_mode"][tcls] if p else None, truth),
            })
    return rows_out


def acc(cells, model, zone):
    c = collections.Counter(x[model] for x in cells if x["zone"] == zone)
    d = c["correct"] + c["wrong"]
    return {"correct": c["correct"], "wrong": c["wrong"], "abstain": c["abstain"],
            "accuracy": c["correct"] / d if d else None}


def measures(cells):
    m = {"M1_sym_border": acc(cells, "sym_TA", "border"),
         "M2_class_interior": acc(cells, "class_checkerboard", "interior")}
    for mdl in LETTER_MODELS + ["palette_true_class", "class_mode_true_class"]:
        m[f"M3_{mdl}"] = acc(cells, mdl, "interior")
    m["targets"] = {"interior": sum(x["zone"] == "interior" for x in cells),
                    "border": sum(x["zone"] == "border" for x in cells),
                    "squares": len({x["id"] for x in cells})}
    return m


def bootstrap(cells, rng, nboot=NBOOT):
    by_sq = collections.defaultdict(list)
    for x in cells:
        by_sq[x["id"]].append(x)
    ids = sorted(by_sq)
    keys = ["M1_sym_border", "M2_class_interior"] + [f"M3_{m}" for m in LETTER_MODELS]
    draws = {k: [] for k in keys}
    for _ in range(nboot):
        sample = [x for sid in (rng.choice(ids) for _ in ids) for x in by_sq[sid]]
        m = measures(sample)
        for k in keys:
            if m[k]["accuracy"] is not None:
                draws[k].append(m[k]["accuracy"])
    out = {}
    for k, v in draws.items():
        v.sort()
        out[k] = [v[int(0.025 * len(v))], v[int(0.975 * len(v)) - 1]] if v else None
    return out


def decide(m):
    t = m["targets"]
    if t["interior"] < 50 or t["border"] < 30:
        return "too few targets"
    m1, m2 = m["M1_sym_border"]["accuracy"], m["M2_class_interior"]["accuracy"]
    letters = [m[f"M3_{x}"]["accuracy"] for x in LETTER_MODELS if m[f"M3_{x}"]["accuracy"] is not None]
    flags = []
    if m1 is not None and m1 < 0.70:
        flags.append("frame fails")
    if m2 is not None and m2 < 0.60:
        flags.append("class fails")
    if letters and max(letters) >= 0.50:
        flags.append("generator signal")
    if flags:
        return "; ".join(flags)
    if m1 is not None and m1 >= 0.80 and m2 is not None and m2 >= 0.70 and letters and max(letters) < 0.40:
        return "recipe holds"
    return "undecided"


def orbit_counts(cells, n_by_id):
    """Interior target orbits all of whose target cells a model gets right."""
    groups = collections.defaultdict(list)
    for x in cells:
        if x["zone"] != "interior":
            continue
        n, i, j = n_by_id[x["id"]], x["row"], x["column"]
        orb = tuple(sorted({(i, j), (j, i), (n - 1 - i, n - 1 - j), (n - 1 - j, n - 1 - i)}))
        groups[(x["id"], orb)].append(x)
    out = {"orbits": len(groups)}
    for mdl in ["class_checkerboard"] + LETTER_MODELS:
        out[mdl] = sum(all(x[mdl] == "correct" for x in g) for g in groups.values())
    return out


def alternates(top):
    if not top or any(not c.isalpha() for c in top):
        return None
    return all((a in V) != (b in V) for a, b in zip(top, top[1:]))


def s1_alternation(cells, mathers_upper, rng):
    per = collections.defaultdict(lambda: [0, 0])
    for x in cells:
        if x["zone"] == "interior" and x["class_checkerboard"] != "abstain":
            per[x["id"]][0] += x["class_checkerboard"] == "correct"
            per[x["id"]][1] += 1
    ids = [sid for sid in sorted(per) if alternates(mathers_upper[sid][0]) is not None]
    lab = [alternates(mathers_upper[sid][0]) for sid in ids]

    def diff(labels):
        a = [per[s] for s, l in zip(ids, labels) if l]
        b = [per[s] for s, l in zip(ids, labels) if not l]
        if not a or not b:
            return None
        return sum(x[0] for x in a) / sum(x[1] for x in a) - sum(x[0] for x in b) / sum(x[1] for x in b)

    obs = diff(lab)
    if obs is None:
        return {"squares": len(ids), "alternating": sum(lab), "difference": None, "p_one_sided": None}
    hits = 0
    for _ in range(NPERM):
        l = lab[:]
        rng.shuffle(l)
        d = diff(l)
        hits += d is not None and d >= obs
    alt = [per[s] for s, l in zip(ids, lab) if l]
    non = [per[s] for s, l in zip(ids, lab) if not l]
    return {"squares": len(ids), "alternating": sum(lab),
            "class_alternating": f"{sum(x[0] for x in alt)}/{sum(x[1] for x in alt)}",
            "class_other": f"{sum(x[0] for x in non)}/{sum(x[1] for x in non)}",
            "difference": obs, "p_one_sided": (1 + hits) / (1 + NPERM)}


def s3_transmission(joined, mathers_upper, rng):
    flagsets, zones = [], collections.defaultdict(lambda: [0, 0])
    for sid, g in sorted(joined.items()):
        m, rows, n = mathers_upper[sid], g["rows"], len(g["rows"])
        cells = []
        for i in range(n):
            for j in range(n):
                if m[i][j].isalpha() and "A" <= rows[i][j] <= "Z":
                    zone = "top" if i == 0 else ("border" if i == n - 1 or j in (0, n - 1) else "interior")
                    d = m[i][j] != rows[i][j]
                    zones[zone][0] += d
                    zones[zone][1] += 1
                    cells.append((zone, d))
        flagsets.append(cells)
    obs = sum(d for cells in flagsets for z, d in cells if z == "interior")
    null = []
    for _ in range(NPERM):
        k = 0
        for cells in flagsets:
            fl = [d for _, d in cells]
            rng.shuffle(fl)
            k += sum(d for (z, _), d in zip(cells, fl) if z == "interior")
        null.append(k)
    return {"disagreement": {z: f"{a}/{b}" for z, (a, b) in zones.items()},
            "interior_observed": obs, "interior_null_mean": round(sum(null) / NPERM, 2),
            "p_one_sided": (1 + sum(x >= obs for x in null)) / (1 + NPERM)}


def score_join(joined, p13, p20, p24, n_by_id, rng):
    cells = cell_outcomes(joined, p13, p20, p24)
    m = measures(cells)
    return cells, {"joined_grids": len(joined), "joined_with_targets": m["targets"]["squares"],
                   "measures": m, "intervals_95": bootstrap(cells, rng),
                   "orbit_counts": orbit_counts(cells, n_by_id), "verdict": decide(m)}


def main():
    check_freeze()
    exp13score = load_module("exp13score", ANALYSIS / "13-dehn-witness-test" / "score.py")
    exp24 = load_module("exp24run", ANALYSIS / "24-square-palette" / "run.py")
    inv = json.load(open(HERE / "inventory.json"))
    readings = load_readings()
    mathers_raw = {s["id"]: s["rows"] for s in json.load(open(DIVE / "sources" / "mathers-squares.json"))["squares"]}
    mathers_upper = {k: [r.upper() for r in v] for k, v in mathers_raw.items()}
    p13 = {s["id"]: s for s in json.load(open(ANALYSIS / "13-dehn-witness-test" / "predictions.json"))["squares"]}
    p20 = {s["id"]: {(c["row"], c["column"]): c["letter_chapter"] for c in s["cells"]}
           for s in json.load(open(ANALYSIS / "20-warburg-witness" / "predictions.json"))["squares"]}
    preds24 = json.load(open(ANALYSIS / "24-square-palette" / "predictions.json"))
    p24 = {s["id"]: {(c["row"], c["column"]): c for c in s["cells"]} for s in preds24["squares"]}

    grids, grids_norm, stats, missing = [], [], collections.Counter(), []
    for g in inv["grids"]:
        a, b = readings["A"].get(g["locator_id"]), readings["B"].get(g["locator_id"])
        if a is None or b is None:
            missing.append(g["locator_id"])
            continue
        stats.update(reader_stats(a, b))
        base = {"locator_id": g["locator_id"], "chapter": g.get("chapter"), "item": g.get("item"),
                "physical_page": g["physical_page"]}
        for target, norm in ((grids, False), (grids_norm, True)):
            rows = square(consensus_grid(a, b, normalize=norm))
            if rows:
                target.append(dict(base, rows=rows))
    consensus = {"grids": grids, "reader_agreement": dict(stats), "missing_readings": missing}

    res = {"protocol": "PROTOCOL.md", "inventory_grids": len(inv["grids"]), "square_consensus_grids": len(grids),
           "S5_reader_agreement": dict(stats), "missing_readings": missing}
    rng = random.Random(SEED)
    n_by_id = {k: len(v) for k, v in mathers_raw.items()}
    primary = primary_join(grids, mathers_upper)
    cells, res["primary"] = score_join(primary, p13, p20, p24, n_by_id, rng)
    res["verdict"] = res["primary"]["verdict"]
    res["S1_seed_alternation"] = s1_alternation(cells, mathers_upper, rng)
    witness = {sid: [r.replace("?", ".") for r in g["rows"]] for sid, g in primary.items()}
    s2 = exp24.score(preds24, witness)
    res["S2_palette_vs_class_mode"] = {k: v for k, v in s2.items() if k != "orbit_rows"}
    res["S3_transmission"] = s3_transmission(primary, mathers_upper, rng)
    secondary = secondary_join(grids, mathers_raw, mathers_upper, exp13score)
    _, res["S4_secondary_join"] = score_join(secondary, p13, p20, p24, n_by_id, rng)
    _, res["S6_j_to_i"] = score_join(primary_join(grids_norm, mathers_upper), p13, p20, p24, n_by_id, rng)
    res["unjoined"] = [{"locator_id": g["locator_id"], "source_id": f"{g['chapter']}/{g['item']}"}
                       for g in grids if f"{g['chapter']}/{g['item']}" not in primary]

    ctext = json.dumps(consensus, indent=1) + "\n"
    ptext = json.dumps({"cells": cells}, indent=1) + "\n"
    rtext = json.dumps(res, indent=1) + "\n"
    if "--check" in sys.argv:
        assert (HERE / "consensus.json").read_text() == ctext, "consensus differs"
        assert (HERE / "cells.json").read_text() == ptext, "cells differ"
        assert (HERE / "results.json").read_text() == rtext, "results differ"
        print("consensus, cells and results reproduce")
        return
    (HERE / "consensus.json").write_text(ctext)
    (HERE / "cells.json").write_text(ptext)
    (HERE / "results.json").write_text(rtext)
    m = res["primary"]["measures"]
    print("grids", len(inv["grids"]), "square consensus", len(grids), "primary joins", len(primary),
          "targets", m["targets"])
    for k in ["M1_sym_border", "M2_class_interior"] + [f"M3_{x}" for x in LETTER_MODELS]:
        print(f"{k:28}", m[k], res["primary"]["intervals_95"].get(k))
    print("verdict", res["verdict"])


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Score the Warburg readings. Every rule is in PROTOCOL.md. Run once."""
import collections, hashlib, json, pathlib, random, sys

HERE = pathlib.Path(__file__).resolve().parent
A = HERE.parent
import importlib.util


def load(name, path):
    """Load a sibling experiment's script by path; several are called run.py or score.py."""
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


r12 = load("e12rows", A / "12-dictionary-index" / "rows_in_dictionary.py")
e13 = load("e13score", A / "13-dehn-witness-test" / "score.py")
e18 = load("e18run", A / "18-german-captions" / "run.py")
e14 = e18.e14
READ = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE     # a second directory is for dry runs on synthetic readings

V = set("AEIOU")
SEED = 20260920


def load_reader(name):
    out = {}
    for it in json.load(open(READ / name))["items"]:
        rows = ["".join(c if ("A" <= c <= "Z" or c in ".?") else "" for c in r.upper().replace(" ", "")) for r in it["rows"]]
        out[(it["chapter"], it["number"])] = [r for r in rows if r]
    return out


def to_square(rows):
    """Return (grid or None, status)."""
    if not rows:
        return None, "empty"
    n = len(rows[0])
    if n < 3 or len(rows) > n or any(len(r) != n for r in rows):
        return None, "ragged"
    return rows + ["." * n] * (n - len(rows)), "ok"


def merge(a, b):
    """Cells both readers agree on; anything else becomes '?'."""
    items, stats = {}, collections.Counter()
    for key in sorted(set(a) | set(b)):
        ra, rb = a.get(key, []), b.get(key, [])
        ga, sa = to_square(ra)
        gb, sb = to_square(rb)
        top = None
        if ra and rb and ra[0] == rb[0] and "?" not in ra[0] and "." not in ra[0]:
            top = ra[0]
        if ga is None or gb is None or len(ga) != len(gb):
            stats["items_unscored_shape"] += 1
            items[key] = {"grid": None, "top": top}
            continue
        n = len(ga)
        g = []
        for i in range(n):
            row = ""
            for j in range(n):
                x, y = ga[i][j], gb[i][j]
                lettered = x.isalpha() or y.isalpha()
                zone = "top" if i == 0 else ("border" if i == n - 1 or j in (0, n - 1) else "interior")
                if lettered:
                    stats[f"lettered_{zone}"] += 1
                    stats[f"agreed_{zone}"] += x == y and x.isalpha()
                row += x if x == y and (x.isalpha() or x == ".") else "?"
            g.append(row)
        stats["items_scored_shape"] += 1
        items[key] = {"grid": g, "top": top}
    return items, stats


def main():
    assert hashlib.sha256((HERE / "predictions.json").read_bytes()).hexdigest() == json.load(open(HERE / "freeze.json"))["predictions_sha256"]
    rng = random.Random(SEED)
    items, stats = merge(load_reader("readings-A.json"), load_reader("readings-B.json"))
    lettered = sum(v for k, v in stats.items() if k.startswith("lettered_"))
    agreed = sum(v for k, v in stats.items() if k.startswith("agreed_"))
    out = {"reader_agreement": dict(stats), "agreed_share": round(agreed / lettered, 3) if lettered else None}
    out["readable"] = bool(lettered) and agreed / lettered >= 0.5

    mathers = {s["id"]: [r.upper() for r in s["rows"]] for s in json.load(open(A.parent / "sources" / "mathers-squares.json"))["squares"]}
    p13 = {s["id"]: s for s in json.load(open(A / "13-dehn-witness-test" / "predictions.json"))["squares"]}
    p20 = {s["id"]: {(c["row"], c["column"]): c["letter_chapter"] for c in s["cells"]} for s in json.load(open(HERE / "predictions.json"))["squares"]}
    wb = [{"id": f"{c}/{k}", "rows": v["grid"], "raw": "", "id_basis": "print numbering"} for (c, k), v in items.items() if v["grid"]]

    def pairs(readings):
        res = []
        for d in readings:
            m, rows = mathers.get(d["id"]), d["rows"]
            if not m or len(m) != len(rows) or any(len(r) != len(rows) for r in m):
                continue
            both = [(i, j) for i in range(len(m)) for j in range(len(m)) if m[i][j].isalpha() and rows[i][j].isalpha()]
            same = sum(m[i][j] == rows[i][j] for i, j in both)
            if both and same / len(both) >= 0.5:
                res.append((d["id"], m, rows, both))
        return res

    def realign_safe(readings):
        masked = [dict(d, rows=[r.replace("?", ".") for r in d["rows"]]) for d in readings]
        # experiment 13's realign compares letters on cells visible in Mathers; blank Warburg cells then count as
        # disagreements, which only makes the gate stricter.
        moved = e13.realign(masked, {k: v for k, v in mathers.items()})
        return [dict(o, id=m["id"]) for o, m in zip(readings, moved)]

    for tag, readings in (("frozen_alignment", wb), ("post_hoc_realignment", realign_safe(wb))):
        pr = pairs(readings)
        tally = collections.defaultdict(collections.Counter)
        zones = collections.defaultdict(lambda: [0, 0])
        flagsets = []
        for sid, m, rows, both in pr:
            n = len(m)
            cells = []
            for i, j in both:
                zone = "top" if i == 0 else ("border" if i == n - 1 or j in (0, n - 1) else "interior")
                diff = m[i][j] != rows[i][j]
                zones[zone][0] += diff
                zones[zone][1] += 1
                cells.append((zone, diff))
            flagsets.append(cells)
            if sid not in p13:
                continue
            for c in p13[sid]["cells"]:
                truth = rows[c["row"]][c["column"]]
                if not truth.isalpha():
                    continue
                zone = "interior" if c["interior"] else "border"
                guesses = {"sym_TA": c["sym_TA"], "letter_class_mode": c["letter_filler"], "letter_most_common": c["letter_global"],
                           "letter_chapter": p20[sid].get((c["row"], c["column"]))}
                for mdl, g in guesses.items():
                    tally[(mdl, zone)]["abstain" if g is None else ("correct" if g == truth else "wrong")] += 1
                cls = c["class_checkerboard"]
                tally[("class_checkerboard", zone)]["abstain" if cls is None else ("correct" if (truth in V) == (cls == "V") else "wrong")] += 1
        obs = sum(f for cells in flagsets for z, f in cells if z == "interior")
        null = []
        for _ in range(5000):
            k = 0
            for cells in flagsets:
                fl = [f for _, f in cells]
                rng.shuffle(fl)
                k += sum(f for (z, _), f in zip(cells, fl) if z == "interior")
            null.append(k)
        out[tag] = {"pairs": len(pr),
                    "blind_cells": {f"{a}|{b}": dict(c) for (a, b), c in sorted(tally.items())},
                    "mathers_vs_warburg": {z: f"{a}/{b}" for z, (a, b) in zones.items()},
                    "interior_excess": {"observed": obs, "control_mean": round(sum(null) / 5000, 2),
                                        "p": round((1 + sum(x >= obs for x in null)) / 5001, 4)}}

    # end state rule
    t = out["frozen_alignment"]["blind_cells"]
    def acc(k):
        c = t.get(k, {})
        d = c.get("correct", 0) + c.get("wrong", 0)
        return (c.get("correct", 0) / d if d else None), d
    best = max((acc(f"{m}|interior")[0] or 0) for m in ("letter_class_mode", "letter_chapter", "letter_most_common"))
    cls_acc, n_int = acc("class_checkerboard|interior")
    if not out["readable"]:
        verdict = "witness unreadable at this resolution"
    elif n_int < 50:
        verdict = "too few blind interior cells; experiment 16 stands alone"
    elif best >= 0.50:
        verdict = "A"
    elif best < 0.40 and cls_acc >= 0.70:
        verdict = "B confirmed"
    else:
        verdict = "undecided"
    out["end_state"] = {"blind_interior_cells": n_int, "best_letter_accuracy": round(best, 3),
                        "class_accuracy": None if cls_acc is None else round(cls_acc, 3), "verdict": verdict}

    # seeds
    vocab = r12.load_vocab()
    idx = r12.near_index(vocab)
    tops = {k: r12.norm(v["top"]) for k, v in items.items() if v["top"] and len(v["top"]) >= 4}
    ex = sum(w in vocab for w in tops.values())
    nr = sum(r12.is_near(w, vocab, idx) for w in tops.values())
    ce = cn = 0
    for w in tops.values():
        for _ in range(200):
            x = r12.cv_shuffle(w, rng)
            ce += x in vocab
            cn += r12.is_near(x, vocab, idx)
    msame = [(k, w) for k, w in tops.items() if f"{k[0]}/{k[1]}" in mathers]
    out["seeds"] = {"warburg_top_rows": len(tops), "exact": ex, "exact_control": round(ce / 200, 2), "near": nr, "near_control": round(cn / 200, 2),
                    "exact_hits": sorted(f"{k[0]}/{k[1]} {w}" for k, w in tops.items() if w in vocab),
                    "same_number_mathers_top_row_identical": sum(r12.norm(mathers[f"{k[0]}/{k[1]}"][0]) == w for k, w in msame),
                    "same_number_pairs": len(msame)}

    # captions per square, on the print's own numbering
    noms = json.load(open(A / "18-german-captions" / "nominations-de.json"))["captions"]
    _, cand = e18.candidates(noms)
    wt = {k: e14.exact(w) for k, w in tops.items()}
    out["caption_to_seed"] = {"per_square|skeleton": e18.per_square(cand, wt, rng, "skeleton"),
                              "per_square|skeleton|without_chapter_5": e18.per_square(cand, wt, rng, "skeleton", skip=(5,)),
                              "per_square|exact": e18.per_square(cand, wt, rng, "exact"),
                              "offsets|skeleton": {str(d): e18.per_square(cand, wt, rng, "skeleton", offset=d)["observed"] for d in (-2, -1, 0, 1, 2)}}

    # three witnesses, descriptive
    dehn = json.load(open(A / "13-dehn-witness-test" / "dehn-readings.json"))["squares"]
    side = collections.Counter()
    wgrid = {f"{c}/{k}": v["grid"] for (c, k), v in items.items() if v["grid"]}
    for d in dehn:
        m, w, rows = mathers.get(d["id"]), wgrid.get(d["id"]), d["rows"]
        if not m or not w or not (len(m) == len(w) == len(rows)) or any(len(r) != len(m) for r in list(m) + list(rows)):
            continue
        for i in range(len(m)):
            for j in range(len(m)):
                a, b, c = m[i][j], rows[i][j].upper(), w[i][j]
                if a.isalpha() and b.isalpha() and c.isalpha() and a != b:
                    side["with_mathers" if c == a else "with_dehn" if c == b else "neither"] += 1
    out["where_mathers_and_dehn_differ_warburg_sides"] = dict(side)
    (READ / "results.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    (READ / "warburg-squares.json").write_text(json.dumps(
        {"source": "https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf", "tier": "PRIMARY, read by two Opus subagents from 100 ppi page images; '?' marks a cell the readers did not agree on",
         "squares": [{"chapter": c, "number": k, "top_row_agreed": v["top"], "grid": v["grid"]} for (c, k), v in sorted(items.items())]},
        indent=1) + "\n")
    print(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()

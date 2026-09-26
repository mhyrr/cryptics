#!/usr/bin/env python3
"""Are there construction types? Every definition is in PROTOCOL.md."""
import collections, importlib.util, json, math, pathlib, random, statistics, sys

HERE = pathlib.Path(__file__).resolve().parent
ANALYSIS = HERE.parent
_spec = importlib.util.spec_from_file_location("exp16", ANALYSIS / "16-interior-freedom" / "run.py")
exp16 = importlib.util.module_from_spec(_spec)  # load(), orbits(); not modified
_spec.loader.exec_module(exp16)

V = "AEIOU"
SEED = 20260926
NPERM = 5000
MIN_REFS = 5
MOTIVATING_SEEDS = {"APPARET", "ETHANIM"}
MOTIVATING_IDS = {"4/2", "4/3"}


def to_grid(rows):
    return [[c if "A" <= c <= "Z" else "." for c in r.upper()] for r in rows]


def square_shaped(rows):
    return rows and len(rows) >= 4 and all(len(r) == len(rows) for r in rows)


def load_mathers():
    squares, _ = exp16.load()
    return [{"id": s["id"], "n": s["n"], "g": s["g"]} for s in squares]


def load_warburg():
    out, seen = [], set()
    for s in json.load(open(ANALYSIS / "20-warburg-witness" / "warburg-squares.json"))["squares"]:
        rows = s.get("grid")
        if not square_shaped(rows):
            continue
        g = to_grid(rows)
        key = tuple("".join(r) for r in g)
        if key not in seen:
            seen.add(key)
            out.append({"id": f'{s["chapter"]}/{s["number"]}', "n": len(g), "g": g})
    return out


def load_dehn():
    out, seen, ids = [], set(), set()
    for s in json.load(open(ANALYSIS / "13-dehn-witness-test" / "dehn-readings.json"))["squares"]:
        rows = s["rows"]
        if s["id"] in ids or not square_shaped(rows):
            continue
        g = to_grid(rows)
        key = tuple("".join(r) for r in g)
        if key not in seen:
            seen.add(key)
            ids.add(s["id"])
            out.append({"id": s["id"], "n": len(g), "g": g})
    return out


def load_dresden():
    out = []
    for x in json.load(open(ANALYSIS / "22-dresden-witness-pilot" / "posthoc-collation.json"))["grids"]:
        a, b = x["reader_a"]["rows"], x["reader_b"]["rows"]
        if a == b and square_shaped(a):
            out.append({"id": x["source_id"], "n": len(a), "g": to_grid(a)})
    return out


def checkerboard_class(g, cell):
    i, j = cell
    return "V" if (g[0][j] in V) ^ (i % 2 == 1) else "C"


def prepare(corpus, drop_motivating=True):
    """Eligible squares: complete top row, at least two visible interior orbits."""
    items = []
    for s in corpus:
        seed = "".join(s["g"][0])
        if "." in seed:
            continue
        if drop_motivating and (seed in MOTIVATING_SEEDS or s["id"] in MOTIVATING_IDS):
            continue
        orbs = exp16.orbits(s)
        if len(orbs) < 2:
            continue
        items.append({
            "id": s["id"], "n": s["n"], "seed": seed,
            "letters": [o["letter"] for o in orbs],
            "cls": [o["cls"] for o in orbs],
            "conform": [checkerboard_class(s["g"], o["cell"]) == o["cls"] for o in orbs],
            "interior": ["".join(r[1:-1]) for r in s["g"][1:-1]],
        })
    return items


def closure(letters, seed):
    st = set(seed)
    return sum(l in st for l in letters)


def attach_moments(items, stratify=False, letters_key="letters"):
    """Set E, sd and z on each item; return (usable items, excluded list)."""
    by_n = collections.defaultdict(list)
    for it in items:
        by_n[it["n"]].append(it)
    usable, excluded = [], []
    for it in items:
        refs = sorted({o["seed"] for o in by_n[it["n"]] if o is not it and o["seed"] != it["seed"]})
        if stratify:
            same = [r for r in refs if len(set(r)) == len(set(it["seed"]))]
            if len(same) >= MIN_REFS:
                refs = same
        letters = it[letters_key]
        if len(refs) < MIN_REFS or not letters:
            excluded.append({"id": it["id"], "reason": "fewer than 5 references or no letters"})
            continue
        ks = [closure(letters, r) for r in refs]
        var = statistics.pvariance(ks)
        if var == 0:
            excluded.append({"id": it["id"], "reason": "zero reference variance"})
            continue
        u = dict(it, letters=letters, E=statistics.fmean(ks), sd=math.sqrt(var), refs=len(refs))
        u["k"] = closure(letters, it["seed"])
        u["z"] = (u["k"] - u["E"]) / u["sd"]
        usable.append(u)
    return usable, excluded


def corpus_stats(zs):
    return {"D": sum(z * z for z in zs), "U": sum(z >= 2 for z in zs),
            "L": sum(z <= -2 for z in zs), "S": sum(zs)}


def null_stats(items, rng):
    by_n = collections.defaultdict(list)
    for k, it in enumerate(items):
        by_n[it["n"]].append(k)
    zs = [0.0] * len(items)
    for idx in by_n.values():
        seeds = [items[k]["seed"] for k in idx]
        rng.shuffle(seeds)
        for k, sd in zip(idx, seeds):
            it = items[k]
            zs[k] = (closure(it["letters"], sd) - it["E"]) / it["sd"]
    return corpus_stats(zs)


def permutation_test(items, nperm, seed=SEED):
    rng = random.Random(seed)
    obs = corpus_stats([it["z"] for it in items])
    nulls = [null_stats(items, rng) for _ in range(nperm)]
    out = {"n_squares": len(items), "observed": obs, "nperm": nperm}
    for key in obs:
        vals = [x[key] for x in nulls]
        out[key] = {"observed": obs[key], "null_mean": statistics.fmean(vals),
                    "p": (1 + sum(v >= obs[key] for v in vals)) / (1 + nperm)}
    diffs = sorted(obs["U"] - x["U"] for x in nulls)
    out["excess_U"] = {"estimate": obs["U"] - out["U"]["null_mean"],
                       "interval_95": [diffs[int(0.025 * nperm)], diffs[int(0.975 * nperm) - 1]]}
    return out


def verdict(test, alpha_support=0.01, alpha_weak=0.05):
    pd, pu = test["D"]["p"], test["U"]["p"]
    if pd < alpha_support and pu < alpha_support:
        return "supported"
    if pd >= alpha_weak and pu >= alpha_weak:
        return "weakened"
    return "open"


def ranks(xs):
    order = sorted(range(len(xs)), key=lambda k: xs[k])
    r = [0.0] * len(xs)
    k = 0
    while k < len(order):
        m = k
        while m + 1 < len(order) and xs[order[m + 1]] == xs[order[k]]:
            m += 1
        for q in range(k, m + 1):
            r[order[q]] = (k + m) / 2 + 1
        k = m + 1
    return r


def spearman(xs, ys):
    rx, ry = ranks(xs), ranks(ys)
    mx, my = statistics.fmean(rx), statistics.fmean(ry)
    sxy = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    sxx = sum((a - mx) ** 2 for a in rx)
    syy = sum((b - my) ** 2 for b in ry)
    return sxy / math.sqrt(sxx * syy) if sxx and syy else 0.0


def a1_alternation(items, nperm, seed=SEED):
    pts = [(it["z"], sum(it["conform"]) / len(it["conform"])) for it in items if len(it["conform"]) >= 3]
    zs, cs = [p[0] for p in pts], [p[1] for p in pts]
    rho = spearman(zs, cs)
    rng = random.Random(seed)
    hits = 0
    for _ in range(nperm):
        c = cs[:]
        rng.shuffle(c)
        hits += abs(spearman(zs, c)) >= abs(rho)
    return {"n_squares": len(pts), "rho": rho, "p_two_sided": (1 + hits) / (1 + nperm)}


def dictionary_seed_ids():
    d = json.load(open(ANALYSIS / "12-dictionary-index" / "rows-in-dictionary.json"))
    return {h["square"] for h in d["hits"] if h["position"] == "top" and h["exact"]}


def a2_dictionary(items, nperm, seed=SEED):
    dic = dictionary_seed_ids()
    lab = [it["id"] in dic for it in items]
    zs = [it["z"] for it in items]

    def diff(labels):
        a = [z for z, l in zip(zs, labels) if l]
        b = [z for z, l in zip(zs, labels) if not l]
        return statistics.fmean(a) - statistics.fmean(b)

    obs = diff(lab)
    rng = random.Random(seed)
    hits = 0
    for _ in range(nperm):
        l = lab[:]
        rng.shuffle(l)
        hits += abs(diff(l)) >= abs(obs)
    return {"n_dictionary": sum(lab), "n_other": len(lab) - sum(lab),
            "mean_z_dictionary_minus_other": obs, "p_two_sided": (1 + hits) / (1 + nperm)}


def class_split(items, cls):
    return [dict(it, letters_cls=[l for l, c in zip(it["letters"], it["cls"]) if c == cls]) for it in items]


def plant_closure(items, rng, share=0.15, prob=0.9):
    """P1: rewrite a random share of squares so interior letters come from the seed."""
    chosen = set(rng.sample(range(len(items)), round(share * len(items))))
    out = []
    for k, it in enumerate(items):
        letters = it["letters"][:]
        if k in chosen:
            for q, c in enumerate(it["cls"]):
                pool = sorted({l for l in it["seed"] if (l in V) == (c == "V")})
                if pool and rng.random() < prob:
                    letters[q] = rng.choice(pool)
        out.append(dict(it, letters=letters))
    return out, sorted(chosen)


def homogeneous_fill(items, rng):
    """P0: every interior letter drawn from the pooled letter frequency of its class."""
    pools = {"V": [], "C": []}
    for it in items:
        for l, c in zip(it["letters"], it["cls"]):
            pools[c].append(l)
    return [dict(it, letters=[rng.choice(pools[c]) for c in it["cls"]]) for it in items]


def dresden_descriptive(m_items):
    """z of each agreed Dresden grid against the Mathers references of its size."""
    by_n = collections.defaultdict(set)
    for it in m_items:
        by_n[it["n"]].add(it["seed"])
    rows = []
    for it in prepare(load_dresden(), drop_motivating=False):
        refs = sorted(by_n[it["n"]] - {it["seed"]})
        if len(refs) < MIN_REFS:
            continue
        ks = [closure(it["letters"], r) for r in refs]
        var = statistics.pvariance(ks)
        if var == 0:
            continue
        k = closure(it["letters"], it["seed"])
        rows.append({"id": it["id"], "seed": it["seed"], "k": k, "m": len(it["letters"]),
                     "E": statistics.fmean(ks), "z": (k - statistics.fmean(ks)) / math.sqrt(var),
                     "conformity": sum(it["conform"]) / len(it["conform"])})
    return rows


def named_list(m, others):
    idx = {name: {it["seed"]: it["z"] for it in items} for name, items in others.items()}
    out = []
    for it in sorted(m, key=lambda x: -x["z"]):
        if it["z"] < 2:
            break
        out.append({"id": it["id"], "seed": it["seed"], "interior": it["interior"],
                    "k": it["k"], "m": len(it["letters"]), "E": round(it["E"], 3), "z": round(it["z"], 3),
                    "conformity": round(sum(it["conform"]) / len(it["conform"]), 3),
                    **{f"z_{name}": (round(v[it["seed"]], 3) if it["seed"] in v else None) for name, v in idx.items()}})
    return out


def run_corpus(corpus, nperm, **kw):
    items, excluded = attach_moments(prepare(corpus, **kw))
    return items, excluded, permutation_test(items, nperm)


def main():
    nperm = NPERM
    results = {"protocol": "PROTOCOL.md", "seed": SEED}
    corpora = {"M": load_mathers(), "W": load_warburg(), "D": load_dehn()}
    items = {}
    for name, corpus in corpora.items():
        it, excl, test = run_corpus(corpus, nperm)
        items[name] = it
        results[name] = {"test": test, "verdict_rule": verdict(test), "excluded": excl}
        print(name, len(it), "squares", {k: (test[k]["observed"], round(test[k]["p"], 4)) for k in "DULS"})
    m = items["M"]
    results["verdict"] = results["M"]["verdict_rule"]
    wt = results["W"]["test"]
    results["replicated_in_W"] = wt["D"]["p"] < 0.05 and wt["U"]["p"] < 0.05
    results["A1_alternation"] = a1_alternation(m, nperm)
    results["A2_dictionary"] = a2_dictionary(m, nperm)

    s1_items, _ = attach_moments(prepare(corpora["M"], drop_motivating=False))
    results["S1_with_motivating"] = permutation_test(s1_items, nperm)
    s2_items, _ = attach_moments(prepare(corpora["M"]), stratify=True)
    results["S2_stratified_references"] = permutation_test(s2_items, nperm)
    for cls in "VC":
        split, _ = attach_moments(class_split(prepare(corpora["M"]), cls), letters_key="letters_cls")
        results[f"S3_{cls}_orbits"] = permutation_test(split, nperm)

    results["named_M_z_ge_2"] = named_list(m, {"W": items["W"], "D": items["D"]})
    results["dresden_descriptive"] = dresden_descriptive(m)

    rng = random.Random(SEED + 1)
    planted, chosen = plant_closure(m, rng)
    planted, _ = attach_moments(planted)
    p1 = permutation_test(planted, 1000)
    results["P1_planted"] = {"n_planted": len(chosen), "test": p1, "verdict_rule": verdict(p1)}
    p0 = []
    for rep in range(20):
        filled, _ = attach_moments(homogeneous_fill(m, random.Random(SEED + 100 + rep)))
        t = permutation_test(filled, 1000, seed=SEED + 200 + rep)
        p0.append({"D_p": t["D"]["p"], "U_p": t["U"]["p"], "verdict_rule": verdict(t)})
    results["P0_homogeneous"] = {
        "replicates": p0,
        "supported": sum(x["verdict_rule"] == "supported" for x in p0),
        "D_p_below_0.05": sum(x["D_p"] < 0.05 for x in p0)}
    results["calibration_ok"] = results["P0_homogeneous"]["supported"] <= 2 and results["P1_planted"]["verdict_rule"] == "supported"

    text = json.dumps(results, indent=1) + "\n"
    out = HERE / "results.json"
    if "--check" in sys.argv:
        assert out.read_text() == text, "results differ from checked-in file"
        print("results reproduce")
        return
    out.write_text(text)
    print("verdict", results["verdict"], "replicated_in_W", results["replicated_in_W"],
          "calibration_ok", results["calibration_ok"])


if __name__ == "__main__":
    main()

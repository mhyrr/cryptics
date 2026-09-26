#!/usr/bin/env python3
"""Post hoc, written after the frozen run: symmetric references.

The frozen estimator excludes a square's own seed from its references, but a
permuted seed is usually inside them. Observed z is then wider than null z and
D is anti-conservative (P0: 7 of 20 homogeneous replicates at p(D) < 0.05).
Here every square's references are all distinct seeds of its size, its own
included, so the moments do not depend on the assignment and the permutation
is exact. Nothing in run.py or results.json is changed.
"""
import json, math, random, statistics, sys, collections

import run


def attach_moments_all(items, letters_key="letters"):
    by_n = collections.defaultdict(set)
    for it in items:
        by_n[it["n"]].add(it["seed"])
    usable, excluded = [], []
    for it in items:
        refs = sorted(by_n[it["n"]])
        letters = it[letters_key]
        if len(refs) < run.MIN_REFS or not letters:
            excluded.append({"id": it["id"], "reason": "fewer than 5 seeds of this size or no letters"})
            continue
        ks = [run.closure(letters, r) for r in refs]
        var = statistics.pvariance(ks)
        if var == 0:
            excluded.append({"id": it["id"], "reason": "zero reference variance"})
            continue
        u = dict(it, letters=letters, E=statistics.fmean(ks), sd=math.sqrt(var), refs=len(refs))
        u["k"] = run.closure(letters, it["seed"])
        u["z"] = (u["k"] - u["E"]) / u["sd"]
        usable.append(u)
    return usable, excluded


def summary(test):
    return {k: {"observed": test[k]["observed"], "null_mean": round(test[k]["null_mean"], 3),
                "p": round(test[k]["p"], 4)} for k in "DULS"} | {"n_squares": test["n_squares"],
                                                                  "excess_U": test["excess_U"]}


def main():
    nperm = run.NPERM
    out = {"status": "post hoc; see README 'Estimator correction'"}
    corpora = {"M": run.load_mathers(), "W": run.load_warburg(), "D": run.load_dehn()}
    for name, corpus in corpora.items():
        items, _ = attach_moments_all(run.prepare(corpus))
        t = run.permutation_test(items, nperm)
        out[name] = {"test": summary(t), "verdict_rule": run.verdict(t)}
        for cls in "VC":
            split, _ = attach_moments_all(run.class_split(run.prepare(corpus), cls), letters_key="letters_cls")
            ts = run.permutation_test(split, nperm)
            out[name][f"{cls}_orbits"] = summary(ts)
        print(name, out[name]["verdict_rule"], {c: (out[name][f"{c}_orbits"]["D"]["p"], out[name][f"{c}_orbits"]["U"]["p"]) for c in "VC"})
    m, _ = attach_moments_all(run.prepare(corpora["M"]))
    reps = []
    for rep in range(20):
        filled, _ = attach_moments_all(run.homogeneous_fill(m, random.Random(run.SEED + 100 + rep)))
        t = run.permutation_test(filled, 1000, seed=run.SEED + 200 + rep)
        reps.append({"D_p": t["D"]["p"], "U_p": t["U"]["p"], "verdict_rule": run.verdict(t)})
    out["P0_homogeneous"] = {"replicates": reps,
                             "supported": sum(x["verdict_rule"] == "supported" for x in reps),
                             "D_p_below_0.05": sum(x["D_p"] < 0.05 for x in reps),
                             "U_p_below_0.05": sum(x["U_p"] < 0.05 for x in reps)}
    print("P0", out["P0_homogeneous"]["supported"], out["P0_homogeneous"]["D_p_below_0.05"], out["P0_homogeneous"]["U_p_below_0.05"])
    text = json.dumps(out, indent=1) + "\n"
    path = run.HERE / "corrected-results.json"
    if "--check" in sys.argv:
        assert path.read_text() == text, "corrected results differ from checked-in file"
        print("corrected results reproduce")
        return
    path.write_text(text)


if __name__ == "__main__":
    main()

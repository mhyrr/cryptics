#!/usr/bin/env python3
"""Is the interior letter free? Every definition is in PROTOCOL.md."""
import collections, json, math, pathlib, random, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent / "13-dehn-witness-test"))
import score as exp13  # agreement(), realign(); not modified

V = "AEIOU"
C = "".join(c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if c not in V)
SEED = 20260920
K = 5.0
LAMBDAS = [0.5 + 0.25 * k for k in range(19)]


def load():
    out, seen, dropped = [], set(), []
    for s in json.load(open(ROOT / "sources" / "mathers-squares.json"))["squares"]:
        rows = [r.upper() for r in s["rows"]]
        n = len(rows)
        if n < 4 or any(len(r) != n for r in rows):
            continue
        g = [[c if "A" <= c <= "Z" else "." for c in r] for r in rows]
        key = tuple("".join(r) for r in g)
        if key in seen:
            dropped.append(s["id"])
            continue
        seen.add(key)
        out.append({"id": s["id"], "chapter": int(s["id"].split("/")[0]), "n": n, "g": g})
    return out, dropped


def orbits(sq):
    n, g, done, res = sq["n"], sq["g"], set(), []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if (i, j) in done:
                continue
            orb = sorted({(i, j), (j, i), (n - 1 - i, n - 1 - j), (n - 1 - j, n - 1 - i)})
            done.update(orb)
            vis = [(a, b) for a, b in orb if g[a][b] != "."]
            if vis:
                a, b = vis[0]
                res.append({"sq": sq["id"], "cell": (a, b), "letter": g[a][b],
                            "cls": "V" if g[a][b] in V else "C"})
    return res


def bits(ps):
    return -sum(math.log2(p) for p in ps) / len(ps)


def base_probs(orbs):
    """Leave-one-square-out M0 distribution for every orbit."""
    tot = {"V": collections.Counter(), "C": collections.Counter()}
    per = collections.defaultdict(lambda: {"V": collections.Counter(), "C": collections.Counter()})
    for o in orbs:
        tot[o["cls"]][o["letter"]] += 1
        per[o["sq"]][o["cls"]][o["letter"]] += 1
    dists = {}
    for sid in per:
        d = {}
        for cls, alpha in (("V", V), ("C", C)):
            cnt = {l: tot[cls][l] - per[sid][cls][l] + 0.5 for l in alpha}
            z = sum(cnt.values())
            d[cls] = {l: v / z for l, v in cnt.items()}
        dists[sid] = d
    return dists


def context_loss(orbs, ctx, dists):
    """LOSO loss and top-one accuracy of the interpolated context model."""
    tot = collections.defaultdict(collections.Counter)
    per = collections.defaultdict(collections.Counter)
    for o, c in zip(orbs, ctx):
        tot[(o["cls"], c)][o["letter"]] += 1
        per[(o["sq"], o["cls"], c)][o["letter"]] += 1
    ps, right = [], 0
    for o, c in zip(orbs, ctx):
        t, own, d = tot[(o["cls"], c)], per[(o["sq"], o["cls"], c)], dists[o["sq"]][o["cls"]]
        nctx = sum(t.values()) - sum(own.values())
        best, bestp = None, -1.0
        for l, p0 in d.items():
            p = (t[l] - own[l] + K * p0) / (nctx + K)
            if p > bestp:
                best, bestp = l, p
            if l == o["letter"]:
                ps.append(p)
        right += best == o["letter"]
    return bits(ps), right / len(orbs)


def seed_model(orbs, seeds, dists):
    by_sq = collections.defaultdict(list)
    for k, o in enumerate(orbs):
        by_sq[o["sq"]].append(k)
    ps, right, lams = [], 0, []
    for sid, held in by_sq.items():
        d = dists[sid]
        S, inseed = [], []
        for k, o in enumerate(orbs):
            if o["sq"] == sid:
                continue
            sd = seeds[o["sq"]]
            S.append(sum(p for l, p in d[o["cls"]].items() if l in sd))
            inseed.append(o["letter"] in sd)
        m = sum(inseed)
        lam = max(LAMBDAS, key=lambda L: m * math.log(L) - sum(math.log(1 + (L - 1) * s) for s in S))
        lams.append(lam)
        for k in held:
            o = orbs[k]
            sd = seeds[sid]
            w = {l: p * (lam if l in sd else 1.0) for l, p in d[o["cls"]].items()}
            z = sum(w.values())
            ps.append(w[o["letter"]] / z)
            right += max(w, key=w.get) == o["letter"]
    return bits(ps), right / len(orbs), sum(lams) / len(lams)


def plug_in(letters_by_class):
    out = {}
    for cls, letters in letters_by_class.items():
        c = collections.Counter(letters)
        n = sum(c.values())
        h = -sum(v / n * math.log2(v / n) for v in c.values())
        out[cls] = {"n": n, "distinct": len(c), "plug_in_bits": round(h, 3),
                    "miller_madow_bits": round(h + (len(c) - 1) / (2 * n * math.log(2)), 3),
                    "uniform_bits": round(math.log2(5 if cls == "V" else 21), 3),
                    "top": c.most_common(6)}
    n = sum(v["n"] for v in out.values())
    out["weighted_miller_madow_bits"] = round(sum(v["n"] * v["miller_madow_bits"] for v in list(out.values())) / n, 3)
    return out


def main():
    rng = random.Random(SEED)
    squares, dropped = load()
    by_id = {s["id"]: s for s in squares}
    orbs = [o for s in squares for o in orbits(s)]
    dists = base_probs(orbs)
    princes = {}
    for grp, chs in json.load(open(HERE / "princes.json"))["groups"].items():
        for ch in chs:
            princes[ch] = grp
    res = {"squares": len(squares), "duplicates_dropped": dropped, "interior_orbits": len(orbs),
           "class_counts": dict(collections.Counter(o["cls"] for o in orbs))}

    # ---- entropy, plug-in
    res["entropy_plug_in"] = {
        "interior_orbits": plug_in({c: [o["letter"] for o in orbs if o["cls"] == c] for c in "VC"}),
        "top_row_cells": plug_in({c: [x for s in squares for x in s["g"][0] if x != "." and (x in V) == (c == "V")] for c in "VC"}),
    }

    # ---- context models
    def ctx_of(name):
        out = []
        for o in orbs:
            s = by_id[o["sq"]]
            i, j = o["cell"]
            if name == "chapter": out.append(s["chapter"])
            elif name == "prince": out.append(princes[s["chapter"]])
            elif name == "position": out.append((i == j, min(i, s["n"] - 1 - i, j, s["n"] - 1 - j) == 1))
            elif name == "above": out.append(s["g"][i - 1][j])
            elif name == "upleft": out.append(s["g"][i - 1][j - 1])
            elif name == "size": out.append(s["n"])
        return out

    ps0, right0 = [], 0
    for o in orbs:
        d = dists[o["sq"]][o["cls"]]
        ps0.append(d[o["letter"]])
        right0 += max(d, key=d.get) == o["letter"]
    m0 = bits(ps0)
    models = {"M0_class_only": {"bits": round(m0, 4), "top1": round(right0 / len(orbs), 4)}}

    sq_ids = [s["id"] for s in squares]

    def permute(name, ctx):
        if name in ("chapter", "prince", "size"):
            lab = {s["id"]: (s["chapter"] if name == "chapter" else princes[s["chapter"]] if name == "prince" else s["n"]) for s in squares}
            vals = [lab[i] for i in sq_ids]
            rng.shuffle(vals)
            m = dict(zip(sq_ids, vals))
            return [m[o["sq"]] for o in orbs]
        groups = collections.defaultdict(list)
        for k, o in enumerate(orbs):
            groups[(o["sq"], o["cls"]) if name == "position" else o["cls"]].append(k)
        new = list(ctx)
        for ks in groups.values():
            vals = [ctx[k] for k in ks]
            rng.shuffle(vals)
            for k, v in zip(ks, vals):
                new[k] = v
        return new

    for tag, name, nperm in (("M1_chapter", "chapter", 1000), ("M2_prince", "prince", 1000),
                             ("M4_position", "position", 500), ("M5_letter_above", "above", 500),
                             ("M6_letter_upleft", "upleft", 500), ("M7_size", "size", 500)):
        ctx = ctx_of(name)
        b, t1 = context_loss(orbs, ctx, dists)
        null = [context_loss(orbs, permute(name, ctx), dists)[0] for _ in range(nperm)]
        models[tag] = {"bits": round(b, 4), "gain_vs_M0": round(m0 - b, 4), "top1": round(t1, 4),
                       "perm_mean_bits": round(sum(null) / nperm, 4), "perm_min_bits": round(min(null), 4),
                       "p": round((1 + sum(x <= b for x in null)) / (nperm + 1), 4), "permutations": nperm}
    seeds = {s["id"]: set(x for x in s["g"][0] if x != ".") for s in squares}
    b, t1, lam = seed_model(orbs, seeds, dists)
    models["M3_seed_weight"] = {"bits": round(b, 4), "gain_vs_M0": round(m0 - b, 4), "top1": round(t1, 4), "mean_lambda": round(lam, 3)}
    res["models"] = models

    # ---- T3 reuse
    full = [s for s in squares if "." not in s["g"][0]]
    fo = [o for o in orbs if "." not in by_id[o["sq"]]["g"][0]]
    def reuse(seedmap, cls=None):
        xs = [o["letter"] in seedmap[o["sq"]] for o in fo if cls in (None, o["cls"])]
        return sum(xs) / len(xs)
    real = {s["id"]: set(s["g"][0]) for s in full}
    obs = {k: reuse(real, c) for k, c in (("all", None), ("vowels", "V"), ("consonants", "C"))}
    null = collections.defaultdict(list)
    bysize = collections.defaultdict(list)
    for s in full:
        bysize[s["n"]].append(s["id"])
    for _ in range(2000):
        m = {}
        for ids in bysize.values():
            sh = ids[:]
            rng.shuffle(sh)
            m.update({a: real[b] for a, b in zip(ids, sh)})
        for k, c in (("all", None), ("vowels", "V"), ("consonants", "C")):
            null[k].append(reuse(m, c))
    res["T3_seed_reuse"] = {k: {"orbits": sum(1 for o in fo if (k == "all") or o["cls"] == k[0].upper()),
                                "observed": round(obs[k], 4), "control_mean": round(sum(null[k]) / 2000, 4),
                                "control_max": round(max(null[k]), 4),
                                "p": round((1 + sum(x >= obs[k] for x in null[k])) / 2001, 4)} for k in obs}

    # ---- T4 AREPO
    def t4(exclude_sator):
        pool = []
        for s in squares:
            g = s["g"]
            if s["n"] != 5 or g[1][1] == "." or g[1][1] in V:
                continue
            if exclude_sator and ("".join(g[1]) == "AREPO" or "".join(g[0]) in ("SATOR", "ROTAS")):
                continue
            cons = [o for o in orbs if o["sq"] == s["id"] and o["cls"] == "C"]
            pool.append((g[1][1], [o["letter"] for o in cons], [o["cell"] for o in cons].index((1, 1))))
        obs_r = sum(a == "R" for a, _, _ in pool)
        null = []
        for _ in range(2000):
            k = 0
            for _, letters, idx in pool:
                sh = letters[:]
                rng.shuffle(sh)
                k += sh[idx] == "R"
            null.append(k)
        others = [l for _, letters, idx in pool for q, l in enumerate(letters) if q != idx]
        return {"squares": len(pool), "R_at_row2_col2": obs_r, "control_mean": round(sum(null) / 2000, 3),
                "control_max": max(null), "p": round((1 + sum(x >= obs_r for x in null)) / 2001, 4),
                "R_share_other_interior_consonant_orbits": f"{sum(l == 'R' for l in others)}/{len(others)}",
                "letters_at_row2_col2": collections.Counter(a for a, _, _ in pool).most_common()}
    res["T4_arepo"] = {"all": t4(False), "without_sator_family": t4(True)}

    # ---- T5 witness disagreement
    mathers = {s["id"]: s["rows"] for s in json.load(open(ROOT / "sources" / "mathers-squares.json"))["squares"]}
    dehn0 = json.load(open(HERE.parent / "13-dehn-witness-test" / "dehn-readings.json"))["squares"]
    def t5(dehn):
        pairs = []
        for d in dehn:
            rows, n = d["rows"], len(d["rows"])
            m = mathers.get(d["id"])
            if not m or len(m) != n or any(len(r) != n for r in m) or any(len(r) != n for r in rows) or n < 4:
                continue
            if not all(c.isalpha() for r in rows for c in r):
                continue
            s, b = exp13.agreement(m, rows)
            if not b or s / b < 0.5:
                continue
            cells = []
            for i in range(n):
                for j in range(n):
                    if m[i][j] == ".":
                        continue
                    zone = "top" if i == 0 else ("border" if i == n - 1 or j in (0, n - 1) else "interior")
                    cells.append((zone, m[i][j].upper() != rows[i][j].upper()))
            pairs.append(cells)
        raw = collections.defaultdict(lambda: [0, 0])
        for cells in pairs:
            for z, dflag in cells:
                raw[z][0] += dflag
                raw[z][1] += 1
        out = {"pairs": len(pairs), "raw": {z: f"{a}/{b}" for z, (a, b) in raw.items()}}
        for tag, keep in (("interior_vs_all_border", ("top", "border", "interior")), ("interior_vs_top_row", ("top", "interior"))):
            sub = [[c for c in cells if c[0] in keep] for cells in pairs]
            obs_i = sum(dflag for cells in sub for z, dflag in cells if z == "interior")
            null = []
            for _ in range(5000):
                k = 0
                for cells in sub:
                    flags = [f for _, f in cells]
                    rng.shuffle(flags)
                    k += sum(f for (z, _), f in zip(cells, flags) if z == "interior")
                null.append(k)
            out[tag] = {"interior_disagreements": obs_i, "control_mean": round(sum(null) / 5000, 2),
                        "control_max": max(null), "p_interior_excess": round((1 + sum(x >= obs_i for x in null)) / 5001, 4)}
        return out
    res["T5_witness_disagreement"] = {"frozen_alignment": t5(dehn0), "post_hoc_realignment": t5(exp13.realign(dehn0, mathers))}

    # ---- verdict by the frozen rule
    gains = {k: v["gain_vs_M0"] for k, v in models.items() if k != "M0_class_only"}
    tops = {k: v["top1"] for k, v in models.items() if k != "M0_class_only"}
    if max(tops.values()) >= 0.50 or max(gains.values()) >= 1.0:
        verdict = "keeps A alive"
    elif max(gains.values()) < 0.5 and max(tops.values()) < 0.40:
        verdict = "supports B"
    else:
        verdict = "undecided"
    res["verdict_by_frozen_rule"] = {"verdict": verdict, "best_gain_bits": max(gains.values()), "best_top1": max(tops.values())}
    (HERE / "results.json").write_text(json.dumps(res, indent=1, default=str) + "\n")
    print(json.dumps({k: res[k] for k in res if k != "duplicates_dropped"}, indent=1, default=str))


if __name__ == "__main__":
    main()

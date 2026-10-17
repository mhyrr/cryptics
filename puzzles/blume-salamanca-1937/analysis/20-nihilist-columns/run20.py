"""Experiment 20: controls, noise, thresholds, target and summary for nihcols.py. The plan is README.md.
Usage (from this folder): python3 -I run20.py controls|noise|thresholds|target|summary
Reuses 18's run.py for the telegrams and the resumable job runner, and its pass rule (adjacency >= 0.90, 8/10).
"""
import json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "18-periodic-solver"))
import nihcols, setsolve  # noqa: E402
import run  # noqa: E402  (18's runner; puts 01-solver on sys.path and makes it the working directory)
import plaintext  # noqa: E402

AZ = run.AZ
BANDS = {"T1": [(5, 8), (9, 12), (13, 16), (17, 20), (21, 24)], "T2": [(5, 8), (9, 11)]}  # T2 9-12 -> 9-11: README amendment
TARGET_NS = {"T1": range(5, 25), "T2": range(5, 12)}
F = {k: os.path.join(HERE, f"{k}.jsonl") for k in ("controls", "noise", "target")}
F_THRESH = os.path.join(HERE, "thresholds.json")


def band_of(text, n):
    return next(f"{lo}-{hi}" for lo, hi in BANDS[text] if lo <= n <= hi)


def control_jobs():
    pr, sr = random.Random("20-plant"), random.Random("20-control-solver")
    jobs = []
    for text in ("T1", "T2"):
        for lo, hi in BANDS[text]:
            for i in range(run.PER_BAND):
                jobs.append(dict(text=text, band=f"{lo}-{hi}", i=i, n=pr.randint(lo, hi), p=pr.randint(0, 20),
                                 b=pr.randint(0, 20), plant_seed=pr.randrange(1 << 30), solver_seed=sr.randrange(1 << 30)))
    return jobs


def control_one(j):
    n, p, b = j["n"], j["p"], j["b"]
    rnd = random.Random(j["plant_seed"]); k = rnd.sample(range(n), n)
    body = plaintext.telegram(run.LENGTH[j["text"]] - p - b, rnd)
    ct, idx = nihcols.plant(body, k, rnd, "".join(rnd.choice(AZ) for _ in range(p)),
                            "".join(rnd.choice(AZ) for _ in range(b)))
    true = [k.index(t) for t in range(n)]
    seeds_rnd = random.Random(j["solver_seed"]); seeds = [seeds_rnd.randrange(1 << 30) for _ in range(21)]
    assert random.Random(seeds[p]).sample(range(n), n) != true, "solver would start at the planted key"
    t0 = time.time(); s, pp, o = nihcols.solve_scan(ct, n, j["solver_seed"]); dt = time.time() - t0
    r, ridx = nihcols.rearrange(ct, n, pp, idx)
    acc = setsolve.adjacency_acc(ridx, o, 0)
    rt = nihcols.rearrange(ct, n, p)
    return dict(j, score=round(s, 4), p_found=pp, adj=round(acc, 4), recovered=acc >= run.PASS_ADJ,
                true_score=round(setsolve.qrows(setsolve.columns(rt, n, 0), true), 4), secs=round(dt, 1), order=o)


def noise_jobs():
    sh, sr = random.Random("20-noise"), random.Random("20-noise-solver")
    return [dict(text=text, band=f"{lo}-{hi}", n=hi, i=i, shuffle_seed=sh.randrange(1 << 30), solver_seed=sr.randrange(1 << 30))
            for text in ("T1", "T2") for lo, hi in BANDS[text] for i in range(3)]


def noise_one(j):
    letters = list(run.telegram(j["text"])); random.Random(j["shuffle_seed"]).shuffle(letters)
    s, p, o = nihcols.solve_scan("".join(letters), j["n"], j["solver_seed"])
    return dict(j, score=round(s, 4), p_found=p, order=o)


def thresholds():
    C = [json.loads(l) for l in open(F["controls"])]; N = [json.loads(l) for l in open(F["noise"])]
    assert len(C) == len(control_jobs()) and len(N) == len(noise_jobs())
    out = {}
    for text in ("T1", "T2"):
        for lo, hi in BANDS[text]:
            band = f"{lo}-{hi}"; cs = [c for c in C if (c["text"], c["band"]) == (text, band)]
            rec = sum(c["recovered"] for c in cs); nm = max(x["score"] for x in N if (x["text"], x["band"]) == (text, band))
            rs = [c["score"] for c in cs if c["recovered"]]; low = min(rs) if rs else None
            thr, rule = ((nm + low) / 2, "midpoint") if low is not None and low > nm else (nm, "overlap: noise maximum")
            out[f"{text} {band}"] = dict(passed=rec >= run.PASS_K, recovered=rec, noise_max=nm, lowest_recovered=low,
                                         threshold=round(thr, 4), rule=rule)
    json.dump(out, open(F_THRESH, "w"), indent=1); print(json.dumps(out, indent=1))


def target_jobs():
    sr = random.Random("20-target-solver")
    return [dict(text=t, n=n, band=band_of(t, n), solver_seed=sr.randrange(1 << 30)) for t in ("T1", "T2") for n in TARGET_NS[t]]


def target_one(j):
    ct = run.telegram(j["text"]); s, p, o = nihcols.solve_scan(ct, j["n"], j["solver_seed"])
    return dict(j, score=round(s, 4), p_found=p, order=o,
                reading="".join(setsolve.dec_rows(nihcols.rearrange(ct, j["n"], p), o, 0))[:80])


def summary():
    C = [json.loads(l) for l in open(F["controls"])] if os.path.exists(F["controls"]) else []
    T = json.load(open(F_THRESH)) if os.path.exists(F_THRESH) else {}
    X = [json.loads(l) for l in open(F["target"])] if os.path.exists(F["target"]) else []
    print("| telegram | band | recovered | median adj | recovered scores | noise max | threshold | verdict |\n|---|---|---|---|---|---|---|---|")
    for text in ("T1", "T2"):
        for lo, hi in BANDS[text]:
            band = f"{lo}-{hi}"; cs = sorted(c["adj"] for c in C if (c["text"], c["band"]) == (text, band))
            rs = [c["score"] for c in C if (c["text"], c["band"]) == (text, band) and c["recovered"]]; t = T.get(f"{text} {band}", {})
            print(f"| {text} | {band} | {sum(a >= run.PASS_ADJ for a in cs)}/{len(cs)} | {cs[len(cs) // 2] if cs else '—'} | "
                  f"{(f'{min(rs):.3f} to {max(rs):.3f}') if rs else '—'} | {t.get('noise_max', '—')} | {t.get('threshold', '—')} | "
                  f"{('pass' if t.get('passed') else 'not testable') if t else '—'} |")
    if X:
        print("\n| telegram | n | score | threshold | margin | p | reading, first 80 |\n|---|---|---|---|---|---|---|")
        for x in sorted(X, key=lambda x: (x["text"], x["n"])):
            t = T[f"{x['text']} {x['band']}"]["threshold"]
            print(f"| {x['text']} | {x['n']} | {x['score']:.3f} | {t:.3f} | {x['score'] - t:+.3f} | {x['p_found']} | {x['reading']} |")
        cand = [x for x in X if x["score"] > T[f"{x['text']} {x['band']}"]["threshold"]]
        print(f"\nCandidates above threshold: {len(cand)}")


def main():
    cmd = sys.argv[1]
    if cmd == "controls":
        run.run_jobs(control_jobs(), control_one, F["controls"], lambda j: (j["text"], j["band"], j["i"]))
    elif cmd == "noise":
        run.run_jobs(noise_jobs(), noise_one, F["noise"], lambda j: (j["text"], j["band"], j["i"]))
    elif cmd == "thresholds":
        thresholds()
    elif cmd == "target":
        if not os.path.exists(F_THRESH):
            sys.exit("thresholds.json missing: run controls, noise and thresholds first (README plan)")
        T = json.load(open(F_THRESH))
        run.run_jobs([j for j in target_jobs() if T[f"{j['text']} {j['band']}"]["passed"]], target_one, F["target"],
                     lambda j: (j["text"], j["n"]))
    elif cmd == "summary":
        summary()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()

"""Experiment 18: controls, noise ceiling, thresholds, target and summary for setsolve.py. The plan is README.md.

Usage (from this folder):
  python3 -I run.py controls     -> controls.jsonl   (resumes: plants already in the file are skipped)
  python3 -I run.py noise        -> noise.jsonl      (resumes)
  python3 -I run.py thresholds   -> thresholds.json  (from controls.jsonl and noise.jsonl)
  python3 -I run.py target       -> target.jsonl     (refuses without thresholds.json; resumes)
  python3 -I run.py summary      -> markdown tables on stdout

Seeds: string-keyed streams (Python hashes a str seed with SHA-512, so they do not depend on PYTHONHASHSEED).
"18-plant" draws every plant's n, p, b and plant seed; "18-control-solver" its solver seed; "18-noise" the
shuffle seeds; "18-noise-solver" and "18-target-solver" the solver seeds of those runs, in a fixed order.
"""
import json, os, random, sys, time
from concurrent.futures import ProcessPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import setsolve  # noqa: E402
sys.path.insert(0, os.path.join(HERE, "..", "01-solver")); os.chdir(os.path.join(HERE, "..", "01-solver"))
import plaintext  # noqa: E402

WORKERS = 3
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PASS_ADJ, PASS_K, PER_BAND = 0.90, 8, 10
BANDS = {"T1": [(8, 10), (11, 15), (16, 20), (21, 30), (31, 40), (41, 50)],
         "T2": [(8, 10), (11, 15), (16, 20), (21, 30)]}
LENGTH = {"T1": 615, "T2": 160}
FAMILIES = ("sets", "nihilist")
NOISE_SHUFFLES = 3
F_CONTROLS, F_NOISE = os.path.join(HERE, "controls.jsonl"), os.path.join(HERE, "noise.jsonl")
F_THRESH, F_TARGET = os.path.join(HERE, "thresholds.json"), os.path.join(HERE, "target.jsonl")


def telegram(name):
    path = os.path.join(HERE, "../../sources", "telegram-1.txt" if name == "T1" else "telegram-2.txt")
    t = "".join(c for c in open(path).read().upper() if c.isalpha())
    assert len(t) == LENGTH[name]
    return t


def band_of(text, n):
    for lo, hi in BANDS[text]:
        if lo <= n <= hi:
            return f"{lo}-{hi}"
    return None


def done_keys(path, key):
    if not os.path.exists(path):
        return set()
    return {key(json.loads(l)) for l in open(path) if l.strip()}


def run_jobs(jobs, fn, path, key):
    have = done_keys(path, key)
    todo = [j for j in jobs if key(j) not in have]
    todo.sort(key=lambda j: -j["n"] * j["n"] * LENGTH[j["text"]])  # largest first
    print(f"{len(todo)} to run, {len(jobs) - len(todo)} already done", file=sys.stderr, flush=True)
    with ProcessPoolExecutor(WORKERS) as ex, open(path, "a") as out:
        futs = [ex.submit(fn, j) for j in todo]
        for f in as_completed(futs):
            r = f.result(); out.write(json.dumps(r) + "\n"); out.flush()
            print(json.dumps({k: v for k, v in r.items() if k not in ("order", "reading")}), file=sys.stderr, flush=True)


# ---------------------------------------------------------------- controls
def control_jobs():
    pr, sr = random.Random("18-plant"), random.Random("18-control-solver")
    jobs = []
    for text in ("T1", "T2"):
        for lo, hi in BANDS[text]:
            for fam in FAMILIES:
                for i in range(PER_BAND):
                    jobs.append(dict(text=text, band=f"{lo}-{hi}", family=fam, i=i, n=pr.randint(lo, hi),
                                     p=pr.randint(0, 20), b=pr.randint(0, 20), plant_seed=pr.randrange(1 << 30),
                                     solver_seed=sr.randrange(1 << 30)))
    assert all(j["plant_seed"] != j["solver_seed"] for j in jobs)
    return jobs


def control_key(j):
    return (j["text"], j["band"], j["family"], j["i"])


def first_start(solver_seed, n, a):
    """setsolve.solve_scan draws one seed per offset from Random(solver_seed); solve's first stage-1 start at
    offset a is Random(that seed).sample(range(n), n)."""
    rnd = random.Random(solver_seed); seeds = [rnd.randrange(1 << 30) for _ in range(n)]
    return random.Random(seeds[a]).sample(range(n), n)


def control_one(j):
    n, p, b = j["n"], j["p"], j["b"]
    rnd = random.Random(j["plant_seed"]); k = rnd.sample(range(n), n)
    body = plaintext.telegram(LENGTH[j["text"]] - p - b, rnd)
    pre, post = "".join(rnd.choice(AZ) for _ in range(p)), "".join(rnd.choice(AZ) for _ in range(b))
    ct, idx = setsolve.plant(body, k, j["family"], rnd, pre, post)
    true = [k.index(t) for t in range(n)]
    assert first_start(j["solver_seed"], n, p % n) != true, "solver would start at the planted key"
    t0 = time.time(); s, a, o = setsolve.solve_scan(ct, n, j["solver_seed"]); dt = time.time() - t0
    acc = setsolve.adjacency_acc(idx, o, a)
    true_s = setsolve.qrows(setsolve.columns(ct, n, p % n), true)
    return dict(j, score=round(s, 4), a=a, adj=round(acc, 4), recovered=acc >= PASS_ADJ,
                true_score=round(true_s, 4), secs=round(dt, 1), order=o)


# ---------------------------------------------------------------- noise
def noise_jobs():
    sh, sr = random.Random("18-noise"), random.Random("18-noise-solver")
    jobs = []
    for text in ("T1", "T2"):
        for lo, hi in BANDS[text]:
            for i in range(NOISE_SHUFFLES):
                jobs.append(dict(text=text, band=f"{lo}-{hi}", n=hi, i=i, shuffle_seed=sh.randrange(1 << 30),
                                 solver_seed=sr.randrange(1 << 30)))
    return jobs


def noise_key(j):
    return (j["text"], j["band"], j["i"])


def noise_one(j):
    letters = list(telegram(j["text"])); random.Random(j["shuffle_seed"]).shuffle(letters)
    t0 = time.time(); s, a, o = setsolve.solve_scan("".join(letters), j["n"], j["solver_seed"])
    return dict(j, score=round(s, 4), a=a, secs=round(time.time() - t0, 1), order=o)


# ---------------------------------------------------------------- thresholds
def thresholds():
    C = [json.loads(l) for l in open(F_CONTROLS)]
    N = [json.loads(l) for l in open(F_NOISE)]
    assert len(C) == len(control_jobs()) and len(N) == len(noise_jobs()), "controls or noise incomplete"
    out = {}
    for text in ("T1", "T2"):
        for lo, hi in BANDS[text]:
            band = f"{lo}-{hi}"
            rec = {f: sum(c["recovered"] for c in C if (c["text"], c["band"], c["family"]) == (text, band, f))
                   for f in FAMILIES}
            passed = all(v >= PASS_K for v in rec.values())
            noise_max = max(x["score"] for x in N if (x["text"], x["band"]) == (text, band))
            rs = [c["score"] for c in C if (c["text"], c["band"]) == (text, band) and c["recovered"]]
            low = min(rs) if rs else None
            if low is not None and low > noise_max:
                thr, rule = (noise_max + low) / 2, "midpoint"
            else:
                thr, rule = noise_max, "overlap: noise maximum, candidates checked by reading"
            out[f"{text} {band}"] = dict(passed=passed, recovered=rec, noise_max=noise_max, lowest_recovered=low,
                                         threshold=round(thr, 4), rule=rule)
    json.dump(out, open(F_THRESH, "w"), indent=1)
    print(json.dumps(out, indent=1))


# ---------------------------------------------------------------- target
def target_jobs():
    sr = random.Random("18-target-solver")
    jobs = []
    for text, ns in (("T1", range(8, 51)), ("T2", range(8, 31))):
        for n in ns:
            jobs.append(dict(text=text, n=n, band=band_of(text, n), solver_seed=sr.randrange(1 << 30)))
    return jobs


def target_key(j):
    return (j["text"], j["n"])


def target_one(j):
    ct = telegram(j["text"])
    t0 = time.time(); s, a, o = setsolve.solve_scan(ct, j["n"], j["solver_seed"])
    reading = "".join(setsolve.dec_rows(ct, o, a))[:80]
    return dict(j, score=round(s, 4), a=a, secs=round(time.time() - t0, 1), order=o, reading=reading)


# ---------------------------------------------------------------- summary
def summary():
    C = [json.loads(l) for l in open(F_CONTROLS)] if os.path.exists(F_CONTROLS) else []
    T = json.load(open(F_THRESH)) if os.path.exists(F_THRESH) else {}
    X = [json.loads(l) for l in open(F_TARGET)] if os.path.exists(F_TARGET) else []
    print("### Controls (recovered / 10; median adjacency; solver score range of recovered plants)\n")
    print("| telegram | band | sets | nihilist | recovered scores | noise max | threshold | verdict |")
    print("|---|---|---|---|---|---|---|---|")
    for text in ("T1", "T2"):
        for lo, hi in BANDS[text]:
            band = f"{lo}-{hi}"; cells = []
            for f in FAMILIES:
                cs = sorted(c["adj"] for c in C if (c["text"], c["band"], c["family"]) == (text, band, f))
                k = sum(a >= PASS_ADJ for a in cs)
                cells.append(f"{k}/{len(cs)} (med {cs[len(cs) // 2]:.2f})" if cs else "—")
            rs = [c["score"] for c in C if (c["text"], c["band"]) == (text, band) and c["recovered"]]
            t = T.get(f"{text} {band}", {})
            rng = f"{min(rs):.3f} to {max(rs):.3f}" if rs else "—"
            verdict = ("pass" if t.get("passed") else "not testable") if t else "—"
            print(f"| {text} | {band} | {cells[0]} | {cells[1]} | {rng} | {t.get('noise_max', '—')} | "
                  f"{t.get('threshold', '—')} | {verdict} |")
    if X:
        print("\n### Target (best over all offsets, per n)\n")
        print("| telegram | n | band | score | threshold | margin | offset | reading, first 80 |")
        print("|---|---|---|---|---|---|---|---|")
        for x in sorted(X, key=lambda x: (x["text"], x["n"])):
            t = T[f"{x['text']} {x['band']}"]["threshold"]
            print(f"| {x['text']} | {x['n']} | {x['band']} | {x['score']:.3f} | {t:.3f} | {x['score'] - t:+.3f} | "
                  f"{x['a']} | {x['reading']} |")
        cand = [x for x in X if x["score"] > T[f"{x['text']} {x['band']}"]["threshold"]]
        print(f"\nCandidates above threshold: {len(cand)}")
        for x in cand:
            print(f"- {x['text']} n {x['n']} offset {x['a']}: {x['score']:.3f} {x['reading']}")


def main():
    cmd = sys.argv[1]
    if cmd == "controls":
        run_jobs(control_jobs(), control_one, F_CONTROLS, control_key)
    elif cmd == "noise":
        run_jobs(noise_jobs(), noise_one, F_NOISE, noise_key)
    elif cmd == "thresholds":
        thresholds()
    elif cmd == "target":
        if not os.path.exists(F_THRESH):
            sys.exit("thresholds.json missing: run controls, noise and thresholds first (README plan)")
        T = json.load(open(F_THRESH))
        jobs = [j for j in target_jobs() if T[f"{j['text']} {j['band']}"]["passed"]]
        run_jobs(jobs, target_one, F_TARGET, target_key)
    elif cmd == "summary":
        summary()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()

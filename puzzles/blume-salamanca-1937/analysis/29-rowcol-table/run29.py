"""Experiment 29: controls, noise, calibration plants, thresholds, target and summary. The plan is README.md.
Usage (from this folder): python3 -I run29.py controls|noise|calib|thresholds|target|summary
Reuses 18's setsolve.solve unchanged (fixed offset 0, every letter scored), 18's run.py for the telegrams and the
resumable job runner, and its pass rule (adjacency >= 0.90, 8/10).

Seeds: string-keyed streams "29-plant", "29-control-solver", "29-noise", "29-noise-solver", "29-calib-plant",
"29-calib-solver", "29-target-shuffle", "29-target-solver", each drawn in a fixed order.
"""
import json, os, random, re, sys, time, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "18-periodic-solver"))
import rowcol, setsolve  # noqa: E402
import run  # noqa: E402  (18's runner; puts 01-solver on sys.path and makes it the working directory)
import plaintext  # noqa: E402

run.WORKERS = 6
AZ = run.AZ
PER_CELL, NOISE_SHUFFLES, CALIB_PER_CELL = 10, 3, 5
LENGTH = {"T1": 615, "T2": 160}
WIDTHS = {"T1": (15, 41), "T2": (8, 10, 16, 20)}
CELLS = [dict(text=t, w=w, direction=d, n=rowcol.set_size(LENGTH[t], w, d))
         for t in ("T1", "T2") for w in WIDTHS[t] for d in rowcol.DIRECTIONS]
F = {k: os.path.join(HERE, f"{k}.jsonl") for k in ("controls", "noise", "calibration", "target")}
F_THRESH = os.path.join(HERE, "thresholds.json")
CALIB_MD = os.path.join(HERE, "..", "..", "sources", "historical-evidence", "calibration-telegrams.md")


def cell_id(c):
    return f"{c['text']} w{c['w']} {c['direction']} n{c['n']}"


def cpu():
    return time.process_time()


# ---------------------------------------------------------------- one plant, solved at offset 0
def solve_plant(body, w, direction, plant_rnd, solver_seed):
    L = len(body); h = L // w; n = rowcol.set_size(L, w, direction)
    ckey = plant_rnd.sample(range(w), w); rkey = plant_rnd.sample(range(h), h)
    ct = rowcol.encrypt(body, w, ckey, rkey, direction)
    rt = rowcol.rearrange(ct, w, direction)
    ridx = rowcol.rearrange(rowcol.encrypt(list(range(L)), w, ckey, rkey, direction), w, direction)
    true = rowcol.true_order(ridx, n)
    assert random.Random(solver_seed).sample(range(n), n) != true, "solver would start at the planted order"
    t0 = cpu(); s, o = setsolve.solve(rt, n, 0, solver_seed); dt = cpu() - t0
    acc = setsolve.adjacency_acc(ridx, o, 0)
    true_s = setsolve.qrows(setsolve.columns(rt, n, 0), true)
    return dict(score=round(s, 4), adj=round(acc, 4), recovered=acc >= run.PASS_ADJ, true_score=round(true_s, 4),
                cpu_s=round(dt, 2), ckey=ckey, rkey=rkey, order=o, ct=ct)


def control_jobs():
    pr, sr = random.Random("29-plant"), random.Random("29-control-solver")
    jobs = [dict(c, cell=cell_id(c), i=i, plant_seed=pr.randrange(1 << 30), solver_seed=sr.randrange(1 << 30))
            for c in CELLS for i in range(PER_CELL)]
    assert all(j["plant_seed"] != j["solver_seed"] for j in jobs)
    return jobs


def control_one(j):
    rnd = random.Random(j["plant_seed"])
    body = plaintext.telegram(LENGTH[j["text"]], rnd)
    assert len(body) == LENGTH[j["text"]] and set(body) <= set(AZ)
    return dict(j, **solve_plant(body, j["w"], j["direction"], rnd, j["solver_seed"]))


# ---------------------------------------------------------------- noise
def noise_jobs():
    sh, sr = random.Random("29-noise"), random.Random("29-noise-solver")
    jobs = []
    for t in ("T1", "T2"):
        for n in sorted({c["n"] for c in CELLS if c["text"] == t}):
            for i in range(NOISE_SHUFFLES):
                seed = sh.randrange(1 << 30)
                for c in CELLS:
                    if (c["text"], c["n"]) == (t, n):
                        jobs.append(dict(c, cell=cell_id(c), i=i, shuffle_seed=seed, solver_seed=sr.randrange(1 << 30)))
    return jobs


def noise_one(j):
    letters = list(run.telegram(j["text"])); random.Random(j["shuffle_seed"]).shuffle(letters)
    rt = rowcol.rearrange("".join(letters), j["w"], j["direction"])
    t0 = cpu(); s, o = setsolve.solve(rt, j["n"], 0, j["solver_seed"]); dt = cpu() - t0
    return dict(j, score=round(s, 4), cpu_s=round(dt, 2), order=o)


# ---------------------------------------------------------------- calibration plants (descriptive)
def normalize(s):
    s = unicodedata.normalize("NFD", s.upper())
    return "".join(ch for ch in s if ch in AZ)


def calib_texts():
    md = open(CALIB_MD, encoding="utf-8").read()
    out = {}
    for name, head in (("P1", "\n## P1."), ("M1", "\n### M1 ")):
        sec = md[md.index(head):]
        out[name] = normalize(re.search(r"```\n(.*?)```", sec, re.S).group(1))
    assert len(out["P1"]) == 1654 and len(out["M1"]) == 903, {k: len(v) for k, v in out.items()}
    return out


def calib_jobs():
    pr, sr = random.Random("29-calib-plant"), random.Random("29-calib-solver")
    T = {k: len(v) for k, v in calib_texts().items()}
    jobs = []
    for c in CELLS:
        if c["text"] != "T1":
            continue
        for i in range(CALIB_PER_CELL):
            src = "P1" if i % 2 == 0 else "M1"
            jobs.append(dict(c, cell=cell_id(c), i=i, source=src, start=pr.randint(0, T[src] - 615),
                             plant_seed=pr.randrange(1 << 30), solver_seed=sr.randrange(1 << 30)))
    return jobs


def calib_one(j):
    body = calib_texts()[j["source"]][j["start"]:j["start"] + 615]
    return dict(j, **solve_plant(body, j["w"], j["direction"], random.Random(j["plant_seed"]), j["solver_seed"]))


# ---------------------------------------------------------------- thresholds
def load(k):
    return [json.loads(l) for l in open(F[k]) if l.strip()] if os.path.exists(F[k]) else []


def thresholds():
    C, N = load("controls"), load("noise")
    assert len(C) == len(control_jobs()) and len(N) == len(noise_jobs())
    out = {}
    for c in CELLS:
        cid = cell_id(c); cs = [x for x in C if x["cell"] == cid]
        nm = max(x["score"] for x in N if (x["text"], x["n"]) == (c["text"], c["n"]))
        rec = sum(x["recovered"] for x in cs); rs = [x["score"] for x in cs if x["recovered"]]
        low = min(rs) if rs else None
        thr, rule = ((nm + low) / 2, "midpoint") if low is not None and low > nm else (nm, "overlap: noise maximum")
        out[cid] = dict(passed=rec >= run.PASS_K, recovered=rec, noise_max=nm, lowest_recovered=low,
                        threshold=round(thr, 4), rule=rule)
    json.dump(out, open(F_THRESH, "w"), indent=1); print(json.dumps(out, indent=1))


# ---------------------------------------------------------------- target
def target_jobs():
    sh, sr = random.Random("29-target-shuffle"), random.Random("29-target-solver")
    jobs = []
    for c in CELLS:
        for kind in ("telegram", "shuffle"):
            jobs.append(dict(c, cell=cell_id(c), kind=kind, shuffle_seed=sh.randrange(1 << 30) if kind == "shuffle" else None,
                             solver_seed=sr.randrange(1 << 30)))
    return jobs


def target_one(j):
    letters = list(run.telegram(j["text"]))
    if j["kind"] == "shuffle":
        random.Random(j["shuffle_seed"]).shuffle(letters)
    rt = rowcol.rearrange("".join(letters), j["w"], j["direction"])
    t0 = cpu(); s, o = setsolve.solve(rt, j["n"], 0, j["solver_seed"]); dt = cpu() - t0
    return dict(j, score=round(s, 4), cpu_s=round(dt, 2), order=o, reading="".join(setsolve.dec_rows(rt, o, 0))[:80])


# ---------------------------------------------------------------- summary
def summary():
    C, N, K, X = load("controls"), load("noise"), load("calibration"), load("target")
    T = json.load(open(F_THRESH)) if os.path.exists(F_THRESH) else {}
    print("| cell | recovered | median adj | recovered scores | noise max | threshold | verdict |\n|---|---|---|---|---|---|---|")
    for c in CELLS:
        cid = cell_id(c); cs = sorted(x["adj"] for x in C if x["cell"] == cid)
        rs = [x["score"] for x in C if x["cell"] == cid and x["recovered"]]; t = T.get(cid, {})
        print(f"| {cid} | {sum(a >= run.PASS_ADJ for a in cs)}/{len(cs)} | {cs[len(cs) // 2] if cs else '—'} | "
              f"{(f'{min(rs):.3f} to {max(rs):.3f}') if rs else '—'} | {t.get('noise_max', '—')} | {t.get('threshold', '—')} | "
              f"{('pass' if t.get('passed') else 'not testable') if t else '—'} |")
    fails = [x for x in C if not x["recovered"]]
    if fails:
        print("\nFailed plants: cell, adj, score vs own true-key score")
        for x in sorted(fails, key=lambda x: x["cell"]):
            print(f"  {x['cell']} i{x['i']}: adj {x['adj']}, score {x['score']} vs true {x['true_score']}"
                  f" ({'above' if x['score'] > x['true_score'] + 1e-9 else 'at or below'} own key)")
    if K:
        print("\nCalibration plants (P1/M1, real 1937 telegrams; descriptive)\n| cell | source | start | adj | recovered | score | true-key score | threshold | above threshold |\n|---|---|---|---|---|---|---|---|---|")
        for x in sorted(K, key=lambda x: (x["cell"], x["i"])):
            t = T.get(x["cell"], {}).get("threshold")
            print(f"| {x['cell']} | {x['source']} | {x['start']} | {x['adj']} | {x['recovered']} | {x['score']:.3f} | {x['true_score']:.3f} | "
                  f"{t if t is not None else '—'} | {('yes' if x['score'] > t else 'no') if t is not None else '—'} |")
    if X:
        print("\n| cell | kind | score | threshold | margin | reading, first 80 |\n|---|---|---|---|---|---|")
        for x in sorted(X, key=lambda x: (x["cell"], x["kind"])):
            t = T[x["cell"]]["threshold"]
            print(f"| {x['cell']} | {x['kind']} | {x['score']:.3f} | {t:.3f} | {x['score'] - t:+.3f} | {x['reading']} |")
        cand = [x for x in X if x["kind"] == "telegram" and x["score"] > T[x["cell"]]["threshold"]]
        print(f"\nTelegram candidates above threshold: {len(cand)}")
    allr = C + N + K + X
    print(f"\nRecorded solver CPU time: {sum(x.get('cpu_s', 0) for x in allr):.1f} s over {len(allr)} solver runs "
          f"(controls {sum(x['cpu_s'] for x in C):.1f}, noise {sum(x['cpu_s'] for x in N):.1f}, "
          f"calibration {sum(x['cpu_s'] for x in K):.1f}, target {sum(x['cpu_s'] for x in X):.1f})")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "controls":
        run.run_jobs(control_jobs(), control_one, F["controls"], lambda j: (j["cell"], j["i"]))
    elif cmd == "noise":
        run.run_jobs(noise_jobs(), noise_one, F["noise"], lambda j: (j["cell"], j["i"]))
    elif cmd == "calib":
        run.run_jobs(calib_jobs(), calib_one, F["calibration"], lambda j: (j["cell"], j["i"]))
    elif cmd == "thresholds":
        thresholds()
    elif cmd == "target":
        if not os.path.exists(F_THRESH):
            sys.exit("thresholds.json missing: run controls, noise and thresholds first (README plan)")
        T = json.load(open(F_THRESH))
        run.run_jobs([j for j in target_jobs() if T[j["cell"]]["passed"]], target_one, F["target"],
                     lambda j: (j["cell"], j["kind"]))
    elif cmd == "summary":
        summary()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()

"""Step A of 17-truncated-bodies: single columnar, forward, incomplete last row, on truncated bodies.

Solver: 15-tail-robustness/colsolve.py, imported and called unchanged (w <= 8 exhaustive; w >= 9 annealing,
2 restarts x 10,000 w steps). Plants: 01-solver/plaintext.telegram (held-out books, 27738 excluded).

Seeds. Plant seeds, shuffle seeds and solver seeds come from separate named streams. For w >= 9 the script
replays colsolve's first restart key from the solver seed and asserts that it differs from the planted key.
The exhaustive search (w <= 8) takes no seed and visits every key.

Usage (from this folder, in this order):
  python3 -I step_a.py controls [WORKERS]   -> out/a_controls.jsonl   (A2)
  python3 -I step_a.py noise [WORKERS]      -> out/a_noise.jsonl      (A3)
  python3 -I step_a.py thresholds           -> prints A4 (copied into thresholds-AC.md before A5)
  python3 -I step_a.py target [WORKERS]     -> out/a_target.jsonl     (A5; refuses unless thresholds-AC.md
                                               holds the A4 lines; appends only missing jobs)
  python3 -I step_a.py summary > result-A.txt
"""
import hashlib, inspect, json, os, random, statistics, sys, time
from concurrent.futures import ProcessPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(HERE, "..", "01-solver")
TAILDIR = os.path.join(HERE, "..", "15-tail-robustness")
sys.path.insert(0, SOLVER); sys.path.insert(0, TAILDIR); os.chdir(SOLVER)   # as 08-letter-fit/fit.py
import plaintext, transpo  # noqa: E402
from control import shift_acc  # noqa: E402
import common, colsolve  # noqa: E402  (common chdirs to 01-solver too)

OUT = os.path.join(HERE, "out")
THRESH_FILE = os.path.join(HERE, "thresholds-AC.md")
PASS_ACC = 0.90            # A2: letters in place after control.py's cyclic-shift tolerance
PASS_BAND = 0.80           # A2: share of a band's plants that must pass
BANDS = [("w 5-8", 5, 8), ("w 9-30", 9, 30), ("w 31-45", 31, 45)]
CTRL_LENGTHS = (611, 600, 595, 155)
PER_BAND = 10
NOISE_WIDTHS = (5, 8, 12, 20, 30, 45)
NOISE_SHUFFLES = 3
WIDTHS = range(5, 46)
FIRST_KEY_XOR = 0x2545F491  # colsolve.solve: random.Random(seed ^ 0x2545F491); checked against its source

assert 27738 in plaintext.HELDOUT_EXCLUDE, "glossary book must be excluded from plants"
assert f"seed ^ {hex(FIRST_KEY_XOR).upper().replace('X', 'x')}" in inspect.getsource(colsolve.solve)
assert (colsolve.RESTARTS, colsolve.ITERS_PER_W) == (2, 10000), "colsolve's frozen schedule changed"


def load(name, n, sha_head, sha_tail):
    t = "".join(c for c in open(os.path.join(HERE, "../../sources", name)).read().upper() if c.isalpha())
    h = hashlib.sha256(t.encode()).hexdigest()
    assert len(t) == n and h.startswith(sha_head) and h.endswith(sha_tail), (name, len(t), h)
    return t


def telegrams():
    return (load("telegram-1.txt", 615, "e266615d", "434c55"), load("telegram-2.txt", 160, "8fd5cfb8", "e17a644"))


def band_of(w):
    return next(lab for lab, lo, hi in BANDS if lo <= w <= hi)


def first_restart_key(solver_seed, w):
    """colsolve.solve's first annealing start key for this seed (w >= 9)."""
    return random.Random(solver_seed ^ FIRST_KEY_XOR).sample(range(w), w)


# ---------------------------------------------------------------- jobs
def control_jobs():
    plant_rng, solver_rng = random.Random("17-A-plant"), random.Random("17-A-solver-controls")
    jobs = []
    for L in CTRL_LENGTHS:
        for lab, lo, hi in BANDS:
            for _ in range(PER_BAND):
                jobs.append(dict(kind="control", i=len(jobs), L=L, band=lab, w=plant_rng.randint(lo, hi),
                                 plant_seed=plant_rng.randrange(1 << 30), solver_seed=solver_rng.randrange(1 << 30)))
    return jobs


def noise_jobs():
    shuf_rng, solver_rng = random.Random("17-A-shuffle"), random.Random("17-A-solver-noise")
    jobs = []
    for body in ("T1[0:600]", "T2[0:155]"):
        for w in NOISE_WIDTHS:
            for _ in range(NOISE_SHUFFLES):
                jobs.append(dict(kind="noise", i=len(jobs), body=body, w=w, shuffle_seed=shuf_rng.randrange(1 << 30),
                                 solver_seed=solver_rng.randrange(1 << 30)))
    return jobs


# README order: b = 5, 10, 15, 20, then 1-4, then T2. Mapped to the nearest control length.
TARGET_BODIES = [(f"T1[0:{615 - b}]", "T1", 615 - b, 611 if b <= 5 else 600 if b <= 15 else 595)
                 for b in (5, 10, 15, 20, 1, 2, 3, 4)] + [("T2[0:155]", "T2", 155, 155)]


def target_jobs():
    solver_rng = random.Random("17-A-solver-target")
    jobs = []
    for body, tel, n, ctrl_L in TARGET_BODIES:
        for w in WIDTHS:
            jobs.append(dict(kind="target", i=len(jobs), body=body, n=n, ctrl_L=ctrl_L, w=w,
                             solver_seed=solver_rng.randrange(1 << 30)))
    return jobs


# ---------------------------------------------------------------- work
def run_control(job):
    t0 = time.time(); w = job["w"]
    assert job["plant_seed"] != job["solver_seed"]
    rnd = random.Random(job["plant_seed"])
    pt = plaintext.telegram(job["L"], rnd); k = rnd.sample(range(w), w)
    ct = transpo.col_enc(pt, k)
    assert len(ct) == job["L"] and colsolve.decrypt(ct, k) == pt
    if w >= 9:
        assert first_restart_key(job["solver_seed"], w) != k, "solver would start at the planted key"
    s, kk = colsolve.solve(ct, w, job["solver_seed"])
    dec = colsolve.decrypt(ct, kk); acc = shift_acc(dec, pt)
    return dict(job, score=round(s, 4), true_score=round(common.qscore([ord(c) - 65 for c in pt]), 4),
                acc=round(acc, 4), ok=acc >= PASS_ACC, key_exact=(list(kk) == k), secs=round(time.time() - t0, 1))


def run_noise(job):
    t0 = time.time(); w = job["w"]
    t1, t2 = telegrams()
    body = list(t1[:600] if job["body"] == "T1[0:600]" else t2[:155])
    random.Random(job["shuffle_seed"]).shuffle(body)
    s, kk = colsolve.solve("".join(body), w, job["solver_seed"])
    return dict(job, score=round(s, 4), key=list(kk), secs=round(time.time() - t0, 1))


def run_target(job):
    t0 = time.time(); w = job["w"]; thr = job["threshold"]
    t1, t2 = telegrams()
    ct = (t1 if job["body"].startswith("T1") else t2)[:job["n"]]
    assert len(ct) == job["n"]
    s, kk = colsolve.solve(ct, w, job["solver_seed"])
    dec = colsolve.decrypt(ct, kk)
    rec = dict(job, score=round(s, 4), key=list(kk), candidate=s > thr, secs=round(time.time() - t0, 1))
    if rec["candidate"]:
        rec["dec200"] = dec[:200]       # recorded for the main thread; not read further here
    return rec


# ---------------------------------------------------------------- thresholds
def read(name):
    p = os.path.join(OUT, name)
    return [json.loads(x) for x in open(p)] if os.path.exists(p) else []


def thresholds(ctrl, noise):
    res = {}
    for L in CTRL_LENGTHS:
        rows = [r for r in ctrl if r["L"] == L]
        bands = {}
        for lab, lo, hi in BANDS:
            rs = [r for r in rows if r["band"] == lab]
            k = sum(r["ok"] for r in rs)
            bands[lab] = dict(k=k, n=len(rs), passed=len(rs) == PER_BAND and k >= PASS_BAND * len(rs))
        passing = [r for r in rows if bands[r["band"]]["passed"] and r["ok"]]
        tel = "T2" if L == 155 else "T1"
        nz = [r for r in noise if r["body"].startswith(tel)]
        ceil = max(r["score"] for r in nz)
        low = min(r["true_score"] for r in passing) if passing else None
        thr = round((ceil + low) / 2, 4) if low is not None else None
        res[L] = dict(bands=bands, noise_ceiling=ceil, low_true=low, threshold=thr, tel=tel)
    return res


def threshold_lines(th):
    return [f"THRESHOLD-A L={L}: {th[L]['threshold']:.4f}" for L in CTRL_LENGTHS]


def print_thresholds():
    ctrl, noise = read("a_controls.jsonl"), read("a_noise.jsonl")
    assert len(ctrl) == len(control_jobs()) and len(noise) == len(noise_jobs()), "controls or noise incomplete"
    th = thresholds(ctrl, noise)
    for L in CTRL_LENGTHS:
        d = th[L]
        bands = "; ".join(f"{b} {v['k']}/{v['n']} {'pass' if v['passed'] else 'FAIL (not testable)'}"
                          for b, v in d["bands"].items())
        print(f"L = {L} ({d['tel']} bodies): {bands}")
        print(f"  noise ceiling ({d['tel']} shuffles, all widths): {d['noise_ceiling']:.4f}; "
              f"lowest true-text score among passing controls: {d['low_true']}")
    for line in threshold_lines(th):
        print(line)


# ---------------------------------------------------------------- driver
def pool_run(fn, jobs, path, workers, extra=()):
    done_ids = set()
    if os.path.exists(path):
        have = {r["i"]: r for r in map(json.loads, open(path))}
        for j in jobs:
            if j["i"] in have:
                assert all(have[j["i"]][x] == j[x] for x in j), j
        done_ids = set(have)
    todo = [j for j in jobs if j["i"] not in done_ids]
    print(f"{len(done_ids)} done, {len(todo)} to run", flush=True)
    t0 = time.time(); n = 0
    with open(path, "a") as f, ProcessPoolExecutor(workers) as ex:
        futs = [ex.submit(fn, j, *extra) for j in todo]
        for fu in as_completed(futs):
            r = fu.result(); f.write(json.dumps(r) + "\n"); f.flush(); n += 1
            tag = r.get("body", r.get("L"))
            msg = f"[{n}/{len(todo)} {time.time() - t0:.0f}s] {r['kind']} {tag} w={r['w']} score={r['score']:.4f}"
            if r["kind"] == "control":
                msg += f" true={r['true_score']:.4f} acc={r['acc']:.3f}"
            if r.get("candidate"):
                msg += "  *** ABOVE THRESHOLD ***"
            print(msg, flush=True)


def main():
    mode = sys.argv[1]; workers = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    assert workers <= 3
    os.makedirs(OUT, exist_ok=True)
    if mode == "controls":
        pool_run(run_control, control_jobs(), os.path.join(OUT, "a_controls.jsonl"), workers)
    elif mode == "noise":
        pool_run(run_noise, noise_jobs(), os.path.join(OUT, "a_noise.jsonl"), workers)
    elif mode == "thresholds":
        print_thresholds()
    elif mode == "target":
        ctrl, noise = read("a_controls.jsonl"), read("a_noise.jsonl")
        assert len(ctrl) == len(control_jobs()) and len(noise) == len(noise_jobs())
        th = thresholds(ctrl, noise)
        written = open(THRESH_FILE).read()
        for line in threshold_lines(th):
            assert line in written, f"threshold not written into thresholds-AC.md: {line}"
        jobs = [dict(j, threshold=th[j["ctrl_L"]]["threshold"]) for j in target_jobs()
                if th[j["ctrl_L"]]["bands"][band_of(j["w"])]["passed"]]
        # Submit body by body in README order, widest first within a body (balances the pool).
        order = {b[0]: n for n, b in enumerate(TARGET_BODIES)}
        jobs.sort(key=lambda j: (order[j["body"]], -j["w"]))
        pool_run(run_target, jobs, os.path.join(OUT, "a_target.jsonl"), workers)
    elif mode == "summary":
        summary()


# ---------------------------------------------------------------- summary
def summary():
    ctrl, noise, tgt = read("a_controls.jsonl"), read("a_noise.jsonl"), read("a_target.jsonl")
    th = thresholds(ctrl, noise)
    print("17-truncated-bodies, step A: single columnar (15-tail-robustness/colsolve.py, unchanged)")
    print(f"Pass: >= {PASS_ACC:.0%} of letters in place (control.py shift_acc); band passes at >= {PASS_BAND:.0%}.\n")
    print("A2. Controls (10 plants per band per length; solver seeded apart from the plant)")
    print("length  band      recovered  median acc  true-text min..max   failures (found score vs true score)")
    for L in CTRL_LENGTHS:
        for lab, lo, hi in BANDS:
            rs = sorted((r for r in ctrl if r["L"] == L and r["band"] == lab), key=lambda r: r["i"])
            k = sum(r["ok"] for r in rs)
            fails = ", ".join(f"w{r['w']} {r['score']:.3f} vs {r['true_score']:.3f} (acc {r['acc']:.2f})"
                              for r in rs if not r["ok"])
            ts = [r["true_score"] for r in rs]
            print(f"{L:6}  {lab:8}  {k:2}/{len(rs):<2} {'pass' if th[L]['bands'][lab]['passed'] else 'FAIL'}"
                  f"   {statistics.median(r['acc'] for r in rs):.3f}      {min(ts):.4f}..{max(ts):.4f}   {fails or '-'}")
    exact = sum(r["key_exact"] for r in ctrl)
    print(f"Exact keys: {exact}/{len(ctrl)}. Mean seconds per control: {statistics.mean(r['secs'] for r in ctrl):.1f}\n")
    print("A3. Noise ceiling (best score on shuffles of the body)")
    for body in ("T1[0:600]", "T2[0:155]"):
        for w in NOISE_WIDTHS:
            sc = [r["score"] for r in sorted(noise, key=lambda r: r["i"]) if r["body"] == body and r["w"] == w]
            print(f"  {body} w={w:2}: " + "  ".join(f"{x:.4f}" for x in sc))
        print(f"  {body} max: {max(r['score'] for r in noise if r['body'] == body):.4f}")
    print("\nA4. Thresholds (halfway between noise ceiling and lowest true-text score among passing controls)")
    for L in CTRL_LENGTHS:
        d = th[L]
        print(f"  L={L}: noise ceiling {d['noise_ceiling']:.4f}, lowest passing true text {d['low_true']}, "
              f"threshold {d['threshold']}")
    print("\nA5. Target: best score per (body, w); * = above threshold; - = band not testable or not run")
    bodies = [b for b, *_ in TARGET_BODIES]
    by = {(r["body"], r["w"]): r for r in tgt}
    print("  w  " + "".join(f"{b:>12}" for b in bodies))
    for w in WIDTHS:
        cells = []
        for b in bodies:
            r = by.get((b, w))
            cells.append(f"{r['score']:.4f}{'*' if r['candidate'] else ' '}" if r else "-")
        print(f"{w:3}  " + "".join(f"{c:>12}" for c in cells))
    print("\nPer body: threshold, best score over widths (width), runs done")
    for body, tel, n, cL in TARGET_BODIES:
        rs = [r for r in tgt if r["body"] == body]
        if rs:
            b = max(rs, key=lambda r: r["score"])
            print(f"  {body}: threshold {th[cL]['threshold']:.4f} (L={cL}); best {b['score']:.4f} at w={b['w']}; "
                  f"margin {b['score'] - th[cL]['threshold']:+.4f}; {len(rs)} widths run")
        else:
            print(f"  {body}: not run")
    cands = [r for r in tgt if r["candidate"]]
    print(f"\nCandidates (score above threshold): {len(cands)}")
    for r in cands:
        print(f"  {r['body']} w={r['w']} score={r['score']:.4f} key={r['key']}\n  first 200: {r['dec200']}")
    print("\nKeys (rank list: key[c] = reading rank of plaintext column c), per (body, w):")
    for body in bodies:
        for w in WIDTHS:
            r = by.get((body, w))
            if r:
                print(f"  {body} w={w} {r['score']:.4f} {','.join(map(str, r['key']))}")


if __name__ == "__main__":
    main()

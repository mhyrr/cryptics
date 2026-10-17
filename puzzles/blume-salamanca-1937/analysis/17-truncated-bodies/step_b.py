"""Step B of 17-truncated-bodies: double columnar CC on T1 bodies with the tail cut off.

The plan is README.md, Step B (pre-registered). The solver is 01-solver/out/dtsolve, unchanged, driven as
03-target-h1/target.py and 15-tail-robustness/run.py drive it. Imports 01-solver the way 08-letter-fit/fit.py
does: its folder goes on sys.path and becomes the working directory.

Usage (from this folder):
  python3 -I step_b.py controls SECS [CELL ...]
      B3 planted controls. CELL is "L/band", e.g. "611/w2 2-11"; with no CELL, all four cells.
      -> controls-B.jsonl (appended, one line per plant and budget) and out/controls-B-<SECS>.jsonl.
  python3 -I step_b.py target SECS_LOW SECS_HIGH THRESHOLD BODIES [--deadline-min M]
      B5 target. SECS_LOW is the budget for w2 2-11, SECS_HIGH for w2 12-15 ("skip" = band not run).
      BODIES is a comma list of b, run in that order, e.g. 5,10,15,20. A body starts only if it can finish
      inside the deadline. Resumes: runs already in result-B.jsonl are skipped (their seeds are checked).
      -> result-B.jsonl (one line per run), out/target-B.jsonl (with full decryptions).
  python3 -I step_b.py summary THRESHOLD
      -> summary-B.txt
  python3 -I step_b.py ctable
      -> the controls table (markdown) on stdout, from controls-B.jsonl

Seeds. Three independent streams, each a random.Random keyed by a string (Python hashes a str seed with
SHA-512, so the streams do not depend on PYTHONHASHSEED):
  "17-B-plant"            plant parameters (w1, w2) and the plant seed (plaintext and keys);
  "17-B-control-solver"   the solver seed of each control;
  "17-B-target-solver"    the solver seed of each target run, drawn in the fixed order b = 5, 10, 15, 20,
                          1, 2, 3, 4 x w1 2-15 x w2 2-15, so a seed does not depend on which bodies were run.
No solver seed is drawn from the stream that made its plant (experiment 15's finding on 05).
"""
import json, os, random, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED

HERE = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(HERE, "..", "01-solver")
sys.path.insert(0, SOLVER); os.chdir(SOLVER)
import plaintext, transpo  # noqa: E402
from control import shift_acc, quad_per_letter  # noqa: E402  (cyclic shift up to 40; per-letter quadgrams)

OUT = os.path.join(HERE, "out")
WORKERS = 5
CONV, LANG = "CC", "es"
PASS_ACC = 0.90
LENGTHS = (611, 595)
BANDS = (("w2 2-11", 2, 11), ("w2 12-15", 12, 15))
W1_PLANT = (8, 15)
PER_CELL = 10
BODY_ORDER = (5, 10, 15, 20, 1, 2, 3, 4)
WIDTHS = range(2, 16)


def t1():
    t = "".join(c for c in open(os.path.join(HERE, "../../sources/telegram-1.txt")).read().upper() if c.isalpha())
    assert len(t) == 615
    return t


def band_of(w2):
    return "w2 2-11" if w2 <= 11 else "w2 12-15"


def dtsolve(ct_path, w1, w2, seed, secs, pt_path="-"):
    out = subprocess.run(["out/dtsolve", "solve", ct_path, str(w1), str(w2), CONV, LANG, str(seed), str(secs), pt_path],
                         capture_output=True, text=True).stdout.strip().splitlines()
    return [json.loads(l) for l in out]


# ---------------------------------------------------------------- B3 controls
def control_jobs():
    pr, sr = random.Random("17-B-plant"), random.Random("17-B-control-solver")
    jobs = []
    for L in LENGTHS:
        for label, lo, hi in BANDS:
            for _ in range(PER_CELL):
                w1, w2 = pr.randint(*W1_PLANT), pr.randint(lo, hi)
                jobs.append(dict(i=len(jobs), L=L, band=label, w1=w1, w2=w2,
                                 plant_seed=pr.randrange(1 << 30), solver_seed=sr.randrange(1 << 30)))
    assert all(j["plant_seed"] != j["solver_seed"] for j in jobs)
    return jobs


def control_one(job, secs):
    rnd = random.Random(job["plant_seed"])
    pt = plaintext.telegram(job["L"], rnd, LANG)
    k1, k2 = rnd.sample(range(job["w1"]), job["w1"]), rnd.sample(range(job["w2"]), job["w2"])
    assert len(pt) == job["L"]
    d = os.path.join(OUT, f"controls-{secs}"); os.makedirs(d, exist_ok=True)
    cp, pp = os.path.join(d, f"{job['i']}_ct.txt"), os.path.join(d, f"{job['i']}_pt.txt")
    open(cp, "w").write(transpo.double_enc(pt, k1, k2, CONV)); open(pp, "w").write(pt)
    t0 = time.time()
    lines = dtsolve(cp, job["w1"], job["w2"], job["solver_seed"], secs, pp)
    fin = lines[-1]
    acc = shift_acc(fin["pt"], pt)
    first_ok = next((l["t"] for l in lines if shift_acc(l["pt"], pt) >= PASS_ACC), None)
    return dict(job, secs=secs, k1=",".join(map(str, k1)), k2=",".join(map(str, k2)),
                acc=round(acc, 4), ok=acc >= PASS_ACC, score=fin["score"], true_score=round(quad_per_letter(pt, LANG), 4),
                idp=fin["idp"], iters=fin["iter"], t_first_ok=first_ok, wall=round(time.time() - t0, 1),
                dec60=fin["pt"][:60], ref60=pt[:60])


def controls(secs, cells):
    jobs = control_jobs()
    if cells:
        want = {tuple(c.split("/", 1)) for c in cells}
        jobs = [j for j in jobs if (str(j["L"]), j["band"]) in want]
        assert jobs, cells
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time(); done = 0
    with open(os.path.join(HERE, "controls-B.jsonl"), "a") as f, \
            open(os.path.join(OUT, f"controls-B-{secs}.jsonl"), "a") as g, ThreadPoolExecutor(WORKERS) as ex:
        for r in ex.map(lambda j: control_one(j, secs), jobs):
            line = json.dumps(r); f.write(line + "\n"); g.write(line + "\n"); f.flush(); g.flush(); done += 1
            print(f"[{done}/{len(jobs)} {time.time() - t0:.0f}s] L={r['L']} {r['band']} {r['w1']}x{r['w2']} "
                  f"acc={r['acc']:.3f} ok={r['ok']} score={r['score']:.3f} true={r['true_score']:.3f} "
                  f"first_ok={r['t_first_ok']} iters={r['iters']}", flush=True)


# ---------------------------------------------------------------- B5 target
def target_jobs():
    sr = random.Random("17-B-target-solver")
    return [dict(b=b, w1=w1, w2=w2, seed=sr.randrange(1 << 30)) for b in BODY_ORDER for w1 in WIDTHS for w2 in WIDTHS]


def target_one(job, secs, text):
    n = 615 - job["b"]
    p = os.path.join(OUT, "bodies", f"T1_0_{n}.txt")
    t0 = time.time()
    fin = dtsolve(p, job["w1"], job["w2"], job["seed"], secs)[-1]
    assert len(fin["pt"]) == n and sorted(fin["pt"]) == sorted(text[:n])
    return dict(body=f"T1[0:{n}]", b=job["b"], n=n, w1=job["w1"], w2=job["w2"], band=band_of(job["w2"]),
                seconds=secs, seed=job["seed"], score=fin["score"], idp=fin["idp"], iters=fin["iter"],
                k1=fin["k1"], k2=fin["k2"], wall=round(time.time() - t0, 1)), fin["pt"]


def target(secs_low, secs_high, threshold, bodies, deadline_min):
    text = t1()
    budget = {"w2 2-11": secs_low, "w2 12-15": secs_high}
    os.makedirs(os.path.join(OUT, "bodies"), exist_ok=True)
    for b in bodies:
        open(os.path.join(OUT, "bodies", f"T1_0_{615 - b}.txt"), "w").write(text[:615 - b])
    rp = os.path.join(HERE, "result-B.jsonl")
    have = {}
    if os.path.exists(rp):
        for r in map(json.loads, open(rp)):
            have[(r["b"], r["w1"], r["w2"])] = r
    alljobs = target_jobs()
    for j in alljobs:
        h = have.get((j["b"], j["w1"], j["w2"]))
        assert h is None or h["seed"] == j["seed"], (j, h)
    queue = []
    for b in bodies:
        js = [j for j in alljobs if j["b"] == b and budget[band_of(j["w2"])] != "skip"
              and (j["b"], j["w1"], j["w2"]) not in have]
        js.sort(key=lambda j: -int(budget[band_of(j["w2"])]))  # long runs first inside a body
        queue.append((b, js))
    t_start = time.time(); deadline = t_start + deadline_min * 60 if deadline_min else None
    done = 0; left_out = []
    with open(rp, "a") as f, open(os.path.join(OUT, "target-B.jsonl"), "a") as g, ThreadPoolExecutor(WORKERS) as ex:
        running = set()

        def drain(block_until_below):
            nonlocal done, running
            while len(running) >= block_until_below:
                fin, running = wait(running, return_when=FIRST_COMPLETED)
                for fu in fin:
                    r, pt = fu.result()
                    f.write(json.dumps(r) + "\n"); f.flush()
                    g.write(json.dumps(dict(r, pt=pt)) + "\n"); g.flush(); done += 1
                    flag = "  CANDIDATE" if r["score"] > threshold else ""
                    print(f"[{done} {time.time() - t_start:.0f}s] {r['body']} {r['w1']}x{r['w2']} {r['seconds']}s "
                          f"score={r['score']:.4f} iters={r['iters']} {pt[:40]}{flag}", flush=True)
                    if flag:
                        with open(os.path.join(OUT, "candidates-B.jsonl"), "a") as c:
                            c.write(json.dumps(dict(r, pt=pt)) + "\n")

        for b, js in queue:
            est = sum(int(budget[band_of(j["w2"])]) + 0.5 for j in js) / WORKERS
            if deadline and time.time() + est > deadline:
                left_out.append(b); continue
            print(f"--- body b={b} (T1[0:{615 - b}]): {len(js)} runs, est {est / 60:.1f} min", flush=True)
            for j in js:
                drain(WORKERS)
                running.add(ex.submit(target_one, j, int(budget[band_of(j["w2"])]), text))
        drain(1)
    print(f"done {done} runs in {time.time() - t_start:.0f}s; bodies left out: {left_out or 'none'}", flush=True)


# ---------------------------------------------------------------- tables
def control_table():
    """Per (budget, L, band): plants recovered, solver and true-text score ranges."""
    rs = [json.loads(l) for l in open(os.path.join(HERE, "controls-B.jsonl"))]
    out = ["| budget | length | band | recovered | verdict | acc range | solver score (recovered) | true-text score (all) |",
           "|---|---|---|---|---|---|---|---|"]
    for secs in sorted({r["secs"] for r in rs}):
        for L in LENGTHS:
            for label, _, _ in BANDS:
                x = [r for r in rs if r["secs"] == secs and r["L"] == L and r["band"] == label]
                if not x:
                    continue
                ok = [r for r in x if r["ok"]]
                k = len(ok); v = "pass" if k >= 0.8 * len(x) else "fail"
                rng = lambda v: f"{min(v):.4f} to {max(v):.4f}" if v else "none"
                out.append(f"| {secs} s | {L} | {label} | {k}/{len(x)} | {v} | {min(r['acc'] for r in x):.3f}–"
                           f"{max(r['acc'] for r in x):.3f} | {rng([r['score'] for r in ok])} | "
                           f"{rng([r['true_score'] for r in x])} |")
    fails = [r for r in rs if not r["ok"]]
    out += ["", "Failed plants:" if fails else "Failed plants: none"]
    for r in fails:
        out.append(f"- {r['secs']} s, L {r['L']}, {r['w1']} x {r['w2']}: acc {r['acc']:.3f}, solver {r['score']:.4f}, "
                   f"true {r['true_score']:.4f}")
    print("\n".join(out))


# ---------------------------------------------------------------- summary
def summary(threshold):
    rs = [json.loads(l) for l in open(os.path.join(HERE, "result-B.jsonl"))]
    lines = [f"Step B target summary: {len(rs)} runs, threshold {threshold} (per-letter Spanish quadgram score)", ""]
    lines.append("best score per body")
    lines.append(f"{'body':12} {'b':>3} {'runs':>5} {'best':>8} {'w1xw2':>7} {'median':>8} {'worst':>8} {'>thr':>5}")
    for b in BODY_ORDER:
        x = sorted((r for r in rs if r["b"] == b), key=lambda r: -r["score"])
        if not x:
            lines.append(f"{'T1[0:' + str(615 - b) + ']':12} {b:>3} {0:>5}   not run"); continue
        sc = [r["score"] for r in x]
        lines.append(f"{x[0]['body']:12} {b:>3} {len(x):>5} {sc[0]:>8.4f} {str(x[0]['w1']) + 'x' + str(x[0]['w2']):>7} "
                     f"{sc[len(sc) // 2]:>8.4f} {sc[-1]:>8.4f} {sum(s > threshold for s in sc):>5}")
    lines += ["", "best score per body and w2 band"]
    for b in BODY_ORDER:
        for label, _, _ in BANDS:
            x = [r for r in rs if r["b"] == b and r["band"] == label]
            if x:
                m = max(x, key=lambda r: r["score"])
                lines.append(f"  b={b:>2} {label:9} runs {len(x):>3}  best {m['score']:.4f} ({m['w1']}x{m['w2']})")
    lines += ["", "top 10 runs overall"]
    for r in sorted(rs, key=lambda r: -r["score"])[:10]:
        lines.append(f"  {r['score']:.4f}  {r['body']} {r['w1']}x{r['w2']} {r['seconds']}s seed {r['seed']} "
                     f"k1 {r['k1']} k2 {r['k2']}")
    open(os.path.join(HERE, "summary-B.txt"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


def main():
    cmd = sys.argv[1]
    if cmd == "controls":
        controls(int(sys.argv[2]), sys.argv[3:])
    elif cmd == "target":
        a = sys.argv[2:]
        dl = float(a[a.index("--deadline-min") + 1]) if "--deadline-min" in a else None
        target(a[0], a[1], float(a[2]), [int(x) for x in a[3].split(",")], dl)
    elif cmd == "summary":
        summary(float(sys.argv[2]))
    elif cmd == "ctable":
        control_table()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()

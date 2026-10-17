"""Planted tail-robustness runs. Plants only: no solver here ever sees a real telegram.

A plant is Spanish telegraph plaintext (01-solver/plaintext.telegram) of L - t letters, enciphered, with t
untransposed letters added at the end or the start, so the total is L. The fill is uniform random letters or
letters drawn from T1's last 20 (common.fill), alternating by plant within a cell. t = 0 is the baseline.
Each solver runs on the full L letters, told the true width, as its exclusion ran.

Usage (from this folder): python3 -I run.py FAMILY [WORKERS] [--resume]
  FAMILY: single | double | periodic | nihilist | grille        -> out/<family>.jsonl
  --resume appends only the jobs missing from out/<family>.jsonl, after checking that the jobs already there
  have the same seeds. (Used once: single's w 31-45 band first ran at t = 0 only; its control passed, so its
  tail cells were added. That band is last in the job stream, so no earlier seed moved.)
"""
import json, os, random, subprocess, sys, time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "05-periodic"))
sys.path.insert(0, os.path.join(HERE, "..", "06-grille"))
import common  # noqa: E402  (chdir to 01-solver)
import colsolve, periodic, grille  # noqa: E402
import plaintext, transpo  # noqa: E402

OUT = os.path.join(HERE, "out")
DT_SECS = 90

# family -> (L, bands, (t at end), (t at start)); a band is (label, lo, hi, plants per cell, t0_only)
FAMILIES = {
    "single": (615, [("w 5-8", 5, 8, 20, False), ("w 9-30", 9, 30, 10, False), ("w 31-45", 31, 45, 10, False)],
               (5, 10, 15, 20), (5, 10, 15)),
    "double": (615, [("10x13", 10, 13, 5, False), ("14x14", 14, 14, 5, False)], (5, 10, 15, 20), (5, 10, 15)),
    "periodic": (615, [(f"n {n}", n, n, 20, False) for n in (5, 10, 20, 35)], (5, 10, 15, 20), (5, 10, 15)),
    "nihilist": (615, [(f"n {n}", n, n, 20, False) for n in (8, 15, 25)], (5, 10, 15, 20), (5, 10, 15)),
    "grille": (160, [("4x4", 4, 4, 20, False)], (5, 10), (5, 10)),
}


def jobs_for(fam):
    L, bands, te, ts = FAMILIES[fam]
    master = random.Random(f"15-tail-{fam}")
    jobs = []
    for label, lo, hi, per, t0_only in bands:
        conds = [(0, "none")] if t0_only else common.conditions(te, ts)
        for t, end in conds:
            for i in range(per):
                fillk = "none" if t == 0 else ("uniform" if i % 2 == 0 else "t1tail")
                if fam == "double":
                    param = (lo, hi)
                else:
                    param = master.randint(lo, hi)
                jobs.append(dict(fam=fam, band=label, param=param, L=L, t=t, end=end, fill=fillk, i=len(jobs),
                                 plant_seed=master.randrange(1 << 30), solver_seed=master.randrange(1 << 30)))
    return jobs


def plant(job):
    """Returns (ciphertext of length L, body reference text, true key)."""
    fam, L, t, end = job["fam"], job["L"], job["t"], job["end"]
    rnd = random.Random(job["plant_seed"])
    body = plaintext.telegram(L - t, rnd)
    if fam == "single":
        w = job["param"]; k = rnd.sample(range(w), w); bct, ref = transpo.col_enc(body, k), body
    elif fam == "double":
        w1, w2 = job["param"]; k = (rnd.sample(range(w1), w1), rnd.sample(range(w2), w2))
        bct, ref = transpo.double_enc(body, k[0], k[1], "CC"), body
    elif fam == "periodic":
        n = job["param"]; k = rnd.sample(range(n), n); bct, ref = periodic.enc(body, k), body
    elif fam == "nihilist":
        # 05's nihilist_control plant: full rows reordered, then each row permuted by one column key.
        # The solver does not restore row order, so the reference is the row-reordered text.
        n = job["param"]; k = rnd.sample(range(n), n); f = len(body) // n * n
        rows = [body[i:i + n] for i in range(0, f, n)]; rnd.shuffle(rows)
        ref = "".join(rows) + body[f:]; bct = periodic.enc(ref, k)
    elif fam == "grille":
        # Full 16-letter blocks through the grille; a partial last block stays in clear (as periodic.enc does).
        _, o, bc = rnd.choice(grille.ALL); k = (o, bc)
        bct, ref = grille.enc(body, o, bc) + body[len(body) // 16 * 16:], body
    extra = common.fill(t, rnd, job["fill"]) if t else ""
    ct = common.assemble(bct, extra, end)
    assert len(ct) == L
    return ct, ref, k


def solve(job, ct):
    fam, seed = job["fam"], job["solver_seed"]
    if fam == "single":
        s, kk = colsolve.solve(ct, job["param"], seed); return s, kk, colsolve.decrypt(ct, kk)
    if fam in ("periodic", "nihilist"):
        s, kk = periodic.solve([ct], job["param"], seed); return s, kk, periodic.dec(ct, kk)
    if fam == "grille":
        s, name, o, bc = grille.best(ct, 1)[0]; return s, (o, bc), grille.dec(ct, o, bc)
    if fam == "double":
        d = os.path.join(OUT, "double"); os.makedirs(d, exist_ok=True)
        p = os.path.join(d, f"{job['i']}_ct.txt"); open(p, "w").write(ct)
        w1, w2 = job["param"]
        out = subprocess.run(["out/dtsolve", "solve", p, str(w1), str(w2), "CC", "es", str(seed), str(DT_SECS)],
                             capture_output=True, text=True).stdout.strip().splitlines()
        fin = json.loads(out[-1])
        kk = ([int(x) for x in fin["k1"].split(",")], [int(x) for x in fin["k2"].split(",")])
        return fin["score"], kk, fin["pt"]


def one(job):
    t0 = time.time()
    ct, ref, k = plant(job)
    s, kk, dec = solve(job, ct)
    acc = common.body_acc(dec, ref, job["t"], job["end"])
    o = 0 if job["end"] != "start" else job["t"]
    rec = dict(job, param=job["param"], acc=round(acc, 4), ok=acc >= common.PASS, key_exact=(kk == k),
               score=round(s, 4), true_score=round(common.qscore([ord(c) - 65 for c in ref]), 4),
               secs=round(time.time() - t0, 1), dec60=dec[o:o + 60], ref60=ref[:60])
    return rec


def main():
    fam = sys.argv[1]; workers = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    jobs = jobs_for(fam)
    os.makedirs(OUT, exist_ok=True)
    path, mode = os.path.join(OUT, f"{fam}.jsonl"), "w"
    if "--resume" in sys.argv:
        have = {r["i"]: r for r in map(json.loads, open(path))}
        for j in jobs:
            if j["i"] in have:
                h = have[j["i"]]
                assert all(h[x] == j[x] for x in ("band", "t", "end", "fill", "plant_seed", "solver_seed")), j
                assert h["param"] == j["param"] or list(h["param"]) == list(j["param"]), j
        jobs = [j for j in jobs if j["i"] not in have]; mode = "a"
        print(f"resume: {len(have)} done, {len(jobs)} to run", flush=True)
    pool = ThreadPoolExecutor if fam == "double" else ProcessPoolExecutor
    t0 = time.time(); done = 0
    with open(path, mode) as f, pool(workers) as ex:
        futs = [ex.submit(one, j) for j in jobs]
        for fu in as_completed(futs):
            r = fu.result(); f.write(json.dumps(r) + "\n"); f.flush(); done += 1
            print(f"[{done}/{len(jobs)} {time.time() - t0:.0f}s] {r['band']} t={r['t']} {r['end']} {r['fill']} "
                  f"param={r['param']} acc={r['acc']:.3f} score={r['score']:.3f} true={r['true_score']:.3f}",
                  flush=True)


if __name__ == "__main__":
    main()

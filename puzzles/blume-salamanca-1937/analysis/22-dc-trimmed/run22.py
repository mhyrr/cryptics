"""22-dc-trimmed: forward double columnar CC, w1 2-15 x w2 16-17, on trimmed T1 bodies, with 21's method.

Pre-registration in README.md. Same binary as 21's controls and target (21-dc-method/out/dcm, SHA-256 checked
against 21-dc-method/dcm_ctlA.sha256), same arguments, 50 M IDP evaluations per run, the whole budget spent.
Plants, seed streams and 01's accuracy rule come from 21-dc-method/run21.py (imported, not modified).

Usage (from this folder):
  python3 -I run22.py controls [WORKERS]   -> results/controls22.jsonl (resumes); logs in out/ctl22_N/
  python3 -I run22.py target [WORKERS]     -> results/target22.jsonl (resumes; only bodies whose length passed)
  python3 -I run22.py summary              -> results/summary.md (also printed)
"""
import sys
sys.dont_write_bytecode = True  # importing run21 must not write into 21-dc-method/ or 01-solver/
import hashlib, json, os, subprocess  # noqa: E402
from concurrent.futures import ThreadPoolExecutor, as_completed  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
D21 = os.path.normpath(os.path.join(HERE, "..", "21-dc-method"))
sys.path.insert(0, D21)
import run21  # noqa: E402  (plant, stream, load_words, shift_acc; read only)

DCM = os.path.join(D21, "out", "dcm")
T1SRC = os.path.normpath(os.path.join(HERE, "..", "..", "sources", "telegram-1.txt"))
RES = os.path.join(HERE, "results")
OUTD = os.path.join(HERE, "out")
CTL = os.path.join(RES, "controls22.jsonl")
TGT = os.path.join(RES, "target22.jsonl")
ARGS = ["budget=50000000", "climb=1", "idp=1", "k1climb=0"]
BODIES = {"T1[0:595]": (0, 595), "T1[5:615]": (5, 615), "T1[10:615]": (10, 615)}
LENGTHS = {b - a: name for name, (a, b) in BODIES.items()}          # 595, 610, 605
SPECS = ["2-15x16-17"] * 6 + ["12-15x17"] * 4                     # trials 0-5 whole band, 6-9 hard corner
PAIRS = [(w1, w2) for w2 in (16, 17) for w1 in range(2, 16)]
BASE_THR, NOISE = -5.10, -5.19
TRIALS, PASS_AT = 10, 8


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def check_binary():
    want = open(os.path.join(D21, "dcm_ctlA.sha256")).read().split()[0]
    got = sha(DCM)
    assert got == want, f"21-dc-method/out/dcm is not the binary 21's controls used ({got} != {want})"
    return got


def t1():
    src = "".join(c for c in open(T1SRC).read().upper() if c.isalpha())
    assert len(src) == 615 and hashlib.sha256(src.encode()).hexdigest().startswith("e266615d"), "telegram 1 changed"
    return src


def cost_table():
    """21's measured CPU s per (w1, w2) at 615 letters, used only to order jobs longest first."""
    return {(r["w1"], r["w2"]): r["cpu"] for r in map(json.loads, open(os.path.join(D21, "results", "target21.jsonl")))}


def dcm_run(args):
    out = subprocess.run([DCM] + args, capture_output=True, text=True, cwd=D21)  # dcm reads out/lm_es_*.bin there
    return out, [l for l in out.stdout.strip().splitlines() if l.startswith("{")]


def load(path):
    return [json.loads(l) for l in open(path)] if os.path.exists(path) else []


# ---------------- controls ----------------
def ctl_tag(n):
    return f"ctl22_{n}"


def ctl_job(job):
    n, i, spec, pt, k1, k2, ct = job
    tag = ctl_tag(n)
    seed = run21.stream("solver", tag, i)
    assert seed != run21.stream("plant", tag, i)
    d = os.path.join(OUTD, tag)
    os.makedirs(d, exist_ok=True)
    cf, pf = os.path.join(d, f"{i}_ct.txt"), os.path.join(d, f"{i}_pt.txt")
    open(cf, "w").write(ct)
    open(pf, "w").write(pt)
    w1, w2 = len(k1), len(k2)
    args = ["solve", cf, f"w1={w1}", f"w2={w2}", "lang=es", f"seed={seed}", "truek2=" + ",".join(map(str, k2)),
            "truek1=" + ",".join(map(str, k1)), f"pt={pf}"] + ARGS
    out, lines = dcm_run(args)
    open(os.path.join(d, f"{i}.log"), "w").write(out.stdout + out.stderr)
    rec = {"n": n, "body": LENGTHS[n], "trial": i, "tag": tag, "spec": spec, "w1": w1, "w2": w2, "seed": seed,
           "plant_k1": k1, "plant_k2": k2, "args": ARGS}
    if out.returncode == 3 and "abort" in out.stderr:
        rec.update(aborted=True, full=False, acc=None, score=None, hit=False, first_ok_nidp=None)
        return rec
    if out.returncode != 0 or not lines:
        raise RuntimeError(f"{args}: rc={out.returncode} {out.stderr[-500:]}")
    fin = json.loads(lines[-1])
    rec.update({k: fin[k] for k in ("t", "cpu", "iter", "n_idp", "n_q", "idp", "score", "k2same", "hit_at", "k1", "k2")})
    rec["aborted"] = False
    rec["acc"] = round(run21.shift_acc(fin["pt"], pt), 4)
    rec["acc_inplace"] = fin["acc"]
    rec["full"] = rec["acc"] >= 0.95
    rec["first_ok_nidp"] = next((json.loads(l)["n_idp"] for l in lines if run21.shift_acc(json.loads(l)["pt"], pt) >= 0.95), None)
    rec["hit"] = fin["hit_at"] >= 0
    return rec


def controls(workers):
    check_binary()
    t1()
    run21.load_words("es")
    done = {(r["n"], r["trial"]) for r in load(CTL)}
    cost = cost_table()
    jobs = []
    for n in LENGTHS:
        for i, spec in enumerate(SPECS):
            if (n, i) in done:
                continue
            pt, k1, k2, ct = run21.plant(ctl_tag(n), i, "es", n, spec, "telegraph")
            assert len(pt) == len(ct) == n and sorted(ct) == sorted(pt)
            jobs.append((n, i, spec, pt, k1, k2, ct))
    jobs.sort(key=lambda j: -cost[(len(j[4]), len(j[5]))])
    print(f"controls: {len(jobs)} to run, {len(done)} done; "
          + ", ".join(f"{j[0]}/{j[1]}:{len(j[4])}x{len(j[5])}" for j in jobs), flush=True)
    os.makedirs(RES, exist_ok=True)
    with ThreadPoolExecutor(workers) as ex, open(CTL, "a") as f:
        for fu in as_completed([ex.submit(ctl_job, j) for j in jobs]):
            r = fu.result()
            f.write(json.dumps(r) + "\n")
            f.flush()
            print(f"ctl n={r['n']} t{r['trial']} {r['w1']}x{r['w2']} acc={r['acc']} full={r['full']} hit={r['hit']} "
                  f"score={r['score']} first_ok={r['first_ok_nidp']} cpu={r.get('cpu')}", flush=True)
    for n in LENGTHS:
        print(status_line(n), flush=True)


def ctl_status(n):
    R = [r for r in load(CTL) if r["n"] == n]
    rec = [r for r in R if r["full"]]
    complete = len({r["trial"] for r in R}) == TRIALS
    passed = complete and len(rec) >= PASS_AT
    low = min((r["score"] for r in rec), default=None)
    thr = BASE_THR if low is None or low > BASE_THR else (low + NOISE) / 2
    return dict(n=n, runs=len(R), complete=complete, recovered=len(rec), passed=passed, lowest=low, threshold=thr)


def status_line(n):
    s = ctl_status(n)
    return (f"length {n} ({LENGTHS[n]}): {s['recovered']}/{s['runs']} recovered, "
            f"{'PASS' if s['passed'] else ('FAIL: not testable' if s['complete'] else 'incomplete')}, "
            f"lowest recovered {s['lowest']}, threshold {s['threshold']:.4f}")


# ---------------- target ----------------
def body_file(name):
    a, b = BODIES[name]
    os.makedirs(OUTD, exist_ok=True)
    p = os.path.join(OUTD, f"T1_{a}-{b}.txt")
    open(p, "w").write(t1()[a:b])
    return p


def tgt_job(job):
    name, cf, w1, w2 = job
    seed = run21.stream("solver", f"target22|{name}", f"{w1}x{w2}")
    args = ["solve", cf, f"w1={w1}", f"w2={w2}", "lang=es", f"seed={seed}"] + ARGS
    out, lines = dcm_run(args)
    d = os.path.join(OUTD, "target22")
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, f"{name}_{w1}x{w2}.log"), "w").write(out.stdout + out.stderr)
    if out.returncode != 0 or not lines:
        raise RuntimeError(f"{args}: rc={out.returncode} {out.stderr[-500:]}")
    fin = json.loads(lines[-1])
    return dict(body=name, n=len(fin["pt"]), w1=w1, w2=w2, seed=seed, args=ARGS,
                **{k: fin[k] for k in ("t", "cpu", "iter", "n_idp", "idp", "score", "k1", "k2", "pt")})


def target(workers):
    check_binary()
    t1()
    done = {(r["body"], r["w1"], r["w2"]) for r in load(TGT)}
    cost = cost_table()
    jobs = []
    for n, name in LENGTHS.items():
        s = ctl_status(n)
        print(status_line(n), flush=True)
        if not s["passed"]:
            print(f"  {name}: not run (controls {'failed' if s['complete'] else 'incomplete'})", flush=True)
            continue
        cf = body_file(name)
        assert len(open(cf).read()) == n
        jobs += [(name, cf, w1, w2) for (w1, w2) in PAIRS if (name, w1, w2) not in done]
    jobs.sort(key=lambda j: -cost[(j[2], j[3])])
    print(f"target: {len(jobs)} to run, {len(done)} done", flush=True)
    with ThreadPoolExecutor(workers) as ex, open(TGT, "a") as f:
        for fu in as_completed([ex.submit(tgt_job, j) for j in jobs]):
            r = fu.result()
            f.write(json.dumps(r) + "\n")
            f.flush()
            thr = ctl_status(r["n"])["threshold"]
            flag = "  CANDIDATE: " + r["pt"][:200] if r["score"] > thr else ""
            print(f"tgt {r['body']} {r['w1']}x{r['w2']} score={r['score']:.4f} thr={thr:.4f} cpu={r['cpu']}{flag}", flush=True)


# ---------------- summary ----------------
def summary():
    L = [f"# 22-dc-trimmed — results (generated by `run22.py summary`)", "",
         f"Binary `21-dc-method/out/dcm`, SHA-256 `{check_binary()}`; arguments `{' '.join(ARGS)}`.", ""]
    C = load(CTL)
    L += ["## Controls (pass: ≥ 95% of positions, cyclic shift ≤ 40; a length passes at ≥ 8/10)", ""]
    for n, name in LENGTHS.items():
        s = ctl_status(n)
        R = sorted((r for r in C if r["n"] == n), key=lambda r: r["trial"])
        firsts = [r["first_ok_nidp"] for r in R if r["full"] and r["first_ok_nidp"] is not None]
        L += [f"### {n} letters ({name}): {s['recovered']}/{s['runs']} recovered — "
              f"{'**pass**' if s['passed'] else ('**fail, not testable**' if s['complete'] else 'incomplete')}; "
              f"threshold {s['threshold']:.4f}"
              + (f"; slowest first recovery {max(firsts) / 1e6:.2f} M evaluations" if firsts else ""), "",
              "| trial | stratum | w1 × w2 | acc (shift ≤ 40) | K2 hit | first ≥ 95% (M eval.) | final score | CPU s |",
              "|---|---|---|---|---|---|---|---|"]
        for r in R:
            fo = f"{r['first_ok_nidp'] / 1e6:.2f}" if r["first_ok_nidp"] is not None else "—"
            sc = f"{r['score']:.4f}" if r["score"] is not None else "aborted"
            L.append(f"| {r['trial']} | {'corner' if r['spec'] == '12-15x17' else 'band'} | {r['w1']} × {r['w2']} | "
                     f"{r['acc']} | {r['hit']} | {fo} | {sc} | {r.get('cpu', '—')} |")
        L.append("")
    T = load(TGT)
    L += ["## Target (candidate: final per-letter score above the length's threshold)", ""]
    for n, name in LENGTHS.items():
        R = sorted((r for r in T if r["body"] == name), key=lambda r: (r["w2"], r["w1"]))
        s = ctl_status(n)
        if not R:
            L += [f"### {name}: not run" + ("" if s["passed"] else " (controls did not pass)"), ""]
            continue
        thr = s["threshold"]
        best = max(R, key=lambda r: r["score"])
        cands = [r for r in R if r["score"] > thr]
        L += [f"### {name}: {len(R)}/{len(PAIRS)} pairs; threshold {thr:.4f}; best {best['score']:.4f} at "
              f"{best['w1']} × {best['w2']} (margin {best['score'] - thr:+.3f}); candidates: {len(cands)}", "",
              "| w1 × w2 | score | margin | CPU s | first 60 letters |", "|---|---|---|---|---|"]
        for r in R:
            L.append(f"| {r['w1']} × {r['w2']} | {r['score']:.4f} | {r['score'] - thr:+.3f} | {r['cpu']} | {r['pt'][:60]} |")
        for r in cands:
            L += ["", f"**Candidate** {name} {r['w1']} × {r['w2']}, score {r['score']:.4f}: `{r['pt'][:200]}`"]
        L.append("")
    text = "\n".join(L)
    os.makedirs(RES, exist_ok=True)
    open(os.path.join(RES, "summary.md"), "w").write(text + "\n")
    print(text)


if __name__ == "__main__":
    cmd = sys.argv[1]
    w = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    {"controls": lambda: controls(w), "target": lambda: target(w), "summary": summary}[cmd]()

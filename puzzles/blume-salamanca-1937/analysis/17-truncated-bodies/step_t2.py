"""Tier 2 of 17-truncated-bodies: head trims, two-sided trims, and the joint T1 + T2 double columnar attack.

The plan is README.md ("Bodies", tier 2; "Steps" A and B), executed as tier 1 ran it (stepAC.md, stepB.md), plus the
joint attack in the region where joint search has power (w1 8-15 x w2 16-17; stepT2.md says why). Nothing in
step_a.py, step_b.py, 01-solver or 15-tail-robustness is changed. step_a.py is imported for colsolve (and its
import-time checks on colsolve's frozen schedule), its run_control, bands and constants; step_b.py for dtsolve's
convention, language, bands and plant ranges. The dtsolve call mirrors step_b.dtsolve, with 03-target-h1's joint
argument (CT2 after PT) added.

Bodies
  T1[a : 615 - b], a in {5, 10, 15, 20}, b in {0, 5, 10, 15, 20}            20 bodies, 575-610 letters
  T2[a : 160 - b], every (a, b) in {0, 5, 10, 15, 20}^2 but (0, 0), (0, 5)   23 bodies, 120-155 letters
  Joint: T1[0 : 615 - b] + T2[0 : 155] under one pair of keys, b in {0, 5, 10, 15, 20}
Run order (groups): t1-head (b = 0), t1-two (a, b > 0), t2-head, t2-tail (a = 0), t2-two; then joint.

Usage, from this folder, in this order (5 worker processes at most, always):
  python3 -I step_t2.py controls-a                       A2 at every body length    -> controls-T2A.jsonl
  python3 -I step_t2.py noise-a                          A3 at every body length    -> noise-T2A.jsonl
  python3 -I step_t2.py thresholds-a > thresholds-T2A.md A4
  python3 -I step_t2.py controls-b SECS ["L/band" ...]   B3; 90 s only for failed cells -> controls-T2B.jsonl
  python3 -I step_t2.py thresholds-b > thresholds-T2B.md B4 and the per-cell budget
  python3 -I step_t2.py controls-j                       joint controls             -> controls-T2J.jsonl
  python3 -I step_t2.py thresholds-j > thresholds-T2J.md
  python3 -I step_t2.py target-a [SEL] [--deadline-min M] [--smoke W,W]               -> result-T2A.jsonl
  python3 -I step_t2.py target-b [SEL] [--deadline-min M] [--smoke W1xW2,...]         -> result-T2B.jsonl
  python3 -I step_t2.py target-j [B,B] [--deadline-min M] [--smoke W1xW2,...]         -> result-T2J.jsonl
  python3 -I step_t2.py check-replay | precheck | report-controls | plan | summary
      check-replay: dts_k2_draws against an instrumented scratch build of dtsolve.c; precheck: every start check
SEL is a comma list of groups (t1-head, t1-two, t2-head, t2-tail, t2-two) or body labels such as "T1[5:615]";
default: every group the step covers, in run order. Each target subcommand refuses to run unless its thresholds
file holds, character for character, the check lines recomputed from the control files; it resumes (runs already
in its results file are skipped, their seeds checked); with --deadline-min it submits a run only if the run can
finish inside the deadline. --smoke runs only the listed widths and writes out/t2/smoke-*.jsonl instead.

Seeds. Every stream is random.Random(<string>) (a str seed is hashed with SHA-512, so streams do not depend on
PYTHONHASHSEED). Plant, control-solver and target-solver streams are separate for each step:
  A: "17-T2-A-plant", "17-T2-A-solver-controls", "17-T2-A-shuffle", "17-T2-A-solver-noise", "17-T2-A-solver-target"
  B: "17-T2-B-plant", "17-T2-B-control-solver", "17-T2-B-target-solver"
  J: "17-T2-J-plant", "17-T2-J-control-solver", "17-T2-J-target-solver"
Target seeds are drawn in one fixed order over every body and width of the step (bodies in run order), so a seed
does not depend on which bodies were run. Start checks, made for every control before any control runs:
  A (w >= 9): colsolve's first annealing key, replayed from the solver seed, differs from the planted key
      (step_a.first_restart_key; step_a.run_control asserts it again). w <= 8 is exhaustive and takes no seed.
  B, J: dtsolve's first K2 candidate is its first random draw (dtsolve.c, solve, step 1). dts_k2_draws replays
      dtsolve's xorshift64* stream (checked against an instrumented scratch build; stepT2.md) and the check
      asserts that the first draw differs from the planted K2 for w2 >= 6. For w2 <= 5 the 200 draws of step 1
      span the whole key space for any seed, so no start can avoid the planted K2; the count of planted-K2 hits
      among the first 200 draws is recorded per plant (k2_hits_first200).
"""
import json, math, os, random, statistics, subprocess, sys, time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, wait, FIRST_COMPLETED

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)        # python3 -I does not put the script's folder on sys.path
import step_a as A              # noqa: E402  chdirs to 01-solver; imports colsolve and asserts its frozen schedule
import step_b as B              # noqa: E402  dtsolve convention CC, Spanish, bands, plant ranges
from step_a import plaintext, transpo, colsolve, shift_acc  # noqa: E402
from control import quad_per_letter  # noqa: E402  (01-solver/control.py; per-letter Spanish quadgram score)

SOLVER = os.path.normpath(os.path.join(HERE, "..", "01-solver"))
OUT = os.path.join(HERE, "out", "t2")
WORKERS = 5
GRID = (0, 5, 10, 15, 20)
B_THRESHOLD, B_NOISE_FAIL = -5.10, -5.19     # 01's threshold and its highest noise failure (README step B4)
J_BS, J_N2, J_W1, J_W2, J_SECS, J_PER = (0, 5, 10, 15, 20), 155, range(8, 16), range(16, 18), 180, 10

# ---------------------------------------------------------------- bodies
GROUPS = {"t1-head": ("T1", [(a, 0) for a in GRID[1:]]),
          "t1-two": ("T1", [(a, b) for a in GRID[1:] for b in GRID[1:]]),
          "t2-head": ("T2", [(a, 0) for a in GRID[1:]]),
          "t2-tail": ("T2", [(0, b) for b in GRID[2:]]),
          "t2-two": ("T2", [(a, b) for a in GRID[1:] for b in GRID[1:]])}
GROUP_ORDER = ("t1-head", "t1-two", "t2-head", "t2-tail", "t2-two")
FULL = {"T1": 615, "T2": 160}


def body(tel, a, b, group):
    n = FULL[tel] - a - b
    return dict(body=f"{tel}[{a}:{FULL[tel] - b}]", tel=tel, a=a, b=b, n=n, group=group)


ALL_BODIES = [body(GROUPS[g][0], a, b, g) for g in GROUP_ORDER for a, b in GROUPS[g][1]]
T1_BODIES = [x for x in ALL_BODIES if x["tel"] == "T1"]
T1_LENGTHS = sorted({x["n"] for x in T1_BODIES}, reverse=True)
T2_LENGTHS = sorted({x["n"] for x in ALL_BODIES if x["tel"] == "T2"}, reverse=True)
A_LENGTHS = T1_LENGTHS + T2_LENGTHS
assert len(ALL_BODIES) == 43 and len({x["body"] for x in ALL_BODIES}) == 43 and len(T1_BODIES) == 20
assert T1_LENGTHS == list(range(610, 574, -5)) and T2_LENGTHS == list(range(155, 119, -5))
assert not any(x["tel"] == "T2" and (x["a"], x["b"]) in ((0, 0), (0, 5)) for x in ALL_BODIES)


def text_of(x):
    t = A.telegrams()[0 if x["tel"] == "T1" else 1]
    s = t[x["a"]:len(t) - x["b"]]
    assert len(s) == x["n"], x
    return s


def select(sel, pool):
    """sel: None (every group in pool) or a comma list of group names and body labels."""
    if not sel:
        return pool
    want = sel.split(",")
    picked = [x for x in pool if x["group"] in want or x["body"] in want]
    unknown = [w for w in want if w not in GROUPS and w not in {x["body"] for x in ALL_BODIES}]
    assert picked and not unknown, (sel, unknown)
    return picked


# ---------------------------------------------------------------- solvers
def dts(ct_path, w1, w2, seed, secs, pt_path="-", ct2_path=None):
    """01-solver/out/dtsolve solve, unchanged: as step_b.dtsolve; CT2 appended as 03-target-h1 does (joint)."""
    args = ["out/dtsolve", "solve", ct_path, str(w1), str(w2), B.CONV, B.LANG, str(seed), str(secs), pt_path]
    if ct2_path:
        args.append(ct2_path)
    p = subprocess.run(args, capture_output=True, text=True, cwd=SOLVER)
    lines = [json.loads(x) for x in p.stdout.strip().splitlines()]
    assert p.returncode == 0 and lines and lines[-1]["tag"] == "final", (args, p.stderr)
    return lines


M64 = (1 << 64) - 1


def dts_k2_draws(seed, w2, count=200):
    """dtsolve's first `count` random K2 (solve, step 1 of iteration 1), replayed from its seed.
    dtsolve.c: rs = 88172645463325252 ^ seed * 0x9E3779B97F4A7C15; ten rnd64(); then random_key per draw
    (Fisher-Yates from the top, j = rnd64() % (i + 1)). k2_idp consumes no random numbers."""
    rs = 88172645463325252 ^ ((seed * 0x9E3779B97F4A7C15) & M64)
    out = []

    def r64():
        nonlocal rs
        rs ^= rs >> 12; rs ^= (rs << 25) & M64; rs ^= rs >> 27
        return (rs * 2685821657736338717) & M64
    for _ in range(10):
        r64()
    for _ in range(count):
        k = list(range(w2))
        for i in range(w2 - 1, 0, -1):
            j = r64() % (i + 1); k[i], k[j] = k[j], k[i]
        out.append(k)
    return out


def check_replay(cases=30):
    """Build a scratch copy of dtsolve.c (in out/t2/dtcheck; 01-solver untouched) that prints its first 200 K2
    draws to stderr and exits, and compare them with dts_k2_draws for random seeds and widths."""
    d = os.path.join(OUT, "dtcheck"); os.makedirs(d, exist_ok=True)
    src = open(os.path.join(SOLVER, "dtsolve.c")).read()
    old = "int k[MAXW]; random_key(k, w2); double v = k2_idp(k);"
    assert src.count(old) == 1
    dump = (' if (iter == 1) { for (int q = 0; q < w2; q++) fprintf(stderr, q ? ",%d" : "%d", k[q]);'
            ' fprintf(stderr, "\\n"); if (r == NRAND - 1) exit(0); }')
    open(os.path.join(d, "dt_dump.c"), "w").write(src.replace(old, old + dump))
    exe = os.path.join(d, "dt_dump")
    subprocess.run(["cc", "-O3", "-o", exe, os.path.join(d, "dt_dump.c"), "-lm"], check=True, capture_output=True)
    rnd = random.Random("17-T2-replay-check"); ok = 0
    for _ in range(cases):
        seed, w1, w2 = rnd.randrange(1 << 30), rnd.randint(2, 15), rnd.randint(2, 17)
        p = subprocess.run([exe, "solve", "out/t1.txt", str(w1), str(w2), "CC", "es", str(seed), "5"],
                           capture_output=True, text=True, cwd=SOLVER)
        got = [list(map(int, x.split(","))) for x in p.stderr.split()]
        ok += len(got) == 200 and got == dts_k2_draws(seed, w2)
    print(f"dts_k2_draws matches the instrumented dtsolve on {ok}/{cases} seeds (200 draws each)")
    assert ok == cases


def dts_start_check(job, k2):
    assert job["plant_seed"] != job["solver_seed"]
    draws = dts_k2_draws(job["solver_seed"], job["w2"])
    if job["w2"] >= 6:
        assert draws[0] != k2, f"dtsolve would start at the planted K2: {job}"
    return sum(k == k2 for k in draws)


# ---------------------------------------------------------------- step A (single columnar, colsolve unchanged)
def a_control_jobs():
    pr, sr = random.Random("17-T2-A-plant"), random.Random("17-T2-A-solver-controls")
    jobs = []
    for L in A_LENGTHS:
        for band, lo, hi in A.BANDS:
            for _ in range(A.PER_BAND):
                jobs.append(dict(kind="control", i=len(jobs), L=L, band=band, w=pr.randint(lo, hi),
                                 plant_seed=pr.randrange(1 << 30), solver_seed=sr.randrange(1 << 30)))
    return jobs


def a_precheck(jobs):
    for j in jobs:
        assert j["plant_seed"] != j["solver_seed"]
        if j["w"] >= 9:
            rnd = random.Random(j["plant_seed"]); plaintext.telegram(j["L"], rnd); k = rnd.sample(range(j["w"]), j["w"])
            assert A.first_restart_key(j["solver_seed"], j["w"]) != k, j
    print(f"start check: {len(jobs)} A controls, no annealing start at a planted key", flush=True)


def run_a_control(job):
    return A.run_control(job), None          # tier 1's code path, unchanged


def noise_body(L):
    """The body whose letters are shuffled for the noise ceiling at length L: the first of that length in run order."""
    return next(x for x in ALL_BODIES if x["n"] == L)


def a_noise_jobs():
    shr, sr = random.Random("17-T2-A-shuffle"), random.Random("17-T2-A-solver-noise")
    jobs = []
    for L in A_LENGTHS:
        x = noise_body(L)
        for w in A.NOISE_WIDTHS:
            for _ in range(A.NOISE_SHUFFLES):
                jobs.append(dict(kind="noise", i=len(jobs), L=L, body=x["body"], tel=x["tel"], a=x["a"], b=x["b"],
                                 n=L, w=w, shuffle_seed=shr.randrange(1 << 30), solver_seed=sr.randrange(1 << 30)))
    return jobs


def run_a_noise(job):
    t0 = time.time()
    s = list(text_of(job)); random.Random(job["shuffle_seed"]).shuffle(s)
    sc, kk = colsolve.solve("".join(s), job["w"], job["solver_seed"])
    return dict(job, score=round(sc, 4), key=list(kk), secs=round(time.time() - t0, 1)), None


def a_target_jobs():
    sr = random.Random("17-T2-A-solver-target")
    return [dict(kind="target", body=x["body"], tel=x["tel"], a=x["a"], b=x["b"], n=x["n"], group=x["group"], w=w,
                 solver_seed=sr.randrange(1 << 30)) for x in ALL_BODIES for w in A.WIDTHS]


def run_a_target(job):
    t0 = time.time()
    ct = text_of(job)
    s, kk = colsolve.solve(ct, job["w"], job["solver_seed"])
    rec = dict(job, score=round(s, 4), key=list(kk), candidate=s > job["threshold"], secs=round(time.time() - t0, 1))
    if rec["candidate"]:
        rec["dec200"] = colsolve.decrypt(ct, kk)[:200]    # recorded for the main thread; not read here
    return rec, None


def a_thresholds(ctrl, noise):
    res = {}
    for L in A_LENGTHS:
        rows = [r for r in ctrl if r["L"] == L]
        bands = {}
        for band, _, _ in A.BANDS:
            rs = [r for r in rows if r["band"] == band]; k = sum(r["ok"] for r in rs)
            bands[band] = dict(k=k, n=len(rs), passed=len(rs) == A.PER_BAND and k >= A.PASS_BAND * len(rs))
        passing = [r for r in rows if bands[r["band"]]["passed"] and r["ok"]]
        nz = [r for r in noise if r["L"] == L]
        ceil = max(r["score"] for r in nz)
        low = min(r["true_score"] for r in passing) if passing else None
        nz_pass = [r["score"] for r in nz if bands[A.band_of(r["w"])]["passed"]]
        res[L] = dict(bands=bands, noise_ceiling=ceil, noise_body=nz[0]["body"], low_true=low,
                      threshold=round((ceil + low) / 2, 4) if low is not None else None,
                      noise_passing_widths=max(nz_pass) if nz_pass else None)
    return res


def a_lines(th):
    out = []
    for L in A_LENGTHS:
        for band, _, _ in A.BANDS:
            v = th[L]["bands"][band]
            out.append(f"BAND-A L={L} {band}: {v['k']}/{v['n']} {'pass' if v['passed'] else 'FAIL'}")
        t = th[L]["threshold"]
        out.append(f"THRESHOLD-A L={L}: " + (f"{t:.4f}" if t is not None else "none (no band passed)"))
    return out


# ---------------------------------------------------------------- step B (double columnar CC, dtsolve unchanged)
def b_control_jobs():
    pr, sr = random.Random("17-T2-B-plant"), random.Random("17-T2-B-control-solver")
    jobs = []
    for L in T1_LENGTHS:
        for band, lo, hi in B.BANDS:
            for _ in range(B.PER_CELL):
                w1, w2 = pr.randint(*B.W1_PLANT), pr.randint(lo, hi)
                jobs.append(dict(i=len(jobs), L=L, band=band, w1=w1, w2=w2,
                                 plant_seed=pr.randrange(1 << 30), solver_seed=sr.randrange(1 << 30)))
    return jobs


def b_plant(job):
    """As step_b.control_one: plaintext, then K1, then K2, from the plant seed."""
    rnd = random.Random(job["plant_seed"])
    pt = plaintext.telegram(job["L"], rnd, B.LANG)
    k1, k2 = rnd.sample(range(job["w1"]), job["w1"]), rnd.sample(range(job["w2"]), job["w2"])
    assert len(pt) == job["L"]
    return pt, k1, k2, None


def j_plant(job):
    """As 01-solver/control.py (joint): plaintext 1, K1, K2, then plaintext 2 of 155 letters under the same keys."""
    rnd = random.Random(job["plant_seed"])
    pt = plaintext.telegram(job["L"], rnd, B.LANG)
    k1, k2 = rnd.sample(range(job["w1"]), job["w1"]), rnd.sample(range(job["w2"]), job["w2"])
    pt2 = plaintext.telegram(J_N2, rnd, B.LANG)
    assert len(pt) == job["L"] and len(pt2) == J_N2
    return pt, k1, k2, pt2


def dts_precheck(jobs, plant):
    hits = {}
    for j in jobs:
        hits[j["i"]] = dts_start_check(j, plant(j)[2])
    small = sum(1 for j in jobs if j["w2"] <= 5)
    print(f"start check: {len(jobs)} plants; first dtsolve K2 differs from the planted K2 for every w2 >= 6; "
          f"{small} plants at w2 <= 5 (step 1 spans the key space there)", flush=True)
    return hits


def run_dts_control(job):
    """One planted control (B: plant at L; J: plant at L + 155 under the same keys). Recovery is measured on the
    T1-length plaintext (dtsolve reports only that decryption), shift_acc >= 0.90, as tier 1."""
    joint = job["step"] == "J"
    pt, k1, k2, pt2 = (j_plant if joint else b_plant)(job)
    hits = dts_start_check(job, k2)
    d = os.path.join(OUT, f"controls-{job['step']}-{job['secs']}"); os.makedirs(d, exist_ok=True)
    cp, pp, cp2 = (os.path.join(d, f"{job['i']}_{s}.txt") for s in ("ct", "pt", "ct2"))
    open(cp, "w").write(transpo.double_enc(pt, k1, k2, B.CONV)); open(pp, "w").write(pt)
    if joint:
        open(cp2, "w").write(transpo.double_enc(pt2, k1, k2, B.CONV))
    t0 = time.time()
    lines = dts(cp, job["w1"], job["w2"], job["solver_seed"], job["secs"], pp, cp2 if joint else None)
    fin = lines[-1]; acc = shift_acc(fin["pt"], pt)
    first_ok = next((x["t"] for x in lines if shift_acc(x["pt"], pt) >= B.PASS_ACC), None)
    true = quad_per_letter(pt, B.LANG)
    if joint:   # dtsolve's joint score: both texts' quadgram sums over both texts' quadgram counts
        n1, n2 = len(pt) - 3, len(pt2) - 3
        true = (true * n1 + quad_per_letter(pt2, B.LANG) * n2) / (n1 + n2)
    return dict(job, k1=",".join(map(str, k1)), k2=",".join(map(str, k2)), acc=round(acc, 4), ok=acc >= B.PASS_ACC,
                score=fin["score"], true_score=round(true, 4), idp=fin["idp"], iters=fin["iter"], t_first_ok=first_ok,
                k2_hits_first200=hits, wall=round(time.time() - t0, 1), dec60=fin["pt"][:60], ref60=pt[:60]), None


def b_verdicts(ctrl):
    res = {}
    for L in T1_LENGTHS:
        cells = {}
        for band, _, _ in B.BANDS:
            c = {}
            for secs in sorted({r["secs"] for r in ctrl}):
                rs = [r for r in ctrl if r["L"] == L and r["band"] == band and r["secs"] == secs]
                if rs:
                    k = sum(r["ok"] for r in rs)
                    c[secs] = dict(k=k, n=len(rs), passed=len(rs) == B.PER_CELL and k >= 0.8 * len(rs))
            if c.get(30, {}).get("passed"):
                budget = 30
            elif 30 in c and 90 in c:
                budget = 90 if c[90]["passed"] else "skip"
            else:
                budget = None          # 30 s not run, or failed and its 90 s rerun not yet run
            cells[band] = dict(runs=c, budget=budget)
        low = min(r["true_score"] for r in ctrl if r["L"] == L)
        thr = B_THRESHOLD if low > B_THRESHOLD else round((low + B_NOISE_FAIL) / 2, 4)
        res[L] = dict(cells=cells, low_true=low, threshold=thr)
    return res


def b_lines(v):
    out = []
    for L in T1_LENGTHS:
        for band, _, _ in B.BANDS:
            c = v[L]["cells"][band]
            runs = "; ".join(f"{s} s {x['k']}/{x['n']} {'pass' if x['passed'] else 'FAIL'}" for s, x in c["runs"].items())
            out.append(f"BUDGET-B L={L} {band}: {c['budget']} ({runs})")
        out.append(f"THRESHOLD-B L={L}: {v[L]['threshold']:.4f}")
    return out


def b_target_jobs():
    sr = random.Random("17-T2-B-target-solver")
    return [dict(body=x["body"], tel="T1", a=x["a"], b=x["b"], n=x["n"], group=x["group"], w1=w1, w2=w2,
                 seed=sr.randrange(1 << 30)) for x in T1_BODIES for w1 in B.WIDTHS for w2 in B.WIDTHS]


def body_file(x):
    d = os.path.join(OUT, "bodies"); os.makedirs(d, exist_ok=True)
    p = os.path.join(d, f"{x['tel']}_{x['a']}_{x['a'] + x['n']}.txt")
    t = text_of(x)
    if not os.path.exists(p) or open(p).read() != t:
        open(p, "w").write(t)
    return p, t


def run_b_target(job):
    p, t = body_file(job)
    t0 = time.time()
    fin = dts(p, job["w1"], job["w2"], job["seed"], job["secs"])[-1]
    assert len(fin["pt"]) == job["n"] and sorted(fin["pt"]) == sorted(t)
    rec = dict(job, score=fin["score"], idp=fin["idp"], iters=fin["iter"], k1=fin["k1"], k2=fin["k2"],
               candidate=fin["score"] > job["threshold"], wall=round(time.time() - t0, 1))
    return rec, dict(pt=fin["pt"])


# ---------------------------------------------------------------- joint (T1[0 : 615 - b] + T2[0 : 155], shared keys)
def j_control_jobs():
    pr, sr = random.Random("17-T2-J-plant"), random.Random("17-T2-J-control-solver")
    jobs = []
    for b in J_BS:
        for _ in range(J_PER):
            w1, w2 = pr.randint(J_W1[0], J_W1[-1]), pr.randint(J_W2[0], J_W2[-1])
            jobs.append(dict(step="J", i=len(jobs), L=615 - b, n2=J_N2, w1=w1, w2=w2, secs=J_SECS,
                             plant_seed=pr.randrange(1 << 30), solver_seed=sr.randrange(1 << 30)))
    return jobs


def j_verdicts(ctrl):
    res = {}
    for b in J_BS:
        rs = [r for r in ctrl if r["L"] == 615 - b]
        k = sum(r["ok"] for r in rs)
        low = min(r["true_score"] for r in rs) if rs else None
        thr = B_THRESHOLD if low is None or low > B_THRESHOLD else round((low + B_NOISE_FAIL) / 2, 4)
        res[615 - b] = dict(k=k, n=len(rs), passed=len(rs) == J_PER and k >= 0.8 * J_PER, low_true=low, threshold=thr)
    return res


def j_lines(v):
    out = []
    for L, x in v.items():
        out.append(f"JOINT L={L}+{J_N2}: {x['k']}/{x['n']} {'pass' if x['passed'] else 'FAIL (not testable)'}")
        out.append(f"THRESHOLD-J L={L}+{J_N2}: {x['threshold']:.4f}")
    return out


def j_target_jobs():
    sr = random.Random("17-T2-J-target-solver")
    return [dict(body=f"T1[0:{615 - b}]+T2[0:{J_N2}]", b=b, n=615 - b, n2=J_N2, w1=w1, w2=w2, secs=J_SECS,
                 seed=sr.randrange(1 << 30)) for b in J_BS for w1 in J_W1 for w2 in J_W2]


def run_j_target(job):
    p1, t1 = body_file(body("T1", 0, job["b"], "joint"))
    p2, t2 = body_file(body("T2", 0, 160 - J_N2, "joint"))
    t0 = time.time()
    fin = dts(p1, job["w1"], job["w2"], job["seed"], job["secs"], "-", p2)[-1]
    assert len(fin["pt"]) == job["n"] and sorted(fin["pt"]) == sorted(t1)
    rec = dict(job, score=fin["score"], idp=fin["idp"], iters=fin["iter"], k1=fin["k1"], k2=fin["k2"],
               candidate=fin["score"] > job["threshold"], wall=round(time.time() - t0, 1))
    k1 = [int(c) for c in fin["k1"].split(",")]; k2 = [int(c) for c in fin["k2"].split(",")]
    return rec, dict(pt=fin["pt"], pt2=transpo.double_dec(t2, k1, k2, B.CONV))


# ---------------------------------------------------------------- driver
def read(path):
    return [json.loads(x) for x in open(path)] if os.path.exists(path) else []


def P(name):
    return os.path.join(HERE, name)


def drive(fn, jobs, key, path, threads, deadline=None, est=None, side_path=None):
    """Run jobs WORKERS at a time; append one JSON line per finished job to path. Resumes: a job whose key is in
    path already is skipped, after checking that every field of the job matches the stored line."""
    have = {key(r): r for r in read(path)}
    for j in jobs:
        h = have.get(key(j))
        assert h is None or all(h[x] == j[x] for x in j), (j, h)
    todo = [j for j in jobs if key(j) not in have]
    print(f"{len(jobs) - len(todo)} done, {len(todo)} to run -> {os.path.relpath(path, HERE)}", flush=True)
    t0, n, left = time.time(), 0, 0
    Ex = ThreadPoolExecutor if threads else ProcessPoolExecutor
    g = open(side_path, "a") if side_path else None
    with open(path, "a") as f, Ex(WORKERS) as ex:
        running = set()

        def collect(block_at):
            nonlocal running, n
            while running and len(running) >= block_at:
                fin, running = wait(running, return_when=FIRST_COMPLETED)
                for fu in fin:
                    rec, side = fu.result()
                    f.write(json.dumps(rec) + "\n"); f.flush()
                    if g and side is not None:
                        g.write(json.dumps(dict(rec, **side)) + "\n"); g.flush()
                    n += 1
                    w = f"{rec['w1']}x{rec['w2']}" if "w1" in rec else f"w={rec['w']}"
                    tag = rec.get("body", rec.get("L"))
                    msg = f"[{n}/{len(todo)} {time.time() - t0:.0f}s] {tag} {w} score={rec['score']:.4f}"
                    if "true_score" in rec:
                        msg += f" true={rec['true_score']:.4f} acc={rec['acc']:.3f}"
                    if rec.get("candidate"):
                        msg += "  *** ABOVE THRESHOLD ***"
                    print(msg, flush=True)

        for idx, j in enumerate(todo):
            collect(WORKERS)
            if deadline and time.time() + est(j) > deadline:
                left = len(todo) - idx
                break
            running.add(ex.submit(fn, j))
        collect(1)
    if g:
        g.close()
    print(f"finished {n} runs in {time.time() - t0:.0f}s; {left} left out by the deadline", flush=True)


def est_a(j):
    """Seconds for one colsolve run (deadline planning only); from tier 1's timings, rounded up."""
    w, n = j["w"], j["n"]
    return 1.0 if w <= 7 else 5.0 * n / 600 if w == 8 else 0.004 * w * n


def check_lines(fname, lines):
    path = P(fname)
    if not os.path.exists(path):
        sys.exit(f"refusing to run: {fname} does not exist (write it with the thresholds subcommand first)")
    written = open(path).read()
    missing = [x for x in lines if x not in written]
    if missing:
        sys.exit(f"refusing to run: {fname} lacks these lines, recomputed from the controls:\n  " + "\n  ".join(missing))


def parse_target_args(argv):
    sel = argv[0] if argv and not argv[0].startswith("--") else None
    dl = float(argv[argv.index("--deadline-min") + 1]) if "--deadline-min" in argv else None
    smoke = argv[argv.index("--smoke") + 1] if "--smoke" in argv else None
    return sel, (time.time() + dl * 60 if dl else None), smoke


def outputs(step, smoke):
    os.makedirs(OUT, exist_ok=True)
    if smoke:
        return os.path.join(OUT, f"smoke-T2{step}.jsonl"), os.path.join(OUT, f"smoke-target-T2{step}.jsonl")
    return P(f"result-T2{step}.jsonl"), os.path.join(OUT, f"target-T2{step}.jsonl")


# ---------------------------------------------------------------- subcommands
def cmd_target_a(argv):
    sel, deadline, smoke = parse_target_args(argv)
    ctrl, noise = read(P("controls-T2A.jsonl")), read(P("noise-T2A.jsonl"))
    assert len(ctrl) == len(a_control_jobs()) and len(noise) == len(a_noise_jobs()), "A controls or noise incomplete"
    th = a_thresholds(ctrl, noise)
    check_lines("thresholds-T2A.md", a_lines(th))
    names = {x["body"] for x in select(sel, ALL_BODIES)}
    jobs = [dict(j, threshold=th[j["n"]]["threshold"]) for j in a_target_jobs()
            if j["body"] in names and th[j["n"]]["bands"][A.band_of(j["w"])]["passed"]]
    if smoke:
        ws = {int(w) for w in smoke.split(",")}; jobs = [j for j in jobs if j["w"] in ws]
    order = {x["body"]: k for k, x in enumerate(ALL_BODIES)}
    jobs.sort(key=lambda j: (order[j["body"]], -j["w"]))      # run order; widest first inside a body
    path, _ = outputs("A", smoke)
    drive(run_a_target, jobs, lambda r: (r["body"], r["w"]), path, threads=False, deadline=deadline, est=est_a)


def cmd_target_b(argv):
    sel, deadline, smoke = parse_target_args(argv)
    v = b_verdicts(read(P("controls-T2B.jsonl")))
    assert all(c["budget"] is not None for L in T1_LENGTHS for c in v[L]["cells"].values()), "B controls incomplete"
    check_lines("thresholds-T2B.md", b_lines(v))
    names = {x["body"] for x in select(sel, T1_BODIES)}
    jobs = []
    for j in b_target_jobs():
        budget = v[j["n"]]["cells"][B.band_of(j["w2"])]["budget"]
        if j["body"] in names and budget != "skip":
            jobs.append(dict(j, secs=budget, threshold=v[j["n"]]["threshold"]))
    if smoke:
        ps = {tuple(map(int, p.split("x"))) for p in smoke.split(",")}; jobs = [j for j in jobs if (j["w1"], j["w2"]) in ps]
    order = {x["body"]: k for k, x in enumerate(T1_BODIES)}
    jobs.sort(key=lambda j: (order[j["body"]], -j["secs"]))     # stable: w1, w2 order inside a body and budget
    path, side = outputs("B", smoke)
    drive(run_b_target, jobs, lambda r: (r["body"], r["w1"], r["w2"]), path, threads=True, deadline=deadline,
          est=lambda j: j["secs"] + 1, side_path=side)


def cmd_target_j(argv):
    sel, deadline, smoke = parse_target_args(argv)
    ctrl = read(P("controls-T2J.jsonl"))
    assert len(ctrl) == len(j_control_jobs()), "joint controls incomplete"
    v = j_verdicts(ctrl)
    check_lines("thresholds-T2J.md", j_lines(v))
    bs = [int(x) for x in sel.split(",")] if sel else list(J_BS)
    jobs = [dict(j, threshold=v[j["n"]]["threshold"]) for j in j_target_jobs() if j["b"] in bs and v[j["n"]]["passed"]]
    if smoke:
        ps = {tuple(map(int, p.split("x"))) for p in smoke.split(",")}; jobs = [j for j in jobs if (j["w1"], j["w2"]) in ps]
    jobs.sort(key=lambda j: bs.index(j["b"]))
    path, side = outputs("J", smoke)
    drive(run_j_target, jobs, lambda r: (r["b"], r["w1"], r["w2"]), path, threads=True, deadline=deadline,
          est=lambda j: j["secs"] + 1, side_path=side)


def fmt(x, nd=4):
    return "—" if x is None else f"{x:.{nd}f}".replace("-", "−")


def thresholds_a():
    ctrl, noise = read(P("controls-T2A.jsonl")), read(P("noise-T2A.jsonl"))
    assert len(ctrl) == len(a_control_jobs()) and len(noise) == len(a_noise_jobs()), "A controls or noise incomplete"
    th = a_thresholds(ctrl, noise)
    print("# Tier 2, step A: thresholds, fixed before any tier-2 target run\n")
    print(f"Generated {time.strftime('%Y-%m-%d %H:%M %Z')} by `python3 -I step_t2.py thresholds-a` from "
          "`controls-T2A.jsonl` and `noise-T2A.jsonl`. Rule (README step A4): halfway between the highest noise score "
          "at that length (shuffles of one body of that length, widths 5, 8, 12, 20, 30, 45, three shuffles each) and "
          "the lowest true-text score among recovered plants of the passing bands at that length. A band passes at "
          "≥ 8/10 plants with ≥ 90% of letters in place. Every body uses the controls of its own length. "
          "`step_t2.py target-a` refuses to run unless every check line below is in this file.\n")
    print("| length | w 5–8 | w 9–30 | w 31–45 | noise body | noise ceiling | noise, passing widths only | "
          "lowest true text (passing) | threshold |")
    print("|---|---|---|---|---|---|---|---|---|")
    for L in A_LENGTHS:
        d = th[L]
        cells = [f"{v['k']}/{v['n']} {'pass' if v['passed'] else '**fail**'}" for v in d["bands"].values()]
        print(f"| {L} | {' | '.join(cells)} | {d['noise_body']} | {fmt(d['noise_ceiling'])} | "
              f"{fmt(d['noise_passing_widths'])} | {fmt(d['low_true'])} | **{fmt(d['threshold'])}** |")
    over = [L for L in A_LENGTHS if d_over(th[L])]
    if over:
        print(f"\nAt L = {', '.join(map(str, over))} the noise ceiling lies at or above the lowest passing true text, "
              "so the threshold as the rule draws it lies above some true texts. It is applied as written; the "
              "main thread judges.")
    print("\nCheck lines:\n```")
    print("\n".join(a_lines(th)))
    print("```")


def d_over(d):
    return d["low_true"] is not None and d["noise_ceiling"] >= d["low_true"]


def thresholds_b():
    ctrl = read(P("controls-T2B.jsonl"))
    v = b_verdicts(ctrl)
    pending = [f"{L}/{band}" for L in T1_LENGTHS for band, c in v[L]["cells"].items() if c["budget"] is None]
    if pending:
        sys.exit("B controls incomplete (run 30 s, then 90 s for failed cells): " + ", ".join(pending))
    print("# Tier 2, step B: thresholds and budgets, fixed before any tier-2 target run\n")
    print(f"Generated {time.strftime('%Y-%m-%d %H:%M %Z')} by `python3 -I step_t2.py thresholds-b` from "
          "`controls-T2B.jsonl`. Rule (README steps B3, B4): a band passes at ≥ 8/10 plants with ≥ 90% of letters in "
          "place; a band that fails at 30 s is rerun at 90 s (same plants, same solver seeds) and, if it passes, its "
          "target runs use 90 s; a band that fails at 90 s is not testable (`skip`). Threshold −5.10 unless a control's "
          "true text scores at or below −5.10 at that length; then halfway between the lowest true text and −5.19. "
          "`step_t2.py target-b` refuses to run unless every check line below is in this file.\n")
    print("| length | band | 30 s | 90 s | budget | lowest true text (all plants at L) | threshold |")
    print("|---|---|---|---|---|---|---|")
    for L in T1_LENGTHS:
        for band, c in v[L]["cells"].items():
            r = c["runs"]
            cell = lambda s: f"{r[s]['k']}/{r[s]['n']} {'pass' if r[s]['passed'] else '**fail**'}" if s in r else "not run"
            print(f"| {L} | {band} | {cell(30)} | {cell(90)} | {c['budget']} | {fmt(v[L]['low_true'])} | "
                  f"{fmt(v[L]['threshold'])} |")
    print("\nCheck lines:\n```")
    print("\n".join(b_lines(v)))
    print("```")


def thresholds_j():
    ctrl = read(P("controls-T2J.jsonl"))
    assert len(ctrl) == len(j_control_jobs()), "joint controls incomplete"
    v = j_verdicts(ctrl)
    print("# Tier 2, joint attack: verdicts and thresholds, fixed before any joint target run\n")
    print(f"Generated {time.strftime('%Y-%m-%d %H:%M %Z')} by `python3 -I step_t2.py thresholds-j` from "
          "`controls-T2J.jsonl`. Plants: T1-length plaintext plus 155 letters under the same keys, w1 8–15, w2 16–17, "
          "180 s, 10 per length. Pass: ≥ 8/10 with ≥ 90% of the T1-length letters in place. A failing length is not "
          "testable and its target is not run. Threshold −5.10 (joint per-letter score, as `03`'s H2) unless a control's "
          "joint true text scores at or below −5.10; then halfway between the lowest true text and −5.19. "
          "`step_t2.py target-j` refuses to run unless every check line below is in this file.\n")
    print("| joint length | recovered | verdict | lowest true text | threshold |")
    print("|---|---|---|---|---|")
    for L, x in v.items():
        print(f"| {L} + {J_N2} | {x['k']}/{x['n']} | {'pass' if x['passed'] else '**fail** (not testable)'} | "
              f"{fmt(x['low_true'])} | {fmt(x['threshold'])} |")
    print("\nCheck lines:\n```")
    print("\n".join(j_lines(v)))
    print("```")


def report_controls():
    ctrl = read(P("controls-T2A.jsonl")); noise = read(P("noise-T2A.jsonl"))
    if ctrl:
        print("### Step A controls (recovered / 10; failures: found score vs true score)\n")
        print("| length | band | recovered | true text min..max | failures |")
        print("|---|---|---|---|---|")
        for L in A_LENGTHS:
            for band, _, _ in A.BANDS:
                rs = sorted((r for r in ctrl if r["L"] == L and r["band"] == band), key=lambda r: r["i"])
                if not rs:
                    continue
                k = sum(r["ok"] for r in rs); ts = [r["true_score"] for r in rs]
                fails = ", ".join(f"w{r['w']} {fmt(r['score'], 3)} vs {fmt(r['true_score'], 3)}" for r in rs if not r["ok"])
                print(f"| {L} | {band} | {k}/{len(rs)} {'pass' if k >= 8 and len(rs) == 10 else '**fail**'} | "
                      f"{fmt(min(ts))}..{fmt(max(ts))} | {fails or '—'} |")
        above = [r for r in ctrl if not r["ok"] and r["score"] > r["true_score"] + 1e-9]
        print(f"\nFailed plants that scored above their own true text (not search failures): {len(above)}")
    if noise:
        print("\n### Step A noise ceiling (best of 3 shuffles per width)\n")
        print("| length | body | " + " | ".join(f"w {w}" for w in A.NOISE_WIDTHS) + " |")
        print("|---|---|" + "---|" * len(A.NOISE_WIDTHS))
        for L in A_LENGTHS:
            rs = [r for r in noise if r["L"] == L]
            if rs:
                print(f"| {L} | {rs[0]['body']} | " + " | ".join(
                    fmt(max((r["score"] for r in rs if r["w"] == w), default=None), 3) for w in A.NOISE_WIDTHS) + " |")
    for step, name in (("B", "controls-T2B.jsonl"), ("J", "controls-T2J.jsonl")):
        rs = read(P(name))
        if not rs:
            continue
        print(f"\n### Step {step} controls\n")
        print("| budget | length | band | recovered | acc range | solver score (recovered) | true text (all) | slowest recovery |")
        print("|---|---|---|---|---|---|---|---|")
        for secs in sorted({r["secs"] for r in rs}):
            for L in sorted({r["L"] for r in rs}, reverse=True):
                for band in sorted({r.get("band", "w2 16-17") for r in rs}):
                    x = [r for r in rs if r["secs"] == secs and r["L"] == L and r.get("band", "w2 16-17") == band]
                    if not x:
                        continue
                    ok = [r for r in x if r["ok"]]; k = len(ok)
                    rng = lambda v: f"{fmt(min(v))} to {fmt(max(v))}" if v else "none"
                    slow = max((r["t_first_ok"] for r in ok if r["t_first_ok"] is not None), default=None)
                    lab = f"{L}" if step == "B" else f"{L} + {J_N2}"
                    print(f"| {secs} s | {lab} | {band} | {k}/{len(x)} {'pass' if k >= 8 and len(x) == 10 else '**fail**'} | "
                          f"{min(r['acc'] for r in x):.3f}–{max(r['acc'] for r in x):.3f} | {rng([r['score'] for r in ok])} | "
                          f"{rng([r['true_score'] for r in x])} | {slow if slow is not None else '—'} s |")
        fails = [r for r in rs if not r["ok"]]
        print("\nFailed plants:" if fails else "\nFailed plants: none")
        for r in fails:
            print(f"- {r['secs']} s, L {r['L']}, {r['w1']} × {r['w2']}: acc {r['acc']:.3f}, solver {fmt(r['score'])}, "
                  f"true {fmt(r['true_score'])}")
        one = {(r["i"], r["w2"], r["k2_hits_first200"]) for r in rs}      # a plant once, whatever its budgets
        small = sum(1 for _, w2, _ in one if w2 <= 5)
        big = sorted((i, w2) for i, w2, h in one if w2 >= 6 and h > 0)
        expect = sum(1 - (1 - 1 / math.factorial(w2)) ** 200 for _, w2, _ in one if w2 >= 6)
        print(f"\nStart check: dtsolve's first K2 differs from the planted K2 in every plant at w2 ≥ 6 (asserted). "
              f"Plants at w2 ≤ 5, where step 1's 200 draws span the K2 space: {small}. Plants at w2 ≥ 6 whose planted "
              f"K2 is among the 200 first-iteration draws (by chance, not the first draw): {len(big)} "
              f"{'(' + ', '.join(f'plant {i}, w2 {w}' for i, w in big) + ') ' if big else ''}against "
              f"{expect:.2f} expected for independent draws.")


def plan():
    """Target job counts and estimated wall time at WORKERS, from the thresholds files' verdicts and the measured
    control and noise timings."""
    ctrl, noise = read(P("controls-T2A.jsonl")), read(P("noise-T2A.jsonl"))
    th = a_thresholds(ctrl, noise)
    timed = ctrl + noise

    def secs_a(n, w):
        same = [r["secs"] for r in timed if r["L"] == n and r["w"] == w]
        if same:
            return statistics.mean(same)
        per = [r["secs"] / r["w"] for r in timed if r["L"] == n and r["w"] >= 9]
        return statistics.median(per) * w if w >= 9 and per else est_a(dict(w=w, n=n))
    tot = {}
    for j in a_target_jobs():
        if th[j["n"]]["bands"][A.band_of(j["w"])]["passed"]:
            g = j["group"]; c, s = tot.get(g, (0, 0.0)); tot[g] = (c + 1, s + secs_a(j["n"], j["w"]))
    print("Step A target (colsolve), by group: runs, CPU s, wall h at 5 workers")
    for g in GROUP_ORDER:
        if g in tot:
            print(f"  {g:8} {tot[g][0]:5} runs {tot[g][1]:9.0f} s  {tot[g][1] / WORKERS / 3600:.2f} h")
    v = b_verdicts(read(P("controls-T2B.jsonl")))
    tb = {}
    for j in b_target_jobs():
        bud = v[j["n"]]["cells"][B.band_of(j["w2"])]["budget"]
        if bud not in ("skip", None):
            c, s = tb.get(j["group"], (0, 0.0)); tb[j["group"]] = (c + 1, s + bud + 0.5)
    print("Step B target (dtsolve), by group")
    for g, (c, s) in tb.items():
        print(f"  {g:8} {c:5} runs {s:9.0f} s  {s / WORKERS / 3600:.2f} h")
    jc = read(P("controls-T2J.jsonl"))
    if len(jc) == len(j_control_jobs()):
        vj = j_verdicts(jc)
        js = [j for j in j_target_jobs() if vj[j["n"]]["passed"]]
        print(f"Joint target: {len(js)} runs, {len(js) * (J_SECS + 0.5) / WORKERS / 3600:.2f} h; lengths run: "
              f"{sorted({j['n'] for j in js}, reverse=True)}")


def summary():
    """Result tables after the target runs (for the main thread)."""
    for step, name in (("A", "result-T2A.jsonl"), ("B", "result-T2B.jsonl"), ("J", "result-T2J.jsonl")):
        rs = read(P(name))
        print(f"\nStep {step}: {len(rs)} runs, {sum(r['candidate'] for r in rs)} above threshold")
        for bd in dict.fromkeys(r["body"] for r in rs):
            x = [r for r in rs if r["body"] == bd]
            m = max(x, key=lambda r: r["score"])
            w = f"{m['w1']}x{m['w2']}" if "w1" in m else f"w {m['w']}"
            print(f"  {bd:22} runs {len(x):4}  best {m['score']:.4f} at {w}  threshold {m['threshold']:.4f}  "
                  f"margin {m['score'] - m['threshold']:+.4f}")
        for r in rs:
            if r["candidate"]:
                print("  CANDIDATE", json.dumps(r))


def main():
    cmd, argv = sys.argv[1], sys.argv[2:]
    os.makedirs(OUT, exist_ok=True)
    if cmd == "controls-a":
        jobs = a_control_jobs(); a_precheck(jobs)
        drive(run_a_control, jobs, lambda r: r["i"], P("controls-T2A.jsonl"), threads=False)
    elif cmd == "noise-a":
        drive(run_a_noise, a_noise_jobs(), lambda r: r["i"], P("noise-T2A.jsonl"), threads=False)
    elif cmd == "thresholds-a":
        thresholds_a()
    elif cmd in ("controls-b", "controls-j"):
        if cmd == "controls-b":
            secs = int(argv[0]); assert secs in (30, 90)
            jobs = [dict(j, step="B", secs=secs) for j in b_control_jobs()]
            if argv[1:]:
                want = {tuple(c.split("/", 1)) for c in argv[1:]}
                jobs = [j for j in jobs if (str(j["L"]), j["band"]) in want]
                assert len(jobs) == B.PER_CELL * len(want), argv
            plant, path = b_plant, P("controls-T2B.jsonl")
        else:
            jobs, plant, path = j_control_jobs(), j_plant, P("controls-T2J.jsonl")
        dts_precheck(jobs, plant)
        drive(run_dts_control, jobs, lambda r: (r["i"], r["secs"]), path, threads=True)
    elif cmd == "thresholds-b":
        thresholds_b()
    elif cmd == "thresholds-j":
        thresholds_j()
    elif cmd == "target-a":
        cmd_target_a(argv)
    elif cmd == "target-b":
        cmd_target_b(argv)
    elif cmd == "target-j":
        cmd_target_j(argv)
    elif cmd == "check-replay":
        check_replay()
    elif cmd == "precheck":
        a_precheck(a_control_jobs())
        dts_precheck([dict(j, step="B", secs=30) for j in b_control_jobs()], b_plant)
        dts_precheck(j_control_jobs(), j_plant)
    elif cmd == "report-controls":
        report_controls()
    elif cmd == "plan":
        plan()
    elif cmd == "summary":
        summary()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()

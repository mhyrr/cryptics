"""Post hoc check of 18's target excess over shuffles (README, "Post hoc check"). Same solver and offset scan as
run.py. Null A: 20 shuffles of T1. Null B: 20 forward double columnar plants with w1, w2 uniform 16-25 (K1).
Usage (from this folder): python3 -I excess.py run   -> excess.jsonl (resumes)
                          python3 -I excess.py summary
"""
import json, os, random, sys
from concurrent.futures import ProcessPoolExecutor, as_completed
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run, setsolve  # noqa: E402  (run puts 01-solver on sys.path and makes it the working directory)
import plaintext, transpo  # noqa: E402

NS, PER = (20, 30), 20
F_OUT = os.path.join(HERE, "excess.jsonl")


def jobs():
    sh, pl, sr = random.Random("18x-shuffle"), random.Random("18x-plant"), random.Random("18x-solver")
    out = []
    for n in NS:
        for kind in ("shuffle", "K1"):
            for i in range(PER):
                out.append(dict(text="T1", n=n, kind=kind, i=i, seed=(sh if kind == "shuffle" else pl).randrange(1 << 30),
                                solver_seed=sr.randrange(1 << 30)))
    return out


def one(j):
    rnd = random.Random(j["seed"])
    if j["kind"] == "shuffle":
        letters = list(run.telegram("T1")); rnd.shuffle(letters); ct = "".join(letters); extra = {}
    else:
        w1, w2 = rnd.randint(16, 25), rnd.randint(16, 25)
        k1, k2 = rnd.sample(range(w1), w1), rnd.sample(range(w2), w2)
        ct = transpo.double_enc(plaintext.telegram(615, rnd), k1, k2, "CC"); extra = dict(w1=w1, w2=w2)
    s, a, o = setsolve.solve_scan(ct, j["n"], j["solver_seed"])
    return dict(j, **extra, score=round(s, 4), a=a)


def summary():
    R = [json.loads(l) for l in open(F_OUT)]
    X = {x["n"]: x["score"] for x in map(json.loads, open(run.F_TARGET)) if x["text"] == "T1"}
    print("| n | target | shuffles (20): median, 95th pct, max; target above | K1 plants (20): 5th pct, median, 95th pct; target above |")
    print("|---|---|---|---|")
    for n in NS:
        def stats(kind):
            v = sorted(r["score"] for r in R if r["n"] == n and r["kind"] == kind)
            return v, sum(x < X[n] for x in v)
        s, sa = stats("shuffle"); k, ka = stats("K1")
        print(f"| {n} | {X[n]:.3f} | {s[10]:.3f}, {s[18]:.3f}, {s[-1]:.3f}; {sa}/20 | "
              f"{k[1]:.3f}, {k[10]:.3f}, {k[18]:.3f}; {ka}/20 |")


if __name__ == "__main__":
    if sys.argv[1] == "run":
        run.run_jobs(jobs(), one, F_OUT, lambda j: (j["n"], j["kind"], j["i"]))
    else:
        summary()

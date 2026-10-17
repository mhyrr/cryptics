"""Fourth post hoc check (README, "Fourth post hoc check"): T1 and 20 shuffles at fixed offsets, n = 20, separating
offsets that keep T1's end in the scored rows from offsets that leave it out.
Usage (from this folder): python3 -I excess4.py run   -> excess4.jsonl (resumes)
                          python3 -I excess4.py summary
"""
import json, os, random, statistics, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run, setsolve  # noqa: E402

N, SHUF = 20, 20
KEPT, DROPPED = (11, 12, 13, 14, 15), (0, 16, 17, 18, 19)
F_OUT = os.path.join(HERE, "excess4.jsonl")


def jobs():
    sh, sr = random.Random("18w-shuffle"), random.Random("18w-solver")
    out = []
    for s in range(SHUF + 1):
        ss = sh.randrange(1 << 30) if s else None
        for a in KEPT + DROPPED:
            out.append(dict(text="T1", n=N, s=s, a=a, shuffle_seed=ss, solver_seed=sr.randrange(1 << 30)))
    return out


def one(j):
    t = list(run.telegram("T1"))
    if j["s"]:
        random.Random(j["shuffle_seed"]).shuffle(t)
    sc, o = setsolve.solve("".join(t), j["n"], j["a"], j["solver_seed"])
    return dict(j, score=round(sc, 4), dropped=(615 - j["a"]) % j["n"])


def summary():
    R = [json.loads(l) for l in open(F_OUT)]
    def mean(s, offs): return statistics.fmean(r["score"] for r in R if r["s"] == s and r["a"] in offs)
    for label, offs in (("end kept (a 11-15)", KEPT), ("end dropped (a 0, 16-19)", DROPPED)):
        t = mean(0, offs); v = sorted(mean(s, offs) for s in range(1, SHUF + 1))
        print(f"{label}: T1 {t:.3f}; shuffles median {statistics.median(v):.3f}, 5th {v[0]:.3f}, 95th {v[-2]:.3f}, "
              f"max {v[-1]:.3f}; T1 above {sum(x < t for x in v)}/{SHUF}; excess {t - statistics.fmean(v):+.3f}")


if __name__ == "__main__":
    if sys.argv[1] == "run":
        run.run_jobs(jobs(), one, F_OUT, lambda j: (j["s"], j["a"]))
    else:
        summary()

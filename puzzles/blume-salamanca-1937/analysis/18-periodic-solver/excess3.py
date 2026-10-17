"""Third post hoc check (README, "Third post hoc check"): T1[0:595] against 20 shuffles of its own letters, n = 20.
Usage (from this folder): python3 -I excess3.py run   -> excess3.jsonl (resumes)
                          python3 -I excess3.py summary
"""
import json, os, random, statistics, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run, setsolve  # noqa: E402

N, SHUF, CUT = 20, 20, 20
F_OUT = os.path.join(HERE, "excess3.jsonl")


def jobs():
    sh, sr = random.Random("18z-shuffle"), random.Random("18z-solver")
    return [dict(text="T1", n=N, s=s, shuffle_seed=sh.randrange(1 << 30) if s else None,
                 solver_seed=sr.randrange(1 << 30)) for s in range(SHUF + 1)]


def one(j):
    body = list(run.telegram("T1")[:615 - CUT])
    if j["s"]:
        random.Random(j["shuffle_seed"]).shuffle(body)
    s, a, o = setsolve.solve_scan("".join(body), j["n"], j["solver_seed"])
    return dict(j, score=round(s, 4), a=a, dropped=(len(body) - a) % j["n"])


def summary():
    R = {r["s"]: r for r in map(json.loads, open(F_OUT))}
    t = R[0]["score"]; v = sorted(R[s]["score"] for s in range(1, SHUF + 1))
    print(f"T1[0:{615 - CUT}] at n = {N}: {t:.3f} (offset {R[0]['a']}, {R[0]['dropped']} end letters unscored)")
    print(f"own shuffles ({SHUF}): " + " ".join(f"{x:.3f}" for x in v))
    print(f"median {statistics.median(v):.3f}, 5th {v[0]:.3f}, 95th {v[-2]:.3f}; T1 body above {sum(x < t for x in v)}/{SHUF}; "
          f"excess over shuffle mean {t - statistics.fmean(v):+.3f}")


if __name__ == "__main__":
    if sys.argv[1] == "run":
        run.run_jobs(jobs(), one, F_OUT, lambda j: (j["s"],))
    else:
        summary()

"""Second post hoc check (README, "Second post hoc check"): excess of a K1 plant over shuffles of its own letters,
against T1's excess over its own shuffles, at n = 20. Same solver and offset scan as run.py.
Usage (from this folder): python3 -I excess2.py run   -> excess2.jsonl (resumes)
                          python3 -I excess2.py summary
"""
import json, os, random, statistics, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run, setsolve  # noqa: E402  (run puts 01-solver on sys.path and makes it the working directory)
import plaintext, transpo  # noqa: E402

N, PLANTS, SHUF = 20, 20, 3
F_OUT = os.path.join(HERE, "excess2.jsonl")


def jobs():
    pl, sh, sr = random.Random("18y-plant"), random.Random("18y-shuffle"), random.Random("18y-solver")
    out = []
    for i in range(PLANTS):
        ps = pl.randrange(1 << 30)
        for s in range(SHUF + 1):  # s = 0: the plant itself; s >= 1: a shuffle of its letters
            out.append(dict(text="T1", n=N, i=i, s=s, plant_seed=ps, shuffle_seed=sh.randrange(1 << 30) if s else None,
                            solver_seed=sr.randrange(1 << 30)))
    return out


def one(j):
    rnd = random.Random(j["plant_seed"])
    w1, w2 = rnd.randint(16, 25), rnd.randint(16, 25)
    k1, k2 = rnd.sample(range(w1), w1), rnd.sample(range(w2), w2)
    ct = transpo.double_enc(plaintext.telegram(615, rnd), k1, k2, "CC")
    if j["s"]:
        letters = list(ct); random.Random(j["shuffle_seed"]).shuffle(letters); ct = "".join(letters)
    s, a, o = setsolve.solve_scan(ct, j["n"], j["solver_seed"])
    return dict(j, w1=w1, w2=w2, score=round(s, 4), a=a)


def summary():
    R = [json.loads(l) for l in open(F_OUT)]
    ex = []
    for i in range(PLANTS):
        rs = {r["s"]: r for r in R if r["i"] == i}
        ex.append((rs[0]["score"] - statistics.mean(rs[s]["score"] for s in range(1, SHUF + 1)), rs[0]["w1"], rs[0]["w2"]))
    E = [json.loads(l) for l in open(os.path.join(HERE, "excess.jsonl"))]
    sh = [e["score"] for e in E if e["n"] == N and e["kind"] == "shuffle"]
    t1 = [json.loads(l) for l in open(run.F_TARGET) if json.loads(l)["text"] == "T1" and json.loads(l)["n"] == N][0]
    t1x = t1["score"] - statistics.mean(sh)
    v = sorted(e[0] for e in ex)
    print(f"T1 excess at n = {N}: {t1x:+.3f} (target {t1['score']:.3f}, mean of {len(sh)} own shuffles {statistics.mean(sh):.3f})")
    print(f"K1 plant excesses ({PLANTS}, sorted): " + " ".join(f"{x:+.3f}" for x in v))
    print(f"K1 5th pct {v[1]:+.3f}, median {v[10]:+.3f}, 95th pct {v[18]:+.3f}; T1 above {sum(x < t1x for x in v)}/{PLANTS}")
    print("per plant (excess, w1, w2): " + ", ".join(f"{x:+.3f} {a}x{b}" for x, a, b in ex))


if __name__ == "__main__":
    if sys.argv[1] == "run":
        run.run_jobs(jobs(), one, F_OUT, lambda j: (j["i"], j["s"]))
    else:
        summary()

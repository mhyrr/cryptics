"""Development runs of the offset scan (setsolve.solve_scan), before the plan is frozen. Seed stream
"18-devscan" only. Plants: 615 letters = p random letters + body + b random letters, p and b in 0-20.
Usage: python3 -I dev_scan.py N[,N...] PLANTS
"""
import os, random, sys, time
from concurrent.futures import ProcessPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import setsolve  # noqa: E402
sys.path.insert(0, os.path.join(HERE, "..", "01-solver")); os.chdir(os.path.join(HERE, "..", "01-solver"))
import plaintext  # noqa: E402
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def one(job):
    n, fam, pseed, sseed = job
    rnd = random.Random(pseed); k = rnd.sample(range(n), n)
    p, b = rnd.randint(0, 20), rnd.randint(0, 20)
    body = plaintext.telegram(615 - p - b, rnd)
    ct, idx = setsolve.plant(body, k, fam, rnd, "".join(rnd.choice(AZ) for _ in range(p)),
                             "".join(rnd.choice(AZ) for _ in range(b)))
    t = time.time(); s, a, o = setsolve.solve_scan(ct, n, sseed); dt = time.time() - t
    true = [k.index(x) for x in range(n)]
    ts = setsolve.qrows(setsolve.columns(ct, n, p % n), true)
    return n, fam, p, b, a, setsolve.adjacency_acc(idx, o, a), s, ts, dt


def main():
    ns = [int(x) for x in sys.argv[1].split(",")]; per = int(sys.argv[2])
    pr, sr = random.Random("18-devscan-plant"), random.Random("18-devscan-solver")
    jobs = [(n, fam, pr.randrange(1 << 30), sr.randrange(1 << 30)) for n in ns for fam in ("sets", "nihilist")
            for _ in range(per)]
    with ProcessPoolExecutor(3) as ex:
        for n, fam, p, b, a, acc, s, ts, dt in ex.map(one, jobs):
            print(f"n {n:3d} {fam:8s} p {p:2d} b {b:2d} a {a:2d} (p%n {p % n:2d}) adj {acc:.2f} "
                  f"score {s:.3f} true {ts:.3f} {dt:6.1f}s", flush=True)


if __name__ == "__main__":
    main()

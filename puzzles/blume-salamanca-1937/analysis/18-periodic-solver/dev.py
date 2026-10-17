"""Development runs for setsolve.py, before the plan is frozen. Seed stream "18-dev" only; never used again.
Not controls: these runs choose the solver's parameters. Usage: python3 -I dev.py N[,N...] PLANTS [key=value ...]
"""
import os, random, sys, time
from concurrent.futures import ProcessPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import setsolve  # noqa: E402
sys.path.insert(0, os.path.join(HERE, "..", "01-solver")); os.chdir(os.path.join(HERE, "..", "01-solver"))
import plaintext  # noqa: E402
from control import shift_acc  # noqa: E402  (cyclic shift up to 40, as the 01 controls)


def one(job):
    n, fam, pseed, sseed, L, kw = job
    rnd = random.Random(pseed); k = rnd.sample(range(n), n); pt = plaintext.telegram(L, rnd)
    ct = setsolve.enc_sets(pt, k) if fam == "sets" else setsolve.enc_nihilist_rows(pt, k, rnd)
    true = [k.index(t) for t in range(n)]
    t = time.time(); s, o = setsolve.solve(ct, n, 0, sseed, **kw); dt = time.time() - t
    # letters in place: decrypted rows put in plaintext row order (the true key's rows say which is which)
    rows_true, rows_got = setsolve.dec_rows(ct, true), setsolve.dec_rows(ct, o)
    by = sorted(range(len(rows_true)), key=lambda i: pt.index(rows_true[i]) if fam != "sets" else i)
    acc = shift_acc("".join(rows_got[i] for i in by), "".join(rows_true[i] for i in by))
    return n, fam, acc, s, setsolve.qrows(setsolve.columns(ct, n, 0), true), dt


def main():
    ns = [int(x) for x in sys.argv[1].split(",")]; per = int(sys.argv[2])
    kw = {a.split("=")[0]: float(a.split("=")[1]) if "." in a else int(a.split("=")[1]) for a in sys.argv[3:]}
    pr, sr = random.Random("18-dev-plant"), random.Random("18-dev-solver")
    jobs = [(n, fam, pr.randrange(1 << 30), sr.randrange(1 << 30), 615, kw)
            for n in ns for fam in ("sets", "nihilist") for _ in range(per)]
    with ProcessPoolExecutor(3) as ex:
        for n, fam, acc, s, ts, dt in ex.map(one, jobs):
            print(f"n {n:3d} {fam:8s} acc {acc:.2f} score {s:.3f} true {ts:.3f} {dt:6.1f}s", flush=True)


if __name__ == "__main__":
    main()

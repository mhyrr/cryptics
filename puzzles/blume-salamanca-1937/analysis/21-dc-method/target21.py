"""Target run of 21-dc-method (README, "Target run"): forward CC on telegram 1 at full length, w1 2-15 x w2 16-17,
exactly control A's method and budget, with the binary the controls used (out/dcm, SHA-256 in dcm_ctlA.sha256,
source dcm_ctlA.c).
Usage (from this folder): python3 -I target21.py run [WORKERS]   -> results/target21.jsonl (resumes)
                          python3 -I target21.py summary
"""
import hashlib, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from run21 import stream  # noqa: E402

DCM = os.path.join(HERE, "out", "dcm")
CT = os.path.join(HERE, "out", "t1_615.txt")  # written from sources/telegram-1.txt by check_inputs
OUT = os.path.join(HERE, "results", "target21.jsonl")
THRESHOLD = -5.10
ARGS = ["budget=50000000", "climb=1", "idp=1", "k1climb=0"]
PAIRS = [(w1, w2) for w2 in (16, 17) for w1 in range(2, 16)]


def check_inputs():
    want = open(os.path.join(HERE, "dcm_ctlA.sha256")).read().split()[0]
    got = hashlib.sha256(open(DCM, "rb").read()).hexdigest()
    assert got == want, "out/dcm is not the binary the controls used"
    src = "".join(c for c in open(os.path.join(HERE, "../../sources/telegram-1.txt")).read().upper() if c.isalpha())
    assert len(src) == 615 and hashlib.sha256(src.encode()).hexdigest().startswith("e266615d"), "telegram 1 changed"
    open(CT, "w").write(src)


def one(pair):
    w1, w2 = pair
    seed = stream("solver", "target21", f"{w1}x{w2}")
    args = [DCM, "solve", CT, f"w1={w1}", f"w2={w2}", "lang=es", f"seed={seed}"] + ARGS
    out = subprocess.run(args, capture_output=True, text=True, cwd=HERE)
    lines = [l for l in out.stdout.strip().splitlines() if l.startswith("{")]
    if out.returncode != 0 or not lines:
        raise RuntimeError(f"{args}: rc={out.returncode} {out.stderr[-500:]}")
    fin = json.loads(lines[-1])
    return dict(w1=w1, w2=w2, seed=seed, args=ARGS, **{k: fin[k] for k in ("t", "cpu", "n_idp", "idp", "score", "k1", "k2", "pt")})


def run(workers):
    check_inputs()
    done = {(r["w1"], r["w2"]) for r in map(json.loads, open(OUT))} if os.path.exists(OUT) else set()
    todo = [p for p in PAIRS if p not in done]
    print(f"{len(todo)} to run, {len(done)} done", flush=True)
    with ThreadPoolExecutor(workers) as ex, open(OUT, "a") as f:
        for fu in as_completed([ex.submit(one, p) for p in todo]):
            r = fu.result(); f.write(json.dumps(r) + "\n"); f.flush()
            print(f"{r['w1']}x{r['w2']} score={r['score']:.4f} cpu={r['cpu']}", flush=True)


def summary():
    R = sorted(map(json.loads, open(OUT)), key=lambda r: (r["w2"], r["w1"]))
    print(f"{len(R)}/{len(PAIRS)} pairs; threshold {THRESHOLD}")
    print("| w1 × w2 | score | margin | first 60 letters |\n|---|---|---|---|")
    for r in R:
        print(f"| {r['w1']} × {r['w2']} | {r['score']:.4f} | {r['score'] - THRESHOLD:+.3f} | {r['pt'][:60]} |")
    best = max(R, key=lambda r: r["score"])
    print(f"\nbest {best['score']:.4f} at {best['w1']} × {best['w2']}; candidates above threshold: "
          f"{sum(r['score'] > THRESHOLD for r in R)}")


if __name__ == "__main__":
    if sys.argv[1] == "run":
        run(int(sys.argv[2]) if len(sys.argv) > 2 else 3)
    else:
        summary()

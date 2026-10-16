"""Target run: the 01-solver engine on the real telegram(s), every (w1, w2) pair in a frozen region,
with the same per-pair budget as the passing controls.

Usage: python3 target.py TAG CONV LANG SECONDS WORKERS W1RANGE W2RANGE SEEDS [JOINT]
  e.g. python3 target.py h1_cc CC es 180 8 2-15 12-15 1
  JOINT=1 adds telegram 2 under the same keys (H2).
Writes out/TAG.jsonl (all runs, with best decryption) and prints one line per run.
"""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
here = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(here, "../01-solver")
T1 = os.path.join(here, "../../sources/telegram-1.txt")
T2 = os.path.join(here, "../../sources/telegram-2.txt")

def rng(s):
    a, _, b = s.partition("-"); return range(int(a), int(b or a) + 1)

def run(job):
    w1, w2, seed, conv, lang, secs, joint = job
    args = ["out/dtsolve", "solve", T1, str(w1), str(w2), conv, lang, str(seed), str(secs), "-"]
    if joint:
        args.append(T2)
    out = subprocess.run(args, capture_output=True, text=True, cwd=SOLVER).stdout.strip().splitlines()
    fin = json.loads(out[-1])
    return {"w1": w1, "w2": w2, "seed": seed, "conv": conv, "lang": lang, "secs": secs, "joint": joint,
            "score": fin["score"], "idp": fin["idp"], "iters": fin["iter"], "k1": fin["k1"], "k2": fin["k2"], "pt": fin["pt"]}

def main():
    tag, conv, lang, secs, workers, r1, r2, seeds = sys.argv[1:9]
    joint = len(sys.argv) > 9 and sys.argv[9] == "1"
    jobs = [(w1, w2, 1000 + s, conv, lang, int(secs), joint)
            for w1 in rng(r1) for w2 in rng(r2) for s in range(int(seeds))]
    os.makedirs(os.path.join(here, "out"), exist_ok=True)
    with open(os.path.join(here, f"out/{tag}.jsonl"), "w") as f, ThreadPoolExecutor(int(workers)) as ex:
        for r in ex.map(run, jobs):
            f.write(json.dumps(r) + "\n"); f.flush()
            print(f"{r['w1']}x{r['w2']} {conv} score={r['score']:.3f} {r['pt'][:60]}", flush=True)

if __name__ == "__main__":
    main()

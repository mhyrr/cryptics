"""Is T1[0:600]'s lead at w1 = 15 (best runs, 15 x 15 at -5.94) a property of the complete rectangle?

Step B's six best runs all fall on T1[0:600] with w1 = 15 (600 = 15 x 40). This runs dtsolve, unchanged, at
15 x 15 and 30 s on three letter shuffles of T1[0:600] (seeds from their own stream, "17-noise-600").
Reading, fixed before the run (main thread, 2026-10-17): if the shuffles score within 0.05 of -5.94 or above,
the pattern is the solver on a complete rectangle; if all three score below -6.10, T1[0:600] at 15 x 15 holds a
little more order than shuffled letters (a weak lead, still 0.84 below the -5.10 threshold).
Usage (from this folder): python3 -I noise_600.py > noise_600.txt
"""
import json, os, random, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(HERE, "..", "01-solver")
os.chdir(SOLVER)
T1 = "".join(c for c in open(os.path.join(HERE, "..", "..", "sources", "telegram-1.txt")).read().upper() if c.isalpha())
body = T1[:600]
os.makedirs(os.path.join(HERE, "out"), exist_ok=True)

def run(i):
    rnd = random.Random(f"17-noise-600-{i}")
    s = list(body); rnd.shuffle(s)
    path = os.path.join(HERE, "out", f"noise600_{i}.txt"); open(path, "w").write("".join(s))
    seed = rnd.randrange(10 ** 9)
    out = subprocess.run(["out/dtsolve", "solve", path, "15", "15", "CC", "es", str(seed), "30"],
                         capture_output=True, text=True).stdout.strip().splitlines()
    return i, seed, json.loads(out[-1])["score"]

with ThreadPoolExecutor(3) as ex:
    res = sorted(ex.map(run, range(3)))
for i, seed, score in res:
    print(f"shuffle {i}: solver seed {seed}, best score {score:.3f}")
print(f"target T1[0:600] at 15 x 15: -5.940 (step B); max shuffle {max(r[2] for r in res):.3f}")

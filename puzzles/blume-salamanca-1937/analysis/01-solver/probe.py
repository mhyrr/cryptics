"""Fitness-distance probe on a planted control: is the IDP selective, and does the climb reach it?
Usage: python3 probe.py W1 W2 SEED [N] [LANG] [STYLE]"""
import os, random, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import transpo, plaintext
w1, w2, seed = map(int, sys.argv[1:4]); n = int(sys.argv[4]) if len(sys.argv) > 4 else 615
lang = sys.argv[5] if len(sys.argv) > 5 else "es"; style = sys.argv[6] if len(sys.argv) > 6 else "telegraph"
rnd = random.Random(seed); pt = plaintext.telegram(n, rnd, lang, style)
k1 = rnd.sample(range(w1), w1); k2 = rnd.sample(range(w2), w2)
open(f"out/_probe_{w1}_{w2}_{seed}.txt", "w").write(transpo.double_enc(pt, k1, k2))
print(subprocess.run(["out/dtsolve", "probe", f"out/_probe_{w1}_{w2}_{seed}.txt", ",".join(map(str, k2)), str(w1), "CC", lang, str(seed), "0"],
                     capture_output=True, text=True).stdout)

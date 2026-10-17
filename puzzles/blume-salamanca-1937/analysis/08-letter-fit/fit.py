"""Do the telegrams' letter counts fit telegraph-style Spanish, Italian or Portuguese?
Reference: 40 chunks of 10,000 letters from random points of the held-out corpus (01-solver/plaintext.py),
per language and style, so no one book dominates. Statistic: chi-square
against the reference, with its null from 500 plants of the same length and style. Also per-letter z.
The plants spell stops as PUNTO/STOP/PONTO; X as a stop sign is not modelled (08 is the first look).
Usage (from this folder): python3 -I fit.py > result.txt
"""
import math, os, random, sys
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(here, "..", "01-solver")
sys.path.insert(0, SOLVER); os.chdir(SOLVER)
import plaintext
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    def load(p): return "".join(c for c in open(os.path.join(here, p)).read().upper() if c.isalpha())
    tel = {"T1": load("../../sources/telegram-1.txt"), "T2": load("../../sources/telegram-2.txt")}
    rnd = random.Random(20261016)
    for lang in ("es", "it", "pt"):
        for style in ("telegraph", "prose"):
            ref = Counter()
            for _ in range(40): ref.update(plaintext.telegram(10000, rnd, lang, style))
            N = sum(ref.values())
            f = {c: ref[c] / N for c in AZ}
            chi = lambda t: sum((Counter(t)[x] - len(t) * f[x]) ** 2 / (len(t) * f[x] + 0.5) for x in AZ)
            for name, t in tel.items():
                sims = sorted(chi(plaintext.telegram(len(t), rnd, lang, style)) for _ in range(500))
                o = chi(t); p = (sum(s >= o for s in sims) + 1) / 501; c = Counter(t)
                z = sorted(((c[x] - len(t) * f[x]) / math.sqrt(len(t) * f[x] + 0.5), x) for x in AZ)
                fmt = lambda zs: ", ".join(f"{x} {c[x]} vs {len(t) * f[x]:.0f} (z {v:+.1f})" for v, x in zs)
                print(f"{lang} {style:9} {name}: chi2 {o:.0f} (plants median {sims[250]:.0f}), p = {p:.3f}")
                print(f"    over: {fmt(z[:-4:-1])}\n    under: {fmt(z[:3])}")

if __name__ == "__main__":
    main()

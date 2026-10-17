"""A1-A3: is there a window, or an end of the telegram, where rare letters concentrate beyond what the letter
counts allow? And is the shuffle null fair for a transposition?

A1  For each window length l in L, the max over all starts of the window's summed surprisal (equivalent to
    the mean, l fixed). p per l from 10,000 shuffles (letter counts fixed). Scan statistic = min-p over l,
    calibrated with the same shuffles.
A2  Summed surprisal of the first g and the last g groups, g = 1-4 (8 statistics), each against the
    shuffles; min-p over the 8, calibrated the same way.
A3  Plants: Spanish telegraph plaintext, letter convention 'stop' (stop word replaced by the letter) or
    'fill' (1-4 of the letter appended before transposition), enciphered by single columnar (5-45) or
    double columnar (8-25). Each plant gets its own calibrated A1 and A2 p from K = 1,000 shuffles, drawn
    from a fixed bank of 4,000 random permutations. Reports how often plants reach the target's p.

Usage (from this folder): python3 -I scan.py > result-scan.txt   (about 8 minutes of CPU)
Per-plant rows go to out/a3_plants.jsonl (gitignored).
"""
import json, os, random, sys, time
from itertools import accumulate, islice
from operator import itemgetter, sub
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script folder
from common import HERE, TEL, Null, plant, surprisal

L = (5, 10, 15, 20, 25, 30, 40, 50, 60)
G = (1, 2, 3, 4)
NAMES = [f"scan l={l}" for l in L] + [f"first {g}" for g in G] + [f"last {g}" for g in G]
GROUPS = {"A1": list(range(len(L))), "A2": list(range(len(L), len(L) + 2 * len(G)))}
N_SHUF, N_PLANT, K_PLANT, BANK = 10000, 500, 1000, 4000


def stats(v):
    P = list(accumulate(v, initial=0))
    n = len(v)
    out = [max(map(sub, islice(P, l, None), P)) for l in L]
    out += [P[5 * g] for g in G]
    out += [P[n] - P[n - 5 * g] for g in G]
    return out


def best_starts(v, l):
    P = list(accumulate(v, initial=0))
    sums = [P[i + l] - P[i] for i in range(len(v) - l + 1)]
    m = max(sums)
    return m, [i for i, x in enumerate(sums) if x == m]


def main():
    t0 = time.process_time()
    ref, s, si = surprisal()
    N = sum(ref.values())
    print("# 09-odd-positions / scan.py (A1-A3)")
    print(f"Reference: 40 x 10,000 letters Spanish telegraph style, N = {N}; floor +1 per letter.")
    print("Surprisal s(c) = -log10 p(c), rarest first:")
    print("  " + "  ".join(f"{c} {s[c]:.2f}" for c in sorted(s, key=lambda c: -s[c])[:12]))
    print("  common: " + "  ".join(f"{c} {s[c]:.2f}" for c in "EAOSNR"))

    target = {}
    for name in ("T1", "T2"):
        t = TEL[name]
        n = len(t)
        v = [si[c] for c in t]
        obs = stats(v)
        rnd = random.Random(9001 if name == "T1" else 9002)
        w, rows = v[:], []
        for _ in range(N_SHUF):
            rnd.shuffle(w)
            rows.append(stats(w))
        null = Null(rows, GROUPS)
        ps, cal = null.cal(obs)
        target[name] = cal
        print(f"\n## {name} ({n} letters), {N_SHUF} shuffles")
        print(f"  mean surprisal of the whole text {sum(v) / n / 1000:.3f}")
        print("  A1 scan: l, max window mean, p, best start(s), window")
        for i, l in enumerate(L):
            m, st = best_starts(v, l)
            assert m == obs[i]
            win = t[st[0]:st[0] + l]
            more = f" (+{len(st) - 1} tied)" if len(st) > 1 else ""
            print(f"    l={l:2}: {m / l / 1000:.3f}  p = {ps[i]:.4f}  start {st[0]}{more}  {win}")
        ib = min(GROUPS["A1"], key=lambda i: ps[i])
        print(f"  A1 min-p over l = {cal['A1'][0]:.4f} at l={L[ib]}; calibrated p = {cal['A1'][1]:.4f}")
        print("  A2 ends: window, mean surprisal, p, letters")
        for j, g in enumerate(G):
            i = len(L) + j
            print(f"    first {g}: {obs[i] / (5 * g) / 1000:.3f}  p = {ps[i]:.4f}  {t[:5 * g]}")
        for j, g in enumerate(G):
            i = len(L) + len(G) + j
            print(f"    last  {g}: {obs[i] / (5 * g) / 1000:.3f}  p = {ps[i]:.4f}  {t[n - 5 * g:]}")
        ib = min(GROUPS["A2"], key=lambda i: ps[i])
        print(f"  A2 min-p over 8 = {cal['A2'][0]:.4f} at '{NAMES[ib]}'; calibrated p = {cal['A2'][1]:.4f}")
        sys.stderr.write(f"{name} target done {time.process_time() - t0:.0f}s\n")

    # A3: plants, each calibrated against its own shuffles (K_PLANT drawn from a fixed permutation bank)
    print("\n## A3: plants (each with its own calibrated p from 1,000 shuffles)")
    print("cells: length x system x convention x letter; 'reach' = plant calibrated p <= target calibrated p")
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    jl = open(os.path.join(HERE, "out", "a3_plants.jsonl"), "w")
    rnd = random.Random(20261017)
    summary = {}
    for name, letters in (("T1", ("X",)), ("T2", ("X", "F"))):
        n = len(TEL[name])
        bank = []
        for _ in range(BANK):
            perm = list(range(n))
            rnd.shuffle(perm)
            bank.append(itemgetter(*perm))
        # the target with the plant procedure (K = 1,000 from the bank), for a like-for-like comparison
        v = [si[c] for c in TEL[name]]
        _, tcal = Null([stats(bank[k](v)) for k in rnd.sample(range(BANK), K_PLANT)], GROUPS).cal(stats(v))
        print(f"\n{name}: target calibrated p, 10,000 shuffles: A1 {target[name]['A1'][1]:.4f}, "
              f"A2 {target[name]['A2'][1]:.4f}; plant procedure (1,000): A1 {tcal['A1'][1]:.4f}, "
              f"A2 {tcal['A2'][1]:.4f}")
        print(f"  {'cell':28} {'N':>4} {'A1 reach':>9} {'A2 reach':>9} {'A1<=.01':>8} {'A1<=.05':>8} "
              f"{'A2<=.01':>8} {'A2<=.05':>8}")
        pooled = []
        for letter in letters:
            for system in ("single", "double"):
                for conv in ("stop", "fill"):
                    res = []
                    for _ in range(N_PLANT):
                        ct = plant(n, rnd, system, conv, letter)
                        v = [si[c] for c in ct]
                        sub_ = rnd.sample(range(BANK), K_PLANT)
                        _, cal = Null([stats(bank[k](v)) for k in sub_], GROUPS).cal(stats(v))
                        res.append((cal["A1"][1], cal["A2"][1]))
                        jl.write(json.dumps({"tel": name, "letter": letter, "system": system, "conv": conv,
                                             "n_letter": ct.count(letter), "A1": cal["A1"][1],
                                             "A2": cal["A2"][1]}) + "\n")
                    pooled += res
                    cell = f"{name} {system} {conv} {letter}"
                    print("  " + row(cell, res, target[name]))
                    summary[cell] = res
                    sys.stderr.write(f"{cell} done {time.process_time() - t0:.0f}s\n")
        print("  " + row(f"{name} all cells pooled", pooled, target[name]))
    jl.close()
    print(f"\nCPU {time.process_time() - t0:.0f} s")


def row(cell, res, tgt):
    N = len(res)
    f = lambda k, thr: sum(r[k] <= thr for r in res) / N
    return (f"{cell:28} {N:>4} {f(0, tgt['A1'][1]):>9.3f} {f(1, tgt['A2'][1]):>9.3f} "
            f"{f(0, .01):>8.3f} {f(0, .05):>8.3f} {f(1, .01):>8.3f} {f(1, .05):>8.3f}")


if __name__ == "__main__":
    main()

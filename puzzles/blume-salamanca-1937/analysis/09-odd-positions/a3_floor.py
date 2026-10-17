"""A3 at the target's resolution. T1's A2 calibrated p is at the floor of 10,000 shuffles (<= 1/10001), but
plant p's come from 1,000 shuffles (floor 1/1001). This script replays scan.py's seeded plant sequence for T1,
checks the replay against out/a3_plants.jsonl (letter counts for every plant; the A2 p for the plants it
recalibrates), and recalibrates every plant at the 1,000-shuffle A2 floor with 10,000 fresh shuffles, as the
target was. A plant reaches the target if its 10,000-shuffle calibrated A2 p is <= the target's.

Usage (from this folder, after scan.py): python3 -I a3_floor.py > a3-floor.txt   (under 1 minute of CPU)
"""
import json, os, random, sys
from operator import itemgetter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script folder
import scan
from common import HERE, TEL, Null, plant, surprisal

FLOOR = 1 / 1001 + 1e-12


def main():
    _, _, si = surprisal()
    rows = [json.loads(l) for l in open(os.path.join(HERE, "out", "a3_plants.jsonl")) if '"tel": "T1"' in l]
    # the target, exactly as scan.py computes it (seed 9001, 10,000 shuffles)
    t = TEL["T1"]
    v = [si[c] for c in t]
    rnd_t, w, nrows = random.Random(9001), v[:], []
    for _ in range(scan.N_SHUF):
        rnd_t.shuffle(w)
        nrows.append(scan.stats(w))
    target = Null(nrows, scan.GROUPS).cal(scan.stats(v))[1]["A2"][1]
    # replay scan.py's A3 random stream for T1
    rnd, n = random.Random(20261017), len(t)
    bank = []
    for _ in range(scan.BANK):
        perm = list(range(n))
        rnd.shuffle(perm)
        bank.append(itemgetter(*perm))
    rnd.sample(range(scan.BANK), scan.K_PLANT)
    fresh = random.Random(9101)
    i, hits, at_floor = 0, [], 0
    for letter in ("X",):
        for system in ("single", "double"):
            for conv in ("stop", "fill"):
                for _ in range(scan.N_PLANT):
                    ct = plant(n, rnd, system, conv, letter)
                    sub_ = rnd.sample(range(scan.BANK), scan.K_PLANT)
                    r = rows[i]; i += 1
                    assert (r["system"], r["conv"], r["n_letter"]) == (system, conv, ct.count(letter)), r
                    if r["A2"] > FLOOR:
                        continue
                    at_floor += 1
                    pv = [si[c] for c in ct]
                    a2 = Null([scan.stats(bank[k](pv)) for k in sub_], scan.GROUPS).cal(scan.stats(pv))[1]["A2"][1]
                    assert abs(a2 - r["A2"]) < 1e-12, (a2, r["A2"])  # replay matches the stored row
                    ww, frows = pv[:], []
                    for _ in range(scan.N_SHUF):
                        fresh.shuffle(ww)
                        frows.append(scan.stats(ww))
                    p10 = Null(frows, scan.GROUPS).cal(scan.stats(pv))[1]["A2"][1]
                    hits.append((system, conv, ct.count(letter), p10))
    assert i == len(rows)
    print("# A3 at the target's resolution (T1, A2 end statistic)")
    print(f"target A2 calibrated p (10,000 shuffles) = {target:.5f}")
    print(f"plants replayed: {i}; at the 1,000-shuffle floor: {at_floor}")
    print("recalibrated with 10,000 fresh shuffles (system, convention, X count, calibrated p):")
    for h in sorted(hits, key=lambda h: h[3]):
        print(f"  {h[0]:6} {h[1]:4}  X={h[2]:2}  p = {h[3]:.5f}" + ("   <= target" if h[3] <= target + 1e-12 else ""))
    k = sum(h[3] <= target + 1e-12 for h in hits)
    print(f"plants reaching the target: {k} of {i} = {k / i:.4f}")


if __name__ == "__main__":
    main()

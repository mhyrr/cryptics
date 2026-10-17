"""A4-A5: do the odd letters sit at regular places (residues, gaps, ends), and which mechanism reproduces
their placement?

Positional statistics of one letter's positions (count c), all integers:
  residue  per modulus m: sum of squared residue counts. Monotone in chi-square against uniform for fixed
           m and c (chi2 = m/c * sumsq - c); every modulus divides the length, so uniform is exact.
  end      count of the letter in the first g and the last g groups, g = 1-4 (8 statistics).
  scan     max count of the letter in any window of length l, l in 5-60 as in A1 (9 statistics). Not in
           the brief: added because the end cluster was seen first, so the honest X-only test must also
           search every place, not only the ends.
A4  min-p over moduli (and over the 8 end windows, and over the 9 scan lengths), each calibrated by placing
    c letters at random positions, 50,000 trials per (length, c). The brief asked for 10,000; the first run
    used 10,000 and put the T1 end p on 4 null events, so the count was raised (same method).
A5  Plant mechanisms at the target length (letter X at 615, F at 160), 1,000 plants each, and report the
    fraction whose calibrated p is at least as extreme (<=) as the target's:
      a-*        stop word replaced by the letter, then single (5-45) or double (8-25) columnar
      b-every-k  c nulls after transposition at o, o+k, ..., k 5-120 (as far as c nulls fit), o random
      b-grp-last c nulls after transposition at the last letter of every q-th group, start random
      b-grp-pos  as b-grp-last, but at a random fixed position (1-5) inside the group (not in the brief;
                 added because T2's F lean to group position 3)
      c-before-* 1-4 of the letter appended to the plaintext before transposition (table fillers)
      c-after    1-4 of the letter appended after single columnar transposition (completing the last group)
    The body is Spanish telegraph plaintext (PUNTO stops unless the letter is the stop). The statistic is
    computed on every occurrence of the letter in the plant, nulls and natural ones, because that is all
    the target shows.

Usage (from this folder): python3 -I residues.py > result-residues.txt   (about 3 minutes of CPU)
"""
import os, random, sys, time
from bisect import bisect_left
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script folder
from common import TEL, Null, encipher, plant, spanish

MODS = {615: (3, 5, 15, 41, 123, 205), 160: (2, 4, 5, 8, 10, 16, 20, 32, 40, 80)}
G = (1, 2, 3, 4)
L = (5, 10, 15, 20, 25, 30, 40, 50, 60)
N_PLACE, N_MECH = 50000, 1000
_cache = {}


def groups(n):
    k = len(MODS[n])
    e = k + 2 * len(G)
    return {"A4": list(range(k)), "end": list(range(k, e)), "scan": list(range(e, e + len(L)))}


def pos_stats(pos, n):
    out = []
    for m in MODS[n]:
        cnt = [0] * m
        for p in pos:
            cnt[p % m] += 1
        out.append(sum(x * x for x in cnt))
    out += [sum(p < 5 * g for p in pos) for g in G]
    out += [sum(p >= n - 5 * g for p in pos) for g in G]
    sp = sorted(pos)  # a best window can always start at a letter; truncating at the end loses nothing
    out += [max(bisect_left(sp, p + l) - i for i, p in enumerate(sp)) for l in L]
    return out


def null(n, c):
    if (n, c) not in _cache:
        rnd = random.Random(100000 * n + c)
        rows = [pos_stats(rnd.sample(range(n), c), n) for _ in range(N_PLACE)]
        _cache[(n, c)] = Null(rows, groups(n))
    return _cache[(n, c)]


def calibrated(text, letter):
    pos = [i for i, ch in enumerate(text) if ch == letter]
    if len(pos) < 1:
        return pos, None, {"A4": (1.0, 1.0), "end": (1.0, 1.0), "scan": (1.0, 1.0)}
    ps, cal = null(len(text), len(pos)).cal(pos_stats(pos, len(text)))
    return pos, ps, cal


def insert_nulls(body, pos, letter, n):
    ps, it = set(pos), iter(body)
    return "".join(letter if i in ps else next(it) for i in range(n))


def mechanism(name, n, rnd, letter, m):
    """One plant of length n; m = the target's count of the letter (nulls planted for b-*)."""
    if name.startswith("a-"):
        return plant(n, rnd, name[2:], "stop", letter)
    if name.startswith("c-before-"):
        return plant(n, rnd, name[9:], "fill", letter)
    if name == "c-after":
        f = rnd.randint(1, 4)
        return encipher(spanish(n - f, rnd), rnd, "single") + letter * f
    if name == "b-every-k":
        k = rnd.randint(5, min(120, (n - 1) // (m - 1)))
        o = rnd.randint(0, n - 1 - (m - 1) * k)
        pos = [o + j * k for j in range(m)]
    else:
        ng = n // 5
        q = rnd.randint(1, (ng - 1) // (m - 1))
        g0 = rnd.randint(0, ng - 1 - (m - 1) * q)
        r = 4 if name == "b-grp-last" else rnd.randint(0, 4)
        pos = [5 * (g0 + j * q) + r for j in range(m)]
    return insert_nulls(encipher(spanish(n - m, rnd), rnd, "single"), pos, letter, n)


MECHS = ("a-single", "a-double", "b-every-k", "b-grp-last", "b-grp-pos", "c-before-single",
         "c-before-double", "c-after")


def report_target(label, text, letter):
    n = len(text)
    pos, ps, cal = calibrated(text, letter)
    c = len(pos)
    print(f"\n### {label}: {letter} in {n} letters, c = {c}")
    print(f"  positions {pos}")
    print(f"  gaps {[b - a for a, b in zip(pos, pos[1:])]}")
    print(f"  group:position (1-based) {[f'{p // 5 + 1}:{p % 5 + 1}' for p in pos]}")
    if c < 2:
        print("  fewer than 2 positions; residues undefined")
        return cal
    k = len(MODS[n])
    for i, m in enumerate(MODS[n]):
        res = sorted(p % m for p in pos)
        chi = m / c * pos_stats(pos, n)[i] - c
        print(f"  mod {m:3}: residues {res}  chi2 {chi:6.1f}  p = {ps[i]:.4f}")
    print(f"  A4 min-p over moduli = {cal['A4'][0]:.4f}; calibrated p = {cal['A4'][1]:.4f}")
    st = pos_stats(pos, n)
    print("  ends: " + "  ".join(f"first {g}: {st[k + j]} (p {ps[k + j]:.3f})" for j, g in enumerate(G)))
    print("        " + "  ".join(f"last {g}: {st[k + 4 + j]} (p {ps[k + 4 + j]:.3f})" for j, g in enumerate(G)))
    print(f"  end min-p over 8 = {cal['end'][0]:.4f}; calibrated p = {cal['end'][1]:.4f}")
    e = k + 2 * len(G)
    for j, l in enumerate(L):
        best = max(range(c), key=lambda i: sum(pos[i] <= q < pos[i] + l for q in pos))
        print(f"  scan l={l:2}: max {st[e + j]} in one window (first at {pos[best]}-{pos[best] + l - 1}), "
              f"p = {ps[e + j]:.4f}")
    ib = min(range(len(L)), key=lambda j: ps[e + j])
    print(f"  scan min-p over l = {cal['scan'][0]:.4f} at l={L[ib]}; calibrated p = {cal['scan'][1]:.4f}")
    return cal


def main():
    t0 = time.process_time()
    print("# 09-odd-positions / residues.py (A4-A5)")
    print(f"Calibration: {N_PLACE} random placements of the same count, per (length, count).")
    print("\n## A4: primary (pre-registered)")
    tgt = {"T1": report_target("T1", TEL["T1"], "X"), "T2": report_target("T2", TEL["T2"], "F")}
    print("\n## A4: secondary (not pre-registered; for context only)")
    report_target("T1", TEL["T1"], "F")
    report_target("T1", TEL["T1"], "K")
    t1 = TEL["T1"]
    merged = "".join("*" if ch in "XKF" else ch for ch in t1)
    report_target("T1 X, K and F together (marked *)", merged, "*")

    print(f"\n## A5: mechanisms, {N_MECH} plants each")
    print("'A4 / end / scan reach' = fraction of plants with calibrated p <= the target's; 'both' = A4 and end at once")
    for name, letter in (("T1", "X"), ("T2", "F")):
        n, m = len(TEL[name]), TEL[name].count(letter)
        print(f"\n{name}, letter {letter}: target calibrated p A4 {tgt[name]['A4'][1]:.4f}, "
              f"end {tgt[name]['end'][1]:.4f}, scan {tgt[name]['scan'][1]:.4f}; target count {m}")
        print(f"  {'mechanism':16} {'median c':>8} {'A4 reach':>9} {'end reach':>10} {'both':>6} "
              f"{'scan reach':>10} {'A4<=.01':>8} {'A4<=.05':>8} {'end<=.01':>9} {'end<=.05':>9}")
        rnd = random.Random(20261018 + n)
        for mech in MECHS:
            rows = []
            for _ in range(N_MECH):
                ct = mechanism(mech, n, rnd, letter, m)
                assert len(ct) == n
                pos, _, cal = calibrated(ct, letter)
                rows.append((len(pos), cal["A4"][1], cal["end"][1], cal["scan"][1]))
            N = len(rows)
            f = lambda cond: sum(1 for r in rows if cond(r)) / N
            a, e, sc = tgt[name]["A4"][1], tgt[name]["end"][1], tgt[name]["scan"][1]
            med = sorted(r[0] for r in rows)[N // 2]
            print(f"  {mech:16} {med:>8} {f(lambda r: r[1] <= a):>9.3f} {f(lambda r: r[2] <= e):>10.3f} "
                  f"{f(lambda r: r[1] <= a and r[2] <= e):>6.3f} {f(lambda r: r[3] <= sc):>10.3f} "
                  f"{f(lambda r: r[1] <= .01):>8.3f} "
                  f"{f(lambda r: r[1] <= .05):>8.3f} {f(lambda r: r[2] <= .01):>9.3f} {f(lambda r: r[2] <= .05):>9.3f}")
            sys.stderr.write(f"{name} {mech} done {time.process_time() - t0:.0f}s\n")
    print(f"\nCPU {time.process_time() - t0:.0f} s")


if __name__ == "__main__":
    main()

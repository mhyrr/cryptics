"""Does a period writing convention explain 08's letter misfits (T1: X high, U low; T2: F high, no X)?
08's method unchanged (40 x 10,000-letter reference, chi-square, 500 plants at the target length, per-letter z),
run once per convention generator (conventions.py). Every generator starts from random.Random(SEED), so g0 must
reproduce 08's "es telegraph" line exactly. Then two more seeds, the Italian/Portuguese check on the two best
Spanish conventions, and the rate sweep.
Usage (from this folder): python3 -I fit.py > result.txt      (raw numbers also go to out/results.json)
"""
import json, math, os, random, re, sys, time
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import conventions as cv
os.chdir(cv.SOLVER)
import plaintext

AZ = cv.AZ
SEED = 20261016
NREF, REFLEN, NPLANT = 40, 10000, 500
ZL = "XFUPMKW"


def load(p):
    return "".join(c for c in open(os.path.join(here, p)).read().upper() if c.isalpha())


def ic(c, n):
    return sum(v * (v - 1) for v in c.values()) / (n * (n - 1))


def pct(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))]


def fit(gen, lang, which, seed, tel):
    rnd = random.Random(seed)
    ref = Counter()
    for _ in range(NREF):
        ref.update(gen(REFLEN, rnd, lang))
    N = sum(ref.values())
    f = {x: ref[x] / N for x in AZ}
    chi = lambda c, n: sum((c[x] - n * f[x]) ** 2 / (n * f[x] + 0.5) for x in AZ)
    res = {"ref_ic": ic(ref, N), "ref_f": f}
    for name in ("T1", "T2"):
        if name not in which:
            continue
        t = tel[name]; n = len(t); c = Counter(t)
        sims, ics, xs, fs = [], [], [], []
        for _ in range(NPLANT):
            s = gen(n, rnd, lang); cs = Counter(s)
            sims.append(chi(cs, n)); ics.append(ic(cs, n)); xs.append(cs["X"]); fs.append(cs["F"])
        o = chi(c, n)
        z = {x: (c[x] - n * f[x]) / math.sqrt(n * f[x] + 0.5) for x in AZ}
        other = max((x for x in AZ if x not in ZL), key=lambda x: abs(z[x]))
        res[name] = {
            "chi": o, "chi_med": pct(sims, 0.5), "chi_90": pct(sims, 0.9), "p": (sum(s >= o for s in sims) + 1) / (NPLANT + 1),
            "z": z, "other": other, "eX615": 615 * f["X"], "eF160": 160 * f["F"],
            "ic_med": pct(ics, 0.5), "ic_lo": pct(ics, 0.05), "ic_hi": pct(ics, 0.95),
            "pX_ge6": sum(v >= 6 for v in xs) / NPLANT, "pF_ge7": sum(v >= 7 for v in fs) / NPLANT,
            "pX0": sum(v == 0 for v in xs) / NPLANT, "ic_obs": ic(c, n),
            "ic_le": sum(v <= ic(c, n) for v in ics) / NPLANT,
        }
    return res


def verdicts(r):
    t1 = r.get("T1"); t2 = r.get("T2")
    v1 = "yes" if t1 and t1["p"] >= 0.2 and abs(t1["z"]["X"]) < 2 else ("no" if t1 else "–")
    v2 = "yes" if t2 and t2["p"] >= 0.2 and abs(t2["z"]["F"]) < 2 else ("no" if t2 else "–")
    return v1, v2


def checks(tel):
    for s in (1, 2, 3):
        for lang in ("es", "it", "pt"):
            for n in (160, 615, 10000):
                a = plaintext.telegram(n, random.Random(s), lang, "telegraph")
                b = cv.generate(n, random.Random(s), lang)
                assert a == b, f"g0 differs from plaintext.telegram: seed {s} {lang} {n}"
    print("check: g0 == plaintext.telegram for seeds 1-3, es/it/pt, n = 160/615/10000: OK")
    txt = open(os.path.join(here, "../../sources/context-cribs.md")).read()
    lines = txt[txt.index("## 3. Probable words"):].splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("| crib |"))
    words = []
    for l in lines[start + 2:]:          # skip the header and the |---| line; stop at the table's end
        if not l.startswith("|"):
            break
        for w in re.findall(r"\b[A-Z]{2,}\b", l.split("|")[1]):
            if w not in words:
                words.append(w)
    assert words == cv.CRIBS, (words, cv.CRIBS)
    print(f"check: crib list matches the context-cribs section 3 table ({len(words)} words; "
          f"{len(cv.CRIBS_NO_XF)} without X or F): OK")
    for k, t in tel.items():
        c = Counter(t)
        print(f"{k}: n = {len(t)}, IC {ic(c, len(t)):.4f}, X {c['X']}, F {c['F']}, U {c['U']}, P {c['P']}, "
              f"M {c['M']}, K {c['K']}, W {c['W']}")


def tables(R, title):
    print(f"\n## {title}\n")
    print("Fit and pass rule (explains: p >= 0.2 and |z| < 2 for X in T1, F in T2)\n")
    print("| gen | T1 chi2 (plants median) | T1 p | T2 chi2 (plants median) | T2 p | E[X] in 615 | P(X>=6 in 615) "
          "| E[F] in 160 | P(F>=7 in 160) | P(no X in 160) | explains T1 X | explains T2 F |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for g, r in R.items():
        t1, t2 = r.get("T1"), r.get("T2"); v1, v2 = verdicts(r)
        a = f"{t1['chi']:.0f} ({t1['chi_med']:.0f}) | {t1['p']:.3f}" if t1 else "– | –"
        b = f"{t2['chi']:.0f} ({t2['chi_med']:.0f}) | {t2['p']:.3f}" if t2 else "– | –"
        ex = f"{t1['eX615']:.1f} | {t1['pX_ge6']:.3f}" if t1 else f"{615 * r['ref_f']['X']:.1f} | –"
        ef = f"{t2['eF160']:.1f} | {t2['pF_ge7']:.3f} | {t2['pX0']:.3f}" if t2 else "– | – | –"
        print(f"| {g} | {a} | {b} | {ex} | {ef} | {v1} | {v2} |")
    for name in ("T1", "T2"):
        print(f"\nPer-letter z, {name} (observed vs expected)\n")
        print("| gen | " + " | ".join(ZL) + " | largest other |")
        print("|---|" + "---|" * (len(ZL) + 1))
        tc = Counter(TEL[name]); n = len(TEL[name])
        for g, r in R.items():
            t = r.get(name)
            if not t:
                continue
            cells = [f"{t['z'][x]:+.1f} ({tc[x]} vs {n * r['ref_f'][x]:.1f})" for x in ZL]
            o = t["other"]
            print(f"| {g} | " + " | ".join(cells) + f" | {o} {t['z'][o]:+.1f} ({tc[o]} vs {n * r['ref_f'][o]:.1f}) |")
    print("\nIndex of coincidence of the plants (median [5%, 95%]; share of plants with IC <= the telegram's);"
          " T1 0.0695, T2 0.0710\n")
    print("| gen | reference (400k letters) | T1-length plants | T1 share <= 0.0695 | T2-length plants | T2 share <= 0.0710 |")
    print("|---|---|---|---|---|---|")
    for g, r in R.items():
        cell = lambda t: f"{t['ic_med']:.4f} [{t['ic_lo']:.4f}, {t['ic_hi']:.4f}] | {t['ic_le']:.3f}" if t else "– | –"
        print(f"| {g} | {r['ref_ic']:.4f} | {cell(r.get('T1'))} | {cell(r.get('T2'))} |")


def main():
    global TEL
    t0 = time.process_time()
    TEL = tel = {"T1": load("../../sources/telegram-1.txt"), "T2": load("../../sources/telegram-2.txt")}
    print(f"# 10-convention-fit: result (seed {SEED}, {NREF} x {REFLEN} reference, {NPLANT} plants)\n")
    checks(tel)
    allres = {}

    es = {g: fit(gen, "es", w, SEED, tel) for g, (gen, w) in cv.GENERATORS.items()}
    allres["es"] = es
    tables(es, f"Spanish, pre-set parameters, seed {SEED}")

    print("\n## Seed noise: Spanish table at three seeds (T1 p / T2 p; z X in T1, z F in T2)\n")
    print(f"| gen | seed {SEED} | seed {SEED + 1} | seed {SEED + 2} | explains T1 X (3 seeds) | explains T2 F (3 seeds) |")
    print("|---|---|---|---|---|---|")
    seeds = {SEED: es}
    for s in (SEED + 1, SEED + 2):
        seeds[s] = {g: fit(gen, "es", w, s, tel) for g, (gen, w) in cv.GENERATORS.items()}
    allres["es_seeds"] = {str(s): v for s, v in seeds.items() if s != SEED}
    for g in cv.GENERATORS:
        cells, v1s, v2s = [], [], []
        for s in seeds:
            r = seeds[s][g]; t1, t2 = r.get("T1"), r.get("T2")
            a = f"{t1['p']:.3f} ({t1['z']['X']:+.1f})" if t1 else "–"
            b = f"{t2['p']:.3f} ({t2['z']['F']:+.1f})" if t2 else "–"
            cells.append(f"{a} / {b}")
            v1, v2 = verdicts(r); v1s.append(v1); v2s.append(v2)
        print(f"| {g} | " + " | ".join(cells) + f" | {'/'.join(v1s)} | {'/'.join(v2s)} |")

    ranked = sorted((g for g in cv.GENERATORS if g not in ("g0", "g8")),
                    key=lambda g: (min(es[g]["T1"]["p"], es[g]["T2"]["p"]), es[g]["T1"]["p"]), reverse=True)
    best = ranked[:2]
    print(f"\nRanking by min(T1 p, T2 p), seed {SEED}: " +
          ", ".join(f"{g} {min(es[g]['T1']['p'], es[g]['T2']['p']):.3f}" for g in ranked))
    print(f"Two best for the Italian/Portuguese check: {', '.join(best)}")
    for lang in ("it", "pt"):
        R = {g: fit(cv.GENERATORS[g][0], lang, "T1 T2", SEED, tel) for g in ["g0"] + best}
        allres[lang] = R
        tables(R, f"{lang}: baseline and the two best Spanish conventions, seed {SEED}")

    print(f"\n## Rate sweep, Spanish, seed {SEED} (tuned: a pass here is 'possible at a tuned rate' only)\n")
    print("| gen | T1 p | T1 z X | T2 p | T2 z F | E[X] in 615 | P(X>=6 in 615) | E[F] in 160 | P(no X in 160) "
          "| IC T1-length median | explains T1 X | explains T2 F |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    sw = {}
    for name, gen, w in cv.SWEEP:
        r = fit(gen, "es", w, SEED, tel); sw[name] = r
        t1, t2 = r.get("T1"), r.get("T2"); v1, v2 = verdicts(r)
        a = f"{t1['p']:.3f} | {t1['z']['X']:+.1f}" if t1 else "– | –"
        b = f"{t2['p']:.3f} | {t2['z']['F']:+.1f}" if t2 else "– | –"
        ex = f"{t1['eX615']:.1f} | {t1['pX_ge6']:.3f}" if t1 else f"{615 * r['ref_f']['X']:.1f} | –"
        ef = f"{t2['eF160']:.1f} | {t2['pX0']:.3f}" if t2 else "– | –"
        icm = f"{t1['ic_med']:.4f}" if t1 else f"(T2) {t2['ic_med']:.4f}"
        print(f"| {name} | {a} | {b} | {ex} | {ef} | {icm} | {v1} | {v2} |")
    allres["sweep"] = sw
    os.makedirs(os.path.join(here, "out"), exist_ok=True)
    json.dump(allres, open(os.path.join(here, "out", "results.json"), "w"), indent=1)
    print(f"\nCPU {time.process_time() - t0:.0f} s")


if __name__ == "__main__":
    main()

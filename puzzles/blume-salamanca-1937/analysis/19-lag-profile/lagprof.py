"""19-lag-profile: Spanish letter-pair association (PMI) by lag, against own shuffles and K1 plants. Plan: README.md.
Usage (from this folder): python3 -I lagprof.py > result.txt
"""
import array, math, os, random, statistics, sys
from concurrent.futures import ProcessPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(HERE, "..", "01-solver")
sys.path.insert(0, SOLVER); os.chdir(SOLVER)
import plaintext, transpo  # noqa: E402

B2 = array.array("f"); B2.fromfile(open("out/lm_es_2.bin", "rb"), 26 * 26)
P1 = [math.log10(sum(10 ** B2[a * 26 + b] for b in range(26))) for a in range(26)]
PMI = [B2[a * 26 + b] - P1[a] - P1[b] for a in range(26) for b in range(26)]
N_SHUF, N_PLANT, N_PLANT_SHUF = 2000, 200, 200


def load(name):
    t = "".join(c for c in open(os.path.join(HERE, "../../sources", name)).read().upper() if c.isalpha())
    return [ord(c) - 65 for c in t]


def profile(v, dmax):
    return [sum(PMI[a * 26 + b] for a, b in zip(v, v[d:])) / (len(v) - d) for d in range(1, dmax + 1)]


def zstats(G, ref):
    """G: one profile; ref: list of shuffle profiles. Returns the z profile."""
    D = len(G); mu = [statistics.fmean(r[d] for r in ref) for d in range(D)]
    sd = [statistics.pstdev([r[d] for r in ref]) for d in range(D)]
    return [(G[d] - mu[d]) / sd[d] for d in range(D)]


def summaries(z):
    return max(z), z.index(max(z)) + 1, sum(z[:19]), sum(z[:29])


def shuffles(v, n, rnd, dmax):
    out = []
    for _ in range(n):
        w = v[:]; rnd.shuffle(w); out.append(profile(w, dmax))
    return out


def target(name, dmax, seed):
    v = load(name); rnd = random.Random(seed)
    ref = shuffles(v, N_SHUF, rnd, dmax)
    z = zstats(profile(v, dmax), ref)
    M, dM, S20, S30 = summaries(z)
    # family-wise null for M and the S's: each shuffle against the other shuffles (leave-one-out is close enough
    # with 2,000; the mean and SD barely move), so use the full reference
    null = [summaries(zstats(r, ref)) for r in ref]
    return dict(name=name, z=z, M=M, dM=dM, S20=S20, S30=S30,
                pM=sum(n[0] >= M for n in null) / len(null),
                pS20=sum(n[2] >= S20 for n in null) / len(null), pS30=sum(n[3] >= S30 for n in null) / len(null))


def plant_one(seed):
    rnd = random.Random(seed)
    w1, w2 = rnd.randint(16, 25), rnd.randint(16, 25)
    k1, k2 = rnd.sample(range(w1), w1), rnd.sample(range(w2), w2)
    ct = transpo.double_enc(plaintext.telegram(615, rnd), k1, k2, "CC")
    v = [ord(c) - 65 for c in ct]
    ref = shuffles(v, N_PLANT_SHUF, rnd, 100)
    return summaries(zstats(profile(v, 100), ref))


def main():
    sr = random.Random("19-shuffle"); pr = random.Random("19-plant")
    seeds = [pr.randrange(1 << 30) for _ in range(N_PLANT)]
    with ProcessPoolExecutor(3) as ex:
        fut_t = [ex.submit(target, "telegram-1.txt", 100, sr.randrange(1 << 30)),
                 ex.submit(target, "telegram-2.txt", 50, sr.randrange(1 << 30))]
        plants = list(ex.map(plant_one, seeds, chunksize=4))
        T = [f.result() for f in fut_t]
    for t in T:
        print(f"{t['name']}: max z {t['M']:.2f} at lag {t['dM']} (family-wise p {t['pM']:.4f}); "
              f"S(20) {t['S20']:+.2f} (p own shuffles {t['pS20']:.4f}); S(30) {t['S30']:+.2f} (p {t['pS30']:.4f})")
        top = sorted(range(len(t["z"])), key=lambda d: -t["z"][d])[:8]
        print("  top lags: " + ", ".join(f"{d + 1} ({t['z'][d]:+.2f})" for d in top))
        print("  z by lag: " + " ".join(f"{x:+.1f}" for x in t["z"]))
    t1 = T[0]
    for key, i in (("M", 0), ("S20", 2), ("S30", 3)):
        v = sorted(p[i] for p in plants)
        print(f"K1 plants ({N_PLANT}) {key}: 5th {v[9]:+.2f}, median {v[99]:+.2f}, 95th {v[189]:+.2f}, 99th {v[197]:+.2f}; "
              f"T1 {t1[key]:+.2f} above {sum(x < t1[key] for x in v)}/{N_PLANT}")


if __name__ == "__main__":
    main()

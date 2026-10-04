"""Experiment 02: seeded-value controls on the f. 539 shape. See README.md (frozen 2026-10-03)."""
import random, sys
from collections import Counter
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "01-annealing"))
import solver as S  # noqa: E402  (frozen solver of experiment 01)

N, D = 344, 145
CELLS = [("KEY", 10), ("KEY", 20), ("KEY", 33), ("KEY", 50), ("CRIB", 20), ("CRIB", 40), ("CRIB", 80)]
SEEDS = 3


def anneal_fixed(table, prob, rng, fixed, p_uni):
    """Same moves, schedule and scoring as S.anneal; fixed signs start at truth and never move."""
    free = [s for s in range(prob.nsigns) if s not in fixed]
    import math
    seq, windows = prob.seq, prob.windows
    n = len(seq)
    sfreq = Counter(seq)
    best_key, best = None, -1e18
    for _ in range(S.RESTARTS):
        key = [rng.randrange(S.A) for _ in range(prob.nsigns)]
        for s, v in fixed.items():
            key[s] = v
        cnt = [0] * S.A
        for sg, f in sfreq.items():
            cnt[key[sg]] += f
        wscore = [S.score_window(table, key, seq, w) for w in windows]
        pen = S.KL_WEIGHT * S.kl_penalty(cnt, n, p_uni)
        total = sum(wscore) - pen
        for step in range(S.STEPS):
            temp = S.T0 * (1 - step / S.STEPS) + 1e-3
            s1 = rng.choice(free)
            if rng.random() < 0.5:
                s2 = None
                old1 = key[s1]
                key[s1] = rng.randrange(S.A)
                cnt[old1] -= sfreq[s1]; cnt[key[s1]] += sfreq[s1]
                touched = prob.win_of_sign[s1]
            else:
                s2 = rng.choice(free)
                old1, old2 = key[s1], key[s2]
                key[s1], key[s2] = old2, old1
                cnt[old1] += sfreq[s2] - sfreq[s1]; cnt[old2] += sfreq[s1] - sfreq[s2]
                touched = set(prob.win_of_sign[s1]) | set(prob.win_of_sign[s2])
            new = {w: S.score_window(table, key, seq, windows[w]) for w in touched}
            new_pen = S.KL_WEIGHT * S.kl_penalty(cnt, n, p_uni)
            delta = sum(new[w] - wscore[w] for w in touched) - (new_pen - pen)
            if delta >= 0 or rng.random() < math.exp(delta / temp):
                for w, v in new.items():
                    wscore[w] = v
                total += delta
                pen = new_pen
            else:
                if s2 is None:
                    cnt[key[s1]] -= sfreq[s1]; cnt[old1] += sfreq[s1]
                    key[s1] = old1
                else:
                    cnt[old1] -= sfreq[s2] - sfreq[s1]; cnt[old2] -= sfreq[s1] - sfreq[s2]
                    key[s1], key[s2] = old1, old2
        if total > best:
            best, best_key = total, key[:]
    return best_key


def run(job):
    kind, k, seed = job
    table = S.load_model()
    _, held = S.split_corpus()
    p_uni = S.unigram()
    rng = random.Random(7000 + 100 * k + seed + (0 if kind == "KEY" else 50000))
    prob, truth, plain = S.make_control(held, rng, N, D, S.target_breaks(N, S.N_BREAKS, rng))
    if kind == "KEY":
        fixed = {s: truth[s] for s, _ in Counter(prob.seq).most_common(k)}
    else:
        fixed = {s: truth[s] for s in prob.seq[:k]}
    key = anneal_fixed(table, prob, random.Random(seed), fixed, p_uni)
    free_pos = [t for t in prob.seq if t not in fixed]
    acc_free = sum(key[t] == truth[t] for t in free_pos) / len(free_pos)
    cover = 1 - len(free_pos) / len(prob.seq)
    return kind, k, seed, acc_free, cover, len(fixed), S.decrypt(prob, key)[:80], plain[:80]


def main():
    jobs = [(kind, k, s) for kind, k in CELLS for s in range(SEEDS)]
    res = {}
    lines = []
    with Pool(4) as pool:
        for kind, k, seed, acc, cover, nfix, dec, plain in pool.imap_unordered(run, jobs):
            res.setdefault((kind, k), []).append((acc, cover, nfix))
            line = f"{kind} {k} seed {seed}: unseeded acc {acc:.3f} coverage {cover:.2f} fixed {nfix}  got {dec}  true {plain}"
            lines.append(line)
            print(line, flush=True)
    (HERE / "runs.txt").write_text("\n".join(sorted(lines)) + "\n")
    out = []
    for kind, k in CELLS:
        r = res[(kind, k)]
        accs = sorted(a for a, _, _ in r)
        med = accs[len(accs) // 2]
        cov = sum(c for _, c, _ in r) / len(r)
        nf = sum(f for _, _, f in r) / len(r)
        out.append(f"{kind:4s} {k:3d}  signs fixed {nf:5.1f}  token coverage {cov:.2f}  unseeded accs "
                   f"{[round(a, 3) for a in accs]}  median {med:.3f}  {'PASS' if med >= 0.80 else 'FAIL'}")
    (HERE / "result.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()

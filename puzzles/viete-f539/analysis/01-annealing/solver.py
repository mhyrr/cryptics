"""Homophonic simulated-annealing solver and matched synthetic controls for f. 539.

Standard library only. Frozen with README.md on 2026-10-01; see README for the protocol.

    python3 solver.py model              # build out/model.bin from out/corpus_raw.txt
    python3 solver.py control            # pre-registered control ladder -> control_result.txt
"""
import array, math, random, re, sys, unicodedata
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"
ALPHA = "abcdefghilmnopqrstuxyz"            # 22 letters: j->i, v->u, k->c, w dropped
A = len(ALPHA)
IDX = {c: i for i, c in enumerate(ALPHA)}
N_ORDER = 5
T0 = 12.0                                   # starting temperature (nats)
KL_WEIGHT = 3.0                             # weight of the letter-distribution penalty
FLOOR = 0.1                                 # pseudo-count for unseen 5-grams
HOLDOUT = 0.10                              # last 10% of the corpus: control plaintexts only


# ---------- text and model ----------

def normalize(text):
    text = text.replace("ſ", "s").replace("æ", "ae").replace("œ", "oe").replace("Æ", "ae").replace("Œ", "oe")
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.replace("j", "i").replace("v", "u").replace("k", "c").replace("w", "")
    return "".join(c for c in text if c in IDX)


def split_corpus():
    t = normalize((OUT / "corpus_raw.txt").read_text())
    cut = int(len(t) * (1 - HOLDOUT))
    return t[:cut], t[cut:]


def build_model():
    """Joint 5-gram log-frequencies, log(c / total), floored at log(FLOOR / total) for unseen 5-grams."""
    train, held = split_corpus()
    x = [IDX[c] for c in train]
    c5 = Counter()
    for i in range(len(x) - 4):
        a, b, c, d, e = x[i:i + 5]
        c5[(((a * A + b) * A + c) * A + d) * A + e] += 1
    total = sum(c5.values())
    floor = math.log(FLOOR / total)
    table = array.array("d", [floor]) * (A ** 5)
    for g, n in c5.items():
        table[g] = math.log(n / total)
    with open(OUT / "model.bin", "wb") as f:
        table.tofile(f)
    print(f"train {len(train)} chars, held-out {len(held)} chars, distinct 5-grams {len(c5)}, floor {floor:.2f}")


def load_model():
    t = array.array("d")
    with open(OUT / "model.bin", "rb") as f:
        t.fromfile(f, A ** N_ORDER)
    return t


# ---------- solver ----------

class Problem:
    """Cipher tokens as sign ids, split into segments at numbers (name codes)."""

    def __init__(self, segments):
        self.segments = [s for s in segments if s]
        self.seq = [t for s in self.segments for t in s]
        self.nsigns = max(self.seq) + 1
        # windows: every 5-gram that lies wholly inside a segment, as a tuple of positions
        self.windows, pos = [], 0
        for s in self.segments:
            for i in range(len(s) - N_ORDER + 1):
                self.windows.append(tuple(range(pos + i, pos + i + N_ORDER)))
            pos += len(s)
        self.win_of_sign = [[] for _ in range(self.nsigns)]
        for w, positions in enumerate(self.windows):
            for sgn in {self.seq[p] for p in positions}:
                self.win_of_sign[sgn].append(w)


def score_window(table, key, seq, positions):
    g = 0
    for p in positions:
        g = g * A + key[seq[p]]
    return table[g]


def unigram():
    train, _ = split_corpus()
    f = Counter(train)
    return [f[c] / len(train) for c in ALPHA]


def kl_penalty(cnt, n, p):
    """n * KL(q || p) for the decryption's letter counts cnt."""
    return sum(c * math.log(c / (n * pl)) for c, pl in zip(cnt, p) if c)


def anneal(table, prob, rng, steps, restarts, t0=T0, weight=KL_WEIGHT, p_uni=None):
    seq, windows = prob.seq, prob.windows
    p_uni = p_uni or unigram()
    n = len(seq)
    sfreq = Counter(seq)
    best_key, best_score = None, -1e18
    for _ in range(restarts):
        key = [rng.randrange(A) for _ in range(prob.nsigns)]
        cnt = [0] * A
        for sgn, f in sfreq.items():
            cnt[key[sgn]] += f
        wscore = [score_window(table, key, seq, w) for w in windows]
        pen = weight * kl_penalty(cnt, n, p_uni)
        total = sum(wscore) - pen
        for step in range(steps):
            temp = t0 * (1 - step / steps) + 1e-3
            s1 = rng.randrange(prob.nsigns)
            if not sfreq[s1]:
                continue
            if rng.random() < 0.5:
                s2 = None
                old1 = key[s1]
                key[s1] = rng.randrange(A)
                cnt[old1] -= sfreq[s1]; cnt[key[s1]] += sfreq[s1]
                touched = prob.win_of_sign[s1]
            else:
                s2 = rng.randrange(prob.nsigns)
                old1, old2 = key[s1], key[s2]
                key[s1], key[s2] = old2, old1
                cnt[old1] += sfreq[s2] - sfreq[s1]; cnt[old2] += sfreq[s1] - sfreq[s2]
                touched = set(prob.win_of_sign[s1]) | set(prob.win_of_sign[s2])
            new = {w: score_window(table, key, seq, windows[w]) for w in touched}
            new_pen = weight * kl_penalty(cnt, n, p_uni)
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
        if total > best_score:
            best_score, best_key = total, key[:]
    return best_key, best_score


def decrypt(prob, key):
    return "|".join("".join(ALPHA[key[t]] for t in s) for s in prob.segments)


# ---------- synthetic controls ----------

def make_control(held, rng, n_tokens, n_signs, break_positions):
    """Encipher a held-out window: homophones per letter proportional to frequency (>= 1)."""
    start = rng.randrange(len(held) - n_tokens - 1)
    plain = held[start:start + n_tokens]
    f = Counter(plain)
    letters = sorted(f, key=lambda c: -f[c])
    alloc = {c: 1 for c in letters}
    while sum(alloc.values()) < n_signs:            # give extra homophones by frequency
        c = max(letters, key=lambda c: f[c] / alloc[c])
        alloc[c] += 1
    ids, sid = {}, 0
    for c in letters:
        ids[c] = list(range(sid, sid + alloc[c]))
        sid += alloc[c]
    truth = {}
    for c, lst in ids.items():
        for s in lst:
            truth[s] = IDX[c]
    toks = [rng.choice(ids[c]) for c in plain]
    segs, prev = [], 0
    for b in sorted(break_positions) + [n_tokens]:
        segs.append(toks[prev:b])
        prev = b
    return Problem(segs), truth, plain


def accuracy(prob, key, truth):
    return sum(key[t] == truth[t] for t in prob.seq) / len(prob.seq)


def target_breaks(n_tokens, n_breaks, rng):
    return sorted(rng.sample(range(5, n_tokens - 5), n_breaks))


CELLS = [
    # name, tokens, signs, seeds, role
    ("PRIMARY f539-matched", 344, 145, 5, "gate"),
    ("POSITIVE marmont-shaped", 1300, 155, 3, "solver validity"),
    ("ladder N=700", 700, 145, 3, "ladder"),
    ("ladder N=1400", 1400, 145, 3, "ladder"),
    ("ladder N=2800", 2800, 145, 3, "ladder"),
    ("merge D=80", 344, 80, 3, "ladder"),
    ("merge D=40", 344, 40, 3, "ladder"),
]
STEPS, RESTARTS = 500000, 12
N_BREAKS = 21                                  # 19 Arabic numbers + 2 Roman numerals (reader A)


def run_cell_seed(args):
    name, n, d, seed = args
    table = load_model()
    _, held = split_corpus()
    rng = random.Random(1000 * n + d + seed)
    prob, truth, plain = make_control(held, rng, n, d, target_breaks(n, N_BREAKS * n // 344, rng))
    key, sc = anneal(table, prob, random.Random(seed), STEPS, RESTARTS)
    acc = accuracy(prob, key, truth)
    return name, seed, acc, decrypt(prob, key)[:70], plain[:70]


def run_controls():
    from multiprocessing import Pool
    jobs = [(name, n, d, seed) for name, n, d, seeds, role in CELLS for seed in range(seeds)]
    accs = {}
    with Pool(4) as pool:
        for name, seed, acc, dec, plain in pool.imap_unordered(run_cell_seed, jobs):
            accs.setdefault(name, []).append(acc)
            print(f"{name} seed {seed}: acc {acc:.3f}  got {dec}  true {plain}", flush=True)
    lines = []
    for name, n, d, seeds, role in CELLS:
        a = sorted(accs[name])
        med = a[len(a) // 2]
        lines.append(f"{name:28s} N={n:5d} D={d:4d} role={role:16s} accs={[round(x, 3) for x in a]} "
                     f"median={med:.3f} {'PASS' if med >= 0.80 else 'FAIL'}")
    (HERE / "control_result.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    {"model": build_model, "control": run_controls}[sys.argv[1]]()

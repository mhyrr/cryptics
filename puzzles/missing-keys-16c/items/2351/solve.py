"""solve.py - the cipher of no. 2351 solved from its own text, under H9 (README, "Stage 3").

    python3 solve.py synth [--seed 1]            a planted cipher of the H9 kind, solved blind; reports recovery
    python3 solve.py run cipher.txt out.tsv [--restarts 8] [--seed 1]
The table has: one consonant for each base that takes vowel marks (a one-to-one map onto the consonants that
occur, v counted with u), one vowel for each of the five vowel marks (a one-to-one map), and one letter or
nothing for each other sign. A marked sign spells consonant + vowel. No plain text is used. The decode is
scored by letter trigrams of period Italian (Machiavelli, Opere vol. 3 OCR; words run together) plus a
penalty when the decode's letter counts leave Italian's. Search: simulated annealing from random tables;
the best of several restarts is kept, and the restarts' agreement is reported.
"""
import math, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "line"))
import align, tied  # noqa: E402

ALPHA = "abcdefghilmnopqrstuz"
VOW = "aeiou"
CONS = [c for c in ALPHA if c not in VOW] + ["u"]          # u doubles as v
K = 0.1


def model():
    corpus = os.path.join(HERE, "..", "2911", "print", "leoperediniccol03milagoog_djvu.txt")
    words = [align.norm_letters(w) for w in re.split(r"[^A-Za-zàèéìòù]+", open(corpus, encoding="utf-8", errors="replace").read())]
    text = "".join(w for w in words if w and all(ch in ALPHA for ch in w))
    idx = {c: i for i, c in enumerate(ALPHA)}
    V = len(ALPHA)
    tri = [0] * (V ** 3)
    bi = [0] * (V ** 2)
    uni = [0] * V
    a = [idx[c] for c in text]
    for i in range(len(a) - 2):
        tri[a[i] * V * V + a[i + 1] * V + a[i + 2]] += 1
        bi[a[i] * V + a[i + 1]] += 1
        uni[a[i]] += 1
    lp = [math.log((tri[k] + K) / (bi[k // V] + K * V)) for k in range(V ** 3)]
    tot = sum(uni)
    return lp, [u / tot for u in uni], idx


def setup(units, mk):
    """-> (seq, bases, marks, others). seq: per sign ('BM', bi, mi) | ('B', bi) | ('W', wi) | None for unread."""
    bases, marks, others, seq = [], list(tied.VMARKS), [], []
    for u in units:
        if u.kind != "sign":
            continue
        if u.sym == "?":
            seq.append(None)
            continue
        kind, a, b = tied.parts(u.sym, mk)
        if kind == "BM":
            if a not in bases:
                bases.append(a)
            seq.append(("BM", bases.index(a), marks.index(b)))
        elif kind == "B":
            if a not in bases:
                bases.append(a)
            seq.append(("B", bases.index(a)))
        else:
            if a not in others:
                others.append(a)
            seq.append(("W", others.index(a)))
    return seq, bases, marks, others


def decode(seq, kb, km, kw):
    out = []
    for s in seq:
        if s is None:
            out.append("")
        elif s[0] == "BM":
            out.append(kb[s[1]] + km[s[2]])
        elif s[0] == "B":
            out.append(kb[s[1]])
        else:
            out.append(kw[s[1]])
    return out


def score(pieces, lp, uni, idx, lam):
    V = len(ALPHA)
    a = [idx[c] for p in pieces for c in p]
    if len(a) < 3:
        return -1e9
    s = 0.0
    x, y = a[0], a[1]
    for z in a[2:]:
        s += lp[x * V * V + y * V + z]
        x, y = y, z
    n = len(a)
    cnt = [0] * V
    for c in a:
        cnt[c] += 1
    chi = sum((cnt[i] - n * uni[i]) ** 2 / (n * uni[i]) for i in range(V))
    return s - lam * chi


def anneal(seq, nb, nw, lp, uni, idx, rng, steps=60000, lam=0.5, t0=6.0):
    cons = CONS[:]
    rng.shuffle(cons)
    while len(cons) < nb:
        cons.append(rng.choice(CONS))
    kb = cons[:nb]
    spare = cons[nb:]
    km = list(VOW)
    rng.shuffle(km)
    kw = [rng.choice(ALPHA) for _ in range(nw)]
    cur = score(decode(seq, kb, km, kw), lp, uni, idx, lam)
    best = (cur, kb[:], km[:], kw[:])
    for step in range(steps):
        t = t0 * (1 - step / steps) + 0.05
        r = rng.random()
        if r < 0.45 and nw:
            i = rng.randrange(nw)
            old = kw[i]
            kw[i] = rng.choice(ALPHA + " ").strip() if rng.random() < 0.9 else ""
            undo = lambda: kw.__setitem__(i, old)
        elif r < 0.85:
            i = rng.randrange(nb)
            if spare and rng.random() < 0.3:
                j = rng.randrange(len(spare))
                kb[i], spare[j] = spare[j], kb[i]
                undo = lambda: (kb.__setitem__(i, spare[j]), spare.__setitem__(j, kb[i]))[0] if False else _swap(kb, i, spare, j)
            else:
                j = rng.randrange(nb)
                kb[i], kb[j] = kb[j], kb[i]
                undo = lambda: _swap(kb, i, kb, j)
        else:
            i, j = rng.sample(range(5), 2)
            km[i], km[j] = km[j], km[i]
            undo = lambda: _swap(km, i, km, j)
        new = score(decode(seq, kb, km, kw), lp, uni, idx, lam)
        if new >= cur or rng.random() < math.exp((new - cur) / t):
            cur = new
            if cur > best[0]:
                best = (cur, kb[:], km[:], kw[:])
        else:
            undo()
    return best


def _swap(a, i, b, j):
    a[i], b[j] = b[j], a[i]


def solve(units, restarts=8, seed=1, steps=60000, log=print):
    mk = tied.markable(units)
    seq, bases, marks, others = setup(units, mk)
    lp, uni, idx = model()
    runs = []
    for r in range(restarts):
        rng = random.Random(seed * 1000 + r)
        sc, kb, km, kw = anneal(seq, len(bases), len(others), lp, uni, idx, rng, steps)
        n = sum(len(p) for p in decode(seq, kb, km, kw))
        runs.append((sc, kb, km, kw))
        log(f"restart {r + 1}: score {sc:.1f}; letters {n}; per letter {sc / max(1, n):.3f}")
    runs.sort(key=lambda x: -x[0])
    return runs, seq, bases, marks, others


def table(run, bases, marks, others):
    sc, kb, km, kw = run
    t = {"B:" + b: v for b, v in zip(bases, kb)}
    t.update({"M:" + m: v for m, v in zip(marks, km)})
    t.update({"W:" + w: v for w, v in zip(others, kw)})
    return t


def run_synth(argv):
    opt = lambda name, d: float(argv[argv.index(name) + 1]) if name in argv else d
    seed = int(opt("--seed", 1))
    ctext, ptext, truth, nsigns, nlet = tied.synth(seed)
    units, _, _ = align.parse_cipher(ctext)
    runs, seq, bases, marks, others = solve(units, int(opt("--restarts", 4)), seed, int(opt("--steps", 60000)))
    t = table(runs[0], bases, marks, others)
    bm = [k for k in t if k[0] in "BM"]
    right = sum(truth.get(k) == t[k] or (truth.get(k) == "v" and t[k] == "u") for k in bm)
    w = [k for k in t if k[0] == "W" and len(truth.get(k, "xx")) == 1]
    print(f"seed {seed}: signs {nsigns}; best score {runs[0][0]:.1f}; bases and marks right {right} of {len(bm)}; "
          f"one-letter signs right {sum(truth[k] == t[k] for k in w)} of {len(w)}")
    print("decode start:", "".join(decode(seq, *runs[0][1:]))[:150])


def run_real(cpath, out, argv):
    opt = lambda name, d: float(argv[argv.index(name) + 1]) if name in argv else d
    units, _, _ = align.parse_cipher(open(cpath, encoding="utf-8").read())
    logs = []
    runs, seq, bases, marks, others = solve(units, int(opt("--restarts", 8)), int(opt("--seed", 1)),
                                            int(opt("--steps", 60000)), logs.append)
    best = table(runs[0], bases, marks, others)
    second = table(runs[1], bases, marks, others) if len(runs) > 1 else best
    bm = [k for k in best if k[0] in "BM"]
    agree = sum(best[k] == second[k] for k in bm)
    rows = [dict(unit=k, value=v, type=align.unit_type(v) if v else "null", support=0, conflict=0, share=0,
                 status="probable", alts="solve.py", positions="") for k, v in sorted(best.items())]
    align.write_key(rows, out)
    print("\n".join(logs))
    print(f"best two restarts agree on {agree} of {len(bm)} bases and marks")
    print("marks:", " ".join(f"{m}={best['M:' + m]}" for m in marks))
    print("decode start:", "".join(decode(seq, *runs[0][1:]))[:300])


if __name__ == "__main__":
    if sys.argv[1] == "synth":
        run_synth(sys.argv[2:])
    else:
        run_real(sys.argv[2], sys.argv[3], sys.argv[4:])

"""synth.py - a planted pair of the 2911 kind, to test a builder where the answer is ours.

    python3 synth.py <variant> [--seed 1] [--cut 0.35] [--unread 0.08] [--wrong 0.02] [--spell 0.05]
Takes the letters of inputs/plain-full.txt as the message. Plants a random key: one sign per letter (two for
each vowel) and one sign for each of the 55 most frequent consonant+vowel pairs. Enciphers the whole message
(an open syllable takes its sign 85% of the time). Then damages both sides the way the real pair is damaged:
  cut     share of the plain text removed, in six stretches (the abridgement)
  unread  share of cipher signs replaced by '?'
  wrong   share of cipher signs replaced by another sign
  spell   share of plain letters changed, dropped or doubled
Runs variants/<variant>.build on the pair and reports, against the planted key: marked rows right and wrong,
and place precision and recall. No real sign value is involved; the output may be read freely.
"""
import importlib, os, random, sys, tempfile, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "variants"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "line"))
import align  # noqa: E402


def make(seed=1, cut=0.35, unread=0.08, wrong=0.02, spell=0.05):
    rng = random.Random(seed)
    T, _, _, _ = align.parse_plain(open(os.path.join(HERE, "inputs", "plain-full.txt"), encoding="utf-8").read())
    cv = collections.Counter(T[i:i + 2] for i in range(len(T) - 1) if T[i] not in "aeiou" and T[i + 1] in "aeiou")
    values = sorted(set(T)) + [v for v in "aeiou"] + [s for s, _ in cv.most_common(55)]
    names = [f"k{i}" for i in range(len(values))]
    rng.shuffle(names)
    key = dict(zip(names, values))
    by_val = collections.defaultdict(list)
    for n, v in key.items():
        by_val[v].append(n)
    signs, i = [], 0                       # (sign, start letter)
    while i < len(T):
        two = T[i:i + 2]
        if len(two) == 2 and two in by_val and rng.random() < 0.85:
            signs.append((rng.choice(by_val[two]), i))
            i += 2
        else:
            signs.append((rng.choice(by_val[T[i]]), i))
            i += 1
    out = []
    for s, _ in signs:
        r = rng.random()
        out.append("?" if r < unread else rng.choice(names) if r < unread + wrong else s)
    keep = [True] * len(T)
    for _ in range(6):
        ln = int(cut * len(T) / 6)
        a = rng.randrange(60, len(T) - ln - 60)
        for k in range(a, a + ln):
            keep[k] = False
    plain = []
    for k, ch in enumerate(T):
        if not keep[k]:
            continue
        r = rng.random()
        if r < spell / 3:
            continue
        if r < 2 * spell / 3:
            plain.append(rng.choice("aeioulnrst"))
            continue
        plain.append(ch)
        if r < spell:
            plain.append(ch)
    lines = [" ".join(out[k:k + 45]) for k in range(0, len(out), 45)]
    covered = sum(1 for s, st in signs if keep[st]) / len(signs)
    return "\n".join(lines) + "\n", "".join(plain) + "\n", key, [s for s, _ in signs], out, covered


def main():
    a = sys.argv[1:]
    opt = lambda name, d: float(a[a.index(name) + 1]) if name in a else d
    seed = int(opt("--seed", 1))
    ctext, ptext, key, true_signs, shown, covered = make(seed, opt("--cut", 0.35), opt("--unread", 0.08),
                                                         opt("--wrong", 0.02), opt("--spell", 0.05))
    d = tempfile.mkdtemp()
    cp, pp = os.path.join(d, "c.txt"), os.path.join(d, "p.txt")
    open(cp, "w").write(ctext)
    open(pp, "w").write(ptext)
    logs = []
    rows = importlib.import_module(a[0]).build(cp, pp, logs.append)
    kmap = align.key_map(rows)
    right = sum(1 for u, v in kmap.items() if key.get(u) == v)
    places = [s for s in shown if s != "?"]
    spoke = [s for s in places if s in kmap]
    ok = sum(1 for s in spoke if key.get(s) == kmap[s])
    print("\n".join(logs[-4:]))
    print(f"seed {seed}: signs {len(shown)}, plain letters {len(ptext) - 1}, cipher covered by the plain {covered:.2f}")
    print(f"marked rows {len(kmap)} of {len(key)}: right {right}, wrong {len(kmap) - right}")
    print(f"place precision {ok / max(1, len(spoke)):.3f} recall {ok / len(places):.3f}")


if __name__ == "__main__":
    main()

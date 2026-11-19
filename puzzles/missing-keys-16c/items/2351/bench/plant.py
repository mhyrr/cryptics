"""plant.py - planted pairs as loose as letter A of no. 2351, and a harness that runs a variant on them.

    python3 plant.py <variant> [--seeds 1-6] [--jobs 6] [--set key=value ...]     counts per seed, no values
    python3 plant.py describe [--seeds 1-6]                                       what a planted pair holds

The planted cipher is of the H9 kind with the lesson of the bench README built in:
- a consonant and the vowel after it are one sign, a base and a vowel mark (one base a consonant, one mark a
  vowel);
- a consonant with no vowel after it is a sign of its own; for `own` of the consonants that sign is the
  consonant's base without a mark, for the rest it is some other sign, which may be ANOTHER base unmarked;
- a vowel on its own has two signs; the 25 heaviest words have word signs (used 8 times in 10); three double letters
  have signs; two signs stand for nothing and are strewn through the text;
- every unmarked name is drawn at random from one pool of unmarked bases and other names, so an unmarked base
  may be a consonant, a vowel, a word, a double letter or nothing.
Readers' noise: unread signs, wrong marks, wrong signs. The plain side: holes of one to three words, words
damaged (a quarter of them read as another word), letters dropped or doubled, a few words after the cipher ends.
The text is Italian of the period (the 1877 print used for no. 2911); nothing of no. 2351 is read.
"""
import importlib, json, os, random, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "variants"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "line"))
import align  # noqa: E402

VMARKS = ("1", "3", "4", "5", "~")
VOW = "aeiou"
CORPUS = os.path.join(HERE, "..", "..", "2911", "print", "leoperediniccol03milagoog_djvu.txt")
_words = []


def corpus():
    if not _words:
        raw = open(CORPUS, encoding="utf-8", errors="replace").read()
        ws = [align.norm_letters(w) for w in re.split(r"[^A-Za-zàèéìòù]+", raw)]
        _words.extend(w for w in ws if w and all(ch in "abcdefghilmnopqrstuz" for ch in w))
    return _words


def plant(seed=1, n_signs=1130, holes=40, own=0.3, unread=0.035, badmark=0.03, wrong=0.02, damage=0.15,
          respell=0.05, hole_max=3, ncode=25, swap=0.25, words=None):
    """-> (cipher text, plain text, truth{sign: value}, facts{...}). words: a word list to draw from at random
    instead of a passage of the corpus (for a unit test that must not depend on a file)."""
    rng = random.Random(seed)
    if words:
        text = [rng.choice(words) for _ in range(n_signs)]
    else:
        ws = corpus()
        i = rng.randrange(20000, len(ws) - 3000)
        text = ws[i:i + n_signs]
    cons = sorted(set("".join(text)) - set(VOW))
    bases = [f"b{k}" for k in range(len(cons))]
    rng.shuffle(bases)
    cb = dict(zip(cons, bases))
    marks = list(VMARKS)
    rng.shuffle(marks)
    vm = dict(zip(VOW, marks))
    freq = {}
    for w in text:
        if len(w) >= 2:
            freq[w] = freq.get(w, 0) + 1
    coded = [w for w, c in sorted(freq.items(), key=lambda kv: (-kv[1] * len(kv[0]), kv[0]))[:ncode]]
    dbl = {}
    for w in text:
        for a, b in zip(w, w[1:]):
            if a == b and a not in VOW:
                dbl[a + b] = dbl.get(a + b, 0) + 1
    doubles = sorted(dbl, key=lambda d: (-dbl[d], d))[:3]
    pool = bases[:] + [f"w{k}" for k in range(30 + ncode)]
    rng.shuffle(pool)
    bare = {}
    for c in cons:
        if rng.random() < own:
            bare[c] = cb[c]
            pool.remove(cb[c])
    for c in cons:
        if c not in bare:
            bare[c] = pool.pop()
    whole = {v: [pool.pop(), pool.pop()] for v in VOW}
    code = {w: pool.pop() for w in coded}
    dsign = {d: pool.pop() for d in doubles}
    nulls = [pool.pop(), pool.pop()]
    signs = []                                   # (sign, word index)
    for wi, w in enumerate(text):
        if w in code and rng.random() < 0.8:
            signs.append((code[w], wi))
        else:
            j = 0
            while j < len(w):
                ch = w[j]
                if w[j:j + 2] in dsign and rng.random() < 0.8:
                    signs.append((dsign[w[j:j + 2]], wi))
                    j += 2
                elif ch not in VOW and j + 1 < len(w) and w[j + 1] in VOW:
                    signs.append((cb[ch] + "+" + vm[w[j + 1]], wi))
                    j += 2
                elif ch not in VOW:
                    signs.append((bare[ch], wi))
                    j += 1
                else:
                    signs.append((rng.choice(whole[ch]), wi))
                    j += 1
        if rng.random() < 0.04:
            signs.append((rng.choice(nulls), wi))
        if len(signs) >= n_signs:
            text = text[:wi + 1]
            break
    truth = {}
    for c, b in cb.items():
        for v, m in vm.items():
            truth[b + "+" + m] = c + v
    for c, s in bare.items():
        truth[s] = c
    for v, ss in whole.items():
        for s in ss:
            truth[s] = v
    for w, s in code.items():
        truth[s] = w
    for d, s in dsign.items():
        truth[s] = d
    for s in nulls:
        truth[s] = ""
    kinds = sorted({s for s, _ in signs})
    shown = []
    for s, _ in signs:
        r = rng.random()
        b, _, m = s.partition("+")
        if r < unread:
            shown.append("?")
        elif r < unread + badmark and (m or b in cb.values()):
            shown.append(b + "+" + rng.choice([x for x in VMARKS if x != m]) if (not m or rng.random() < 0.6) else b)
        elif r < unread + badmark + wrong:
            shown.append(rng.choice(kinds))
        else:
            shown.append(s)
    nw = len(text)
    hidden = [False] * nw
    starts = rng.sample(range(nw), holes)
    if rng.random() < 0.5:
        starts[0] = 0
    for st in starts:
        for k in range(st, min(nw, st + rng.randint(1, hole_max))):
            hidden[k] = True
    plain = []
    for wi, w in enumerate(text):
        if hidden[wi]:
            if not plain or plain[-1] != "[...]":
                plain.append("[...]")
            continue
        r = rng.random()
        if r < damage:
            k = rng.random()
            if k < swap:                                  # a word read as another word
                w = rng.choice(text)
            elif k < 0.5:
                w = "".join(rng.choice("aeioulnrst") if rng.random() < 0.3 else ch for ch in w)
            elif k < 0.75 and len(w) > 2:
                x = rng.randrange(len(w))
                w = w[:x] + w[x + 1:]
            else:
                x = rng.randrange(len(w) + 1)
                w = w[:x] + rng.choice("aeioulnrst") + w[x:]
        elif r < damage + respell:
            x = rng.randrange(len(w))
            w = w[:x] + w[x] + w[x:] if rng.random() < 0.5 or len(w) < 3 else w[:x] + w[x + 1:]
        plain.append(w)
    ws = corpus() if not words else words
    plain += [rng.choice(ws) for _ in range(rng.randint(0, 4))]
    ctext = "# planted\n" + "\n".join(" ".join(shown[k:k + 46]) for k in range(0, len(shown), 46)) + "\n"
    facts = dict(signs=len(shown), kinds=len(set(shown) - {"?"}), letters=sum(len(w) for w in plain if w != "[...]"),
                 holes=plain.count("[...]"), hidden_words=sum(hidden), words=nw,
                 own=sum(1 for c in cons if bare[c] == cb[c]), bases=len(cons),
                 marked_places=sum(1 for s in shown if "+" in s))
    return ctext, " ".join(plain) + "\n", truth, facts


def judge(rows, truth, ctext):
    """the bench's score against a planted truth -> dict of counts. A sign that stands for nothing is in
    the truth with the value ''; a builder that gives it letters is wrong there."""
    toks = [t for ln in ctext.splitlines() if not ln.startswith("#") for t in ln.split() if t != "?"]
    tab = {r["unit"]: r["value"] for r in rows if r.get("status") in ("certain", "probable")}
    shared = [s for s in tab if s in truth]
    same = sum(tab[s] == truth[s] for s in shared)
    pa = [t for t in toks if t in truth and truth[t]]
    spoke = [t for t in toks if t in truth and t in tab]
    ok = sum(tab[t] == truth[t] for t in spoke)
    tied_kinds = [s for s in shared if "+" in s]
    return dict(marked=len(tab), shared=len(shared), same=same, wrong=len(shared) - same,
                tied=len(tied_kinds), tied_same=sum(tab[s] == truth[s] for s in tied_kinds),
                precision=ok / max(1, len(spoke)), recall=ok / max(1, len(pa)),
                passed=len(shared) >= 20 and same >= 0.8 * len(shared))


def one(job):
    variant, seed, settings, kw = job
    mod = importlib.import_module(variant)
    for k, v in settings.items():
        setattr(mod, k, type(getattr(mod, k))(v))
    ctext, ptext, truth, facts = plant(seed, **kw)
    with tempfile.TemporaryDirectory() as d:
        cp, pp = os.path.join(d, "c.txt"), os.path.join(d, "p.txt")
        open(cp, "w").write(ctext)
        open(pp, "w").write(ptext)
        logs = []
        rows = mod.build(cp, pp, logs.append)
    return seed, facts, judge(rows, truth, ctext), logs


def seeds_of(argv):
    if "--seeds" not in argv:
        return list(range(1, 7))
    a, _, b = argv[argv.index("--seeds") + 1].partition("-")
    return list(range(int(a), int(b or a) + 1))


def main():
    argv = sys.argv[1:]
    seeds = seeds_of(argv)
    kw = {}
    settings = {}
    for k, a in enumerate(argv):
        if a == "--set":
            name, _, val = argv[k + 1].partition("=")
            settings[name] = val
        if a == "--plant":
            name, _, val = argv[k + 1].partition("=")
            kw[name] = float(val) if "." in val else int(val)
    if argv[0] == "describe":
        for s in seeds:
            _, _, truth, f = plant(s, **kw)
            print(f"seed {s}: " + ", ".join(f"{k} {v}" for k, v in f.items()))
        return
    jobs = int(argv[argv.index("--jobs") + 1]) if "--jobs" in argv else 6
    if "--one" in argv:                       # a child: one seed, the result as one line of JSON
        print(json.dumps(one((argv[0], seeds[0], settings, kw))))
        return
    # one process a seed (multiprocessing cannot be used here: line/queue.py shadows the library's queue)
    res, running, todo = {}, [], list(seeds)
    while todo or running:
        while todo and len(running) < jobs:
            s = todo.pop(0)
            rest = [a for k, a in enumerate(argv) if a != "--seeds" and (k == 0 or argv[k - 1] != "--seeds")]
            cmd = [sys.executable, os.path.abspath(__file__)] + rest + ["--seeds", str(s), "--one"]
            running.append((s, subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)))
        s, pr = running.pop(0)
        out, err = pr.communicate()
        if pr.returncode:
            sys.exit(f"seed {s} failed:\n{err[-2000:]}")
        res[s] = json.loads(out.strip().splitlines()[-1])
    res = [res[s] for s in seeds]
    print(f"variant {argv[0]} {settings or ''} {kw or ''}")
    print("seed\tsigns\tletters\tholes\tmarked\tshared\tsame\twrong\ttied\ttied_same\tprecision\trecall\tpass")
    npass = 0
    for seed, f, j, logs in res:
        npass += j["passed"]
        print(f"{seed}\t{f['signs']}\t{f['letters']}\t{f['holes']}\t{j['marked']}\t{j['shared']}\t{j['same']}\t"
              f"{j['wrong']}\t{j['tied']}\t{j['tied_same']}\t{j['precision']:.3f}\t{j['recall']:.3f}\t{j['passed']}")
        if "--logs" in argv:
            for ln in logs:
                print("   ", ln)
    print(f"passed {npass} of {len(res)}")


if __name__ == "__main__":
    main()

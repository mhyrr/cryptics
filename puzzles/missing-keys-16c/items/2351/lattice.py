"""lattice.py - letter B read from readers H, G, I at once. Port of ../1336/lattice.py (README, "Stage 8").

    python3 lattice.py selftest   results/b-lattice-selftest.tsv   planted lines; run first
    python3 lattice.py test       results/b-lattice-test.tsv       the registered test (key-v0.tsv); run once
    python3 lattice.py read       results/b-lattice-read.txt       only after the test
    python3 lattice.py words      results/b-words.tsv              support of each phrase listed in b-words.txt

Columns: readers G and I lined up on reader H, line by line. Each column holds the three votes. A vote's
candidate is the key's value for that sign (a whole sign, or base + mark); an unread or unvalued vote is "any
one letter" and prints as '?'. The best path is found by log vote share plus letter-trigram gain, so the
letter model chooses only among letters some reader supports. Gain is log p + log 20 for each trigram, and
nothing for a trigram wholly inside one sign's value: without both rules a table is rewarded or punished for
the length of its values (the key holds "ancora" and "senza"; no. 1336's key held single letters), and on
planted lines of random letters the true table then beat its shuffles 14 times in 20. Control: the same with the key's values
shuffled inside each class (bases, marks, whole signs), as in stage 4b.
"""
import difflib, math, multiprocessing, os, random, re, sys
import multiprocessing.pool, multiprocessing.queues     # before ../../line is on the path: it has a queue.py
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "line"))
import align, run as item, tied  # noqa: E402

RES = os.path.join(HERE, "results")
CORPUS = os.path.join(HERE, "..", "2911", "print", "leoperediniccol03milagoog_djvu.txt")
READERS = ("H", "G", "I")
ANY, NONE = "*", ""
ALPHA = "abcdefghilmnopqrstuz"
IDX = {c: i for i, c in enumerate(ALPHA)}
V = len(ALPHA)
LOGV = math.log(V)
K = 0.1
EPS = 0.02                                                     # floor on a candidate's vote share
START = V                                                      # index of "no letter yet"


def votes(tok):
    """-> [(sign or None for unread, weight)] for one token."""
    if tok == "?":
        return [(None, 1.0)]
    if "|" in tok:
        parts = [p.rstrip("?") for p in tok.split("|")]
        return [(p or None, 1.0 / len(parts)) for p in parts]
    if tok.endswith("?"):
        return [(tok[:-1], 0.7), (None, 0.3)]
    return [(tok, 1.0)]


def first(tok):
    return votes(tok)[0][0] or "?"


def reader_rows(name="B.txt"):
    """-> {reader: [line: [token]]}, names mapped by names.tsv, base^mark written base+mark."""
    return {r: [[item.join(t) for t in row] for row in item.cipher_rows(r, name)] for r in READERS}


def columns(rows, readers=READERS):
    """One line. rows: {reader: [token]}. -> list of columns {reader: token}; reader 0 is the frame."""
    cols = [{readers[0]: t} for t in rows[readers[0]]]
    for rd in readers[1:]:
        idx = [i for i, c in enumerate(cols) if readers[0] in c]
        a = [first(cols[i][readers[0]]) for i in idx]
        toks = rows[rd]
        b = [first(t) for t in toks]
        extra = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            n = min(i2 - i1, j2 - j1) if op in ("equal", "replace") else 0
            for k in range(n):
                cols[idx[i1 + k]][rd] = toks[j1 + k]
            at = idx[i1 + n] if i1 + n < len(idx) else len(cols)
            extra += [(at, t) for t in toks[j1 + n:j2]]
        for at, t in sorted(extra, key=lambda e: -e[0]):
            if at > 0 and readers[0] not in cols[at - 1] and rd not in cols[at - 1]:
                cols[at - 1][rd] = t
            else:
                cols.insert(at, {rd: t})
    return cols


def value(sign, t):
    b, _, m = sign.partition("+")
    if "W:" + sign in t:
        return t["W:" + sign]
    if m in tied.VMARKS and "B:" + b in t and "M:" + m in t:
        return t["B:" + b] + t["M:" + m]
    return None


def entries(sign, t):
    b, _, m = sign.partition("+")
    if "W:" + sign in t:
        return ("W:" + sign,)
    if m in tied.VMARKS and "B:" + b in t and "M:" + m in t:
        return ("B:" + b, "M:" + m)
    return ()


def candidates(col, t, readers=READERS):
    """-> {candidate: share}. candidate: a value string, ANY, or NONE."""
    c = {}
    for rd in readers:
        tok = col.get(rd)
        if tok is None:
            c[NONE] = c.get(NONE, 0) + 1.0
            continue
        for s, w in votes(tok):
            v = value(s, t) if s else None
            key = v if v else ANY
            c[key] = c.get(key, 0) + w
    n = float(len(readers))
    return {k: v / n for k, v in c.items()}


def model():
    words = [align.norm_letters(w) for w in re.split(r"[^A-Za-zàèéìòùÀÈÉÌÒÙ]+",
                                                     open(CORPUS, encoding="utf-8", errors="replace").read())]
    text = "".join(w for w in words if w and all(ch in ALPHA for ch in w))
    cut = int(len(text) * 0.9)
    train, held = text[:cut], text[cut:]
    tri, bi = [0] * (V ** 3), [0] * (V ** 2)
    a = [IDX[c] for c in train]
    for i in range(len(a) - 2):
        tri[a[i] * V * V + a[i + 1] * V + a[i + 2]] += 1
        bi[a[i] * V + a[i + 1]] += 1
    lp = [math.log((tri[k] + K) / (bi[k // V] + K * V)) for k in range(V ** 3)]
    return lp, held, len(train)


def best(cols, t, lp, readers=READERS):
    """-> (score, lm score, letters emitted, path). path: [(candidate, emitted, share)] per column."""
    states = {(START, START): (0.0, 0.0, None)}      # last two letters -> (score, lm, history)
    for col in cols:
        cand = candidates(col, t, readers)
        new = {}
        for k, share in cand.items():
            ls = math.log(max(share, EPS))
            if k == NONE:
                for st, (sc, lm, hist) in states.items():
                    tot = sc + ls
                    if st not in new or tot > new[st][0]:
                        new[st] = (tot, lm, (hist, k, "", share))
            elif k == ANY:
                for (x, y), (sc, lm, hist) in states.items():
                    base = sc + ls - LOGV
                    row = None if x == START else (x * V + y) * V
                    for c in range(V):
                        d = 0.0 if row is None else lp[row + c] + LOGV
                        tot = base + d
                        st = (y, c)
                        if st not in new or tot > new[st][0]:
                            new[st] = (tot, lm + d, (hist, k, ALPHA[c], share))
            else:
                ki = [IDX[ch] for ch in k]
                for (x, y), (sc, lm, hist) in states.items():
                    d = 0.0
                    for j, c in enumerate(ki):
                        if x != START and j < 2:     # a trigram wholly inside one value earns nothing
                            d += lp[(x * V + y) * V + c] + LOGV
                        x, y = y, c
                    tot = sc + ls + d
                    st = (x, y)
                    if st not in new or tot > new[st][0]:
                        new[st] = (tot, lm + d, (hist, k, k, share))
        states = new
    sc, lm, hist = max(states.values(), key=lambda v: v[0])
    path = []
    while hist is not None:
        path.append(hist[1:])
        hist = hist[0]
    path.reverse()
    return sc, lm, sum(len(o) for _, o, _ in path), path


def key(name):
    return {r["unit"]: r["value"] for r in align.read_key(os.path.join(HERE, name))
            if r["status"] in ("certain", "probable")}


def shuffled(t, rng):
    s = {}
    for p in ("B:", "M:", "W:"):
        ks = [k for k in t if k.startswith(p)]
        vs = [t[k] for k in ks]
        rng.shuffle(vs)
        s.update(zip(ks, vs))
    return s


def all_columns():
    rows = reader_rows()
    n = len(rows[READERS[0]])
    by_line = [columns({r: rows[r][k] for r in READERS}) for k in range(n)]
    return by_line, [c for ln in by_line for c in ln]


_G = {}


def _one(tab):
    sc, lm, n, _ = best(_G["cols"], tab, _G["lp"])
    return sc, lm / max(1, n - 2)


def test():
    lp, held, ntrain = model()
    _, cols = all_columns()
    _G.update(cols=cols, lp=lp)
    out = [f"columns\t{len(cols)}", f"readers\t{' '.join(READERS)}", f"train_letters\t{ntrain}"]
    for name in ("key-v0.tsv", "key-v1.tsv"):
        t = key(name)
        sc, lm, n, path = best(cols, t, lp)
        rng = random.Random(1)
        tabs = [shuffled(t, rng) for _ in range(200)]
        with multiprocessing.get_context("fork").Pool(8) as pool:
            res = pool.map(_one, tabs)
        sh, shlm = [r[0] for r in res], [r[1] for r in res]
        below = sum(1 for x in sh if x < sc)
        sup = sum(1 for k, o, _ in path if k not in (ANY, NONE))
        out += [f"## {name}", f"table_entries\t{len(t)}", f"columns_with_a_supported_value\t{sup}",
                f"path_letters\t{n}", f"true_score\t{sc:.2f}", f"shuffles_below_true\t{below} of 200",
                f"shuffle_score_mean\t{sum(sh) / len(sh):.2f}", f"shuffle_score_max\t{max(sh):.2f}",
                f"pass\t{below >= 190}", f"true_gain_per_letter\t{lm / max(1, n - 2):.3f}",
                f"shuffle_gain_per_letter_mean\t{sum(shlm) / len(shlm):.3f}",
                f"shuffle_gain_per_letter_max\t{max(shlm):.3f}"]
    open(os.path.join(RES, "b-lattice-test.tsv"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))


def read_path():
    """-> per line: list of (column, candidates, chosen candidate, emitted, share, new) for key-v1."""
    lp, _, _ = model()
    by_line, cols = all_columns()
    t, t0 = key("key-v1.tsv"), key("key-v0.tsv")
    added = set(t) - set(t0)
    _, _, _, path = best(cols, t, lp)
    out, i = [], 0
    for ln in by_line:
        row = []
        for col in ln:
            k, o, share = path[i]
            i += 1
            new = any(e in added for tok in col.values() for s, _ in votes(tok) if s
                      for e in entries(s, t) if value(s, t) == k)
            row.append((col, candidates(col, t), k, o, share, new))
        out.append(row)
    return out


def strings(row):
    """-> (supported, with fill, all-three, stage-7) strings of one line, letter for letter aligned."""
    sup, fill, full, st7 = [], [], [], []
    for col, cand, k, o, share, new in row:
        if k == NONE:
            continue
        s = "?" if k == ANY else o
        sup.append(s)
        fill.append(o.upper() if k == ANY else o)
        full.append(s if (k == ANY or share >= 0.99) else "." * len(s))
        st7.append(("^" if new else " ") * len(s))
    return "".join(sup), "".join(fill), "".join(full), "".join(st7)


def read():
    rows = read_path()
    out = ["# letter B by lattice, key-v1.tsv (certain and probable rows). Script output; no word division.",
           "# supported: letters some reader's sign supports; '?' = no reader's sign has a value there.",
           "# with fill: the letter model's guess at each '?' in capitals. Not evidence.",
           "# all three: letters that all three readers support; '.' = supported by one or two.",
           "# stage 7:   '^' under letters that rest on a value added at stage 7 (bbar, zm).",
           "# votes: H/G/I per column; '-' = that reader has no sign there.", ""]
    tot = {"cols": 0, "sup": 0, "all": 0, "open_unvalued": 0, "open_unread": 0, "letters": 0}
    for n, row in enumerate(rows, 1):
        sup, fill, full, st7 = strings(row)
        out += [f"line {n}", f"  supported:  {sup}", f"  with fill:  {fill}", f"  all three:  {full}"]
        if st7.strip():
            out.append(f"  stage 7:    {st7.rstrip()}")
        out.append("  " + " ".join("/".join(col.get(r) or "-" for r in READERS) for col, *_ in row))
        for col, cand, k, o, share, new in row:
            if k == NONE:
                continue
            tot["cols"] += 1
            if k == ANY:
                unread = sum(w for tok in col.values() for s, w in votes(tok) if s is None) + \
                    sum(1 for r in READERS if r not in col)
                tot["open_unread" if unread >= len(READERS) / 2 else "open_unvalued"] += 1
            else:
                tot["sup"] += 1
                tot["letters"] += len(o)
                tot["all"] += share >= 0.99
    out += ["", f"# columns read\t{tot['cols']}", f"# columns with a supported value\t{tot['sup']}",
            f"#   of those, all three readers\t{tot['all']}", f"# supported letters\t{tot['letters']}",
            f"# open: readers agree enough but the key has no value\t{tot['open_unvalued']}",
            f"# open: half the votes or more unread or missing\t{tot['open_unread']}"]
    open(os.path.join(RES, "b-lattice-read.txt"), "w").write("\n".join(out) + "\n")
    print("\n".join(out[-6:]))


def words():
    """b-words.txt: lines `line<TAB>phrase` (my word division; '?' allowed). For each, find the phrase's
    letters in that line's supported string and count the support under them."""
    rows = read_path()
    out = ["line\tphrase\tfound\tletters\tall_three\tone_or_two\topen\ton_stage7_values"]
    for ln in open(os.path.join(HERE, "b-words.txt"), encoding="utf-8"):
        if ln.startswith("#") or not ln.strip():
            continue
        n, phrase = ln.rstrip("\n").split("\t")[:2]
        sup, full, st7 = "", "", ""
        for k in (int(x) for x in n.split("-")):
            a, _, b, c = strings(rows[k - 1])
            sup, full, st7 = sup + a, full + b, st7 + c
        want = re.sub(r"[^a-z?]", "", phrase.lower())
        at = sup.find(want)
        if at < 0:
            out.append(f"{n}\t{phrase}\tno\t{len(want)}\t\t\t\t")
            continue
        seg, f, s7 = sup[at:at + len(want)], full[at:at + len(want)], st7[at:at + len(want)]
        out.append(f"{n}\t{phrase}\tyes\t{len(want)}\t{sum(a != '?' and b != '.' for a, b in zip(seg, f))}\t"
                   f"{f.count('.')}\t{seg.count('?')}\t{s7.count('^')}")
    open(os.path.join(RES, "b-words.tsv"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))


PLANT = 300                                                    # letters in a planted passage


def _plant(args):
    kind, seed = args
    lp, held, t = _G["lp"], _G["held"], _G["t"]
    rng = random.Random(seed)
    B = {v: k[2:] for k, v in t.items() if k.startswith("B:") and len(v) == 1}
    M = {v: k[2:] for k, v in t.items() if k.startswith("M:")}
    Wd = {}
    for k, v in t.items():
        if k.startswith("W:") and len(v) == 1:
            Wd.setdefault(v, []).append(k[2:])
    inv = sorted({b + "+" + m for b in B.values() for m in M.values()} | {s for v in Wd.values() for s in v})
    blank = ["delta", "beta", "gamma", "hash"]
    if kind == "italian":
        i = rng.randrange(len(held) - PLANT)
        plain = held[i:i + PLANT]
    else:
        plain = "".join(rng.choice(ALPHA) for _ in range(PLANT))
    true, j = [], 0
    while j < len(plain):
        a, b = plain[j], plain[j + 1:j + 2]
        if rng.random() < 0.15:                      # a sign the key does not hold
            true.append(rng.choice(blank))
            j += 1
        elif a in B and b in M and rng.random() < 0.8:
            true.append(B[a] + "+" + M[b])
            j += 2
        elif a in Wd:
            true.append(rng.choice(Wd[a]))
            j += 1
        else:
            true.append(rng.choice(blank))
            j += 1
    ws = sorted(k for k in t if k.startswith("W:"))
    hidden = set(rng.sample(ws, len(ws) // 4))
    km = {k: v for k, v in t.items() if k not in hidden}
    rows = {}
    for rd in READERS:
        r_ = []
        for s_ in true:
            x = rng.random()
            if x < 0.02:
                continue
            r_.append("?" if x < 0.06 else rng.choice(inv) if x < 0.14 else s_)
        rows[rd] = r_
    cols = columns(rows)
    sc, lm, n, path = best(cols, km, lp)
    below = sum(best(cols, shuffled(km, rng), lp)[0] < sc for _ in range(50))
    got = "".join("?" if k == ANY else o for k, o, _ in path)
    sm = difflib.SequenceMatcher(None, got, plain, autojunk=False)
    valued = sum(1 for s_ in true if value(s_, km)) / len(true)
    return below >= 48, sum(b_.size for b_ in sm.get_matching_blocks()), sum(1 for ch in got if ch != "?"), valued


def selftest():
    """Planted passages: 20 windows of held-out Italian and 20 of random letters, 300 letters each, enciphered
    with the real key's signs (base + mark where two letters allow it, an unvalued sign where the key has
    none, and for 15% of letters besides), then read by three noisy readers (8% of signs wrong, 4% unread, 2%
    dropped; a quarter of the key's whole-sign entries hidden, so that about 0.7 of the signs have a value
    as in letter B; hiding a quarter of bases and marks as well leaves under half valued and 12 of 20 pass). Reports how often the test passes (50 shuffles, bar 48) and the share of supported
    letters that are right. On planted lines of 80 letters the test is too weak to use: 9 of 20 Italian
    lines passed. The real test is on the whole letter, about 1,930 columns."""
    lp, held, _ = model()
    _G.update(lp=lp, held=held, t=key("key-v0.tsv"))
    out = ["kind\tpassed_of_20\tsupported_letters_right\tmean_share_of_signs_valued"]
    with multiprocessing.get_context("fork").Pool(8) as pool:
        for kind in ("italian", "random"):
            res = pool.map(_plant, [(kind, 100 * (kind == "random") + s) for s in range(1, 21)])
            out.append(f"{kind}\t{sum(r[0] for r in res)}\t{sum(r[1] for r in res)}/{sum(r[2] for r in res)}\t{sum(r[3] for r in res) / 20:.2f}")
    open(os.path.join(RES, "b-lattice-selftest.tsv"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    {"test": test, "read": read, "selftest": selftest, "words": words}[sys.argv[1]]()

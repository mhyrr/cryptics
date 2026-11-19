"""newvalues.py - stage 7 of no. 2351: are the blind table's extra values new values or errors? (README, "Stage 7")

    python3 newvalues.py check-A     results/newvalues-check-A.tsv   power check on the text the values came from
    python3 newvalues.py test        results/newvalues-test.tsv      the registered test, on letter B; run once
    python3 newvalues.py key         key-v1.tsv                      key-v0 rows unchanged, plus what passed

The candidates are the entries listed at the foot of results/compare-v2-v0.tsv (compare_tables.py). They were
built from letter A alone. Letter B has no clear text, so each is judged by a letter-trigram model against
other values put on the same sign, with key-v0.tsv held fixed around it.
"""
import collections, math, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "line"))
import align, solve, tied  # noqa: E402

W, RES = os.path.join(HERE, "work"), os.path.join(HERE, "results")
LOGV = math.log(len(solve.ALPHA))
MIN_PLACES = 6
NALT = 199
ERR_PLACES = 15


def candidates():
    """-> [(entry, blind value)] from the comparison file, in its order."""
    out = []
    for ln in open(os.path.join(RES, "compare-v2-v0.tsv"), encoding="utf-8"):
        m = re.match(r"# ([BMW]:\S+)\t(\S+)\t(\S+)\t", ln)
        if m:
            out.append((m.group(1), m.group(2)))
    return out


def lines_of(name):
    return [ln.split() for ln in open(os.path.join(W, name), encoding="utf-8")
            if ln.strip() and not ln.startswith("#")]


def piece(tok, t):
    """-> (value or None, parts) with parts the key entries used."""
    b, _, m = tok.partition("+")
    if "W:" + tok in t:
        return t["W:" + tok], ("W:" + tok,)
    if m in tied.VMARKS and "B:" + b in t and "M:" + m in t:
        return t["B:" + b] + t["M:" + m], ("B:" + b, "M:" + m)
    return None, ()


def decode(lines, t, entry=None):
    """-> runs: lists of (letter index, owner). owner is the place number when the letter comes from `entry`."""
    runs, cur, place = [], [], 0
    for ln in lines:
        for tok in ln:
            place += 1
            v, parts = piece(tok, t)
            if v is None:
                if cur:
                    runs.append(cur)
                cur = []
                continue
            if entry in parts and len(parts) == 2:        # base + mark: only the entry's own letters are owned
                lb = len(t[parts[0]])
                own = [place if (parts[0] == entry) == (k < lb) else None for k in range(len(v))]
            else:
                own = [place if entry in parts else None] * len(v)
            cur += list(zip(v, own))
        # a line end does not break a run: the text runs on
    if cur:
        runs.append(cur)
    return runs


def places(lines, t, entry):
    n = 0
    for ln in lines:
        for tok in ln:
            b, _, m = tok.partition("+")
            if entry[0] == "W":
                n += tok == entry[2:]
            elif entry[0] == "B":
                n += b == entry[2:] and m in tied.VMARKS and "M:" + m in t
            else:
                n += m == entry[2:] and "B:" + b in t and "W:" + tok not in t
    return n


def gain(lines, t, entry, lp, idx):
    """Sum of (log p + log 20) over trigrams that hold a letter of `entry` and are not wholly inside one of
    its places: how well the value fits what stands round it, against a uniform guess."""
    V, g = len(solve.ALPHA), 0.0
    for run in decode(lines, t, entry):
        for i in range(len(run) - 2):
            o = (run[i][1], run[i + 1][1], run[i + 2][1])
            if o == (None, None, None) or (o[0] is not None and o[0] == o[1] == o[2]):
                continue
            g += lp[idx[run[i][0]] * V * V + idx[run[i + 1][0]] * V + idx[run[i + 2][0]]] + LOGV
    return g


def total(lines, t, lp, idx):
    V, g = len(solve.ALPHA), 0.0
    for run in decode(lines, t):
        for i in range(len(run) - 2):
            g += lp[idx[run[i][0]] * V * V + idx[run[i + 1][0]] * V + idx[run[i + 2][0]]] + LOGV
    return g


def corpus_text():
    words = [align.norm_letters(w) for w in re.split(r"[^A-Za-zàèéìòù]+", open(os.path.join(
        HERE, "..", "2911", "print", "leoperediniccol03milagoog_djvu.txt"), encoding="utf-8", errors="replace").read())]
    return "".join(w for w in words if w and all(ch in solve.ALPHA for ch in w))


def alternatives(value, text, extra=()):
    if len(value) == 1:
        alts = [c for c in solve.ALPHA if c != value]
    else:
        n = len(value)
        c = collections.Counter(text[i:i + n] for i in range(len(text) - n + 1))
        alts = [g for g, _ in c.most_common(NALT + 1) if g != value][:NALT]
    return alts + [x for x in extra if x not in alts and x != value]


def judge(lines, t0, entry, value, alts, lp, idx):
    """-> (places, gain of the value, alternatives strictly below, number of alternatives, best alternative)."""
    t = dict(t0)
    t[entry] = value
    n = places(lines, t, entry)
    g = gain(lines, t, entry, lp, idx)
    ga = []
    for a in alts:
        t[entry] = a
        ga.append((gain(lines, t, entry, lp, idx), a))
    below = sum(x < g for x, _ in ga)
    return n, g, below, len(ga), max(ga) if ga else (0.0, "")


def run(name, outname, do_joint):
    lp, _, idx = solve.model()
    text = corpus_text()
    t0 = {r["unit"]: r["value"] for r in align.read_key(os.path.join(HERE, "key-v0.tsv"))}
    lines = lines_of(name)
    halves = {"whole": lines, "odd": lines[0::2], "even": lines[1::2]}
    out = ["entry\tvalue\tv0_value\tpart\tplaces\tgain\talts_below\talts\tshare_below\tbest_alt\tbest_alt_gain"]
    verdicts = []
    for entry, value in candidates():
        extra = (t0[entry],) if entry in t0 else ()
        alts = alternatives(value, text, extra)
        res = {}
        for part, ls in halves.items():
            n, g, below, na, (bg, ba) = judge(ls, t0, entry, value, alts, lp, idx)
            res[part] = (n, g, below / na)
            out.append(f"{entry}\t{value}\t{t0.get(entry, '-')}\t{part}\t{n}\t{g:.2f}\t{below}\t{na}\t{below / na:.3f}\t{ba}\t{bg:.2f}")
        n, g, sh = res["whole"]
        ok = n >= MIN_PLACES and g > 0 and sh >= 0.95
        beaten = False                   # a differing entry: does key-v0's own value fit better everywhere?
        if entry in t0:
            beaten = all(judge(ls, t0, entry, t0[entry], [], lp, idx)[1] > res[p][1] for p, ls in halves.items())
        if beaten or (n >= ERR_PLACES and g <= 0 and sh < 0.5):
            v = "error"
        elif not ok:
            v = "unknown"
        elif all(res[p][1] > 0 and res[p][2] >= 0.95 for p in ("odd", "even")):
            v = "certain"
        elif all(res[p][2] >= 0.75 for p in ("odd", "even")):
            v = "probable"
        else:
            v = "unknown"
        verdicts.append((entry, value, v, n))
    new = [(e, v) for e, v in candidates() if e not in t0]
    met = tried = 0                      # power: key-v0's own entries, one at a time, by the whole-text bar
    for e, v in t0.items():
        n, g, below, na, _ = judge(lines, t0, e, v, alternatives(v, text), lp, idx)
        if n >= MIN_PLACES:
            tried += 1
            met += g > 0 and below / na >= 0.95
    out += ["", f"# power: key-v0 entries with {MIN_PLACES} places or more that meet the whole-text bar\t{met} of {tried}"]
    if do_joint:
        t = dict(t0)
        t.update(new)
        true = total(lines, t, lp, idx)
        rng, sh = random.Random(1), []
        for _ in range(200):
            vs = [v for _, v in new]
            rng.shuffle(vs)
            t.update(zip([e for e, _ in new], vs))
            sh.append(total(lines, t, lp, idx))
        below = sum(x < true for x in sh)
        joint = below >= 190
        out += ["", f"# joint: key-v0 plus the {len(new)} new entries, total gain\t{true:.2f}",
                f"# joint: key-v0 alone\t{total(lines, t0, lp, idx):.2f}",
                f"# joint: shuffles below\t{below} of 200", f"# joint: shuffle mean\t{sum(sh) / len(sh):.2f}",
                f"# joint: shuffle max\t{max(sh):.2f}", f"# joint: pass\t{joint}"]
        if not joint:
            verdicts = [(e, v, "probable" if s == "certain" else s, n) for e, v, s, n in verdicts]
    out.append("")
    out += [f"# verdict\t{e}\t{v}\t{s}\tplaces {n}" for e, v, s, n in verdicts]
    open(os.path.join(RES, outname), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\n".join(out))


def key():
    """key-v1.tsv: every row of key-v0.tsv as it stands, then the entries that passed, with their places."""
    rows = align.read_key(os.path.join(HERE, "key-v0.tsv"))
    t0 = {r["unit"]: r["value"] for r in rows}
    lines = lines_of("B-merged.txt")
    whole = {}
    for ln in open(os.path.join(RES, "newvalues-test.tsv"), encoding="utf-8"):
        f = ln.rstrip("\n").split("\t")
        if len(f) > 8 and f[3] == "whole":
            whole[f[0]] = f
    for ln in open(os.path.join(RES, "newvalues-test.tsv"), encoding="utf-8"):
        if not ln.startswith("# verdict"):
            continue
        _, e, v, s, _ = ln.rstrip("\n").split("\t")
        if e in t0 or s == "error":      # key-v0's rows are never overwritten; an error is not entered
            continue
        t = dict(t0)
        t[e] = v
        where = []
        for i, toks in enumerate(lines, 1):
            for j, tok in enumerate(toks, 1):
                if e in piece(tok, t)[1]:
                    where.append(f"{i}.{j}")
        f = whole[e]
        rows.append(dict(unit=e, value=v, type=align.unit_type(v), support=f[6], conflict=int(f[7]) - int(f[6]),
                         share=f[8], status=s, alts="stage 7: blind build on letter A, tested on letter B",
                         positions="B " + " ".join(where)))
    align.write_key(rows, os.path.join(HERE, "key-v1.tsv"))
    print("\n".join(f"{r['unit']}\t{r['value']}\t{r['status']}" for r in rows[len(t0):]))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "check-A":
        run("A-merged.txt", "newvalues-check-A.tsv", False)
    elif cmd == "test":
        run("B-merged.txt", "newvalues-test.tsv", True)
    else:
        key()

"""tied.py - a builder for a cipher that writes a consonant as a base and the vowel after it as a mark (H9).

    python3 tied.py synth [--seed 1] [--keep 0.4]     a planted pair with the real pair's holes; reports recovery
    python3 tied.py build cipher.txt plain.txt out.tsv
The cipher is read in order against the plain text with a pointer, as in align.beam_read, but the table has
three kinds of entry, and a sign with a mark has no value of its own:
    B:<base>   one consonant           for a base that takes the vowel marks
    M:<mark>   one vowel               for a vowel mark
    W:<sign>   one to three letters    for a sign that never takes a vowel mark
A marked sign spells consonant(base) + vowel(mark). An unmarked base of the first kind spells its consonant.
An entry met for the first time takes its value from the letters at the pointer and earns nothing; an entry
met again must spell its value and earns one point a letter. Stretches of cipher with no plain text under
them are gaps (cheap to open at a hole in the plain text). No value is typed in; which bases are of the
first kind is read off the cipher text alone (a base seen with a vowel mark three times or more).
Rows are marked by evidence as in align.mark_by_evidence: hits and misses against chance.
"""
import math, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "line"))
import align  # noqa: E402

VMARKS = ("1", "3", "4", "5", "~")
VOW = set("aeiou")
BEAM, PERJ = int(os.environ.get("TIED_BEAM", 3000)), 40
OPEN, EXT, MISS, DMAX = 3.0, 0.1, 0.4, 2
LAC_OPEN = 1.0
PASSES = 3
HIT = 0.55


def split(sym):
    b, _, m = sym.partition("+")
    return b, m


def markable(units):
    n = {}
    for u in units:
        if u.kind == "sign" and u.sym != "?":
            b, m = split(u.sym)
            if m in VMARKS:
                n[b] = n.get(b, 0) + 1
    return {b for b, c in n.items() if c >= 3}


def parts(sym, mk):
    """-> ('BM', base, mark) | ('B', base, None) | ('W', sym, None)"""
    b, m = split(sym)
    if b in mk and m in VMARKS:
        return "BM", b, m
    if b in mk and not m:
        return "B", b, None
    return "W", sym, None


def new_cost(v, inv):
    c = 0.0 if len(v) == 1 else 1.0 if len(v) == 2 else 1.5
    return c + (0.7 if v in inv else 0.0)


def search(units, P, lac, mk, known=None):
    """-> (score, table, ops). ops[i] = (kind, j0, j1, hits, misses): hits and misses are lists of table keys
    that spelled, or failed to spell, their value at this unit."""
    m = len(P)
    start = dict(known or {})
    s0 = hash(tuple(sorted(start.items())))
    hyps = [(0.0, 0, 0, start, s0, None), (-EXT, 0, 1, start, s0, None)]
    for i, u in enumerate(units):
        new = {}

        def put(sc, j, g, tab, sig, hist):
            k = (j, g, sig)
            h = new.get(k)
            if h is None or sc > h[0]:
                new[k] = (sc, j, g, tab, sig, hist)

        def extend(tab, sig, **kv):
            t2 = dict(tab)
            t2.update(kv)
            return t2, sig ^ hash(tuple(sorted(kv.items())))

        for sc, j, g, tab, sig, hist in hyps:
            if g:
                put(sc - EXT, j, 1, tab, sig, (hist, "G", j, j, (), ()))
            if u.kind == "clear":
                put(sc, j, 0, tab, sig, (hist, "C", j, j, (), ()))
                continue
            if u.sym == "?":
                for ln, c in ((1, 0.3), (2, 0.5), (0, 1.0)):
                    if j + ln <= m:
                        put(sc - c, j + ln, 0, tab, sig, (hist, "Q", j, j + ln, (), ()))
                if not g:
                    put(sc - (LAC_OPEN if lac[j] else OPEN), j, 1, tab, sig, (hist, "G", j, j, (), ()))
                continue
            kind, a, b = parts(u.sym, mk)
            if kind == "BM":
                kb, km = "B:" + a, "M:" + b
                c, v = tab.get(kb), tab.get(km)
                for d in range(DMAX + 1):
                    x = j + d
                    if x + 2 > m:
                        break
                    pc, pv = P[x], P[x + 1]
                    if pc in VOW or pv not in VOW:
                        continue
                    pen = d * MISS
                    if c is not None and v is not None:
                        if pc == c and pv == v:
                            put(sc + 2 - pen, x + 2, 0, tab, sig, (hist, "M", x, x + 2, (kb, km), ()))
                            break
                        if pc == c:
                            put(sc + 1 - MISS - pen, x + 2, 0, tab, sig, (hist, "S", x, x + 2, (kb,), (km,)))
                        elif pv == v:
                            put(sc + 1 - MISS - pen, x + 2, 0, tab, sig, (hist, "S", x, x + 2, (km,), (kb,)))
                    elif c is not None:
                        if pc == c:
                            t2, s2 = extend(tab, sig, **{km: pv})
                            put(sc + 1 - pen, x + 2, 0, t2, s2, (hist, "A", x, x + 2, (kb,), ()))
                    elif v is not None:
                        if pv == v:
                            t2, s2 = extend(tab, sig, **{kb: pc})
                            put(sc + 1 - pen, x + 2, 0, t2, s2, (hist, "A", x, x + 2, (km,), ()))
                    elif d == 0:
                        t2, s2 = extend(tab, sig, **{kb: pc, km: pv})
                        put(sc - 0.2, x + 2, 0, t2, s2, (hist, "A", x, x + 2, (), ()))
                miss = tuple(k for k in (kb, km) if k in tab)
                if j + 2 <= m:
                    put(sc - MISS, j + 2, 0, tab, sig, (hist, "S", j, j + 2, (), miss))
                put(sc - MISS, j, 0, tab, sig, (hist, "I", j, j, (), miss))
            elif kind == "B":
                kb = "B:" + a
                c = tab.get(kb)
                if c is not None:
                    hit = False
                    for d in range(DMAX + 1):
                        if j + d < m and P[j + d] == c:
                            put(sc + 1 - d * MISS, j + d + 1, 0, tab, sig, (hist, "M", j + d, j + d + 1, (kb,), ()))
                            hit = d == 0
                            break
                    if not hit:
                        if j + 1 <= m:
                            put(sc - MISS, j + 1, 0, tab, sig, (hist, "S", j, j + 1, (), (kb,)))
                        put(sc - MISS, j, 0, tab, sig, (hist, "I", j, j, (), (kb,)))
                else:
                    if j < m and P[j] not in VOW:
                        t2, s2 = extend(tab, sig, **{kb: P[j]})
                        put(sc, j + 1, 0, t2, s2, (hist, "A", j, j + 1, (), ()))
                    put(sc - MISS, j, 0, tab, sig, (hist, "I", j, j, (), ()))
            else:
                kw = "W:" + a
                v = tab.get(kw)
                if v is not None:
                    ln, hit = len(v), False
                    for d in range(DMAX + 1):
                        if P.startswith(v, j + d):
                            put(sc + ln - d * MISS, j + d + ln, 0, tab, sig, (hist, "M", j + d, j + d + ln, (kw,), ()))
                            hit = d == 0
                            break
                    if not hit:
                        if j + ln <= m:
                            put(sc - MISS, j + ln, 0, tab, sig, (hist, "S", j, j + ln, (), (kw,)))
                        put(sc - MISS, j, 0, tab, sig, (hist, "I", j, j, (), (kw,)))
                else:
                    inv = set(x for k, x in tab.items() if k[0] == "W")
                    for ln in (1, 2, 3):
                        if j + ln > m:
                            break
                        val = P[j:j + ln]
                        t2, s2 = extend(tab, sig, **{kw: val})
                        put(sc - new_cost(val, inv), j + ln, 0, t2, s2, (hist, "A", j, j + ln, (), ()))
                    put(sc - MISS, j, 0, tab, sig, (hist, "I", j, j, (), ()))
            if not g:
                put(sc - (LAC_OPEN if lac[j] else OPEN), j, 1, tab, sig, (hist, "G", j, j, (), ()))
        ranked = sorted(new.values(), key=lambda h: -h[0])
        hyps, per = [], {}
        for h in ranked:
            c = per.get(h[1], 0)
            if c < PERJ:
                per[h[1]] = c + 1
                hyps.append(h)
                if len(hyps) >= BEAM:
                    break
    best = hyps[0]
    ops, h = [], best[5]
    while h is not None:
        ops.append(h[1:])
        h = h[0]
    ops.reverse()
    return best[0], best[3], ops


def rows_from(P, tab, ops):
    hit, miss = {}, {}
    for kind, j0, j1, hs, ms in ops:
        for k in hs:
            hit[k] = hit.get(k, 0) + 1
        for k in ms:
            miss[k] = miss.get(k, 0) + 1
    freq = {}
    for ln in (1, 2, 3):
        for j in range(len(P) - ln + 1):
            freq[P[j:j + ln]] = freq.get(P[j:j + ln], 0) + 1
    rows = []
    for k, v in tab.items():
        h, x = hit.get(k, 0), miss.get(k, 0)
        pc = min(0.5, 3.0 * freq.get(v, 0) / len(P))
        ev = h * math.log(HIT / max(pc, 1e-4)) + x * math.log((1 - HIT) / (1 - pc))
        status = "certain" if ev >= 10 and h >= 5 else "probable" if ev >= 4 and h >= 3 else "unknown"
        rows.append(dict(unit=k, value=v, type=align.unit_type(v), support=h, conflict=x,
                         share=round(h / max(1, h + x), 3), status=status, alts=f"ev {ev:.1f}", positions=""))
    rows.sort(key=lambda r: (-r["support"], r["unit"]))
    return rows


def build(units, P, lac, log=None):
    mk = markable(units)
    known = {}
    for k in range(PASSES):
        score, tab, ops = search(units, P, lac, mk, known)
        rows = rows_from(P, tab, ops)
        kinds = {}
        for o in ops:
            kinds[o[0]] = kinds.get(o[0], 0) + 1
        if log:
            log(f"pass {k + 1}: held {len(known)}; score {score:.1f}; path {' '.join(f'{a}={b}' for a, b in sorted(kinds.items()))}")
        known = {r["unit"]: r["value"] for r in rows if r["status"] == "certain"}
    return rows, mk


def sign_values(rows, mk, signs, minimum=("certain", "probable")):
    """-> {sign: value} for every sign whose parts are marked."""
    t = {r["unit"]: r["value"] for r in rows if r["status"] in minimum}
    out = {}
    for s in signs:
        kind, a, b = parts(s, mk)
        if kind == "BM" and "B:" + a in t and "M:" + b in t:
            out[s] = t["B:" + a] + t["M:" + b]
        elif kind == "B" and "B:" + a in t:
            out[s] = t["B:" + a]
        elif kind == "W" and "W:" + a in t:
            out[s] = t["W:" + a]
    return out


# ---------------------------------------------------------------- planted pair
def synth(seed=1, keep=0.4, n_letters=1500, unread=0.035, wrong=0.03, word_err=0.1):
    """A planted cipher of the H9 kind over real Italian, with the plain side cut to `keep` of its words in
    runs, the way the readers' texts of c. 233 are."""
    rng = random.Random(seed)
    corpus = os.path.join(HERE, "..", "2911", "print", "leoperediniccol03milagoog_djvu.txt")
    words = [align.norm_letters(w) for w in re.split(r"[^A-Za-zàèéìòù]+", open(corpus, encoding="utf-8", errors="replace").read())]
    words = [w for w in words if w and all(ch in "abcdefghilmnopqrstuz" for ch in w)]
    i = rng.randrange(20000, len(words) - 2000)
    text, n = [], 0
    while n < n_letters:
        text.append(words[i])
        n += len(words[i])
        i += 1
    cons = sorted(set("".join(text)) - VOW)
    bases = [f"b{k}" for k in range(len(cons))]
    rng.shuffle(bases)
    cb = dict(zip(cons, bases))
    marks = list(VMARKS)
    rng.shuffle(marks)
    vm = dict(zip("aeiou", marks))
    whole = {v: [f"w{v}{k}" for k in range(2)] for v in "aeiou"}
    codes = {}
    for w in ("che", "non", "per", "con", "et"):
        codes[w] = "k" + w
    signs = []                                   # (sign, word index)
    for wi, w in enumerate(text):
        if w in codes and rng.random() < 0.7:
            signs.append((codes[w], wi))
            continue
        j = 0
        while j < len(w):
            ch = w[j]
            if ch not in VOW and j + 1 < len(w) and w[j + 1] in VOW:
                signs.append((cb[ch] + "+" + vm[w[j + 1]], wi))
                j += 2
            elif ch not in VOW:
                signs.append((cb[ch], wi))
                j += 1
            else:
                signs.append((rng.choice(whole[ch]), wi))
                j += 1
    allsigns = sorted({s for s, _ in signs})
    shown = []
    for s, _ in signs:
        r = rng.random()
        shown.append("?" if r < unread else rng.choice(allsigns) if r < unread + wrong else s)
    plain, on = [], True
    for wi, w in enumerate(text):
        if rng.random() < (0.28 if on else 0.42):  # runs of read words and of holes
            on = not on
        if on and rng.random() < keep / 0.6:
            if rng.random() < word_err:
                w = "".join(rng.choice("aeioulnrst") if rng.random() < 0.3 else ch for ch in w)
            plain.append(w)
        elif not plain or plain[-1] != "[...]":
            plain.append("[...]")
    truth = {"B:" + b: c for c, b in cb.items()}
    truth.update({"M:" + m: v for v, m in vm.items()})
    for v, ws in whole.items():
        for w in ws:
            truth["W:" + w] = v
    for w, k in codes.items():
        truth["W:" + k] = w
    ctext = "\n".join(" ".join(shown[k:k + 46]) for k in range(0, len(shown), 46)) + "\n"
    return ctext, " ".join(plain) + "\n", truth, len(signs), sum(len(w) for w in plain if w != "[...]")


def run_synth(argv):
    opt = lambda name, d: float(argv[argv.index(name) + 1]) if name in argv else d
    seed, keep = int(opt("--seed", 1)), opt("--keep", 0.4)
    ctext, ptext, truth, nsigns, nlet = synth(seed, keep)
    units, _, _ = align.parse_cipher(ctext)
    P, wb, lac, _ = align.parse_plain(ptext)
    logs = []
    rows, mk = build(units, P, lac, logs.append)
    marked = [r for r in rows if r["status"] != "unknown"]
    right = sum(truth.get(r["unit"]) == r["value"] for r in marked)
    bm = [r for r in marked if r["unit"][0] in "BM"]
    print("\n".join(logs))
    print(f"seed {seed}: signs {nsigns}, plain letters kept {nlet}, holes {ptext.count('[...]')}")
    print(f"marked rows {len(marked)}: right {right}, wrong {len(marked) - right}; "
          f"bases and marks marked {len(bm)} of {sum(1 for k in truth if k[0] in 'BM')}, right "
          f"{sum(truth.get(r['unit']) == r['value'] for r in bm)}")
    return len(marked), right


def run_build(cpath, ppath, out):
    units, P, wb, lac, _ = align.load_pair(cpath, ppath)
    logs = []
    rows, mk = build(units, P, lac, logs.append)
    align.write_key(rows, out)
    st = {}
    for r in rows:
        st[r["status"]] = st.get(r["status"], 0) + 1
    print(f"{logs[-1]}; rows {st}; bases that take marks: {len(mk)}")


if __name__ == "__main__":
    if sys.argv[1] == "synth":
        run_synth(sys.argv[2:])
    else:
        run_build(*sys.argv[2:5])

"""stage7.py - widen key-v2.tsv with values proposed from part of c. 652r, tested on text held out
(README, "Seventh stage"). Run in this order, once each:

    python3 stage7.py propose   results/stage7-propose.tsv   values from c. 652r lines 4-5, 10-12 + clear frame
    python3 stage7.py test      results/stage7-test.tsv      the registered test on the held-out text
    python3 stage7.py key       key-v3.tsv                   only if the test file says pass
    python3 stage7.py read      results/stage7-read.txt      only after the test result is committed

Inputs: readers J K L M (c652.txt), E F A B (c14.txt), C D A B (c269.txt), PA (p270.txt), key-v2.tsv,
key-c269-m4.tsv, key-c44-v0.tsv. Readers N and O are not read. key-v2.tsv is never written.

A run is a list of columns; a column is {sign | None (unread) | NONE (no sign here): share of the votes}.
A run is scored as in lattice.py: log vote share plus letter trigrams, an unvalued or unread vote is "any one
letter" at a cost of log 20. New here: a run may have fixed letters before and after it (the clear frame).
"""
import math, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "line"))
import align, merge  # noqa: E402
import lattice, lattice652, run  # noqa: E402

R, RES = os.path.join(HERE, "readers"), os.path.join(HERE, "results")
KEY2, KEY3 = os.path.join(HERE, "key-v2.tsv"), os.path.join(HERE, "key-v3.tsv")
ANY, NONE, ALPHA, EPS = lattice.ANY, lattice.NONE, lattice.ALPHA, lattice.EPS
CLR = lattice652.CLR
MIN_WEIGHT = 2.0          # votes for a sign in the proposal runs, in places, before it may be given a value
SHUFFLES, SEED, BAR = 200, 1, 190

# c. 652r rows as the readers wrote them: rows 1..8 are lines 4, 5, 6, 7, 8, 10, 11, 12.
# The cipher runs on from line 4 to line 5 and from line 5 to line 6 without a clear word between.
# Clear frame: the last two letters before a run and the first two after it, only where PJ and PK give the
# same letters and the word is written out (no abbreviation). '' where they differ or the neighbour is held out.
#   (row, segment) segments are the stretches of a row between [[clear]] columns, counted from 0.
PROPOSE = [                      # (name, [(row, segment), ...] chained, before, after)
    ("lines 4-5a", [(1, 0), (2, 0)], "sa", "a"),      # "nella cosa" | run | "a S. S.ta"
    ("line 5b", [(2, 1)], "lo", ""),                  # "celo" / "uelo" | run | line 6 (held out)
    ("line 10", [(6, 0)], "ge", ""),                  # "si aggiunge" | run | "da alcuni" / "Se alcuno"
    ("line 11", [(7, 0)], "er", "pe"),                # "hauer" / "Sauer" | run | "per la quale"
    ("line 12", [(8, 0)], "le", ""),                  # "per la quale" | run | "haa" / "Sua"
]
HELD652 = [("lines 6-7", [(3, 0), (4, 0)], "", "")]  # row 5 (line 8: two valued signs) is in neither set
C14_BEFORE = "oe"                                    # "il tutto e" (PC and PD agree)


# ------------------------------------------------------------------ runs
def segments(cols):
    """one c. 652r row -> list of segments; a segment is a list of vote columns."""
    out, cur = [], []
    for col in cols:
        t = merge.tally(col, len(lattice652.READERS), lattice.RENAME)
        if t.get(CLR, 0) >= 0.5:
            if cur:
                out.append(cur)
            cur = []
        else:
            t.pop(CLR, None)
            cur.append(t)
    if cur:
        out.append(cur)
    return out


def runs652(spec):
    rows = [segments(c) for c in lattice652.columns()]
    return [(name, [col for r, s in parts for col in rows[r - 1][s]], b, a) for name, parts, b, a in spec]


def run14():
    cols, readers = lattice.columns()
    out = []
    for col in cols:
        t = {}
        for rd in readers:
            tok = col.get(rd)
            for s, w in ([(NONE, 1.0)] if tok is None else lattice.votes(tok)):
                t[s] = t.get(s, 0) + w / len(readers)
        out.append(t)
    return [("c14", out, C14_BEFORE, "")]


def runs269():
    """The runs of results/omitted.txt, made again from the readers' files with key-v2.tsv held: three or
    more signs of the four-reader merge with no counterpart in the c. 270r text. One merged token a place."""
    files = [merge.read_rows(os.path.join(R, x, "c269.txt")) for x in "CDAB"]
    text = "\n".join(" ".join(merge.merge_line([f[k] for f in files], 0.5, lattice.RENAME)[0])
                     for k in range(len(files[0])))
    units, _, _ = align.parse_cipher(text)
    P, _, lac, _ = align.parse_plain(" ".join(run.plain_words(run.rd(R, "PA", "p270.txt"))))
    _, _, ops = align.beam_read(units, P, lac, None, table2())
    out, i = [], 0
    while i < len(ops):
        if ops[i][0] in "GI":
            j = i
            while j < len(ops) and ops[j][0] in "GI":
                j += 1
            if j - i >= 3:
                ptr = ops[i][1]
                cols = [{(None if u.sym == "?" else u.sym): 1.0} for u in units[i:j]]
                out.append((f"c269 run {len(out) + 1} (line {units[i].line})", cols, P[max(0, ptr - 2):ptr], P[ptr:ptr + 2]))
            i = j
        else:
            i += 1
    return out


def held_runs():
    return runs652(HELD652) + run14() + runs269()


# ------------------------------------------------------------------ scoring
def best(cols, kmap, lp, before="", after=""):
    """-> (score, path). path: [(candidate, emitted, share)] per column."""
    b2 = ("^^" + before)[-2:]
    states = {(b2[0], b2[1]): (0.0, None)}

    def step(a, b, o):
        add = 0.0
        for ch in o:
            if a != "^":
                add += lp(a, b, ch)
            a, b = b, ch
        return a, b, add
    for col in cols:
        cand = {}
        for s, w in col.items():
            k = NONE if s == NONE else (kmap.get(s) if s else None) or ANY
            cand[k] = cand.get(k, 0) + w
        new = {}
        for (a, b), (sc, hist) in states.items():
            for k, share in cand.items():
                base = sc + math.log(max(share, EPS)) - (math.log(len(ALPHA)) if k == ANY else 0.0)
                for o in ([NONE] if k == NONE else list(ALPHA) if k == ANY else [k]):
                    x, y, add = step(a, b, o)
                    if (x, y) not in new or base + add > new[(x, y)][0]:
                        new[(x, y)] = (base + add, (hist, k, o, share))
        states = new
    sc, hist = max(((v[0] + step(a, b, after)[2], v[1]) for (a, b), v in states.items()), key=lambda v: v[0])
    path = []
    while hist is not None:
        path.append(hist[1:])
        hist = hist[0]
    path.reverse()
    return sc, path


def total(runs, kmap, lp):
    return sum(best(cols, kmap, lp, b, a)[0] for _, cols, b, a in runs)


def weight(runs):
    w = {}
    for _, cols, _, _ in runs:
        for col in cols:
            for s, x in col.items():
                if s and s != NONE:
                    w[s] = w.get(s, 0) + x
    return w


def table2():
    return align.key_map(align.read_key(KEY2))


# ------------------------------------------------------------------ propose
def propose():
    lp, _, _ = lattice.model()
    runs, k2 = runs652(PROPOSE), table2()
    w = weight(runs)
    elig = sorted((s for s in w if s not in k2 and w[s] >= MIN_WEIGHT), key=lambda s: (-w[s], s))
    tab, base = dict(k2), total(runs, k2, lp)
    for _ in range(10):
        changed = False
        for s in elig:
            rest = {k: v for k, v in tab.items() if k != s}
            sc = sorted(((total(runs, dict(rest, **{s: ch}), lp), ch) for ch in ALPHA), reverse=True)
            new = sc[0][1] if sc[0][0] > total(runs, rest, lp) else None
            if new != tab.get(s):
                changed = True
            tab = dict(rest, **({s: new} if new else {}))
        if not changed:
            break
    out = [f"proposal_runs\t{' ; '.join(n for n, _, _, _ in runs)}", f"columns\t{sum(len(c) for _, c, _, _ in runs)}",
           f"score_key_v2\t{base:.2f}", f"score_with_proposals\t{total(runs, tab, lp):.2f}",
           f"unvalued_signs_seen\t{' '.join(f'{s}:{w[s]:.2f}' for s in sorted(w, key=lambda s: -w[s]) if s not in k2)}",
           f"eligible (weight >= {MIN_WEIGHT})\t{' '.join(elig) or '-'}",
           "sign\tweight\tvalue\tgain_over_unvalued\tmargin_over_second\tsecond"]
    for s in elig:
        rest = {k: v for k, v in tab.items() if k != s}
        sc = sorted(((total(runs, dict(rest, **{s: ch}), lp), ch) for ch in ALPHA), reverse=True)
        out.append(f"{s}\t{w[s]:.2f}\t{tab.get(s, '-')}\t{sc[0][0] - total(runs, rest, lp):.2f}\t"
                   f"{sc[0][0] - sc[1][0]:.2f}\t{sc[1][1]}")
    open(os.path.join(RES, "stage7-propose.tsv"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))


def proposals():
    rows = [ln.split("\t") for ln in open(os.path.join(RES, "stage7-propose.tsv")).read().splitlines()]
    at = [i for i, r in enumerate(rows) if r[0] == "sign"][0]
    return {r[0]: r[2] for r in rows[at + 1:] if r[2] != "-"}


# ------------------------------------------------------------------ test
def pair(sign, value):
    """-> (hits, misses, text): what the two blind builds on paired text hold for this sign (rows under
    their bar included). Another value there counts its support as misses."""
    h = m = 0
    notes = []
    for name in ("key-c269-m4.tsv", "key-c44-v0.tsv"):
        for r in align.read_key(os.path.join(HERE, name)):
            if r["unit"] == sign:
                if r["value"] == value:
                    h, m = h + r["support"], m + r["conflict"]
                else:
                    m += r["support"] + r["conflict"]
                notes.append(f"{name[4:-4]}: {r['value']} {r['support']}/{r['support'] + r['conflict']}")
    return h, m, "; ".join(notes) or "not in the pairs"


def status(d, rank, h, ph, pm):
    contradicted = ph + pm >= 3 and ph < 0.5 * (ph + pm)
    if d > 0 and rank == 1 and h >= 3 and ph >= 3 and ph >= 0.75 * (ph + pm):
        return "certain"
    if d > 0 and rank <= 3 and h >= 2 and not contradicted:
        return "probable"
    return "unknown"


def test():
    lp, _, _ = lattice.model()
    runs, k2, prop = held_runs(), table2(), proposals()
    out = [f"proposed\t{' '.join(f'{s}={v}' for s, v in prop.items()) or '-'}"]
    if not prop:
        out += ["pass\tFalse", "reason\tno sign met the proposal rule; nothing to test"]
        open(os.path.join(RES, "stage7-test.tsv"), "w").write("\n".join(out) + "\n")
        print("\n".join(out))
        return
    k3 = dict(k2, **prop)
    parts = {"c652 lines 6-7": [r for r in runs if r[0] == "lines 6-7"], "c14": [r for r in runs if r[0] == "c14"],
             "c269 omitted runs": [r for r in runs if r[0].startswith("c269")]}
    t3, t2 = total(runs, k3, lp), total(runs, k2, lp)
    rng, signs, vals, sh = random.Random(SEED), list(k3), [k3[s] for s in k3], []
    for _ in range(SHUFFLES):
        v = vals[:]
        rng.shuffle(v)
        ctl = dict(zip(signs, v))
        ctl.update(k2)                               # the 28 old rows keep their values; new signs keep the draw
        sh.append(total(runs, ctl, lp))
    below = sum(x < t3 for x in sh)
    ok = below >= BAR and t3 > t2
    hw = weight(runs)
    out += [f"held_out_runs\t{len(runs)}", f"held_out_columns\t{sum(len(c) for _, c, _, _ in runs)}",
            f"score_key_v2\t{t2:.2f}", f"score_key_v2_plus_proposals\t{t3:.2f}"]
    out += [f"  part {n}\tcolumns {sum(len(c) for _, c, _, _ in rs)}\tv2 {total(rs, k2, lp):.2f}\t"
            f"with proposals {total(rs, k3, lp):.2f}" for n, rs in parts.items()]
    out += [f"controls_below_true\t{below} of {SHUFFLES}", f"control_score_mean\t{sum(sh) / len(sh):.2f}",
            f"control_score_max\t{max(sh):.2f}", f"control_score_min\t{min(sh):.2f}",
            f"above_key_v2\t{t3 > t2}", f"pass\t{ok}",
            "sign\tvalue\theld_weight\tgain_leave_one_out\trank_of_20\tbest_letter\tpair_hits\tpair_misses\tpair\tstatus_if_pass"]
    for s, v in prop.items():
        rest = {k: x for k, x in k3.items() if k != s}
        sc = sorted(((total(runs, dict(rest, **{s: ch}), lp), ch) for ch in ALPHA), reverse=True)
        rank = [ch for _, ch in sc].index(v) + 1 if v in ALPHA else 0
        d = t3 - total(runs, rest, lp)
        ph, pm, note = pair(s, v)
        out.append(f"{s}\t{v}\t{hw.get(s, 0):.2f}\t{d:.2f}\t{rank}\t{sc[0][1]}\t{ph}\t{pm}\t{note}\t"
                   f"{status(d, rank, hw.get(s, 0), ph, pm)}")
    open(os.path.join(RES, "stage7-test.tsv"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))


# ------------------------------------------------------------------ key and reading (after the test)
def key():
    rows = [ln.split("\t") for ln in open(os.path.join(RES, "stage7-test.tsv")).read().splitlines()]
    if ["pass", "True"] not in rows:
        raise SystemExit("the test did not pass: no key-v3.tsv")
    at = [i for i, r in enumerate(rows) if r[0] == "sign"][0]
    pw = weight(runs652(PROPOSE))
    old = align.read_key(KEY2)
    new = [dict(unit=r[0], value=r[1], type="letter", support=int(r[6]), conflict=int(r[7]),
                share=round(int(r[6]) / max(1, int(r[6]) + int(r[7])), 3), status=r[9],
                alts=f"stage 7: proposed from c652 lines 4-5, 10-12 ({pw[r[0]]:.1f} places); held-out weight {r[2]}, "
                     f"gain {r[3]}, rank {r[4]} of 20; pairs: {r[8]}", positions="") for r in rows[at + 1:]]
    align.write_key(old + new, KEY3)
    print("\n".join(f"{r['unit']}\t{r['value']}\t{r['status']}" for r in new))


def read():
    lp, _, _ = lattice.model()
    name = "key-v3.tsv" if os.path.exists(KEY3) else "key-v2.tsv"
    kmap = align.key_map(align.read_key(os.path.join(HERE, name)))
    out = [f"table: {name}, {len(kmap)} values in force (certain or probable)"]
    for label, rs in (("c. 652r, proposal runs", runs652(PROPOSE)), ("held out", held_runs())):
        out.append(f"## {label}")
        for n, cols, b, a in rs:
            _, path = best(cols, kmap, lp, b, a)
            shown = [(("?" if k == ANY else o), o.upper() if k == ANY else o, share) for k, o, share in path if k != NONE]
            out += [f"{n}  [before '{b}', after '{a}']", "  supported:  " + "".join(s for s, _, _ in shown),
                    "  with fill:  " + "".join(f for _, f, _ in shown),
                    "  all votes:  " + "".join(s if sh >= 0.99 else "." * len(s) for s, _, sh in shown),
                    "  " + " ".join("/".join(f"{'-' if s == NONE else s or '?'}:{w:.2f}".replace(":1.00", "")
                                             for s, w in sorted(col.items(), key=lambda e: -e[1])) for col in cols)]
    out += ["", "supported: letters some vote's sign has a value for; ? = none. with fill: the letter model's guess",
            "at ? in capitals (not evidence). all votes: letters every vote supports."]
    open(os.path.join(RES, "stage7-read.txt"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    {"propose": propose, "test": test, "key": key, "read": read}[sys.argv[1]]()

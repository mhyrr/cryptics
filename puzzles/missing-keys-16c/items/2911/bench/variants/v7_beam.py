"""v7: read the cipher in order against the plain text, carrying the table as part of each hypothesis.

This is how a person rebuilds a key from a deciphered letter. Walk the cipher from its first sign with a
pointer in the plain text. A sign met for the first time takes its value from the letters at the pointer
(1, 2 or 3 of them): that costs little and earns nothing. A sign met again must spell its value at the
pointer: that earns one point per letter. If it does not, the hypothesis pays (a sign with no counterpart, a
different spelling, a skipped plain letter) or opens a gap: a run of cipher the plain side leaves out, with
the pointer held. The table is never fitted globally; a hypothesis is one table plus one pointer, and a beam
keeps the best few thousand. Wrong segmentations die because their signs fail to repeat.

No null value exists in this builder (step 3 of the prompt: no direct evidence, no null). No value is typed
in. A builder sees only its cipher file and its plain file.

build() then marks a row from the support its value has on the best path:
  The plain side is a loose abridgement: a right value spells it at about HIT of its places, a wrong one at
  CHANCE. Evidence = hits * log(HIT/CHANCE) + misses * log((1-HIT)/(1-CHANCE)).
  certain   evidence >= 8 and 3 repeats or more;  probable  evidence >= 3.5
The first pass cannot take back a wrong early guess. So the cipher is read PASSES times: each later pass
starts from the certain rows of the pass before and gives every other sign a fresh value.
Parameters from the environment for trials: V7_BEAM, V7_PERJ, V7_OPEN, V7_EXT, V7_MISS.
"""
import math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "..", "line"))
import align  # noqa: E402

BEAM = int(os.environ.get("V7_BEAM", 4000))       # hypotheses kept per unit
PERJ = int(os.environ.get("V7_PERJ", 40))         # of them, at most this many at one pointer
OPEN = float(os.environ.get("V7_OPEN", 3.0))      # entering a gap
EXT = float(os.environ.get("V7_EXT", 0.1))        # each unit in a gap
MISS = float(os.environ.get("V7_MISS", 0.4))      # a known sign that does not spell its value; a skipped letter
PASSES = int(os.environ.get("V7_PASSES", 3))  # reread with the certain values of the pass before held
DMAX = 2                                          # plain letters that may be skipped before a known sign
HIT = 0.55                                        # share of places where a right value spells the plain text
CHANCE = {1: 0.08, 2: 0.015, 3: 0.003}            # the same for a wrong value, by length
VOWELS = set("aeiou")
UNREAD = {1: 0.3, 2: 0.5, 0: 1.0}                 # an unread sign takes 1, 2 or 0 letters


def new_cost(v, inv):
    """Cost of giving a new sign the value v. Letters and open syllables are the common kinds."""
    if len(v) == 1:
        c = 0.0
    elif len(v) == 2:
        c = 0.2 if (v[0] not in VOWELS and v[1] in VOWELS) else 1.0
    else:
        c = 1.5
    return c + (0.7 if v in inv else 0.0)


def search(units, P, lac, log=None, known=None):
    """-> (score, table, ops). ops[i] = (kind, j0, j1) for unit i; kind: M match, A assign, S other spelling,
    I no counterpart, G in a gap, Q unread, C clear word. known: a table to start from (signs fixed)."""
    m = len(P)
    start_tab = dict(known or {})
    start_inv = frozenset(start_tab.values())
    hyps = [(0.0, 0, 0, start_tab, start_inv, 0, None), (-EXT, 0, 1, start_tab, start_inv, 0, None)]
    for i, u in enumerate(units):
        new = {}

        def put(sc, j, g, tab, inv, sig, hist):
            k = (j, g, sig)
            h = new.get(k)
            if h is None or sc > h[0]:
                new[k] = (sc, j, g, tab, inv, sig, hist)

        sym, kind = u.sym, u.kind
        for sc, j, g, tab, inv, sig, hist in hyps:
            if g:                                              # stay in the gap
                put(sc - EXT, j, 1, tab, inv, sig, (hist, "G", j, j))
            if kind == "clear":
                t = u.text
                put(sc, j, 0, tab, inv, sig, (hist, "C", j, j))
                if P.startswith(t, j):
                    put(sc + len(t), j + len(t), 0, tab, inv, sig, (hist, "C", j, j + len(t)))
                continue
            if sym == "?":
                for ln, c in UNREAD.items():
                    if j + ln <= m:
                        put(sc - c, j + ln, 0, tab, inv, sig, (hist, "Q", j, j + ln))
                if not g:
                    put(sc - OPEN, j, 1, tab, inv, sig, (hist, "G", j, j))
                continue
            v = tab.get(sym)
            if v is not None:
                ln = len(v)
                hit = False
                for d in range(DMAX + 1):
                    if P.startswith(v, j + d):
                        put(sc + ln - d * MISS, j + d + ln, 0, tab, inv, sig, (hist, "M", j + d, j + d + ln))
                        hit = d == 0
                        break
                if hit:
                    continue
                if j + ln <= m:
                    put(sc - MISS, j + ln, 0, tab, inv, sig, (hist, "S", j, j + ln))
                put(sc - MISS, j, 0, tab, inv, sig, (hist, "I", j, j))
            else:
                for ln in (1, 2, 3):
                    if j + ln > m:
                        break
                    val = P[j:j + ln]
                    t2 = dict(tab)
                    t2[sym] = val
                    put(sc - new_cost(val, inv), j + ln, 0, t2, inv | {val}, sig ^ hash((sym, val)),
                        (hist, "A", j, j + ln))
                put(sc - MISS, j, 0, tab, inv, sig, (hist, "I", j, j))
            if not g:
                put(sc - (1.0 if lac[j] else OPEN), j, 1, tab, inv, sig, (hist, "G", j, j))
        ranked = sorted(new.values(), key=lambda h: -h[0])
        hyps, per = [], {}
        for h in ranked:
            c = per.get(h[1], 0)
            if c < PERJ:
                per[h[1]] = c + 1
                hyps.append(h)
                if len(hyps) >= BEAM:
                    break
        if log and (i + 1) % 200 == 0:
            b = hyps[0]
            log(f"unit {i + 1}: best score {b[0]:.1f} pointer {b[1]} of {m} table {len(b[3])} "
                f"{'in gap' if b[2] else ''}")
    best = hyps[0]
    ops, h = [], best[6]
    while h is not None:
        ops.append(h[1:])
        h = h[0]
    ops.reverse()
    return best[0], best[3], ops


def rows_from(units, P, tab, ops, known=()):
    """Key rows with the support each value has on the path."""
    hit, miss, gap, first = {}, {}, {}, {s: "" for s in known}
    for u, (kind, j0, j1) in zip(units, ops):
        s = u.sym
        if u.kind != "sign" or s == "?":
            continue
        if kind == "M":
            hit[s] = hit.get(s, 0) + 1
        elif kind == "A":
            first[s] = u.line
        elif kind in ("S", "I"):
            if s in first:
                miss[s] = miss.get(s, 0) + 1
        else:
            gap[s] = gap.get(s, 0) + 1
    rows = []
    for s, v in tab.items():
        h, x = hit.get(s, 0), miss.get(s, 0)
        if s in known:                 # no first place on this path: every place had to spell the value
            h -= 1
        share = (h + 1) / max(1, h + 1 + x)
        pc = CHANCE[min(3, len(v))]
        llr = h * math.log(HIT / pc) + x * math.log((1 - HIT) / (1 - pc))
        status = "certain" if llr >= 8 and h >= 3 else "probable" if llr >= 3.5 else "unknown"
        rows.append(dict(unit=s, value=v, type=align.unit_type(v), support=h + 1, conflict=x,
                         share=round(share, 3), status=status, alts=f"gap×{gap.get(s, 0)}",
                         positions=str(first.get(s, ""))))
    rows.sort(key=lambda r: (-r["support"], r["unit"]))
    return rows


def summary(units, ops):
    c = {}
    for kind, j0, j1 in ops:
        c[kind] = c.get(kind, 0) + 1
    return " ".join(f"{k}={c[k]}" for k in sorted(c))


def build(cipher, plain, log):
    units, P, wb, lac, pairs = align.load_pair(cipher, plain)
    known = {}
    for k in range(PASSES):
        score, tab, ops = search(units, P, lac, log, known)
        rows = rows_from(units, P, tab, ops, known)
        log(f"pass {k + 1}: started from {len(known)} values; score {score:.1f}; table {len(tab)} signs; "
            f"path: {summary(units, ops)}")
        known = {r["unit"]: r["value"] for r in rows if r["status"] == "certain"}
    log("M match, A first value, S other spelling, I no counterpart, G gap, Q unread, C clear")
    st = {}
    for r in rows:
        st[r["status"]] = st.get(r["status"], 0) + 1
    log(f"rows: {st}")
    return rows

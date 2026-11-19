"""lattice652_67.py - c. 652r lines 6 and 7 read from six readers at once with key-v2.tsv (README, "Reading
update, lines 6-7, six readers").

    python3 lattice652_67.py     -> results/c652-67-six.txt

A READING UPDATE, NOT A TEST. Lines 6-7 were held-out text in the failed seventh stage and their key-v2
decode has been seen. Nothing here is evidence for any value; key-v2.tsv is read and never written; no
shuffled-table control is run, because no bar is registered and none could be.

Readers: J, K, L, M (c652.txt rows 3 and 4, guide revision 1) and N, O (c652-67.txt, guide revision 2).
J-M's names are brought to revision-2 names by shape rulings only:
  1. rename-r2.tsv, per reader (made-up name -> listed name). The table's note on n-vloop is applied: reader
     M's first n-vloop on line 7 (the sign the guide's 6.5 gives as its `odot` example) is `odot`; M's other
     n-vloop are `v`.
  2. Revision 2 (6.1) splits the long-barred q off as `qxl`. Under revision 1 that shape was written `q` by
     K and L, `qx` by M and `qx|q` by J (their NOTES). So a revision-1 `q` is `q|qxl` and a revision-1 `qx`
     is `qx|qxl`, half each, at every place. No value is consulted to resolve them.
  Nothing else is changed. Revision 2 also re-rules H against N (6.2); J-M's H and N stand as written.
  3. Dots (6.3): N and O write `.` tokens; J-M's brief had none (M's notes say the dots were seen and left
     out). A dot has no value and four readers could not vote on it, so dots are taken out of the rows before
     the lining-up and listed apart with the sign they follow. Left in, each would be a column of two votes
     against four "no sign", dropped by the path, and it would push the sign after it out of line.
Columns: merge.columns (reader J the frame), lined up with q, qx and qxl counted as one family for the
lining-up only. Votes as merge.py: sign 1, sign? 0.7 + 0.3 unread, a|b shared equally, ? unread, no token =
no sign. Path: stage7.best with no frame letters, which is lattice652.best over tallied columns (log vote
share plus letter trigrams; an unvalued or unread vote is any one letter at a cost of log 20), one line at a
time as lattice652.py does.
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "line"))
import align, merge  # noqa: E402
import lattice, stage7  # noqa: E402

R, RES = os.path.join(HERE, "readers"), os.path.join(HERE, "results")
REV1, REV2 = ("J", "K", "L", "M"), ("N", "O")
READERS = REV1 + REV2
LINES = (6, 7)
SPLIT = {"q": ("q", "qxl"), "qx": ("qx", "qxl")}
FAMILY = {"q": "q*", "qx": "q*", "qxl": "q*"}                  # for lining up only
ANY, NONE = lattice.ANY, lattice.NONE


def rename_table():
    out = {}
    for row in csv.DictReader(open(os.path.join(HERE, "rename-r2.tsv"), encoding="utf-8"), delimiter="\t"):
        out[(row["reader"], row["made_up"])] = row["guide_name"]
    return out


def read_rows(reader):
    name, pick = ("c652.txt", (2, 3)) if reader in REV1 else ("c652-67.txt", (0, 1))
    rows = merge.read_rows(os.path.join(R, reader, name))
    return [rows[i] for i in pick]


def parse(tok):
    """-> [(sign or None for unread, weight)], names as written."""
    if tok == "?":
        return [(None, 1.0)]
    if "|" in tok:
        parts = [p.rstrip("?") for p in tok.split("|")]
        return [(p or None, 1.0 / len(parts)) for p in parts]
    if tok.endswith("?"):
        return [(tok[:-1], 0.7), (None, 0.3)]
    return [(tok, 1.0)]


def to_r2(reader, line, toks, ren):
    """one reader's row -> list of vote lists in revision-2 names."""
    out, vloop = [], 0
    for tok in toks:
        v = {}
        for s, w in parse(tok):
            if s is not None:
                if reader == "M" and s == "n-vloop":
                    vloop += 1
                    s = "odot" if (line == 7 and vloop == 1) else "v"
                else:
                    s = ren.get((reader, s), s)
            parts = SPLIT.get(s, (s,)) if reader in REV1 else (s,)
            for p in parts:
                v[p] = v.get(p, 0) + w / len(parts)
        out.append(sorted(v.items(), key=lambda e: (-e[1], str(e[0]))))
    return out


def show(v):
    signs = [s for s, _ in v if s is not None]
    doubt = any(s is None for s, _ in v)
    return ("|".join(signs) + ("?" if doubt else "")) if signs else "?"


def line_columns(k, ren):
    """-> list of columns; a column is {reader index: vote list}."""
    line = LINES[k]
    raw = [read_rows(r)[k] for r in READERS]
    dots = []
    for r, toks in zip(READERS, raw):
        n = 0
        for t in toks:
            if t.rstrip("?") in (".", ","):
                dots.append(f"{r} after its sign {n}")
            else:
                n += 1
    conv = [to_r2(r, line, [t for t in toks if t.rstrip("?") not in (".", ",")], ren) for r, toks in zip(READERS, raw)]
    # merge.columns lines up token strings; give it one string per token and carry the votes beside it
    rows = [[f"{i}:{show(v)}" for i, v in enumerate(row)] for row in conv]
    keyed = [[show(v) for v in row] for row in conv]
    cols = merge.columns(keyed_rows(keyed), FAMILY)
    return [{r: conv[r][int(t.split(":")[0])] for r, t in col.items()} for col in relabel(cols, rows, keyed)], dots


def keyed_rows(keyed):
    return [[Tok(t, i) for i, t in enumerate(row)] for row in keyed]


class Tok(str):
    """a token string that remembers its index in its reader's row."""
    def __new__(cls, text, index):
        o = str.__new__(cls, text)
        o.index = index
        return o


def relabel(cols, rows, keyed):
    return [{r: rows[r][t.index] for r, t in col.items()} for col in cols]


def tally(col):
    n, c = float(len(READERS)), {}
    for r in range(len(READERS)):
        v = col.get(r)
        if v is None:
            c[NONE] = c.get(NONE, 0) + 1.0 / n
        else:
            for s, w in v:
                c[s] = c.get(s, 0) + w / n
    return c


def cause(t, kmap):
    """why a place is open. t: {sign | None | NONE: share}."""
    signs = {s: w for s, w in t.items() if s not in (None, NONE)}
    top = max(signs, key=signs.get) if signs else None
    if top is not None and signs[top] >= 0.5:
        if top not in kmap:
            return f"key has no value for {top} (readers agree, {signs[top]:.2f})"
        rest = ", ".join(f"{s} {w:.2f}" for s, w in sorted(signs.items(), key=lambda e: -e[1])[1:3])
        return f"readers disagree ({top} {signs[top]:.2f} against {rest}; unread {t.get(None, 0):.2f}); the path takes the unvalued votes"
    unval = sum(w for s, w in signs.items() if s not in kmap)
    lead = ", ".join(f"{s} {w:.2f}" for s, w in sorted(signs.items(), key=lambda e: -e[1])[:3])
    extra = f"; unvalued signs hold {unval:.2f}" if unval >= 0.25 else ""
    return f"readers disagree ({lead}; unread {t.get(None, 0):.2f}){extra}"


def main():
    lp, _, _ = lattice.model()
    kmap = align.key_map(align.read_key(os.path.join(HERE, "key-v2.tsv")))
    ren = rename_table()
    out = ["c. 652r lines 6-7, six readers (J K L M under guide revision 1, brought to revision-2 names; N O under",
           "revision 2). key-v2.tsv, 28 values, unchanged. READING UPDATE: post hoc for the key, no evidence for any value.",
           "Made by lattice652_67.py; see its head for the renaming rules.", ""]
    tot = dict(columns=0, kept=0, unanimous=0, unread=0, dropped=0, letter=0, open=0, nosign=0, weak=0)
    causes, summary = [], []
    for k, line in enumerate(LINES):
        cols, dots = line_columns(k, ren)
        tallies = [tally(c) for c in cols]
        sc, path = stage7.best(tallies, kmap, lp)
        sup, maj, six, fill, merged, rows, mark = [], [], [], [], [], [], []
        place = 0
        for i, (col, t, (kk, o, share)) in enumerate(zip(cols, tallies, path), 1):
            tot["columns"] += 1
            signs = {s: w for s, w in t.items() if s not in (None, NONE)}
            top = max(signs, key=signs.get) if signs else None
            none = t.get(NONE, 0)
            if none >= 0.5 and none >= max(t.values()):
                m = "(dropped)"
                tot["dropped"] += 1
            elif top is not None and signs[top] >= 0.5:
                m = top
                tot["kept"] += 1
                tot["unanimous"] += signs[top] > 0.999
            else:
                m = "?"
                tot["unread"] += 1
            if m != "(dropped)":
                merged.append(m)
            cand = {}
            for s, w in t.items():
                c = NONE if s == NONE else (kmap.get(s) if s else None) or ANY
                cand[c] = cand.get(c, 0) + w
            cs = " ".join(f"{('-' if c == NONE else '?' if c == ANY else c)}:{w:.2f}"
                          for c, w in sorted(cand.items(), key=lambda e: -e[1]))
            if kk == NONE:
                res, why = "-", "no sign here by the path"
                tot["nosign"] += 1
            else:
                place += 1
                if kk == ANY:
                    res, why = "?", "OPEN: " + cause(t, kmap)
                    tot["open"] += 1
                    causes.append((line, place, why))
                    sup.append("?"); six.append("?"); fill.append(o.upper()); mark.append(" ")
                else:
                    res = o
                    tot["letter"] += 1
                    why = ""
                    if share < 0.5:
                        tot["weak"] += 1
                        why = "under half the votes"
                        if top is not None and signs[top] >= 0.5 and top not in kmap:
                            why += f"; the majority sign {top} ({signs[top]:.2f}) has no value"
                        causes.append((line, place, f"WEAK {o} {share:.2f}: {why}"))
                    sup.append(o); fill.append(o); mark.append(("^" if share < 0.5 else " ") * len(o))
                    six.append(o if share >= 0.99 else "." * len(o))
            if kk != NONE:
                lets = sorted(((w, c) for c, w in cand.items() if c not in (ANY, NONE)), reverse=True)
                ok = lets and lets[0][0] >= 0.5 - 1e-9 and (len(lets) == 1 or lets[1][0] < lets[0][0] - 1e-9)
                maj.append(lets[0][1] if ok else "?")
                if kk != ANY and ok and lets[0][1] != o:
                    why += f"; by vote alone {lets[0][1]} ({lets[0][0]:.2f})"
                    causes[-1] = (line, place, causes[-1][2] + f"; by vote alone {lets[0][1]} ({lets[0][0]:.2f})")
            toks = "/".join(show(col[r]) if r in col else "-" for r in range(len(READERS)))
            st = " ".join(f"{s}:{w:.2f}" for s, w in sorted(signs.items(), key=lambda e: -e[1]))
            rows.append(f"  {i:>3}\t{(place if kk != NONE else '-')!s:>3}\t{res}\t{(share if kk != NONE else none):.2f}\t{m}\t{toks}\t{st}\t{cs}\t{why}")
        out += [f"line {line}  (lattice score {sc:.2f}; {len(cols)} columns)",
                "  supported:      " + "".join(sup),
                "  under half:     " + "".join(mark).rstrip(),
                "  by vote alone:  " + "".join(maj),
                "  all six:        " + "".join(six),
                "  with fill:      " + "".join(fill),
                "  merged signs:   " + " ".join(merged),
                "  dots (not in the columns): " + ("; ".join(dots) or "none"),
                "  col\tplace\tletter\tshare\tmerged\tJ/K/L/M/N/O\tsign shares\tcandidate shares\tnote"] + rows + [""]
        summary.append((line, "".join(sup), "".join(maj)))
    out += ["Merge of the six readers (half the votes or more keeps a sign):",
            f"  columns {tot['columns']}, kept {tot['kept']} (all six agree, no doubt: {tot['unanimous']}), "
            f"unread {tot['unread']}, dropped {tot['dropped']}",
            f"  kept share of the columns not dropped: {tot['kept'] / (tot['columns'] - tot['dropped']):.3f}",
            "Lattice:",
            f"  places with a supported letter {tot['letter']} (of them under half the votes: {tot['weak']}), "
            f"open {tot['open']}, columns the path takes as no sign {tot['nosign']}",
            "", "Open and weak places, by cause (line, place counted along the printed rows):"]
    out += [f"  line {ln} place {p}: {why}" for ln, p, why in causes]
    out += ["",
            "supported: the letter on the best path, where some reader's sign has that value; ? = no vote there has a",
            "value the path can use. under half: ^ marks a supported letter whose signs hold under half the votes. by vote alone: no letter model; the letter whose signs hold half the six votes or",
            "more (? if none does, or two tie); it can differ from the path's letter, and a two-letter value (tt)",
            "makes that row one longer. all six: every reader's sign gives the path's letter. with fill: the letter",
            "model's guess at ? in capitals (not evidence). share: the vote share of the letter (or of 'no sign').",
            "candidate shares: ? = unvalued or unread, - = no sign. A revision-1 q counts half q, half qxl; a",
            "revision-1 qx half qx, half qxl; qxl has no value in key-v2.tsv, so at a place both revision-2 readers",
            "give qxl, an n (from qx) or g (from q) on the supported row rests only on the unresolved half of the",
            "revision-1 tokens. The 'by vote alone' row leaves those places open."]
    open(os.path.join(RES, "c652-67-six.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()

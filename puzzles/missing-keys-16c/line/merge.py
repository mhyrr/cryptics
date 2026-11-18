"""merge.py - one transcription from three or more readers of the same cipher text.

    python3 merge.py a.txt b.txt c.txt [d.txt ...] --out merged.txt [--min 0.5] [--report report.tsv]
Readers' files have the same manuscript lines (rows not starting with '#'). The first file is the frame: in
each line the other readers are lined up on it by difflib on sign names, and a stretch a reader has and the
frame lacks becomes columns of its own. Each column holds one vote per reader:
    sign      weight 1        sign?   0.7 for the sign, 0.3 unread
    x|y       0.5 each        ?       unread          (no token there)  no sign
The merged line keeps a column's sign when its share of the readers is at least --min; a column where "no
sign" has at least --min is dropped; any other column becomes '?'. Two readers who agree outvote two who
disagree with each other, so the merged text keeps places a two-reader consensus loses.
The report gives, per line: columns, kept, unread, dropped, and kept with every reader's full vote.
"""
import difflib, sys

NONE = ""


def votes(tok, rename=None):
    """-> [(sign, or None for unread, weight)] for one token."""
    rn = (rename or {}).get
    if tok == "?":
        return [(None, 1.0)]
    if "|" in tok:
        parts = [p.rstrip("?") for p in tok.split("|")]
        return [((rn(p, p) or None), 1.0 / len(parts)) for p in parts]
    if tok.endswith("?"):
        return [(rn(tok[:-1], tok[:-1]), 0.7), (None, 0.3)]
    return [(rn(tok, tok), 1.0)]


def first(tok, rename=None):
    return votes(tok, rename)[0][0] or "?"


def columns(rows, rename=None):
    """rows: list of token lists, the frame first. -> list of columns; a column is {reader index: token}."""
    cols = [{0: t} for t in rows[0]]
    for r in range(1, len(rows)):
        idx = [i for i, c in enumerate(cols) if 0 in c]
        a = [first(cols[i][0], rename) for i in idx]
        toks = rows[r]
        b = [first(t, rename) for t in toks]
        extra = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            n = min(i2 - i1, j2 - j1) if op in ("equal", "replace") else 0
            for k in range(n):
                cols[idx[i1 + k]][r] = toks[j1 + k]
            at = idx[i1 + n] if i1 + n < len(idx) else len(cols)
            extra += [(at, t) for t in toks[j1 + n:j2]]
        for at, t in sorted(extra, key=lambda e: -e[0]):
            if at > 0 and 0 not in cols[at - 1] and r not in cols[at - 1]:
                cols[at - 1][r] = t          # a lone column from another reader at this place takes it
            else:
                cols.insert(at, {r: t})
    return cols


def tally(col, n, rename=None):
    """-> {sign | None (unread) | NONE (no sign): share of n readers}."""
    c = {}
    for r in range(n):
        tok = col.get(r)
        if tok is None:
            c[NONE] = c.get(NONE, 0) + 1.0
            continue
        for s, w in votes(tok, rename):
            c[s] = c.get(s, 0) + w
    return {k: v / n for k, v in c.items()}


def merge_line(rows, minimum=0.5, rename=None):
    """-> (tokens, stats) for one manuscript line."""
    n = len(rows)
    out, st = [], dict(columns=0, kept=0, unread=0, dropped=0, unanimous=0)
    for col in columns(rows, rename):
        st["columns"] += 1
        t = tally(col, n, rename)
        if t.get(NONE, 0) >= minimum and t.get(NONE, 0) >= max(v for v in t.values()):
            st["dropped"] += 1
            continue
        signs = {k: v for k, v in t.items() if k not in (None, NONE)}
        top = max(signs, key=signs.get) if signs else None
        if top is not None and signs[top] >= minimum:
            out.append(top)
            st["kept"] += 1
            st["unanimous"] += signs[top] > 0.999
        else:
            out.append("?")
            st["unread"] += 1
    return out, st


def read_rows(path):
    return [ln.split() for ln in open(path, encoding="utf-8").read().splitlines() if ln.strip() and not ln.startswith("#")]


def merge_files(paths, minimum=0.5, rename=None):
    files = [read_rows(p) for p in paths]
    if len({len(f) for f in files}) != 1:
        raise SystemExit(f"readers differ in line count: {[len(f) for f in files]}")
    lines, stats = [], []
    for k in range(len(files[0])):
        toks, st = merge_line([f[k] for f in files], minimum, rename)
        lines.append(" ".join(toks))
        stats.append(st)
    return lines, stats


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)

    def opt(name, d=None):
        if name in a:
            i = a.index(name)
            v = a[i + 1]
            del a[i:i + 2]
            return v
        return d
    out, rep, minimum = opt("--out"), opt("--report"), float(opt("--min", 0.5))
    lines, stats = merge_files(a, minimum)
    open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    keys = ("columns", "kept", "unread", "dropped", "unanimous")
    tot = {k: sum(s[k] for s in stats) for k in keys}
    rows = ["line\t" + "\t".join(keys)] + [f"{i}\t" + "\t".join(str(s[k]) for k in keys) for i, s in enumerate(stats, 1)]
    rows.append("all\t" + "\t".join(str(tot[k]) for k in keys))
    if rep:
        open(rep, "w").write("\n".join(rows) + "\n")
    print(rows[-1])


if __name__ == "__main__":
    main()

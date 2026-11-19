"""merge_c215.py - agreement and vote merge of the four cipher readers of c. 215 (CA, CB, CC, CD).

    python3 -I merge_c215.py     -> results/c215-agree.tsv, results/c215-merged.txt, results/c215-merge.tsv

Each reader's c215.txt; the rename table rename-c215.tsv (made from the readers' shape descriptions, never from
values) is applied per token; a name that maps to two names becomes two tokens. Gaps `/` are taken out before
comparing signs (they are counted apart); `:` and `.` stay as tokens. [[clear]] markers are dropped.
Pairwise agreement = 2 * matched / (len a + len b), difflib on the renamed token names with '?' stripped.
The merge is line/merge.py (first reader the frame, share >= 0.5 keeps a sign).
"""
import csv, difflib, itertools, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "line"))
import merge  # noqa: E402

READERS = ["CA", "CB", "CC", "CD"]


def table():
    t = {}
    for row in csv.DictReader(open(os.path.join(HERE, "rename-c215.tsv"), encoding="utf-8"), delimiter="\t"):
        t[row["made_up"]] = row["merged_name"].split()
    return t


def ren_tok(tok, t):
    """rename every alternative inside a token; keep ? and | marks."""
    if tok == "?":
        return [tok]
    q = tok.endswith("?")
    core = tok[:-1] if q else tok
    alts = core.split("|")
    if len(alts) == 1:
        parts = t.get(core, [core])
        return [p + ("?" if q else "") for p in parts]
    return ["|".join(t.get(a.rstrip("?"), [a])[0] for a in alts) + ("?" if q else "")]


def load(r, t):
    rows = {}
    for ln in open(os.path.join(HERE, "readers", r, "c215.txt"), encoding="utf-8"):
        if not ln.startswith("L"):
            continue
        lab, *toks = ln.split()
        out, gaps = [], 0
        for k in toks:
            if k == "/":
                gaps += 1
                continue
            if k.startswith("[["):
                continue
            out += ren_tok(k, t)
        rows[lab] = (out, gaps)
    return rows


def bare(tok):
    return tok if tok == "?" else tok.rstrip("?").split("|")[0]


def main():
    t = table()
    data = {r: load(r, t) for r in READERS}
    labels = list(data["CA"])
    res = os.path.join(HERE, "results")
    os.makedirs(res, exist_ok=True)
    out = ["pair\tmatched\tlen_a\tlen_b\tagreement"]
    for a, b in itertools.combinations(READERS, 2):
        m = la = lb = 0
        for lab in labels:
            x = [bare(k) for k in data[a][lab][0]]
            y = [bare(k) for k in data[b][lab][0]]
            m += sum(bl.size for bl in difflib.SequenceMatcher(None, x, y, autojunk=False).get_matching_blocks())
            la, lb = la + len(x), lb + len(y)
        out.append(f"{a}-{b}\t{m}\t{la}\t{lb}\t{2 * m / (la + lb):.3f}")
    open(os.path.join(res, "c215-agree.tsv"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))
    merged, rep = ["# 2946-c215 merged (CA CB CC CD; rename-c215.tsv; min 0.5)"], ["line\tcolumns\tkept\tunread\tdropped\tunanimous"]
    tk = tu = 0
    for lab in labels:
        rows = [data[r][lab][0] for r in READERS]
        toks, st = merge.merge_line(rows, 0.5)
        merged.append(f"{lab} " + " ".join(toks))
        rep.append(f"{lab}\t" + "\t".join(str(st[k]) for k in ("columns", "kept", "unread", "dropped", "unanimous")))
        tk += st["kept"]; tu += st["unread"]
    open(os.path.join(res, "c215-merged.txt"), "w").write("\n".join(merged) + "\n")
    open(os.path.join(res, "c215-merge.tsv"), "w").write("\n".join(rep) + "\n")
    print(f"merged: kept {tk}, unread {tu}")


if __name__ == "__main__":
    main()

"""compare.py - agreement between two readers' transcriptions of the same cipher pages (PIPELINE.md stage 2).

    python3 compare.py <readerA file|dir> <readerB file|dir> [--out agreement.tsv] [--diffs diffs.txt]
                       [--consensus consensus.txt]

Both sides are in the cipher format of align.py. Directories are paired by file name; one row per file, then a
total. Two comparisons, each aligned with difflib.SequenceMatcher(autojunk=False):
  tokens: one entry per transcribed token, its text with the doubt mark '?' stripped ('?' alone stays '?');
          a clear word counts as one token, written [[normalized text]].
  units:  align.py's units (base, mark after, marks above), by symbol.
Agreement = 2 * matched / (len A + len B). doubt_a / doubt_b count tokens marked doubtful or unread.
--consensus (single file pair only) writes the tokens both readers agree on, each stretch of disagreement
replaced by one '?', in reader A's line breaks. A's anchors are kept where they fall.
"""
import argparse, difflib, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import align  # noqa: E402

COLS = ["file", "tokens_a", "tokens_b", "token_agreement", "units_a", "units_b", "unit_agreement", "doubt_a", "doubt_b"]


class Tok:
    __slots__ = ("text", "line", "doubt", "index")

    def __init__(self, text, line, doubt, index):
        self.text, self.line, self.doubt, self.index = text, line, doubt, index


def tokens(units):
    """Group units by token index -> list of Tok (text without the doubt mark)."""
    out, seen = [], {}
    for u in units:
        if u.tok in seen:
            t = out[seen[u.tok]]
            t.doubt = t.doubt or u.doubt
            continue
        if u.kind == "clear":
            text = u.sym
        else:
            text = u.raw if u.raw == "?" else u.raw.rstrip("?") or "?"
        seen[u.tok] = len(out)
        out.append(Tok(text, u.line, u.doubt or text == "?", u.tok))
    return out


def agreement(a, b):
    """-> (matched, SequenceMatcher)."""
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return sum(blk.size for blk in sm.get_matching_blocks()), sm


def ratio(matched, na, nb):
    return 2 * matched / (na + nb) if na + nb else 1.0


def compare_texts(text_a, text_b):
    ua, _, _ = align.parse_cipher(text_a)
    ub, _, _ = align.parse_cipher(text_b)
    ta, tb = tokens(ua), tokens(ub)
    tm, tsm = agreement([t.text for t in ta], [t.text for t in tb])
    um, _ = agreement([u.sym for u in ua], [u.sym for u in ub])
    return dict(tokens_a=len(ta), tokens_b=len(tb), tok_matched=tm, units_a=len(ua), units_b=len(ub), unit_matched=um,
                doubt_a=sum(t.doubt for t in ta), doubt_b=sum(t.doubt for t in tb), ta=ta, tb=tb, sm=tsm)


def diff_lines(name, r):
    ta, tb, out = r["ta"], r["tb"], []
    for op, i1, i2, j1, j2 in r["sm"].get_opcodes():
        if op == "equal":
            continue
        la = f"A l.{ta[i1].line}-{ta[i2 - 1].line}" if i2 > i1 else f"A l.{ta[i1 - 1].line if i1 else 0}+"
        lb = f"B l.{tb[j1].line}-{tb[j2 - 1].line}" if j2 > j1 else f"B l.{tb[j1 - 1].line if j1 else 0}+"
        out.append(f"{name}\t{op}\t{la}\t{lb}\tA: {' '.join(t.text for t in ta[i1:i2])}\t"
                   f"B: {' '.join(t.text for t in tb[j1:j2])}")
    return out


def _consensus(ta, tb):
    """-> list of (text, line in A, A token position or None for a '?' stretch with no A tokens)."""
    _, sm = agreement([t.text for t in ta], [t.text for t in tb])
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                a, b = ta[i1 + k], tb[j1 + k]
                out.append((a.text + ("?" if (a.doubt or b.doubt) and a.text != "?" else ""), a.line, i1 + k))
        else:
            line = ta[i1].line if i2 > i1 else (ta[i1 - 1].line if i1 else (ta[0].line if ta else 1))
            out.append(("?", line, i1 if i2 > i1 else None))
    return out


def consensus(units_a, units_b):
    """Tokens both readers agree on; each disagreeing stretch becomes one '?' token."""
    return [t for t, _, _ in _consensus(tokens(units_a), tokens(units_b))]


def write_consensus(text_a, text_b, path):
    ua, anch, _ = align.parse_cipher(text_a)
    ub, _, _ = align.parse_cipher(text_b)
    ta, tb = tokens(ua), tokens(ub)
    # anchor -> A token position it precedes
    unit_tok = [u.tok for u in ua]
    tokpos = {t.index: k for k, t in enumerate(ta)}
    before = {}
    for name, ui in anch.items():
        k = tokpos[unit_tok[ui]] if ui < len(ua) else len(ta)
        before.setdefault(k, []).append(name)
    lines, cur, ln, used = [], [], None, set()
    for text, line, k in _consensus(ta, tb):
        if line != ln and cur:
            lines.append(" ".join(cur))
            cur = []
        ln = line
        if k is not None:
            for kk in sorted(x for x in before if x <= k and x not in used):
                cur += before[kk]
                used.add(kk)
        cur.append(text)
    for kk in sorted(x for x in before if x not in used):
        cur += before[kk]
    if cur:
        lines.append(" ".join(cur))
    with open(path, "w", encoding="utf-8") as f:
        f.write("# consensus of two readers; '?' marks a stretch where they disagree\n")
        f.write("\n".join(lines) + "\n")


def pairs(pa, pb):
    if os.path.isdir(pa) and os.path.isdir(pb):
        na = {n for n in os.listdir(pa) if os.path.isfile(os.path.join(pa, n)) and not n.startswith(".")}
        nb = {n for n in os.listdir(pb) if os.path.isfile(os.path.join(pb, n)) and not n.startswith(".")}
        for n in sorted(na ^ nb):
            print(f"unpaired: {n} only in {'A' if n in na else 'B'}", file=sys.stderr)
        return [(n, os.path.join(pa, n), os.path.join(pb, n)) for n in sorted(na & nb)]
    if os.path.isdir(pa) or os.path.isdir(pb):
        sys.exit("give two files or two directories")
    return [(os.path.basename(pa), pa, pb)]


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("a"), ap.add_argument("b")
    ap.add_argument("--out"), ap.add_argument("--diffs"), ap.add_argument("--consensus")
    a = ap.parse_args(argv)
    ps = pairs(a.a, a.b)
    rows, diffs = [], []
    tot = dict(tokens_a=0, tokens_b=0, tok_matched=0, units_a=0, units_b=0, unit_matched=0, doubt_a=0, doubt_b=0)
    for name, fa, fb in ps:
        r = compare_texts(read(fa), read(fb))
        for k in tot:
            tot[k] += r[k]
        rows.append((name, r))
        diffs += diff_lines(name, r)
    if len(ps) > 1:
        rows.append(("TOTAL", tot))

    def fmt(name, r):
        return [name, r["tokens_a"], r["tokens_b"], f"{ratio(r['tok_matched'], r['tokens_a'], r['tokens_b']):.3f}",
                r["units_a"], r["units_b"], f"{ratio(r['unit_matched'], r['units_a'], r['units_b']):.3f}",
                r["doubt_a"], r["doubt_b"]]

    text = "\t".join(COLS) + "\n" + "".join("\t".join(map(str, fmt(n, r))) + "\n" for n, r in rows)
    sys.stdout.write(text)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
    if a.diffs:
        with open(a.diffs, "w", encoding="utf-8") as f:
            f.write("# file\top\tA lines\tB lines\tA tokens\tB tokens\n" + "".join(d + "\n" for d in diffs))
    if a.consensus:
        if len(ps) != 1:
            sys.exit("--consensus takes one file pair")
        write_consensus(read(ps[0][1]), read(ps[0][2]), a.consensus)


if __name__ == "__main__":
    main()

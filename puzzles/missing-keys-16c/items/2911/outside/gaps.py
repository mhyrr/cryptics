"""gaps.py - working view: for each reader name, what the printed text has between its two neighbours.

    python3 gaps.py [cipher.txt] [min_count]

Decodes with truth.tsv, aligns to the printed text (difflib), and for every token whose left and right
neighbours both land on the print within 14 letters of each other, takes the print letters between them.
Prints, per token name, the commonest such strings. Used to choose among the sheet signs that one reader
name could stand for (truth.tsv column basis = context). Not a result; no figure is quoted from it.
"""
import sys, os, difflib, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import decode

def run(path, minc=1, only=None):
    key = decode.load_truth()
    lines = decode.decode_file(path, key)
    P = decode.norm(open(os.path.join(HERE, "..", "work", "plain-print.txt"), encoding="utf-8").read())
    flat, seq, owner = [], [], []
    for li, row in enumerate(lines):
        for tok, val, typ in row:
            flat.append((li, tok, val, typ))
            if typ not in ("clear", "unread", "missing", "null"):
                for ch in decode.norm(val):
                    seq.append(ch); owner.append(len(flat) - 1)
    sm = difflib.SequenceMatcher(None, "".join(seq), P, autojunk=False)
    lo, hi = {}, {}
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            o = owner[a + k]
            lo.setdefault(o, b + k); hi[o] = b + k
    res = collections.defaultdict(collections.Counter)
    for o, (li, tok, val, typ) in enumerate(flat):
        if o - 1 in hi and o + 1 in lo and 0 <= lo[o + 1] - hi[o - 1] - 1 <= 14:
            res[tok][P[hi[o - 1] + 1:lo[o + 1]]] += 1
    tot = collections.Counter(f[1] for f in flat)
    for tok, n in tot.most_common():
        if n < minc or (only and tok not in only):
            continue
        c = res[tok]
        print("%-12s n=%-4d cur=%-8s seen=%-4d %s" % (tok, n, key.get(tuple(tok.split("_")), ("-",))[0] if tok != "?" else "#", sum(c.values()),
              " ".join("%s:%d" % (k or "''", v) for k, v in c.most_common(9))))

if __name__ == "__main__":
    a = sys.argv[1:]
    run(a[0] if a else os.path.join(HERE, "..", "work", "cipher-primary.txt"), int(a[1]) if len(a) > 1 else 1, set(a[2:]) or None)

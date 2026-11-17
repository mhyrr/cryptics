"""explore.py - working view used while matching reader names to sheet signs (not a result).

    python3 explore.py [cipher.txt] [--name NAME]

Decodes with truth.tsv (via decode.py), aligns the letters to the printed text with difflib, and prints each
cipher line with token=value and the stretch of print it falls on. With --name, lists every place of that
reader name with the print letters around its aligned position.
"""
import sys, os, difflib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import decode

def main():
    args = sys.argv[1:]
    name = None
    if "--name" in args:
        i = args.index("--name"); name = args[i + 1]; del args[i:i + 2]
    path = args[0] if args else os.path.join(HERE, "..", "work", "cipher-primary.txt")
    key = decode.load_truth()
    lines = decode.decode_file(path, key)
    P = decode.norm(open(os.path.join(HERE, "..", "work", "plain-print.txt"), encoding="utf-8").read())
    seq, owner = [], []
    flat = []
    for li, row in enumerate(lines):
        for ti, (tok, val, typ) in enumerate(row):
            flat.append((li, tok, val, typ))
            for ch in decode.norm(val or ""):
                seq.append(ch); owner.append(len(flat) - 1)
    D = "".join(seq)
    sm = difflib.SequenceMatcher(None, D, P, autojunk=False)
    d2p = {}
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            d2p[a + k] = b + k
    first = {}
    for di, o in enumerate(owner):
        if di in d2p:
            first.setdefault(o, d2p[di])
    if name:
        last = 0
        for o, (li, tok, val, typ) in enumerate(flat):
            if o in first: last = first[o]
            if tok == name:
                ctx = " ".join(t for (_, t, _, _) in flat[max(0, o - 4):o + 5])
                print(li + 1, ctx, "|", P[max(0, last - 12):last + 16], "|", "hit" if o in first else "~")
        return
    cur = 0
    for li, row in enumerate(lines):
        os_ = [o for o, f in enumerate(flat) if f[0] == li]
        ps = [first[o] for o in os_ if o in first]
        print("L%d %s" % (li + 1, " ".join("%s=%s" % (t, v if v is not None else "#") for (t, v, ty) in row)))
        if ps:
            lo, hi = min(ps), max(ps)
            if hi - lo < 400:
                print("   P[%d:%d] %s" % (lo, hi, P[lo:hi + 3]))
            else:
                print("   P scattered %d..%d" % (lo, hi))
        print()

if __name__ == "__main__":
    main()

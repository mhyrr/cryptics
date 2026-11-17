"""doubles_check.py - does VI/82 confirm the doubled shapes that ../doubles.py joins from counts?

    python3 doubles_check.py   -> doubles-check.tsv

Reads ../results/doubles.tsv (sign, count, pairs, expected, decision) and truth.tsv. A pair `x x` is "a sign of
its own on the sheet" when truth.tsv has a row whose seq is `x x` (the row then gives the sheet cell). Also lists
truth.tsv sequences of two different names (one sheet sign the readers wrote as two tokens, or a name number),
with their counts in ../work/cipher-primary.txt. No value is written to the output.
"""
import os, csv, collections
HERE = os.path.dirname(os.path.abspath(__file__))
import decode

truth = list(csv.DictReader(open(os.path.join(HERE, "truth.tsv"), encoding="utf-8"), delimiter="\t"))
seqs = {tuple(r["seq"].split()): r for r in truth if r["type"] != "none"}
toks = []
for row in open(os.path.join(HERE, "..", "work", "cipher-primary.txt"), encoding="utf-8"):
    if not row.startswith("#"):
        toks += [t for k, t, _ in decode.tokens(row.strip())] + ["|"]
bi = collections.Counter(zip(toks, toks[1:]))
out = ["kind\tsign\tcount\tpairs\texpected\tdoubles.py\ton_sheet_as_one_sign\tsheet_type\tsheet_cell"]
n_join = n_join_ok = n_missed = 0
for r in csv.DictReader(open(os.path.join(HERE, "..", "results", "doubles.tsv"), encoding="utf-8"), delimiter="\t"):
    x = r["sign"].replace("+", "^")
    t = seqs.get((x, x))
    joined = r["decision"] == "join"
    n_join += joined
    n_join_ok += joined and t is not None
    n_missed += (not joined) and t is not None
    out.append("\t".join(["same-sign pair", x + " " + x, r["count"], r["pairs"], r["expected"], r["decision"] or "not joined",
                          "yes" if t else "no", t["type"] if t else "", t["sheet"] if t else ""]))
for k, t in seqs.items():
    if len(k) == 2 and k[0] != k[1]:
        out.append("\t".join(["two-name sequence", " ".join(k), "", str(bi[k]), "", "not considered", "yes", t["type"], t["sheet"]]))
out.append("# joined by doubles.py: %d; of those on the sheet as one sign: %d; on the sheet but not joined: %d"
           % (n_join, n_join_ok, n_missed))
open(os.path.join(HERE, "doubles-check.tsv"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out))

"""score.py - score a blind table for no. 2351 against the confirmed key. Counts only, never values.

    python3 score.py <table.tsv> <label>
<table.tsv>: tab-separated with a header; columns `unit`, `value`, `status`. `unit` is a sign exactly as it
stands in inputs/cipher-A.txt (`x+4`, `3`, `delta`); rows with status `certain` or `probable` are scored.
The answer is ../key-v0.tsv (entries B:, M:, W:), expanded to every sign of the cipher text it gives a value
to. This script may read the answer; a builder and its author may not. It prints and appends to
runs/results.tsv: signs the answer values, rows marked, rows shared with the answer, rows the same, and the
share of the cipher's places whose sign the table values the same as the answer (place recall) and of the
places the table values that the answer values the same (place precision, on places the answer values).
"""
import csv, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
VM = ("1", "3", "4", "5", "~")


def answer(signs):
    t = {r["unit"]: r["value"] for r in csv.DictReader(open(os.path.join(HERE, "..", "key-v0.tsv")), delimiter="\t")}
    out = {}
    for s in signs:
        b, _, m = s.partition("+")
        if "W:" + s in t:
            out[s] = t["W:" + s]
        elif m in VM and "B:" + b in t and "M:" + m in t:
            out[s] = t["B:" + b] + t["M:" + m]
    return out


def main():
    path, label = sys.argv[1], sys.argv[2]
    toks = [t for ln in open(os.path.join(HERE, "inputs", "cipher-A.txt")) if not ln.startswith("#")
            for t in ln.split() if t != "?"]
    ans = answer(set(toks))
    tab = {r["unit"]: r["value"] for r in csv.DictReader(open(path), delimiter="\t")
           if r.get("status") in ("certain", "probable")}
    shared = [s for s in tab if s in ans]
    same = sum(tab[s] == ans[s] for s in shared)
    pa = [t for t in toks if t in ans]
    spoke = [t for t in pa if t in tab]
    ok = sum(tab[t] == ans[t] for t in spoke)
    passed = len(shared) >= 20 and same >= 0.8 * len(shared)
    row = [time.strftime("%Y-%m-%d %H:%M"), label, len(ans), len(tab), len(shared), same,
           f"{same / max(1, len(shared)):.3f}", f"{ok / max(1, len(spoke)):.3f}", f"{ok / max(1, len(pa)):.3f}", passed]
    head = "when\tlabel\tanswer_signs\tmarked\tshared\tsame\tshare_same\tplace_precision\tplace_recall\tpass"
    res = os.path.join(HERE, "runs", "results.tsv")
    new = not os.path.exists(res)
    with open(res, "a") as f:
        if new:
            f.write(head + "\n")
        f.write("\t".join(map(str, row)) + "\n")
    print(head)
    print("\t".join(map(str, row)))


if __name__ == "__main__":
    main()

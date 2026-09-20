#!/usr/bin/env python3
"""Do interior rows or columns CONTAIN a dictionary transliteration?

Same vocabulary, normalization and seed as rows_in_dictionary.py. For each full
interior line (rows, plus columns where the square is not transpose-symmetric)
of length n >= 5, test whether any vocabulary word of length 4..n-1 occurs as a
contiguous substring, forward or reversed. Control: the cv_shuffle of the same
line, 200 draws. Exact substring match only.
"""
import collections, json, random
from rows_in_dictionary import HERE, SQ, DRAWS, norm, load_vocab, cv_shuffle


def contains(w, vocab):
    n = len(w)
    for L in range(4, n):
        for i in range(n - L + 1):
            s = w[i:i + L]
            if s in vocab or s[::-1] in vocab:
                return s
    return None


def main():
    vocab = load_vocab()
    rng = random.Random(20260920)
    c = collections.Counter()
    found = []
    for s in json.load(open(SQ))["squares"]:
        rows = s["rows"]
        n = len(rows)
        if n < 5 or any(len(r) != n for r in rows):
            continue
        cols = ["".join(r[j] for r in rows) for j in range(n)]
        lines = [("row", i, rows[i]) for i in range(1, n - 1)]
        if cols != rows:
            lines += [("col", j, cols[j]) for j in range(1, n - 1) if cols[j] != rows[j]]
        for kind, i, r in lines:
            if "." in r:
                continue
            w = norm(r)
            if len(w) != n:
                continue
            c["lines"] += 1
            hit = contains(w, vocab)
            if hit:
                c["observed"] += 1
                found.append({"square": s["id"], "line": f"{kind}{i+1}", "text": w, "substring": hit})
            c["control"] += sum(bool(contains(cv_shuffle(w, rng), vocab)) for _ in range(DRAWS)) / DRAWS
    out = {"lines": c["lines"], "observed": c["observed"], "control_mean": round(c["control"], 2), "found": found}
    (HERE / "substrings-in-dictionary.json").write_text(json.dumps(out, indent=1) + "\n")
    print({k: v for k, v in out.items() if k != "found"})
    for f in found:
        print(f)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Are square rows words of the dictionary's Hebrew-transliteration vocabulary?

Discovery analysis on the already exposed Mathers export. No captions are used.
For every full row (no blanks) of every analyzable square, by row position,
count matches against the OCR vocabulary of Hebrew-adjacent tokens
(tokens.tsv). Compare with three controls on the same rows:

  reversed      the row read right to left (skipped for palindromes)
  cv_shuffle    vowels permuted among vowel slots, consonants among consonant
                slots; keeps pronounceability and the letter multiset
  full_shuffle  all letters permuted

Matching tiers, applied identically to rows and controls:
  exact    equal after normalization
  near     Levenshtein distance <= 1, only for length >= 5

Normalization: upper case A-Z; long s -> S; J -> I; V -> U; W -> U.
Because the OCR often prints long s as f, each vocabulary token containing F
is indexed twice, as printed and with F -> S. This is an OCR tolerance.
Shuffles use random.Random(20260920); 200 draws per row; the control rate is
the mean over draws. Rows shorter than 4 letters are skipped.
"""
import collections, csv, json, pathlib, random

HERE = pathlib.Path(__file__).resolve().parent
SQ = HERE.parents[1] / "sources" / "mathers-squares.json"
VOWELS = set("AEIOU")
DRAWS = 200


def norm(s):
    s = s.upper().replace("ſ", "S").replace("J", "I").replace("V", "U").replace("W", "U")
    return "".join(c for c in s if "A" <= c <= "Z")


def load_vocab():
    v = set()
    with open(HERE / "tokens.tsv", encoding="utf8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            t = norm(r["token"])
            if len(t) >= 4:
                v.add(t)
                if "F" in t:
                    v.add(t.replace("F", "S"))
    return v


def near_index(vocab):
    idx = collections.defaultdict(set)
    for w in vocab:
        if len(w) >= 4:
            for i in range(len(w)):
                idx[w[:i] + "*" + w[i + 1:]].add(w)   # substitution
                idx[w[:i] + w[i + 1:]].add(w)           # vocabulary word has one extra letter
    return idx


def is_near(w, vocab, idx):
    if len(w) < 5:
        return False
    if w in vocab:
        return True
    for i in range(len(w)):
        if idx.get(w[:i] + "*" + w[i + 1:]):
            return True
        if w[:i] + w[i + 1:] in vocab:                  # row has one extra letter
            return True
    return bool(idx.get(w) and any(len(x) == len(w) + 1 for x in idx[w]))


def cv_shuffle(w, rng):
    vs = [c for c in w if c in VOWELS]
    cs = [c for c in w if c not in VOWELS]
    rng.shuffle(vs), rng.shuffle(cs)
    vi, ci = iter(vs), iter(cs)
    return "".join(next(vi) if c in VOWELS else next(ci) for c in w)


def position(i, n):
    if i == 0:
        return "top"
    if i == n - 1:
        return "bottom"
    if n % 2 and i == n // 2:
        return "centre"
    return "upper_inner" if i < n / 2 else "lower_inner"


def main():
    vocab = load_vocab()
    idx = near_index(vocab)
    rng = random.Random(20260920)
    squares = json.load(open(SQ))["squares"]
    stats = collections.defaultdict(lambda: collections.Counter())
    hits = []
    for s in squares:
        rows = s["rows"]
        n = len(rows)
        if n < 4 or any(len(r) != n for r in rows):
            continue
        for i, r in enumerate(rows):
            if "." in r:
                continue
            w = norm(r)
            if len(w) != n:
                continue
            pos = position(i, n)
            c = stats[pos]
            c["rows"] += 1
            ex, nr = w in vocab, is_near(w, vocab, idx)
            c["exact"] += ex
            c["near"] += nr
            if ex or nr:
                hits.append({"square": s["id"], "row": i + 1, "position": pos, "text": w, "exact": ex})
            if w != w[::-1]:
                c["rev_rows"] += 1
                c["rev_exact"] += w[::-1] in vocab
                c["rev_near"] += is_near(w[::-1], vocab, idx)
            for name, fn in (("cv", cv_shuffle), ("full", lambda x, g: "".join(g.sample(x, len(x))))):
                e = m = 0
                for _ in range(DRAWS):
                    x = fn(w, rng)
                    e += x in vocab
                    m += is_near(x, vocab, idx)
                c[name + "_exact"] += e / DRAWS
                c[name + "_near"] += m / DRAWS
    out = {"vocabulary_size": len(vocab), "draws": DRAWS,
           "by_position": {k: {a: round(b, 3) for a, b in v.items()} for k, v in sorted(stats.items())},
           "hits": hits}
    (HERE / "rows-in-dictionary.json").write_text(json.dumps(out, indent=1) + "\n")
    print("vocab", len(vocab))
    print(f"{'position':12} rows exact near | rev: rows exact near | cv: exact near | full: exact near")
    for k, c in sorted(stats.items()):
        print(f"{k:12} {c['rows']:4} {c['exact']:5} {c['near']:4} | {c['rev_rows']:4} {c['rev_exact']:5} {c['rev_near']:4} | "
              f"{c['cv_exact']:6.2f} {c['cv_near']:6.2f} | {c['full_exact']:6.2f} {c['full_near']:6.2f}")


if __name__ == "__main__":
    main()

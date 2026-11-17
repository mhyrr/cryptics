"""fluency.py - how much of a decode is covered by words of a period word list, against permuted keys (stage 5).

    python3 fluency.py <cipher.txt> <key.tsv> <wordlist.txt> [--perms 20] [--minlen 3] [--seed 1] [--min probable]

Decodes with align.key_map / align.decode_units. An unknown unit and a clear-text word both break the letter
stream into runs; clear text is not counted. In each run a dynamic programme picks the segmentation that
covers the most letters with list words of length >= minlen (other letters stay uncovered).
Word list: one word per line (first field used; '#' lines skipped), normalized with align.norm_letters.
The control decodes the same text with --perms keys whose values are shuffled within type (align.permuted).
Output: key<TAB>value lines.
"""
import argparse, os, random, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import align  # noqa: E402


def load_words(path, merge=True):
    words = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or not line.split():
                continue
            w = align.norm_letters(line.split()[0], merge)
            if w:
                words.add(w)
    return words


def covered(run, words, minlen=3, maxlen=None):
    """Most letters of `run` (a-z only) that a segmentation into list words (len >= minlen) can cover."""
    if maxlen is None:
        maxlen = max((len(w) for w in words), default=0)
    n = len(run)
    best = [0] * (n + 1)
    for i in range(1, n + 1):
        b = best[i - 1]
        for ln in range(minlen, min(maxlen, i) + 1):
            if best[i - ln] + ln > b and run[i - ln:i] in words:
                b = best[i - ln] + ln
        best[i] = b
    return best[n]


def covered_share(text, words, minlen=3):
    """Share of the letters of `text` covered by list words. Any character outside a-z breaks a run."""
    runs = [r for r in re.split(r"[^a-z]+", text) if r]
    total = sum(len(r) for r in runs)
    if not total:
        return 0.0
    maxlen = max((len(w) for w in words), default=0)
    return sum(covered(r, words, minlen, maxlen) for r in runs) / total


def stream(units, kmap):
    """Decoded letters with '|' at every unknown unit and clear word."""
    out = []
    for p in align.decode_units(units, kmap):
        if p is None or p.startswith("["):
            out.append("|")
        else:
            out.append(p)
    return "".join(out)


def measure(units, kmap, words, minlen):
    s = stream(units, kmap)
    runs = [r for r in s.split("|") if r]
    dec = sum(len(r) for r in runs)
    maxlen = max((len(w) for w in words), default=0)
    cov = sum(covered(r, words, minlen, maxlen) for r in runs)
    return dec, cov, (cov / dec if dec else 0.0)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("cipher"), ap.add_argument("key"), ap.add_argument("wordlist")
    ap.add_argument("--perms", type=int, default=20)
    ap.add_argument("--minlen", type=int, default=3)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--min", default="probable", help="lowest key status used: probable or certain")
    ap.add_argument("--no-merge", action="store_true")
    a = ap.parse_args(argv)
    merge = not a.no_merge
    with open(a.cipher, encoding="utf-8") as f:
        units, _, _ = align.parse_cipher(f.read(), merge)
    kmap = align.key_map(align.read_key(a.key), a.min)
    words = load_words(a.wordlist, merge)
    dec, cov, share = measure(units, kmap, words, a.minlen)
    rng = random.Random(a.seed)
    shares = [measure(units, align.permuted(kmap, rng), words, a.minlen)[2] for _ in range(a.perms)]
    signs = [u for u in units if u.kind == "sign"]
    out = [("units", len(signs)), ("units_unknown", sum(1 for u in signs if u.sym not in kmap)),
           ("words_in_list", len(words)), ("minlen", a.minlen),
           ("letters_decoded", dec), ("letters_covered", cov), ("share", f"{share:.3f}"),
           ("perms", a.perms),
           ("perm_mean_share", f"{sum(shares) / len(shares):.3f}" if shares else "NA"),
           ("perm_max_share", f"{max(shares):.3f}" if shares else "NA")]
    for k, v in out:
        print(f"{k}\t{v}")


if __name__ == "__main__":
    main()

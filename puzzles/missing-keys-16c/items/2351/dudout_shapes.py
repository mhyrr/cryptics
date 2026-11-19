"""dudout_shapes.py - counts behind results/dudout-shapes.md: Dudout's tokens against our sign names.

    python3 -I dudout_shapes.py        -> results/dudout-counts.tsv

His files hold no images, so a shape can be compared only by his written legend and by how a sign behaves:
how often it stands, whether it takes a figure above, and what stands next to it. His transcriptions
(sources/raw-bourdeau-2026-11-19/, fetched 2026-11-19 from github.com/dbourdeau/cyphersolver, CLAIMANT) are
read as data only. Ours: work/A-merged.txt and work/B-merged.txt.
"""
import collections, glob, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "sources", "raw-bourdeau-2026-11-19")


def theirs():
    toks = []
    for f in sorted(glob.glob(os.path.join(RAW, "*transcription_*.txt"))):
        for ln in open(f, encoding="utf-8"):
            if ln.startswith("#") or ":" not in ln[:12]:
                continue
            body = re.sub(r"\[.*?\]", " ", ln.split(":", 1)[1])
            toks += [t.rstrip("?") for t in body.split() if t.rstrip("?")]
            toks.append("|")
    return toks


def ours():
    toks = []
    for name in ("A-merged.txt", "B-merged.txt"):
        for ln in open(os.path.join(HERE, "work", name), encoding="utf-8"):
            if not ln.startswith("#"):
                toks += [t.replace("+", "^") for t in ln.split()] + ["|"]
    return toks


def base(t):
    return t.split("^")[0]


def mark(t):
    return t.split("^")[1] if "^" in t else ""


def report(name, toks, signs, vowel_marks):
    n = sum(t != "|" for t in toks)
    out = [f"## {name}: {n} tokens"]
    vowel_marks = list(vowel_marks)
    mk = collections.Counter(mark(t) for t in toks if mark(t) in vowel_marks)
    tot = sum(mk.values())
    out.append(f"vowel marks ({tot}; share of them, share of all tokens)\t" + "\t".join(
        f"^{m} {mk[m]} ({mk[m] / tot:.3f}, {mk[m] / n:.3f})" for m in vowel_marks))
    out.append("sign\tbare\tper_1000\twith_vowel_mark\tcommonest before (bare)\tcommonest after (bare)")
    for s in signs:
        bare = [i for i, t in enumerate(toks) if t == s]
        marked = sum(1 for t in toks if base(t) == s and mark(t) in vowel_marks)
        bef = collections.Counter(toks[i - 1] for i in bare if i > 0)
        aft = collections.Counter(base(toks[i + 1]) for i in bare if i + 1 < len(toks))
        f = lambda c: " ".join(f"{k}×{v}" for k, v in c.most_common(4))
        out.append(f"{s}\t{len(bare)}\t{1000 * len(bare) / n:.1f}\t{marked}\t{f(bef)}\t{f(aft)}")
    return out


def main():
    out = report("Dudout, Pandolfini 1514-15 (7 transcriptions)", theirs(),
                 ["F", "J", "H", "4#", "L#", "Z", "2", "0", "M", "α", "P", "t#", "W", "6", "y"], "12345")
    out += [""] + report("ours, Acciaiuoli 1513 (letters A and B, merged)", ours(),
                         ["flong", "gamma", "hash", "L4", "tt", "ttt", "2", "z", "zm", "Q", "alpha", "bbar",
                          "omega", "6", "y"], "1~345")
    t = ours()
    one = collections.Counter(base(x) for x in t if mark(x) == "1")
    out += ["", "our ^1 by base\t" + " ".join(f"{k}×{v}" for k, v in one.most_common())]
    th = theirs()
    one = collections.Counter(base(x) for x in th if mark(x) == "1")
    out += ["their ^1 by base\t" + " ".join(f"{k}×{v}" for k, v in one.most_common())]
    open(os.path.join(HERE, "results", "dudout-counts.tsv"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()

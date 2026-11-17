"""doubles.py - join immediate repeats of a sign into one token where the data say the pair is a sign.

    python3 doubles.py <cipher.txt> [--report doubles.tsv] > <cipher-doubles.txt>
Added after the stage 4 failure (README, "After the failure"). The sign guide told readers to write each sign
of a doubled shape. Counting shows that for a few signs the pair is far commoner than chance (a a: 80 pairs
where 8 are expected), so the pair is a sign of its own and must not share a value with the single sign.
Rule, from counts only: a sign x is joined as `xx` when x x occurs at least 4 times and at least 4 times as
often as its frequency predicts. Pairs are taken left to right; a third x stays single.
"""
import collections, re, sys


def main(path, report=None):
    rows = open(path, encoding="utf-8").read().splitlines()
    toks = [t for r in rows if not r.startswith("#") for t in re.sub(r"\[\[.*?\]\]", " | ", r).split()]
    n = len(toks)
    c = collections.Counter(toks)
    bi = collections.Counter(zip(toks, toks[1:]))
    join, rep = set(), []
    for x, k in c.items():
        if x in ("?", "|") or x.endswith("?") or "|" in x:
            continue
        pairs, exp = bi[(x, x)], k * k / n
        ok = pairs >= 4 and pairs >= 4 * exp
        rep.append((x, k, pairs, round(exp, 1), "join" if ok else ""))
        if ok:
            join.add(x)
    if report:
        with open(report, "w") as f:
            f.write("sign\tcount\tpairs\texpected\tdecision\n")
            for r in sorted(rep, key=lambda r: -r[2]):
                if r[2]:
                    f.write("\t".join(map(str, r)) + "\n")
    for r in rows:
        if r.startswith("#"):
            print(r)
            continue
        out = []
        for part in re.split(r"(\[\[.*?\]\])", r):
            if part.startswith("[["):
                out.append(part)
                continue
            ts, i = part.split(), 0
            while i < len(ts):
                if ts[i] in join and i + 1 < len(ts) and ts[i + 1] == ts[i]:
                    out.append(ts[i] + ts[i])
                    i += 2
                else:
                    out.append(ts[i])
                    i += 1
        print(" ".join(out))


if __name__ == "__main__":
    rp = sys.argv[sys.argv.index("--report") + 1] if "--report" in sys.argv else None
    main(sys.argv[1], rp)

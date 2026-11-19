"""plain_compare.py - agreement between the two plain readers of each page, clear words and gloss apart.

    python3 -I plain_compare.py            -> results/plain-agree.tsv and a summary on stdout

A row is `Lnn y=.. | text`. Clear words are the words outside `{...}`; gloss words are those inside (margin
gloss included). Words are lower-cased; `(...)` expansions are kept as letters; `[?]` is dropped from the word;
`[...]` and partial words holding `[...]` count as unread. Per line, the two readers' word lists are aligned
(difflib); agreement = matched words / the longer list. Lines past the shorter file (signature rows) are left out.
"""
import difflib, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
PAIRS = {"2947-691": ("PA", "PB"), "2947-692": ("PA", "PB"), "2947-693": ("PC", "PD"),
         "2947-694": ("PC", "PD"), "2946-c215": ("PC", "PD")}


def parse(path):
    rows = {}
    for ln in open(path, encoding="utf-8"):
        m = re.match(r"(L\d+)\s+y=\S*\s*\|\s*(.*)", ln.strip())
        if not m:
            continue
        txt = m.group(2)
        gloss = " ".join(re.findall(r"\{(?:margin:)?([^}]*)\}", txt))
        clear = re.sub(r"\{[^}]*\}", " ", txt).replace("[cipher]", " ")
        rows[m.group(1)] = (words(clear), words(gloss))
    return rows


def words(s):
    out = []
    for w in s.split():
        w = w.lower().replace("[?]", "").replace("(", "").replace(")", "").replace("^", "")
        if "[...]" in w or not re.search(r"[a-z]", w):
            continue
        out.append(re.sub(r"[^a-z]", "", w))
    return [w for w in out if w]


def agree(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return sum(t.size for t in sm.get_matching_blocks()), max(len(a), len(b))


def main():
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    out = ["page\tline\tclear_match\tclear_n\tgloss_match\tgloss_n"]
    print("page\tlines\tclear\tgloss (matched words / longer list)")
    for page, (r1, r2) in PAIRS.items():
        a = parse(os.path.join(HERE, "readers", r1, page + ".txt"))
        b = parse(os.path.join(HERE, "readers", r2, page + ".txt"))
        tot = [0, 0, 0, 0]
        for k in sorted(set(a) & set(b)):
            cm, cn = agree(a[k][0], b[k][0])
            gm, gn = agree(a[k][1], b[k][1])
            out.append(f"{page}\t{k}\t{cm}\t{cn}\t{gm}\t{gn}")
            for i, v in enumerate((cm, cn, gm, gn)):
                tot[i] += v
        print(f"{page}\t{len(set(a) & set(b))}\t{tot[0]}/{tot[1]} = {tot[0]/max(1,tot[1]):.2f}\t"
              f"{tot[2]}/{tot[3]} = {tot[2]/max(1,tot[3]):.2f}")
    open(os.path.join(HERE, "results", "plain-agree.tsv"), "w").write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

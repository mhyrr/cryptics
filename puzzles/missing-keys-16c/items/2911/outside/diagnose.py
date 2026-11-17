"""diagnose.py - ceiling, coverage and reader error for the 2911 pair, measured with the period key (truth.tsv).

    python3 diagnose.py            (about ten minutes; writes the files below beside itself)

Inputs  ../work/cipher-primary.txt (both-readers consensus, base+mark joined), ../work/cipher-doubles.txt,
        ../readers/A/*.txt and ../readers/B/*.txt through ../units.py, truth.tsv,
        ../work/plain-print.txt (1877 print of Machiavelli's copy), ../work/plain-consensus.txt.
Outputs diagnosis.tsv      one row per measure (input, plain side, measure, value, note)
        uncovered.tsv      stretches of the cipher with no counterpart in the plain text
        reader-error.tsv   reader A against reader B, judged by the printed text
        name-evidence.tsv  per reader name: what the printed text has between its neighbours (HOLDS VALUES)
        decode-*.txt       the decodes (HOLD VALUES)

Method. decode.py turns tokens into items (one truth.tsv row applied, or an unread / unknown sign). The decoded
letters are aligned to the plain letters by seqalign.py (affine gaps, so cipher text the copy left out is not
forced on to the plain text). An item is "anchored" if at least one of its letters sits on an equal plain letter.
A run of MINGAP or more source tokens without an anchored item is a gap; what lies between two gaps is an
island; an island with fewer than ISL_MIN matched letters or a match rate under ISL_RATE is dissolved into the
gaps round it. The gaps left are the "uncovered stretches". Plain text is normalised by ../../../line/align.py
(parse_plain: lower case, no accents, u/v and i/j merged, lacunae dropped).
The held-out-style figure uses align.score line by line: for each manuscript line, the true-key pieces of its
covered items against the stretch of plain text they span (matched / decoded letters, as align.heldout does).
"""
import os, sys, csv, glob, difflib, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ITEM = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, ITEM); sys.path.insert(0, os.path.join(ITEM, "..", "..", "line"))
import decode, seqalign, units, align

MINGAP, ISL_MIN, ISL_RATE = 10, 12, 0.40
LETTERED = ("letter", "syllable", "double", "word", "name")
PAGES = ("V140-1r", "V140-1v", "V140-2r")


def read(p):
    return open(os.path.join(ITEM, p), encoding="utf-8").read()


def cipher_text(label):
    if label == "primary":
        return read("work/cipher-primary.txt")
    if label == "doubles":
        return read("work/cipher-doubles.txt")
    return "".join(units.join_text(read("readers/%s/%s.txt" % (label[-1], pg))) for pg in PAGES)


def plain(label):
    P, wb, lac, _ = align.parse_plain(read("work/plain-%s.txt" % label))
    return P


def alt_values():
    """truth.tsv column also_covers -> {seq: [other sheet values the same reader name stands for]}."""
    skip = ("a figure", "first half", "digit", "probably", "part of", "half of", "c with")
    out = {}
    with open(os.path.join(HERE, "truth.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            vals = []
            for part in r["also_covers"].split(";"):
                part = part.strip()
                if not part or part.startswith(skip):
                    continue
                w = part.split(" ")[0]
                vals.append("" if w == "null" else w)
            if vals and r["type"] != "none":
                out[tuple(r["seq"].split())] = vals
    return out


def oracle(R):
    """Places where the truth value does not sit on the print but another sheet value of the same reader name
    is exactly what the print has between the two neighbours. -> {item index: value}, counts per name."""
    alts, it, P = alt_values(), R["items"], R["P"]
    sub, judged, hit = {}, collections.Counter(), collections.Counter()
    for k, x in enumerate(it):
        if x["names"] not in alts or not (0 < k < len(it) - 1) or not x.get("cov"):
            continue
        if not (it[k - 1]["ppos"] and it[k + 1]["ppos"]):
            continue
        a, b = it[k - 1]["ppos"][-1], it[k + 1]["ppos"][0]
        if not 0 <= b - a - 1 <= 6:
            continue
        nm = " ".join(x["names"])
        judged[nm] += 1
        between = P[a + 1:b]
        if between == x["letters"]:
            continue
        for v in alts[x["names"]]:
            if between == v or (v and between == v.replace("et", "e")):
                sub[k] = v; hit[nm] += 1
                break
    return sub, judged, hit


def analyse(text, P, key, override=None):
    rows = decode.decode_text(text, key)
    items = []
    for ln, row in enumerate(rows, 1):
        for it in row:
            it = dict(it, line=ln, letters=decode.norm(it["value"]) if it["type"] in LETTERED else "")
            items.append(it)
    for k, v in (override or {}).items():
        items[k]["letters"] = v
        if items[k]["type"] == "null" and v:
            items[k]["type"] = "syllable"
    D, owner = [], []
    for k, it in enumerate(items):
        for ch in it["letters"]:
            D.append(ch); owner.append(k)
    pairs = seqalign.align("".join(D), P)
    for it in items:
        it["m"], it["x"], it["g"], it["ppos"] = 0, 0, 0, []
    pgap = 0
    for i, j in pairs:
        if i is None:
            pgap += 1
            continue
        it = items[owner[i]]
        if j is None:
            it["g"] += 1
        elif D[i] == P[j]:
            it["m"] += 1; it["ppos"].append(j)
        else:
            it["x"] += 1
    # gaps and islands over source tokens
    n = len(items)
    cov = [None] * n                       # True covered, False uncovered
    runs, k = [], 0
    while k < n:
        a = items[k]["m"] > 0
        e = k
        while e < n and (items[e]["m"] > 0) == a:
            e += 1
        runs.append([a, k, e]); k = e
    ntok = lambda a, b: sum(len(items[q]["src"]) for q in range(a, b) if items[q]["type"] != "clear")
    blocks = []                             # alternate island / gap
    for a, s, e in runs:
        isgap = (not a) and ntok(s, e) >= MINGAP
        if blocks and blocks[-1][0] == isgap:
            blocks[-1][2] = e
        else:
            blocks.append([isgap, s, e])
    changed = True
    while changed:
        changed = False
        for b in blocks:
            if not b[0]:
                m = sum(items[q]["m"] for q in range(b[1], b[2]))
                d = sum(len(items[q]["letters"]) for q in range(b[1], b[2]))
                edge = b is blocks[0] or b is blocks[-1]
                if m < ISL_MIN or m / max(1, d) < ISL_RATE:
                    b[0] = True; changed = True
        merged = []
        for b in blocks:
            if merged and merged[-1][0] == b[0]:
                merged[-1][2] = b[2]
            else:
                merged.append(b)
        blocks = merged
    for isgap, s, e in blocks:
        for q in range(s, e):
            items[q]["cov"] = not isgap
    return dict(rows=rows, items=items, D="".join(D), P=P, pgap=pgap, blocks=blocks)


def measures(R):
    it = [x for x in R["items"] if x["type"] != "clear"]
    tok = lambda xs: sum(len(x["src"]) for x in xs)
    allt, unread = tok(it), tok([x for x in it if x["type"] == "unread"])
    missing = tok([x for x in it if x["type"] == "missing"])
    valued = [x for x in it if x["type"] not in ("unread", "missing")]
    L = sum(len(x["letters"]) for x in valued)
    out = collections.OrderedDict()
    out["source tokens (signs and unread)"] = allt
    out["unread tokens"] = unread
    out["tokens the truth table has no row for"] = missing
    out["tokens given a value"] = tok(valued)
    out["share of all tokens given a value"] = tok(valued) / allt
    out["share of read tokens given a value"] = tok(valued) / (allt - unread)
    out["valued items (a doubled or split sign counts once)"] = len(valued)
    out["decoded letters"] = L
    out["letters per valued item"] = L / len(valued)
    out["letters per valued token"] = L / tok(valued)
    out["letters per token, unread and unknown included"] = L / allt
    for ty in ("null", "letter", "syllable", "double", "word", "name"):
        k = [x for x in valued if x["type"] == ty]
        out["share of valued items: " + ty] = len(k) / len(valued)
    multi = [x for x in valued if len(x["src"]) > 1]
    out["share of valued items written by the readers as two or more tokens"] = len(multi) / len(valued)
    M = sum(x["m"] for x in it); X = sum(x["x"] for x in it); G = sum(x["g"] for x in it)
    out["plain letters"] = len(R["P"])
    out["decoded letters on an equal plain letter (matched)"] = M
    out["decoded letters on a different plain letter"] = X
    out["decoded letters with no plain partner"] = G
    out["plain letters with no decoded partner"] = R["pgap"]
    out["share of decoded letters matched, whole pair"] = M / max(1, L)
    out["share of plain letters accounted for (matched)"] = M / max(1, len(R["P"]))
    cov = [x for x in it if x["cov"]]
    Lc = sum(len(x["letters"]) for x in cov); Mc = sum(x["m"] for x in cov)
    out["tokens in covered stretches"] = tok(cov)
    out["share of tokens in covered stretches"] = tok(cov) / allt
    out["share of tokens in uncovered stretches"] = 1 - tok(cov) / allt
    out["share of decoded letters matched, covered stretches only"] = Mc / max(1, Lc)
    out["unread share of tokens in covered stretches"] = tok([x for x in cov if x["type"] == "unread"]) / max(1, tok(cov))
    # align.score, line by line
    for name, sel in (("covered stretches", lambda x: x["cov"]), ("whole pair", lambda x: True)):
        mat = dec = tru = 0
        by = collections.defaultdict(list)
        for x in R["items"]:
            if sel(x):
                by[x["line"]].append(x)
        for ln, xs in by.items():
            pos = [p for x in xs for p in x["ppos"]]
            truth = R["P"][min(pos):max(pos) + 1] if pos else ""
            pieces = []
            for x in xs:
                if x["type"] == "clear":
                    pieces.append("[" + decode.norm(x["value"]) + "]")
                elif x["type"] in ("unread", "missing"):
                    pieces.append(None)
                else:
                    pieces.append(x["letters"])
            a, b, t = align.score(pieces, truth)
            mat += a; dec += b; tru += t
        out["align.score accuracy (matched / decoded letters), true key, %s" % name] = mat / max(1, dec)
        out["align.score recall (matched / plain letters), true key, %s" % name] = mat / max(1, tru)
    return out


def stretches(R):
    it = R["items"]
    out = []
    nb = len(R["blocks"])
    for bi, (isgap, s, e) in enumerate(R["blocks"]):
        if not isgap:
            continue
        xs = [x for x in it[s:e] if x["type"] != "clear"]
        if not xs:
            continue
        where = "opening" if bi == 0 else "closing" if bi == nb - 1 else "interior"
        out.append(dict(where=where, first_unit=xs[0]["src"][0], last_unit=xs[-1]["src"][-1],
                        first_line=xs[0]["line"], last_line=xs[-1]["line"],
                        tokens=sum(len(x["src"]) for x in xs),
                        unread=sum(len(x["src"]) for x in xs if x["type"] == "unread"),
                        decoded_letters=sum(len(x["letters"]) for x in xs)))
    return out


def evidence(R, path):
    it = R["items"]
    res, tot, cur = collections.defaultdict(collections.Counter), collections.Counter(), {}
    P = R["P"]
    for k, x in enumerate(it):
        nm = " ".join(x["names"])
        tot[nm] += 1
        cur[nm] = x["value"] if x["type"] in LETTERED else {"null": "(null)"}.get(x["type"], "(%s)" % x["type"])
        if 0 < k < len(it) - 1 and it[k - 1]["ppos"] and it[k + 1]["ppos"]:
            a, b = it[k - 1]["ppos"][-1], it[k + 1]["ppos"][0]
            if 0 <= b - a - 1 <= 14:
                res[nm][P[a + 1:b]] += 1
    with open(path, "w", encoding="utf-8") as f:
        f.write("name\tcount\ttruth_value\tplaces_judged\tplain_between_neighbours\n")
        for nm, n in tot.most_common():
            c = res[nm]
            f.write("%s\t%d\t%s\t%d\t%s\n" % (nm, n, cur[nm], sum(c.values()),
                    " ".join("%s:%d" % (s or "(nothing)", v) for s, v in c.most_common(8))))


def flags(R):
    """per source token: (name, 'agree' | 'disagree' | 'out' | 'neutral')."""
    out = {}
    for x in R["items"]:
        if x["type"] == "clear":
            continue
        if not x["cov"]:
            f = "out"
        elif x["type"] == "null":
            f = "neutral"
        elif x["letters"] and x["m"] == len(x["letters"]):
            f = "agree"
        else:
            f = "disagree"
        for s, nm in zip(x["src"], x["names"]):
            out[s] = (nm, f)
    return [out[s] for s in sorted(out)]


def reader_error(RA, RB, path):
    fa, fb = flags(RA), flags(RB)
    sm = difflib.SequenceMatcher(None, [n for n, _ in fa], [n for n, _ in fb], autojunk=False)
    err = {"A": 0, "B": 0}
    conf = collections.Counter()
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        a, b = fa[i1:i2], fb[j1:j2]
        for who, mine, other in (("A", a, b), ("B", b, a)):
            if mine and other and all(f == "agree" for _, f in other) and any(f == "disagree" for _, f in mine):
                err[who] += sum(1 for _, f in mine if f == "disagree")
                conf[(who, " ".join(n for n, _ in other), " ".join(n for n, _ in mine))] += 1
    res = {}
    for who, fl in (("A", fa), ("B", fb)):
        inside = [f for _, f in fl if f != "out"]
        res[who] = dict(tokens=len(fl), covered=len(inside), agree=inside.count("agree"),
                        disagree=inside.count("disagree"), err=err[who])
    with open(path, "w", encoding="utf-8") as f:
        f.write("# part 1: per reader\nreader\ttokens\tin_covered_stretches\tagree_with_print\tdisagree_with_print\t"
                "disagree_where_other_reader_agrees\tshare_of_covered_tokens\n")
        for who in "AB":
            r = res[who]
            f.write("%s\t%d\t%d\t%d\t%d\t%d\t%.3f\n" % (who, r["tokens"], r["covered"], r["agree"], r["disagree"],
                                                      r["err"], r["err"] / max(1, r["covered"])))
        f.write("# part 2: sign names misread (the name the agreeing reader wrote -> what the other wrote), both readers\n"
                "right_name\twritten_as\tcount\treaders\n")
        agg = collections.defaultdict(collections.Counter)
        for (who, right, wrong), c in conf.items():
            agg[(right, wrong)][who] += c
        for (right, wrong), c in sorted(agg.items(), key=lambda kv: -sum(kv[1].values())):
            f.write("%s\t%s\t%d\t%s\n" % (right, wrong, sum(c.values()), ",".join("%s:%d" % kv for kv in sorted(c.items()))))
        f.write("# part 3: the ten right names most often misread\nright_name\ttimes\twritten_as\n")
        byr = collections.defaultdict(collections.Counter)
        for (right, wrong), c in agg.items():
            byr[right][wrong] += sum(c.values())
        for right, c in sorted(byr.items(), key=lambda kv: -sum(kv[1].values()))[:10]:
            f.write("%s\t%d\t%s\n" % (right, sum(c.values()), "; ".join("%s x%d" % kv for kv in c.most_common(5))))
    return res


def main():
    key = decode.load_truth()
    rows_out, R = [], {}
    def put(inp, pl, d):
        for k, v in d.items():
            rows_out.append((inp, pl, k, ("%.3f" % v) if isinstance(v, float) else str(v)))
    for inp in ("primary", "doubles", "reader-A", "reader-B"):
        txt = cipher_text(inp)
        with open(os.path.join(HERE, "decode-%s.txt" % inp), "w", encoding="utf-8") as f:
            for n, row in enumerate(decode.decode_text(txt, key), 1):
                f.write("L%02d\t%s\n\t%s\n" % (n, " ".join("%s=%s" % ("_".join(i["names"]), decode.show(i)) for i in row),
                                              decode.running(row)))
    same = open(os.path.join(HERE, "decode-primary.txt")).read() == open(os.path.join(HERE, "decode-doubles.txt")).read()
    rows_out.append(("doubles", "-", "decode identical to primary (joined pairs are split back; truth.tsv keys doubles as sequences)", str(same)))
    for inp, pl in (("primary", "print"), ("primary", "consensus"), ("reader-A", "print"), ("reader-B", "print")):
        print("aligning", inp, pl, file=sys.stderr)
        r = analyse(cipher_text(inp), plain(pl), key)
        R[(inp, pl)] = r
        put(inp, pl, measures(r))
        if inp == "primary":
            st = stretches(r)
            with open(os.path.join(HERE, "uncovered-%s.tsv" % pl), "w", encoding="utf-8") as f:
                cols = ["where", "first_unit", "last_unit", "first_line", "last_line", "tokens", "unread", "decoded_letters"]
                f.write("\t".join(cols) + "\n")
                for s in st:
                    f.write("\t".join(str(s[c]) for c in cols) + "\n")
            tot = sum(s["tokens"] for s in st)
            put(inp, pl, collections.OrderedDict([
                ("uncovered stretches (count)", len(st)),
                ("tokens in uncovered stretches", tot),
                ("of which opening", sum(s["tokens"] for s in st if s["where"] == "opening")),
                ("of which interior", sum(s["tokens"] for s in st if s["where"] == "interior")),
                ("of which closing", sum(s["tokens"] for s in st if s["where"] == "closing")),
                ("longest uncovered stretch (tokens)", max([s["tokens"] for s in st] or [0]))]))
    evidence(R[("primary", "print")], os.path.join(HERE, "name-evidence.tsv"))
    # how much of the shortfall is one reader name standing for several sheet signs
    sub, judged, hit = oracle(R[("primary", "print")])
    r2 = analyse(cipher_text("primary"), plain("print"), key, override=sub)
    m2 = measures(r2)
    keep = ("share of decoded letters matched, covered stretches only", "share of plain letters accounted for (matched)",
            "align.score accuracy (matched / decoded letters), true key, covered stretches",
            "share of tokens in uncovered stretches")
    put("primary, merged names resolved at judged places", "print", collections.OrderedDict((k, m2[k]) for k in keep))
    put("primary, merged names resolved at judged places", "print", collections.OrderedDict([
        ("places judged (name stands for more than one sheet sign, both neighbours on the print)", sum(judged.values())),
        ("of those, places where another sheet sign of the same name is what the print has", sum(hit.values()))]))
    with open(os.path.join(HERE, "merged-names.tsv"), "w", encoding="utf-8") as f:
        f.write("name\ttokens_in_pair\tplaces_judged\tother_sheet_sign_fits\tshare\n")
        tot = collections.Counter(" ".join(x["names"]) for x in R[("primary", "print")]["items"])
        for nm, n in judged.most_common():
            f.write("%s\t%d\t%d\t%d\t%.3f\n" % (nm, tot[nm], n, hit[nm], hit[nm] / n))
    res = reader_error(R[("reader-A", "print")], R[("reader-B", "print")], os.path.join(HERE, "reader-error.tsv"))
    for who in "AB":
        r = res[who]
        put("reader-" + who, "print", collections.OrderedDict([
            ("reader error: tokens disagreeing with print where the other reader agrees", r["err"]),
            ("reader error: share of the reader's tokens in covered stretches", r["err"] / max(1, r["covered"])),
            ("tokens agreeing with print, share of covered", r["agree"] / max(1, r["covered"]))]))
    with open(os.path.join(HERE, "diagnosis.tsv"), "w", encoding="utf-8") as f:
        f.write("input\tplain_side\tmeasure\tvalue\n")
        for r in rows_out:
            f.write("\t".join(r) + "\n")


if __name__ == "__main__":
    main()

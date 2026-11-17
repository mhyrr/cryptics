"""score.py - score a built key table against the period key, place by place. HOLDS NO VALUES in its output.

    python3 score.py <key.tsv> <cipher.txt> [--min probable]
The cipher file is decoded twice: with the true key (../outside/truth.tsv, through ../outside/decode.py) and
with the built table. The true decode groups tokens into sheet signs (a doubled sign is one item). For each
item the built value is the built table's values of its tokens joined (a token doubles.py joined, `aa`, counts
for both halves). An item is:
  right    built value == true value (u/v, i/j merged); a true null needs a built null
  wrong    the built table gives a value and it differs
  silent   the built table has no marked value for one of the item's units
Reported: items, coverage (not silent), precision (right / (right + wrong)), recall (right / items), the same
over sign types that occur ten times or more, the null share of built values, and table counts:
marked rows right / wrong against truth.tsv (a row is right if its value is the value of any sheet sign its
name covers: truth.tsv `value` or a value named in `also_covers`).
"""
import csv, os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "outside"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "line"))
import decode, align  # noqa: E402


def built_units(path):
    """-> {source token index: unit name as align.py sees it}."""
    out, src = {}, 0
    for row in open(path, encoding="utf-8").read().splitlines():
        if not row.strip() or row.lstrip().startswith("#"):
            continue
        for part in re.split(r"(\[\[.*?\]\])", row):
            if part.startswith("[["):
                src += len(part[2:-2].split())
                continue
            for t in part.split():
                if t.startswith("@"):
                    continue
                out[src] = "?" if t == "?" else t.rstrip("?").split("|")[0]
                src += 1
    return out


def score(key_path, cipher_path, minimum="probable"):
    kmap = align.key_map(align.read_key(key_path), minimum)
    truth = decode.load_truth()
    rows = decode.decode_file(cipher_path, truth)
    units = built_units(cipher_path)
    tally, by_sign = collections.Counter(), collections.defaultdict(collections.Counter)
    nulls = valued = 0
    for row in rows:
        for it in row:
            if it["type"] in ("clear", "unread", "missing"):
                continue
            srcs = sorted(set(it["src"]))
            vals = [kmap.get(units[s]) for s in srcs]
            name = " ".join(it["names"])
            if any(v is None for v in vals):
                verdict = "silent"
            else:
                built = "".join(vals)
                valued += 1
                nulls += built == ""
                tv = decode.norm(it["value"] or "")
                ok = decode.norm(built) == tv and (built == "") == (it["type"] == "null")
                verdict = "right" if ok else "wrong"
            tally[verdict] += 1
            by_sign[name][verdict] += 1
    n = sum(tally.values())
    freq = {s: c for s, c in by_sign.items() if sum(c.values()) >= 10}
    fr = sum(1 for c in freq.values() if c["right"] > c["wrong"] + c["silent"])
    # table rows
    tv = collections.defaultdict(set)
    for r in csv.DictReader(open(os.path.join(HERE, "..", "outside", "truth.tsv"), encoding="utf-8"), delimiter="\t"):
        if r["type"] == "none":
            continue
        tv[r["unit"]].add(decode.norm(r["value"]))
        for m in re.finditer(r"(?:^|;\s*)([a-z]+|null)\s*\(", r["also_covers"] or ""):
            tv[r["unit"]].add("" if m.group(1) == "null" else decode.norm(m.group(1)))
    mr = mw = mo = 0
    for u, v in kmap.items():
        u2 = {"aa": "a a", "bb": "b b", "ss": "s s", "ff": "f f", "oo": "o o"}.get(u, u)
        if u2 not in tv:
            mo += 1
        elif decode.norm(v) in tv[u2]:
            mr += 1
        else:
            mw += 1
    return [("items", n), ("coverage", round(1 - tally["silent"] / n, 3)),
            ("precision", round(tally["right"] / max(1, tally["right"] + tally["wrong"]), 3)),
            ("recall", round(tally["right"] / n, 3)),
            ("frequent_signs", len(freq)), ("frequent_signs_mostly_right", fr),
            ("built_null_share", round(nulls / max(1, valued), 3)),
            ("marked_rows", len(kmap)), ("marked_rows_right", mr), ("marked_rows_wrong", mw),
            ("marked_rows_not_a_sheet_sign", mo)]


if __name__ == "__main__":
    a = sys.argv[1:]
    mn = a[a.index("--min") + 1] if "--min" in a else "probable"
    for k, v in score(a[0], a[1], mn):
        print(f"{k}\t{v}")

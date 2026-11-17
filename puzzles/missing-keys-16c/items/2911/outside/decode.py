"""decode.py - decode a cipher transcription of item 2911 with the period key as read into truth.tsv.

    python3 decode.py <cipher.txt> [--out decode.txt]

Input: a reader file (tokens `base^mark`) or a file already through ../units.py or ../doubles.py (`base+mark`,
`aa`). Every token is brought to one form: `+` is read as `^`, a trailing `?` is dropped, `a|b` takes a, and a
token that doubles.py joined (`aa`, `bb`, `ss`, `ff`, `oo`) is split back into its two copies, because
truth.tsv keys the sheet's doubled signs as sequences (`a a`). truth.tsv rows whose `seq` has several tokens
are matched first, longest first, left to right; then single tokens. A bare `?` is an unread sign. Clear words
`[[..]]` are kept. Output, two rows per manuscript line: `token=value` pairs (`#` unread, `~` sign not in
truth.tsv, `0` null; a sequence is shown joined by `_`), then the running text.
"""
import os, re, sys, csv, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
DOUBLED = {"aa": "a", "bb": "b", "ss": "s", "ff": "f", "oo": "o"}


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(ch for ch in s if ch.isalpha() and ord(ch) < 128)
    return s.replace("v", "u").replace("j", "i")


def load_truth(path=None):
    key = {}
    with open(path or os.path.join(HERE, "truth.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r["type"] != "none":                  # rows of type none: reader forms the sheets do not have
                key[tuple(r["seq"].split())] = (r["value"], r["type"])
    return key


def tokens(row, start=0):
    """-> list of (kind, name, src) ; src = index of the source token in file order (clear words one each)."""
    out, src = [], start
    for part in re.split(r"(\[\[.*?\]\])", row):
        if part.startswith("[["):
            for w in part[2:-2].split():
                out.append(("clear", w, src)); src += 1
            continue
        for t in part.split():
            if t.startswith("@"):
                continue
            if t == "?":
                out.append(("unread", "?", src)); src += 1
                continue
            t = t.rstrip("?").split("|")[0].replace("+", "^")
            if t in DOUBLED:
                out += [("sign", DOUBLED[t], src)] * 2
            else:
                out.append(("sign", t, src))
            src += 1
    return out


def decode_tokens(toks, key):
    """-> list of dict(names, value, type, src) ; type: clear, unread, missing, or the truth type."""
    longest = max(len(k) for k in key)
    out, i = [], 0
    while i < len(toks):
        kind, t, src = toks[i]
        if kind == "clear":
            out.append(dict(names=("[[%s]]" % t,), value=t, type="clear", src=[src])); i += 1; continue
        if kind == "unread":
            out.append(dict(names=("?",), value=None, type="unread", src=[src])); i += 1; continue
        for n in range(longest, 0, -1):
            seg = toks[i:i + n]
            if len(seg) == n and all(k == "sign" for k, _, _ in seg):
                k = tuple(x for _, x, _ in seg)
                if k in key:
                    v, ty = key[k]
                    out.append(dict(names=k, value=v, type=ty, src=[s for _, _, s in seg])); i += n
                    break
        else:
            out.append(dict(names=(t,), value=None, type="missing", src=[src])); i += 1
    return out


def decode_text(text, key):
    """-> list of rows (one per manuscript line), each a list of items from decode_tokens."""
    rows, src = [], 0
    for row in text.splitlines():
        if not row.strip() or row.lstrip().startswith("#"):
            continue
        toks = tokens(row, src)
        if toks:
            src = toks[-1][2] + 1
        rows.append(decode_tokens(toks, key))
    return rows


def decode_file(path, key):
    return decode_text(open(path, encoding="utf-8").read(), key)


def show(it):
    return {"unread": "#", "missing": "~", "null": "0"}.get(it["type"], it["value"])


def running(row):
    return "".join({"unread": "#", "missing": "~", "null": ""}.get(it["type"], " [%s] " % it["value"] if it["type"] == "clear"
                                                                   else it["value"]) for it in row)


def main(argv=None):
    a = argv or sys.argv[1:]
    out = a[a.index("--out") + 1] if "--out" in a else None
    rows = decode_file(a[0], load_truth())
    text = []
    for n, row in enumerate(rows, 1):
        text.append("L%02d\t" % n + " ".join("%s=%s" % ("_".join(it["names"]), show(it)) for it in row))
        text.append("\t" + running(row))
    res = "\n".join(text) + "\n"
    if out:
        open(out, "w", encoding="utf-8").write(res)
    else:
        sys.stdout.write(res)


if __name__ == "__main__":
    main()

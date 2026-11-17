"""units.py - join each base and its marks into one unit for align.py (the unit decision of SIGN-GUIDE.md section 4).

    python3 units.py <cipher.txt> [--out <joined.txt>]

Readers write `base^mark`. align.py's split_token would score `a^o` as two units, 'a' and '^o'. This script
rewrites every `^` inside a sign token to `+`, so `a^o` becomes the single unit `a+o` and `y^o^wave` becomes
`y+o+wave`. Doubt marks (`?`), alternatives (`a|b`, each side rewritten), clear words (`[[...]]`), anchors
(`@name`) and comment rows are left as they are. The reader files are never changed: this writes a copy.
"""
import argparse, re, sys


def join_token(tok):
    if tok.startswith("@") or tok == "?":
        return tok
    return tok.replace("^", "+")


def join_text(text):
    out = []
    for row in text.splitlines():
        if not row.strip() or row.lstrip().startswith("#"):
            out.append(row)
            continue
        parts = []
        for part in re.split(r"(\[\[.*?\]\])", row):
            if part.startswith("[["):
                parts.append(part)
            else:
                parts.append(" ".join(join_token(t) for t in part.split()))
        out.append(" ".join(p for p in parts if p))
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("cipher")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    with open(a.cipher) as f:
        res = join_text(f.read())
    if a.out:
        with open(a.out, "w") as f:
            f.write(res)
    else:
        sys.stdout.write(res)


if __name__ == "__main__":
    main()

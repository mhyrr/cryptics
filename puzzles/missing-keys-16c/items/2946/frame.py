"""frame.py - the line frame for cipher readers, from the two plain readers of each page.

    python3 -I frame.py PAGE      -> prints one line per letter line: label, y, first clear word or 'signs'

y is the mean of the two readers' y (good to about 15 px). The landmark is the first clear word of the main hand
as reader 1 wrote it (the cipher readers see those words on the strip anyway); no gloss is passed on. Rows that
are only clear words (no [cipher]) in both readers are marked 'clear only'. Signature and address rows are dropped.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plain_compare import PAIRS, HERE

STOP = {"2947-694": 17, "2946-c215": 19}   # last letter line (the dateline); later rows are signature/address


def rows(path):
    out = {}
    for ln in open(path, encoding="utf-8"):
        m = re.match(r"(L\d+)\s+y=~?(\d+)\S*\s*\|\s*(.*)", ln.strip())
        if m:
            out[m.group(1)] = (int(m.group(2)), m.group(3))
    return out


def main(page):
    r1, r2 = PAIRS[page]
    a = rows(os.path.join(HERE, "readers", r1, page + ".txt"))
    b = rows(os.path.join(HERE, "readers", r2, page + ".txt"))
    keys = sorted(set(a) & set(b), key=lambda k: int(k[1:]))
    if page in STOP:
        keys = [k for k in keys if int(k[1:]) <= STOP[page]]
    for k in keys:
        y = round((a[k][0] + b[k][0]) / 2)
        t = re.sub(r"\{[^}]*\}", " ", a[k][1]).split()
        has = "[cipher]" in a[k][1] or "[cipher]" in b[k][1]
        first = t[0] if t else ""
        land = "starts with signs" if first == "[cipher]" else f"starts with the clear word '{first}'"
        if not has:
            land = f"clear words only ('{first}'); no signs expected"
        print(f"{k}\ty~{y}\t{land}")


if __name__ == "__main__":
    main(sys.argv[1])

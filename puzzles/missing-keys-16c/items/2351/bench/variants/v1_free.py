"""v1_free: ../tied.py as it stands, with an unmarked base treated as a sign of its own (tied.BARE_FREE).
The table of bases, marks and other signs is written out one row per sign of the cipher text: a sign with a
vowel mark gets consonant + vowel when both its base and its mark are marked; its status is the weaker one."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "..", "line"))
import align, tied  # noqa: E402

RANK = {"certain": 2, "probable": 1, "unknown": 0}
NAME = {v: k for k, v in RANK.items()}


def sign_rows(rows, mk, units):
    """tied rows (B:, M:, W:) -> one row per sign of the cipher text."""
    t = {r["unit"]: r for r in rows}
    count = {}
    for u in units:
        if u.kind == "sign" and u.sym != "?":
            count[u.sym] = count.get(u.sym, 0) + 1
    out = []
    for s, n in count.items():
        kind, a, b = tied.parts(s, mk)
        if kind == "BM":
            rb, rm = t.get("B:" + a), t.get("M:" + b)
            if not rb or not rm:
                continue
            value, st = rb["value"] + rm["value"], min(RANK[rb["status"]], RANK[rm["status"]])
            sup, con = min(rb["support"], rm["support"]), max(rb["conflict"], rm["conflict"])
        else:
            r = t.get(("B:" if kind == "B" else "W:") + a)
            if not r:
                continue
            value, st, sup, con = r["value"], RANK[r["status"]], r["support"], r["conflict"]
        out.append(dict(unit=s, value=value, type=align.unit_type(value), support=sup, conflict=con,
                        share=round(sup / max(1, sup + con), 3), status=NAME[st], alts=f"places {n}", positions=""))
    out.sort(key=lambda r: (-RANK[r["status"]], -r["support"], r["unit"]))
    return out


def build(cipher, plain, log):
    units, P, wb, lac, _ = align.load_pair(cipher, plain)
    old = tied.BARE_FREE[0]
    tied.BARE_FREE[0] = True
    try:
        rows, mk = tied.build(units, P, lac, log)
        st = {}
        for r in rows:
            if r["status"] != "unknown":
                st[r["unit"][0]] = st.get(r["unit"][0], 0) + 1
        log(f"entries marked by kind: {st}")
        return sign_rows(rows, mk, units)
    finally:
        tied.BARE_FREE[0] = old

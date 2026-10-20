"""Experiment 29: the one-table row-and-column transposition (Givierge 1925, Hitt 1916 "double transposition")
on complete rectangles, and the fixed rearrangement that turns it into experiment 18's sets-of-n problem.

Keys are rank arrays: ckey[c] is the reading rank of table column c, rkey[r] the reading rank of table row r.
A complete rectangle has w columns and h = len(text) / w rows; no filler, no preamble.

D1, write rows / read columns: plaintext p[r*w + c] sits in row r, column c. The cipher reads the columns in
    column-key order, each column's letters in row-key order.
    Rearrangement: cut the cipher into w chunks of h, read across. Gives h sets of n = w; each set is one plaintext
    row, permuted by the column key; sets in row-key order.
D2, write columns / read rows: plaintext p[c*h + r] sits in row r, column c. The cipher reads the rows in row-key
    order, each row's letters in column-key order.
    Rearrangement: every w-th letter. Gives w sets of n = h; each set is one block of h consecutive plaintext
    letters (one table column), permuted by the row key; sets in column-key order.

encrypt() builds the table explicitly and does not share code with rearrange(). Works on strings or lists.
Self-test: python3 -I rowcol.py (asserts against 28's check.py and 18's setsolve.py).
"""
import importlib.util, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIRECTIONS = ("D1", "D2")


def _join(seq, like):
    return "".join(seq) if isinstance(like, str) else list(seq)


def encrypt(pt, w, ckey, rkey, direction):
    L = len(pt); assert L % w == 0, "complete rectangles only"
    h = L // w; assert sorted(ckey) == list(range(w)) and sorted(rkey) == list(range(h))
    grid = [[None] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            grid[r][c] = pt[r * w + c] if direction == "D1" else pt[c * h + r]
    col_order = sorted(range(w), key=lambda c: ckey[c])
    row_order = sorted(range(h), key=lambda r: rkey[r])
    if direction == "D1":
        out = [grid[r][c] for c in col_order for r in row_order]
    else:
        out = [grid[r][c] for r in row_order for c in col_order]
    return _join(out, pt)


def set_size(L, w, direction):
    return w if direction == "D1" else L // w


def rearrange(ct, w, direction):
    """The fixed rearrangement: returns a text of sets of n, concatenated (18's layout at offset 0)."""
    L = len(ct); h = L // w; assert L % w == 0
    if direction == "D1":
        out = [ct[k * h + i] for i in range(h) for k in range(w)]
    else:
        out = [ct[j + i * w] for j in range(w) for i in range(h)]
    return _join(out, ct)


def unrearrange(rt, w, direction):
    L = len(rt); h = L // w
    out = [None] * L
    if direction == "D1":
        for i in range(h):
            for k in range(w):
                out[k * h + i] = rt[i * w + k]
    else:
        for j in range(w):
            for i in range(h):
                out[j + i * w] = rt[j * h + i]
    return _join(out, rt)


def true_order(ridx, n):
    """Plaintext order of rearranged columns, from the index map of the first set."""
    s = ridx[:n]; lo = min(s)
    return [s.index(lo + t) for t in range(n)]


def decrypt_with_keys(ct, w, ckey, rkey, direction):
    """Independent inverse of encrypt (used by verify29.py): rebuilds the table from the keys."""
    L = len(ct); h = L // w
    col_order = sorted(range(w), key=lambda c: ckey[c])
    row_order = sorted(range(h), key=lambda r: rkey[r])
    grid = [[None] * w for _ in range(h)]
    it = iter(ct)
    if direction == "D1":
        for c in col_order:
            for r in row_order:
                grid[r][c] = next(it)
        out = [grid[r][c] for r in range(h) for c in range(w)]
    else:
        for r in row_order:
            for c in col_order:
                grid[r][c] = next(it)
        out = [grid[r][c] for c in range(w) for r in range(h)]
    return _join(out, ct)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


def _selftest():
    c28 = _load("check28", os.path.join(HERE, "..", "28-historical-evidence", "check.py"))
    sys.path.insert(0, os.path.join(HERE, "..", "18-periodic-solver"))
    import setsolve
    rnd = random.Random("29-selftest")
    shapes = [(615, 15), (615, 41), (160, 8), (160, 10), (160, 16), (160, 20)]
    for trial in range(300):
        L, w = shapes[trial % len(shapes)]; h = L // w
        ckey = rnd.sample(range(w), w); rkey = rnd.sample(range(h), h)
        idx = list(range(L))
        a = encrypt(idx, w, ckey, rkey, "D1"); b = encrypt(idx, w, ckey, rkey, "D2")
        # same cipher as 28's independent simulation
        assert a == c28.rowcol_rows_then_columns(L, w, ckey, rkey)
        assert b == c28.rowcol_columns_then_rows(L, w, ckey, rkey)
        for d, x in (("D1", a), ("D2", b)):
            n = set_size(L, w, d)
            r = rearrange(x, w, d)
            assert unrearrange(r, w, d) == x
            sets = [r[i:i + n] for i in range(0, L, n)]
            assert c28.is_sets_family(sets), (L, w, d)
            # 28's regrouping gives the same sets
            g = c28.regroup_chunks(x, w, h) if d == "D1" else c28.regroup_residues(x, w, h)
            assert g == sets
            assert decrypt_with_keys(x, w, ckey, rkey, d) == idx
            # 18's machinery: the true order decrypts every set, adjacency 1
            o = true_order(r, n)
            assert setsolve.adjacency_acc(r, o, 0) == 1.0
    # on letters: the true order reads the plaintext back (D2 in order; D1 as a permutation of rows)
    pt = "".join(rnd.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(160))
    for w in (8, 10, 16, 20):
        h = 160 // w; ckey = rnd.sample(range(w), w); rkey = rnd.sample(range(h), h)
        for d in DIRECTIONS:
            n = set_size(160, w, d)
            ct = encrypt(pt, w, ckey, rkey, d)
            ridx = rearrange(encrypt(list(range(160)), w, ckey, rkey, d), w, d)
            rows = setsolve.dec_rows(rearrange(ct, w, d), true_order(ridx, n), 0)
            assert sorted(rows) == sorted(pt[i:i + n] for i in range(0, 160, n))
    # Givierge's printed example is a single columnar pass (h rows, identity row key, incomplete): not used here,
    # but 28 reproduces it; our D1 with identity row key on a complete table equals 28's columnar().
    pt = "LASIXIEMEDIVISIONPARTIRACESOIRXXXXXX"[:36]
    ck = c28.rank("MARSEILLE")
    assert encrypt(pt, 9, ck, list(range(4)), "D1") == c28.columnar(pt, ck)
    print("rowcol self-test passed")


if __name__ == "__main__":
    _selftest()

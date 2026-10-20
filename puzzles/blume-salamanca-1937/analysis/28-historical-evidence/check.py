"""Checks behind sources/historical-evidence/: no target decryption, no solver run.

1. Givierge (1925) keyword numbering and table transposition reproduce his printed cryptogram.
2. The one-table row-and-column transposition he calls "double transposition", on a complete rectangle,
   reduces after a fixed rearrangement to experiment 18's family (letters permuted within sets of n by
   one key, sets in any order), in both writing directions. Checked by simulation on plaintext indices.
3. Complete-rectangle shapes for T1 (615) and T2 (160), and which set sizes fall in 18's tested bands.
4. Overlap of HE-K01's contextual names with 24's phrase lists.
5. solver-options.jsonl parses, has unique ids and the required fields.
"""
import importlib.util
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIVE = HERE.parent.parent
OPTIONS = DIVE / "sources" / "historical-evidence" / "solver-options.jsonl"


def rank(s):
    # Ties left to right: the first occurrence gets the lower number.
    order = sorted(range(len(s)), key=lambda i: (s[i], i))
    key = [0] * len(s)
    for r, i in enumerate(order):
        key[i] = r
    return key


def columnar(text, key):
    w = len(key)
    cols = [text[c::w] for c in range(w)]
    return "".join(cols[c] for c in sorted(range(w), key=lambda c: key[c]))


def givierge():
    key = rank("MARSEILLE")
    plain = "LASIXIEMEDIVISIONPARTIRACESOIR"
    printed = "AIRIXSREPSIIAEOCMNELDAOSVTRIII"
    got = columnar(plain, key)
    return [k + 1 for k in key], got, got == printed


def rowcol_rows_then_columns(n, w, ckey, rkey):
    # Write by rows; read columns in column-key order, each column's rows in row-key order.
    h = n // w
    rows_order = sorted(range(h), key=lambda r: rkey[r])
    out = []
    for c in sorted(range(w), key=lambda c: ckey[c]):
        out += [r * w + c for r in rows_order]
    return out


def rowcol_columns_then_rows(n, w, ckey, rkey):
    # Write down the columns (column c holds plaintext c*h .. c*h+h-1), table columns in key order;
    # read by rows in row-key order.
    h = n // w
    cols_order = sorted(range(w), key=lambda c: ckey[c])
    out = []
    for r in sorted(range(h), key=lambda r: rkey[r]):
        out += [c * h + r for c in cols_order]
    return out


def regroup_chunks(cipher, w, h):
    # Cut into w chunks of h, read across: sets of w.
    return [[cipher[k * h + i] for k in range(w)] for i in range(h)]


def regroup_residues(cipher, w, h):
    # Take every w-th letter: sets of h.
    return [[cipher[j + i * w] for i in range(h)] for j in range(w)]


def is_sets_family(sets):
    # Each set is one contiguous plaintext block, permuted by the same within-set key.
    n = len(sets[0])
    pattern = None
    for s in sets:
        lo = min(s)
        if sorted(s) != list(range(lo, lo + n)) or lo % n:
            return False
        p = [x - lo for x in s]
        if pattern is None:
            pattern = p
        elif p != pattern:
            return False
    return True


def reduction_check(trials=200, seed="28-reduction"):
    rng = random.Random(seed)
    shapes = [(615, 15), (615, 41), (160, 8), (160, 10), (160, 16), (160, 20)]
    ok = {"rows_then_columns": 0, "columns_then_rows": 0}
    for _ in range(trials):
        n, w = rng.choice(shapes)
        h = n // w
        ckey = rng.sample(range(w), w)
        rkey = rng.sample(range(h), h)
        a = rowcol_rows_then_columns(n, w, ckey, rkey)
        b = rowcol_columns_then_rows(n, w, ckey, rkey)
        ok["rows_then_columns"] += is_sets_family(regroup_chunks(a, w, h))
        ok["columns_then_rows"] += is_sets_family(regroup_residues(b, w, h))
    return trials, ok


def shapes():
    out = {}
    for n, tested in ((615, (8, 50)), (160, (8, 15))):
        rows = []
        for w in range(2, n):
            if n % w == 0:
                h = n // w
                sizes = sorted({w, h})
                rows.append(dict(w=w, h=h, set_sizes_after_rearrangement=sizes,
                                 in_18_tested_band=[s for s in sizes if tested[0] <= s <= tested[1]]))
        out[n] = dict(tested_band_18=list(tested), shapes=rows)
    return out


def phrase_overlap():
    spec = importlib.util.spec_from_file_location("phrases24", DIVE / "analysis" / "24-phrase-seeded" / "phrases.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    listed = {mod.normalize(p) for p in mod.PEOPLE + mod.PLACES + mod.FIRMS + mod.TRADE}
    new = ["MORITZ VICTOR OSWALD", "MORITZ VIKTOR OSWALD", "BANCO GUIPUZCOANO", "MIRACONCHA",
           "VICTOR M OSWALD", "SAN SEBASTIAN", "VICTOR OSWALD"]
    return {p: {"normalized": mod.normalize(p), "length": len(mod.normalize(p)),
                "already_single_component": mod.normalize(p) in listed} for p in new}


REQUIRED = ["id", "rank", "evidence_type", "evidence_class", "solver_ready", "title", "raw_text",
            "source_locator", "source_tier", "original_read", "date", "connection_to_messages", "confidence",
            "computational_consequence", "derivation_preparation", "bounded_variants", "prior_search_overlap",
            "proposed_test", "negative_result_means", "fresh_controls_required"]


def validate_options():
    recs = [json.loads(line) for line in OPTIONS.read_text().splitlines() if line.strip()]
    ids = [r["id"] for r in recs]
    missing = {r["id"]: [k for k in REQUIRED if k not in r] for r in recs}
    return dict(records=len(recs), unique_ids=len(set(ids)) == len(ids),
                missing_fields={k: v for k, v in missing.items() if v},
                solver_ready=[r["id"] for r in recs if r["solver_ready"]],
                ranked=sorted((r["rank"], r["id"]) for r in recs if r["rank"] is not None))


def main():
    key, got, match = givierge()
    trials, ok = reduction_check()
    print("1. Givierge MARSEILLE key:", " ".join(map(str, key)))
    print("   cryptogram:", got, "matches printed:", match)
    print(f"2. Reduction to 18's sets family, {trials} random complete-rectangle keys:", json.dumps(ok))
    print("3. Complete-rectangle shapes:")
    print(json.dumps(shapes(), indent=1))
    print("4. HE-K01 overlap with 24's single-component lists:")
    print(json.dumps(phrase_overlap(), indent=1))
    print("5. solver-options.jsonl:", json.dumps(validate_options()))


if __name__ == "__main__":
    main()

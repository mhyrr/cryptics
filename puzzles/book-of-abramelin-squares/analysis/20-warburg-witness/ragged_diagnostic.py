#!/usr/bin/env python3
"""POST HOC, after scoring. Why are 132 of 251 items 'ragged', and can they be read?

score_checked.py's gate counts every printed position of a ragged item as not
agreed. This separates two causes: the print setting rows of unequal length
(format), and the two readers differing (legibility)."""
import collections, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
def load(n):
    return {(i["chapter"], i["number"]): [r.upper().replace("J", "I") for r in i["rows"]] for i in json.load(open(HERE / n))["items"]}
a, b = load("readings-A.json"), load("readings-B.json")
def regular(rows):
    return bool(rows) and len(rows[0]) >= 3 and len(rows) <= len(rows[0]) and all(len(r) == len(rows[0]) for r in rows)
c = collections.Counter()
for k in sorted(a):
    ra, rb = a[k], b[k]
    if regular(ra) and regular(rb) and len(ra[0]) == len(rb[0]):
        continue
    c["ragged_items"] += 1
    same_shape = [len(r) for r in ra] == [len(r) for r in rb]
    c["same_shape_in_both_readers"] += same_shape
    c["ragged_in_both_readers"] += (not regular(ra)) and (not regular(rb))
    if same_shape:
        for x, y in zip("".join(ra), "".join(rb)):
            c["positions_same_shape"] += 1
            c["positions_agreed"] += x == y and x.isalpha()
    else:
        c["positions_shape_differs"] += max(sum(map(len, ra)), sum(map(len, rb)))
    c["rows_printed_shorter_than_first"] += sum(len(r) < len(ra[0]) for r in ra[1:]) if ra else 0
out = dict(c)
out["agreement_on_same_shape_positions"] = round(c["positions_agreed"] / c["positions_same_shape"], 3)
(HERE / "ragged-diagnostic.json").write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps(out, indent=1))

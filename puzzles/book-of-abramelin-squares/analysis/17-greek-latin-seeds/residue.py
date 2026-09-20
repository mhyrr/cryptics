#!/usr/bin/env python3
"""Sort the top rows that experiment 12 left unmatched. See PROTOCOL.md."""
import collections, csv, json, pathlib, random, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "12-dictionary-index"))
import rows_in_dictionary as r12   # norm, near_index, is_near, cv_shuffle, load_vocab; not modified

DRAWS = 200
ORDER = ["hebrew_line", "greek", "latin"]


def load(name):
    v, where = set(), {}
    with open(HERE / name, encoding="utf8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            t = r12.norm(r["form"])
            if len(t) < 4:
                continue
            for x in {t, t.replace("F", "S")}:
                v.add(x)
                where.setdefault(x, f'{r["volume"]}:{r["scan"]} {r["headword_ocr"]} [{r["printed"]}]')
    return v, where


def main():
    rng = random.Random(20260920)
    heb = r12.load_vocab()
    squares = json.load(open(HERE.parents[1] / "sources" / "mathers-squares.json"))["squares"]
    tops = []
    for s in squares:
        rows = s["rows"]
        n = len(rows)
        if n < 4 or any(len(r) != n for r in rows) or "." in rows[0]:
            continue
        w = r12.norm(rows[0])
        if len(w) == n:
            tops.append((s["id"], w))
    matched = [(i, w) for i, w in tops if w in heb]
    residue = [(i, w) for i, w in tops if w not in heb]
    vocabs = {"hebrew_line": load("hebrew-line-vocab.tsv"), "greek": load("greek-vocab.tsv"), "latin": load("latin-vocab.tsv")}
    near = {k: r12.near_index(v[0]) for k, v in vocabs.items()}
    near["hebrew_adjacent"] = r12.near_index(heb)
    table = {}
    for k, (v, _) in vocabs.items():
        ex = sum(w in v for _, w in residue)
        nr = sum(r12.is_near(w, v, near[k]) for _, w in residue)
        ce = cn = 0.0
        for _, w in residue:
            for _ in range(DRAWS):
                x = r12.cv_shuffle(w, rng)
                ce += x in v
                cn += r12.is_near(x, v, near[k])
        table[k] = {"vocabulary": len(v), "exact": ex, "exact_control": round(ce / DRAWS, 2),
                    "near": nr, "near_control": round(cn / DRAWS, 2)}
    nr = sum(r12.is_near(w, heb, near["hebrew_adjacent"]) for _, w in residue)
    cn = sum(r12.is_near(r12.cv_shuffle(w, rng), heb, near["hebrew_adjacent"]) for _, w in residue for _ in range(DRAWS))
    table["hebrew_adjacent_near"] = {"vocabulary": len(heb), "near": nr, "near_control": round(cn / DRAWS, 2)}

    # one label per residue row, first tier that fires, fixed priority
    rows_out, counts = [], collections.Counter()
    for sid, w in residue:
        label, ev = "unexplained", None
        for k in ORDER:
            if w in vocabs[k][0]:
                label, ev = k + "_exact", vocabs[k][1][w]
                break
        else:
            if r12.is_near(w, heb, near["hebrew_adjacent"]):
                label = "hebrew_adjacent_near"
            elif r12.is_near(w, vocabs["greek"][0], near["greek"]):
                label = "greek_near"
        counts[label] += 1
        rows_out.append({"square": sid, "top_row": w, "label": label, "evidence": ev})
    out = {"top_rows_complete": len(tops), "matched_in_experiment_12_vocabulary": len(matched),
           "residue": len(residue), "per_vocabulary": table, "labels": dict(counts), "rows": rows_out}
    (HERE / "residue.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps({k: out[k] for k in out if k != "rows"}, indent=1))


if __name__ == "__main__":
    main()

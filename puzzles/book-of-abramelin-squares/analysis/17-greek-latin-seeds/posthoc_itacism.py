#!/usr/bin/env python3
"""POST HOC, written after residue.json was read. Not part of the frozen test.

The frozen run labelled OIKETIS (οἰκέτης) as a near match only. German
humanists around 1600 mostly read Greek in the Reuchlinian way, η and ει as I.
This run adds that one reading (η -> I, ει -> I) to the frozen scheme and
repeats the exact-match count and its control on the same 176 rows. The Greek
words are re-read from greek-vocab.tsv's `printed` column, so only first
occurrences of each frozen form are covered.
"""
import csv, json, pathlib, random, sys, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "12-dictionary-index"))
import rows_in_dictionary as r12
import romanize

vocab = {}
with open(HERE / "greek-vocab.tsv", encoding="utf8") as f:
    for r in csv.DictReader(f, delimiter="\t"):
        g = "".join(c for c in r["printed"] if c.isalpha())
        base, rough = romanize.letters(g)
        if not base:
            continue
        it = base.replace("ει", "ι").replace("η", "ι")
        if it == base:
            continue
        for v in romanize.variants(it):
            if rough:
                vocab.setdefault("H" + v, r["printed"])
            vocab.setdefault(r12.norm(v), r["printed"])
res = json.load(open(HERE / "residue.json"))
frozen = {x["top_row"] for x in res["rows"] if x["label"].endswith("exact")}
rows = [x["top_row"] for x in res["rows"]]
rng = random.Random(20260920)
hits = [(w, vocab[w]) for w in rows if w in vocab]
ctrl = sum(r12.cv_shuffle(w, rng) in vocab for w in rows for _ in range(200)) / 200
out = {"status": "post hoc", "added_forms": len(vocab), "exact": len(hits), "exact_control": round(ctrl, 2),
       "hits": [{"top_row": w, "greek": g, "already_labelled_exact": w in frozen} for w, g in hits]}
(HERE / "posthoc-itacism.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print(json.dumps(out, ensure_ascii=False, indent=1))

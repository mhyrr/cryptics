#!/usr/bin/env python3
"""Score the image readings. See PROTOCOL.md."""
import csv, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
A = HERE.parent
sys.path.insert(0, str(A / "12-dictionary-index"))
sys.path.insert(0, str(A / "14-caption-seed-test"))
import rows_in_dictionary as r12
import run as e14


def fs(w):
    return r12.norm(w).replace("F", "S")


def main():
    work = json.load(open(HERE / "worklist.json"))
    reads = {r["crop"]: r for r in json.load(open(HERE / "readings.json"))["readings"]}
    ocr = {}
    with open(A / "12-dictionary-index" / "entries.tsv", encoding="utf8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            ocr[(r["volume"], int(r["scan"]), r["headword_ocr"])] = {fs(t) for t in r["hebrew_adjacent"].split()}
    tops = {}
    for s in json.load(open(A.parent / "sources" / "mathers-squares.json"))["squares"]:
        rows = s["rows"]
        if len(rows) >= 4 and all(len(r) == len(rows) for r in rows) and "." not in rows[0]:
            tops.setdefault(int(s["id"].split("/")[0]), set()).add(e14.skeleton(r12.norm(rows[0])))
    hits, gap = [], []
    recall_n = recall_d = 0
    for w in work:
        rd = reads.get(w["crop"], {})
        words = [x for x in rd.get("transliterations", [])]
        if w["kind"] == "hit":
            ok = any(e14.skeleton(r12.norm(x)) == e14.skeleton(w["top_row"]) for x in words)
            hits.append({"chapter": w["chapter"], "top_row": w["top_row"], "german": w["german"], "scan": f'{w["volume"]}:{w["scan"]}',
                         "headword_ocr": w["headword_ocr"], "confirmed": ok, "image_reading": words, "entry_found": rd.get("entry_found")})
        else:
            have = ocr[(w["volume"], w["scan"], w["headword_ocr"])]
            missed = [x for x in words if fs(x) not in have]
            recall_d += len(words)
            recall_n += len(words) - len(missed)
            own = [x for x in missed if e14.skeleton(r12.norm(x)) in tops.get(w["chapter"], set())]
            other = sum(e14.skeleton(r12.norm(x)) in t for x in missed for ch, t in tops.items() if ch != w["chapter"])
            gap.append({"chapter": w["chapter"], "german": w["german"], "scan": f'{w["volume"]}:{w["scan"]}',
                        "headword_ocr": w["headword_ocr"], "entry_found": rd.get("entry_found"), "image_reading": words,
                        "missed_by_ocr": missed, "missed_words_matching_own_chapter_seed": own,
                        "missed_words_matching_other_chapter_seeds": other})
    rows_hit = {(h["chapter"], h["top_row"]) for h in hits}
    rows_ok = {(h["chapter"], h["top_row"]) for h in hits if h["confirmed"]}
    out = {"hit_rows_read": len(rows_hit), "hit_rows_confirmed": len(rows_ok),
           "hit_rows_not_confirmed": sorted(rows_hit - rows_ok),
           "gap_sample_entries": len(gap), "gap_entries_found_on_crop": sum(bool(g["entry_found"]) for g in gap),
           "image_transliterations": recall_d, "harvested_by_ocr": recall_n,
           "ocr_recall": round(recall_n / recall_d, 3) if recall_d else None,
           "new_own_chapter_seed_matches": sum(len(g["missed_words_matching_own_chapter_seed"]) for g in gap),
           "other_chapter_matches_per_chapter": round(sum(g["missed_words_matching_other_chapter_seeds"] for g in gap) / max(len(tops) - 1, 1), 3),
           "hits": hits, "gap_sample": gap}
    (HERE / "results.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k not in ("hits", "gap_sample")}, indent=1))


if __name__ == "__main__":
    main()

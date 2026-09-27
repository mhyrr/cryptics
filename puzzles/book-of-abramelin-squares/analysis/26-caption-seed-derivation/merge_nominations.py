#!/usr/bin/env python3
"""Merge the three raw nominator files into nominations.json without edits (union, tagged)."""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
keys = [it["key"] for ch in json.load(open(HERE / "nominator-input.json", encoding="utf8"))["chapters"] for it in ch["items"]]
raw = {x: json.load(open(HERE / "nominations-raw" / f"nominations-{x}.json", encoding="utf8")) for x in "ABC"}
merged = []
for k in keys:
    noms = []
    for x in "ABC":
        items = [it for it in raw[x]["items"] if it["key"] == k]
        assert len(items) == 1, (x, k, len(items))
        assert len(items[0]["nominations"]) <= 3, (x, k)
        for n in items[0]["nominations"]:
            noms.append({"german": n["german"], "renders": n.get("renders", ""), "reason": n.get("reason", ""), "nominator": x})
    merged.append({"key": k, "nominations": noms})
for x in "ABC":
    assert {it["key"] for it in raw[x]["items"]} == set(keys), x
data = {"nominators": {x: "fresh Opus agent, captions and headings only, isolated, 2026-09-27" for x in "ABC"},
        "note": "Union of nominations-raw/*.json without edits; each record tagged with its nominator.",
        "items": merged}
text = json.dumps(data, indent=1, ensure_ascii=False) + "\n"
if "--check" in sys.argv:
    assert (HERE / "nominations.json").read_text(encoding="utf8") == text
    print("nominations reproduce")
else:
    (HERE / "nominations.json").write_text(text, encoding="utf8")
    print(len(merged), "captions;", sum(len(m["nominations"]) for m in merged), "nominations;",
          sum(1 for m in merged if m["nominations"]), "with at least one;",
          len({n["german"].strip() for m in merged for n in m["nominations"]}), "distinct headwords")

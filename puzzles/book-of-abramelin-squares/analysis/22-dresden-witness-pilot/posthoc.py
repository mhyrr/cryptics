#!/usr/bin/env python3
"""Apply source-locator adjudication without editing either raw transcription."""
import argparse
import collections
import json

import score

HERE = score.HERE


def remap(a, b, mapping):
    """Reject omissions, duplicate reader uses and cross-page joins."""
    seen_a, seen_b, seen_locators = set(), set(), set()
    left, right, records = {}, {}, []
    for index, entry in enumerate(mapping, 1):
        page = entry["physical_page"]
        ka = (page, entry["reader_a_grid_index"])
        kb = (page, entry["reader_b_grid_index"])
        locator = entry["locator_id"]
        if ka not in a or kb not in b or ka in seen_a or kb in seen_b or locator in seen_locators:
            raise ValueError("Locator map is not one-to-one on the reader records")
        if any(type(entry[k]) is not int or entry[k] < 1 for k in ("chapter", "number")):
            raise ValueError("Adjudicated source identifiers must be explicit positive integers")
        seen_a.add(ka)
        seen_b.add(kb)
        seen_locators.add(locator)
        key = (page, index)
        for raw, target in ((a[ka], left), (b[kb], right)):
            target[key] = dict(raw, grid_index=index, chapter=entry["chapter"], number=entry["number"])
        records.append({"physical_page": page, "grid_index": index, "locator_id": locator,
                        "source_id": f"{entry['chapter']}/{entry['number']}",
                        "alignment_reason": entry["reason"], "reader_a": a[ka], "reader_b": b[kb]})
    if seen_a != set(a) or seen_b != set(b):
        raise ValueError("Locator map omits a reader record")
    return left, right, records


def cell_records(record):
    a, b = record["reader_a"]["rows"], record["reader_b"]["rows"]
    if not a or list(map(len, a)) != list(map(len, b)):
        return None
    cells = []
    for i, (ra, rb) in enumerate(zip(a, b), 1):
        for j, (x, y) in enumerate(zip(ra, rb), 1):
            u, v = x.replace("J", "I"), y.replace("J", "I")
            agreed = u == v and u != "?"
            cells.append({"row_group": i, "position": j, "reader_a": x, "reader_b": y,
                          "consensus": u if agreed else "?",
                          "status": "agreed_blank" if u == v == "." else
                          "agreed_letter" if agreed else "unknown" if "?" in (u, v) else "conflict"})
    return cells


def coverage(cells, mathers):
    """Report exact prediction coverage at square and TA-orbit levels."""
    groups = collections.defaultdict(list)
    for cell in cells:
        groups[cell["source_id"]].append(cell)
    output = []
    for sid, rows in sorted(groups.items()):
        n = len(mathers[sid])
        orbits = collections.defaultdict(list)
        for cell in rows:
            i, j = cell["row"] - 1, cell["column"] - 1
            key = min((i, j), (j, i), (n - 1 - i, n - 1 - j), (n - 1 - j, n - 1 - i))
            orbits[key].append(cell)
        models = {}
        for model in rows[0]["outcomes"]:
            models[model] = {"predicted_positions": sum(c["predictions"][model] is not None for c in rows),
                             "outcomes": dict(collections.Counter(c["outcomes"][model] for c in rows)),
                             "all_target_positions_correct": all(c["outcomes"][model] == "correct" for c in rows),
                             "target_orbits_all_correct": sum(all(c["outcomes"][model] == "correct" for c in cs) for cs in orbits.values())}
        output.append({"source_id": sid, "target_positions": len(rows), "target_TA_orbits": len(orbits),
                       "scope": "Frozen Mathers-blank targets only; class correctness is not letter recovery", "models": models})
    return output


def render_collation(records):
    lines = ["# Dresden N 111 — three-page reading packet", "",
             "Generated from the post hoc source alignment. Both readers used Sol.",
             "These are agreed transcriptions, not an adjudicated edition or model fills.",
             "`?` retains a reader conflict or unknown. Row lists preserve uneven lengths.",
             "Source identifiers are Dresden book IV chapter/item, not a Mathers mapping.", ""]
    for record in records:
        source = record["source_locator"]
        lines.extend([f"## {record['locator_id']} — IV.{record['source_id'].replace('/', '.')}", "",
                      f"PRIMARY — [source image, physical {record['physical_page']}, label {record['page_label']}]({record['source_url']}). "
                      f"Column {source['page_region']['column']}, {source['page_region']['vertical']}.", "",
                      f"Coordinate type: `{record['coordinate_kind']}`. "
                      f"Original reader indices: A {record['reader_a']['grid_index']}, B {record['reader_b']['grid_index']}.", ""])
        if record["cells"] is None:
            lines.extend(["Shapes differ; consult both raw records. No consensus coordinates.", ""])
            continue
        rows = collections.defaultdict(list)
        uncertain = []
        for cell in record["cells"]:
            rows[cell["row_group"]].append(cell["consensus"])
            if cell["status"] in ("conflict", "unknown"):
                uncertain.append(f"- Row group {cell['row_group']}, position {cell['position']}: A `{cell['reader_a']}`, B `{cell['reader_b']}`.")
        lines.extend(["```text", *(" ".join(row) for row in rows.values()), "```", ""])
        if uncertain:
            lines.extend([*uncertain, ""])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    alignment = json.loads((HERE / "alignment.json").read_text())
    for name, expected in alignment["input_sha256"].items():
        if score.sha(HERE / name) != expected:
            raise ValueError(f"Changed alignment input: {name}")
    freeze = json.loads((HERE / "freeze.json").read_text())
    for rel, expected in freeze["sha256"].items():
        if score.sha(score.ROOT / rel) != expected:
            raise ValueError(f"Changed frozen input: {rel}")
    manifest = json.loads((HERE / "image-manifest.json").read_text())
    sources = {im["physical_page"]: im for im in manifest["images"]}
    for source in sources.values():
        if score.sha(score.PUZZLE / "sources/cache/dresden-n111" / source["filename"]) != source["sha256"]:
            raise ValueError("Changed source image")
    a, b, records = remap(score.readers(HERE / "readings-A.json"), score.readers(HERE / "readings-B.json"), alignment["items"])
    locator_data = json.loads((HERE / "locator-audit.json").read_text())
    locators = {g["id"]: g for g in locator_data["grids"]}
    if len(locators) != len(records) or {r["locator_id"] for r in records} != set(locators):
        raise ValueError("Alignment does not cover the source-only locator inventory")
    grids, agreement, issues = score.consensus(a, b)
    for record in records:
        source = sources[record["physical_page"]]
        locator = locators[record["locator_id"]]
        if (record["physical_page"], record["source_id"]) != (locator["physical_page"], f"{locator['source_chapter']}/{locator['item_number']}"):
            raise ValueError("Alignment differs from source-only locator audit")
        record.update(witness="Mscr.Dresd.N.111", source_url=source["original_image"],
                      image_sha256=source["sha256"], page_label=source["page_label"],
                      source_locator=locator, cells=cell_records(record))
        rows = record["reader_a"]["rows"]
        record["coordinate_kind"] = "square_row_column" if record["cells"] is not None and all(len(r) == len(rows) for r in rows) else "row_group_position_only"
    by_key = {(r["physical_page"], r["grid_index"]): r for r in records}
    mathers = {s["id"]: [r.upper() for r in s["rows"]] for s in json.loads((score.PUZZLE / "sources/mathers-squares.json").read_text())["squares"]}
    p13 = {s["id"]: s["cells"] for s in json.loads((HERE.parent / "13-dehn-witness-test/predictions.json").read_text())["squares"]}
    p20 = {s["id"]: {(c["row"], c["column"]): c["letter_chapter"] for c in s["cells"]}
           for s in json.loads((HERE.parent / "20-warburg-witness/predictions.json").read_text())["squares"]}
    result = score.evaluate(grids, mathers, p13, p20)
    for key in ("aligned", "excluded", "cells"):
        for record in result[key]:
            record["locator_id"] = by_key[(record["physical_page"], record["grid_index"])]["locator_id"]
    interior = result["tally"].get("class_checkerboard|interior", {})
    result.update(agreement=agreement, reading_issues=issues,
                  evaluated_interior_cells=interior.get("correct", 0) + interior.get("wrong", 0),
                  coverage=coverage(result["cells"], mathers),
                  interpretation="Post hoc source-locator correction. No confirmatory A/B verdict, no letter repairs.",
                  independence="Historical ancestry and model-training exposure unknown; adjacent grids and their cells are not independent trials.",
                  alignment_sha256=score.sha(HERE / "alignment.json"))
    outputs = {"posthoc-results.json": result,
               "posthoc-collation.json": {"scope": "Post hoc source alignment; both raw readings retained; not a corrected edition", "grids": records}}
    for name, data in outputs.items():
        text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        if args.check:
            if (HERE / name).read_text() != text:
                raise ValueError(f"Does not reproduce: {name}")
        else:
            (HERE / name).write_text(text)
    markdown = render_collation(records)
    if args.check:
        if (HERE / "COLLATION.md").read_text() != markdown:
            raise ValueError("Does not reproduce: COLLATION.md")
    else:
        (HERE / "COLLATION.md").write_text(markdown)
    print("Post hoc collation reproduces" if args.check else json.dumps({k: result[k] for k in ("agreement", "aligned", "excluded", "tally", "evaluated_interior_cells")}, indent=2))


if __name__ == "__main__":
    main()

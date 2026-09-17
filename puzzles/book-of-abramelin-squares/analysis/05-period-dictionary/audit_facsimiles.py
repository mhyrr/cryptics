#!/usr/bin/env python3
"""Compare exposed, image-read Latin excerpts; never load or score a square."""

import argparse
import csv
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = HERE.parent.parent / "sources" / "period-dictionary"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(text):
    return text.replace("ſ", "s").translate(
        str.maketrans("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    )


def audit():
    # Check original bytes, including the supplied provenance table.
    manifest = SOURCES / "MANIFEST.sha256"
    for line in manifest.read_text().splitlines():
        digest, name = line.split(maxsplit=1)
        if sha256(SOURCES / name) != digest:
            raise ValueError(f"Source checksum mismatch: {name}")
    with (SOURCES / "SOURCES.tsv").open(newline="") as stream:
        sources = {row["filename"]: row for row in csv.DictReader(stream, delimiter="\t")}
    claims = json.loads((HERE / "claims.json").read_text())["records"]
    readings = json.loads((HERE / "facsimile-readings.json").read_text())["records"]
    if len({r["id"] for r in readings}) != len(readings):
        raise ValueError("Duplicate facsimile reading ID")
    by_id = {r["id"]: r for r in claims}
    if set(by_id) != {r["id"] for r in readings}:
        raise ValueError("Reading and quotation inventories differ")
    comparisons = []
    for reading in readings:
        claim = by_id[reading["id"]]
        source = sources[reading["image"]]
        word = reading["target_transliteration_raw"]
        operations = []
        for op in reading["layout_operations"]:
            # A single explicitly recorded line join; no general deletion rule.
            if (reading["id"] != "water" or op != {
                "operation": "join_printed_line_break", "from": "ma-\niim", "to": "maiim"
            } or word != op["from"]):
                raise ValueError("Unreviewed layout operation")
            word = op["to"]
            operations.append(op)
        normalized = normalize(word)
        comparisons.append({
            "id": reading["id"],
            "tier": "PRIMARY facsimile / CLAIMANT square quotation",
            "image": reading["image"],
            "image_sha256": sha256(SOURCES / reading["image"]),
            "viewer_url": source["viewer_url"],
            "viewer_page": source["viewer_page"],
            "signature": source["printed_page_or_signature"],
            "raw": reading["target_transliteration_raw"],
            "layout_operations": operations,
            "layout_joined": word,
            "normalized": normalized,
            "quoted_dictionary_spelling": claim["reported_dictionary_spelling"],
            "dictionary_quote_agrees": normalized == normalize(claim["reported_dictionary_spelling"]),
            "quoted_square_spelling": claim["edition_square_spelling"],
            "quoted_square_agrees": normalized == normalize(claim["edition_square_spelling"]),
            "discovery_exposed": True,
        })
    paths = [HERE / name for name in [
        "facsimile-readings.json", "claims.json", "audit_facsimiles.py"
    ]] + [manifest, SOURCES / "SOURCES.tsv"]
    return {
        "scope": "Exposed facsimile spelling audit; NOT a reconstruction evaluation",
        "historical_score": None,
        "independent_lexicon": False,
        "input_sha256": {str(p.relative_to(HERE.parent.parent)): sha256(p) for p in paths},
        "comparisons": comparisons,
        "counts": {
            "readings": len(comparisons),
            "dictionary_quotes_agree": sum(r["dictionary_quote_agrees"] for r in comparisons),
            "quoted_square_spellings_agree": sum(r["quoted_square_agrees"] for r in comparisons),
        },
        "limits": [
            "Checks saved transcription consistency, not visual reading correctness.",
            "All targets were selected from known claimant correspondences.",
            "Hebrew ambiguity and the edition-specific error claim remain unresolved.",
            "No square positions, unseen letters, or independent witnesses scored.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    output = json.dumps(audit(), ensure_ascii=False, indent=2) + "\n"
    path = HERE / "facsimile-audit.json"
    if args.check:
        if not path.exists() or path.read_text() != output:
            raise SystemExit("Facsimile audit differs; inspect changes before regenerating")
        print("Facsimile audit and source checksums verified")
    else:
        path.write_text(output)
        print(output)

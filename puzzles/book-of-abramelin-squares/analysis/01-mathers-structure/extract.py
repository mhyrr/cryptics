#!/usr/bin/env python3
"""Parse the pinned web-tool row export, without repairing the digital witness."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "sources/mathers-web-rows.txt"
URL = "https://www.esotericarchives.com/abramelin/abramelin.htm"
MARKER = re.compile(r"(?<!\S)(\d+)\\(\d+)(\*|\^\{\d+\})?(?=\s)")


def extract(text):
    squares = []
    for line in text.splitlines():
        prefix = re.fullmatch(r"L(\d+): (.*)", line)
        if not prefix:
            raise ValueError(f"Malformed snapshot line: {line!r}")
        line_number, contents = prefix.groups()
        markers = list(MARKER.finditer(contents))
        if not markers or markers[0].start() != 0:
            raise ValueError(f"Missing square identifier: {line!r}")
        for i, marker in enumerate(markers):
            end = markers[i + 1].start() if i + 1 < len(markers) else len(contents)
            raw = contents[marker.end():end].strip()
            rows = [s.strip() for s in raw.split(",")]
            sid = f"{marker[1]}/{marker[2]}"
            square = {"id": sid, "source_url": URL,
                      "web_export_line": int(line_number), "source_marker": marker[0],
                      "raw_rows": raw, "rows": rows, "grid": None}
            if sid == "25/4":
                square["note"] = "Source labels this 25/4 within chapter 24; retain label pending facsimile audit."
            if not all(re.fullmatch(r"[A-Z.]+", row) for row in rows):
                square["exclude_reason"] = "Non-A–Z/dot content or missing row delimiter; inspect layout."
            elif len(rows) < 2 or any(len(row) != len(rows) for row in rows):
                square["exclude_reason"] = f"Ragged: {len(rows)} rows with lengths {[len(row) for row in rows]}; no padding."
            else:
                square["grid"] = [[None if cell == "." else cell for cell in row] for row in rows]
            squares.append(square)
    if len({s["id"] for s in squares}) != len(squares):
        raise ValueError("Duplicate identifiers in snapshot")
    return squares


def main():
    raw = SOURCE.read_bytes()
    squares = extract(raw.decode())
    corpus = {"source_url": URL, "accessed": "2026-09-16",
              "transmission": "Peterson digital Mathers, web-tool row export; not collated against 1898 print",
              "source_sha256": hashlib.sha256(raw).hexdigest(),
              "normalization": "Trim delimiter whitespace; dot -> null. No letter, case, numbering or shape repairs.",
              "squares": squares}
    destination = ROOT / "sources/mathers-squares.json"
    destination.write_text(json.dumps(corpus, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"records": len(squares),
                      "by_source_chapter": dict(sorted(Counter(int(s["id"].split("/")[0]) for s in squares).items())),
                      "excluded": [{"id": s["id"], "reason": s["exclude_reason"]} for s in squares if "exclude_reason" in s]}, indent=2))


if __name__ == "__main__":
    main()

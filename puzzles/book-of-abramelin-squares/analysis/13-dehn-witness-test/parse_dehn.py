#!/usr/bin/env python3
"""Extract Peterson's `D:` square readings from the cached Mathers HTML.

A reading is attached to the square whose `chapter\\number` marker is the last
one printed before the note in the same table row. Rows are split on commas;
no letter is repaired. Footnote readings are quoted and often end with
"Compare Mathers c\\n" or "= Mathers c\\n"; that explicit reference then names
the square, because Dehn's order differs from Mathers's. Notes that are not comma lists of capital words (for
example caption-order notes) are kept in `other_notes` untouched.
"""
import hashlib, html, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parents[1] / "sources" / "cache" / "e2" / "mathers.html"


def main():
    raw = SRC.read_bytes()
    t = raw.decode("utf8", errors="replace")
    squares, other = [], []
    for tr in re.split(r"(?i)<TR>", t):
        ids = re.findall(r"(?<![\d\\])(\d{1,2})\\(\d{1,2})(?!\d)", tr)
        for m in re.finditer(r"(?s)\bD:\s*(.*?)(?=</TD>|<P>|<BR>|\bD:|$)", tr):
            body = html.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))
            body = re.sub(r"\s+", " ", body).strip()
            quoted = re.match(r'"([A-Z, .]+?)\.?"', body)
            explicit = re.search(r"Mathers (\d{1,2})\\(\d{1,2})", body)
            listing = quoted.group(1) if quoted else body
            rows = [r.strip() for r in listing.rstrip(".").split(",")]
            if len(rows) >= 3 and all(re.fullmatch(r"[A-Z.?\[\]]{2,}", r) for r in rows):
                target = "/".join(explicit.groups()) if explicit else ("/".join(ids[0]) if ids else None)
                squares.append({"id": target, "id_basis": "explicit Mathers reference" if explicit else "marker in the same table row",
                                "peterson_comment": body[quoted.end():].strip() if quoted else "",
                                "ids_in_row": ["/".join(i) for i in ids],
                                "raw": body, "rows": rows})
            else:
                other.append({"ids_in_row": ["/".join(i) for i in ids], "raw": body[:400]})
    doc = {"source": "sources/cache/e2/mathers.html", "source_sha256": hashlib.sha256(raw).hexdigest(),
           "source_url": "https://www.esotericarchives.com/abramelin/abramelin.htm",
           "tier": "edited PRIMARY at two removes: German MSS > Dehn edition > Peterson notes",
           "squares": squares, "other_notes": other}
    (HERE / "dehn-readings.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print(len(squares), "square readings;", len(other), "other D notes")
    print("without id:", [s["raw"][:40] for s in squares if not s["id"]])
    print("multi-id rows:", [(s["ids_in_row"]) for s in squares if len(s["ids_in_row"]) > 1][:10])


if __name__ == "__main__":
    main()

"""taken.py - which catalogue ids already have a target folder in Bourdeau's repository.

    python3 taken.py <profiles.json> > taken.tsv
Input: a JSON map {path: text of targets/<name>/profile.json}, fetched from the public repository
(recipe in sources/PROVENANCE.md). The catalogue file does not record work in progress; the target
folders do. An id counts as taken when a profile names it as "catalogue N", "catalogue no. N",
"lead N" or in a "catalogue"/"catalogue_id" field. Output: id, target, first 100 characters of the title.
"""
import json, re, sys


def ids_in(text):
    found = set()
    for m in re.finditer(r"(?i)\b(?:catalogue|catalog|lead)s?\s*(?:entry|entries|no\.?|nos\.?|id|#)?\s*((?:\d{1,4})(?:\s*(?:,|and|&|/|-)\s*\d{1,4})*)", text):
        found.update(int(x) for x in re.findall(r"\d{1,4}", m.group(1)))
    for m in re.finditer(r'"catalogue(?:_ids?|_entry)?"\s*:\s*(\[[^\]]*\]|"?\d+"?)', text):
        found.update(int(x) for x in re.findall(r"\d+", m.group(1)))
    return found


def main(path):
    profiles = json.load(open(path, encoding="utf-8"))
    rows = []
    for p, text in sorted(profiles.items()):
        name = p.split("/")[1]
        try:
            title = json.loads(text).get("title", "")
        except Exception:
            title = ""
        for i in sorted(ids_in(text)):
            rows.append((i, name, title[:100].replace("\t", " ")))
    print("id\ttarget\ttitle")
    for r in sorted(rows):
        print("\t".join(map(str, r)))
    print(f"# {len(profiles)} profiles, {len({r[0] for r in rows})} catalogue ids named", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1])

#!/usr/bin/env python3
"""Extract the spirit-name lists of Book II chapter 19 from the cached Peterson HTML.

Two sources, kept apart:
  mathers  the running text (Mathers's translation of the French manuscript)
  dehn     Peterson's `D:` notes inside the same chapter (Dehn's German-based lists)
A list runs from "be:" or "viz. :" to the "(= N spirits" count in the running
text. Names are split on full stops and commas. Nothing is respelled.
"""
import hashlib, html, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parents[1] / "sources" / "cache" / "e2" / "mathers.html"


def plain(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def names(s):
    return [w for w in re.split(r"[.,;]\s*", s) if re.fullmatch(r"[A-Z][a-z]{2,}", w.strip()) for w in [w.strip()]]


def main():
    raw = SRC.read_bytes()
    t = re.sub(r"(?s)<!--.*?-->", "", raw.decode("utf8", errors="replace"))
    i = t.find("Gosegas")
    start, end = t.rfind("<H3", 0, i), t.find("<H3", i)
    seg = t[start:end]
    notes = re.findall(r'(?s)<TD CLASS="NOTE">(.*?)</TD>', seg)
    body = plain(re.sub(r'(?s)<TD CLASS="NOTE">.*?</TD>', " ", seg))
    lists = []
    for m in re.finditer(r"(?s)((?:The|These|the)[^:]{0,160}?)(?:be|viz\.)\s*:\s*(.*?)\(=\s*(\d+)", body):
        lists.append({"source": "mathers", "heading": m.group(1).strip()[-120:], "stated_count": int(m.group(3)),
                      "names": names(re.sub(r"\s\d+\s", " ", m.group(2)))})
    for n in notes:
        for m in re.finditer(r"(?s)\bD:\s*(.*?)(?=\bD:|$)", plain(n)):
            ns = names(m.group(1))
            if len(ns) >= 5:
                lists.append({"source": "dehn", "heading": "", "stated_count": None, "names": ns})
    doc = {"source_sha256": hashlib.sha256(raw).hexdigest(), "lists": lists}
    (HERE / "spirit-names.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    for l in lists:
        print(l["source"], l["stated_count"], len(l["names"]), "|", l["heading"][-60:], "|", " ".join(l["names"][:6]))


if __name__ == "__main__":
    main()

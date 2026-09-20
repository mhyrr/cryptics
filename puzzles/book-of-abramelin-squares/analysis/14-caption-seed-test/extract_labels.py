#!/usr/bin/env python3
"""Extract Mathers's numbered English purpose labels for Book III chapters 1-30.

Reads only the numbered `(n) text` lists and chapter headings from the cached
Peterson HTML. It does not read square rows or notes. Output: labels.json.
"""
import hashlib, html, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parents[1] / "sources" / "cache" / "e2" / "mathers.html"


def text(s):
    s = re.sub(r"(?s)<SUP>.*?</SUP>", "", s)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def main():
    raw = SRC.read_bytes()
    t = re.sub(r"(?s)<!--.*?-->", "", raw.decode("utf8", errors="replace"))
    marks = [(m.start(), int(m.group(1))) for m in re.finditer(r'<A NAME="b3chap(\d+)">', t)]
    out = []
    for k, (pos, ch) in enumerate(marks):
        end = marks[k + 1][0] if k + 1 < len(marks) else len(t)
        seg = t[pos:end]
        head = re.search(r"(?s)</H3>\s*(?:<P>)?(.*?)</TD>", seg)
        first_square = re.search(r"\d{1,2}\\\d{1,2} ", seg)
        lst = seg[: first_square.start()] if first_square else seg
        lst = re.sub(r'(?s)<TD CLASS="NOTE">.*?</TD>', "", lst)
        labels = []
        for nums, b in re.findall(r"(?s)\((\d{1,2}(?:\s*,\s*\d{1,2})*)\)\s*(.*?)(?=<BR>|\(\d{1,2}[,)]|</TD>)", lst):
            for n in re.findall(r"\d+", nums):   # "(2, 3) text" labels both squares
                labels.append({"number": int(n), "label": text(b)})
        if not labels:                            # chapter 14 has a heading and no list
            labels = [{"number": 0, "label": text(head.group(1)) if head else ""}]
        out.append({"chapter": ch, "heading": text(head.group(1)) if head else "", "labels": labels})
    doc = {"source_sha256": hashlib.sha256(raw).hexdigest(), "chapters": out}
    (HERE / "labels.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print(len(out), "chapters;", sum(len(c["labels"]) for c in out), "labels")
    for c in out:
        print(c["chapter"], len(c["labels"]), "|", c["heading"][:70], "|", "; ".join(l["label"] for l in c["labels"][:3])[:110])


if __name__ == "__main__":
    main()

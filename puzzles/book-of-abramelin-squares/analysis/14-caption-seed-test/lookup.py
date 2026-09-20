#!/usr/bin/env python3
"""Bounded German headword lookup against the local OCR index (experiment 12).

Every operation is listed in PROTOCOL.md with its reason. The same key function
is applied to the nominated word and to the OCR headword. Nothing here touches
a Hebrew transliteration: those are returned as the OCR printed them.
"""
import csv, pathlib, re, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ENTRIES = HERE.parent / "12-dictionary-index" / "entries.tsv"
FRAME_HEADS = ("gestalt",)          # caption frame, not the entity: "in Adlersgestalt"
LINKS = ("s", "en", "n", "")        # linking elements tried in this order


def key(word):
    w = unicodedata.normalize("NFKD", word.lower().replace("ſ", "s").replace("ß", "ss"))
    w = "".join(c for c in w if c.isalpha() or c == " ")
    w = w.replace("sch", "$").replace("ch", "#")
    for a, b in (("th", "t"), ("ck", "k"), ("tz", "z"), ("dt", "t"), ("v", "u"), ("w", "u"), ("j", "i"), ("y", "i"),
                 ("c", "k"), ("eu", "ei"), ("ai", "ei"), ("ue", "u"), ("ae", "a"), ("oe", "o")):
        w = w.replace(a, b)
    w = re.sub(r"([a-z$#])\1+", r"\1", w)           # doubled letters: Mann / man, Reitter / Reiter
    w = " ".join(p[:-1] if len(p) > 3 and p.endswith("e") else p for p in w.split())   # Blum / Blume
    return w


def strip_frame(word):
    """Adlersgestalt -> candidate modifiers [Adler, Adlers...]; others -> []."""
    low = word.lower().replace("ſ", "s")
    for head in FRAME_HEADS:
        if low.endswith(head) and len(low) > len(head) + 2:
            stem = word[: len(word) - len(head)]
            out = []
            for link in LINKS:
                if link == "" or stem.lower().endswith(link):
                    cand = stem[: len(stem) - len(link)] if link else stem
                    if len(cand) >= 3 and cand not in out:
                        out.append(cand)
            return out
    return []


def within_one(a, b):
    if a == b:
        return True
    if abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) == 1
    if len(a) > len(b):
        a, b = b, a
    return any(a == b[:i] + b[i + 1:] for i in range(len(b)))


class Index:
    def __init__(self, path=ENTRIES):
        self.rows = []
        self.by_key = {}
        with open(path, encoding="utf8") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                segs = [s.strip(" .,:;") for s in re.split(r"[/|]", r["headword_ocr"])]
                r["keys"] = {key(s) for s in segs if s} | {key(r["headword_ocr"])}
                self.rows.append(r)
                for k in r["keys"]:
                    self.by_key.setdefault(k, []).append(r)

    def find(self, nomination):
        """Return (tier, entries). Tiers: exact_key, frame_stripped, ocr_tolerant, none."""
        k = key(nomination)
        if k in self.by_key:
            return "exact_key", self.by_key[k]
        for cand in strip_frame(nomination):
            if key(cand) in self.by_key:
                return "frame_stripped", self.by_key[key(cand)]
        if len(k) >= 5:
            near = [r for kk, rs in self.by_key.items() if len(kk) >= 5 and within_one(k, kk) for r in rs]
            if near:
                return "ocr_tolerant", near
        return "none", []


if __name__ == "__main__":
    import sys
    ix = Index()
    for w in sys.argv[1:]:
        tier, es = ix.find(w)
        print(w, "->", tier)
        for e in es[:8]:
            print("   ", e["volume"], e["scan"], repr(e["headword_ocr"]), "|", e["hebrew_adjacent"])

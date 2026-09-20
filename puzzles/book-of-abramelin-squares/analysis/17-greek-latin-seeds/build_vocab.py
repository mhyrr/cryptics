#!/usr/bin/env python3
"""Extend experiment 12's index with the Greek and Latin columns of the dictionary.

Imports experiment 12's build_index.py for page parsing and entry detection;
that file is not modified and no second parser exists. Three vocabularies are
written, each as `form <tab> volume <tab> scan <tab> headword_ocr <tab> printed`
with the first locator only:

  greek-vocab.tsv        romanized Greek-script words (romanize.py, frozen)
  latin-vocab.tsv        Latin-script words of entry bodies, 4 to 12 letters
  hebrew-line-vocab.tsv  Latin-script words on a line that carries Hebrew type,
                         or on the line after it (a wider net than experiment
                         12's adjacent-word harvest)
Needs out/hocr of experiment 12 (fetch_hocr.py fetch).
"""
import csv, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "12-dictionary-index"))
import build_index as b12
from romanize import variants


def main():
    grk, lat, hebl = {}, {}, {}
    n_grk_tokens = 0
    for vol in sorted(p.name for p in b12.HOCR.iterdir() if p.is_dir()):
        for p in sorted((b12.HOCR / vol).glob("*.hocr")):
            scan = int(p.stem)
            lines = b12.parse_page(p.read_text(encoding="utf8", errors="replace"))
            for e in b12.entries_of(lines):
                prev_heb = False
                for L in e["lines"]:
                    toks = [w[4] for w in L["toks"]]
                    has_heb = any(b12.script(t) == "heb" for t in toks)
                    for t in toks:
                        s = b12.script(t)
                        if s == "grk":
                            n_grk_tokens += 1
                            for v in variants("".join(c for c in t if c.isalpha())):
                                if 4 <= len(v) <= 12:
                                    grk.setdefault(v, (vol, scan, e["head"], t))
                        elif s == "lat":
                            c = b12.clean(t).replace("-", "")
                            if 4 <= len(c) <= 12:
                                lat.setdefault(c.lower(), (vol, scan, e["head"], t))
                                if has_heb or prev_heb:
                                    hebl.setdefault(c.lower(), (vol, scan, e["head"], t))
                    prev_heb = has_heb
    for name, d in (("greek-vocab.tsv", grk), ("latin-vocab.tsv", lat), ("hebrew-line-vocab.tsv", hebl)):
        with open(HERE / name, "w", newline="", encoding="utf8") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            w.writerow(["form", "volume", "scan", "headword_ocr", "printed"])
            for k in sorted(d):
                w.writerow([k, *d[k]])
    print("greek tokens", n_grk_tokens, "romanized forms", len(grk), "latin forms", len(lat), "hebrew-line forms", len(hebl))


if __name__ == "__main__":
    main()

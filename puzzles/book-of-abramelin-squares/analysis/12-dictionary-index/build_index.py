#!/usr/bin/env python3
"""Turn the downloaded hOCR into a local entry index for both dictionary volumes.

Output (checked in):
  entries.tsv   one row per detected German headword line:
                volume, scan, column, y, headword_ocr, body_start_ocr,
                hebrew_adjacent (Latin-script tokens printed next to Hebrew type)
  tokens.tsv    every Hebrew-adjacent token with its locator (volume, scan, headword)

Everything here is OCR. It is a locator and a statistical vocabulary, never a
reading. A transliteration that a result depends on is read from the page image.

Method
  1. Words come from ocrx_word boxes. The column gutter is the x position in the
     middle 30 % of the page crossed by the fewest word boxes.
  2. Inside a column, words are regrouped into lines by vertical overlap, then
     sorted left to right. This undoes OCR lines that run across both columns.
  3. A headword line is indented on both sides by at least 8 % of the column
     width, has at most six words, is not the POETICE rubric, and is not the
     line directly under a POETICE rubric (that line repeats the Latin lemma).
  4. An entry runs to the next headword line in the same column order.
  5. A Hebrew-adjacent token is the Latin-script word nearest to the LEFT or
     RIGHT of a Hebrew-script word on the same line, or the first word of the
     next line when the Hebrew word ends its line. Hyphenated line ends are joined.
     The whole entry is searched: Greek often precedes the Hebrew gloss.
"""
import csv, html, pathlib, re, sys, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
HOCR = HERE / "out" / "hocr"
WORD = re.compile(r'class="ocrx_word" title="bbox (\d+) (\d+) (\d+) (\d+)[^"]*">([^<]*)<')
PAGE = re.compile(r'class="ocr_page" title="[^"]*bbox 0 0 (\d+) (\d+)')
GREEK_MARK = re.compile(r"^Gr[æeęaœ]{1,2}c?i?$", re.I)


def script(tok):
    for ch in tok:
        if "֐" <= ch <= "׿" or "יִ" <= ch <= "ﭏ":
            return "heb"
        if "Ͱ" <= ch <= "Ͽ" or "ἀ" <= ch <= "῿":
            return "grk"
    return "lat" if any(c.isalpha() for c in tok) else "pun"


def words_of(text):
    out = []
    for x0, y0, x1, y1, w in WORD.findall(text):
        w = html.unescape(w).strip()
        if w:
            out.append((int(x0), int(y0), int(x1), int(y1), w))
    return out


def gutter(words, width):
    lo, hi = int(width * 0.35), int(width * 0.65)
    cover = [0] * (hi - lo)
    for x0, _, x1, _, _ in words:
        for x in range(max(x0, lo), min(x1, hi)):
            cover[x - lo] += 1
    best = min(cover) if cover else 0
    xs = [i for i, c in enumerate(cover) if c == best]
    return lo + xs[len(xs) // 2] if xs else width // 2


def lines_of(words):
    """Cluster words into lines by vertical centre; return lines top to bottom."""
    words = sorted(words, key=lambda w: (w[1] + w[3]) / 2)
    lines = []
    for w in words:
        yc = (w[1] + w[3]) / 2
        if lines and abs(lines[-1]["yc"] - yc) < 0.55 * (w[3] - w[1] or 30) and True:
            L = lines[-1]
            L["w"].append(w)
            L["yc"] = sum((a[1] + a[3]) / 2 for a in L["w"]) / len(L["w"])
        else:
            lines.append({"yc": yc, "w": [w]})
    for L in lines:
        L["w"].sort(key=lambda a: a[0])
    return lines


def clean(tok):
    return "".join(c for c in tok if c.isalpha() or c in "-ſ")


def parse_page(text):
    m = PAGE.search(text)
    width = int(m.group(1)) if m else 1328
    ws = words_of(text)
    if not ws:
        return []
    g = gutter(ws, width)
    cols = [[w for w in ws if (w[0] + w[2]) / 2 < g], [w for w in ws if (w[0] + w[2]) / 2 >= g]]
    out = []
    for ci, cw in enumerate(cols):
        if not cw:
            continue
        body = [w for w in cw if w[2] - w[0] > 0]
        left = sorted(w[0] for w in body)[len(body) // 20]
        right = sorted(w[2] for w in body)[-1 - len(body) // 20]
        span = max(right - left, 1)
        lines = lines_of(cw)
        prev_poetice = False
        for L in lines:
            toks = [w[4] for w in L["w"]]
            txt = " ".join(toks)
            x0, x1 = L["w"][0][0], L["w"][-1][2]
            is_poet = re.sub(r"[^A-Za-z]", "", txt).upper().startswith("POET")
            centred = (x0 - left) > 0.08 * span and (right - x1) > 0.08 * span
            nalpha = [t for t in toks if script(t) == "lat"]
            head = (centred and not is_poet and not prev_poetice and 1 <= len(nalpha) <= 6
                    and all(script(t) in ("lat", "pun") for t in toks))
            out.append({"col": ci, "y": int(L["yc"]), "toks": L["w"], "text": txt, "head": head})
            prev_poetice = is_poet
    return out


def entries_of(lines):
    cur = None
    for L in lines:
        if L["head"]:
            if cur:
                yield cur
            cur = {"head": L["text"], "col": L["col"], "y": L["y"], "lines": []}
        elif cur:
            cur["lines"].append(L)
    if cur:
        yield cur


def harvest(entry):
    """Latin-script words printed next to Hebrew type, anywhere in the entry."""
    flat = [(li, w[4]) for li, L in enumerate(entry["lines"]) for w in L["toks"]]
    joined, i = [], 0
    while i < len(flat):                      # join hyphenated line ends
        li, t = flat[i]
        if t.endswith("-") and len(t) > 1 and i + 1 < len(flat) and flat[i + 1][0] != li and script(t) == "lat":
            joined.append(t[:-1] + flat[i + 1][1])
            i += 2
        else:
            joined.append(t)
            i += 1
    adj = []
    for k, t in enumerate(joined):
        if script(t) == "heb":
            for d in (1, 2, -1):              # next word, the one after a stray point, previous word
                j = k + d
                if 0 <= j < len(joined) and script(joined[j]) == "lat" and len(clean(joined[j])) >= 3:
                    adj.append(clean(joined[j]))
                    break
    return adj


def main():
    rows, toks = [], []
    for vol in sorted(p.name for p in HOCR.iterdir() if p.is_dir()):
        for p in sorted((HOCR / vol).glob("*.hocr")):
            scan = int(p.stem)
            lines = parse_page(p.read_text(encoding="utf8", errors="replace"))
            for e in entries_of(lines):
                adj = harvest(e)
                body = " ".join(L["text"] for L in e["lines"][:6])[:300]
                rows.append([vol, scan, e["col"], e["y"], e["head"], body, " ".join(adj)])
                for a in adj:
                    toks.append([vol, scan, e["head"], a])
    with open(HERE / "entries.tsv", "w", newline="", encoding="utf8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["volume", "scan", "column", "y", "headword_ocr", "body_start_ocr", "hebrew_adjacent"])
        w.writerows(rows)
    with open(HERE / "tokens.tsv", "w", newline="", encoding="utf8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["volume", "scan", "headword_ocr", "token"])
        w.writerows(toks)
    print(len(rows), "entries;", len(toks), "hebrew-adjacent tokens;", len({t[3].lower() for t in toks}), "distinct")


if __name__ == "__main__":
    main()

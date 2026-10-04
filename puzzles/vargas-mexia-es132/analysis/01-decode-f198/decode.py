"""Apply Tomokiyo's Cipher 4 key to a reader's transcription of es. 132 ff. 198–199.

Frozen 2026-10-03 before either transcription was opened. Standard library only.
    python3 decode.py ../../sources/transcription/reader-A/f198.txt > out_A.txt
Output: per line, clear text in [[ ]] kept as is, cipher decoded; unknown tokens as ⟨tok⟩;
every interpretive decision is listed in a FLAGS section with line:token position.
"""
import re, sys

BASE = {12: "a", 11: "b", 10: "c", 9: "d", 8: "e", 7: "f", 6: "g", 5: "h", 4: "i", 3: "l",
        2: "m", 1: "n", 23: "o", 22: "p", 21: "q", 20: "r", 19: "s", 18: "t", 17: "u",
        16: "x", 15: "y", 14: "z"}
LETTER_SIGNS = {"y": "a", "d": "d", "o": "o", "v": "o", "a": "u"}           # bare consonant/letter
CLUSTERS = {"B": "bl", "C": "cl", "f": "fr", "g": "gr", "p": "pr", "t": "tr",
            "F": "fl", "G": "gl", "P": "pl", "b": "br", "c": "cr"}               # F G P b c: conjectures
CONJECTURE = set("FGPbc")
CODES = {"vo": "[V.Magd]", "co": "[carta]"}
VOWEL = {".": "a", "+": "e", "_": "i", "^": "u"}
NULLS = {"<hat>", "<v>"}

MARK_RE = re.compile(r"(<[^>]+>|[.+_^])")


def split_token(tok):
    """core, list of marks, uncertain flag."""
    unc = tok.endswith("?")
    tok = tok.rstrip("?")
    m = re.match(r"^(<sign:[^>]*>|[0-9]+|[A-Za-z]+)(.*)$", tok)
    if not m:
        return tok, [], unc
    core, rest = m.group(1), m.group(2)
    marks = MARK_RE.findall(rest)
    leftover = MARK_RE.sub("", rest)
    if leftover:
        marks.append(f"<?{leftover}>")
    return core, marks, unc


def parse_digits(s):
    """Digit run -> list of (base, o_vowel) units. Rules, in order (frozen):
    R1 whole value 1..23 and not ending in 6 with a valid prefix -> one base.
    R2 ends in '6' and prefix is 1..23 -> base(prefix) + vowel o   (so '16' = 'no', not 'x').
    R3 bare '6' -> g.  R4 otherwise split left-to-right into units (2-digit base 10..23 first,
       then 1-digit), each optionally followed by '6' as vowel o; returns None if impossible."""
    if s == "6":
        return [(6, False)], "R3"
    if len(s) >= 2 and s.endswith("6") and int(s[:-1]) in BASE:
        return [(int(s[:-1]), True)], "R2"
    if int(s) in BASE:
        return [(int(s), False)], "R1"
    units, i = [], 0
    while i < len(s):
        for w in (2, 1):
            part = s[i:i + w]
            if len(part) == w and part[0] != "0" and int(part) in BASE and (w == 1 or int(part) >= 10):
                o = s[i + w:i + w + 1] == "6" and not (1 <= int(s[i + w:i + w + 2] or "0") <= 23 and len(s[i + w:i + w + 2]) == 2 and i + w + 2 == len(s))
                units.append((int(part), o))
                i += w + (1 if o else 0)
                break
        else:
            return None, "R4-fail"
    return units, "R4"


def decode_line(line, lno, flags):
    out = []
    pos = 0
    for chunk in re.split(r"(\[\[.*?\]\])", line):
        if chunk.startswith("[["):
            out.append(chunk)
            continue
        for tok in chunk.split():
            pos += 1
            where = f"{lno}:{pos}"
            core, marks, unc = split_token(tok)
            if unc:
                flags.append(f"{where} uncertain reading '{tok}'")
            if any(m in NULLS for m in marks):
                flags.append(f"{where} null mark on '{tok}' (caret/hacek: null per Tomokiyo; Devos: doubling)")
                out.append("·")
                continue
            vowels = [VOWEL[m] for m in marks if m in VOWEL]
            others = [m for m in marks if m not in VOWEL and m not in NULLS]
            if others:
                flags.append(f"{where} unclassified mark(s) {others} on '{tok}'")
            if len(vowels) > 1:
                flags.append(f"{where} several vowel marks {marks} on '{tok}'; first used")
            v = vowels[0] if vowels else ""
            if core in CODES:
                out.append(CODES[core]); continue
            if core.isdigit():
                units, rule = parse_digits(core)
                if units is None:
                    flags.append(f"{where} unparseable digits '{core}'")
                    out.append(f"⟨{tok}⟩"); continue
                if rule in ("R2", "R4") or len(units) > 1:
                    flags.append(f"{where} {rule} parse of '{core}' -> {units}")
                s = ""
                for k, (b, o) in enumerate(units):
                    s += BASE[b] + ("o" if o else "")
                if v:
                    if units[-1][1]:
                        flags.append(f"{where} vowel mark on a '6'-voweled unit '{tok}'")
                    s += v
                out.append(s); continue
            if core in CLUSTERS:
                if core in CONJECTURE:
                    flags.append(f"{where} conjectural cluster '{core}'")
                out.append(CLUSTERS[core] + v); continue
            if core in LETTER_SIGNS:
                if core == "o":
                    flags.append(f"{where} bare 'o': letter o (not code 'hu')")
                out.append(LETTER_SIGNS[core] + v); continue
            flags.append(f"{where} unknown sign '{tok}'")
            out.append(f"⟨{tok}⟩")
    return " ".join(out)


def main(path):
    flags, n_cipher = [], 0
    for lno, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        if line.startswith("#"):
            print(line); continue
        print(f"{lno:3d}  {decode_line(line, lno, flags)}")
    print("\n## FLAGS")
    for f in flags:
        print(f)


if __name__ == "__main__":
    main(sys.argv[1])

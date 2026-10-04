"""Cipher 3 (Devos Cp.30, per Tomokiyo) decoder, v2: reads the notation of
../../sources/transcription/CIPHER3-GUIDE.md. Frozen 2026-10-04 before any v2 transcription exists.
    python3 decode_c3_v2.py <transcription> [--tsv] > out.txt
Rules (key: ../../sources/keys/cipher3.tsv; extensions: c3_extensions.tsv):
- Bases: numbers 2..37 per Cp.30 row 1/row 2 and clusters; letter forms per Cp.30 rows 2-3.
  35 is "pl" in Cp.30 and "pr" in Tomokiyo's Borgia table: output "p(l|r)" and flag.
  1, 5 and 0 have no value in Cp.30: output ⟨n⟩ and flag.
- Marks after: '+' a, '.' e, 'p' (hook) o, '<tbar>' u, a joined final '6' (curl) i.
- Marks above: <acute> l, <grave> m, <hat> n, <v> r, <bar> s, <2dot> doubles the base consonant,
  <cross> marks a code word (value from c3_extensions.tsv or ⟨#…⟩), <dot> unknown (flagged).
- Digit runs (frozen order): R1 whole value is a key number -> one base (flag if it ends in 6, since
  N+curl is possible). R2 ends in 6 and the prefix is a key number -> prefix + curl (i). R3 otherwise:
  split into key numbers (2-digit 10..37 before 1-digit) with a final 6 read as curl; fewest units
  wins; ties go to the left-greedy split. Every R2/R3 parse is flagged. No parse -> code ⟨#n⟩.
- Extensions in c3_extensions.tsv match whole tokens first; output in UPPER CASE.
"""
import re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
L = {10: "a", 8: "b", 7: "c", 6: "d", 4: "e", 2: "f", 11: "g", 12: "h", 13: "i", 15: "l", 16: "m",
     17: "n", 18: "o", 20: "p", 21: "q", 22: "r", 23: "s", 24: "t", 25: "u", 27: "x", 28: "y", 29: "z",
     9: "a", 3: "e", 14: "i", 19: "o", 26: "u",
     30: "br", 31: "cr", 32: "dr", 33: "fr", 34: "gr", 35: "p(l|r)", 36: "tr", 37: "vr"}
UNVALUED = {0, 1, 5}
LETTER_FORMS = {c: c for c in "bcdfghmnpqrstxyz"} | {"L": "l", "S": "s", "T": "ch",
                "a": "a", "e": "e", "i": "i", "o": "o", "u": "u"}
AFTER = {"+": "a", ".": "e", "p": "o", "<tbar>": "u"}
ABOVE = {"<acute>": "l", "<grave>": "m", "<hat>": "n", "<v>": "r", "<bar>": "s"}
ALIAS = {"<crossabove>": "<cross>", "<cross above>": "<cross>"}


def load_ext():
    ext = {}
    p = HERE / "c3_extensions.tsv"
    if p.exists():
        for row in p.read_text(encoding="utf-8").splitlines()[1:]:
            if row.strip() and not row.startswith("#"):
                tok, val = row.split("\t")[:2]
                ext[tok] = val
    return ext


def parse_digits(s):
    """-> (list of base numbers, curl_i flag, rule) or (None, False, 'none')."""
    v = int(s)
    if v in L or v in UNVALUED:
        return [v], False, "R1"
    if len(s) >= 2 and s.endswith("6") and int(s[:-1]) in L:
        return [int(s[:-1])], True, "R2"
    best = None
    def rec(i, acc):
        nonlocal best
        if i == len(s):
            cand = (acc, False)
        elif s[i:] == "6" and acc:
            cand = (acc, True)
        else:
            cand = None
        if cand:
            if best is None or len(cand[0]) < len(best[0]):
                best = cand
            return
        for w in (2, 1):
            part = s[i:i + w]
            if len(part) == w and part[0] != "0" and (int(part) in L or int(part) in UNVALUED) \
                    and (w == 1 or int(part) >= 10):
                rec(i + w, acc + [int(part)])
    rec(0, [])
    if best is None:
        return None, False, "none"
    return best[0], best[1], "R3"


def tok(t0, ext, flags, where):
    t = t0
    for a, b in ALIAS.items():
        t = t.replace(a, b)
    unc = t.endswith("?")
    t = t.rstrip("?")
    if "|" in t:
        flags.append(f"{where} alternative reading '{t0}': first used")
        t = t.split("|")[0]
    if unc:
        flags.append(f"{where} uncertain '{t0}'")
    if t in ext:
        return ext[t].upper()
    if t in ("/", ","):
        return t
    m = re.match(r"^(\d+|[A-Za-z])((?:[+.p]|<[^>]+>)*)$", t)
    if not m:
        flags.append(f"{where} unparsed token '{t0}'")
        return f"⟨{t0}⟩"
    core, rest = m.group(1), m.group(2)
    marks = re.findall(r"<[^>]+>|[+.p]", rest)
    curl = False
    if core.isdigit():
        units, curl, rule = parse_digits(core)
        if units is None:
            flags.append(f"{where} no parse '{core}': code")
            base = f"⟨#{core}⟩"
        else:
            if rule == "R1" and core.endswith("6") and len(core) > 1:
                flags.append(f"{where} R1 '{core}' (could be {core[:-1]}+curl)")
            if rule in ("R2", "R3"):
                flags.append(f"{where} {rule} '{core}' -> {units}{' +curl' if curl else ''}")
            parts = []
            for u in units:
                if u in UNVALUED:
                    flags.append(f"{where} unvalued number {u} in '{t0}'")
                    parts.append(f"⟨{u}⟩")
                else:
                    if u == 35:
                        flags.append(f"{where} 35: pl (Cp.30) or pr (Borgia)")
                    parts.append(L[u])
            base = "".join(parts)
    else:
        if core not in LETTER_FORMS:
            flags.append(f"{where} unknown letter form '{core}'")
            return f"⟨{t0}⟩"
        base = LETTER_FORMS[core]
    vowel, cons, code = "i" if curl else "", "", False
    for mk in marks:
        if mk in AFTER:
            if vowel:
                flags.append(f"{where} second vowel mark '{mk}' in '{t0}'")
            vowel += AFTER[mk]
        elif mk in ABOVE:
            cons += ABOVE[mk]
        elif mk == "<2dot>":
            base = base + base[-1] if base and base[-1].isalpha() else base
        elif mk == "<cross>":
            code = True
        else:
            flags.append(f"{where} unhandled mark '{mk}' in '{t0}'")
    if code:
        flags.append(f"{where} code word '{t0}'")
        return f"⟨#{core}{''.join(m for m in marks if m != '<cross>')}⟩"
    return base + vowel + cons


def main(path, tsv=False):
    ext, flags = load_ext(), []
    for lno, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        if line.startswith("#"):
            print(line); continue
        out = []
        for chunk in re.split(r"(\[\[.*?\]\])", line):
            if chunk.startswith("[["):
                out.append(chunk); continue
            for i, t in enumerate(chunk.split(), 1):
                d = tok(t, ext, flags, f"{lno}:{len(out) + 1}")
                out.append(d)
                if tsv:
                    print(f"TOK\t{lno}\t{t}\t{d}", file=sys.stderr)
        print(f"{lno:3d}  {' '.join(out)}")
    print("\n## FLAGS")
    print("\n".join(flags))


if __name__ == "__main__":
    main(sys.argv[1], "--tsv" in sys.argv)

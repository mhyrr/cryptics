"""check_notation.py - test that the notation of SIGN-GUIDE.md parses with line/align.py, and count what the guide names.

    python3 check_notation.py

Run from this directory. Reads SIGN-GUIDE.md: the names in the tables of sections 3 and 4, and the worked example
(the fenced block tagged `cipher`). Checks:
  1. every base name is one unit under align.split_token, and has no forbidden character;
  2. base^mark splits into base and '^mark'; two marks into three units; '?' and 'a|b' set the doubt flag;
  3. the worked example parses, every base and mark in it is named in the guide, and '[[...]]' gives clear units;
  4. units.py joins base and marks into one unit, and leaves clear words, doubt and row count alone;
  5. the sheet cells in signsheet.py use only names from the guide, and the guide's sheet references are in range.
Prints the counts used in the item README and the report.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "line"))
sys.path.insert(0, HERE)
import align, units, signsheet  # noqa: E402

guide = open(os.path.join(HERE, "SIGN-GUIDE.md")).read()


def section(start, end):
    a = guide.index(start)
    return guide[a:guide.index(end, a)]


def names(block):
    return re.findall(r"^\| `([^`]+)` \|", block, re.M)


groups = {
    "letter forms": names(section("### 3a.", "### 3b.")),
    "changed letter forms": names(section("### 3b.", "### 3c.")),
    "figures": names(section("### 3c.", "### 3d.")),
    "invented marks": names(section("### 3d.", "### 3e.")),
}
bases = [n for g in groups.values() for n in g]
marks = names(section("## 4. Marks above", "## 5. Notation"))
assert len(set(bases)) == len(bases), "duplicate base name"
assert all(m.startswith("^") for m in marks)

# 1
for b in bases:
    assert re.fullmatch(r"[A-Za-z0-9]+", b), b
    assert align.split_token(b) == ([b], False), b
# 2
for b in bases:
    for m in marks:
        assert align.split_token(b + m) == ([b, m], False), b + m
assert align.split_token("y^o^wave") == (["y", "^o", "^wave"], False)
assert align.split_token("sigma?") == (["sigma"], True)
assert align.split_token("a^o?") == (["a", "^o"], True)
assert align.split_token("q|qbar") == (["q"], True)
assert align.split_token("?") == (["?"], True)
# 3
ex = re.search(r"```cipher\n(.*?)```", guide, re.S).group(1)
one_line = " ".join(ex.split("\n")).strip()
us, anchors, nlines = align.parse_cipher("# page V140-1r\n" + one_line + "\n")
assert nlines == 1 and not anchors
signs = [u for u in us if u.kind == "sign"]
clear = [u for u in us if u.kind == "clear"]
for u in signs:
    assert u.sym in bases or u.sym in marks, u.sym
tokens = len({u.tok for u in signs})
# 4
joined = units.join_text("# page x\n[[Bn vale]] a^o b y^o^wave? q|qbar^o ?\n")
assert joined == "# page x\n[[Bn vale]] a+o b y+o+wave? q|qbar+o ?\n", joined
ju, _, jl = align.parse_cipher(units.join_text("# page V140-1r\n" + one_line + "\n"))
assert jl == 1 and len([u for u in ju if u.kind == "sign"]) == tokens
assert align.split_token("a+o") == (["a+o"], False)
# 5
for name, _, _ in signsheet.CELLS:
    for part in align.split_token(name)[0]:
        assert part in bases or part in marks, name
per = signsheet.COLS * signsheet.ROWS
nsheets = -(-len(signsheet.CELLS) // per)
for s, r, c in re.findall(r"\b(\d)\.(\d)\.(\d)\b", guide):
    assert 1 <= int(s) <= nsheets and 1 <= int(r) <= signsheet.ROWS and 1 <= int(c) <= signsheet.COLS, (s, r, c)
for b, cells in re.findall(r"^\| `([^`]+)` \|[^|]*\| ([^|]*) \|", guide, re.M):
    for s, r, c in re.findall(r"\b(\d)\.(\d)\.(\d)\b", cells):
        cell = signsheet.CELLS[(int(s) - 1) * per + (int(r) - 1) * signsheet.COLS + int(c) - 1][0]
        assert b in align.split_token(cell)[0], (b, cell)

print("all notation checks pass")
for g, v in groups.items():
    print("%s\t%d" % (g, len(v)))
print("base shapes named\t%d" % len(bases))
print("marks above named\t%d" % len(marks))
print("sheet cells\t%d on %d sheets" % (len(signsheet.CELLS), nsheets))
print("worked example\t%d sign tokens, %d sign units as written, %d clear words" % (tokens, len(signs), len(clear)))

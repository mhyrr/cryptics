"""Convert Tomokiyo's partial transcription of f. 11r–12r (Cryptiana spanish3D.htm, Shift-JIS) to our notation.
His marks: '.' underdot (-i), '^' overdot (-o), '・' dot at the right (-u), 'e' hook (-a), '+' (-e), '~' overbar.
Ours (CIPHER2-GUIDE.md): '_' dot below, '^' dot above, '.' dot at the right, 'e', '+', '<bar>'.
Free ρ -> <rho>; ♀ -> <venus>; 〓 -> <sign:geta>. Lines of clear text become [[...]]; '**' (his line cut) is dropped.
    python3 convert_tomokiyo.py > tomokiyo_f11.txt
"""
import re, html
from pathlib import Path
SRC = Path(__file__).resolve().parents[2] / "sources" / "cache" / "cryptiana" / "spanish3D.htm"
t = SRC.read_bytes().decode("shift_jis", errors="replace")
t = re.sub(r"<script.*?</script>", "", t, flags=re.S)
t = re.sub(r"<br\s*/?>", "\n", t)
t = re.sub(r"<[^>]+>", " ", t)
t = html.unescape(t)
a = t.find("null?", t.find("Partial Transcription")) + 5
seg = t[a:t.find("Use of Duplicates", a)]
# Clear words the regex misses (short or with an apostrophe), and his truncated "d" of the clear "do":
FIX = [("me [[haparecido", "[[me haparecido"), ("[[yassi]] lo [[sera queros por]] V'ra [[parte]]",
        "[[yassi lo sera queros por V'ra parte]]"), ("Re y [[delo", "Re [[y delo"), ("14 pe d", "14 pe")]
CLEAR = re.compile(r"[a-z]{3,}")
print("# Tomokiyo's partial transcription of f. 11r-12r (Cipher 2), converted to CIPHER2-GUIDE notation.")
print("# Source: cryptiana.web.fc2.com/code/spanish3D.htm (cached). Page markers kept as comments.")
for raw in seg.splitlines():
    line = raw.replace("**", "").strip()
    if not line or line == "..":
        continue
    if line.startswith("(f."):
        print("# " + line); continue
    out = []
    for tok in line.split():
        if CLEAR.fullmatch(re.sub(r"[.']", "", tok)) and tok not in ("pe",):
            out.append(f"[[{tok}]]"); continue
        if tok == "...":
            continue
        tok = tok.replace("ρ", "<rho>").replace("♀", "<venus>").replace("〓", "<sign:geta>")
        m = re.match(r"^(<[^>]+>|\d+|[A-Za-z])(.*)$", tok)
        if not m:
            out.append(tok); continue
        b, rest = m.groups()
        rest = rest.replace(".", "_").replace("・", ".").replace("~", "<bar>")
        # a free <rho> glued after a sign ("12.ρ", "R+ρ") is a separate sign in his text
        rest = rest.replace("<rho>", " <rho>")
        out.append(b + rest)
    line = " ".join(out)
    for a, b in FIX:
        line = line.replace(a, b)
    print(re.sub(r"\]\] \[\[", " ", line))

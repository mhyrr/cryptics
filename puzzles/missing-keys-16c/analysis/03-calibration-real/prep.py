"""Make the real calibration pair from es. 132 f. 255 and Teulet's print of the Simancas minute.

    python3 prep.py   -> cipher.txt, plain.txt, truth.tsv
Cipher: ../../../vargas-mexia-es132/sources/transcription/f255/transcription.txt (one blind reader, guide v2.2),
text rows 11-34: from the row that begins the Scottish matter to the row that ends in the virgula
after "liviandad". The rows were chosen with the known decode (07-after-arrest/f255_dec.txt); in a real item the
extent of a pair is seen on the page.
Notation: es. 132 tokens are rewritten in the line's notation. Digit runs are split by the es. 132 decoder's
frozen rule (numbers run 1-37; a joined final 6 is the curl mark), which is a rule about shapes.
Plain: Teulet, Relations politiques, vol. 5 (1862), pp. 213-214, as transcribed in
../../../vargas-mexia-es132/analysis/07-after-arrest/teulet_check.py (three consecutive passages).
Truth: Cp.30 as the es. 132 decoder holds it (cipher3.tsv; 35 = pr).
"""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ES = HERE.parent.parent.parent / "vargas-mexia-es132"
sys.path.insert(0, str(ES / "analysis" / "04-cipher3"))
sys.path.insert(0, str(ES / "analysis" / "07-after-arrest"))
sys.argv = sys.argv[:1]
import decode_c3_v2 as c3  # noqa: E402

AFTER = {"+": "plus", ".": "dot", "p": "hook", "<tbar>": "tbar"}
FIRST, LAST = 11, 34


def convert(tok):
    q = "?" if tok.endswith("?") else ""
    t = tok.rstrip("?").split("|")[0]
    if t in ("/", ","):
        return [t]
    if t.startswith("<sign:") or not t:
        return ["?"]
    m = re.match(r"^(\d+|[A-Za-z])((?:[+.p]|<[^>]+>)*)$", t)
    if not m:
        return ["?"]
    core, marks = m.group(1), re.findall(r"<[^>]+>|[+.p]", m.group(2))
    bases, curl = [core], False
    if core.isdigit():
        units, curl, _ = c3.parse_digits(core)
        if units is None:
            bases = [core]
        else:
            bases = [str(u) for u in units]
    after = "curl" if curl else ""
    above = []
    for mk in marks:
        if mk in AFTER:
            after = after or AFTER[mk]
        else:
            above.append(re.sub(r"[^a-z0-9]", "", mk.lower()) or "mark")
    last = bases[-1] + (":" + after if after else "") + "".join("^" + a for a in above) + q
    return bases[:-1] + [last]


def main():
    rows = [r for r in (ES / "sources/transcription/f255/transcription.txt").read_text(encoding="utf-8").splitlines()
            if r.strip() and not r.startswith("#")]
    out = ["# es. 132 f. 255, text rows %d-%d, rewritten by prep.py" % (FIRST, LAST)]
    for r in rows[FIRST - 1:LAST]:
        toks = []
        for part in re.split(r"(\[\[.*?\]\]|<sign:[^>]*>\??)", r):
            if part.startswith("[["):
                toks.append(part)
            elif part.startswith("<sign:"):
                toks.append("?")
            else:
                for t in part.split():
                    toks += convert(t)
        out.append(" ".join(toks))
    (HERE / "cipher.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    src = (ES / "analysis/07-after-arrest/teulet_check.py").read_text(encoding="utf-8")
    ns = {}
    exec(src[src.index("PASSAGES = {"):src.index("for path in")], ns)
    (HERE / "plain.txt").write_text("\n".join(ns["PASSAGES"][k] for k in ("t213", "t213b", "t214")) + "\n",
                                    encoding="utf-8")
    truth = {str(k): v for k, v in c3.L.items()}
    truth["35"] = "pr"
    truth.update({k: v for k, v in c3.LETTER_FORMS.items()})
    truth.update({":plus": "a", ":dot": "e", ":hook": "o", ":tbar": "u", ":curl": "i",
                  "^acute": "l", "^grave": "m", "^hat": "n", "^v": "r", "^bar": "s", "/": "", ",": ""})
    truth = {k: v.replace("v", "u").replace("j", "i") for k, v in truth.items()}
    (HERE / "truth.tsv").write_text("".join(f"{k}\t{v}\n" for k, v in sorted(truth.items())), encoding="utf-8")
    print(f"{LAST - FIRST + 1} cipher rows")


if __name__ == "__main__":
    main()

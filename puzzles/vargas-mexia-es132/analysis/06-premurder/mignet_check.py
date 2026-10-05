"""External check: do the printed passages of the 8 Mar 1578 letter (Mignet 1846 app. E, from the Simancas minute
B.47 n. 47) appear in our decode of f. 17-25? Scores the share of each passage's letters found, in order, in the decoded
text (character-level alignment after normalising spelling: v/u, y/i, z/ç/c, ss/s, h dropped, qu/q, doubled letters,
spaces and brackets removed). A passage that is in the letter scores high; Spanish that is not scores ~0.3–0.5 (control:
the same passages against the f. 11 decode).
    python3 mignet_check.py <decoded.txt> [<decoded2.txt> ...]
"""
import re, sys, difflib

PASSAGES = {
    "p437n2": "Muy bien haveis hecho en avisarme de lo que el duque de Guisa havia comunicado",
    "p437n2b": "y seria muy conveniente tener grangeados al dicho duque y a los de Guisa, y mantener los en mi devocion por "
               "los mejores medios que se pudiere. Y assy os ancargo que vos lo procureys por vuestra parte, tratandolo "
               "con la dissimulacion y cordura que vos sabreis",
    "p439n5": "Ha sido bien advertirme",
    "p439n5b": "sobre lo de los casamientos del rey de Escocia con la hija de Lorrena, y de mi hermano con la de Escocia. "
               "Y aunque estas cosas deven de ser por via de discurso y de poco fundamento, todavia es conveniente tener "
               "noticia de lo que se dize y discurre en semejantes materias",
}


def norm(s):
    s = s.lower()
    s = re.sub(r"\[\[|\]\]", "", s)
    s = re.sub(r"\[[^\]]*\]", "#", s)          # unknown sign -> one wildcard char that never matches
    s = re.sub(r"[^a-zñç#]", "", s)
    for a, b in (("qu", "q"), ("v", "u"), ("y", "i"), ("z", "c"), ("ç", "c"), ("h", ""), ("ñ", "n")):
        s = s.replace(a, b)
    return re.sub(r"(.)\1+", r"\1", s)


def decoded_text(path):
    out = []
    for line in open(path, encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        out.append(re.sub(r"^\s*\d+\s{2}", "", line.rstrip("\n")))
    return norm(" ".join(out))


def best(passage, text):
    """Best in-order match of the passage inside a window of the text about its length."""
    p = norm(passage); n = len(p); top = (0, 0)
    sm = difflib.SequenceMatcher(None, p, text, autojunk=False)
    # seed windows at the longest blocks, then score each window
    seeds = sorted(sm.get_matching_blocks(), key=lambda b: -b.size)[:12]
    for b in seeds:
        start = max(0, b.b - b.a - n // 4); win = text[start:start + n + n // 2]
        m = difflib.SequenceMatcher(None, p, win, autojunk=False)
        k = sum(x.size for x in m.get_matching_blocks())
        top = max(top, (k, start))
    return top[0] / n, top[1]


def main(paths):
    for path in paths:
        text = decoded_text(path)
        print(f"# {path} ({len(text)} normalised letters)")
        for k, v in PASSAGES.items():
            r, at = best(v, text)
            print(f"{k:8s} {r:.0%}  at char {at}")


if __name__ == "__main__":
    main(sys.argv[1:])

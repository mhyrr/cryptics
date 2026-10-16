"""Period telegraph-style plaintext from held-out books (never from the model's training books).

Telegraphese transform (a proxy, stated so it can be argued with): words normalised as in lm.py;
articles and QUE dropped with probability 0.7; PUNTO inserted at sentence ends; with probability
0.03 per word a spelled quantity (e.g. QUINIENTOSKILOS, MILPESETAS) is inserted. Bourdeau's
letter counts suggest exactly this kind of text (too few Q, L, U, A; extra P, T).
"""
import json, os, random, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lm import normalise, strip_gutenberg, EXCLUDE

DROP = {"es": {"EL", "LA", "LOS", "LAS", "LO", "UN", "UNA", "UNOS", "UNAS", "QUE"},
        "it": {"IL", "LO", "LA", "I", "GLI", "LE", "UN", "UNO", "UNA", "CHE"},
        "pt": {"O", "A", "OS", "AS", "UM", "UMA", "QUE"}}
STOP = {"es": "PUNTO", "it": "STOP", "pt": "PONTO"}
QTY = {"es": ["CIEN", "MIL", "DOSCIENTOS", "QUINIENTOS", "TRES", "CINCO", "DIEZ", "VEINTE", "TREINTA"],
       "it": ["CENTO", "MILLE", "DUECENTO", "CINQUECENTO", "TRE", "CINQUE", "DIECI", "VENTI"],
       "pt": ["CEM", "MIL", "DUZENTOS", "QUINHENTOS", "TRES", "CINCO", "DEZ", "VINTE"]}
UNIT = {"es": ["KILOS", "PESETAS", "FRANCOS", "TONELADAS"], "it": ["CHILI", "LIRE", "FRANCHI"], "pt": ["QUILOS", "ESCUDOS", "FRANCOS"]}

_cache = {}
def heldout_words(lang):
    if lang not in _cache:
        man = json.load(open("corpus_manifest.json"))
        toks = []
        for b in man[lang]:
            if b["split"] != "heldout" or b["id"] in EXCLUDE:
                continue
            raw = strip_gutenberg(open(f"out/raw_{lang}/{b['id']}.txt", encoding="utf-8", errors="replace").read())
            for tok in re.findall(r"[^\W\d_]+|[.!?;]", raw):
                toks.append("." if tok in ".!?;" else normalise(tok, lang))
        _cache[lang] = [t for t in toks if t]
    return _cache[lang]

def telegram(n, rnd, lang="es", style="telegraph"):
    w = heldout_words(lang)
    i = rnd.randrange(len(w) - 5000)
    out = []
    while sum(map(len, out)) < n:
        t = w[i]; i += 1
        if t == ".":
            if style == "telegraph" and out and out[-1] != STOP[lang]:
                out.append(STOP[lang])
            continue
        if style == "telegraph":
            if t in DROP[lang] and rnd.random() < 0.7:
                continue
            if rnd.random() < 0.03:
                out.append(rnd.choice(QTY[lang]) + rnd.choice(UNIT[lang]))
        out.append(t)
    return "".join(out)[:n]

if __name__ == "__main__":
    r = random.Random(1)
    for lang in ("es", "it", "pt"):
        print(lang, telegram(200, r, lang))

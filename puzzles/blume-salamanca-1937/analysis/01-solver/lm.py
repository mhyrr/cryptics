"""Telegraph-style normalisation and letter n-gram tables.

normalise(): uppercase A-Z only. Accents stripped, Ñ -> N, Ç -> C, digits spelled out
in the corpus language, everything else removed. This is how a 1937 telegram clerk's
alphabet looks: 26 letters, no spaces, no accents.

Builds out/lm_<lang>_2.bin and out/lm_<lang>_4.bin: float32 log10 probabilities,
indexed a*26+b and ((a*26+b)*26+c)*26+d, with add-0.01 smoothing floor.
Writes lm_summary.json (checked in).
Usage: python3 -I lm.py
"""
import array, json, math, os, re, unicodedata, hashlib

EXCLUDE = {69948, 31552, 22065}  # two dictionaries and an English-language reader

ONES = {
 "es": "CERO UNO DOS TRES CUATRO CINCO SEIS SIETE OCHO NUEVE".split(),
 "it": "ZERO UNO DUE TRE QUATTRO CINQUE SEI SETTE OTTO NOVE".split(),
 "pt": "ZERO UM DOIS TRES QUATRO CINCO SEIS SETE OITO NOVE".split(),
}

def spell_digits(m, lang):
    # telegraph practice spelled figures out; digit-by-digit is a crude but language-true stand-in
    return "".join(ONES[lang][int(c)] for c in m.group(0))

def strip_gutenberg(t):
    s = re.search(r"\*\*\* ?START OF (THE|THIS) PROJECT GUTENBERG.*?\*\*\*", t)
    e = re.search(r"\*\*\* ?END OF (THE|THIS) PROJECT GUTENBERG", t)
    return t[s.end() if s else 0: e.start() if e else len(t)]

def normalise(t, lang="es"):
    t = re.sub(r"[0-9]+", lambda m: spell_digits(m, lang), t)
    t = unicodedata.normalize("NFKD", t.upper())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^A-Z]", "", t)

def load_split(lang, split, manifest):
    out = []
    for b in manifest[lang]:
        if b["split"] != split or b["id"] in EXCLUDE:
            continue
        raw = open(f"out/raw_{lang}/{b['id']}.txt", encoding="utf-8", errors="replace").read()
        out.append(normalise(strip_gutenberg(raw), lang))
    return "".join(out)

def table(text, n):
    counts = array.array("d", [0.0]) * (26 ** n)
    v = [ord(c) - 65 for c in text]
    for i in range(len(v) - n + 1):
        k = 0
        for j in range(n):
            k = k * 26 + v[i + j]
        counts[k] += 1
    tot = sum(counts) + 0.01 * len(counts)
    return array.array("f", (math.log10((c + 0.01) / tot) for c in counts))

def main():
    manifest = json.load(open("corpus_manifest.json"))
    summary = {}
    for lang in ("es", "it", "pt"):
        train = load_split(lang, "train", manifest)
        held = load_split(lang, "heldout", manifest)
        open(f"out/heldout_{lang}.txt", "w").write(held)
        open(f"out/train_{lang}.txt", "w").write(train)
        info = {"train_letters": len(train), "heldout_letters": len(held)}
        for n in (2, 4):
            tb = table(train, n)
            p = f"out/lm_{lang}_{n}.bin"
            tb.tofile(open(p, "wb"))
            info[f"sha256_{n}"] = hashlib.sha256(open(p, "rb").read()).hexdigest()
        summary[lang] = info
        print(lang, info)
    json.dump(summary, open("lm_summary.json", "w"), indent=1)

if __name__ == "__main__":
    main()

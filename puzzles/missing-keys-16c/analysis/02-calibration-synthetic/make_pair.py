"""Make a synthetic pair: period Spanish enciphered with Cp.30 (es. 132 Cipher 3), with reader noise.

    python3 make_pair.py <letters> <seed> <outdir>
Plaintext: Lazarillo de Tormes, tratado primero (es.wikisource, 1921 edition; sources/PROVENANCE.md).
Key: ../../../vargas-mexia-es132/sources/keys/cipher3.tsv rows 1-2 (numbers), clusters and marks. Added for the
test, because class A ciphers have them and Cp.30 as printed does not: eight word codes (numbers 101-108 with a
cross above) for the commonest words of five letters or more, and two nulls (0 and 1) at 2% of tokens.
Noise on the cipher side, 12% of tokens in all: a mark above dropped (4%), a base misread as another base (4%),
a token missed (2%), a mark after misread (2%). Noise on the plain side: 1.5% of letters changed or dropped
(the period decipherer's spelling). Writes cipher.txt, plain.txt, truth.tsv (unit -> value).
"""
import random, re, sys, unicodedata
from pathlib import Path
HERE = Path(__file__).resolve().parent
BASE = {"a": ["10", "9"], "b": ["8"], "c": ["7"], "d": ["6"], "e": ["4", "3"], "f": ["2"], "g": ["11"],
        "h": ["12"], "i": ["13", "14"], "l": ["15"], "m": ["16"], "n": ["17"], "o": ["18", "19"], "p": ["20"],
        "q": ["21"], "r": ["22"], "s": ["23"], "t": ["24"], "u": ["25", "26"], "x": ["27"], "y": ["28"], "z": ["29"]}
CLUSTER = {"br": "30", "cr": "31", "dr": "32", "fr": "33", "gr": "34", "pl": "35", "tr": "36"}
AFTER = {"a": "plus", "e": "dot", "i": "curl", "o": "hook", "u": "tbar"}
ABOVE = {"l": "acute", "m": "grave", "n": "hat", "r": "v", "s": "bar"}
VOW = "aeiou"


def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z]", "", w.replace("v", "u").replace("j", "i").replace("k", "c").replace("w", "u"))


def encipher_word(w, rng):
    out, i = [], 0
    while i < len(w):
        c2 = w[i:i + 2]
        if c2 in CLUSTER:
            base, i = CLUSTER[c2], i + 2
        elif w[i] in VOW:
            out.append(rng.choice(BASE[w[i]]))
            i += 1
            continue
        else:
            base, i = rng.choice(BASE[w[i]]), i + 1
        tok = base
        if i < len(w) and w[i] in VOW:
            tok += ":" + AFTER[w[i]]
            i += 1
            if i < len(w) and w[i] in ABOVE and (i + 1 == len(w) or w[i + 1] not in VOW) and rng.random() < 0.8:
                tok += "^" + ABOVE[w[i]]
                i += 1
        out.append(tok)
    return out


def main(nlet, seed, outdir):
    rng = random.Random(seed)
    raw = (HERE / "../../sources/cache/lazarillo-wikisource.txt").read_text(encoding="utf-8")
    raw = raw[raw.index("Pues sepa"):]
    words = [w for w in (norm(x) for x in raw.split()) if w]
    k, n = 0, 0
    while n < nlet:
        n += len(words[k]); k += 1
    words = words[:k]
    freq = {}
    for w in words:
        if len(w) >= 5:
            freq[w] = freq.get(w, 0) + 1
    codes = {w: str(101 + r) for r, (w, _) in enumerate(sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:8])}
    truth = {}
    for l, bs in BASE.items():
        for b in bs:
            truth[b] = l
    truth.update({v: k2 for k2, v in CLUSTER.items()})
    truth.update({":" + v: k2 for k2, v in AFTER.items()})
    truth.update({"^" + v: k2 for k2, v in ABOVE.items()})
    truth.update({v: k2 for k2, v in codes.items()})
    truth.update({"^cross": "", "0": "", "1": ""})
    bases = sorted(set(sum(BASE.values(), [])) | set(CLUSTER.values()))
    toks, plain = [], []
    for w in words:
        if w in codes and rng.random() < 0.85:
            wt = [codes[w] + "^cross"]
        else:
            wt = encipher_word(w, rng)
        for t in wt:
            if rng.random() < 0.02:
                toks.append(rng.choice(["0", "1"]))
            r = rng.random()
            if r < 0.04 and "^" in t:
                t = t[:t.rindex("^")]
            elif r < 0.08:
                m = re.match(r"^(\d+)(.*)$", t)
                t = rng.choice(bases) + m.group(2)
            elif r < 0.10:
                continue
            elif r < 0.12 and ":" in t:
                t = re.sub(r":[a-z]+", ":" + rng.choice(sorted(AFTER.values())), t)
            toks.append(t)
        pw = "".join(c for c in w if rng.random() > 0.0075)
        pw = "".join(rng.choice("aeiosnrl") if rng.random() < 0.0075 else c for c in pw)
        plain.append(pw)
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    lines = [" ".join(toks[i:i + 22]) for i in range(0, len(toks), 22)]
    (out / "cipher.txt").write_text("# synthetic Cp.30 pair, seed %d\n" % seed + "\n".join(lines) + "\n")
    (out / "plain.txt").write_text(" ".join(plain) + "\n")
    (out / "truth.tsv").write_text("".join(f"{u}\t{v}\n" for u, v in sorted(truth.items())))
    print(f"{len(words)} words, {sum(map(len, words))} letters, {len(toks)} tokens, {len(lines)} lines, codes {codes}")


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])

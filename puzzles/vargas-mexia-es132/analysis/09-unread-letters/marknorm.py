"""Exp 09: per-reader vowel-mark normalisation. Frozen 2026-10-16 before f. 174 B and any f. 185 output exists.

Problem: blind readers sometimes write a Cipher 3 vowel mark-after with the wrong guide symbol, consistently (f. 174 A
writes the -o hook as a curl, so "lo que" decodes "li qe"). The key is not at fault; the reader's notation is.

Method (mechanical, no hand-chosen words):
- Language model: letter trigrams (add-one smoothing) over every clear-Spanish span `[[ … ]]` in
  ../../sources/transcription/*/transcription.txt, excluding the transcription being scored.
- The frozen decoder (`../04-cipher3/decode_c3_v2.py --v22 --tsv`) decodes each token; the vowel contributed by its
  mark-after (+ a, . e, p o, <tbar> u, joined curl i) is identified per token. All 120 permutations of those five
  vowels are tried on the mark vowels only (base-letter vowels, codes and clear text untouched); each result is scored
  by mean trigram log-probability per character. The best permutation wins.
- Control (pre-stated): on f. 202 A/B and f. 37 A/B the identity assignment must win. If it does not, the method is not
  used.
- Output: the winning permutation, its score, the identity score and rank; with --write, the normalised decode
  (never over the reader's file).

    python3 marknorm.py <transcription.txt> [--write OUT]
"""
import itertools, math, re, subprocess, sys, tempfile
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TR = HERE.parent.parent / "sources" / "transcription"
DEC = HERE.parent / "04-cipher3" / "decode_c3_v2.py"
VOWEL_SYM = {"a": "+", "e": ".", "o": "p", "i": "6", "u": "<tbar>"}
SYMS = ["+", ".", "p", "6", "<tbar>"]


def letters(s):
    s = re.sub(r"⟨[^⟩]*⟩", " ", s).lower()
    s = s.replace("v", "u").replace("j", "i").replace("y", "i").replace("ç", "z")
    return re.sub(r"[^a-zñ]+", " ", s)


def build_lm(exclude):
    c3, c2 = Counter(), Counter()
    for f in TR.glob("*/transcription.txt"):
        if f.resolve() == Path(exclude).resolve():
            continue
        for m in re.finditer(r"\[\[(.*?)\]\]", f.read_text(encoding="utf-8", errors="ignore")):
            t = " " + letters(m.group(1)) + " "
            for i in range(len(t) - 2):
                c3[t[i:i + 3]] += 1; c2[t[i:i + 2]] += 1
    return c3, c2


def score(text, lm):
    c3, c2 = lm
    t = " " + re.sub(r"\s+", " ", letters(text)) + " "
    if len(t) < 10:
        return -99
    tot = sum(math.log((c3[t[i:i + 3]] + 1) / (c2[t[i:i + 2]] + 28)) for i in range(len(t) - 2))
    return tot / (len(t) - 2)


MARK_V = {"+": "a", ".": "e", "p": "o", "<tbar>": "u"}


def alias(path):
    """Amendment 2026-10-16 (after f. 185a B, before its A): a number followed by `e` is the guide's hook `p` (guide §2
    lists "an e with a tail" under the hook). Applied outside [[ ]] only. Returns a temp file path."""
    out = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            out.append(line); continue
        parts = re.split(r"(\[\[.*?\]\])", line)
        parts = [c if c.startswith("[[") else re.sub(r"(?<![\w<])(\d+)e(?=[<\s?]|$)", r"\1p", c) for c in parts]
        out.append("".join(parts))
    f = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False)
    f.write("\n".join(out) + "\n"); f.close()
    return f.name


def tokens(path):
    """Decoder --tsv token stream: (line, token, decoded, mark vowel or None)."""
    r = subprocess.run([sys.executable, "-I", str(DEC), alias(path), "--v22", "--tsv"], capture_output=True, text=True)
    out = []
    for row in r.stderr.splitlines():
        if not row.startswith("TOK\t"):
            continue
        _, ln, t, d = row.split("\t", 3)
        m = re.match(r"^(\d+|[A-Za-z])(\+|\.|p|<tbar>)?", t)
        v = MARK_V.get(m.group(2)) if m and m.group(2) else None
        if v is None and m and m.group(1).isdigit() and len(m.group(1)) >= 2 and m.group(1).endswith("6") \
                and not d.startswith("⟨") and d.rstrip("lmnrs").endswith("i"):
            v = "i"  # joined curl parsed by the decoder as -i
        out.append((int(ln), t, d, v))
    return out


def apply(toks, perm):
    """perm: vowel as written -> vowel meant. Replaces the mark vowel inside each decoded token."""
    lines = {}
    for ln, t, d, v in toks:
        if v and not d.startswith("⟨"):
            core = d.rstrip("lmnrs")
            k = core.rfind(v)
            if k >= 0:
                d = d[:k] + perm[v] + d[k + 1:]
        lines.setdefault(ln, []).append(d)
    return "\n".join(f"{ln:3d}  " + " ".join(ws) for ln, ws in sorted(lines.items()))


def main():
    path = sys.argv[1]
    lm = build_lm(path)
    toks = tokens(path)
    results = []
    for vs in itertools.permutations("aeoiu"):
        perm = dict(zip("aeoiu", vs))
        results.append((score(apply(toks, perm), lm), vs, perm))
    results.sort(reverse=True)
    ident = [r for r in results if r[1] == tuple("aeoiu")][0]
    fmt = lambda vs: " ".join(f"{w}->{m}" for w, m in zip("aeoiu", vs) if w != m) or "identity"
    print(f"{path}\nbest: {fmt(results[0][1])}  score {results[0][0]:.3f}\n"
          f"identity score {ident[0]:.3f} (rank {results.index(ident) + 1}/120)\n"
          f"runner-up: {fmt(results[1][1])}  score {results[1][0]:.3f}")
    if "--write" in sys.argv:
        Path(sys.argv[sys.argv.index("--write") + 1]).write_text(apply(toks, results[0][2]) + "\n", encoding="utf-8")


main()

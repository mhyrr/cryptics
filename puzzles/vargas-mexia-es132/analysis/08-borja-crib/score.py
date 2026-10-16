"""Exp 08: score a blind Cipher 3 transcription of Borja's letter (BnF fr. 15561 ff. 42-43) against the contemporary
marginal decipherment. Frozen 2026-10-16 before any reader output exists.

    python3 score.py <cipher transcription.txt> <margin plaintext.txt> [--show]

Inputs
- Cipher transcription in CIPHER3-GUIDE v2.2 notation, with passage headers `# ===== P1 =====` .. `# ===== P4 =====`.
  Clear text in [[ ]] is ignored.
- Margin plaintext with headers `# P1` .. `# P4`. Abbreviation expansions in [ ] are kept as letters.

Method (rules fixed here, not after seeing results)
- Each cipher token is decoded with the frozen decoder `../04-cipher3/decode_c3_v2.py --v22` (key
  `../../sources/keys/cipher3.tsv` = Cp.30, extensions `../04-cipher3/c3_extensions.tsv`). Tomokiyo's Borgia table is
  NOT used: it was reconstructed from this letter, so scoring with it would be circular.
- Normalisation, both sides: lower case; accents dropped; v->u, j->i, y->i, ç->z; letters only. Unknowns ⟨…⟩ dropped;
  "(x|y)" alternatives take the first. Code values (upper case from the extensions) are letters like any other.
- Per passage, difflib (autojunk off) aligns the decoded letter stream to the plaintext stream.
  recall = matched / plaintext letters; precision = matched / decoded letters.
- Per token: correct = it decodes to >= 1 letter and every one of its letters is matched. Per base (the number or
  letter form without marks): n tokens, n correct.
- Named checks: every token whose base is 108 or that carries <cross> (H12, codes), and every 35 (H11), is printed with
  its decoded value and the plaintext aligned to it (for a token with no matched letters: the plaintext between the
  nearest matched letters on either side).
"""
import importlib.util, re, sys, difflib, unicodedata
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.argv.append("--v22")  # decoder reads its mode from argv at import
spec = importlib.util.spec_from_file_location("dec", HERE.parent / "04-cipher3" / "decode_c3_v2.py")
dec = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dec)
sys.argv.remove("--v22")


def norm(s):
    s = re.sub(r"⟨[^⟩]*⟩", "", s)
    s = re.sub(r"\(([^|)]*)\|[^)]*\)", r"\1", s)
    s = s.lower().replace("ç", "z")
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    s = s.replace("v", "u").replace("j", "i").replace("y", "i")
    return re.sub(r"[^a-zñ]", "", s)


def read_cipher(path):
    ext, flags = dec.load_ext(), []
    passages, cur = defaultdict(list), None
    for lno, line in enumerate(open(path, encoding="utf-8"), 1):
        m = re.match(r"^#\s*=+\s*(P\d)\b", line)
        if m:
            cur = m.group(1); continue
        if line.startswith("#") or not line.strip() or cur is None:
            continue
        line = re.sub(r"\[\[.*?\]\]", " ", line)
        for t in line.split():
            passages[cur].append((lno, t, dec.tok(t, ext, flags, f"{lno}")))
    return passages


def read_plain(path):
    out, cur = defaultdict(str), None
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^#\s*(P\d)\b", line)
        if m:
            cur = m.group(1); continue
        if line.startswith("#") or cur is None:
            continue
        out[cur] += " " + line.strip()
    return out


def base_of(t):
    m = re.match(r"^(\d+|[A-Za-z])", t)
    return m.group(1) if m else t


def main():
    show = "--show" in sys.argv
    cipher, plain = read_cipher(sys.argv[1]), read_plain(sys.argv[2])
    per_base = defaultdict(lambda: [0, 0])
    tot = [0, 0, 0]
    named = []
    for p in sorted(set(cipher) | set(plain)):
        toks = cipher.get(p, [])
        stream, owner = [], []
        for i, (_, _, d) in enumerate(toks):
            for c in norm(d):
                stream.append(c); owner.append(i)
        a, b = "".join(stream), norm(plain.get(p, ""))
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        amap = {}
        for blk in sm.get_matching_blocks():
            for k in range(blk.size):
                amap[blk.a + k] = blk.b + k
        matched = len(amap)
        tot[0] += matched; tot[1] += len(b); tot[2] += len(a)
        print(f"{p}: {len(toks)} tokens; plaintext {len(b)} letters, decoded {len(a)}; matched {matched}: "
              f"recall {matched / max(1, len(b)):.0%}, precision {matched / max(1, len(a)):.0%}")
        pos = defaultdict(list)
        for k, i in enumerate(owner):
            pos[i].append(k)
        for i, (lno, t, d) in enumerate(toks):
            ks = pos[i]
            ok = bool(ks) and all(k in amap for k in ks)
            pb = per_base[base_of(t)]
            pb[0] += 1; pb[1] += ok
            if base_of(t) in ("108", "35") or "<cross>" in t:
                hit = [amap[k] for k in ks if k in amap]
                if hit:
                    seg = b[min(hit):max(hit) + 1]
                else:
                    before = [amap[k] for k in amap if owner[k] < i]
                    after = [amap[k] for k in amap if owner[k] > i]
                    lo = max(before) + 1 if before else 0
                    hi = min(after) if after else len(b)
                    seg = f"(gap) {b[lo:hi]}"
                ctx = " ".join(x[2] for x in toks[max(0, i - 3):i + 4])
                named.append(f"{p} l.{lno} {t} -> {d!r}; plaintext: {seg!r}; context: {ctx}")
        if show:
            out = []
            for op, i1, i2, j1, j2 in sm.get_opcodes():
                out.append(a[i1:i2] if op == "equal" else f"[{a[i1:i2]}|{b[j1:j2]}]")
            print("   " + "".join(out))
    print(f"ALL: recall {tot[0] / max(1, tot[1]):.0%} ({tot[0]}/{tot[1]}), precision {tot[0] / max(1, tot[2]):.0%} "
          f"({tot[0]}/{tot[2]})")
    print("\n## Per base (n, correct)")
    for k, (n, c) in sorted(per_base.items(), key=lambda kv: (-kv[1][0], kv[0])):
        print(f"{k}\t{n}\t{c}\t{c / n:.0%}")
    print("\n## Named checks (108, <cross>, 35)")
    print("\n".join(named) or "(none)")


main()

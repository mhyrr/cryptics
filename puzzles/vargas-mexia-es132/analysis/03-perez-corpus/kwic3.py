"""Held-out test 3: every occurrence of the five extensions in ff. 157 and 179 (decoded context)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "02-key-extensions"))
import decode_v1 as v
CAND = {"21. que": r"^21\.\??$", "21_ qui": r"^21_\??$", "2H que": r"^2H[+._^]*\??$",
        "H ne": r"^H[+._^]*\??$", "Sigma o": r"^(<sign:Sigma>|ε)"}
for f in ["f157", "f179"]:
    toks = []
    for lno, line in enumerate(open(HERE.parent.parent / "sources/transcription" / f / "transcription.txt"), 1):
        if line.startswith("#"): continue
        for ch in re.split(r"(\[\[.*?\]\])", line.rstrip("\n")):
            if ch.startswith("[["): toks.append((lno, ch, ch)); continue
            for t in ch.split(): toks.append((lno, t, v.decode_line(t, lno, [])))
    for name, rx in CAND.items():
        hits = [i for i, (_, t, _) in enumerate(toks) if not t.startswith("[[") and re.search(rx, t)]
        print(f"\n== {f} · {name} · {len(hits)}")
        for i in hits:
            l = " ".join(x[2] for x in toks[max(0, i-6):i]); r = " ".join(x[2] for x in toks[i+1:i+7])
            print(f"  l{toks[i][0]:>2} …{l[-55:]:>55} {{{toks[i][1]}}} {r[:55]}…")

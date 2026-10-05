"""Compare cabinet-noir's readings (CLAIMANT; sources/cache/thirdparty/cn_*lecture.md, cn_f017.md) with our frozen decodes.
Every Spanish quotation in « … » is scored as in mignet_check.py: the share of its normalised letters found in order in a
window of our decoded text. Control: the same quotations against a decode of a different letter. Run only after our
decodes were frozen (they were: see git log).
    python3 thirdparty_compare.py > thirdparty_compare.txt
"""
import re
from pathlib import Path
from mignet_check import norm, decoded_text, best
TP = Path(__file__).resolve().parents[2] / "sources" / "cache" / "thirdparty"
PAIRS = [("f. 11-12v", "cn_f011-012_lecture.md", ["f11_A_decoded.txt", "f11_B_decoded.txt"], "f34_A_decoded.txt"),
         ("f. 17-25", "cn_f017.md", ["f17_A_decoded.txt", "f17_B_decoded.txt", "f22_A_decoded.txt"], "f11_A_decoded.txt"),
         ("f. 34", "cn_f034_lecture.md", ["f34_A_decoded.txt", "f34_B_decoded.txt"], "f11_A_decoded.txt")]
SPANISH = re.compile(r"\b(que|de|los|las|por|mi|con|del|y)\b")


def quotes(path):
    t = Path(path).read_text(encoding="utf-8")
    out = []
    for q in re.findall(r"«([^»]{40,})»", t, flags=re.S):
        q = re.sub(r"\[[^\]]*\]", " ", q)
        if len(SPANISH.findall(q)) >= 4:
            out.append(" ".join(q.split()))
    return out


for name, cn, ours, ctrl in PAIRS:
    qs = quotes(TP / cn)
    texts = {o: decoded_text(o) for o in ours}
    ct = decoded_text(ctrl)
    print(f"## {name}: {len(qs)} quotations from {cn}")
    rs, cs = [], []
    for q in qs:
        r = max(best(q, t)[0] for t in texts.values()); c = best(q, ct)[0]
        rs.append(r); cs.append(c)
        print(f"{r:4.0%} (control {c:4.0%})  {q[:110]}")
    if rs:
        rs.sort(); cs.sort()
        print(f"median {rs[len(rs)//2]:.0%} vs control median {cs[len(cs)//2]:.0%}\n")


# pangoleen/cipher-readings f. 26r (CLAIMANT): the decoded Spanish paragraphs, sentence by sentence.
pg = (TP / "pg_reading_f26r.md").read_text(encoding="utf-8")
sp = pg[pg.index("## Spanish"):pg.index("## English")]
sp = re.sub(r"\[[^\]]*\]|\(\?\)|…", " ", sp.split("\n", 2)[2])
sents = [s.strip() for s in re.split(r"(?<=[.;])\s+", " ".join(sp.split())) if len(s) > 40]
texts = [decoded_text(o) for o in ("f26_A_decoded.txt", "f26_B_decoded.txt")]
ct = decoded_text("f34_A_decoded.txt")
print(f"## f. 26r: {len(sents)} sentences from pg_reading_f26r.md")
rs, cs = [], []
for s in sents:
    r = max(best(s, t)[0] for t in texts); c = best(s, ct)[0]
    rs.append(r); cs.append(c)
    print(f"{r:4.0%} (control {c:4.0%})  {s[:110]}")
rs.sort(); cs.sort()
print(f"median {rs[len(rs)//2]:.0%} vs control median {cs[len(cs)//2]:.0%}")


# pangoleen ff. 87, 157, 179 (Cipher 4 runs inside Pérez's clear letters): each «…» cipher run vs our exp-05 v2 decode.
V2 = Path(__file__).resolve().parent.parent / "05-cipher4-v2"
pp = (TP / "pg_reading_perez_f87_f157_f179.md").read_text(encoding="utf-8")
secs = {"f. 87": ("## 1.", "## 2.", "f87_v2.txt"), "f. 157": ("## 2.", "## 3.", "f157_v2.txt"),
        "f. 179": ("## 3.", None, "f179_v2.txt")}
for name, (a, b, ours) in secs.items():
    sec = pp[pp.index(a):pp.index(b) if b else None]
    sec = sec[:sec.index("### English")] if "### English" in sec else sec
    runs = [" ".join(re.sub(r"\[[^\]]*\]|\(\?\)", " ", r).split()) for r in re.findall(r"«([^»]+)»", sec)]
    runs = [r for r in runs if len(norm(r)) >= 12]
    t = decoded_text(V2 / ours); ct = decoded_text("f11_A_decoded.txt")
    rs = sorted(best(r, t)[0] for r in runs); cs = sorted(best(r, ct)[0] for r in runs)
    print(f"\n## {name} (pangoleen) vs ../05-cipher4-v2/{ours}: {len(runs)} cipher runs of >= 12 letters; "
          f"median {rs[len(rs)//2]:.0%} vs control median {cs[len(cs)//2]:.0%}; runs under 70%: "
          f"{sum(r < .7 for r in rs)}")

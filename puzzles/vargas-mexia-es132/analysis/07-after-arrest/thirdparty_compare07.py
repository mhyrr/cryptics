"""Exp 07: cabinet-noir's readings (CLAIMANT; sources/cache/thirdparty/cn_fNNN_lecture.md, fetched 2026-10-05 after our
decodes were frozen) against our frozen decodes, scored as in ../06-premurder/thirdparty_compare.py (every Spanish
«…» quotation, best in-order letter match in our decoded text). Control: the same quotations against another letter.
    python3 thirdparty_compare07.py > thirdparty_compare07.txt"""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "06-premurder"))
from mignet_check import decoded_text, best  # noqa: E402
TP = Path(__file__).resolve().parents[2] / "sources" / "cache" / "thirdparty"
PAIRS = [("f. 215", "cn_f215_lecture.md", ["f215_A_dec.txt", "f215_B2_dec.txt"], "f228_dec.txt"),
         ("f. 220/224", "cn_f220-221_lecture.md", ["f220_2_dec.txt", "f224_2_dec.txt"], "f228_dec.txt"),
         ("f. 222/226", "cn_f222_lecture.md", ["f222_2_dec.txt", "f226_2_dec.txt"], "f228_dec.txt"),
         ("f. 228/231", "cn_f228-229_lecture.md", ["f228_dec.txt", "f231_dec.txt"], "f220_2_dec.txt"),
         ("f. 245/247", "cn_f245_lecture.md", ["f245_dec.txt", "f247_dec.txt"], "f228_dec.txt"),
         ("f. 255/261", "cn_f255_lecture.md", ["f255_dec.txt", "f261_dec.txt"], "f228_dec.txt")]
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
    texts = [decoded_text(o) for o in ours]
    ct = decoded_text(ctrl)
    rs, cs = [], []
    print(f"## {name}: {len(qs)} quotations from {cn}")
    for q in qs:
        r = max(best(q, t)[0] for t in texts); c = best(q, ct)[0]
        rs.append(r); cs.append(c)
        print(f"{r:4.0%} (control {c:4.0%})  {q[:100]}")
    if rs:
        rs.sort(); cs.sort()
        print(f"median {rs[len(rs)//2]:.0%} vs control median {cs[len(cs)//2]:.0%}\n")

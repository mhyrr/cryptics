"""List the dated entries in chosen sections of the Mingshi Wuxing and Tianwen treatises.

Usage:
  python3 -I mingshi.py data/raw/papers/mingshi_28.wiki data/raw/papers/mingshi_27.wiki > results/mingshi.txt

Each section starts with a line '▲NAME'. Within a section, an entry begins at an
era tag {{YL|ERA N年}} or at a bare 'N年' that continues the previous era. The
script prints every entry from 1436 to 1464 and, for each section, the first
Ming year it records.
"""
import re, sys

ERAS = {"洪武": 1368, "建文": 1399, "永樂": 1403, "洪熙": 1425, "宣德": 1426, "正統": 1436, "正统": 1436, "永乐": 1403, "景泰": 1450,
        "天順": 1457, "天顺": 1457, "成化": 1465, "弘治": 1488, "正德": 1506, "嘉靖": 1522, "隆慶": 1567, "隆庆": 1567,
        "萬曆": 1573, "万历": 1573, "泰昌": 1620, "天啓": 1621, "天启": 1621, "崇禎": 1628, "崇祯": 1628}
NUM = {"元": 1, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}
SECTIONS = {"恆寒", "恆陰", "雨雪隕霜", "日变月变", "晕适", "云气", "天变"}


def cnum(s):
    if s in NUM:
        return NUM[s]
    a, _, b = s.partition("十")
    return (NUM[a] if a else 1) * 10 + (NUM[b] if b else 0)


for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    for sec in re.split(r"▲", text)[1:]:
        name, _, body = sec.partition("\n")
        name = name.strip()
        if name not in SECTIONS:
            continue
        body = re.sub(r"\{\{YL\|([^}]*)\}\}", r"\1", body)
        era, out = None, []
        for m in re.finditer(r"(" + "|".join(ERAS) + r")?([元一二三四五六七八九十]+)年([^。]*。)", body):
            if m.group(1):
                era = m.group(1)
            if era is None:
                continue
            try:
                y = ERAS[era] + cnum(m.group(2)) - 1
            except KeyError:  # e.g. '二、四月' read as a year; skip
                continue
            out.append((y, (m.group(1) or era) + m.group(2) + "年" + m.group(3)))
        print("== %s (%s): %d dated clauses; first year %s" % (name, path.split("/")[-1], len(out),
                                                                 out[0][0] if out else "-"))
        for y, t in out:
            if 1436 <= y <= 1464:
                print("  %d  %s" % (y, t))

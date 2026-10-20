"""Dump every sheet of an .xlsx workbook to TSV files, standard library only.

usage: python3 -I xlsx2tsv.py BOOK.xlsx OUTDIR

Reads shared strings and cell values only. Formulas give their cached value.
Output files are named sheetN.tsv; a sheets.txt index maps N to the sheet name.
"""
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
RNS = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"


def col_index(ref):
    letters = re.match(r"[A-Z]+", ref).group(0)
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch) - 64)
    return n - 1


def main(book, outdir):
    os.makedirs(outdir, exist_ok=True)
    z = zipfile.ZipFile(book)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        root = ET.fromstring(z.read("xl/sharedStrings.xml"))
        for si in root.findall("m:si", NS):
            shared.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    target = {r.get("Id"): r.get("Target") for r in rels}
    index = []
    for i, sh in enumerate(wb.find("m:sheets", NS), 1):
        path = "xl/" + target[sh.get(RNS + "id")].lstrip("/").replace("xl/", "")
        root = ET.fromstring(z.read(path))
        rows = []
        for row in root.iter("{%s}row" % NS["m"]):
            cells = {}
            for c in row.findall("m:c", NS):
                v = c.find("m:v", NS)
                t = c.get("t")
                if t == "inlineStr":
                    val = "".join(x.text or "" for x in c.iter("{%s}t" % NS["m"]))
                elif v is None:
                    continue
                elif t == "s":
                    val = shared[int(v.text)]
                else:
                    val = v.text
                cells[col_index(c.get("r"))] = val.replace("\t", " ").replace("\n", " ")
            if cells:
                rows.append([cells.get(j, "") for j in range(max(cells) + 1)])
        with open(os.path.join(outdir, "sheet%d.tsv" % i), "w", encoding="utf-8") as f:
            for r in rows:
                f.write("\t".join(r) + "\n")
        index.append("%d\t%s\t%d rows" % (i, sh.get("name"), len(rows)))
    with open(os.path.join(outdir, "sheets.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(index) + "\n")
    print("\n".join(index))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

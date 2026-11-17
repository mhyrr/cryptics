#!/usr/bin/env python3
"""Fetch the page images for catalogue item 2911 (Dieci di Balia to Machiavelli, 17 Aug 1510,
BNCF Carte Machiavelli V/134), its sibling 2910 (V/125) and the pair candidates, from BNCF Teca.

Standard library only. Rerunnable: files already in cache/ are kept, not refetched.

    python3 -I fetch.py                 # masters (300 dpi, about 2700 x 3700 px) of the PAGES list
    python3 -I fetch.py --survey        # viewer-size copies (about 900 x 1250 px) of every page of GROUPS
    python3 -I fetch.py --mag           # only refresh the MAG records (page lists) into cache/mag/
    python3 -I fetch.py --keysheets     # masters of every page of Carte Machiavelli VI/82 (period key sheets)
                                        # into cache/keysheets/ (for keysheet-check.md; KEY MATERIAL: the
                                        # main thread and the readers stay out of that folder)

Recipe (found 2026-11-16):
  1. Page list: OAI-PMH GetRecord, metadataPrefix=mag, on
     https://teca.bncf.firenze.sbn.it/OAI/servlet/OAIHandler
     identifier oai:bncf.firenze.sbn.it:21:FI0098:AutografiPalatini:Machiavelli_<vol>_<n>[_<m>]
     (folders group several documents: V_124_133, V_134_136, V_141_149 ...). Each <mag:img> gives
     the sequence number, the carta ("Carta: 1 r"), the image id RisIdr=BNCF000385xxxx and the
     master's pixel size. The viewer's own list is .../ImageViewer/servlet/ImageViewer?idr=<folder>&azione=readBook.
  2. Image: https://teca.bncf.firenze.sbn.it/ImageViewer/servlet/ImageViewer?idr=<image id>&azione=showImg&usage=2
     serves the 300 dpi master (pixel size as in the MAG record); without usage=2 (or with usage=3)
     it serves the 100 dpi copy the viewer shows. The MAG's own file URLs on digitale.bncf.firenze.sbn.it
     return 404. The served master's md5 differs from the MAG md5 (re-encoded); sha256 is recorded here.
  Folders carry no per-document boundaries: which carte belong to which shelfmark is read from the
  page (lapis document number top right) and recorded in gate.md.
"""
import hashlib
import re
import struct
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HOST = "https://teca.bncf.firenze.sbn.it"
OAI = HOST + "/OAI/servlet/OAIHandler"
UA = {"User-Agent": "Mozilla/5.0 (compatible; research-fetch/1.0)"}
HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache"
DATE = "2026-11-16"

# OAI record suffixes surveyed
GROUPS = ["V_134_136", "V_124_133", "V_139", "V_140", "V_123", "V_141_149"]

# masters fetched: (group, carta label as in the MAG, e.g. "1 r"); identified from the survey (see gate.md)
PAGES = [
    # V/134 (item 2911) = V_134_136 cc. 1-2 (lapis "134", old foliation 230)
    ("V_134_136", "1 r"), ("V_134_136", "1 v"), ("V_134_136", "2 r"), ("V_134_136", "2 v"),
    # V/135 (18 Aug 1510, printed Opere VI pp. 72-74) = V_134_136 cc. 3-4 (lapis "135", old 235)
    ("V_134_136", "3 r"), ("V_134_136", "3 v"), ("V_134_136", "4 r"), ("V_134_136", "4 v"),
    # V/136 copy of the Dieci's letter to Francesco Pandolfini = cc. 5-6 (lapis "136", old 250);
    # c. 7 a modern sheet "Copia di lettera a Francesco Pandolfini a Milano" (lapis "136"); c. 8 blank
    ("V_134_136", "5 r"), ("V_134_136", "5 v"), ("V_134_136", "6 r"), ("V_134_136", "6 v"),
    ("V_134_136", "7 r"), ("V_134_136", "7 v"),
    # V/125 (item 2910) = V_124_133 c. 5 (lapis "125", old 252); 5v blank
    ("V_124_133", "5 r"), ("V_124_133", "5 v"),
    # V/140 (Niccolini's letter of 5 Aug 1510, copied in cipher) and V/139 (Dieci, 7 Aug 1510;
    # Machiavelli's decipherment of V/140 on cc. 1v-2r)
    ("V_140", "1 r"), ("V_140", "1 v"), ("V_140", "2 r"), ("V_140", "2 v"),
    ("V_139", "1 r"), ("V_139", "1 v"), ("V_139", "2 r"), ("V_139", "2 v"),
    # V/123: cipher slip and Machiavelli's decipherment slip
    ("V_123", "1 r"), ("V_123", "1 v"), ("V_123", "2 r"), ("V_123", "2 v"), ("V_123", "3 r"),
]


def get(url, tries=3, timeout=120):
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read()
        except Exception as e:  # reported, not hidden
            last = e
            time.sleep(3 * (i + 1))
    raise RuntimeError(f"{url}: {last}")


def jpeg_size(b):
    i = 2
    while i < len(b):
        if b[i] != 0xFF:
            i += 1
            continue
        m = b[i + 1]
        if m in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", b[i + 5:i + 9])
            return w, h
        i += 2 + struct.unpack(">H", b[i + 2:i + 4])[0]
    return None, None


def mag(group):
    p = CACHE / "mag" / f"{group}.mag.xml"
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        ident = "oai:bncf.firenze.sbn.it:21:FI0098:AutografiPalatini:Machiavelli_" + group
        url = f"{OAI}?verb=GetRecord&metadataPrefix=mag&identifier={urllib.parse.quote(ident)}"
        p.write_bytes(get(url))
    t = p.read_text("utf8")
    out = []
    for blk in re.findall(r"(?s)<mag:img>(.*?)</mag:img>", t):
        seq = int(re.search(r"<mag:sequence_number>(\d+)<", blk).group(1))
        nom = re.search(r"<mag:nomenclature>([^<]*)<", blk).group(1).replace("Carta: ", "").strip()
        rid = re.search(r"RisIdr=(BNCF\d+)", blk).group(1)
        out.append((seq, nom, rid))
    return out


KEYSHEETS = "VI_82"  # OAI suffix of Carte Machiavelli VI/82 (Teca folder idr BNCF0003858588)


def fetch(group, seq, nom, rid, master, sub=None):
    tag = "" if master else "_s"
    name = f"{group}_{seq:02d}_{re.sub(r'[^A-Za-z0-9]+', '', nom)}{tag}.jpg"
    path = CACHE / (sub if sub else "" if master else "survey") / name
    url = f"{HOST}/ImageViewer/servlet/ImageViewer?idr={rid}&azione=showImg" + ("&usage=2" if master else "")
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        b = get(url)
        if b[:2] != b"\xff\xd8":
            raise RuntimeError(f"{url}: not a JPEG")
        path.write_bytes(b)
        time.sleep(0.5)
    b = path.read_bytes()
    w, h = jpeg_size(b)
    rel = path.relative_to(HERE)
    print(f"| {rel} | {url} | {DATE} | {w}x{h} | {hashlib.sha256(b).hexdigest()[:16]} |")


def main():
    if "--mag" in sys.argv:
        for g in GROUPS:
            (CACHE / "mag" / f"{g}.mag.xml").unlink(missing_ok=True)
            print(g, len(mag(g)), "images")
        return
    if "--keysheets" in sys.argv:
        for seq, nom, rid in mag(KEYSHEETS):
            fetch(KEYSHEETS, seq, nom, rid, master=True, sub="keysheets")
        return
    if "--survey" in sys.argv:
        for g in GROUPS:
            for seq, nom, rid in mag(g):
                fetch(g, seq, nom, rid, master=False)
        return
    for g, carta in PAGES:
        hits = [x for x in mag(g) if x[1] == carta]
        if not hits:
            raise SystemExit(f"{g} {carta}: not in the MAG record")
        fetch(g, *hits[0], master=True)


if __name__ == "__main__":
    main()

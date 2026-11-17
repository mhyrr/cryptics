#!/usr/bin/env python3
"""Fetch the page images for catalogue item 2345 (Baldovino del Monte, 1554-55) from ASF PAD.

Standard library only. Rerunnable: files already in cache/ are kept, not refetched.

    python3 -I fetch.py            # fetch everything, print a PROVENANCE line per file
    python3 -I fetch.py --probe    # only resolve ptif names and read IIIF info.json

Recipe (from the catalogue's access_note, 2026-11-16):
  1. https://archiviodistatofirenze.cultura.gov.it/archividigitali/riproduzione/?id=<rid>&ua=<filza>
     is an HTML page that names a .ptif under /data/iip-data/asfi/mdp_carteggio_universale/<filza>/.
     The ptif file name is <seq>_C_<carta>_<R|V>.ptif, so the carta can be checked from it.
  2. IIIF: /iipsrv/iipsrv.fcgi?IIIF=<ptif>/info.json gives the native width and height;
     <ptif>/full/max/0/default.jpg (or full/<w>,/0/default.jpg) gives the image;
     <ptif>/<x>,<y>,<w>,<h>/full/0/default.jpg gives a native-resolution crop.

The riproduzione ids for 436 cc. 849-851 and 443 cc. 78, 678-679 come from the catalogue entry's links.
The ids for 443 cc. 79 and 85 are guessed from the sequence (two ids per carta) and checked against the
carta in the ptif name; if the guess is wrong, neighbouring ids are tried.
"""
import hashlib
import json
import re
import struct
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HOST = "https://archiviodistatofirenze.cultura.gov.it"
UA = {"User-Agent": "Mozilla/5.0 (compatible; research-fetch/1.0)"}
HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache"
DATE = "2026-11-16"

# (filza, carta, side, riproduzione id, id is known (True) or guessed (False))
PAGES = [
    (436, 849, "r", 594973, True), (436, 849, "v", 594974, True),
    (436, 850, "r", 594975, True), (436, 850, "v", 594976, True),
    (436, 851, "r", 594977, True), (436, 851, "v", 594978, True),
    (443, 78, "r", 601430, True), (443, 78, "v", 601431, True),
    (443, 79, "r", 601432, False), (443, 79, "v", 601433, False),
    (443, 85, "r", 601444, False), (443, 85, "v", 601445, False),
    (443, 678, "r", 602630, True), (443, 678, "v", 602631, True),
    (443, 679, "r", 602632, True), (443, 679, "v", 602633, True),
]


def get(url, tries=3, timeout=90):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:  # network errors are reported, not hidden
            last = e
            time.sleep(3 * (i + 1))
    raise RuntimeError(f"{url}: {last}")


def ptif_of(rid, filza):
    html = get(f"{HOST}/archividigitali/riproduzione/?id={rid}&ua={filza}").decode("utf8", "replace")
    names = sorted(set(re.findall(r"/data/iip-data/[\w/.\-]+?\.ptif", html)))
    return names[0] if names else None


def carta_of(ptif):
    m = re.search(r"_C_0*(\d+)\w*?_([RV])\.ptif$", ptif, re.I)
    return (int(m.group(1)), m.group(2).lower()) if m else (None, None)


def resolve(filza, carta, side, rid, known):
    cands = [rid] if known else [rid] + [rid + d for d in (-2, 2, -4, 4, -1, 1, -6, 6)]
    for c in cands:
        p = ptif_of(c, filza)
        if p and carta_of(p) == (carta, side):
            return c, p
        if known:
            return c, p  # trust the catalogue's id; the mismatch is reported by the caller
    return None, None


def jpeg_size(b):
    i = 2
    while i < len(b):
        if b[i] != 0xFF:
            i += 1
            continue
        mk = b[i + 1]
        if mk in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", b[i + 5:i + 9])
            return w, h
        i += 2 + struct.unpack(">H", b[i + 2:i + 4])[0]
    return None


def iiif(ptif, tail):
    return f"{HOST}/iipsrv/iipsrv.fcgi?IIIF={ptif}/{tail}"


def main():
    probe = "--probe" in sys.argv
    try:
        get(f"{HOST}/archividigitali/unita-archivistica/?id=443", tries=1, timeout=30)
    except RuntimeError as e:
        sys.exit(f"ASF PAD unreachable, nothing fetched: {e}")
    CACHE.mkdir(exist_ok=True)
    lines = []
    for filza, carta, side, rid, known in PAGES:
        name = f"{filza}_c{carta}{side}.jpg"
        rid2, ptif = resolve(filza, carta, side, rid, known)
        if not ptif:
            print(f"# {name}: no ptif found near id {rid}", file=sys.stderr)
            continue
        if carta_of(ptif) != (carta, side):
            print(f"# {name}: id {rid2} names {ptif}, not c. {carta}{side}", file=sys.stderr)
        info = json.loads(get(iiif(ptif, "info.json")))
        w, h = info.get("width"), info.get("height")
        print(f"# {name}: rid {rid2} ptif {ptif} native {w}x{h} sizes {info.get('sizes', '')[-1:] if info.get('sizes') else ''}",
              file=sys.stderr)
        if probe:
            continue
        out = CACHE / name
        url = iiif(ptif, "full/max/0/default.jpg")
        if not out.exists():
            try:
                b = get(url)
            except RuntimeError:
                url = iiif(ptif, f"full/{w},/0/default.jpg")
                b = get(url)
            out.write_bytes(b)
            time.sleep(1)
        b = out.read_bytes()
        sz = jpeg_size(b)
        lines.append(f"| {name} | {url} | {DATE} | {sz[0]}x{sz[1]} | {hashlib.sha256(b).hexdigest()[:16]} |")
    if not probe and PAGES:
        # one native-resolution crop, to show that region requests work (top strip of the bare letter)
        rid2, ptif = resolve(443, 679, "r", 602632, True)
        if ptif:
            url = iiif(ptif, "0,0,1200,400/full/0/default.jpg")
            out = CACHE / "443_c679r_crop_0_0_1200_400.jpg"
            if not out.exists():
                out.write_bytes(get(url))
            b = out.read_bytes()
            sz = jpeg_size(b)
            lines.append(f"| {out.name} | {url} | {DATE} | {sz[0]}x{sz[1]} | {hashlib.sha256(b).hexdigest()[:16]} |")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

"""signsheet.py - cut the example cells for SIGN-GUIDE.md from V/140 c. 1r and paste them into sheets.

    python3 signsheet.py

Run from this directory. Standard library plus `sips`. Writes sign-sheet/sheet-<n>.jpg (checked in: the sheets
are part of the frozen guide). Each sheet is ROWS x COLS cells; a cell is CW x CH page pixels around the point
given below, enlarged SCALE times. The sign meant is the one under the black tick at the top centre of its cell.
The names are shape names only. The list order here is the reading order of the sheets (row by row, left to
right), and SIGN-GUIDE.md repeats it.
"""
import os, subprocess, tempfile
import crop

SRC = "V_140_02_1r.jpg"
CW, CH, SCALE, COLS, ROWS = 150, 170, 2, 5, 4
GAP = 6

# (name, centre x, centre y) in pixels of cache/V_140_02_1r.jpg
CELLS = [
    # sheet 1: bowl-and-tail signs, b family, y family, crosses
    ("q", 1325, 550), ("qbar", 1843, 1050), ("qj", 890, 535), ("g", 743, 1065), ("g", 890, 1070),
    ("phi", 1595, 550), ("d", 1140, 540), ("bbar^o", 970, 530), ("b", 1200, 640), ("beta", 1405, 1120),
    ("y", 1708, 645), ("ybar", 1745, 1215), ("alpha", 809, 1065), ("ex", 1065, 555), ("xdots", 1710, 550),
    ("dotcross", 1275, 545), ("plus", 1097, 725), ("hash", 1457, 1288), ("tt", 1686, 1210), ("ttt", 1397, 1288),
    # sheet 2: c family, round and boxed signs, figures, small signs
    ("sigma", 1235, 535), ("moondot", 625, 1143), ("c", 720, 1061), ("e", 830, 1143), ("circdot", 673, 1143),
    ("theta", 630, 1061), ("o", 1588, 645), ("O", 1948, 1043), ("boxdot", 1033, 640), ("delta", 1622, 625),
    ("z", 1311, 645), ("2", 1939, 640), ("3", 1360, 545), ("3tail", 1089, 815), ("8", 2465, 550),
    ("odiv", 1777, 795), ("arch", 1331, 1126), ("gamma", 763, 805), ("r", 1425, 550), ("dollar", 867, 805),
    # sheet 3: marks above, capitals, the rest
    ("a^o", 1030, 540), ("p^tick", 1465, 540), ("t^wave", 1272, 630), ("8^3", 2160, 540), ("c^s", 1151, 1120),
    ("y^wave", 1323, 1048), ("w", 772, 640), ("w^bar", 2372, 782), ("f", 1185, 550), ("s", 930, 540),
    ("A", 733, 720), ("Lx", 1378, 800), ("dbbar", 1700, 715), ("h", 1505, 545), ("i", 1097, 645),
    ("R", 509, 2791), ("B", 1264, 964), ("m^o", 2100, 1200), ("n", 1228, 723), ("2^o", 701, 1140),
]


def main():
    out = os.path.join(crop.HERE, "sign-sheet")
    os.makedirs(out, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        full = os.path.join(tmp, "f.bmp")
        crop.sips("-s", "format", "bmp", os.path.join(crop.CACHE, SRC), "--out", full)
        W, H, rows = crop.read_bmp(full)
        per = COLS * ROWS
        white, black = b"\xff\xff\xff", b"\x00\x00\x00"
        for s in range(0, len(CELLS), per):
            cells = CELLS[s:s + per]
            sw, sh = COLS * CW + (COLS + 1) * GAP, ROWS * CH + (ROWS + 1) * GAP
            canvas = [bytearray(white * sw) for _ in range(sh)]
            for k, (name, cx, cy) in enumerate(cells):
                r, c = divmod(k, COLS)
                ox, oy = GAP + c * (CW + GAP), GAP + r * (CH + GAP)
                x0 = min(max(0, cx - CW // 2), W - CW)
                y0 = min(max(0, cy - CH // 2), H - CH)
                for dy in range(CH):
                    canvas[oy + dy][ox * 3:(ox + CW) * 3] = rows[y0 + dy][x0 * 3:(x0 + CW) * 3]
                for dy in range(12):                      # the tick: 3 px wide, 12 px high, top centre
                    for dx in (-1, 0, 1):
                        p = (ox + CW // 2 + dx) * 3
                        canvas[oy + dy][p:p + 3] = black
            bmp = os.path.join(tmp, "s.bmp")
            crop.write_bmp(bmp, [bytes(r) for r in canvas], 0, 0, sw, sh)
            n = s // per + 1
            crop.sips("-s", "format", "jpeg", "-s", "formatOptions", "90", "--resampleWidth", str(sw * SCALE),
                      bmp, "--out", os.path.join(out, "sheet-%d.jpg" % n))
            print("sheet-%d.jpg: %s" % (n, ", ".join(nm for nm, _, _ in cells)))


if __name__ == "__main__":
    main()

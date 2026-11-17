"""crop.py - cut the pages of item 2911 into overlapping reading strips (PIPELINE.md stage 2 preparation).

    python3 crop.py [--lines 4] [--step 3] [--only <page>] [--debug]

Run from this directory. Python standard library plus macOS `sips` (JPEG <-> BMP only; all geometry is done here).

For each page in PAGES:
  1. sips writes a small BMP (width ANALYSIS_W) and a full-size BMP to a temporary directory.
  2. On the small copy: find the paper (bright area), mark ink (pixels much darker than the paper), find the text
     block (rows and columns that carry ink), find the text lines (peaks of the smoothed row profile, spacing
     taken from its autocorrelation).
  3. Bands of `--lines` text lines, stepping `--step` lines, so that neighbouring bands share
     (lines - step) line(s). Each band is cut whole-width and as a left half 'a' and a right half 'b'
     that overlap by 10% of the text width. Cut at native resolution from the full BMP.
  4. Output cache/strips/<page>-<nn>.jpg (whole width), <page>-<nn>a.jpg, <page>-<nn>b.jpg, and strips.tsv:
     page, band, part, file, x0, y0, x1, y1 (pixel box in the page image, x1 and y1 exclusive), first_line, last_line
     (text lines counted by this script from 1; a count of ink rows, not an edition's line numbers).

The whole-width strip is for orientation (it is reduced on screen); the halves are the reading strips.
"""
import argparse, os, struct, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
OUT = os.path.join(CACHE, "strips")
ANALYSIS_W = 700

# page name -> source file. The page name is what readers and strips.tsv use.
PAGES = [
    ("V140-1r", "V_140_02_1r.jpg"),
    ("V140-1v", "V_140_03_1v.jpg"),
    ("V140-2r", "V_140_04_2r.jpg"),
    ("V139-1v", "V_139_03_1v.jpg"),
    ("V139-2r", "V_139_04_2r.jpg"),
    ("V134-1r", "V_134_136_02_1r.jpg"),
    ("V125-5r", "V_124_133_10_5r.jpg"),
]


def sips(*args):
    subprocess.run(["sips", *args], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def read_bmp(path):
    """-> (width, height, rows) with rows top-down, each a bytes object of width*3 (B, G, R)."""
    with open(path, "rb") as f:
        data = f.read()
    if data[:2] != b"BM":
        raise ValueError("not a BMP: " + path)
    off = struct.unpack_from("<I", data, 10)[0]
    w, h = struct.unpack_from("<ii", data, 18)
    bpp = struct.unpack_from("<H", data, 28)[0]
    comp = struct.unpack_from("<I", data, 30)[0]
    if bpp not in (24, 32) or comp not in (0, 3):
        raise ValueError("unsupported BMP (bpp %d, compression %d): %s" % (bpp, comp, path))
    topdown = h < 0
    h = abs(h)
    bpx = bpp // 8
    stride = (w * bpx + 3) & ~3
    rows = []
    for y in range(h):
        src = y if topdown else h - 1 - y
        row = data[off + src * stride: off + src * stride + w * bpx]
        if bpx == 4:
            row = bytes(b for i, b in enumerate(row) if i % 4 != 3)
        rows.append(row)
    return w, h, rows


def write_bmp(path, rows, x0, y0, x1, y1):
    w, h = x1 - x0, y1 - y0
    stride = (w * 3 + 3) & ~3
    pad = b"\0" * (stride - w * 3)
    body = b"".join(rows[y][x0 * 3:x1 * 3] + pad for y in range(y1 - 1, y0 - 1, -1))
    head = b"BM" + struct.pack("<IHHI", 54 + len(body), 0, 0, 54)
    info = struct.pack("<IiiHHIIiiII", 40, w, h, 1, 24, 0, len(body), 11811, 11811, 0, 0)  # 11811 px/m = 300 dpi
    with open(path, "wb") as f:
        f.write(head + info + body)


def luminance(rows, w):
    return [[(r[3 * x] * 11 + r[3 * x + 1] * 59 + r[3 * x + 2] * 30) // 100 for x in range(w)] for r in rows]


def smooth(v, k):
    k = max(1, k)
    out, n = [], len(v)
    acc = [0]
    for x in v:
        acc.append(acc[-1] + x)
    for i in range(n):
        a, b = max(0, i - k), min(n, i + k + 1)
        out.append((acc[b] - acc[a]) / (b - a))
    return out


def run_bounds(flags, min_gap):
    """First and last True index, after dropping isolated runs separated from the main mass by > min_gap."""
    runs, start = [], None
    for i, f in enumerate(list(flags) + [False]):
        if f and start is None:
            start = i
        elif not f and start is not None:
            runs.append([start, i])
            start = None
    if not runs:
        return None
    merged = [runs[0]]
    for a, b in runs[1:]:
        if a - merged[-1][1] <= min_gap:
            merged[-1][1] = b
        else:
            merged.append([a, b])
    best = max(merged, key=lambda r: r[1] - r[0])
    return best[0], best[1]


def analyse(lum, w, h):
    """-> dict with text box and line centres, in small-image pixels."""
    flat = sorted(v for row in lum[::4] for v in row[::4])
    paper = flat[int(len(flat) * 0.70)]                 # the paper is the bright majority
    bright = paper * 0.72
    # paper box: rows and columns that are mostly bright
    prow = [sum(1 for v in row if v > bright) / w > 0.5 for row in lum]
    pcol = [sum(1 for y in range(0, h, 2) if lum[y][x] > bright) / (h / 2) > 0.5 for x in range(w)]
    py0, py1 = run_bounds(prow, 3)
    px0, px1 = run_bounds(pcol, 3)
    inset = int(0.02 * w)
    py0, py1, px0, px1 = py0 + inset, py1 - inset, px0 + inset, px1 - inset
    ink_t = paper * 0.66
    ink = [[1 if (px0 <= x < px1 and py0 <= y < py1 and lum[y][x] < ink_t) else 0 for x in range(w)] for y in range(h)]
    rowp = [sum(r) for r in ink]
    # text rows: smoothed profile above a fraction of its upper level
    rs = smooth(rowp, 2)
    top = sorted(rs)[int(len(rs) * 0.90)]
    ty = run_bounds([v > 0.12 * top for v in rs], int(0.08 * h))
    ty0, ty1 = ty
    colp = [sum(ink[y][x] for y in range(ty0, ty1)) for x in range(w)]
    cs = smooth(colp, 3)
    ctop = sorted(cs)[int(len(cs) * 0.80)]
    tx0, tx1 = run_bounds([v > 0.20 * ctop for v in cs], int(0.04 * w))
    # line pitch by autocorrelation of the row profile inside the block
    seg = [sum(ink[y][tx0:tx1]) for y in range(ty0, ty1)]
    m = sum(seg) / len(seg)
    d = [v - m for v in seg]
    lo, hi = max(6, int(0.012 * h)), int(0.06 * h)
    best, pitch = None, lo
    for lag in range(lo, min(hi, len(d) // 2)):
        c = sum(d[i] * d[i + lag] for i in range(len(d) - lag)) / (len(d) - lag)
        if best is None or c > best:
            best, pitch = c, lag
    ss = smooth(seg, max(1, pitch // 5))
    peak_level = sorted(ss)[int(len(ss) * 0.85)]
    cand = [i for i in range(1, len(ss) - 1) if ss[i] >= ss[i - 1] and ss[i] > ss[i + 1] and ss[i] > 0.18 * peak_level]
    lines = []
    for i in sorted(cand, key=lambda i: -ss[i]):
        if all(abs(i - j) >= 0.6 * pitch for j in lines):
            lines.append(i)
    lines.sort()
    # a gap of more than 1.55 pitch that carries ink hides a missed line: fill it evenly
    filled = []
    for a, b in zip(lines, lines[1:]):
        filled.append(a)
        n = round((b - a) / pitch)
        if b - a > 1.55 * pitch and n >= 2:
            for q in range(1, n):
                y = a + (b - a) * q // n
                if max(ss[max(0, y - pitch // 3): y + pitch // 3 + 1]) > 0.10 * peak_level:
                    filled.append(y)
    filled.append(lines[-1])
    lines = [ty0 + i for i in filled]
    return {"paper": (px0, py0, px1, py1), "text": (tx0, ty0, tx1, ty1), "pitch": pitch, "lines": lines}


def bands(lines, pitch, nlines, step):
    """-> list of (first_line, last_line, y0, y1), lines counted from 1; y in small-image pixels (float)."""
    out, i, n = [], 0, len(lines)
    while True:
        j = min(i + nlines, n) - 1
        if j == n - 1 and n >= nlines:
            i = n - nlines if out else i          # last band: keep the full height, slide up
            i = max(i, (out[-1][0] - 1 + 1) if out else 0)
        out.append((i + 1, j + 1, lines[i] - 0.85 * pitch, lines[j] + 0.85 * pitch))
        if j == n - 1:
            return out
        i += step


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--lines", type=int, default=4)
    ap.add_argument("--step", type=int, default=3)
    ap.add_argument("--only")
    ap.add_argument("--debug", action="store_true", help="print the analysis, write nothing")
    a = ap.parse_args(argv)
    os.makedirs(OUT, exist_ok=True)
    rows_out = []
    with tempfile.TemporaryDirectory() as tmp:
        for page, src in PAGES:
            if a.only and a.only != page:
                continue
            srcp = os.path.join(CACHE, src)
            small, full = os.path.join(tmp, "s.bmp"), os.path.join(tmp, "f.bmp")
            sips("-s", "format", "bmp", "--resampleWidth", str(ANALYSIS_W), srcp, "--out", small)
            sips("-s", "format", "bmp", srcp, "--out", full)
            sw, sh, srows = read_bmp(small)
            info = analyse(luminance(srows, sw), sw, sh)
            W, H, frows = read_bmp(full)
            k = W / sw
            tx0, ty0, tx1, ty1 = info["text"]
            print("%s: page %dx%d, text box x %d-%d y %d-%d, pitch %.0f px, %d lines" % (
                page, W, H, tx0 * k, tx1 * k, ty0 * k, ty1 * k, info["pitch"] * k, len(info["lines"])), file=sys.stderr)
            if a.debug:
                print("  line centres (y, px):", [round(y * k) for y in info["lines"]], file=sys.stderr)
                continue
            pad = 0.04 * W
            X0, X1 = max(0, int(tx0 * k - pad)), min(W, int(tx1 * k + pad))
            tw = X1 - X0
            parts = [("", X0, X1), ("a", X0, X0 + int(0.55 * tw)), ("b", X0 + int(0.45 * tw), X1)]
            bmps = []
            for n, (l0, l1, y0, y1) in enumerate(bands(info["lines"], info["pitch"], a.lines, a.step), 1):
                Y0, Y1 = max(0, int(y0 * k)), min(H, int(y1 * k))
                for part, xa, xb in parts:
                    name = "%s-%02d%s" % (page, n, part)
                    write_bmp(os.path.join(tmp, name + ".bmp"), frows, xa, Y0, xb, Y1)
                    bmps.append(name)
                    rows_out.append((page, n, part or "full", "cache/strips/%s.jpg" % name, xa, Y0, xb, Y1, l0, l1))
            for name in bmps:
                sips("-s", "format", "jpeg", "-s", "formatOptions", "92",
                     os.path.join(tmp, name + ".bmp"), "--out", os.path.join(OUT, name + ".jpg"))
                os.remove(os.path.join(tmp, name + ".bmp"))
    if a.debug:
        return
    tsv = os.path.join(HERE, "strips.tsv")
    old = []
    if a.only and os.path.exists(tsv):
        with open(tsv) as f:
            old = [ln.rstrip("\n").split("\t") for ln in f.readlines()[1:] if not ln.startswith(a.only + "\t")]
    order = {p: i for i, (p, _) in enumerate(PAGES)}
    allrows = sorted(old + [[str(v) for v in r] for r in rows_out], key=lambda r: (order.get(r[0], 99), int(r[1]), r[2] != "full", r[2]))
    with open(tsv, "w") as f:
        f.write("page\tband\tpart\tfile\tx0\ty0\tx1\ty1\tfirst_line\tlast_line\n")
        for r in allrows:
            f.write("\t".join(r) + "\n")
    counts = {}
    for r in allrows:
        counts[r[0]] = counts.get(r[0], 0) + 1
    for p, _ in PAGES:
        if p in counts:
            print("%s\t%d strips (%d bands)" % (p, counts[p], counts[p] // 3))


if __name__ == "__main__":
    main()

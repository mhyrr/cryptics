"""sign_height.py - measure sign height in pixels on a page image (the "Readable" gate, METHOD "What you need").

    python3 -I sign_height.py page.jpg [--box W,H,X,Y] [--minarea 6]

Converts the image (or the box cut from it) to greyscale PGM with ImageMagick `magick`, binarizes at Otsu's
threshold, labels 8-connected ink components and reports:
  comps       number of components kept (area >= minarea, height and width under 1/4 of the box)
  h_median    median component height in px: the sign height
  h_p25/p75   quartiles
  h_median_a30  median height of components of 30 px area or more: drops dots and specks, which pull
              h_median down on numeral ciphers with separating dots (no. 649, no. 2395 doc. 733).
              Report both; the gate reads h_median_a30 when dots are part of the script, and says so.
  line_pitch  median distance between line centres from the row ink profile (px), if lines are found
Components are signs, parts of signs, or ligatures; the median is the figure the gate uses (15 px or more).
Give --box round the cipher block so that clear text, margins and stains do not count.
Output is one tab-separated line with a header.
"""
import subprocess, sys, statistics


def load_pgm(path, box=None):
    cmd = ["magick", path]
    if box:
        w, h, x, y = box
        cmd += ["-crop", f"{w}x{h}+{x}+{y}", "+repage"]
    cmd += ["-colorspace", "Gray", "-depth", "8", "pgm:-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    # P5 header: magic, width, height, maxval, each separated by whitespace
    parts, i = [], 0
    while len(parts) < 4:
        while raw[i:i + 1].isspace() or raw[i:i + 1] == b"#":
            if raw[i:i + 1] == b"#":          # header comment, runs to end of line
                while raw[i:i + 1] not in (b"\n", b""):
                    i += 1
            i += 1
        j = i
        while not raw[j:j + 1].isspace():
            j += 1
        parts.append(raw[i:j])
        i = j
    i += 1
    w, h = int(parts[1]), int(parts[2])
    return w, h, raw[i:i + w * h]


def otsu(px):
    hist = [0] * 256
    for v in px:
        hist[v] += 1
    total, sum_all = len(px), sum(i * c for i, c in enumerate(hist))
    best, t_best, wb, sb = -1, 128, 0, 0
    for t in range(256):
        wb += hist[t]
        if wb == 0 or wb == total:
            continue
        sb += t * hist[t]
        mb, mf = sb / wb, (sum_all - sb) / (total - wb)
        between = wb * (total - wb) * (mb - mf) ** 2
        if between > best:
            best, t_best = between, t
    return t_best


def components(w, h, ink):
    parent = list(range(w * h))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for y in range(h):
        row = y * w
        for x in range(w):
            p = row + x
            if not ink[p]:
                continue
            for q in ((p - 1) if x > 0 else -1, (p - w - 1) if x > 0 and y > 0 else -1,
                      (p - w) if y > 0 else -1, (p - w + 1) if y > 0 and x < w - 1 else -1):
                if q >= 0 and ink[q]:
                    ra, rb = find(p), find(q)
                    if ra != rb:
                        parent[ra] = rb
    boxes = {}
    for p in range(w * h):
        if ink[p]:
            r = find(p)
            y, x = divmod(p, w)
            b = boxes.get(r)
            if b is None:
                boxes[r] = [x, y, x, y, 1]
            else:
                b[0] = min(b[0], x); b[1] = min(b[1], y); b[2] = max(b[2], x); b[3] = max(b[3], y); b[4] += 1
    return boxes.values()


def line_pitch(w, h, ink):
    prof = [sum(ink[y * w:(y + 1) * w]) for y in range(h)]
    if not prof or max(prof) == 0:
        return None
    k = 3
    sm = [sum(prof[max(0, i - k):i + k + 1]) / (2 * k + 1) for i in range(h)]
    thr = 0.3 * max(sm)
    peaks, inband, start = [], False, 0
    for i, v in enumerate(sm + [0]):
        if v >= thr and not inband:
            inband, start = True, i
        elif v < thr and inband:
            inband = False
            peaks.append((start + i) / 2)
    gaps = [b - a for a, b in zip(peaks, peaks[1:])]
    return statistics.median(gaps) if gaps else None


def main(argv):
    path = argv[0]
    box = None
    minarea = 6
    if "--box" in argv:
        box = tuple(int(v) for v in argv[argv.index("--box") + 1].split(","))
    if "--minarea" in argv:
        minarea = int(argv[argv.index("--minarea") + 1])
    w, h, px = load_pgm(path, box)
    t = otsu(px)
    ink = bytearray(1 if v <= t else 0 for v in px)
    hs, big = [], []
    for x0, y0, x1, y1, area in components(w, h, ink):
        ch, cw = y1 - y0 + 1, x1 - x0 + 1
        if area >= minarea and ch < h / 4 and cw < w / 4:
            hs.append(ch)
            if area >= 30:
                big.append(ch)
    hs.sort()
    q = (lambda f: hs[int(f * (len(hs) - 1))]) if hs else (lambda f: 0)
    lp = line_pitch(w, h, ink)
    print("image\tbox\twidth\theight\totsu\tcomps\th_median\th_p25\th_p75\th_median_a30\tline_pitch")
    print(f"{path}\t{','.join(map(str, box)) if box else 'full'}\t{w}\t{h}\t{t}\t{len(hs)}\t"
          f"{statistics.median(hs) if hs else 0}\t{q(0.25)}\t{q(0.75)}\t{statistics.median(big) if big else 0}\t{lp if lp else ''}")


if __name__ == "__main__":
    main(sys.argv[1:])

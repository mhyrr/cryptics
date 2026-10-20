"""Parse saved search pages into dated hit tables, and day lists into article counts.

Usage:
  python3 -I parse.py DATA OUTDIR

Writes:
  OUTDIR/sillok_hits.tsv      one row per (term, Sillok article)
  OUTDIR/ming_hits.tsv        one row per (term, Ming Shilu article)
  OUTDIR/sillok_articles.tsv  articles per lunar month, for the fetched windows
  OUTDIR/calendar_check.txt   how well the date conversion matches the record

Date conversion (stated method):
  * Lunar year Y (Western label from the Sillok month lists, or Ming era + n - 1).
  * Month 11 of year Y-1 is the lunar month that contains the winter solstice.
    New moons and the solstice are computed astronomically (Meeus, Astronomical
    Algorithms, ch. 25 and 49) for local time UTC+8.
  * Month 1 of Y starts two lunations later, three if year Y-1 had a leap 11th or
    12th month. Each later month, leap months included, adds one lunation. Leap
    months come from the Sillok month lists (the Joseon court used the Ming
    calendar); Ming dates use the same leap months.
  * Day d is month start + d - 1. For Sillok rows the record's sexagenary day
    (ganzhi) then fixes the exact Julian Day: the JD with that ganzhi nearest the
    estimate. The residual (estimate minus fixed) is a check on the method.
  * Western dates are given in the Julian calendar before 1582-10-15 and the
    Gregorian after, plus proleptic Gregorian for every row (for season).
"""
import glob, gzip, math, os, re, sys, collections

STEMS = "甲乙丙丁戊己庚辛壬癸"
BRANCH = "子丑寅卯辰巳午未申酉戌亥"
HSTEMS = "갑을병정무기경신임계"
HBRANCH = "자축인묘진사오미신유술해"
KINGS = {"태조실록": "kaa", "정종실록": "kba", "태종실록": "kca", "세종실록": "kda", "문종실록": "kea",
         "단종실록": "kfa", "세조실록": "kga", "예종실록": "kha", "성종실록": "kia", "연산군일기": "kja",
         "중종실록": "kka", "인종실록": "kla", "명종실록": "kma", "선조실록": "kna", "선조수정실록": "knb",
         "광해군중초본": "koa", "광해군정초본": "kob", "인조실록": "kpa", "효종실록": "kqa", "현종실록": "kra",
         "현종개수실록": "krb", "숙종실록": "ksa", "숙종보궐정오": "ksb", "경종실록": "kta", "경종수정실록": "ktb",
         "영조실록": "kua", "정조실록": "kva", "순조실록": "kwa", "헌종실록": "kxa", "철종실록": "kya",
         "고종실록": "kza", "순종실록": "kzb", "순종실록부록": "kzc"}
ERAS = {"洪武": 1368, "建文": 1399, "永樂": 1403, "洪熙": 1425, "宣德": 1426, "正統": 1436, "景泰": 1450,
        "天順": 1457, "成化": 1465, "弘治": 1488, "正德": 1506, "嘉靖": 1522, "隆慶": 1567, "萬曆": 1573,
        "泰昌": 1620, "天啓": 1621, "天啟": 1621, "崇禎": 1628}
NUM = {"元": 1, "正": 1, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}


def cnum(s):
    s = s.replace("廿", "二十").replace("卅", "三十")
    if s in NUM:
        return NUM[s]
    if "十" in s:
        a, b = s.split("十", 1)
        return (NUM[a] if a else 1) * 10 + (NUM[b] if b else 0)
    raise ValueError(s)


def ganzhi_index(s):
    if len(s) != 2:
        return None
    if s[0] in STEMS and s[1] in BRANCH:
        a, b = STEMS.index(s[0]), BRANCH.index(s[1])
    elif s[0] in HSTEMS and s[1] in HBRANCH:
        a, b = HSTEMS.index(s[0]), HBRANCH.index(s[1])
    else:
        return None
    for n in range(60):
        if n % 10 == a and n % 12 == b:
            return n


def jd_ganzhi(jdn):  # 0 = 甲子; JDN 2433191 (1949-10-01) is 甲子
    return (jdn - 11) % 60


# --- astronomy (Meeus) ---------------------------------------------------
def new_moon_jde(k):
    T = k / 1236.85
    jde = 2451550.09766 + 29.530588861 * k + 0.00015437 * T * T - 0.00000015 * T ** 3
    E = 1 - 0.002516 * T - 0.0000074 * T * T
    M = math.radians(2.5534 + 29.10535670 * k - 0.0000014 * T * T)
    Mp = math.radians(201.5643 + 385.81693528 * k + 0.0107582 * T * T)
    F = math.radians(160.7108 + 390.67050284 * k - 0.0016118 * T * T)
    O = math.radians(124.7746 - 1.56375588 * k + 0.0020672 * T * T)
    c = (-0.40720 * math.sin(Mp) + 0.17241 * E * math.sin(M) + 0.01608 * math.sin(2 * Mp)
         + 0.01039 * math.sin(2 * F) + 0.00739 * E * math.sin(Mp - M) - 0.00514 * E * math.sin(Mp + M)
         + 0.00208 * E * E * math.sin(2 * M) - 0.00111 * math.sin(Mp - 2 * F) - 0.00057 * math.sin(Mp + 2 * F)
         + 0.00056 * E * math.sin(2 * Mp + M) - 0.00042 * math.sin(3 * Mp) + 0.00042 * E * math.sin(M + 2 * F)
         + 0.00038 * E * math.sin(M - 2 * F) - 0.00024 * E * math.sin(2 * Mp - M) - 0.00017 * math.sin(O))
    return jde + c


def sun_long(jde):
    T = (jde - 2451545.0) / 36525
    L0 = 280.46646 + 36000.76983 * T + 0.0003032 * T * T
    M = math.radians(357.52911 + 35999.05029 * T - 0.0001537 * T * T)
    C = ((1.914602 - 0.004817 * T - 0.000014 * T * T) * math.sin(M) + (0.019993 - 0.000101 * T) * math.sin(2 * M)
         + 0.000289 * math.sin(3 * M))
    O = math.radians(125.04 - 1934.136 * T)
    return (L0 + C - 0.00569 - 0.00478 * math.sin(O)) % 360


def delta_t_days(year):  # rough Morrison-Stephenson style; minutes only matter here
    u = (year - 1820) / 100
    return (-20 + 32 * u * u) / 86400


def local_day(jde, year):  # civil day number (JDN) at UTC+8
    return math.floor(jde - delta_t_days(year) + 8 / 24 + 0.5)


def winter_solstice_day(year):
    jd = julian_to_jdn(year, 12, 12) - 0.5
    for _ in range(50):
        d = ((270 - sun_long(jd) + 180) % 360) - 180
        if abs(d) < 1e-6:
            break
        jd += d / 360 * 365.2422
    return local_day(jd, year)


def new_moon_on_or_before(day, year):
    k = math.floor((day - 2451550.1) / 29.530588861) + 1
    while local_day(new_moon_jde(k), year) > day:
        k -= 1
    while local_day(new_moon_jde(k + 1), year) <= day:
        k += 1
    return k


def julian_to_jdn(y, m, d):
    a = (14 - m) // 12
    y2, m2 = y + 4800 - a, m + 12 * a - 3
    return d + (153 * m2 + 2) // 5 + 365 * y2 + y2 // 4 - 32083


def jdn_to_julian(j):
    c = j + 32082
    d = (4 * c + 3) // 1461
    e = c - 1461 * d // 4
    m = (5 * e + 2) // 153
    return d - 4800 + m // 10, m + 3 - 12 * (m // 10), e - (153 * m + 2) // 5 + 1


def jdn_to_greg(j):
    a = j + 32044
    b = (4 * a + 3) // 146097
    c = a - 146097 * b // 4
    d = (4 * c + 3) // 1461
    e = c - 1461 * d // 4
    m = (5 * e + 2) // 153
    return 100 * b + d - 4800 + m // 10, m + 3 - 12 * (m // 10), e - (153 * m + 2) // 5 + 1


def fmt(t):
    return "%04d-%02d-%02d" % t


# --- calendar from Sillok month lists -------------------------------------
def load_months(data):
    """reign map (code, reign_year) -> Western lunar year; leap months per lunar year."""
    reign, leaps = {}, collections.defaultdict(set)
    for f in glob.glob(os.path.join(data, "raw", "months", "*.html.gz")):
        code = os.path.basename(f)[:3]
        t = gzip.open(f).read().decode("utf-8")
        for block in re.split(r'<div class="month-title">', t)[1:]:
            m = re.search(r"<span>(\d{4})년", block)
            if not m:
                continue
            wy = int(m.group(1))
            for mid in re.findall(code + r"_(\d{6})(?!\d)", block):
                ry, mo, lp = int(mid[1:3]), int(mid[3:5]), mid[5] == "1"
                reign[(code, ry)] = wy
                if lp:
                    leaps[wy].add(mo)
    return reign, leaps


def month_start(year, month, leap, leaps):
    ws = winter_solstice_day(year - 1)
    k11 = new_moon_on_or_before(ws, year - 1)
    k = k11 + 2 + len([m for m in leaps.get(year - 1, ()) if m >= 11])
    for mo in range(1, month):
        k += 1 + (1 if mo in leaps.get(year, ()) else 0)
    if leap:
        k += 1
    return local_day(new_moon_jde(k), year)


def convert(year, month, leap, day, gz, leaps):
    est = month_start(year, month, leap, leaps) + day - 1
    jd, resid = est, ""
    if gz is not None:
        off = (gz - jd_ganzhi(est) + 30) % 60 - 30
        jd = est + off
        resid = str(-off)
    cal = jdn_to_julian(jd) if jd < 2299161 else jdn_to_greg(jd)
    return jd, fmt(cal), fmt(jdn_to_greg(jd)), resid


# --- page parsers -----------------------------------------------------------
def clean(s):
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip().replace("\t", " ")


def parse_sillok(data, reign, leaps, out):
    rows, bad = [], collections.Counter()
    for f in sorted(glob.glob(os.path.join(data, "raw", "search", "w_*.html.gz"))):
        term = bytes.fromhex(os.path.basename(f).split("_")[1]).decode("utf-8")
        t = gzip.open(f).read().decode("utf-8")
        for m in re.finditer(r"goView\('([^']+)'[^>]*class=\"subject\">(.*?)</a>\s*<p class=\"text\">(.*?)</p>", t, re.S):
            aid, subj, snip = m.group(1), clean(m.group(2)), clean(m.group(3))
            s = re.match(r"\d+\. (\S+) (\d+)권, \S+ (즉위년|\d+년) (윤?)(\d+)월 (\d+)일 (\S{2}) (\d+)번째기사 / (.*)", subj)
            if not s:
                bad["undated"] += 1
                continue
            book, vol, ry, lp, mo, dy, gz, num, title = s.groups()
            code = KINGS.get(book)
            ry = 0 if ry == "즉위년" else int(ry[:-1])
            wy = reign.get((code, ry))
            if wy is None:
                bad["no-year"] += 1
                continue
            g = ganzhi_index(gz)
            jd, wdate, gdate, resid = convert(wy, int(mo), lp == "윤", int(dy), g, leaps)
            rows.append([term, aid, book, vol, str(ry), ("윤" if lp else "") + mo, dy, gz, num, str(wy),
                         str(jd), wdate, gdate, resid, title, snip])
    hdr = ["term", "id", "book", "vol", "reign_year", "month", "day", "ganzhi", "article_no", "lunar_year",
           "jdn", "date_western", "date_greg_proleptic", "ganzhi_residual_days", "title_ko", "snippet"]
    with open(os.path.join(out, "sillok_hits.tsv"), "w", encoding="utf-8") as f:
        f.write("\t".join(hdr) + "\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    return rows, bad


def parse_ming(data, leaps, out):
    rows, bad = [], collections.Counter()
    for f in sorted(glob.glob(os.path.join(data, "raw", "search", "m_*.html.gz"))):
        term = bytes.fromhex(os.path.basename(f).split("_")[1]).decode("utf-8")
        t = gzip.open(f).read().decode("utf-8")
        for m in re.finditer(r"goView\('([^']+)'[^>]*class=\"subject\">(.*?)</a>\s*<p class=\"text\">(.*?)</p>", t, re.S):
            aid, subj, snip = m.group(1), clean(m.group(2)), clean(m.group(3))
            s = re.match(r"\d+\. (\S+實錄) (卷\S+) (\S\S)(\S+)年 (閏?)(\S+)月 (\S+)日 (\d+)번째 기사 / (.*)", subj)
            if not s or s.group(3) not in ERAS:
                bad["undated"] += 1
                continue
            book, vol, era, ey, lp, mo, dy, num, lead = s.groups()
            try:
                wy = ERAS[era] + cnum(ey) - 1
                mo_n, dy_n = cnum(mo), cnum(dy)
            except (ValueError, KeyError):
                bad["numeral"] += 1
                continue
            g = re.match(r"[○△]\s*(?:朔)?([甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥])", lead)
            jd, wdate, gdate, _ = convert(wy, mo_n, lp == "閏", dy_n, None, leaps)
            check = ""
            if g:
                check = str((ganzhi_index(g.group(1)) - jd_ganzhi(jd) + 30) % 60 - 30)
            rows.append([term, aid, book, vol, era + ey, ("閏" if lp else "") + mo, dy, num, str(wy), str(jd),
                         wdate, gdate, check, lead, snip])
    hdr = ["term", "id", "book", "vol", "era_year", "month", "day", "article_no", "lunar_year", "jdn",
           "date_western", "date_greg_proleptic", "lead_ganzhi_minus_computed_days", "lead", "snippet"]
    with open(os.path.join(out, "ming_hits.tsv"), "w", encoding="utf-8") as f:
        f.write("\t".join(hdr) + "\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    return rows, bad


def parse_days(data, reign, out):
    n = collections.Counter()
    for f in glob.glob(os.path.join(data, "raw", "days", "*.html.gz")):
        b = os.path.basename(f)
        code, mid = b[:3], b[4:10]
        t = gzip.open(f).read().decode("utf-8")
        ids = set(re.findall(code + "_" + mid[:5] + r"\d{3}_\d{3}", t))
        wy = reign.get((code, int(mid[1:3])))
        n[(code, wy, mid)] = len(ids)
    with open(os.path.join(out, "sillok_articles.tsv"), "w", encoding="utf-8") as f:
        f.write("code\tlunar_year\tmonth_id\tarticles\n")
        for k in sorted(n, key=lambda k: (k[1], k[2])):
            f.write("%s\t%s\t%s\t%d\n" % (k[0], k[1], k[2], n[k]))


if __name__ == "__main__":
    data, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    reign, leaps = load_months(data)
    srows, sbad = parse_sillok(data, reign, leaps, out)
    mrows, mbad = parse_ming(data, leaps, out)
    parse_days(data, reign, out)
    res = collections.Counter(r[13] for r in srows)
    mres = collections.Counter(r[12] for r in mrows if r[12] != "")
    with open(os.path.join(out, "calendar_check.txt"), "w", encoding="utf-8") as f:
        f.write("Sillok rows: %d; skipped: %s\n" % (len(srows), dict(sbad)))
        f.write("Sillok: estimated day minus ganzhi-fixed day (days): count\n")
        for k in sorted(res, key=lambda x: int(x) if x else 99):
            f.write("  %s: %d\n" % (k, res[k]))
        f.write("Ming rows: %d; skipped: %s\n" % (len(mrows), dict(mbad)))
        f.write("Ming: leading ganzhi in text minus computed day (days), rows that have one: count\n")
        for k in sorted(mres, key=int):
            f.write("  %s: %d\n" % (k, mres[k]))
        # spot check against the record's own Western year label and a known date
        f.write("Spot check: Danjong 1/1/1 己未 ->  %s\n" % (convert(1453, 1, False, 1, ganzhi_index("己未"), leaps),))
    print(open(os.path.join(out, "calendar_check.txt"), encoding="utf-8").read())

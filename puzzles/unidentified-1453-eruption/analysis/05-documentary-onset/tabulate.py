"""Count weather notices per lunar year and compare target years with baselines.

Usage:
  python3 -I tabulate.py OUTDIR > results/tabulate.txt

Reads OUTDIR/sillok_hits.tsv, OUTDIR/sillok_articles.tsv, OUTDIR/ming_hits.tsv
(written by parse.py).

A Sillok "notice" in category C is an article whose Korean title (the modern
translators' one-line summary) matches C's title pattern AND whose classical
Chinese snippet matches C's text pattern. Each article counts once per category.
Rates are per 1,000 articles in that lunar year (all articles, from the day lists).

For each target window the script reports observed notices, the count expected
from the baseline rate, a one-sided Poisson p-value P(X >= observed), and the
target rate as a z-score against the baseline years' rates.

Ming Shilu has no translated titles. A Ming "cold report" is an article whose
snippet matches COLD_ZH and is not only a metaphor (see MING_EXCLUDE). Ming counts
are raw (no article totals were fetched), so they compare years within one reign.
"""
import collections, csv, math, os, re, sys

CATS = {
    "snow": (r"눈[이과비을]|비와 눈|눈비|우설|대설|큰 눈", r"雪"),
    "frost": (r"서리", r"霜"),
    "hail": (r"우박", r"雹"),
    "dust_haze": (r"흙비|토우|황사|풍매|흙[이가]|매[가우]", r"霾|雨土|黃霧"),
    "fog_gloom": (r"안개|어둡|어두|캄캄|침침|자욱", r"霧|晦冥|昏"),
    "sun_dim_red": (r"(해|햇빛|일광|일색|햇볕)[^,.]{0,10}(붉|빛이 없|어둡|어두|흐리|희미|광채|빛을 잃)|해가 빛",
                    r"日色|日無光|日赤|無光|日光"),
    "red_vapour": (r"붉은 기운|적기", r"赤氣"),  # mostly night-sky (auroral) records, kept apart
    "cold_freeze": (r"춥|추위|추워|추웠|얼어|얼음|동사|한기|차가", r"凍|寒|冷|氷|冰|霜|雪"),
    "halo_control": (r"햇무리|일훈", r"暈"),
    "white_rainbow": (r"흰 무지개|백홍", r"白虹"),
}

COLD_ZH = r"大雪|積雪|雨雪|凍死|凍餓|凍餒|冰結|氷結|隆寒|嚴寒|寒沍|沍寒|大寒|隕霜|霜災|被霜|霜殺|殺稼|木冰|木氷|木稼|寒如冬|冰不解|氷猶不解|恒寒|恆寒|雪雹|風雪"
MING_EXCLUDE = r"雪冤|伸雪|昭雪|未雪|雪其|雪兒|雪山|寒心|饑寒|飢寒|寒微|寒素|寒士|貧寒|禦寒|冬寒艱"

# (label, target lunar years, baseline lunar years)
WINDOWS = [
    ("UE1453: 1452", [1452], list(range(1446, 1452)) + list(range(1455, 1461))),
    ("UE1453: 1453", [1453], list(range(1446, 1452)) + list(range(1455, 1461))),
    ("UE1453: 1454", [1454], list(range(1446, 1452)) + list(range(1455, 1461))),
    ("UE1453: 1453-54", [1453, 1454], list(range(1446, 1452)) + list(range(1455, 1461))),
    ("UE1453: 1453-54 vs pre-only 1440-51", [1453, 1454], list(range(1440, 1452))),
    ("Kuwae 1458: 1459", [1459], list(range(1446, 1452)) + list(range(1461, 1466))),
    ("Huaynaputina Feb 1600: 1600", [1600], list(range(1595, 1600)) + list(range(1602, 1607))),
    ("Huaynaputina Feb 1600: 1601", [1601], list(range(1595, 1600)) + list(range(1602, 1607))),
    ("Komagatake Jul 1640 / Parker Jan 1641: 1641", [1641], list(range(1636, 1640)) + list(range(1643, 1647))),
    ("Komagatake Jul 1640 / Parker Jan 1641: 1642", [1642], list(range(1636, 1640)) + list(range(1643, 1647))),
    ("Laki/Asama 1783: 1783", [1783], list(range(1779, 1783)) + list(range(1785, 1789))),
    ("Laki/Asama 1783: 1784", [1784], list(range(1779, 1783)) + list(range(1785, 1789))),
    ("Tambora Apr 1815: 1815", [1815], list(range(1810, 1815)) + list(range(1817, 1821))),
    ("Tambora Apr 1815: 1816", [1816], list(range(1810, 1815)) + list(range(1817, 1821))),
]


def poisson_sf(k, lam):  # P(X >= k)
    if k <= 0:
        return 1.0
    term, cdf = math.exp(-lam), 0.0
    for i in range(k):
        cdf += term
        term *= lam / (i + 1)
    return max(0.0, 1 - cdf)


def read(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def main(out):
    hits = read(os.path.join(out, "sillok_hits.tsv"))
    arts = collections.Counter()
    for r in read(os.path.join(out, "sillok_articles.tsv")):
        if r["lunar_year"] != "None":
            arts[int(r["lunar_year"])] += int(r["articles"])
    notices = {c: collections.defaultdict(dict) for c in CATS}
    for r in hits:
        for c, (tk, tz) in CATS.items():
            if re.search(tk, r["title_ko"]) and re.search(tz, r["snippet"]):
                notices[c][int(r["lunar_year"])][r["id"]] = r

    print("# Sillok weather notices per lunar year (title AND text pattern), per 1,000 articles\n")
    years = sorted(y for y in arts if arts[y] > 0)
    print("year  articles  " + "  ".join("%13s" % c for c in CATS))
    for y in years:
        print("%4d  %8d  " % (y, arts[y]) + "  ".join(
            "%5d (%5.1f)" % (len(notices[c][y]), 1000 * len(notices[c][y]) / arts[y]) for c in CATS))

    print("\n# Target vs baseline (Poisson on article-normalised baseline rate; z on yearly rates)\n")
    for label, tgt, base in WINDOWS:
        base = [y for y in base if arts.get(y)]
        if not base or not all(arts.get(y) for y in tgt):
            print("%s: no article counts for some years, skipped" % label)
            continue
        print("## %s   (target %s, %d articles; baseline %d-%d, %d yrs)" % (
            label, tgt, sum(arts[y] for y in tgt), min(base), max(base), len(base)))
        for c in CATS:
            obs = sum(len(notices[c][y]) for y in tgt)
            bn = sum(len(notices[c][y]) for y in base)
            ba = sum(arts[y] for y in base)
            lam = bn / ba * sum(arts[y] for y in tgt)
            rates = [1000 * len(notices[c][y]) / arts[y] for y in base]
            mu = sum(rates) / len(rates)
            sd = (sum((x - mu) ** 2 for x in rates) / max(1, len(rates) - 1)) ** 0.5
            tr = 1000 * obs / sum(arts[y] for y in tgt)
            z = (tr - mu) / sd if sd > 0 else float("nan")
            flag = " <-- p<0.05" if poisson_sf(obs, lam) < 0.05 else ""
            print("  %-14s obs %3d  exp %6.1f  p(>=obs) %.3g  rate %5.1f vs base %5.1f±%4.1f  z %5.2f%s" % (
                c, obs, lam, poisson_sf(obs, lam), tr, mu, sd, z, flag))
        print()

    print("# Whole-dynasty raw notice counts (no normalisation): rank of each year, 1392-1863\n")
    for c in ["snow", "frost", "cold_freeze", "sun_dim_red", "red_vapour", "dust_haze", "fog_gloom"]:
        per = {y: len(v) for y, v in notices[c].items() if 1392 <= y <= 1863}
        allyears = range(1392, 1864)
        ranked = sorted(allyears, key=lambda y: -per.get(y, 0))
        rank = {y: i + 1 for i, y in enumerate(ranked)}
        show = [1452, 1453, 1454, 1459, 1600, 1601, 1641, 1642, 1783, 1784, 1815, 1816]
        print("  %-12s top: %s" % (c, ", ".join("%d:%d" % (y, per.get(y, 0)) for y in ranked[:8])))
        print("  %-12s     " % "" + ", ".join("%d:%d (rank %d)" % (y, per.get(y, 0), rank[y]) for y in show))

    print("\n# Sillok notices in lunar years 1452-1455, every category, chronological\n")
    seen = {}
    for c in CATS:
        for y in (1452, 1453, 1454, 1455):
            for aid, r in notices[c][y].items():
                seen.setdefault(aid, (r, []))[1].append(c)
    for aid, (r, cs) in sorted(seen.items(), key=lambda kv: int(kv[1][0]["jdn"])):
        print("  %s  %s  %s/%s/%s %s  [%s]  %s | %s" % (
            r["date_western"], aid, r["reign_year"], r["month"], r["day"], r["ganzhi"], ",".join(cs),
            r["title_ko"], r["snippet"][:90]))

    ming = read(os.path.join(out, "ming_hits.tsv"))
    byid = {}
    for r in ming:
        if re.search(COLD_ZH, r["snippet"]):
            s = re.sub(MING_EXCLUDE, "", r["snippet"])
            if re.search(COLD_ZH, s):
                byid[r["id"]] = r
    per = collections.Counter(int(r["lunar_year"]) for r in byid.values())
    print("\n# Ming Shilu cold/snow reports (raw article counts, COLD_ZH minus metaphors)\n")
    for lo, hi in [(1436, 1464), (1595, 1606), (1636, 1644)]:
        print("  " + " ".join("%d:%d" % (y, per.get(y, 0)) for y in range(lo, hi + 1)))
    for label, tgt, base in [("1453-54 vs 1436-51 & 1455-64", [1453, 1454], list(range(1436, 1452)) + list(range(1455, 1465))),
                             ("1601 vs 1595-99 & 1602-06", [1601], list(range(1595, 1600)) + list(range(1602, 1607))),
                             ("1641-42 vs 1636-39 & 1643-44", [1641, 1642], list(range(1636, 1640)) + [1643, 1644])]:
        obs = sum(per.get(y, 0) for y in tgt)
        lam = sum(per.get(y, 0) for y in base) / len(base) * len(tgt)
        print("  %-30s obs %3d  exp %5.1f  p(>=obs) %.3g" % (label, obs, lam, poisson_sf(obs, lam)))
    print("\n# Ming cold/snow reports, lunar years 1452-1455\n")
    for r in sorted((r for r in byid.values() if 1452 <= int(r["lunar_year"]) <= 1455), key=lambda r: int(r["jdn"])):
        print("  %s  %s  %s %s月%s日  %s" % (r["date_western"], r["id"], r["era_year"], r["month"], r["day"],
                                          r["snippet"][:110]))


if __name__ == "__main__":
    main(sys.argv[1])

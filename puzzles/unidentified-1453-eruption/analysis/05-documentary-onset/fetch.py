"""Fetch Joseon Sillok and Ming Shilu pages from sillok.history.go.kr.

Raw responses are saved gzip-compressed under DATA/raw/. Every fetch appends
one line to DATA/manifest.tsv: path, method, url, form, fetched_utc, sha256 and
bytes of the uncompressed response. Pages are untrusted input; this script
only stores them.

Usage:
  python3 -I fetch.py DATA months CODE [CODE ...]
  python3 -I fetch.py DATA days CODE FIRST_REIGN_YEAR LAST_REIGN_YEAR
  python3 -I fetch.py DATA search TYPE TERM [TERM ...]     TYPE: w (Sillok) | m (Ming Shilu)
  python3 -I fetch.py DATA article ID [ID ...]
"""
import datetime, gzip, hashlib, os, re, sys, threading, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = "https://sillok.history.go.kr"
UA = {"User-Agent": "Mozilla/5.0 (research; cryptics UE1453 documentary sweep)"}
LOCK = threading.Lock()


def fetch(data, rel, url, form=None, tries=4):
    path = os.path.join(data, "raw", rel + ".gz")
    if os.path.exists(path):
        with gzip.open(path, "rb") as f:
            return f.read().decode("utf-8")
    body = urllib.parse.urlencode(form).encode() if form else None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=body, headers=UA)
            b = urllib.request.urlopen(req, timeout=120).read()
            break
        except Exception as e:  # network errors: back off and retry
            if i == tries - 1:
                raise
            time.sleep(5 * (i + 1))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wb") as f:
        f.write(b)
    row = [os.path.relpath(path, data), "POST" if form else "GET", url,
           urllib.parse.urlencode(form) if form else "",
           datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           hashlib.sha256(b).hexdigest(), str(len(b))]
    with LOCK, open(os.path.join(data, "manifest.tsv"), "a", encoding="utf-8") as f:
        f.write("\t".join(row) + "\n")
    time.sleep(0.3)
    return b.decode("utf-8")


def months(data, codes):
    for c in codes:
        fetch(data, f"months/{c}.html", f"{BASE}/search/inspectionMonthList.do?id={c}")


def days(data, code, y0, y1):
    t = fetch(data, f"months/{code}.html", f"{BASE}/search/inspectionMonthList.do?id={code}")
    ids = sorted(set(re.findall(code + r"_(\d{6})(?!\d)", t)))
    want = [i for i in ids if i[0] == "1" and y0 <= int(i[1:3]) <= y1]
    with ThreadPoolExecutor(3) as ex:
        list(ex.map(lambda i: fetch(data, f"days/{code}_{i}.html",
                                    f"{BASE}/search/inspectionDayList.do?id={code}_{i}"), want))
    print(code, len(want), "month pages")


def search(data, typ, terms):
    def page(term, p):
        form = {"topSearchWord": term, "pageIndex": str(p), "initPageUnit": "0", "type": typ}
        if typ != "w":
            form["sillokType"] = "SMC"
        tag = term.encode("utf-8").hex()
        return fetch(data, f"search/{typ}_{tag}_p{p:04d}.html", f"{BASE}/search/searchResultList.do", form)

    key = {"w": "countW", "m": "countM", "k": "countK"}[typ]
    for term in terms:
        t = page(term, 1)
        n = int(re.search(rf'id="{key}" name="{key}" value="(\d+)"', t).group(1))
        npages = (n + 49) // 50
        with ThreadPoolExecutor(3) as ex:
            list(ex.map(lambda p: page(term, p), range(2, npages + 1)))
        print(typ, term, n, "hits", npages, "pages")


def article(data, ids):
    for i in ids:
        fetch(data, f"articles/{i}.html", f"{BASE}/id/{i}")


if __name__ == "__main__":
    data, cmd, args = sys.argv[1], sys.argv[2], sys.argv[3:]
    if cmd == "months":
        months(data, args)
    elif cmd == "days":
        days(data, args[0], int(args[1]), int(args[2]))
    elif cmd == "search":
        search(data, args[0], args[1:])
    elif cmd == "article":
        article(data, args)
    else:
        sys.exit(__doc__)

"""English corpus for the language factor: Gutenberg books by authors born 1860-1905, as 01-solver does
for es/it/pt (01-solver/fetch_corpus.py). Every 5th book is held out; plants come only from held-out books.

Writes out/raw_en/<id>.txt (downloads, untrusted; gitignored) and en_manifest.json (checked in).
Then builds out/lm_en_2.bin and out/lm_en_4.bin with 01-solver/lm.py's table() (same format, same
smoothing), and copies the Spanish tables from 01-solver/out so the solver here finds both.
Usage: python3 -I fetch_en.py
"""
import hashlib, json, os, re, shutil, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
S01 = os.path.join(HERE, "..", "01-solver")
sys.path.insert(0, S01)
from lm import table, strip_gutenberg  # noqa: E402  (01-solver, read only)

HDR = {"User-Agent": "cryptics-research/0.1"}
N_BOOKS = 15
ONES_EN = "ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE".split()


def normalise_en(t):
    t = re.sub(r"[0-9]+", lambda m: "".join(ONES_EN[int(c)] for c in m.group(0)), t)
    return re.sub(r"[^A-Z]", "", t.upper())


def get(url):
    for _ in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=HDR), timeout=120).read()
        except Exception as e:  # network hiccup: retry
            print("retry", url, e, file=sys.stderr)
            time.sleep(3)
    raise RuntimeError(url)


def books():
    url = "https://gutendex.com/books/?languages=en&author_year_start=1860&author_year_end=1905"
    out = []
    while url and len(out) < N_BOOKS:
        d = json.loads(get(url))
        for b in d["results"]:
            if b["languages"] != ["en"]:
                continue
            txt = [u for k, u in b["formats"].items() if k.startswith("text/plain")]
            if txt:
                out.append({"id": b["id"], "title": b["title"],
                            "authors": [(a["name"], a["birth_year"]) for a in b["authors"]], "url": txt[0]})
        url = d["next"]
    return out[:N_BOOKS]


def main():
    raw = os.path.join(HERE, "out", "raw_en")
    os.makedirs(raw, exist_ok=True)
    man = os.path.join(HERE, "en_manifest.json")
    bl = json.load(open(man)) if os.path.exists(man) else books()
    train, held = [], []
    for i, b in enumerate(bl):
        b["split"] = "heldout" if i % 5 == 4 else "train"
        p = os.path.join(raw, f"{b['id']}.txt")
        if not os.path.exists(p):
            open(p, "wb").write(get(b["url"]))
        t = normalise_en(strip_gutenberg(open(p, encoding="utf-8", errors="replace").read()))
        (held if b["split"] == "heldout" else train).append(t)
        print(b["id"], b["split"], b["title"][:60], b["authors"], len(t))
    json.dump(bl, open(man, "w"), indent=1, ensure_ascii=False)
    train = "".join(train)
    info = {"train_letters": len(train), "heldout_letters": sum(map(len, held))}
    for n in (2, 4):
        p = os.path.join(HERE, "out", f"lm_en_{n}.bin")
        table(train, n).tofile(open(p, "wb"))
        info[f"sha256_{n}"] = hashlib.sha256(open(p, "rb").read()).hexdigest()
    for n in (2, 4):
        shutil.copy(os.path.join(S01, "out", f"lm_es_{n}.bin"), os.path.join(HERE, "out", f"lm_es_{n}.bin"))
    json.dump(info, open(os.path.join(HERE, "lm_en_summary.json"), "w"), indent=1)
    print(info)


if __name__ == "__main__":
    main()

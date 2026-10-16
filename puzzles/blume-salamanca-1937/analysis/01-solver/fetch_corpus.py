"""Fetch period prose (authors born 1860-1905) from Project Gutenberg via the Gutendex API.

Writes out/raw_<lang>/<id>.txt and corpus_manifest.json (checked in: which books, which split).
Usage: python3 -I fetch_corpus.py es it pt
"""
import json, os, sys, urllib.request, time

HDR = {"User-Agent": "cryptics-research/0.1"}
MAX_BOOKS = {"es": 40, "it": 25, "pt": 25}

def get(url):
    for attempt in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=HDR), timeout=120).read()
        except Exception as e:
            print("retry", url, e, file=sys.stderr); time.sleep(3)
    raise RuntimeError(url)

def books(lang):
    url = f"https://gutendex.com/books/?languages={lang}&author_year_start=1860&author_year_end=1905"
    out = []
    while url and len(out) < MAX_BOOKS[lang]:
        d = json.loads(get(url))
        for b in d["results"]:
            if b["languages"] != [lang]:
                continue
            txt = [u for k, u in b["formats"].items() if k.startswith("text/plain")]
            if txt:
                out.append({"id": b["id"], "title": b["title"],
                            "authors": [(a["name"], a["birth_year"]) for a in b["authors"]],
                            "url": txt[0]})
        url = d["next"]
    return out[:MAX_BOOKS[lang]]

def main():
    manifest = json.load(open("corpus_manifest.json")) if os.path.exists("corpus_manifest.json") else {}
    for lang in sys.argv[1:]:
        os.makedirs(f"out/raw_{lang}", exist_ok=True)
        bl = books(lang)
        for i, b in enumerate(bl):
            # every 5th book is held out: the control plaintexts come from these, never the model
            b["split"] = "heldout" if i % 5 == 4 else "train"
            p = f"out/raw_{lang}/{b['id']}.txt"
            if not os.path.exists(p):
                open(p, "wb").write(get(b["url"]))
            print(lang, b["id"], b["split"], b["title"][:60], b["authors"])
        manifest[lang] = bl
    json.dump(manifest, open("corpus_manifest.json", "w"), indent=1, ensure_ascii=False)

main()

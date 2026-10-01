"""Fetch the period-French corpus for the n-gram model. Standard library only.

Sources (fixed 2026-10-01):
  - Brantôme, Vies des dames galantes, Project Gutenberg #39220 (period spelling).
  - Montaigne, Essais, Livres I–III, fr.wikisource.org chapter subpages, rendered
    (exemplaire de Bordeaux, 1595: u/v, i/j and long s as printed).
Writes out/corpus_raw.txt and prints its length and SHA-256. Gallica's full text was not
used: its texteBrut endpoint is behind a bot check.
"""
import hashlib, json, re, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent / "out"
H = {"User-Agent": "cryptics-research/0.1 (contact: repository owner)"}


def get(u):
    for attempt in range(6):
        try:
            time.sleep(1.5)
            return urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=120).read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
            time.sleep(30 * (attempt + 1))
    raise RuntimeError("rate limited: " + u)


def ws_api(**p):
    p["format"] = "json"
    return json.loads(get("https://fr.wikisource.org/w/api.php?" + urllib.parse.urlencode(p)))


def rendered_text(title):
    """Rendered chapter text; the pages transclude the 1595 edition from Page: scans."""
    h = ws_api(action="parse", page=title, prop="text", formatversion=2)["parse"]["text"]
    h = re.sub(r"<style.*?</style>", " ", h, flags=re.S)
    h = re.sub(r'<div class="[^"]*headertemplate.*?</div>\s*</div>', " ", h, flags=re.S)
    h = re.sub(r'<span[^>]*class="[^"]*pagenum[^"]*"[^>]*>.*?</span>', " ", h, flags=re.S)
    return re.sub(r"<[^>]+>", " ", h)


def main():
    OUT.mkdir(exist_ok=True)
    parts = []
    g = get("https://www.gutenberg.org/cache/epub/39220/pg39220.txt")
    s, e = g.find("*** START"), g.find("*** END")
    parts.append(g[g.find("\n", s):e])
    for livre in ["I", "II", "III"]:
        d = ws_api(action="query", list="allpages", apprefix=f"Essais/Livre {livre}/Chapitre ",
                   aplimit=200, apnamespace=0)
        for p in d["query"]["allpages"]:
            parts.append(rendered_text(p["title"]))
    text = "\n".join(parts)
    (OUT / "corpus_raw.txt").write_text(text)
    print(len(text), hashlib.sha256(text.encode()).hexdigest())


if __name__ == "__main__":
    main()

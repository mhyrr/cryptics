"""Counts for README from items.tsv, pairs.tsv, linecounts.tsv. Run: python3 count.py
Line estimates = sum over pages of linecount(view, side) * fraction of the page in that kind.
linecount.py undercounts dense cipher pages by roughly 10-15% (view 6: 32/33 vs about 37/40 by eye)."""
import csv
def rows(f): return list(csv.DictReader(open(f), delimiter="\t"))
lc = {int(r["view"]): (int(r["left"]), int(r["right"])) for r in rows("linecounts.tsv")}
def est(spec):
    t = 0.0
    for p in filter(None, spec.split(",")):
        p, _, fr = p.partition("*"); v, s = int(p[:-1]), p[-1]
        t += lc[v][0 if s == "L" else 1] * float(fr or 1)
    return round(t)
items = {r["id"]: r for r in rows("items.tsv")}; pairs = rows("pairs.tsv")
kinds = {}
for r in items.values(): kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
print("items by kind:", kinds)
c = [i for i, r in items.items() if r["kind"] == "letter with cipher"]
d = [i for i, r in items.items() if r["kind"] == "decipherment sheet"]
print(f"cipher letters {len(c)}, decipherment sheets {len(d)}, pairs {len(pairs)}")
print("\npair\tcipher_lines\tdecip_lines\tratio\tdocket\tadjacent\tconfidence")
for p in pairs:
    a, b = est(items[p["cipher_id"]]["cipher_pages"]), est(items[p["decip_id"]]["decip_pages"])
    print(f'{p["cipher_id"]}->{p["decip_id"]}\t{a}\t{b}\t{b/a:.2f}\t{p["docket_agree"]}\t{p["adjacent"]}\t{p["confidence"]}')
pc = {p["cipher_id"] for p in pairs}; pd = {p["decip_id"] for p in pairs}
print("\nunpaired cipher letters:")
for i in c:
    if i not in pc: r = items[i]; print(f'{i}\tviews {r["first_view"]}-{r["last_view"]}\tff. {r["folios"]}\t{r["docket_as_written"][:40]}\t~{est(r["cipher_pages"])} cipher lines')
print("unpaired decipherment sheets:", [i for i in d if i not in pd] or "none")
print("pairs with docket disagreement:", [p["cipher_id"] for p in pairs if p["docket_agree"] != "yes"] or "none")
print("non-adjacent pairs:", [p["cipher_id"] for p in pairs if p["adjacent"] != "yes"] or "none")

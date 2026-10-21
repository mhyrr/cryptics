"""Query PANGAEA's Elasticsearch-backed search API; print DOI + title per hit.

Usage: python3 -I pangaea_search.py "query" OUT.json
"""
import json, sys, urllib.parse, urllib.request
q, out = sys.argv[1], sys.argv[2]
u = "https://ws.pangaea.de/es/pangaea/panmd/_search?" + urllib.parse.urlencode({"q": q, "size": 50})
req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
d = urllib.request.urlopen(req, timeout=120).read()
open(out, "wb").write(d)
for h in json.loads(d)["hits"]["hits"]:
    s = h.get("_source", {})
    print(h["_id"], "|", (s.get("citation_title") or s.get("title") or str(s)[:150]))

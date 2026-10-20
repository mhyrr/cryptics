"""Fetch helper for 13-kamchatka-date. Usage: python3 -I fetch13.py <outfile> <url>
Prints sha256 and size. Standard library only."""
import hashlib, sys, urllib.request
out, url = sys.argv[1], sys.argv[2]
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (research; cryptics repo)'})
data = urllib.request.urlopen(req, timeout=120).read()
open(out, 'wb').write(data)
print(hashlib.sha256(data).hexdigest(), len(data), out, url)

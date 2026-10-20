"""Download a URL into data/ and print its sha256 and size.

Usage: python3 -I fetch14.py <out_dir> <name> <url>
Retries without TLS verification if verification fails, and says so.
"""
import hashlib, os, ssl, sys, urllib.request

def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (research; stdlib urllib)'})
    try:
        return urllib.request.urlopen(req, timeout=60).read(), 'verified'
    except urllib.error.URLError as e:
        if 'CERTIFICATE' not in str(e):
            raise
        ctx = ssl._create_unverified_context()
        return urllib.request.urlopen(req, timeout=60, context=ctx).read(), 'UNVERIFIED TLS'

out, name, url = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
try:
    data, tls = get(url)
except Exception as e:
    print('FAIL', name, url, e); sys.exit(1)
p = os.path.join(out, name)
open(p, 'wb').write(data)
print(name, len(data), hashlib.sha256(data).hexdigest(), tls)

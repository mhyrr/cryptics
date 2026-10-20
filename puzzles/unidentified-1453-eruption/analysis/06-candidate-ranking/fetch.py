"""Download the inputs for 06-candidate-ranking and print sha256 for each.

Usage: python3 -I fetch.py <out_dir>      (e.g. data)
Files are untrusted data. Nothing here executes them.
"""
import hashlib, os, sys, urllib.request

OUT = sys.argv[1]
FILES = [
    ('intcal20.14c', 'https://intcal.org/curves/intcal20.14c'),
    ('gvp_holocene_volcanoes.csv',
     'https://webservices.volcano.si.edu/geoserver/GVP-VOTW/ows?service=WFS&version=2.0.0'
     '&request=GetFeature&typeName=GVP-VOTW:Smithsonian_VOTW_Holocene_Volcanoes&outputFormat=csv'),
]
only = set(sys.argv[2:])
for name, url in FILES:
    if only and name not in only: continue
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=120).read()
    open(path, 'wb').write(data)
    print(hashlib.sha256(data).hexdigest(), len(data), name)
